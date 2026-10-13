# GitHub 检索记录

[English](search.md) · [简体中文](search.zh-CN.md) · [首页](../README.zh-CN.md)

检索日：**2026-10-13**。首期建库时间窗口：**2026-10-07 至 2026-10-13，UTC**。

## 全站关键词搜索

通过已登录的 GitHub CLI，使用 GitHub 仓库、代码和提交搜索发现线索。以下查询不限制仓库所有者，均为全站检索。命中数是搜索结果快照，不是符合收录条件的 REA 项目数。

| 搜索类型 | 完整查询 | 本次覆盖 |
| --- | --- | --- |
| 仓库 | `"morluto/rea" in:readme fork:false` | 402 个结果，已取完 5 页。 |
| 仓库 | `"reverse engineer anything" in:readme created:2026-10-07..2026-10-13 fork:false` | 274 个结果，已取完 3 页。 |
| 提交 | `"rea-cli" committer-date:2026-10-07..2026-10-13` | 已取得 20 个结果。 |
| 代码 | `"rea-agents"` | 返回总量 4,760，查看前 100 个作为线索，未穷尽。 |
| 代码 | `"rea.tools"` | 检查命中仓库，区分具体成果与 REA 工具副本。 |

两组仓库查询合并后有 **594 个不重复的仓库名**。这是元数据层面的线索发现，不代表已逐一审查 594 个仓库的源码。其中很多是镜像、复制的 skill、新闻流、个人主页和资源目录。对可能属于成果的项目，继续检查其 README、分析报告、工具输出、源码文件和提交。

另外组合 REA 标识与应用名称、`Ghidra`、`decompilation`、游戏、设备和 Adobe 产品名进行定向补搜。Adobe 先全站检索，再搜索 `storytold` 并逐一阅读七个相关应用的源码说明，见 [Adobe 核查记录](adobe-related.zh-CN.md)。

其他已记录的查询包括 `"rea.tools" in:readme created:2026-10-07..2026-10-13 fork:false`（68 个仓库结果）、`"reverse-engineer-anything" "reimplementation" -repo:morluto/rea`（14 个代码结果），以及 `"REA" "reimplementation" committer-date:2026-10-07..2026-10-13 -repo:morluto/rea`（3 个提交结果）。这三组均取得全部返回结果，源码核查聚焦可能符合条件的项目。仓库定向提交搜索还找到了 [PGMMV-decrypt 实现提交](https://github.com/nosini/PGMMV-decrypt/commit/4ebe64cc539dff0e3852526f81673379bf8bf97c)中的 REA 归因。

核查后排除的例子包括 [RingSwitch](https://github.com/Zy-zz/ringswitch)，其说明明确表示未运行 REA；以及 [EXCELL-7ASSIBA](https://github.com/Rib4ko/EXCELL-7ASSIBA)，虽包含 REA 工具，但缺少该工具参与电子表格实现的明确记录。这些判断针对已读证据，不代表对项目实用性的评价。

游戏与设备补搜还使用了仓库查询 `REA decompilation created:2026-10-07..2026-10-13`（7 个结果）、`"rea-cli" in:readme created:2026-10-07..2026-10-13`（28 个）、`"morluto/rea" in:readme game`（141 个）、`"morluto/rea" in:readme firmware`（109 个），以及提交查询 `REA Ghidra committer-date:2026-10-07..2026-10-13`（1,585 个）。这些查询每组最多查看前 100 个结果，较大的结果集未穷尽。

## 复查命令

可使用 GitHub CLI 重复以下查询：

```bash
gh search repos '"morluto/rea" in:readme fork:false' --limit 500
gh search code '"rea.tools"' --limit 100
gh search commits '"rea-cli" committer-date:2026-10-07..2026-10-13' --limit 100
```

按页检查 API 时，下面的命令只读取第一页，不修改仓库：

```bash
gh api -X GET search/repositories \
  -f 'q="morluto/rea" in:readme fork:false' \
  -f per_page=100 -f page=1
```

后续检索请更新日期范围。提交日期仅用于发现近期活动；目录建库日期始终使用仓库 API 的 `created_at`。

## 覆盖边界

本次广泛检索 GitHub 可搜索的公开索引，没有遍历 GitHub 每个文件，也不能证明已找到所有相关项目。索引、结果上限、仓库变更和作者未公开使用方法都会影响覆盖；关键词未命中不等于没有使用 REA。收录仍需直接来源，规则见[核查方法](curation.zh-CN.md)。
