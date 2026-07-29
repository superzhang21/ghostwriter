---
name: ghostwriter
description: "Use when switching AI persona/language style. Syncs 13+ character profiles (Ding Yuanying, Lin Daiyu, Lu Xun, Li Yunlong, etc.) from GitHub, generates persona prompts with thinking patterns, rhetoric, and speech traits."
version: 1.1.0
author: superzhang21
license: CC-BY-NC-ND-4.0
metadata:
  hermes:
    tags: [persona, character, writing, style, roleplay, language]
    related_skills: [persona-protocols]
---

# Ghostwriter — 影子作家角色切换系统

## Overview

本项目包含 13+ 个角色的语言与思维特征数据，可通过配套脚本一键生成 persona prompt，
注入 AI 对话即可切换角色风格。支持写作模仿、角色扮演、风格迁移等场景。

**脚本完全独立，不依赖任何 Agent 框架。** 任何能执行 Python 脚本的环境都能用。

## When to Use

- 需要 AI 以特定人物风格说话/写作
- 角色扮演、文学创作、风格迁移
- 为 AI 助手注入不同的人格特征

## 快速开始

### 1. 安装

**独立使用（推荐，零依赖）：**
```bash
git clone https://github.com/superzhang21/ghostwriter.git
cd ghostwriter
python3 skill/scripts/ghostwriter-sync.py --list
```

**作为 Hermes Agent Skill：**
```bash
git clone https://github.com/superzhang21/ghostwriter.git
ln -s $(pwd)/skill ~/.hermes/skills/creative/ghostwriter
```

**其他 Agent / 通用：**
脚本只需 Python 3.8+，能执行 shell 命令的 Agent 都能调用。

### 2. 列出所有角色

```bash
python3 skill/scripts/ghostwriter-sync.py --list
```

### 3. 切换角色

```bash
# 生成丁元英的 persona prompt
python3 skill/scripts/ghostwriter-sync.py --apply 丁元英

# 生成鲁迅的 persona prompt
python3 skill/scripts/ghostwriter-sync.py --apply 鲁迅
```

输出的 prompt 片段可直接粘贴到系统提示词中，或通过 `--json` 参数程序化调用。

### 4. 查看角色详情

```bash
python3 skill/scripts/ghostwriter-sync.py --info 林黛玉
```

## 可用角色

| 角色 | 来源 | 文件 |
|------|------|------|
| 丁元英 | 《天道》 | Tiandao_DingYuanying.json |
| 芮小丹 | 《天道》 | Tiandao_RuiXiaodan.json |
| 林黛玉 | 《红楼梦》 | Honglou_LinDaiyu.json |
| 祁同伟 | 《人民的名义》 | Renmindemingyi_QiTongwei.json |
| 林月如 | 《仙剑奇侠传》 | Xianjianqixiazhuan_Linyueru.json |
| 绫波丽 | 新世纪福音战士 | Ribendongman_Lingboli.json |
| 叶子农 | 《天幕红尘》 | Tianmuhongchen_YeZinong.json |
| 鲁迅 | 公共数据 | Public_LuXun.json |
| 张仪 | 《大秦帝国》 | Public_ZhangYi.json |
| 雷布斯 | 演讲数据 | Speaker_Lei.json |
| 李云龙 | 《亮剑》 | Liangjian_LiYunlong.json |
| 吕子乔 | 《爱情公寓》 | Aiqinggongyu_LvZiqiao.json |
| 胡锡进 | 微博 | Weibo_Hu.json |

> 📌 角色库持续更新中。想加角色？去 [Issues](https://github.com/superzhang21/ghostwriter/issues) 提需求。

## 路径策略

脚本的 data 目录始终位于 **skill/data/** 下（与 scripts/ 平级），无论 skill 被安装到哪里：

```
skill/
├── SKILL.md
├── data/              ← 角色 JSON 同步到这里
│   ├── Tiandao_DingYuanying.json
│   └── ...
├── scripts/
│   └── ghostwriter-sync.py
└── .cache/            ← 临时 git clone 目录（自动管理）
```

首次运行时自动从 GitHub 克隆并提取 JSON；后续运行自动更新。不需要手动管理项目目录。

## 命令参考

| 命令 | 说明 |
|------|------|
| `--list` | 列出所有角色 |
| `--list --json` | JSON 格式列出角色 |
| `--info <角色名>` | 查看角色详情 |
| `--apply <角色名>` | 生成 persona prompt（文本格式） |
| `--apply <角色名> --json` | 生成 persona prompt（JSON 格式） |
| `--no-sync` | 跳过 GitHub 同步，使用本地缓存 |

支持按角色名或文件名模糊匹配。

## Pitfalls

- 角色切换仅影响语言风格和思维模式，不改变工具权限和安全边界
- 部分 JSON 格式有兼容性问题，脚本已内置修复逻辑
- 网络同步使用 `ghfast.top` 代理加速，代理失效时自动回退直连
- 框架版本差异：v2.1（李云龙、吕子乔）心理维度更丰富

## Verification

- [ ] `--list` 正确列出角色
- [ ] `--apply 丁元英` 输出完整 persona prompt
- [ ] `--apply 鲁迅 --json` 返回合法 JSON
