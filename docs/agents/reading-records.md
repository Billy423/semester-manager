# Reading Inherited Records

How to read the records this project inherited - the migrated fall26 design corpus, anything quoted from it, and any frozen document handed to you as input. Where the domain documents live is `domain.md`; this file is about what a document you are reading is authority for.

## Before treating any list as exhaustive, state what question it was written to answer

Every enumeration in the corpus was written to answer one question, and it is complete only for that question. Before you use a list as "all of them" - all the fields, all the kinds, all the open items, all the rulings - **write down the question its author was answering, and check that it is your question.** If you cannot say what question it answered, you may not treat it as exhaustive.

This rule was written after two agent errors that were the same reasoning move: an agent argued for two rounds against a ruling it had not read, because the list it was working from did not contain it and it read the list as the whole set. Two independent passes over the corpus reached this same conclusion from different evidence.

## An artifact hands over its vocabulary along with its content

When you take content from a frozen document, **you take its words too, and its words may predate the ruling you are working under.** Check the vocabulary of anything you quote or build on against the current terms in `CONTEXT.md` before you reuse it.

The named instance: a frozen artifact's vocabulary set the units of a plan written after it, and the plan then reasoned in units the current design had already replaced. This is not a rare slip - it is the shape of four of the corpus records that are known to be standing wrong today, each one a record frozen before a ruling that still supplies vocabulary to readers arriving after it.

## "Check the changelog for the reasoning" does not work everywhere

The corpus's changelogs do not cover its whole period, and the gap is not marked:

- **The spec records carry their reasoning in changelogs.** Fifty-four entries across five files, twenty-one in the schema record alone. Every live contradiction found in those files was found from the changelogs rather than from suspicion. Reading the changelog first works here.
- **The domain records do not, before 2026-08-25.** Their changelogs only cover the 2026-08-25 import housekeeping and the 2026-08-28 corrections. **The reasoning for everything decided between 2026-08-21 and 2026-08-24 lives in in-place banners inside the sections, not in the changelog.** A changelog-first read of those files silently misses four days of decisions, and two rulings exist only in a changelog line with no body anywhere.

So: for anything dated before 2026-08-25, read the section and its banners. An absent changelog entry is not evidence that nothing was decided.

## Provenance

- Stating a list's question before treating it as exhaustive: `fall26:evidence/2026-08-29-course-level/NOTES.md` §3
- Vocabulary travelling with content: `fall26:evidence/2026-08-27-tier-recut/NOTES.md` · `fall26:evidence/2026-08-28-ring-0/NOTES.md`
- The changelog gap: `fall26:records/domain/model.md` and `fall26:records/domain/domain-design.md` changelogs, against `fall26:records/spec/*` changelogs; the corpus names this hazard against itself in `fall26:records/spec/architecture.md` §4, `fall26:records/spec/schema.md` (2026-08-28) and `fall26:records/spec/write-rules.md` (2026-08-28)
