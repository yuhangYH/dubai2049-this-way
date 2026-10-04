# THIS WAY · 跟我来
**Vidu AI Video Hackathon · Dubai — "A Letter from the Future: Dubai 2049"**
Creator: Yuhang Guo · Runtime: 1 min 18 s (78 s) · 16:9 · 1080p
Process archive: https://github.com/yuhangYH/dubai2049-this-way

---

## English

### Logline
In 2026, a letter from her 50-year-old self warns Shiyu that a storm will take her within 24 hours, and tells her to trust a boy in a red shemagh. In 2049, she wades into a flood to find that boy again and bring him home.

### Synopsis
Dawn in Dubai. A kraft-paper envelope with a crimson wax seal lies on the floor, the Burj Khalifa behind it. The postmark reads **OASIS 2049**. Shiyu, a 27-year-old Chinese photographer, opens it and reads: *"Within 24 hours, the storm will take you."*

That afternoon a sandstorm swallows the desert and she falls. A small, scarred hand grabs her wrist. A 7-year-old boy in a red-and-white shemagh shouts **"This way!"** and leads her through the sand to the lights of a festival camp. When she turns to thank him he is gone, lost among hundreds of red shemaghs.

For years she searches the old souks of Dubai, letter in hand, checking the back of every stranger's hand. She walks through the Dubai Frame and the city on the other side becomes 2049.

In 2049 a super-storm floods the city. In a drowning underpass a 30-year-old man wades back toward his ruined blueprints. Shiyu, now 50, grabs his wrist and sees the same pale scar. This time she is the one who shouts **"This way!"** On the steps she hands him the letter: *"I spent 23 years finding you. Your story isn't over."*

That night she sits at her desk, writes the letter, and presses the wax seal. It is the same envelope that will reach her in 2026.

### How it answers the brief
| Brief question | Our answer |
|---|---|
| Who is the important person? | Zayd, the boy who saves her in 2026. As a 30-year-old storm-resistant architect, he is the one who needs saving in 2049. |
| Why did future-me send the letter? | To make sure the first rescue happens, so that the second one can happen. The letter closes its own loop when she writes it in 2049. |
| What happens when she finds him? | Two mirrored rescues: he pulls her out of the sand, and 23 years later she pulls him out of the water. Same scarred wrist, same two words. |
| A letter that drives the story | The letter predicts the storm, guides the 23-year search, is handed to Zayd as proof, and is written in the final shot. |
| Recognizable Dubai elements | Burj Khalifa (opening skyline and sandstorm horizon), desert dunes and a festival camp, an old-town souk, and the **Dubai Frame as the gate between 2026 and 2049**. Each one carries part of the plot. |

### Characters and visual anchors
- **Shiyu (时雨), 27 → 50.** A landscape photographer who came to Dubai to shoot sandstorms. Her name means "timely rain," and in 2049 she is exactly that for Zayd. She wears a sand-coloured trench coat in 2026 and a dark wool coat in 2049, with a silver streak at her temple and the same worn leather satchel holding the letter.
- **Zayd (زيد, "growth"), 7 → 30.** A child of the desert raised on the Bedouin rule that you never leave a lost traveller in the sand. The scar on his right hand came from a falcon's talon. He grows up to design buildings that can stand against storms, and when his project fails he loses his footing.
- **Continuity tokens.** These are repeated in every prompt: the red-and-white shemagh, the scar on the back of the right hand, the leather satchel, and the kraft envelope with crimson wax seal and OASIS 2049 postmark.

### Structure (10 Vidu clips)
| # | Scene | Vidu task ID |
|---|---|---|
| C1 | The letter arrives (Burj Khalifa at dawn) | 1004024402716659712 |
| C2 | Reading: "Within 24 hours, the storm will take you." | 1004029748256452608 |
| C3 | Lost in the sandstorm | 1004043007143448576 |
| C4 | First rescue: "This way!" | 1004054225803550720 |
| C5 | Vanished into the crowd | 1004041019341156352 |
| C6 | Searching the souk | 1004041933879812096 |
| C7 | Through the Dubai Frame, 2026 → 2049 | 1004044088292450304 |
| C8 | Second rescue in the flood: "This way!" | 1004061237606092800 |
| C9 | The letter on the steps | 1004048244084314112 |
| C10 | She writes the letter (loop closes) | 1004051275463004160 |

