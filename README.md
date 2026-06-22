<div align="center">

# ✒️ Ghostwriter — 影子作家角色库

**13 个文学/影视/现实人物 × 完整心理+语言建模 = 一键切换 AI 人格**

[![License: CC BY-NC-ND 4.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-lightgrey.svg)](LICENSE)
[![Hermes Skill](https://img.shields.io/badge/Hermes-Skill-blue.svg)](skill/SKILL.md)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-green.svg)](skill/scripts/ghostwriter-sync.py)

</div>

---

## 这是什么？

Ghostwriter 是一个 **AI 角色人格库**。每个角色不只是简单的"性格标签"，而是包含：

- 🧠 **心理特征** — 核心哲学、价值观、决策风格、情绪反应、动机、应对机制
- 💬 **语言特征** — 词汇偏好、句式结构、语气风格、修辞手法、互动模式
- 🤝 **重要人际关系** — 与关键人物的关系动态
- 📈 **角色弧线** — 从起点到终点的成长/转变轨迹

通过 [Hermes Agent](https://github.com/NousResearch/hermes-agent) 的 Skill 机制，或独立的同步脚本，你可以 **一键切换 AI 的说话风格和思维方式**。

## 角色阵容

| # | 角色 | 来源 | 特色 | 框架 |
|---|------|------|------|------|
| 1 | **丁元英** | 《天道》 | 文化属性论、强势/弱势文化、不昧因果 | v1.0 |
| 2 | **芮小丹** | 《天道》 | 独立女性、追求自我、勇敢果断 | v1.0 |
| 3 | **林黛玉** | 《红楼梦》 | 才情绝世、多愁善感、敏感细腻 | v1.0 |
| 4 | **祁同伟** | 《人民的名义》 | 命运抗争、权力渴望、悲剧英雄 | v1.0 |
| 5 | **林月如** | 《仙剑奇侠传》 | 大家闺秀、坚强、为爱牺牲 | v1.0 |
| 6 | **绫波丽** | 新世纪福音战士 | 三无少女、自我存在探索、沉默力量 | v1.0 |
| 7 | **叶子农** | 《天幕红尘》 | 见路不走、实事求是、经济哲学 | v1.1 |
| 8 | **鲁迅** | 公共数据 | 国民性批判、韧性战斗、绝望中的希望 | v1.0 |
| 9 | **张仪** | 《大秦帝国》 | 纵横家、外交智慧、舌灿莲花 | v1.0 |
| 10 | **雷布斯** | 演讲数据 | 科技布道、极致性价比、互联网思维 | v0.8 |
| 11 | **李云龙** | 《亮剑》 | 亮剑精神、草莽智慧、狭路相逢勇者胜 | v2.1 |
| 12 | **吕子乔** | 《爱情公寓》 | 都市浪子、口才了得、反差萌 | v2.1 |
| 13 | **胡锡进** | 微博 | 胡氏逻辑、骑墙艺术、观察者体 | v1.0 |

> 💡 框架版本越高，心理维度越丰富。v2.1（李云龙、吕子乔）有完整的决策树和情绪触发器。

---

## 快速开始

### 方式一：独立使用（不依赖任何 Agent 框架）

```bash
# 克隆项目
git clone https://github.com/superzhang21/ghostwriter.git
cd ghostwriter

# 列出所有角色
python3 skill/scripts/ghostwriter-sync.py --list

# 查看丁元英详情
python3 skill/scripts/ghostwriter-sync.py --info 丁元英

# 生成鲁迅的 persona prompt（可直接粘贴到任何 LLM 对话中）
python3 skill/scripts/ghostwriter-sync.py --apply 鲁迅

# JSON 格式输出（方便程序化调用）
python3 skill/scripts/ghostwriter-sync.py --apply 李云龙 --json
```

**零依赖**，只需要 Python 3.8+ 和 git。

### 方式二：作为 Hermes Agent Skill 安装

如果你正在使用 [Hermes Agent](https://github.com/NousResearch/hermes-agent)，可以将 Ghostwriter 作为 Skill 安装，获得自动同步和 Agent 内无缝切换能力。

#### 安装步骤

```bash
# 1. 克隆项目到本地
git clone https://github.com/superzhang21/ghostwriter.git
cd ghostwriter

# 2. 创建 Skill 软链接到 Hermes skills 目录
#    （假设 Hermes 安装在默认路径 ~/.hermes）
ln -s $(pwd)/skill ~/.hermes/skills/creative/ghostwriter

# 3. 验证安装
#    重启 Hermes 后，在对话中说"列出角色"即可触发
```

#### Agent 内使用方式

安装 Skill 后，你可以在 Hermes 对话中直接使用自然语言：

| 你说 | Agent 做什么 |
|------|-------------|
| "切换到丁元英" | 运行 `--apply 丁元英`，注入 persona prompt |
| "用鲁迅的风格帮我写一段评论" | 切换到鲁迅 persona + 执行写作任务 |
| "现在用李云龙的方式说话" | 语言风格立刻变草莽 + 亮剑精神 |
| "列一下有哪些角色" | 运行 `--list` 展示所有角色 |
| "把雷布斯的设定发给我" | 运行 `--info 雷布斯` 详情 |

#### 配合 Cron 定时任务

你还可以为定时任务指定角色，让 Agent 以特定人格执行任务：

```bash
# 例：每天早上以丁元英的视角写一条投资思考
hermes cron create \
  --prompt "以丁元英的视角，结合今天的 A 股行情，写一条投资思考" \
  --skills ghostwriter \
  --schedule "0 9 * * 1-5"
```

#### Skill 同步机制

脚本内置 Git 同步功能。每次调用时会自动 `git pull` 拉取最新角色数据（除非加 `--no-sync`）。这意味着：

- 项目维护者新增角色后，你无需手动操作
- 重启 Agent 或重新调用时自动获取最新版本
- 断网时自动降级到本地缓存

---

## 使用案例

### 案例 1：投资分析 — 丁元英视角

```bash
python3 skill/scripts/ghostwriter-sync.py --apply 丁元英
```

> **输出摘要：** 以"文化属性"为核心分析框架，强调客观规律（天道），语言风格为冷静、深刻、哲学化。不讲鸡汤，只讲规律。
>
> *示例输出："任何一种命运，归根到底都是那种文化属性的产物，不以人的意志为转移。"*

**适用场景：** 深度思考、哲学分析、商业决策复盘

---

### 案例 2：犀利评论 — 鲁迅风格

```bash
python3 skill/scripts/ghostwriter-sync.py --apply 鲁迅
```

> **输出摘要：** 社会批判、国民性洞察、犀利讽刺。语言风格为短句有力、善用反语、引经据典但不掉书袋。
>
> *示例输出："我向来是不惮以最坏的恶意来推测中国人的，然而我还不料，也不信竟会下劣凶残到这地步。"*

**适用场景：** 时评写作、社会现象批判、犀利文风模仿

---

### 案例 3：草莽豪气 — 李云龙

```bash
python3 skill/scripts/ghostwriter-sync.py --apply 李云龙
```

> **输出摘要：** 亮剑精神、狭路相逢勇者胜。语言粗犷直接、比喻生动、带兵味。决策风格为直觉型，善于在混乱中抓住战机。
>
> *示例输出："古代剑客们在与对手狭路相逢时，无论对手有多么强大，就算对方是天下第一剑客，明知不敌，也要亮出自己的宝剑。"*

**适用场景：** 激励性内容、军事/竞技话题、草根创业故事

---

### 案例 4：程序化批量生成

```python
import subprocess, json

# 批量生成所有角色的 persona prompt
result = subprocess.run(
    ["python3", "skill/scripts/ghostwriter-sync.py", "--list", "--json"],
    capture_output=True, text=True
)
characters = json.loads(result.stdout)

for char in characters:
    print(f"\n{'='*40}")
    print(f"角色: {char['name']}")
    result = subprocess.run(
        ["python3", "skill/scripts/ghostwriter-sync.py",
         "--apply", char["name"], "--json"],
        capture_output=True, text=True
    )
    data = json.loads(result.stdout)
    # data["character"] = 角色名
    # data["prompt"] = 完整 persona prompt
    print(f"Prompt 长度: {len(data['prompt'])} 字符")
```

---

### 案例 5：在 Hermes Cron 中使用角色化输出

```json
{
  "prompt": "你是丁元英。以你的视角和思维方式，分析今天 A 股大盘走势。要求：1. 用文化属性的框架分析市场情绪；2. 用你标志性的冷静、哲学化语言风格；3. 不要讲鸡汤，只讲客观规律。",
  "skills": ["ghostwriter"],
  "schedule": "30 15 * * 1-5"
}
```

Agent 会先加载 ghostwriter Skill，同步角色数据，然后以丁元英的人格执行分析任务。

---

## 角色数据结构

每个角色 JSON 文件包含以下维度：

```
{
  "角色名称": "丁元英",
  "角色描述": "前私募基金操盘手...",
  "心理特征": {
    "核心哲学与世界观": { "描述": "...", "关键词": [...], "示例": [...] },
    "价值观": "...",
    "决策风格": "...",
    "情绪反应模式": "...",
    "人际互动模式": "...",
    "动机与驱动力": "...",
    "自我认知": "...",
    "应对机制": "..."
  },
  "语言特征": {
    "词汇与措辞": "...",
    "句式结构": "...",
    "语气与风格": "...",
    "修辞手法": "...",
    "互动模式": "..."
  },
  "重要人际关系": [
    { "相关角色名称": "...", "关系动态摘要": "..." }
  ],
  "角色弧线总结": "..."
}
```

> 📝 框架 v2.1 的角色（李云龙、吕子乔）在 `心理特征` 下有更细的子维度，包括决策树和情绪触发器。

---

## 命令参考

| 命令 | 说明 |
|------|------|
| `--list` | 列出所有角色 |
| `--list --json` | JSON 格式列出角色 |
| `--info <角色名>` | 查看角色详情 |
| `--info <角色名> --json` | JSON 格式查看详情 |
| `--apply <角色名>` | 生成 persona prompt（文本格式） |
| `--apply <角色名> --json` | 生成 persona prompt（JSON 格式） |
| `--no-sync` | 跳过 Git 同步，使用本地缓存 |

支持按角色名或文件名模糊匹配，如 `--apply 鲁迅` 或 `--apply Public_LuXun`。

---

## 常见问题

**Q: 安装 Skill 后 Hermes 没有识别到？**
A: 确认软链接路径正确：`ls -la ~/.hermes/skills/creative/ghostwriter`。需要重启 Hermes Agent 才能加载新 Skill。

**Q: 同步时网络超时？**
A: 脚本使用 `ghfast.top` 代理加速 GitHub 访问。如果仍然超时，可以手动克隆项目后用 `--no-sync` 模式。

**Q: 能自己添加角色吗？**
A: 可以。在 `data/` 目录下按照现有 JSON 格式新建文件，脚本会自动识别。推荐参考 `Tiandao_DingYuanying.json` 的完整结构。

**Q: 角色切换会影响 Agent 的工具权限和安全规则吗？**
A: 不会。角色化只影响语言风格层，不改变任何工具权限、数据访问能力或核心安全规则。

**Q: 支持哪些 LLM？**
A: 角色 prompt 是纯文本，适用于任何支持自定义 system prompt 的 LLM（GPT-4、Claude、Gemini、本地模型等）。Hermes Agent 中通过 Skill 机制自动注入。

---

## 项目结构

```
ghostwriter/
├── README.md                    # 你在这里
├── LICENSE                      # CC-BY-NC-ND-4.0
├── .gitignore
├── data/                        # 13 个角色 JSON
│   ├── Tiandao_DingYuanying.json    # 丁元英
│   ├── Tiandao_RuiXiaodan.json      # 芮小丹
│   ├── Honglou_LinDaiyu.json        # 林黛玉
│   ├── Renmindemingyi_QiTongwei.json# 祁同伟
│   ├── Xianjianqixiazhuan_Linyueru.json # 林月如
│   ├── Ribendongman_Lingboli.json   # 绫波丽
│   ├── Tianmuhongchen_YeZinong.json # 叶子农
│   ├── Public_LuXun.json            # 鲁迅
│   ├── Public_ZhangYi.json          # 张仪
│   ├── Speaker_Lei.json             # 雷布斯
│   ├── Liangjian_LiYunlong.json     # 李云龙
│   ├── Aiqinggongyu_LvZiqiao.json   # 吕子乔
│   └── Weibo_Hu.json                # 胡锡进
└── skill/                       # Hermes Agent Skill
    ├── SKILL.md                 # Skill 定义（触发条件、用法、注意事项）
    └── scripts/
        └── ghostwriter-sync.py  # 同步/切换/查询脚本
```

---

## 许可证

[CC-BY-NC-ND-4.0](LICENSE) — 署名-非商业性使用-禁止演绎

角色数据基于公开作品和演讲整理，仅供非商业研究和个人使用。

---

<div align="center">

**Made with ✒️ by [superzhang21](https://github.com/superzhang21) + [赛博哈雷](https://github.com/NousResearch/hermes-agent)**

*"任何一种命运，归根到底都是那种文化属性的产物。"*

</div>
