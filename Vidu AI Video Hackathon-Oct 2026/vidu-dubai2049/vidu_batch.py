"""Vidu API batch runner for the Dubai 2049 hackathon.
Vidu API 批量生成脚本：提交 → 轮询 → 下载 → 抽首尾帧 → 记录（比赛过程证明）。

用法 / Usage:
    export VIDU_API_KEY=xxxx
    python vidu_batch.py shots.json            # 生成 shots.json 里所有未完成的镜头
    python vidu_batch.py shots.json S03 S07    # 只生成/重生成指定镜头
    python vidu_batch.py shots.json --dry-run  # 只打印请求，不花积分

shots.json 示例见 shots.example.json。每个镜头的 "mode" 可选:
    img2video        一张首帧图 → 视频
    reference2video  1-7 张参考图（人物/道具一致性）+ prompt
    start-end2video  首帧 + 尾帧 → 过渡视频（适合 2026→2049 转场）
    text2video       纯文本
"""
import csv
import json
import os
import subprocess
import sys
import time
from base64 import b64encode
from datetime import datetime, timezone
from pathlib import Path

import requests

BASE = "https://api.vidu.com/ent/v2"
KEY = os.environ.get("VIDU_API_KEY", "")
HEADERS = {"Authorization": f"Token {KEY}", "Content-Type": "application/json"}

ROOT = Path(__file__).parent
OUT = ROOT / "clips"
FRAMES = ROOT / "records" / "frames"
LOG = ROOT / "records" / "generation_log.csv"
STATE = ROOT / "records" / "state.json"
LOG_FIELDS = ["time_utc", "shot", "mode", "model", "duration", "resolution", "seed",
              "prompt", "images", "task_id", "state", "credits", "file", "first_frame", "last_frame"]

# 默认参数：省积分 / cost-saving defaults
DEFAULTS = {"model": "viduq2-turbo", "duration": 5, "resolution": "720p",
            "movement_amplitude": "auto", "audio": False, "bgm": False}


def image_ref(p):
    """本地路径转 base64 data URI，URL 原样返回。"""
    if p.startswith("http"):
        return p
    data = Path(ROOT / p).read_bytes()
    ext = Path(p).suffix.lstrip(".").lower().replace("jpg", "jpeg")
    return f"data:image/{ext};base64," + b64encode(data).decode()


def build_body(shot, defaults, load_images=True):
    body = {**DEFAULTS, **defaults, **{k: v for k, v in shot.items()
                                       if k not in ("id", "mode", "images", "note")}}
    if shot.get("images"):
        body["images"] = [image_ref(p) if load_images else p for p in shot["images"]]
    body.pop("off_peak", None)  # 错峰模式最长 48h 才出片，24h 比赛绝对不能用
    return body


def submit(mode, body):
    r = requests.post(f"{BASE}/{mode}", headers=HEADERS, json=body, timeout=120)
    r.raise_for_status()
    return r.json()


def poll(task_id, every=10, timeout=1800):
    t0 = time.time()
    while time.time() - t0 < timeout:
        r = requests.get(f"{BASE}/tasks/{task_id}/creations", headers=HEADERS, timeout=60)
        r.raise_for_status()
        j = r.json()
        if j.get("state") in ("success", "failed"):
            return j
        time.sleep(every)
    raise TimeoutError(task_id)


def download(url, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    with requests.get(url, stream=True, timeout=300) as r:
        r.raise_for_status()
        with open(dst, "wb") as f:
            for chunk in r.iter_content(1 << 20):
                f.write(chunk)


def extract_frames(video, stem):
    """首帧/尾帧截图，比赛要求的过程证明。"""
    FRAMES.mkdir(parents=True, exist_ok=True)
    first, last = FRAMES / f"{stem}_first.png", FRAMES / f"{stem}_last.png"
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(video),
                    "-frames:v", "1", str(first)], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-sseof", "-0.1", "-i", str(video),
                    "-frames:v", "1", "-update", "1", str(last)], check=True)
    return first, last


def log_row(row):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    new = not LOG.exists()
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=LOG_FIELDS)
        if new:
            w.writeheader()
        w.writerow(row)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    dry = "--dry-run" in sys.argv
    if not args:
        sys.exit(__doc__)
    plan = json.loads(Path(args[0]).read_text(encoding="utf-8"))
    only = set(args[1:])
    state = json.loads(STATE.read_text()) if STATE.exists() else {}
    if not KEY and not dry:
        sys.exit("请先 export VIDU_API_KEY=...")

    spent = sum(v.get("credits", 0) for k, v in state.items() if "_v" in k)
    budget = plan.get("budget", 5000)
    print(f"已用积分 credits spent so far: {spent}/{budget}")

    for shot in plan["shots"]:
        sid = shot["id"]
        if only and sid not in only:
            continue
        if not only and state.get(sid, {}).get("state") == "success":
            continue  # 已成功的不重复花钱
        mode = shot.get("mode", "img2video")
        body = build_body(shot, plan.get("defaults", {}), load_images=not dry)
        if dry:
            preview = {k: (v if k != "images" else [i[:60] for i in v]) for k, v in body.items()}
            print(f"[DRY] {sid} POST /{mode}\n{json.dumps(preview, ensure_ascii=False, indent=2)}")
            continue

        attempt = sum(1 for k in state if k.startswith(f"{sid}_v")) + 1
        stem = f"{sid}_v{attempt}"
        print(f"→ {stem} submitting ({mode}, {body['model']}, {body['duration']}s, {body['resolution']})")
        task = submit(mode, body)
        tid = task["task_id"]
        res = poll(tid)
        row = {"time_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
               "shot": stem, "mode": mode, "model": body["model"], "duration": body["duration"],
               "resolution": body["resolution"], "seed": res.get("seed", body.get("seed", "")),
               "prompt": body.get("prompt", ""), "images": ";".join(shot.get("images", [])),
               "task_id": tid, "state": res["state"], "credits": res.get("credits", task.get("credits", 0))}
        if res["state"] == "success":
            url = res["creations"][0]["url"]  # 链接 24h 失效，立刻下载
            video = OUT / f"{stem}.mp4"
            download(url, video)
            first, last = extract_frames(video, stem)
            row.update(file=str(video.relative_to(ROOT)), first_frame=str(first.relative_to(ROOT)),
                       last_frame=str(last.relative_to(ROOT)))
            print(f"  ✓ {video.name}  credits={row['credits']}  task_id={tid}")
        else:
            print(f"  ✗ failed: {res.get('err_code')}  task_id={tid}")
        log_row(row)
        state[stem] = {"state": res["state"], "task_id": tid, "credits": row["credits"]}
        state[sid] = state[stem]
        STATE.write_text(json.dumps(state, indent=2))
        spent = sum(v["credits"] for k, v in state.items() if "_v" in k)
        print(f"  累计积分 total spent: {spent}/{budget}")
        if spent > budget * 0.9:
            print("⚠️ 已用超过 90% 积分，停止批量生成。")
            break


if __name__ == "__main__":
    main()
