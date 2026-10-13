# GitHub search log

[English](search.md) · [简体中文](search.zh-CN.md) · [Home](../README.md)

Search date: **2026-10-13**. Initial creation-date window: **2026-10-07 through 2026-10-13, UTC**.

## Global keyword searches

Discovery used GitHub's repository, code and commit search through the authenticated GitHub CLI. The searches below were global, without an owner restriction. Their counts are a snapshot of search results, not a count of qualifying REA projects.

| Search type | Exact query | Snapshot coverage |
| --- | --- | --- |
| Repositories | `"morluto/rea" in:readme fork:false` | 402 results, all 5 pages fetched. |
| Repositories | `"reverse engineer anything" in:readme created:2026-10-07..2026-10-13 fork:false` | 274 results, all 3 pages fetched. |
| Commits | `"rea-cli" committer-date:2026-10-07..2026-10-13` | 20 results fetched. |
| Code | `"rea-agents"` | 4,760 reported matches; first 100 inspected as leads, not exhaustive. |
| Code | `"rea.tools"` | Results inspected for result repositories versus copies of the REA tool. |

The two repository queries produced **594 distinct repository names** combined. This is metadata-level discovery: not all 594 repositories received a source review. Many hits were mirrors, copied skills, news feeds, profiles or lists. Potential results were then checked in their own repositories, including README files, analysis reports, tool output, source files and commits.

Additional targeted searches combined REA identifiers with application names, `Ghidra`, `decompilation`, games, devices and Adobe product names. For Adobe, global results were followed by searches inside `storytold` and source review of all seven related applications. See the [Adobe review](adobe-related.md).

Other recorded queries included `"rea.tools" in:readme created:2026-10-07..2026-10-13 fork:false` (68 repository results), `"reverse-engineer-anything" "reimplementation" -repo:morluto/rea` (14 code results), and `"REA" "reimplementation" committer-date:2026-10-07..2026-10-13 -repo:morluto/rea` (3 commit results). All results of these three queries were fetched; source review focused on plausible projects. Exact project searches also found the REA attribution in [PGMMV-decrypt's implementation commit](https://github.com/nosini/PGMMV-decrypt/commit/4ebe64cc539dff0e3852526f81673379bf8bf97c).

Examples excluded after checking include [RingSwitch](https://github.com/Zy-zz/ringswitch), whose own notes say REA was not run, and [EXCELL-7ASSIBA](https://github.com/Rib4ko/EXCELL-7ASSIBA), which contains the REA tool but provides no clear record linking it to the spreadsheet implementation. These decisions reflect the reviewed evidence, not judgments about the projects' usefulness.

Game and device discovery also used repository queries `REA decompilation created:2026-10-07..2026-10-13` (7 results), `"rea-cli" in:readme created:2026-10-07..2026-10-13` (28), `"morluto/rea" in:readme game` (141) and `"morluto/rea" in:readme firmware` (109), plus commit query `REA Ghidra committer-date:2026-10-07..2026-10-13` (1,585). These searches inspected at most the first 100 results each; larger result sets were not exhausted.

## Repeat a query

GitHub CLI's repository search can be repeated as follows:

```bash
gh search repos '"morluto/rea" in:readme fork:false' --limit 500
gh search code '"rea.tools"' --limit 100
gh search commits '"rea-cli" committer-date:2026-10-07..2026-10-13' --limit 100
```

For page-by-page API inspection, this reads the first page without changing a repository:

```bash
gh api -X GET search/repositories \
  -f 'q="morluto/rea" in:readme fork:false' \
  -f per_page=100 -f page=1
```

Update the date window for future searches. Commit dates help locate recent activity; only the repository API's `created_at` is used for catalog creation dates.

## Coverage boundary

This is a broad search of GitHub's searchable public index, not a crawl of every file on GitHub or proof that every relevant project was found. Search indexing, result limits, repository changes and missing public attribution can hide relevant work. A missing keyword does not prove that REA was never used. Inclusion still requires a direct source, as described in the [review method](curation.md).
