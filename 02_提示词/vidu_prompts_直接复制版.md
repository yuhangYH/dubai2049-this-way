# 《This Way》Vidu 提示词 · 直接复制版
> 使用方法：Image Generation 页面 → 按"参考图"栏顺序上传图片 → 粘贴提示词 → 模型选 Q2 Pro、比例 16:9、1K → 提交
> ⚠️ 参考图上传顺序必须和文中标注一致（提示词里的 reference image 1/2/3 按上传顺序对应）
> ✅ = 已生成定稿，勿重复生成

参考图文件位置（03_截图/ 文件夹内）：
- 【时雨27】角色图_时雨27_task1003895224356851712.png
- 【时雨50】角色图_时雨50_task1003916013223305216.png
- 【Zayd7】角色图_Zayd7_task1003896164971470848.png
- 【Zayd30】角色图_Zayd30_task1003919063249862656.png
- 【信封】C1首帧_信到_task1003919887652892672.jpg

---

## ✅ C1 信到（已完成 task 1003919887652892672）
## ✅ C2 读信（已完成 task 1003947587541159936）

---

## C3 ｜ 沙暴迷失
**参考图**：① 时雨27
**首帧提示词**：
```
The 27-year-old East Asian woman from the reference image, shoulder-length black hair, sand-colored trench coat, worn brown leather satchel across her body, clear goggles pulled down over her eyes, alone in a raging desert sandstorm, a towering sand wall behind her, near-zero visibility, dunes of the Dubai desert; she stumbles and falls to her knees; cinematic, 35mm film still, photorealistic, shallow depth of field, warm golden highlights with teal shadows, fine film grain
```
**运动提示词**：
```
She struggles forward through the whipping sand, loses balance and falls; her goggle lens cracks; the sand wall swallows the horizon; violent wind, shaking camera, low angle.
```

## C4 ｜ 第一次救援 ★核心镜头
**参考图**：① Zayd7 ② 时雨27
**首帧提示词**：
```
Extreme close-up in a sandstorm: the small hand of the 7-year-old Arab boy from reference image 1, a thin pale scar on the back of his hand, gripping the wrist of the woman from reference image 2; behind them the boy shouts against the wind, his red-and-white checkered shemagh with black agal flying, beige thobe covered in sand; cinematic, 35mm film still, photorealistic, shallow depth of field, warm golden highlights with teal shadows, fine film grain
```
**运动提示词**：
```
The boy pulls her up and leads her forward through the sand; his red checkered shemagh whips ahead in the yellow storm as she follows; camera follows behind them, sand swirling, a faint warm light appears ahead.
```

## C5 ｜ 消失人海
**参考图**：① 时雨27
**首帧提示词**：
```
The 27-year-old East Asian woman from the reference image, shoulder-length black hair, sand-colored trench coat, worn brown leather satchel, standing at the entrance of a glowing desert festival tent at dusk, catching her breath, turning back toward a bustling crowd; several men in the crowd wear red-and-white checkered shemaghs, none of them a child; cinematic, 35mm film still, photorealistic, shallow depth of field, warm golden highlights with teal shadows, fine film grain
```
**运动提示词**：
```
She turns to thank the boy but he is gone; the camera pans across the crowd — many men in red-and-white checkered shemaghs, none of them him; her face falls; slow pan, crowd bokeh.
```

## C6 ｜ 寻找（单场景版，替代原蒙太奇方案）
**⚠️ 翻车教训**：首帧提示词里禁止出现 montage / match cuts / day to night / 多场景并列——会被生成成九宫格拼贴图。多场景感只能放运动提示词或靠剪辑。
**参考图**：① 时雨27 ② 信封
**首帧提示词**：
```
The 27-year-old East Asian woman from reference image 1, shoulder-length black hair, sand-colored trench coat, worn brown leather satchel, standing in a narrow Dubai old-town souk alley with Al Fahidi-style wind towers, holding the open weathered kraft-paper letter from reference image 2; in the soft-focus foreground, the bare hand of a passing man in a red-and-white checkered shemagh; she stares at his hand intently, comparing it with her memory; golden afternoon light filtering through wooden lattice, dust in the air; one single continuous scene, single frame composition; cinematic, 35mm film still, photorealistic, shallow depth of field, warm golden highlights with teal shadows, fine film grain
```
**运动提示词**：
```
She raises the letter slightly and studies the passing man's hand, then lowers it with quiet disappointment and walks deeper into the souk; the camera follows her in one continuous smooth tracking shot; golden light flickers across her face through the lattice as she moves; crowds pass in soft bokeh; single continuous shot, no cuts.
```
（可选加拍：若积分充裕想还原"走遍迪拜"蒙太奇，可单独再出 2 张单场景首帧——地铁站台 / 哈利法塔观景台夜景，各 4s，CapCut 快切；非必需）

