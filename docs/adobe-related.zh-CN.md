# Adobe 相关项目

[English](adobe-related.md) · [简体中文](adobe-related.zh-CN.md) · [返回首页](../README.zh-CN.md)

核查日期：**2026-10-13**。

## 已收录的 REA 案例：Review

原软件的用途：**macOS 预览（Preview）**用于看图片、阅读和批注 PDF；**Photoshop**用于修图、合成图片，也提供细致的照片打印设置。

[Review](https://github.com/KingDomino/review) 是主要参考 macOS Preview 的 Rust PDF 与图片查看器，其中照片打印对话框参考了 **Adobe Photoshop 2025 的 Print Settings**。

其[一手分析记录](https://github.com/KingDomino/review/blob/main/docs/photoshop-print-analysis.md)明确说明：使用 REA 6.4 `inspect-macho` 检查 Photoshop 导入的打印 API，并结合发行版中的 EXV 布局与字符串资源进行独立实现。[2026-10-12 的源码提交](https://github.com/KingDomino/review/commit/14453a167af97a77a3f0f8859cae86a010f12fcc)加入照片定位、等比缩放、纸张设置、PPI 显示、裁切标记和 PDF 输出，具体代码位于 [src/printing.rs](https://github.com/KingDomino/review/blob/main/src/printing.rs)。

仓库[创建于 2026-10-12（UTC）](https://api.github.com/repos/KingDomino/review)。本目录将其收录为“有具体证据、局部实现”的案例：Adobe 相关工作限于打印流程，作者说明没有反编译或复制 Adobe 代码。

## ArtCraft 七件套相关项目

ArtCraft 团队在 `storytold` GitHub 组织中公开了以下 Rust 独立实现。[官方家族列表](https://github.com/storytold/photocraft#the-crafting-apps)直接链接七个仓库；公开提交可确认 [Brandon Thomas（`echelon`）与 Claude Opus 5.5 协作](https://github.com/storytold/filmcraft/commit/fccddb6ea82deab89eeb881db5cf8d7d4c143e45)。

**截至 2026-10-13，本次核查尚未找到能够确认这七个项目使用 REA 的一手证据。** 项目自己的文档描述了依据公开规格、文档及允许范围内的行为观察进行实现的方法，因此在此作为相关项目单独维护，不计入 REA 案例数量。

| 项目 | 原软件及主要用途 | 仓库创建日期（UTC） | 项目的一手方法说明 |
|---|---|---|---|
| [PhotoCraft](https://github.com/storytold/photocraft) | **Photoshop** — 修照片、抠图和合成图片，用来做海报、宣传图等视觉作品。 | [2026-09-30](https://api.github.com/repos/storytold/photocraft) | 依据[公开规格及行为、外观观察](https://github.com/storytold/photocraft/blob/main/AGENTS.md)独立编写代码。 |
| [VectorCraft](https://github.com/storytold/vectorcraft) | **Illustrator** — 绘制放大后依然清晰的图形，常用来做标志、图标和插画。 | [2026-09-30](https://api.github.com/repos/storytold/vectorcraft) | 依据[公开文档](https://github.com/storytold/vectorcraft/blob/main/AGENTS.md)，所有者规则明确禁止使用 Adobe 软件作为研究参照。 |
| [FilmCraft](https://github.com/storytold/filmcraft) | **Premiere Pro** — 剪辑和拼接视频，添加字幕、配乐，再导出成片。 | [2026-09-30](https://api.github.com/repos/storytold/filmcraft) | [独立实现 Rust 编辑器与编解码器](https://github.com/storytold/filmcraft)，编解码器依据公开标准编写。 |
| [LightCraft](https://github.com/storytold/lightcraft) | **Lightroom** — 管理大量照片，批量调整曝光和色彩，常用于摄影后期。 | [2026-09-30](https://api.github.com/repos/storytold/lightcraft) | 依据[公开规格与只读观察](https://github.com/storytold/lightcraft/blob/main/AGENTS.md)，禁止读取或反汇编 Adobe 安装包。 |
| [EffectCraft](https://github.com/storytold/effectcraft) | **After Effects** — 制作动画字幕、片头和视频特效，也能把多个画面合成为新场景。 | [2026-10-01](https://api.github.com/repos/storytold/effectcraft) | 依据[公开文档与行为观察](https://github.com/storytold/effectcraft)，独立实现渲染和媒体组件。 |
| [DesignCraft](https://github.com/storytold/designcraft) | **InDesign** — 编排书籍、杂志、画册等多页文档，把文字和图片排成适合印刷或电子阅读的页面。 | [2026-10-01](https://api.github.com/repos/storytold/designcraft) | 使用合成文档进行[界面黑箱观察](https://github.com/storytold/designcraft/blob/main/AGENTS.md)，禁止读取或反汇编 InDesign 安装包。 |
| [PdfCraft](https://github.com/storytold/pdfcraft) | **Acrobat** — 阅读和编辑 PDF，合并或拆分文档，填写表格和添加签名。 | [2026-09-30](https://api.github.com/repos/storytold/pdfcraft) | 依据 [ISO 32000、Arlington 模型、公开文档及黑箱观察](https://github.com/storytold/pdfcraft/blob/main/AGENTS.md)。 |

Acrobat 对应项目在当前仓库和官方家族列表中使用 **PdfCraft** 名称。七仓均早于 **2026-10-07 至 2026-10-13** 这一周创建，但当周都有更新；上表日期来自 GitHub 元数据，不代表仓库转为公开的时间。

## 本次核查范围

本次读取了七仓的 README、贡献者规则、仓库元数据与公开提交，并使用 GitHub 全站代码、提交及仓库搜索，交叉查找 REA 和 Adobe 产品名。在 `storytold` 组织内对 `morluto`、`rea-agents`、`reverse-engineer-anything` 的代码搜索均无命中。

**搜索无命中不能证明项目没有使用过 REA。** 后续若出现作者说明或公开分析记录，可以据此补充归因；目前状态为未确认。证据标准见本目录的[核查方法](curation.zh-CN.md)。

本页手写维护，不参与生成式案例数据的统计。
