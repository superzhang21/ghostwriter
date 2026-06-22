#!/usr/bin/env python3
"""
ghostwriter-sync.py — 影子作家角色库管理工具
从 GitHub 同步角色数据到本地 data/ 目录，列出/查看/生成 persona prompt。

用法:
  python3 ghostwriter-sync.py                    # 同步 + 列出角色
  python3 ghostwriter-sync.py --list             # 仅列出角色
  python3 ghostwriter-sync.py --list --no-sync   # 列出（跳过同步）
  python3 ghostwriter-sync.py --info 丁元英       # 查看角色详情
  python3 ghostwriter-sync.py --apply 丁元英      # 生成 persona prompt
  python3 ghostwriter-sync.py --apply 鲁迅 --json # JSON 格式输出
"""

import os
import sys
import json
import re
import subprocess
import argparse
from pathlib import Path

REPO_URL = "https://github.com/superzhang21/ghostwriter.git"
PROXY_URL = "https://ghfast.top/" + REPO_URL

# ── 路径策略 ──────────────────────────────────────────────
# 脚本始终在 skill/scripts/ 下，data 目录始终在 skill/data/ 下。
# 无论 skill 被 symlink 到哪里，data 都跟 skill 走。
SCRIPT_DIR = Path(__file__).resolve().parent          # skill/scripts/
SKILL_DIR = SCRIPT_DIR.parent                         # skill/
DATA_DIR = SKILL_DIR / "data"                         # skill/data/
CACHE_DIR = SKILL_DIR / ".cache"                      # skill/.cache/ (临时 git clone)


def sync_repo():
    """从 GitHub 拉取最新角色 JSON 到本地 data/"""
    # 已有本地数据时，尝试更新
    if DATA_DIR.exists() and list(DATA_DIR.glob("*.json")):
        if CACHE_DIR.exists():
            print("正在更新角色库...")
            try:
                subprocess.run(
                    ["git", "-C", str(CACHE_DIR), "pull", "--ff-only"],
                    capture_output=True, timeout=30,
                )
            except Exception:
                print("更新失败，使用本地缓存")
                return
            # 同步更新后的 JSON 到 data/
            _copy_json_files()
            return

    # 首次同步：clone 到 .cache/，提取 JSON 到 data/
    print("正在从 GitHub 同步角色库...")
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    for url in [PROXY_URL, REPO_URL]:
        try:
            subprocess.run(
                ["git", "clone", "--depth", "1", url, str(CACHE_DIR)],
                capture_output=True, timeout=60, check=True,
            )
            print("同步完成")
            _copy_json_files()
            return
        except Exception:
            continue
    print("错误: 无法连接 GitHub", file=sys.stderr)
    sys.exit(1)


def _copy_json_files():
    """从 .cache/ 的 data/ 目录复制 JSON 到 skill/data/"""
    src = CACHE_DIR / "data"
    if not src.exists():
        print(f"警告: 仓库中未找到 data/ 目录", file=sys.stderr)
        return
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    count = 0
    for f in src.glob("*.json"):
        dest = DATA_DIR / f.name
        content = f.read_text(encoding="utf-8")
        # 写入前先修复格式
        fixed = fix_json(content)
        dest.write_text(fixed, encoding="utf-8")
        count += 1
    print(f"已同步 {count} 个角色到 {DATA_DIR}")


def fix_json(raw: str) -> str:
    """修复常见 JSON 格式问题"""
    # 去掉 // 注释
    raw = re.sub(r"//[^\n]*", "", raw)
    # 去掉 /* */ 注释
    raw = re.sub(r"/\*.*?\*/", "", raw, flags=re.DOTALL)
    # 修复数组中未加引号的字符串: ["xxx" (yyy)] -> ["xxx yyy"]
    raw = re.sub(r'"([^"]+)"\s*\(([^)]+)\)', r'"\1 \2"', raw)
    # 去掉尾逗号
    raw = re.sub(r",(\s*[}\]])", r"\1", raw)
    return raw


def load_character(filepath: Path) -> dict | None:
    """安全加载角色 JSON"""
    try:
        with open(filepath, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, UnicodeDecodeError):
        try:
            with open(filepath, encoding="utf-8") as f:
                raw = f.read()
            return json.loads(fix_json(raw))
        except Exception:
            return None


def list_characters() -> list[dict]:
    """列出所有可用角色"""
    chars = []
    if not DATA_DIR.exists():
        return chars
    for f in sorted(DATA_DIR.glob("*.json")):
        d = load_character(f)
        if d:
            name = d.get("角色名称", f.stem)
            desc = d.get("角色描述", "")[:80]
            chars.append({"file": f.name, "name": name, "desc": desc})
    return chars


