#!/usr/bin/env python3
"""Validate the bilingual catalog and deterministically render its Markdown pages."""

import argparse
from collections import Counter
from datetime import date, datetime
import html
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ("en", "zh-CN")
INITIAL_WINDOW = ("2026-10-07", "2026-10-13")
CATEGORIES = {
    "desktop": ("Desktop and productivity", "桌面与效率工具"),
    "media": ("Audio, video and creative tools", "音视频与创作工具"),
    "web": ("Web products and services", "网站产品与服务"),
    "devices": ("Devices, drivers and protocols", "设备、驱动与协议"),
    "games": ("Games and game tooling", "游戏与游戏工具"),
    "limited": ("Limited REA involvement", "REA 有限参与"),
}
STAGES = {
    "implementation": ("Implementation", "已有实现"),
    "prototype": ("Prototype", "原型"),
    "partial": ("Partial reconstruction", "局部重建"),
    "compatibility": ("Compatibility tool", "兼容工具"),
    "research": ("Research", "研究"),
}
EVIDENCE = {
    "documented": ("Documented", "具体记录"),
    "attributed": ("Author attribution", "作者声明"),
    "limited": ("Limited", "有限参与"),
}
FIELDS = {
    "id", "name", "target", "target_description", "repo", "category", "stage", "evidence",
    "evidence_urls", "summary", "rea", "limitations", "created_at", "reviewed_at",
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_catalog():
    entries = []
    ids, repositories = set(), set()
    for path in sorted((ROOT / "data").glob("*.json")):
        records = json.loads(path.read_text(encoding="utf-8"))
        require(isinstance(records, list), f"{path.name}: expected an array")
        for item in records:
            require(isinstance(item, dict), f"{path.name}: expected an object")
            label = f"{path.name}:{item.get('id', '?')}"
            require(set(item) == FIELDS, f"{label}: missing or unexpected fields")
            require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", item["id"]), f"{label}: invalid id")
            require(item["id"] not in ids, f"{label}: duplicate id")
            ids.add(item["id"])
            require(re.fullmatch(r"https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", item["repo"]), f"{label}: invalid repository URL")
            repository = item["repo"].casefold()
            require(repository not in repositories, f"{label}: duplicate repository")
            repositories.add(repository)
            for field in ("name", "target"):
                require(isinstance(item[field], str) and item[field].strip(), f"{label}: empty {field}")
            for field, values in (("category", CATEGORIES), ("stage", STAGES), ("evidence", EVIDENCE)):
                require(item[field] in values, f"{label}: invalid {field}")
            require((item["category"] == "limited") == (item["evidence"] == "limited"), f"{label}: limited evidence must use the limited category")
            for field in ("target_description", "summary", "rea", "limitations"):
                require(isinstance(item[field], dict) and set(item[field]) == set(LANGUAGES), f"{label}: {field} needs both languages")
                for language, text in item[field].items():
                    require(isinstance(text, str) and text.strip() and "\n" not in text, f"{label}: invalid {field}.{language}")
            links = item["evidence_urls"]
            require(isinstance(links, list) and 1 <= len(links) <= 2, f"{label}: provide one or two evidence URLs")
            require(len(set(links)) == len(links), f"{label}: duplicate evidence URL")
            for link in links:
                parsed = urlparse(link)
                require(parsed.scheme == "https" and parsed.netloc and not parsed.username and not parsed.password, f"{label}: invalid evidence URL")
            require(re.fullmatch(r"\d{4}-\d{2}-\d{2}", item["reviewed_at"]), f"{label}: expected YYYY-MM-DD review date")
            reviewed = date.fromisoformat(item["reviewed_at"])
            if item["created_at"] is not None:
                require(re.fullmatch(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z", item["created_at"]), f"{label}: expected UTC timestamp")
                created = datetime.fromisoformat(item["created_at"].replace("Z", "+00:00"))
                require(created.date() <= reviewed, f"{label}: creation is after review")
            entries.append(item)
    require(entries, "No catalog entries found")
    return sorted(entries, key=lambda entry: (entry["name"].casefold(), entry["id"]))


def clean(text):
    return html.escape(text, quote=False).replace("|", "&#124;").replace("[", "&#91;").replace("]", "&#93;")


def in_initial_window(item):
    return item["created_at"] is not None and INITIAL_WINDOW[0] <= item["created_at"][:10] <= INITIAL_WINDOW[1]


def table(entries, language):
    n = LANGUAGES.index(language)
    headings = ("Project / what the original software does", "What this project delivers", "REA evidence", "Created · UTC") if n == 0 else ("项目／原软件做什么", "这个项目做到了什么", "REA 证据", "建库日 · UTC")
    lines = ["| " + " | ".join(headings) + " |", "| --- | --- | --- | --- |"]
    for item in entries:
        target_label = "Original: " if n == 0 else "原软件："
        name = f"[{clean(item['name'])}]({item['repo']})<br>**{target_label}{clean(item['target'])}**<br>{clean(item['target_description'][language])}"
        scope = f"**{STAGES[item['stage']][n]}** — {clean(item['summary'][language])}<br>{clean(item['limitations'][language])}"
        source_label = "source" if n == 0 else "来源"
        sources = " · ".join(f"[{source_label} {i}]({url})" for i, url in enumerate(item["evidence_urls"], 1))
        evidence = f"**{EVIDENCE[item['evidence']][n]}** — {clean(item['rea'][language])} {sources}"
        created = item["created_at"]
        stamp = f"[{created[:10]}](https://api.github.com/repos/{item['repo'].removeprefix('https://github.com/')})" if created else ("Not checked" if n == 0 else "未核对")
        lines.append(f"| {name} | {scope} | {evidence} | {stamp} |")
    return "\n".join(lines)


def homepage(entries, language):
    n = LANGUAGES.index(language)
    counts = Counter(item["category"] for item in entries)
    evidence_counts = Counter(item["evidence"] for item in entries)
    reviewed = max(item["reviewed_at"] for item in entries)
    recent = sum(in_initial_window(item) for item in entries)
    unknown = sum(item["created_at"] is None for item in entries)
    lines = ["# Awesome REA", "", "<!-- Generated by scripts/build_catalog.py. Edit data/*.json, then rebuild. -->", "", "[English](README.md) · [简体中文](README.zh-CN.md)", ""]
    if n == 0:
        lines += [
            "A curated collection of software reconstructions, compatibility tools and research built with [REA — Reverse Engineer Anything](https://github.com/morluto/rea), with links to the actual implementations and evidence.", "",
            "The initial collection focuses on closed-source targets discovered during October 2026. Each entry starts with a plain-language introduction to what the original software does, then explains what the project delivers, what REA contributed, and what remains incomplete. REA connects coding agents to analysis tools; using it does not mean the original source code was recovered.", "",
            f"**{len(entries)} projects · {evidence_counts['documented']} with specific analysis records · {evidence_counts['attributed']} with author attribution · {evidence_counts['limited']} with limited REA involvement.** Last reviewed: **{reviewed}**.", "",
            f"**Initial review window, October 7–13, 2026:** {recent} repositories were created during this window. Older repositories are retained with their actual creation dates; {unknown} creation dates remain unchecked. Dates link to GitHub metadata and are UTC repository-creation dates, not release dates or proof of when a private repository became public.", "",
            "## Start here", "",
            "- [REA repository and documentation](https://github.com/morluto/rea)",
            "- [REA website](https://rea.tools/)",
            "- [Official website sources](https://github.com/morluto/rea/tree/main/website)",
            "- [Contributing](CONTRIBUTING.md) · [Catalog data](data/) · [Review method](docs/curation.md)", "",
            "- [Adobe: confirmed work and related projects](docs/adobe-related.md) · [GitHub keyword search log](docs/search.md)", "",
            f"- [Only repositories created October 7–13: {recent} projects](collections/2026-10-07--2026-10-13.en.md)", "",
            "## How to read this list", "",
            "- **Documented:** the linked source includes concrete REA operations, evidence IDs, function references or analysis records. This is source review, not our own reproduction.",
            "- **Author attribution:** the author explicitly says REA was used, but detailed tool output or provenance is not public.",
            "- **Limited:** REA handled preliminary inspection, or its deeper analysis failed and other tools did the main work. These entries have their own section.", "",
            "Stages describe the artifact: an implementation, prototype, partial reconstruction, compatibility tool or research output. They are not quality scores. We have not built or run the listed projects; test and hardware claims belong to their authors. Public source availability does not grant a license to original software or assets.", "",
            "## Browse by category", "",
        ]
    else:
        lines += [
            "收集使用 [REA — Reverse Engineer Anything](https://github.com/morluto/rea) 开展的软件重建、兼容工具和研究，直接链接实际实现与分析证据。", "",
            "首批条目聚焦 2026 年 10 月发现的闭源软件案例。每项先用一句话介绍原软件是做什么的，再说明这个项目做到了什么、REA 起了什么作用、还有哪些未完成。REA 帮助编程智能体调用分析工具；使用过 REA 不代表恢复了原始源码。", "",
            f"**{len(entries)} 个项目 · {evidence_counts['documented']} 项有具体分析记录 · {evidence_counts['attributed']} 项有作者声明 · {evidence_counts['limited']} 项属于 REA 有限参与。** 最近核查：**{reviewed}**。", "",
            f"**首期时间窗口：2026 年 10 月 7—13 日。** 其中 {recent} 个仓库在此期间创建；较早仓库保留实际建库日期，另有 {unknown} 项日期尚未核对。日期链接到 GitHub 元数据，采用 UTC，表示建库时间，不表示正式发布或私有仓库转公开时间。", "",
            "## 从这里开始", "",
            "- [REA 仓库与文档](https://github.com/morluto/rea)",
            "- [REA 官网](https://rea.tools/)",
            "- [官方网站源码](https://github.com/morluto/rea/tree/main/website)",
            "- [贡献指南](CONTRIBUTING.zh-CN.md) · [目录数据](data/) · [核查方法](docs/curation.zh-CN.md)", "",
            "- [Adobe：已确认案例与相关项目](docs/adobe-related.zh-CN.md) · [GitHub 关键词检索记录](docs/search.zh-CN.md)", "",
            f"- [仅查看 10 月 7—13 日新建仓库：{recent} 项](collections/2026-10-07--2026-10-13.zh-CN.md)", "",
            "## 如何阅读", "",
            "- **具体记录**：来源中可找到 REA 操作、证据 ID、函数引用或分析记录；这是文献与源码核查，不是本目录独立复现实验。",
            "- **作者声明**：作者明确说使用了 REA，但未公开详细工具输出或完整分析过程。",
            "- **有限参与**：REA 只承担初步检查，或深度分析失败后由其他工具完成主要工作；这类条目单独列出。", "",
            "阶段标签描述已有实现、原型、局部重建、兼容工具或研究成果，不是质量评分。本目录未逐一编译或运行项目；测试与硬件验证结果来自作者记录。源码公开不代表获得原软件或资源的使用许可。", "",
            "## 按类别浏览", "",
        ]
    for category, titles in CATEGORIES.items():
        lines.append(f"- [{titles[n]}](#{category}) — {counts[category]} · [" + ("category page" if n == 0 else "分类页") + f"](categories/{language}/{category}.md)")
    for category, titles in CATEGORIES.items():
        lines += ["", f'<a id="{category}"></a>', "", f"## {titles[n]}", "", table([x for x in entries if x["category"] == category], language)]
    if n == 0:
        lines += ["", "## Contribute", "", "Add or correct a project through a pull request or the [project submission form](https://github.com/jiaqiwang969/awsome-rea/issues/new?template=project.yml). Include a direct source for REA involvement and an honest scope statement. Edit the bilingual data, then run `python3 scripts/build_catalog.py`. See [CONTRIBUTING.md](CONTRIBUTING.md).", "", "## Acknowledgments and license", "", "The category-based collection and generated homepage are inspired by [yibie/awesome-jev](https://github.com/yibie/awesome-jev). REA is maintained by [morluto and contributors](https://github.com/morluto/rea); this is an independent community catalog. [Other discovery resources](docs/curation.md#discovery-resources) help find leads but do not substitute for original evidence.", "", "The catalog text and maintenance scripts are available under the [MIT License](LICENSE). Linked projects, original programs and assets retain their own licenses and rights.", ""]
    else:
        lines += ["", "## 参与贡献", "", "欢迎通过 Pull Request 或[项目提交表单](https://github.com/jiaqiwang969/awsome-rea/issues/new?template=project.yml)补充、纠正或移除条目。请提供 REA 参与的一手来源和准确的完成范围。编辑双语数据后运行 `python3 scripts/build_catalog.py`，详见[贡献指南](CONTRIBUTING.zh-CN.md)。", "", "## 致谢与许可", "", "分类组织和自动汇总首页的方式参考了 [yibie/awesome-jev](https://github.com/yibie/awesome-jev)。REA 由 [morluto 与贡献者](https://github.com/morluto/rea)维护；本项目是独立社区目录。[其他检索资源](docs/curation.zh-CN.md#discovery-resources)用于发现线索，不能替代原始证据。", "", "本目录文字及维护脚本采用 [MIT 许可](LICENSE)。链接项目、原程序及资源保留各自的许可与权利。", ""]
    return "\n".join(lines)


def build_pages(entries):
    pages = {}
    for language in LANGUAGES:
        n = LANGUAGES.index(language)
        readme = "README.md" if n == 0 else "README.zh-CN.md"
        pages[ROOT / readme] = homepage(entries, language)
        recent = [entry for entry in entries if in_initial_window(entry)]
        other_language = "zh-CN" if n == 0 else "en"
        snapshot = "2026-10-07--2026-10-13"
        title = "New repositories: October 7–13, 2026" if n == 0 else "2026 年 10 月 7—13 日新建仓库"
        note = (f"{len(recent)} catalog entries whose GitHub creation dates fall within this UTC window. This fixed snapshot is not a rolling feed; creation does not establish release or public-visibility dates." if n == 0 else f"仅列出 GitHub 建库日期落在这一 UTC 时间窗口内的 {len(recent)} 个条目。本页为固定快照，不是滚动更新列表；建库日不等于发布日或转公开日。")
        lines = [f"# {title}", "", "<!-- Generated by scripts/build_catalog.py. -->", "", f"[{'Home' if n == 0 else '首页'}](../{readme}) · [{'简体中文' if n == 0 else 'English'}]({snapshot}.{other_language}.md)", "", note]
        for category, titles in CATEGORIES.items():
            subset = [entry for entry in recent if entry["category"] == category]
            if subset:
                lines += ["", f"## {titles[n]}", "", table(subset, language)]
        pages[ROOT / "collections" / f"{snapshot}.{language}.md"] = "\n".join(lines) + "\n"
        for category, titles in CATEGORIES.items():
            other = "zh-CN" if n == 0 else "en"
            subset = [entry for entry in entries if entry["category"] == category]
            text = f"# {titles[n]}\n\n<!-- Generated by scripts/build_catalog.py. -->\n\n"
            text += f"[{'Home' if n == 0 else '首页'}](../../{readme}) · [" + ("简体中文" if n == 0 else "English") + f"](../{other}/{category}.md)\n\n"
            text += ("Evidence labels and review scope are explained on the homepage." if n == 0 else "证据标签与核查范围见首页说明。") + "\n\n"
            text += table(subset, language) + "\n"
            pages[ROOT / "categories" / language / f"{category}.md"] = text
    return pages


def check_local_links():
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for target in re.findall(r"\]\(([^\s)]+)\)", path.read_text(encoding="utf-8")):
            if urlparse(target).scheme or target.startswith("#"):
                continue
            destination = target.split("#", 1)[0]
            require((path.parent / destination).exists(), f"{path.relative_to(ROOT)}: missing local link {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Validate data, generated pages and local links without writing")
    args = parser.parse_args()
    try:
        entries = read_catalog()
        pages = build_pages(entries)
        stale = []
        for path, content in pages.items():
            if args.check:
                if not path.exists() or path.read_text(encoding="utf-8") != content:
                    stale.append(str(path.relative_to(ROOT)))
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content, encoding="utf-8")
        require(not stale, "Generated files are stale: " + ", ".join(stale) + "; run python3 scripts/build_catalog.py")
        check_local_links()
        print(f"{'Checked' if args.check else 'Built'} {len(entries)} projects, {len(pages)} bilingual pages; data and local links valid.")
    except (ValueError, TypeError, KeyError, OSError) as error:
        print(f"Catalog error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
