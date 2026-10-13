# Adobe-related projects

[English](adobe-related.md) · [简体中文](adobe-related.zh-CN.md) · [Home](../README.md)

Reviewed on **2026-10-13**.

## Included REA case: Review

The original apps serve different everyday tasks: **macOS Preview** opens images and lets you read and annotate PDFs; **Photoshop** edits and combines photos and offers detailed photo-printing settings.

[Review](https://github.com/KingDomino/review) is a Rust PDF and image viewer inspired primarily by macOS Preview, with a photo-printing dialog modelled on **Adobe Photoshop 2025 Print Settings**.

Its [first-party analysis](https://github.com/KingDomino/review/blob/main/docs/photoshop-print-analysis.md) records REA 6.4 `inspect-macho` inspection of Photoshop's imported printing APIs, combined with the shipped EXV layout and string resources. The [implementation commit dated 2026-10-12](https://github.com/KingDomino/review/commit/14453a167af97a77a3f0f8859cae86a010f12fcc) adds photo placement, proportional resizing, paper settings, a PPI readout, crop marks and PDF output; the code is in [src/printing.rs](https://github.com/KingDomino/review/blob/main/src/printing.rs).

The repository was [created on 2026-10-12 (UTC)](https://api.github.com/repos/KingDomino/review). This catalog includes it as a documented, partial case: the Adobe-related work covers the print workflow, and the author reports no decompilation or copying of Adobe code.

## ArtCraft's seven related applications

The ArtCraft team publishes the following independent Rust applications under the `storytold` GitHub organization. Their [official family index](https://github.com/storytold/photocraft#the-crafting-apps) links all seven. Public commits identify [Brandon Thomas (`echelon`) and Claude Opus 5.5 collaboration](https://github.com/storytold/filmcraft/commit/fccddb6ea82deab89eeb881db5cf8d7d4c143e45).

**As of 2026-10-13, this review has not found first-party evidence establishing REA use for these seven projects.** Their own documents describe implementation from public specifications, documentation and, where permitted, observed behavior. They are maintained here as related projects and are excluded from the REA case count.

| Project | Adobe reference / what it does | Repository created (UTC) | First-party description of the method |
|---|---|---|---|
| [PhotoCraft](https://github.com/storytold/photocraft) | **Photoshop** — Edit and retouch photos, cut out subjects and combine images to make posters and other graphics. | [2026-09-30](https://api.github.com/repos/storytold/photocraft) | [Public specifications and observation of behavior and appearance](https://github.com/storytold/photocraft/blob/main/AGENTS.md), with independently written code. |
| [VectorCraft](https://github.com/storytold/vectorcraft) | **Illustrator** — Draw graphics that stay sharp at any size, such as logos, icons and illustrations. | [2026-09-30](https://api.github.com/repos/storytold/vectorcraft) | [Public documentation only](https://github.com/storytold/vectorcraft/blob/main/AGENTS.md); the owner's rules explicitly prohibit using Adobe software as a reference. |
| [FilmCraft](https://github.com/storytold/filmcraft) | **Premiere Pro** — Cut and arrange video clips, add subtitles and music, and export a finished video. | [2026-09-30](https://api.github.com/repos/storytold/filmcraft) | [Independent Rust editing and codec implementation](https://github.com/storytold/filmcraft), with codecs written from public standards. |
| [LightCraft](https://github.com/storytold/lightcraft) | **Lightroom** — Organize photo collections and adjust exposure and color across many photos, especially for photography work. | [2026-09-30](https://api.github.com/repos/storytold/lightcraft) | [Public specifications and read-only observation](https://github.com/storytold/lightcraft/blob/main/AGENTS.md); reading or disassembling Adobe app bundles is prohibited. |
| [EffectCraft](https://github.com/storytold/effectcraft) | **After Effects** — Create animated titles, motion graphics and visual effects, and combine footage into new scenes. | [2026-10-01](https://api.github.com/repos/storytold/effectcraft) | [Public documentation and observed behavior](https://github.com/storytold/effectcraft), with independently implemented rendering and media components. |
| [DesignCraft](https://github.com/storytold/designcraft) | **InDesign** — Lay out books, magazines and brochures, arranging text and images for print or digital publication. | [2026-10-01](https://api.github.com/repos/storytold/designcraft) | [Black-box UI observation using synthetic documents](https://github.com/storytold/designcraft/blob/main/AGENTS.md); reading or disassembling the InDesign bundle is prohibited. |
| [PdfCraft](https://github.com/storytold/pdfcraft) | **Acrobat** — Read and edit PDFs, combine or split documents, fill in forms and add signatures. | [2026-09-30](https://api.github.com/repos/storytold/pdfcraft) | [ISO 32000, the Arlington model, public documentation and black-box observation](https://github.com/storytold/pdfcraft/blob/main/AGENTS.md). |

The current repository and family index use **PdfCraft** for the Acrobat-related application. All seven repositories were created before **2026-10-07–2026-10-13**, although each had updates during that week; creation dates come from GitHub metadata and do not establish when a repository became public.

## What was checked

The review checked the seven README and contributor-instruction files, repository metadata and public commits, alongside GitHub-wide code, commit and repository searches for REA and Adobe product names. Organization-scoped code searches for `morluto`, `rea-agents` and `reverse-engineer-anything` returned no matches.

**A search with no matches does not prove that REA was never used.** An author's report or a public analysis record could establish the connection later; it is currently unconfirmed. See the catalog's [review method](curation.md) for the evidence standards.

This page is maintained manually and is not part of the generated case data.
