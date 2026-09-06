# Issue #85: the routing definition, its drafts and its blind reviews

The raw artifacts behind the resolution comment on [#85](https://github.com/Billy423/semester-manager/issues/85), kept because `docs/agents/research-method.md` says a conclusion whose evidence was deleted is not auditable. Nothing here is a ruling; the ruling is the posted comment (`drafts/v8.md`) and the records it landed as, `0101` and `0102`.

## What is here

- `preregistration.md` - written before the first review ran and not edited afterwards: the lenses, the thresholds, the judgment calls, and seven predictions of what the reviews would find. It names the reviewed file as `resolution-85.md`; that file is `drafts/v1.md` here, renamed on copy.
- `drafts/v1.md` to `drafts/v8.md` - every draft of the resolution comment. `v8.md` is what was posted.
- `reviews/01` to `reviews/08` - every blind review, verbatim, with a header saying what the reviewer was given and withheld. Reviews 1 and 2 ran on `v1` under two lenses (attribution, falsification); reviews 3-8 ran the falsification lens on each subsequent draft, each by a fresh subagent blind to the earlier reviews. Reviews 7 and 8 used Claude Opus at the owner's request; the rest used Claude Sonnet.

## The trajectory

| draft | review | blocking | what the review found |
|---|---|---|---|
| v1 | 1, 2 | 9 | the domain enumerated from four landed reads and the test fitted to them; five records cited from memory for aspects they do not speak about |
| v2 | 3 | 13 | the definition reaching into ring 0's present content (`0042`, `0038`) and letting it shape routing |
| v3 | 4 | 6 | output type under-specified (no relations, fan-in), test quantifier loose |
| v4 | 5 | 7 | the predicate language extended again; `REPEAT` infinite on cycles; `0004` collision |
| v5 | 6 | 4 | predicate cannot reference an earlier path position; one-return premise stricter than its ground; `#12 item 6` misattributed |
| v6 | 7 | 10 | the ruled *type* was the enumeration one grain up; test quantifier circular; extension ambiguous; spontaneity unrecorded |
| v7 | 8 | **0** | ten repairs, applied in v8 |

## Scoring against the pre-registration

Of the seven predictions, one was hit (P4, composition undefined), three were partially hit, three missed. Forty-nine blocking findings across the six falsification reviews were outside the prediction list. Per `research-method.md`, the exercise is scored on that unpredicted yield, and its largest item was the method finding the comment's third paragraph records: the step list, the precise types of an intent and a path, and the test's formalisation are the query grammar, which #84 places after the map, and none could be completed before #86-#88 supply the judgments they must serve. Deliverable 3 therefore landed as the test's informal wording plus three formalisation questions, a demotion the comment states rather than hides.

## Two things a reader should know

**The reviewers were withheld the session's analysis, not the material** (`research-method.md`). What they lacked that the material could not supply were rulings the owner made in the session - the effectiveness constraint, the `0001` authorization, spontaneity, paths, one-call chaining, the wildcard's exposure. Each was flagged as unrecorded until the comment recorded it. The later briefs told reviewers to treat those as ruled; the earlier ones did not, and the earlier reviews' findings on that score are correct as stated.

**The reviewers were told that ring 0's present content does not constrain routing** from review 4 onward, on the owner's ruling that the ticket's premise makes ring 0 downstream. Findings of the form *routing contradicts what ring 0 currently holds* were thereafter repair, not blocking; findings of the form *the draft misdescribes a record* stayed blocking. The distinction, and why it is not a licence to ignore inconvenient records, is argued in the session and summarised in the comment's third paragraph.
