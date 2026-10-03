# 《This Way》Vidu 提示词手册 v1
> 用法：先生成并挑选满意的"首帧图"，再用图生视频（image-to-video）+ 运动提示词。
> 每条片段生成后：① 截图首帧/末帧 ② 记录任务 ID 到 `03_截图/`。

## 0. 一致性锚点模块（每条提示词按需复制对应模块，逐字不要改）

- HER27 = `a 27-year-old East Asian woman, shoulder-length black hair, sand-colored trench coat, worn brown leather satchel across her body, clear goggles pushed up on her forehead`
- HER50 = `a 50-year-old East Asian woman, same face aged gracefully, one streak of silver-gray hair at her temple, dark long wool coat, the same worn brown leather satchel`
- BOY7 = `a 7-year-old Arab mixed-race boy, calm dark eyes, red-and-white checkered shemagh headscarf with a black agal ring, beige thobe, a thin pale scar on the back of his right hand`
- MAN30 = `a 30-year-old Arab mixed-race man, light stubble, exhausted eyes, red-and-white checkered shemagh with black agal soaked dark red, wet white thobe, a thin pale scar on the back of his right hand`
- LETTER = `a weathered kraft-paper envelope, ornate Arabic-pattern crimson wax seal, circular postmark stamp reading "OASIS 2049"`
- STYLE = `cinematic, 35mm film still, photorealistic, shallow depth of field, warm golden highlights with teal shadows, fine film grain`

---

## C1 ｜ 信到（8s）清晨公寓
**首帧图**：`Close-up of LETTER sliding across a wooden floor from beneath an apartment door, soft dawn light; through the window behind, the silhouette of Burj Khalifa at sunrise; STYLE`
**运动提示词**：`The envelope slides slowly across the floor and stops; camera pushes in toward the "OASIS 2049" postmark until it fills the frame; dust motes drift in the dawn light; slow cinematic push-in.`

## C2 ｜ 读信（8s）
**首帧图**：`HER27 sitting by the window holding an open letter, her eyes wide with disbelief, morning light on her face; on the table lies LETTER; STYLE`
**运动提示词**：`Her eyes move down the letter line by line, she looks up slowly toward the darkening sky outside the window, wind begins to stir the curtains; subtle handheld camera, slow zoom on her face.`
**字幕（剪辑加）**："Within 24 hours, the storm will take you."

## C3 ｜ 沙暴迷失（8s）沙漠
**首帧图**：`HER27 alone in a raging desert sandstorm, goggles down, sand wall towering behind her, near-zero visibility, dunes of Dubai desert; she stumbles and falls to her knees; STYLE`
**运动提示词**：`She struggles forward through the whipping sand, loses balance and falls; her goggle lens cracks; the sand wall swallows the horizon; violent wind, shaking camera, low angle.`

## C4 ｜ 第一次救援（8s）★核心镜头
**首帧图**：`Extreme close-up: a small child's hand with a thin pale scar on its back gripping a woman's wrist in a sandstorm; behind, BOY7 shouts against the wind, his red-and-white checkered shemagh flying; STYLE`
**运动提示词**：`The boy pulls her up and leads her forward through the sand; his red checkered shemagh whips ahead in the yellow storm as she follows; camera follows behind them, sand swirling, a faint warm light appears ahead.`
**字幕（剪辑加）**："This way!" —— 手写体小字，画面下三分之一，暖白微光。

## C5 ｜ 消失人海（8s）
**首帧图**：`HER27 standing at the entrance of a glowing desert festival tent at dusk, catching her breath, turning back toward a bustling crowd; STYLE`
**运动提示词**：`She turns to thank the boy but he is gone; the camera pans across the crowd — many men in red-and-white checkered shemaghs, none of them him; her face falls; slow pan, crowd bokeh.`

## C6 ｜ 寻找蒙太奇（8s）
**首帧图**：`HER27 in a Dubai old-town souk alley (Al Fahidi style wind towers), holding the open letter, studying the hands of passers-by; golden afternoon light; STYLE`
**运动提示词**：`Montage feel: she walks through the souk, then a metro platform, then the Burj Khalifa observation deck, always comparing strangers' hands with her memory; quick elegant match cuts, time passing, day to night.`

## C7 ｜ 穿越迪拜之框（8s）★时间之门
**首帧图**：`HER27 walking toward the giant Dubai Frame at golden hour, seen from behind; the glass panels reflect the city skyline; STYLE`
**运动提示词**：`As she passes through the Frame, the skyline reflected in the glass morphs from 2026 Dubai into a futuristic 2049 Dubai; her reflection ages — a silver streak appears at her temple, coat turns dark; seamless transformation, glowing light wash.`
（备选降级方案：正常穿过 Frame，时空转换在 CapCut 里用叠化完成。）

## C8 ｜ 第二次救援（8s）★核心镜头
**首帧图**：`2049 Dubai, torrential rain, a flooded underpass; MAN30 wades waist-deep toward floating soaked blueprints; HER50 at the entrance reaching into the water, grabbing his wrist — the same thin pale scar visible; STYLE, cold blue palette with emergency orange light`
**运动提示词**：`She grips his scarred wrist and pulls; recognition flashes across her face; she shouts against the rain and leads him through the waist-deep water toward the stairway light; his soaked red shemagh streams behind; camera mirrors the 2026 sandstorm shot exactly — same framing, water instead of sand.`
**字幕（剪辑加）**："This way!" —— 同一手写体，但更大、带轻微回声混响；她的声音。

## C9 ｜ 台阶上的信（8s）
**首帧图**：`On the underpass steps at night, HER50 takes LETTER from her worn leather satchel and holds it out to MAN30, who sits wringing his soaked shemagh; rain softening to drizzle, warm street light; STYLE`
**运动提示词**：`He takes the yellowed envelope with trembling hands, reads the 2049 postmark, looks up at her in disbelief; she smiles, eyes wet; slow push-in on the letter between them.`
**字幕（剪辑加）**："I spent 23 years finding you. Your story isn't over."

## C10 ｜ 闭环·写信（8s）
**首帧图**：`Night, 2049 apartment, HER50 writing at a desk by lamplight, an Arabic-pattern wax seal and a stick of crimson sealing wax beside the letter; futuristic Dubai glowing outside the window; STYLE`
**运动提示词**：`She folds the letter, seals it with the crimson wax stamp; as the seal presses down, the image dissolves — the same envelope slides across a wooden floor from beneath a door in 2026 dawn light (match cut to C1); slow, quiet, conclusive.`

---

## 字幕规范
- 全片仅 4 处文字：信文三行（C2 打字机字体逐行浮现）+ 两处 "This way!" + C9 一句。
- "This way!"：手写体（推荐 Caveat / Ma Shan Zheng），白色描边暖光；第一次小而轻，第二次大而稳，配回声。
- 除字幕外不加旁白，用环境声 + 配乐。

## 生成与积分纪律
- 全部 Q2 + 720p；先定首帧图再动，首帧不满意不动视频。
- 预算：10 条正片 + 每条最多重试 2 次 ≈ 30 条；C4/C8 各预留 3 次额度；总控制在 40 条以内，留 10 条机动。
- 每次生成：改提示词只动一个变量；截图首末帧 + 任务 ID 存入 `03_截图/`。
