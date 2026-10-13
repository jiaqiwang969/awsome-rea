# Review method

[English](curation.md) · [简体中文](curation.zh-CN.md) · [Home](../README.md)

## Scope

The initial collection comes from a review of public GitHub projects and author reports on October 13, 2026, with particular attention to repositories created October 7–13. It focuses on closed-source software targets, browser-visible products, proprietary formats and device clients. Earlier projects with relevant REA work are retained and dated honestly.

Only public descriptions and source artifacts were inspected. This catalog did not install, compile, run or independently benchmark the listed projects. Claims of successful tests or hardware operation belong to the linked authors.

The [GitHub search log](search.md) records global repository, code and commit queries and their coverage. The [Adobe review](adobe-related.md) distinguishes a confirmed REA-assisted printing feature from related Adobe-style applications whose REA attribution remains unconfirmed.

## Inclusion and evidence

Each project appears in one category and has a direct implementation link, REA provenance, a scope description and a limitation statement. Specific tool output, evidence IDs, function references and execution records support `documented`. An explicit first-party claim without those details supports `attributed`. Preliminary inspection or failed deep analysis followed by other tools supports `limited`.

Evidence strength is separate from implementation completeness: detailed analysis may yield only a few functions; a substantial application may have used REA only to inspect package metadata. A reconstruction can retain original assets or runtime dependencies. The catalog states those boundaries where known.

Repositories that only install REA, copy its skill, list it as a future plan or contain no identifiable result are excluded. Projects that explicitly say REA was not adopted are excluded rather than counted as REA examples. Social demonstrations without public result repositories are outside the initial implementation catalog.

## Dates

`created_at` comes from GitHub's repository API and is stored in UTC. It is not a commit author date, release date, project start date or public-visibility timestamp. A recent documentation commit does not make an older repository a new project. `reviewed_at` records the source-check date, not a promise that the project will remain unchanged.

## Maintenance

Edit the bilingual records in `data/`, then regenerate the documentation. CI checks structural consistency on pushes and pull requests. There is no scheduled crawler, automatic acceptance or automatic publishing of unreviewed search results.

Use a correction issue to report a moved link, missing license, inaccurate summary or overstated result. A failed link should be investigated before removal; a transient HTTP failure alone does not establish that a project disappeared.

<a id="discovery-resources"></a>

## Discovery resources

These lists helped find leads. Inclusion in another list is not proof that REA was used.

- [awesome-REA-cases](https://github.com/songshikang0111/awesome-REA-cases)
- [awesome-REA](https://github.com/AIshihzong/awesome-REA)
- [rea-gems](https://github.com/sqwu/rea-gems)
- [rea-awesome](https://github.com/miles990/rea-awesome)
- [Awesome REA](https://awesomerea.com/)
- [REA Directory](https://readirectory.app/)

Organization is inspired by [awesome-jev](https://github.com/yibie/awesome-jev). Descriptions here are written for this catalog and point back to the original project evidence.
