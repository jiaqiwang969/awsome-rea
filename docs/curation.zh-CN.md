# 核查方法

[English](curation.md) · [简体中文](curation.zh-CN.md) · [首页](../README.zh-CN.md)

## 范围

首批目录来自 2026 年 10 月 13 日对公开 GitHub 项目及作者记录的核查，重点关注 10 月 7—13 日创建的仓库。范围包括闭源软件、可通过浏览器观察的产品、专有格式与设备客户端。较早但有相关 REA 工作的项目也会保留，并标注真实日期。

本目录仅查看了公开说明与源码文件，没有安装、编译、运行或独立测试这些项目。测试通过和硬件操作成功等结果来自链接中的作者记录。

[GitHub 检索记录](search.zh-CN.md)列出全站仓库、代码和提交查询及覆盖范围。[Adobe 核查记录](adobe-related.zh-CN.md)分别说明已确认使用 REA 的打印功能案例，以及尚未确认 REA 归因的 Adobe 风格相关应用。

## 收录与证据

每个项目仅归入一个类别，包含实现链接、REA 使用依据、成果范围和限制说明。具体工具输出、证据 ID、函数引用或执行记录支持 `documented`；只有作者一手声明时采用 `attributed`；仅初步检查或深度分析失败后改用其他工具时采用 `limited`。

证据强度和实现完成度分开判断：详细分析可能只产出几个函数；代码较完整的应用也可能仅用 REA 检查过包信息。重建项目可能继续依赖原版资源或运行时，已知边界会明确写出。

仅安装 REA、复制 skill、列入未来计划或没有明确成果的仓库不收录。明确表示没有采用 REA 的项目不算 REA 案例。只有社交展示、没有公开成果仓库的项目不进入首批实现目录。

## 日期

`created_at` 来自 GitHub 仓库 API，保存 UTC 时间，不是提交作者日期、发布日、项目起始日或转公开时间。近期新增研究文档不能把旧仓库变成本周新项目。`reviewed_at` 记录来源核查日期，不保证外部项目此后不变。

## 维护

修改 `data/` 的双语记录后重新生成文档。CI 在推送和 Pull Request 时检查结构一致性。首版没有定时爬虫、自动接收条目或自动发布未经核查的搜索结果。

链接迁移、许可遗漏、描述错误或结果夸大可通过纠错 Issue 报告。删除前需核查失效链接；单次 HTTP 失败不能证明项目已经消失。

<a id="discovery-resources"></a>

## 检索资源

以下目录用于发现线索，不能仅因其他目录收录，就证明项目使用了 REA。

- [awesome-REA-cases](https://github.com/songshikang0111/awesome-REA-cases)
- [awesome-REA](https://github.com/AIshihzong/awesome-REA)
- [rea-gems](https://github.com/sqwu/rea-gems)
- [rea-awesome](https://github.com/miles990/rea-awesome)
- [Awesome REA](https://awesomerea.com/)
- [REA Directory](https://readirectory.app/)

组织方式参考了 [awesome-jev](https://github.com/yibie/awesome-jev)。本目录重新撰写说明，并链接到项目原始证据。
