<div align="center">

# ✒️ Ghostwriter — 影子作家角色库

**想让 AI 像谁说话，就像谁说话。**

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)](skill/scripts/ghostwriter-sync.py)

</div>

---

## 这是什么？

一句话：**你跟 AI 说"用鲁迅的风格帮我写段评论"，AI 就真的会用鲁迅的风格写。**

Ghostwriter 是一个 AI 角色人格库。每个角色都经过深度建模——不只是"性格标签"，而是完整的说话方式、思维方式、用词习惯。你不需要写复杂的 prompt，只需要说一句"切换到 XX"，AI 就自动变成那个人。

**支持任何 AI 平台：** ChatGPT、Claude、Gemini、本地模型、Hermes Agent、任何支持自定义 prompt 的工具都行。

## 角色阵容

| 角色 | 来源 | 一句话特色 |
|------|------|-----------|
| 🧠 丁元英 | 《天道》 | 用"文化属性"解构一切，冷静到骨子里 |
| 🔥 李云龙 | 《亮剑》 | "狭路相逢勇者胜"，草莽英雄的直觉决策 |
| ✒️ 鲁迅 | 公共数据 | 短句如刀，讽刺入骨，绝望里找希望 |
| 💎 林黛玉 | 《红楼梦》 | 才情绝世，敏感细腻，字字珠玑 |
| 🎯 祁同伟 | 《人民的名义》 | 命运抗争者，权力渴望与悲剧宿命 |
| ⚡ 绫波丽 | 新世纪福音战士 | 沉默的力量，三无少女的存在探索 |
| 🌊 叶子农 | 《天幕红尘》 | "见路不走"，实事求是的经济哲学 |
| 🗡️ 张仪 | 《大秦帝国》 | 纵横家的三寸不烂之舌 |
| 💻 雷布斯 | 演讲数据 | 科技布道师，极致性价比代言人 |
| 🌸 林月如 | 《仙剑奇侠传》 | 大家闺秀外表下的刚烈与深情 |
| 🎭 吕子乔 | 《爱情公寓》 | 都市浪子的口才与反差萌 |
| 📢 胡锡进 | 微博 | 胡氏观察者体，永远在骑墙 |
| 🏃 芮小丹 | 《天道》 | 独立女性，勇敢追求自我 |