### Creative and technical approach
- **Mirror structure.** C4 and C8 are framed as a pair: sand becomes water, gold becomes blue, and the hand-on-wrist gesture is reversed. The emotional payoff comes from the image, not from narration.
- **Character consistency.** Four character reference images were generated first (Shiyu 27 and 50, Zayd 7 and 30). Each older version was generated from its younger reference so the faces stay continuous. Keyframes were built with reference images in Vidu Q2 Pro and then animated with image-to-video (viduq2-pro, 1080p, 8 s; C5 is 5 s).
- **Motion control.** Quiet scenes (C1, C2, C9, C10) use low motion, travel scenes (C6, C7) use medium, and the storm and rescue scenes (C3, C4, C8) use high.
- **Lesson learned.** Prompts that mentioned "montage" or several scenes produced collage-style keyframes. Every keyframe was rewritten as one moment in one place, and the montage feeling was built in the edit.
- **Restraint.** There is no voice-over. Only four lines of on-screen text appear (the letter, two "This way!", and the closing line). Vidu's built-in audio and BGM were switched off so that music and sound effects could be placed precisely in CapCut.
- **Editing.** Clips were assembled in CapCut with three transitions: a dissolve, a white flash for the 23-year jump, and a final dissolve. The final cut is 78 s.

### Process timeline (Dubai time, GST)
| Time | Milestone |
|---|---|
| 3 Oct, 12:36 | Concept drafts and story development (Word documents, timestamped) |
| 3 Oct, 13:13–15:12 | Four character reference images and the C1 keyframe generated in Vidu |
| 3 Oct, 16:41 | C2 keyframe locked |
| 3 Oct, 17:46 onward | Video generation C1 → C10 |
| 3 Oct, 21:26 | GitHub archive opened (story, prompt book, references, task log) |
| 4 Oct, 00:32 | All 10 clips archived (77.8 s of raw footage) |
| 4 Oct, 01:15 | Edit plan and sound design |
| 4 Oct, 07:19 | C10 revised and regenerated |
| 4 Oct, 08:42 | Final cut exported |

The repository contains the story bible, the prompt book (character, keyframe and motion prompts), all reference images and keyframes named with their task IDs, the task log, the sound design plan and the editing guide.

### Tools
Vidu (image generation, reference-to-image, image-to-video) · CapCut (editing, text, music and sound effects) · Claude (brainstorming, script and prompt development) · GitHub (process archive)

---

## 中文

### 一句话梗概
2026 年，50 岁的自己寄来一封信，警告时雨："24 小时内，风暴会带走你。"信里让她相信那个戴红格纹头巾的男孩。2049 年，她走进洪水，把这个男孩找了回来，也把他带回了家。

### 故事
迪拜清晨，一封牛皮纸信封落在地板上，窗外是哈利法塔，邮戳上写着 **OASIS 2049**。27 岁的中国摄影师时雨拆开信，读到："Within 24 hours, the storm will take you."

当天下午，沙暴吞没了沙漠，她跌倒在沙里。一只手背有疤的小手抓住了她的手腕。7 岁的男孩 Zayd 戴着红白格纹头巾，喊了一声 **"This way!"**，带她穿过风沙，走到节日营地的灯光前。等她回头想道谢，男孩已经消失在一片红格纹头巾里。

此后很多年，她拿着那封信走遍迪拜的老城市集，看过每一个陌生人的手背。她穿过迪拜之框，门另一边的城市变成了 2049 年。