def get_character(query: str) -> dict | None:
    """按名称或文件名查找角色"""
    if not DATA_DIR.exists():
        return None
    for f in DATA_DIR.glob("*.json"):
        d = load_character(f)
        if d:
            char_name = d.get("角色名称", "")
            if query in char_name or query in f.name:
                return d
    return None


def build_persona_prompt(character: dict) -> str:
    """从角色数据构建 persona prompt 片段"""
    name = character.get("角色名称", "未知")
    desc = character.get("角色描述", "")
    psych = character.get("心理特征", {})
    lang = character.get("语言特征", {})
    relationships = character.get("重要人际关系", [])
    arc = character.get("角色弧线总结", "")

    lines = [f"## 角色设定：{name}\n"]
    lines.append(f"**角色描述**：{desc}\n")

    if psych:
        lines.append("### 心理特征")
        for k, v in psych.items():
            if isinstance(v, str):
                lines.append(f"- **{k}**：{v}")
            elif isinstance(v, dict):
                desc_text = v.get("描述", "")
                keywords = v.get("关键词", v.get("keywords", ""))
                if desc_text:
                    lines.append(f"- **{k}**：{desc_text}")
                if keywords:
                    lines.append(f"  关键词: {keywords}")
        lines.append("")

    if lang:
        lines.append("### 语言特征")
        for k, v in lang.items():
            if isinstance(v, str):
                lines.append(f"- **{k}**：{v}")
            elif isinstance(v, dict):
                desc_text = v.get("描述", "")
                if desc_text:
                    lines.append(f"- **{k}**：{desc_text}")
            elif isinstance(v, list):
                lines.append(f"- **{k}**：{'; '.join(str(x) for x in v[:5])}")
        lines.append("")

    if relationships:
        lines.append("### 重要人际关系")
        for r in relationships[:3]:
            if isinstance(r, dict):
                rname = r.get("相关角色名称", "")
                rdesc = r.get("关系动态摘要", "")[:100]
                lines.append(f"- **{rname}**：{rdesc}")
        lines.append("")

    if arc:
        lines.append(f"### 角色弧线\n{arc}\n")

    lines.append(f"\n---\n请以「{name}」的身份和风格回应。严格遵循上述心理特征和语言特征，保持角色一致性。")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Ghostwriter 影子作家角色库管理")
    parser.add_argument("--list", action="store_true", help="列出所有角色")
    parser.add_argument("--info", type=str, help="查看角色详情")
    parser.add_argument("--apply", type=str, help="生成角色 persona prompt")
    parser.add_argument("--no-sync", action="store_true", help="跳过 GitHub 同步")
    parser.add_argument("--json", action="store_true", help="JSON 格式输出")
    args = parser.parse_args()

    # 未指定任何操作时，默认 list
    if not args.list and not args.info and not args.apply:
        args.list = True

    if not args.no_sync:
        sync_repo()

    if not DATA_DIR.exists() or not list(DATA_DIR.glob("*.json")):
        print("错误: 角色库为空，请先同步（去掉 --no-sync）", file=sys.stderr)
        sys.exit(1)

    if args.list:
        chars = list_characters()
        if args.json:
            print(json.dumps(chars, ensure_ascii=False, indent=2))
        else:
            print(f"共 {len(chars)} 个角色:\n")
            for i, c in enumerate(chars, 1):
                print(f"  {i:2d}. {c['name']:<16} ({c['file']})")
                if c["desc"]:
                    print(f"      {c['desc']}")
            print(f"\n使用 --apply <角色名> 生成 persona prompt")
        return

    if args.info:
        char = get_character(args.info)
        if not char:
            print(f"未找到角色: {args.info}", file=sys.stderr)
            sys.exit(1)
        if args.json:
            print(json.dumps(char, ensure_ascii=False, indent=2))
        else:
            print(f"角色: {char.get('角色名称')}")
            print(f"描述: {char.get('角色描述')}")
            print(f"\n心理特征:")
            for k, v in char.get("心理特征", {}).items():
                if isinstance(v, dict):
                    print(f"  {k}: {v.get('描述', str(v))[:100]}")
                elif isinstance(v, str):
                    print(f"  {k}: {v[:100]}")
            print(f"\n语言特征:")
            for k, v in char.get("语言特征", {}).items():
                if isinstance(v, dict):
                    print(f"  {k}: {v.get('描述', str(v))[:100]}")
                elif isinstance(v, str):
                    print(f"  {k}: {v[:100]}")
        return

    if args.apply:
        char = get_character(args.apply)
        if not char:
            print(f"未找到角色: {args.apply}", file=sys.stderr)
            sys.exit(1)
        prompt = build_persona_prompt(char)
        if args.json:
            print(json.dumps({"character": char.get("角色名称"), "prompt": prompt}, ensure_ascii=False, indent=2))
        else:
            print(prompt)
        return


if __name__ == "__main__":
    main()