> 📌 **角色库持续更新中。** 想要某个角色？直接在 [Issues](https://github.com/superzhang21/ghostwriter/issues) 里提需求，我会持续开发。

---

## 快速开始

### 方式一：直接用脚本（零依赖）

```bash
# 克隆项目
git clone https://github.com/superzhang21/ghostwriter.git
cd ghostwriter

# 看看有哪些角色
python3 skill/scripts/ghostwriter-sync.py --list

# 让 AI 用鲁迅的风格说话，把输出的 prompt 粘贴到任何对话里
python3 skill/scripts/ghostwriter-sync.py --apply 鲁迅
```

就这样。脚本输出的 prompt 直接粘到 ChatGPT / Claude / 任何 AI 对话框里，就能切换风格。

### 方式二：作为 AI Agent Skill 安装

如果你在用 AI Agent（Hermes、Claude Code、Cursor、自建 Agent 等），可以把 Ghostwriter 装成 Skill，实现一键切换。

**Hermes Agent 安装：**

```bash
git clone https://github.com/superzhang21/ghostwriter.git
ln -s $(pwd)/skill ~/.hermes/skills/creative/ghostwriter
```

然后在对话里说"切换到丁元英"就行。

**其他 Agent / 通用安装：**

任何 Agent 只要能执行 shell 命令，就能调用这个 Skill。核心就一个 Python 脚本，没有特殊依赖。

---

## 使用场景

### 📝 写文案，不想千篇一律

你是个新媒体运营，每天要写不同风格的内容。用 Ghostwriter，一句话切换文风：

> **你：** "切换到鲁迅，帮我写一段关于内卷的评论"
>
> **AI 输出：** "我向来不惮以最坏的恶意来推测资本家的，然而我还不料，也不信竟会下劣凶残到这地步。所谓内卷，不过是少数人制定规则，多数人在规则里互相倾轧罢了。"

> **你：** "换成丁元英的风格重新说"
>
> **AI 输出：** "内卷的本质是文化属性的产物。当一个群体信奉弱势文化——期望救主、期望救恩——内卷就是必然结果。不以人的意志为转移。"

同一个话题，两个人说出来完全不一样。

### 🎮 做游戏 / 写小说，角色说话要对味

你在写一个武侠剧本，需要不同角色的对话风格：

> **你：** "以李云龙的风格说一句开战前的动员"
>
> **AI：** "兄弟们！对面人多又怎样？狭路相逢勇者胜！咱独立团从来就没有怂过！冲上去，干他娘的！"

> **你：** "以林黛玉的风格安慰一个失恋的朋友"
>
> **AI：** "你也不必太过伤怀。这世上的缘分，本就是聚散有时。他既不懂得珍惜，便是他的福分浅了。你只管保重自己，莫要为不值当的人落了泪。"

### 💼 商业分析，需要不同视角

同一份市场报告，让不同角色解读：

> **丁元英视角：** "这家公司的增长逻辑是强势文化的产物——它找到了规律，然后顺势而为。但要注意，任何增长都有天花板，关键看它的文化属性是否支撑可持续性。"

> **雷布斯视角：** "这个赛道我们非常看好。极致的产品 + 极致的性价比 = 用户口碑。只要把这一条做到极致，其他的都是战术问题。"

### 🌙 深夜睡不着，想跟有趣的人聊聊

> **你：** "切换到吕子乔，陪我聊会天"
>
> **AI（吕子乔）：** "哟，半夜睡不着？是不是又在想那个谁？来来来，子乔哥教你一招——感情这东西，你越在乎越没戏。放轻松，该来的总会来。话说你吃夜宵了没？"

### 📰 写时评，要犀利不要温和

> **你：** "用胡锡进的风格评论一下最近的热点"
>
> **AI：** "老胡认为，这件事需要从多个维度来看。一方面……另一方面……我们既不要盲目乐观，也不必过度悲观。相信国家的智慧，也相信市场的自我调节能力。最终，时间会给出答案。"

（对，就是那个味儿。）

---

## 命令参考

```bash
# 列出所有角色
python3 skill/scripts/ghostwriter-sync.py --list

# 查看角色详情
python3 skill/scripts/ghostwriter-sync.py --info 丁元英

# 生成 persona prompt（文本格式，直接粘贴用）
python3 skill/scripts/ghostwriter-sync.py --apply 鲁迅

# 生成 persona prompt（JSON 格式，程序化调用）
python3 skill/scripts/ghostwriter-sync.py --apply 李云龙 --json

# 跳过网络同步，用本地缓存
python3 skill/scripts/ghostwriter-sync.py --list --no-sync
```

---

## 常见问题

**Q: 这个只能给 Hermes Agent 用吗？**
A: 不是。脚本是纯 Python，输出的就是普通文本 prompt。你可以粘贴到 ChatGPT、Claude、Gemini、任何 AI 对话里。Agent Skill 安装只是其中一种使用方式。

**Q: 角色切换会影响 AI 的安全规则吗？**
A: 不会。角色化只影响说话风格，不改变任何安全边界。

**Q: 能自己加角色吗？**
A: 能。在 `data/` 目录下照着现有 JSON 格式新建文件就行。推荐参考 `Tiandao_DingYuanying.json`。

**Q: 我想要某个角色，但还没有？**
A: 去 [Issues](https://github.com/superzhang21/ghostwriter/issues) 提需求，说明你想要谁、什么场景用。角色库在持续开发中。

**Q: 同步时网络超时怎么办？**
A: 脚本默认用 `ghfast.top` 代理加速 GitHub 访问。如果还不行，手动克隆后加 `--no-sync` 用本地缓存。

---

## 项目结构

```
ghostwriter/
├── README.md                    # 你在这里
├── LICENSE                      # CC-BY-NC-ND-4.0
├── data/                        # 角色 JSON（持续增加中）
│   ├── Tiandao_DingYuanying.json
│   ├── Liangjian_LiYunlong.json
│   ├── Public_LuXun.json
│   ├── Honglou_LinDaiyu.json
│   └── ...（更多角色）
└── skill/                       # AI Agent Skill
    ├── SKILL.md                 # Skill 定义
    └── scripts/
        └── ghostwriter-sync.py  # 同步/切换/查询脚本
```

---

## 许可证

[CC-BY-NC-ND-4.0](LICENSE) — 署名-非商业性使用-禁止演绎

---

<div align="center">

**Made with ✒️ by [superzhang21](https://github.com/superzhang21) + [赛博哈雷](https://github.com/NousResearch/hermes-agent)**

</div>