2049 年，超级风暴让城市内涝。在积水的地下通道里，30 岁的 Zayd 转身走回深水，去捞他被泡烂的图纸。50 岁的时雨抓住他的手腕，看到了同一道疤。这一次，换她喊出 **"This way!"** 台阶上，她把那封信递给他："I spent 23 years finding you. Your story isn't over."

当晚，她在书桌前写下这封信，盖上火漆印。正是这个信封，会在 2026 年送到她手里。

### 如何回应命题
- **重要的人是谁**：2026 年救了她的男孩 Zayd。30 岁时他是防风暴建筑设计师，也是 2049 年需要被救的人。
- **未来的我为何寄信**：为了让第一次救援发生，第二次救援才可能发生。信在 2049 年由她亲手写成，形成闭环。
- **找到后发生什么**：两场镜像救援。他把她从沙里拉出来，23 年后她把他从水里拉出来。同一个有疤的手腕，同一句话。
- **信推动剧情**：信预言了沙暴，指引了 23 年的寻找，在台阶上交到 Zayd 手里作为证明，最后一镜里由她亲手写下。
- **迪拜元素**：哈利法塔（开场天际线和沙暴地平线）、沙丘与节日营地、老城市集，以及作为 2026 与 2049 之间时间之门的**迪拜之框**。每个元素都承担了一部分叙事。

### 人物与一致性
- **时雨**（27 → 50 岁）：风光摄影师，来迪拜拍沙暴。名字取"及时雨"之意，2049 年她正是 Zayd 的那场及时雨。2026 年穿沙色风衣，2049 年换深色长外套、鬓角一缕灰白，始终背着装信的旧皮挎包。
- **Zayd**（7 → 30 岁）：阿拉伯语意为"成长"。他是沙漠的孩子，从小被教导贝都因人的规矩：在沙漠里遇到迷路的人，一定要带回家。右手背的疤是驯猎隼时被隼爪划伤的。长大后他设计能抵御风暴的建筑，项目失败让他一度走向绝望。
- **一致性信物**：红白格纹头巾、右手背的疤、旧皮挎包、牛皮纸信封（火漆印和 OASIS 2049 邮戳），每条提示词都重复描述。

### 创作与技术方法
- **镜像结构**：C4 与 C8 构图对称，沙变成水，金色变成蓝色，抓手腕的动作反转。情绪靠画面传达，不靠旁白。
- **角色一致性**：先生成 4 张角色基准图（时雨 27/50 岁、Zayd 7/30 岁），年长版都以年少版为参考生成，保证面孔延续。首帧用 Vidu Q2 Pro 参考生图，再用图生视频制作（viduq2-pro、1080p、8 秒，C5 为 5 秒）。
- **运动控制**：静场戏（C1、C2、C9、C10）用 low，走戏（C6、C7）用 medium，风暴和救援（C3、C4、C8）用 high。
- **踩坑经验**：首帧提示词里写了 montage 或多个场景，会被生成成九宫格拼贴图。所以每个首帧都改写成"一个场景、一个时刻"，蒙太奇感交给剪辑完成。
- **克制**：全片没有旁白，只有 4 处字幕（信文、两次 "This way!"、结尾台词）。关闭了 Vidu 自带的音频和 BGM，配乐和音效都在 CapCut 里精确对位。
- **剪辑**：在 CapCut 完成，只用了 3 个转场：叠化、表示 23 年跨越的白闪、结尾叠化。成片 78 秒。

### 创作时间线与过程证据
2026-10-03 12:36 开始写构思草稿，13:13 起生成角色图和首帧，17:46 开始生成视频，21:26 建立 GitHub 存档。10-04 00:32 十条片段全部归档，07:19 修改并重新生成 C10，08:42 导出成片。全过程都在 24 小时比赛窗口内。

所有提示词、角色基准图、首帧截图（文件名带任务 ID）、任务台账、声音设计和剪辑方案都在 GitHub 仓库：https://github.com/yuhangYH/dubai2049-this-way
