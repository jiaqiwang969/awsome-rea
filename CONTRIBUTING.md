# Contributing to Awesome REA

[English](CONTRIBUTING.md) · [简体中文](CONTRIBUTING.zh-CN.md)

Additions, corrections and removals are welcome. A useful entry connects a named target, a concrete REA contribution and a public implementation or research artifact.

## Include a project

1. Find a first-party source: the author's repository, analysis notes, commit, issue or public account. A directory listing alone is not evidence.
2. Check that REA actually participated. Merely installing its skill or adding MCP configuration is insufficient.
3. Describe the available artifact and the remaining gaps. A parser is not a recovered application, and two replacement functions are not a recovered game.
4. Provide English and Simplified Chinese text with the same scope. Do not translate an uncertainty into a stronger claim.
5. Add exactly one entry to a JSON array in `data/`. The source file is only an editing group; the entry's `category` determines where it appears.

Do not submit credential material, original commercial binaries, extracted assets or copied third-party code to this catalog. Link to the project's own evidence instead. Do not label a project open source solely because its repository is public.

## Data fields

Every record has the following fields; existing records provide complete examples.

| Field | Meaning |
| --- | --- |
| `id` | Stable, unique lowercase slug. |
| `name`, `target`, `repo` | Result name, original target, and canonical public GitHub repository URL. |
| `category` | `desktop`, `media`, `web`, `devices`, `games`, or `limited`. |
| `stage` | `implementation`, `prototype`, `partial`, `compatibility`, or `research`; not a quality rating. |
| `evidence` | `documented`, `attributed`, or `limited`, as defined on the homepage. |
| `evidence_urls` | One or two direct first-party evidence links. Prefer a specific file or commit over a repository root. |
| `summary` | Objects with `en` and `zh-CN`: what the public artifact does. |
| `rea` | Objects with `en` and `zh-CN`: what REA actually contributed. |
| `limitations` | Objects with `en` and `zh-CN`: important incompleteness, dependency or verification boundary. |
| `created_at` | GitHub `created_at` as `YYYY-MM-DDTHH:MM:SSZ`, or `null` if unchecked. Never substitute a commit or search-index date. |
| `reviewed_at` | Date the entry's sources were checked, as `YYYY-MM-DD`. |

Use `category: limited` whenever `evidence: limited`. The entry may still contain substantial working code; the label describes REA involvement, not the quality of that code. An explicit author claim without detailed provenance belongs to `attributed`.

## Build and check

Python 3.10 or newer is sufficient; no third-party packages are needed.

```bash
python3 scripts/build_catalog.py
python3 scripts/build_catalog.py --check
```

The builder generates both READMEs, the bilingual category pages and the initial date-window snapshot in `collections/`. Commit the JSON changes and regenerated Markdown together. Do not edit generated pages by hand.

Checks cover required bilingual fields, dates, unique projects, evidence classifications, generated output consistency and local links. The checks do not execute listed software, establish legal status, or prove that external claims are true. Review external evidence manually.

## Pull requests

- Keep each submission focused and explain why the entry qualifies.
- AI-assisted contributions follow the same source requirements. Verify the links and claims yourself.
- Include corrections when a report overstates REA's role or the implementation's coverage.
- Do not copy this catalog's MIT license onto a linked project's code or assets.

You can also use the [project submission form](https://github.com/jiaqiwang969/awsome-rea/issues/new?template=project.yml) or [correction form](https://github.com/jiaqiwang969/awsome-rea/issues/new?template=correction.yml).
