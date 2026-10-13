# 参与 Awesome REA

[English](CONTRIBUTING.md) · [简体中文](CONTRIBUTING.zh-CN.md)

欢迎补充、纠正和移除条目。一个有用的案例应同时说明原目标、REA 的具体贡献，以及公开的实现或研究成果。

## 收录项目

1. 找到一手来源：作者仓库、分析笔记、提交、问题讨论或公开账号。聚合目录不能单独作为证据。
2. 确认 REA 确实参与。仅安装 skill 或添加 MCP 配置不满足条件。
3. 描述现有成果和剩余缺口。解析器不等于恢复整个应用，两个替代函数不等于恢复整款游戏。
4. 同时提供英文和简体中文，保持范围与不确定性一致，不在翻译中增强结论。
5. 在 `data/` 的一个 JSON 数组中加入一条记录。文件仅用于编辑分组，实际展示类别由 `category` 决定。

先用一两句通俗的话介绍原软件：用户拿它做什么、主要有哪些功能。游戏说明怎么玩；设备应用说明能控制什么。例如 Everything 可以写成“输入文件名，就能快速找到 Windows 电脑里的文件和文件夹”。原软件的用途与重建项目实际具备的功能分别描述。

不要向本目录提交凭据、原商业程序、提取资源或复制的第三方代码；直接链接项目自身的证据。不要仅因仓库公开，就把项目称为开源软件。

## 数据字段

每条记录必须包含以下字段，现有记录可作为完整示例。

| 字段 | 含义 |
| --- | --- |
| `id` | 稳定且唯一的小写标识。 |
| `name`、`target`、`repo` | 成果名称、原目标、规范的公开 GitHub 仓库链接。 |
| `target_description` | 含 `en` 与 `zh-CN` 的对象：用一两句通俗的话介绍原软件用途及主要功能。 |
| `category` | `desktop`、`media`、`web`、`devices`、`games` 或 `limited`。 |
| `stage` | `implementation`、`prototype`、`partial`、`compatibility` 或 `research`，不表示质量评分。 |
| `evidence` | `documented`、`attributed` 或 `limited`，定义见首页。 |
| `evidence_urls` | 一至两个直接的一手证据链接，优先具体文件或提交。 |
| `summary` | 含 `en` 与 `zh-CN` 的对象：公开成果能做什么。 |
| `rea` | 含 `en` 与 `zh-CN` 的对象：REA 实际做了什么。 |
| `limitations` | 含 `en` 与 `zh-CN` 的对象：重要缺口、依赖或验证边界。 |
| `created_at` | GitHub `created_at`，格式为 `YYYY-MM-DDTHH:MM:SSZ`；未核对时填 `null`，不能用提交日期或搜索收录日期替代。 |
| `reviewed_at` | 实际核查来源的日期，格式为 `YYYY-MM-DD`。 |

`evidence: limited` 必须配合 `category: limited`。项目可以有大量可用代码，这个标签只描述 REA 的参与范围。作者明确声明但没有详细分析依据时，采用 `attributed`。

## 生成与检查

需要 Python 3.10 或更新版本，不依赖第三方包。

```bash
python3 scripts/build_catalog.py
python3 scripts/build_catalog.py --check
```

脚本生成两份 README、全部双语分类页及 `collections/` 中的首期时间窗口快照。请同时提交 JSON 修改及重新生成的 Markdown，不要手动修改生成页。

检查涵盖双语字段、日期、项目去重、证据分类、生成结果一致性和本地链接；不会运行所收录的软件，也不会证明外部结论真实或确定法律状态。外部证据仍需人工核查。

## 提交修改

- 每次提交聚焦明确的条目，并说明收录依据。
- AI 辅助贡献遵守相同的证据标准，需要核对链接和结论。
- 发现 REA 贡献或实现覆盖范围被夸大时，欢迎直接纠正。
- 不要把本目录的 MIT 许可套用到链接项目的代码或资源上。

也可以使用[项目提交表单](https://github.com/jiaqiwang969/awsome-rea/issues/new?template=project.yml)或[纠错表单](https://github.com/jiaqiwang969/awsome-rea/issues/new?template=correction.yml)。