## C7 ｜ 穿越迪拜之框 ★时间之门
**参考图**：① 时雨27
**首帧提示词**：
```
The 27-year-old East Asian woman from the reference image, shoulder-length black hair, sand-colored trench coat, worn brown leather satchel, walking toward the giant Dubai Frame at golden hour, seen from behind; the glass panels of the Frame reflect the city skyline; cinematic, 35mm film still, photorealistic, shallow depth of field, warm golden highlights with teal shadows, fine film grain
```
**运动提示词**：
```
As she passes through the Frame, the skyline reflected in the glass morphs from 2026 Dubai into a futuristic 2049 Dubai; her reflection ages — a silver streak appears at her temple, her coat turns dark; seamless transformation, glowing light wash.
```
（降级方案：若变身效果翻车，只生成"正常穿过 Frame"，时空转换在 CapCut 里叠化完成）

## C8 ｜ 第二次救援 ★核心镜头
**参考图**：① Zayd30 ② 时雨50
**首帧提示词**：
```
2049 Dubai, torrential rain, a flooded underpass; the 30-year-old Arab man from reference image 1, light stubble, exhausted eyes, red-and-white checkered shemagh soaked dark red, wet white thobe, wades waist-deep toward floating soaked blueprints; the 50-year-old East Asian woman from reference image 2, one streak of silver-gray hair at her temple, dark long wool coat, worn brown leather satchel, stands at the entrance reaching into the water and grabbing his wrist — a thin pale scar visible on the back of his right hand; cinematic, 35mm film still, photorealistic, shallow depth of field, cold blue palette with emergency orange light, fine film grain
```
**运动提示词**：
```
She grips his scarred wrist and pulls; recognition flashes across her face; she shouts against the rain and leads him through the waist-deep water toward the stairway light; his soaked red shemagh streams behind; camera mirrors a desert sandstorm rescue — same framing, water instead of sand.
```

## C9 ｜ 台阶上的信
**参考图**：① 时雨50 ② Zayd30 ③ 信封
**首帧提示词**：
```
On flooded underpass steps at night, the 50-year-old East Asian woman from reference image 1, silver-gray streak at her temple, dark long wool coat, takes the weathered kraft-paper envelope with crimson wax seal from reference image 3 out of her worn leather satchel and holds it out; the 30-year-old Arab man from reference image 2 sits on the steps wringing his soaked red checkered shemagh; rain softening to drizzle, warm street light; cinematic, 35mm film still, photorealistic, shallow depth of field, warm golden highlights with teal shadows, fine film grain
```
**运动提示词**：
```
He takes the yellowed envelope with trembling hands, reads the 2049 postmark, looks up at her in disbelief; she smiles, eyes wet; slow push-in on the letter between them.
```

## C10 ｜ 闭环·写信（v2 单场景版）
**⚠️ 同 C6 教训**：首帧提示词只写"一个时刻"，不要罗列写信/熔蜡/盖章/门下等多个动作（会被生成成拼贴）。已裁切拼贴图得到 13 张备用帧（~/Downloads/C10_裁切/），但正式首帧用下面这条重新生成。
**参考图**：① 时雨50 ② 信封
**首帧提示词**：
```
Night in a 2049 Dubai apartment, the 50-year-old East Asian woman from reference image 1, one streak of silver-gray hair at her temple, dark long wool coat, sits at a wooden desk writing a letter by the warm light of a brass desk lamp; on the desk beside her hand, the weathered kraft-paper envelope from reference image 2, an ornate Arabic-pattern wax seal stamp and a stick of crimson sealing wax; futuristic Dubai skyline glowing through the window behind her; one single continuous scene, single frame composition, no collage, no split screen; cinematic, 35mm film still, photorealistic, shallow depth of field, warm golden highlights with teal shadows, fine film grain
```
**运动提示词**：
```
She finishes writing, folds the letter slowly, melts the crimson wax and presses the seal; as the seal comes down, the warm lamplight flickers; slow quiet push-in toward the wax seal; single continuous shot, no cuts; conclusive, gentle mood.
```
（与 C1 的闭环切换在 CapCut 里做 match cut：本片段结尾的火漆印特写 → C1 的信封滑入门缝；备选素材可用 C10_裁切/ 里的 C10-2、C10-13 门下信封帧）

---

## 视频生成设置（Image-to-Video 页面）
- 上传对应首帧图 → 粘贴运动提示词 → 模型 viduq2-pro → 720p → 时长 8s
- 每条生成后：截图首帧+末帧、记任务 ID 到 03_截图/任务记录.md

## 字幕（CapCut 里加，共 4 处）
- C2: "Within 24 hours, the storm will take you."（打字机字体逐行浮现）
- C4: "This way!"（手写体小字，画面下三分之一，暖白微光）
- C8: "This way!"（同一手写体，更大，带回声）
- C9: "I spent 23 years finding you. Your story isn't over."
