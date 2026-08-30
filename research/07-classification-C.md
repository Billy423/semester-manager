# Classification C - Fields and identity (M40-M65)

**Scope.** 26 things. Proposals only: nothing here is written to `CONTEXT.md`, to `docs/adr/`, or to an issue. Where cluster B has already named a term, I classify against B's name and say so; where I think B's dependent claim is wrong I say that too, in M40.

**Two things the zoom changed before anything else.** Both are corrections to the inputs, not to the corpus.

1. **The graveyard has sixteen rows, not fifteen.** S2 counted fifteen and the inventory (M62, C51) repeats it. `schema.md §7` at source lists sixteen `| absent | why |` rows. The derived figure "thirteen of fifteen carry no changelog line" is therefore over the wrong denominator and should not be quoted.
2. **A Billy ruling dated 2026-08-29 sits in `evidence/`, not in a record, and it withdraws a measurement that a truth record still carries.** `evidence/2026-08-29-course-level/NOTES.md §6`: the 2c03 note bodies are a subagent's own compressions written before `write-rules.md` existed, so every character count taken from them - 87-278, 871, 1,010, 459 - has no standing. `model.md §10.5`'s `MEASURED 2026-08-28` banner rests entirely on those numbers and is **still in the record, uncorrected**. This is the load-bearing input to M59 and it inverts that thing's shape.

**The 22 correction, applied.** `architecture.md §4` (Billy, 08-28) at source: a fresh extraction found **14** obligations for 2c03, and the old 22 included recurring tutorial attendance, which the graveyard forbids. Things in this cluster whose reasoning quotes 22: **M45** ("3 of 22 rows are exam sittings"), **M54** ("one instance in 22"), **M55** ("3 of 22 obligations with no artifact"), **M62** (the whole table's arithmetic), **M63** ("six unlike purposes across the 22 fixture rows"), **M64** (`term_start`: "one week-relative obligation in 22"). Each is marked below. `evidence/2026-08-29-course-level/measurements.txt` independently reproduces **14 obligations, 4 course notes, 7 obligation notes, 6 of 14 carrying an annotation**.

---

## M40. `id` - the identity scheme

**Destination: `ADR`.**

**Proposed title:** *An id is opaque, assigned and never constructed; one id space, and every read returns handles.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** Idempotent landing keys on it, every link endpoint holds one, and a monotone never-reused counter cannot be retrofitted over a history of derived ids. One id space is refactor trigger A. |
| Surprising without context | **Yes.** A knowledge base whose identifiers say nothing about what they name, in a project whose entire subject is meaning, reads as a mistake. The retired scheme (`<course_id>-slug(name)`) is the obvious one and was live. |
| Result of a real trade-off | **Yes.** The derived scheme bought forward reference - a writer could construct A9's id from A9's name before A9 existed. It was given up on measured material, and forward reference was re-answered three other ways. |

**Body.** An `id` is opaque, monotone and assigned by the system, taken from **one id space shared by every kind that can be a link endpoint**, and it is never reused, a delete included. Nothing constructs one: an id is obtained by reading it back, so **every read that returns records must return their ids** or the rule cannot be followed. Constructing an id is a bet on reproducing another writer's spelling - a cognition problem wearing a mechanism's clothes.

**Shape that rides.**

```
id       := the next unused value in ONE id space, shared by every kind that can be a link endpoint
never reused, a delete included
obtained := by reading it back.  Nothing constructs one.
therefore   every read that returns records returns their ids
```

**Evidence that must travel, because it is what makes the ruling non-obvious.** One course names the same series `ChildMath A1` and `ChildsMath A4`; another spells one row `Week 2 Lab deliverables` and the next two `Week 3 / Week 4 Lab diliverables`. The three replacements for forward reference: list before linking · surface an untracked target to the user rather than auto-adding it · resolve a batch ingest in two passes.

**Where I disagree with cluster B, and why.** B's M31 proposes that B owns "the one-id-space commitment" and C owns "the id's properties". At source the id space is defined **inside `schema.md §1.1`'s definition of `id`**, in the shape block above, and `Ref` is a separate convention row in §1 that cites it. Recommendation: **M40 owns the one-id-space clause; B's M31 cites it.** The `Ref` ADR still owns kind-tagging, dangling and not-a-foreign-key, which are properties of the pointer and not of the id.

**The asymmetry B flagged, confirmed and worth stating in one of the two ADRs.** Nodes get opaque assigned ids; links have **no surrogate id at all** and are identified by the natural key `(from, to, kind, role, locator)` (`schema.md §5`). No survey states this. It should be one sentence, in whichever ADR reconciliation prefers - I would put it in B's M30, which is where the natural key is argued.

**Sequencing stripped.** "Scoped to the kinds that exist; it settles nothing about `concept` or `artifact`" is *not* sequencing and must be kept - it is a self-limit on the ruling, not an ordering.

**Touched by Billy's rulings.** None of the nine directly.

**Merge candidates.** **M41** (same trade-off, opposite side: where the material supplies an identifier, opacity is dropped). **F's M101** (addressing at the surface) - F says explicitly this is "the other half of the opaque id"; the two are one decision seen from two tiers and I would merge them if reconciliation wants three ADRs instead of four. **B's M31**.

**Cross-cluster.** B (M30, M31), F (M101).

**Zoomed.** Yes - `schema.md §1.1` and `§1`, `architecture.md §3` and `§5`. Confirms every clause verbatim. The zoom also confirms C29: `architecture.md §3` consequence 4 and `schema.md §1.1` are the same claim in two tiers' words, and the 08-28 changelog names the cost of the gap ("a divergence between two ruled records that nobody had propagated").

---

## M41. `course.id` - the exception to opacity

**Destination: `ADR`.**

**Proposed title:** *The id space is deliberately not uniformly opaque: an id is assigned only where the material supplies none.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** `course.id` is the string every course-scoped read, every `Ref("course", …)` and every render's grouping key is written against. |
| Surprising without context | **Yes.** A record that has just ruled ids opaque and meaningless then carries `2c03` as an id. Read without the rule, it looks like the opacity rule was not applied consistently. |
| Result of a real trade-off | **Yes.** Uniform opacity was available and simpler. It loses because inventing an identifier where the source already issues a canonical unique one adds a mapping nobody needs. |

**Body.** `course.id` is the supplied course code, and the line is drawn by the material rather than by the kind: **an id is assigned only where the material supplies no identifier of its own**, which today is every kind but `course`. A course code is canonical, unique and consistent wherever it appears, which is exactly what an obligation's name is not.

**The self-limit, which must travel.** "This is scoped to the kinds that exist. It settles nothing about `concept` or `artifact`, whose own material has not been read for this question." This clause is the reason the exception does not become a licence.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #1 indirectly: v1's boundary is coursework inside academics, so no kind arrives that would test the line again before v2.

**Merge candidates.** **M40** - same trade-off, and reconciliation may well want one ADR titled *"ids are opaque and assigned, except where the source issues one"*. I keep them separate as instructed, but this is the strongest merge pair in my cluster.

**Cross-cluster.** B's M16 (a course IS a node) is the companion and does not contradict this. B's `kind` term names `course`; my term list defines it.

**Zoomed.** Yes - `schema.md §1.1`, `§2`, `write-rules.md §2`. Confirms, and confirms the demotion S2 recorded: `write-rules.md §2` now carries `id | none` with a pointer, because "sitting in a `records/spec/` table was giving an agent recommendation `ruled` standing by placement."

---

## M42. `kind` as a discriminator, and `layer` as a separate axis

**Destination: `ADR`.** Taking cluster B's proposed split: **C owns the mechanism, B owns the names.**

**Proposed title:** *`kind` is a required discriminator, not metadata, and `layer` is a different axis.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** Every serialized line carries it, cold start dispatches on it, and construction is the only validation there is. Removing it means inferring shape from which fields are present, across every record ever written. |
| Surprising without context | **Yes.** `kind` looks like metadata - a label you could drop and still know what a record is. The record says the opposite: remove it and the node has no shape. |
| Result of a real trade-off | **Yes.** Shape-sniffing was the live alternative and is what a JSONL store invites. It loses because dispatching on which fields are present is exactly the control flow `design.md §3.1`'s trigger B forbids. |

**Body.** Every node record carries a required discriminator field named `kind` whose value is that kind's own name; it selects which declared field set the payload has, and a record cannot be constructed without it. **`layer` is a different axis** and only three kinds have one - conflating the two is the named failure mode, not an incidental risk.

**A repair worth recording inside the ADR.** The argument for `kind` originally rested on a degenerate record (a progress record with a null `state`, which carries no distinguishing field at all). The `progress.state` reversal removed that record from existence, and the 08-28 changelog re-grounded the rule on shape-sniffing-is-dispatch rather than withdrawing it. It is the cleanest instance in the corpus of an argument being repaired when its example was withdrawn, and it is the reason a reader should not conclude the rule went with the example.

**Sequencing stripped.** Nothing here; B strips "slice 1 introduces four kinds, slice 2 adds two" on the names side.

**Touched by Billy's rulings.** #8 through B: the word `layer` collides with Billy's "content layer / time layer". I support B's proposal to say **the skeleton** and **the time projection**, and to reserve `layer` for the three strata. My things are affected only through this ADR's second clause.

**Merge candidates.** **B's M25** - "relations are records, not fields on the related thing" is refactor trigger C and this is trigger B. B suspects recording one trigger while its siblings land elsewhere is worse than recording all five once, and I agree: **recommend one ADR carrying all five refactor triggers**, with M42, M43 and B's M25 citing it rather than each restating one. Flagged for reconciliation, not decided here.

**Cross-cluster.** B (M15 - the names; M25 - the sibling trigger), F (M98 - the four `§3` consequences may restate the trigger list), F (M106 - construction as the only gate is what makes `kind` load-bearing).

**Zoomed.** Yes - `schema.md §1` and `§8`. Confirms both the rule and the re-grounding. `§8` adds the clause that makes the ADR sharp: "without it the construct-by-kind step has nothing to dispatch on."

---

## M43. The conventions block - `null`, one free-text field, field-grain CRUD, timestamps

**Destination: `ADR`.**

**Proposed title:** *Four conventions that range over every kind.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** Field-grain CRUD determines the whole application-tier method set; a one-free-text-field cap is a constraint every future kind is designed against; `null` means *no record* everywhere or nowhere. |
| Surprising without context | **Yes, twice.** "Landing performs partial update, never whole-record replacement" is not how a JSONL store is usually written. And a **cap of one** free-text field, with `course` at zero, reads as arbitrary until you see the reason. |
| Result of a real trade-off | **Yes.** Billy's own statement of it: more than one free-text field and he has to decide where things go, so the overhead he is escaping returns; zero and it is over-structured. |

**Body.** Four conventions hold across every kind: `null` means **no record**, never a default, and must render as absence · **at most one free-text field per kind**, and `course` has zero, which is a cap and not a quota · **every field is individually CRUD-able**, so landing performs partial update and never whole-record replacement · timestamps are ISO 8601, with `added_at` on `course` and `obligation` and `created_at`/`updated_at` on the annotation kinds, because a note is modifiable and a record's birth is not its last claim.

**Shape that rides.**

```
null       -> no record.  Never a default.  Renders as absence.
             one deliberate exception: progress.state is not nullable, so there is no null to render
free text  -> at most one field per kind.  course: zero.
mutability -> field grain.  Landing = partial update, never whole-record replacement.
timestamps -> added_at on course, obligation.  created_at + updated_at on the annotation kinds.
```

**`added_at` is one of the rigidity rule's two declared exemptions** (B's M26). It is carried with no mechanism reading it, deliberately, against a future reader - stated as an exemption rather than an oversight. B is right that the rule must never be stated without the exemption clause; this is the thing that holds one half of it.

**A correction the ADR should carry rather than inherit silently.** `§1` used to say `added_at` was on every node. Neither annotation kind's field table carried it, so the blanket sentence was false as stated and would have misled a slice-2 kind author. It was corrected 08-28.

**22 correction.** None of the four conventions rests on a count.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #4 indirectly, through the `null` convention's carve-out: `progress.state` is not nullable *precisely so* the agent does not keep asking. That carve-out is written into the convention itself at source and is not a footnote.

**Merge candidates.** **B's M25 and my M42** - field-grain CRUD is one of the five refactor triggers. Same recommendation: record the five once. The **one-free-text-field rule** is a separate candidate: it and **M63** (`obligation.notes` and the non-overlap rule) are one argument seen from two ends - the cap only works because there is no catch-all field.

**Cross-cluster.** B (M26 - `added_at` is one of the two exemptions; M25 - the triggers), A (M10 touches the rigidity rule).

**Zoomed.** Yes - `schema.md §1` and its 08-28 changelog. **The zoom changed one thing.** The `null` convention's canonical example at source is now **`grade_share_conditional`**, not `progress.state`: "Rendered as a default, a null `grade_share_conditional` becomes an assertion that the stored share is a stated fact when no source said so - measured as the largest single class of unfaithful claim." The record re-grounded the convention on a live example when the old one was withdrawn. This partly repairs **C39** - see M50.

**⟂container.** "Must render as absence" is a rendering rule sitting in a record whose own conditions line says a rule about what an agent should DO is presentation tier. The surface it named is the CLI. The rule survives the container change; its home does not.

---

## M44. `obligation.course` - a field, not an edge

**Destination: `ADR`.**

**Proposed title:** *Course membership is a field, because the rule that relations are records exists to stop a polymorphic target becoming one.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** It is the grouping key of the projection and the set the symmetry rule ranges over; making it a link later re-homes every read. |
| Surprising without context | **Yes.** This project ruled that relations are records, not fields, and then made its most obvious relation a field. Without the reason that reads as an inconsistency. |
| Result of a real trade-off | **Yes.** A typed edge was the consistent move and was rejected on a stated boundary: course membership is single-valued, mandatory and monomorphic, and nobody walks it. |

**Body.** `obligation.course` is a `Ref` field on `obligation`, not an edge, and it is a property of `obligation` rather than of every node - a concept is not per-course. The rule that relations are records exists to stop a **polymorphic** target becoming a field, and this target is not polymorphic; the capability *list this course's obligations* is an enumeration either way.

**The rider, and it must travel inside the ADR.** **Whether the field is mutable is not ruled.** `write-rules.md §3` says so in its own words: it is an application-tier question, "still open at `../plan/application-tier.md §7.1` as a recommendation with no ruling. The code implements the recommendation; this record does not decide it." So the code implements an unruled recommendation. That is the ADR's one open edge and dropping it loses the only warning anyone has written about it.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine directly.

**Merge candidates.** **B's M25** shares the *rule* (relations are records) but not the *trade-off*: M25 is the rule's positive case, M44 is its declared boundary. They are the same decision's two sides and would read better as one ADR with the boundary stated inside. Flagged, not merged.

**Cross-cluster.** B (M16 - a course is a node does **not** make membership a link; this is the near-miss a reader trips on, and B flags it too), B (M25).

**Zoomed.** Yes - `schema.md §3`, `write-rules.md §3`, `schema.md` changelog 08-27. Confirms both halves, including that the mutability pointer was **demoted out of the write-rules table into a pointer** on 08-28 because sitting in the table was giving an agent recommendation `ruled` standing by placement.

---

## M45. `due`, and what a date-only value means

**Destination: `ADR`.**

**Proposed title:** *A date without a time resolves to `23:59`, at the schema level and not at the parser's discretion.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** Every stored date, every band-A window test and every derived `done_by` is read through it. Changing it moves every undated-time obligation by a day. |
| Surprising without context | **Yes.** The failure it fixes is silent: nothing errored, nothing tested it, and 2aa4's three dated obligations were a day early in **all 60 runs**. It was found only because it invalidated an experiment's tie. |
| Result of a real trade-off | **Yes.** `T00:00` is the parser default and was what the system actually did. The competing framing - leave it to whichever surface parses - is the thing the ruling names as the defect. |

**Body.** `due` is `Date | DateTime`, nullable, and is **the moment this obligation is anchored to** - the deadline for something handed in, the start for a sitting. A `Date` resolves to **`23:59`** at read time and the stored value is always returned raw; a `DateTime` is a stated time and is never overwritten by that default. A date without a time needs an explicit convention at the schema level, not at the parser's discretion.

**Shape that rides.**

```
due : Date | DateTime | null
Date      -> resolves to 23:59 at read time; stored value returned raw
DateTime  -> a stated time; never overwritten by the default
Date -> DateTime is an ordinary field-grain CRUD (the midterm pattern: a date first, a time later)
```

**22 correction.** The definition's own defence quotes "the 3 of 22 rows that are exam sittings". Over the live 14-row extraction that count is not re-derivable. The *argument* survives untouched - a definition narrowed to "the deadline" is false for exam sittings, and 2c03's live rows still contain them - but the number should not be quoted.

**One thing that is open and is not this ADR's to close.** **Which layer applies the `23:59` resolution.** `schema.md §3` says presentation tier; the 08-29 course-level cycle listed it as mandate item D and judged it "one line; a defensible default exists, so it is not a gate". It is the smallest open item in my cluster and it does not need a deferral issue - it needs a line in whichever presentation record is written first.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine directly. #3 touches it only in that a calendar surface is out.

**Merge candidates.** None sharing the trade-off. **M46** is the adjacent field but a different decision.

**Cross-cluster.** D (ring 0's band-A window `today-7d .. today+14d` reads `due`), F (M108, calendar).

**Zoomed.** Yes - `schema.md §3` and changelog 08-27, `model.md §8.3`. Confirms C32 exactly: `model.md §8.3` carries the prose ("the end of that day") and `schema.md` restored the number, attributed "Billy 2026-08-24 via `archive/changelog-2026-08-24-slice-1.md:241`". It is the one case in the corpus of a caught precision loss in transcription.

---

## M46. `done_by` / `target_date` / `finished_by` - one field, three names

**Destination: `CONTEXT`.**

This is the first of my three one-field-several-names cases. It is a naming resolution with a definition attached, not a decision with live alternatives - the alternatives are dead names, not competing designs.

**Proposed term.**

- **`done_by`** - the date the owner chose to have an obligation finished by. A stored value always means it was chosen; nothing computes one.
  _Avoid_: **`target_date`** (the name in Billy's own year-old Notion table and still live in `model.md §8`'s vocabulary block, defined nowhere in either corpus), **`finished_by`** (retired; "never had a ruling behind it"), and **start date** - rendering it as a start date is the measured misread the rename exists to fix.

**The identification no record makes, and it belongs in the `_Avoid_` line.** `target_date` and `done_by` are the same field. `target_date` is the name in the one artifact Billy actually maintains by hand, and **no record anywhere says they are the same field**. That is a three-survey merge finding and it dies unless the term list carries it.

**What is a rule and not a definition, and where it goes.** "A planner wanting a work-back date computes `due − 7 days` as a **derived** value under its own name, and computes nothing when `due` is null." That is a rule about a *different* value and belongs wherever the planner is specified - not in this term, and not lost. The empirical anchor for the 7 days is in a third survey the spec does not cite: Billy's own reports are dated **7-13 days ahead of each due date**.

**Why it is not an ADR.** The rename *was* a measured mechanism - it fixed the misread `finish 17 : start 1` across six runs - but what survives to be recorded is a name and a definition, and the measurement is the evidence for the name rather than a trade-off between designs.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine directly.

**Merge candidates.** **M47** and **M55** share the *shape* (one field, several names, resolve and name the loser) but not the trade-off. They should stay three terms, not one ADR.

**Cross-cluster.** D (`done_by` is a band-A trigger in ring 0; "triggering and ordering are different jobs" is D's, not mine).

**Zoomed.** Yes - `schema.md §3` and changelog 08-27, `ring-0.md §3` and `§5`. Confirms. `ring-0.md §5` adds the clause that keeps the two jobs apart: "`due` is the primary key, **not** `min(due, done_by)`."

---

## M47. `grade_share` / `weight` / `worth_percent` - one field, three names, and a standing exemption

**Destination: `CONTEXT`.**

**Proposed term.**

- **`grade_share`** - the approximate share of the final course grade an obligation carries, in percent, held for the person to read and **never** as an input to a computed ranking.
  _Avoid_: **`weight`** (`model.md §8`'s vocabulary; the derivation found it "absent from the schema entirely" and it is now the name of a thing that does not exist), **`worth_percent`** (`model.md §10.9`), and treating it as a partition of 100.

**The exemption clause, which belongs with the field and not only with the rule.** `grade_share` is a **standing declared exemption** from the rigidity rule: no mechanism reads it, and the exemption is the point rather than an oversight. B's M26 owns the rule and asks that the two exemptions live with their fields; this is one of them, `added_at` (M43) is the other.

**One honest limit on my own resolution.** `design.md §7` item 1 records the field's name as **not settled, owner: the user**. All four spec records use `grade_share` and Billy's 08-27 and 08-29 rulings both use it. So this term entry is a proposal that needs one word from Billy to become a resolution - not drift I am entitled to close by fiat. If reconciliation wants it as a deferral instead, the wake-up is trivial and the deferral is not worth an issue; I would rather ship the term and let him overwrite the string.

**What must not be lost from the exemption's own reason.** The stated ground is "because workload is judged from **progress plus size** rather than from the percentage" - and the size half of that mechanism was later removed from `parts` (M49, C35). **Billy's ruling 2 answers this**, and the answer should be written into the term's context rather than left as a dangling C35: both halves hold, size is judged from progress and load, and the new clause is that **the work need not be a functional one-pass - the agent sees the skeleton and ring 0, notices, and asks when needed.** The removed mechanism was replaced by an interaction, not by another field.

**A defect the field cannot hold, found at source and in no survey.** `evidence/2026-08-28-corpus/2c03/RULINGS-NEEDED.md` R2: 2c03's real shares already sum to 100, and the course grants two bonuses that are **additive, outside the 100**. Storing `1` asserts something false, and `optional: true` is the only signal separating them and does not carry additive semantics. The file records this as new - "four independent spec reviews missed it, because seeing it requires the arithmetic". It has no M-number. Listed under Orphan rulings.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #2 directly, both halves.

**Merge candidates.** **M46**, **M55** (same shape, different trade-off - keep separate). The **exemption clause** merges with B's M26 and with M43's `added_at`.

**Cross-cluster.** B (M26), A (M10), D (`ring-0.md §6` excludes it from the projection on a measured 38% and on an argument that needs no measurement).

**Zoomed.** Yes - `schema.md §3`, `ring-0.md §6`. Confirms, and `ring-0.md §6` marks its own number's standing honestly: the 38% "has **not** been re-derived structurally, which `CAVEATS.md §7` asks for before any metric in that folder is trusted." The measurement-free ground - the column sums to 95 and two 1% rows are bonuses outside the 100 - is the one that survives, and it is the same arithmetic R2 found.

---

## M48. `grade_share_conditional`, and the conditional-weighting defect

**Destination: `ADR`.**

**Proposed title:** *A conditional grade weight gets a marker, not a model, and the pointer to the rule is optional.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes** for the marker: it is the flag every reader of `grade_share` checks, and adding a `weighting_scheme` later means re-reading every stored share. |
| Surprising without context | **Yes.** The defect it fixes is the top-ranked faithfulness failure in the corpus, and the fix is one nullable bool that stores no part of the rule it warns about. A reader learns the number is conditional and may have no way to learn how. |
| Result of a real trade-off | **Yes, and it was made twice.** The general form - a `weighting_scheme` naming the alternatives with a derived weight - was rejected as over-built for one concrete calculation. Then the *required* pointer was made optional, on the ground that a schema rule manufacturing a conflict nobody would care about is a defect in the rule. |

**Body.** `grade_share_conditional` is a nullable bool: true when the stored share is one reading of a rule the course states conditionally or as a bound, **null means unknown and never *not conditional***. The rule itself **may optionally** be left on a one-line sticky note; requiring one is not a rule. A bound (*"worth at least 30%"*) is the same defect as a conditional (*"10/10/30 or 0/0/50"*).

**The narrowing, which must be recorded with the ruling and not smoothed.** Billy's 08-23 ruling made the fix "a `conditional` marker **plus a pointer to the rule**, so no reader can take the stored number for a stated fact." The 08-27 ruling made the pointer optional. The later ruling wins by recency and its ground is sound, but **the pointer was half of what made the marker actionable**, and the defect it exists to fix is 29 of 77 unsupported-or-contradicted claims - 38% of every measured faithfulness failure, and the only defect kind appearing in every configuration group. The sharpest statement of the mechanism, from E7: *the agent acts on a note that NEGATES a field and cannot act on a note that makes a field CONDITIONAL.*

**Rejected alternative, recorded so it is not re-proposed.** `weighting_scheme` - naming the alternatives with a derived weight. Rejected as over-built; the supporting observation is that nothing in 60 runs ever attempted to compare the two branches, so the ability to compare them is unevidenced. **Candidate graveyard row** (see the graveyard section).

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #2 indirectly - `grade_share` is reference only, which is what keeps a conditional share from needing to be computable. #7 has an edge here: an optional pointer means the system can hold a number and a note that qualify each other, or a number and no note at all; the second is not a conflict, but the first is exactly the shallow-versus-deep case ruling 7 partitions.

**Merge candidates.** **M47** shares the field but not the trade-off. The real sibling is the **late-day budget** (C37, `design.md §3.2`): both are rules that get *stored* as free text rather than *modelled*, so "what does it cost me later" is not computable in either. That is one trade-off made twice and reconciliation may want it named once.

**Cross-cluster.** A (the faithfulness guard), D (`ring-0.md §6`), E (the note that carries the rule is written under the render test, M58).

**Zoomed.** Yes - `schema.md §3` and changelog 08-27, `model.md §10.9`, `ring-0.md §6`. Confirms both rulings and the narrowing. `model.md §10.9` also carries a self-correction worth not re-inheriting: the often-repeated "four delivery paths" phrasing is an overstatement corrected by adversarial review - two mechanisms, two of them n = 1.

---

## M49. `parts`

**Destination: `ADR`.**

**Proposed title:** *`parts` carries the concepts that recur, as canonical singular names, and does not carry size.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** It is the only field carrying concept information before the concept kind exists, and every string written under a different rule has to be rewritten - the recurrence test alone took 50 candidate strings to 28 on one course. |
| Surprising without context | **Yes.** A field called `parts` on an obligation that splits into independently assessed parts carries **neither** those parts' scores **nor** their size, and stores concepts instead. And it stores a name the source never printed. |
| Result of a real trade-off | **Yes.** The field had two candidate responsibilities, both ruled live at one point: *let size be judged ordinally* and *be the connection point to concepts*. The archive recommended the first; the second was ruled and the recommendation is dead. Per-part weights and scores were measured and knowingly given up. |

**Body.** `parts` carries the concepts an obligation's source carries, as raw strings and never as pointers to concept nodes. A part is **a concept worth capturing because it might occur elsewhere in the system**, and the writer writes the canonical singular name of the concept rather than the phrase the source used - `Stacks and Queues` becomes `Stack` · `Queue`. It does not carry size, and it carries no status or score of its own.

**Shape that rides.**

```
parts : [string]                       -- concepts, raw strings, never Refs
kept:    Graph · Queue · Big-O · Linked List · Cuckoo Hashing · Priority Queue
dropped: Multiple Choice · Problem Solving       (noise - the paper's structure, not its content)
         Monte-Carlo · A5Tree · Life on the River (one-off and local to a single assignment)
```

**The finding B made and neither record states, and it belongs here.** `write-rules.md §3.4`'s **recurrence test is the concept-granularity ruling**. C21 recorded the adopted granularity rule ("cut at one thing that can be separately asked about or separately taught") as contradicting the agent's own "do not rescue the first hub by splitting into per-topic analysis concepts". A recurrence test forbids the per-topic split, and the worked rows keep `Big-O` while dropping `Monte-Carlo` as local. B zoomed it and closed it; I concur, and **C21 should be closed rather than carried**. The ADR should say the rule does two jobs, because two records own one rule and neither says so.

**The live hole, and Billy's ruling 2 closes it.** C35 is the inventory's most consequential cross-survey conflict: `workload` was retired on the ground that "size is observed ordinally - from `parts` and item notes first", and `write-rules.md §3.4` then removed size from `parts` and deferred the reader with no owner and no trigger beyond "when a need arises". So ring 0, whose declared job is routing, carries **no size or effort signal of any kind**. **Ruling 2 answers it and the answer must be written into this ADR:** the replacement is not another field but an interaction - the agent sees the skeleton and ring 0, **notices**, and **asks when needed**; the work need not be a functional one-pass. Ask-frequency is deferred to acceptance and evaluation, measurable only after the system is roughly built. **This closes E2 / C35 and it should not travel into reconciliation as an open escalation.**

**What is still owed on the field, narrowed by zoom.** `schema.md §9` item 1 no longer says the whole rule is owed - at source it now reads "Its **target** is settled: it carries concepts. What is owed is what counts as one, what context the writer must hold, and what the wording is for." Of those three, `write-rules.md §3.4` answers *what counts as one* (recurrence) and *what the wording is for* (the canonical singular name). **Only "what context the writing agent must hold" remains open**, and `schema.md §6` states why it is hard: *"flow method"* read alone is meaningless. That single residue is the honest statement of C38, and it is much narrower than either record implies.

**Two clauses that must not be lost.** (a) The **cost is stated and is not a defect**: a row whose material is entirely one-off gets few parts or none, and the empty Final Exam is the live instance - an exam's concepts are the course's concepts, so they recur and the rule keeps them. (b) `parts` is **excluded from ring 0's projection but is not unreadable** - Billy rejected the agent's "`obligation.parts` is homeless" reading on 08-29: ring 0 governs **residency, not readability**, and `parts` returns with any read of the record.

**22 correction.** Not load-bearing here. The measured figures (50 → 28; 12 of 22 fixture obligations carry parts) are per-course extraction counts; the 12-of-22 figure should not be quoted, and `evidence/2026-08-29-course-level/measurements.txt` gives the live shape: 14 rows, `parts` empty on 3.

**Sequencing stripped.** "The concept layer is slice 2, so the pointer question is not live" is dropped. The ruling that `parts` carries strings and never Refs is not an ordering.

**Touched by Billy's rulings.** #2 directly and decisively - see above.

**Merge candidates.** **B's M28** (the surviving hub) - same record, `write-rules.md §3.4`, and the same rule doing a second job. They are not the same trade-off (mine is what the field carries; B's is how the concept layer is cut) but the rule is one and should be **stated once and cited twice**. **M53** (`workload`) shares the C35 trade-off exactly and the two must not state ruling 2 differently.

**Cross-cluster.** B (M28), E (M94 - concept split / merge / rename), D (`ring-0.md §4`'s exclusion).

**Zoomed.** Yes - `write-rules.md §3.4`, `schema.md §3`/`§6`/`§9`, `ring-0.md §4`, `evidence/2026-08-29-course-level/NOTES.md`. **The zoom changed two things:** `schema.md §9` item 1 is narrower than the inventory reports, and Billy's 08-29 rejection of the homeless-`parts` reading is recorded in evidence and in commit `63612df`, not in any survey.

---

## M50. `optional`

**Destination: `ADR`.**

**Proposed title:** *A nullable bool means unknown; the writer supplies the obvious default, not the schema.*

| test | verdict |
|---|---|
| Hard to reverse | **Moderately.** Not the field, but the two-layer pattern: once a nullable-means-unknown field has a write rule defaulting it, un-splitting them means re-reading every stored null. |
| Surprising without context | **Yes.** The schema makes the field nullable *so the system never asserts what no source stated*, and then a write rule tells the writer to assert it anyway when the answer is obvious. Read separately the two look like they cancel. |
| Result of a real trade-off | **Yes.** A non-nullable bool was the alternative and was rejected because it forces the system to assert what no source stated. The cost of the nullable version - a record saying *unknown* about something obvious - is what the write rule pays, deliberately in a different record and a different tier. |

**Body.** `optional` is a nullable bool: true when nothing is lost by not doing it, and **null means unknown, never *not optional***. A separate **write rule** tells the writer to default it to false unless a source states otherwise, which leaves a stored null meaning the writer genuinely could not tell. This is a rule about the writer, not about the field, and the schema is unchanged by it.

**Shape that rides.**

```
schema (application tier):  optional : bool | null     null = UNKNOWN, never "not optional"
write rule (presentation):  default to false unless a source states otherwise
                            => a stored null means the writer genuinely could not tell
```

**Why the field exists at all.** "Without it a plan ranks a +1% survey among required work purely by date." That sentence is the whole justification and is the only mechanism-reads-it evidence the field has.

**The generalisation, stated as OWED and not to be smoothed into a rule.** `write-rules.md §1.2`: "**Absent is not unknown when a person would not hesitate - OWED.** §3.5 is the first instance of a pattern that probably generalises… Whether that is one rule or one rule per field is not settled." Carry it as the ADR's stated open edge rather than as a second ADR.

**C39, corrected by zoom.** The inventory says the 08-27 nullability ruling cited the `progress.state` analogy, that analogy flipped on 08-28, and "the two consumers stand unrevisited". **Half of that is now wrong.** `schema.md §1`'s `null` convention at source has been rewritten to use **`grade_share_conditional`** as its canonical example, with `progress` carved out explicitly as "the one deliberate exception, and it is not one of these nulls". So the convention no longer rests on the flipped analogy. What *is* still unrevisited is only the 08-27 **changelog line**, which still reads "the same defect as rendering a null `progress.state` as `not_started`" - a stale sentence in a history, not a live ground. C39 should be downgraded accordingly.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #4 indirectly: the same instinct that makes `progress.state` non-nullable (do not give the agent a reason to ask) is what the write rule applies here from the other direction - do not leave a record saying *unknown* about something obvious.

**Merge candidates.** **M48** - `optional` and `grade_share_conditional` were made nullable in one 08-27 ruling on one ground. That is genuinely the same trade-off made once for two fields, and it is the strongest cross-thing merge in my cluster after M40/M41.

**Cross-cluster.** E (write rules are E's tier; the §1.2 OWED generalisation may belong there).

**Zoomed.** Yes - `schema.md §1`, `§3`, changelog 08-27; `write-rules.md §3.5`, `§1.2`. See C39 above; the zoom materially changed the finding.

---

## M51. `progress` - its carrier, its kind, and its default

**Destination: `ADR`.**

**Proposed title:** *`progress` is an annotation kind with a non-nullable state, defaulted so the agent has no reason to ask.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** The carrier decision determines whether progress has an id, a target link and its own kind tag, or is a row on `obligation`. Three carriers were tried in three days and each move rewrote the field grain. |
| Surprising without context | **Yes, and it is the clearest instance in the corpus.** A prohibition ("null must render as absence, never as `not_started`") that came from a **measured incident** was **reversed** four days later, and four body sites that used that incident as their canonical example were rewritten. A reader finding the incident will think the reversal is the mistake. |
| Result of a real trade-off | **Yes.** A nullable state is honest - the system does not know. It was given up because a nullable state makes the system announce it does not know, which gives an agent a reason to ask *have you started this yet*, and that is the system chasing the agent, which `architecture.md §3` rules a defect in the rule. |

**Body.** `progress` is an **annotation with its own kind**, a sibling of `sticky_note` sharing one shape and distinguished by its `kind` value rather than by a type hierarchy, targeted by an `about` link rather than by a field. Its `state` is a non-nullable enum `not_started | in_progress | done` with **no unknown state**: an obligation with no progress record reads as `not_started`, because that is what a thing nobody has touched is, and nothing needs to be written at creation. A **defined** default is not an invention; what the measured incident recorded was a run inventing a default where none was specified.

**Shape that rides.**

```
progress := kind · id · state · detail · origin · created_at · updated_at
state    : not_started | in_progress | done          NOT nullable.  No unknown state.
detail   : free text - an elaboration of state, illegal without one
target   : an `about` link, not a field

rule                                   enforced at
  detail illegal without state           construction   (both fields on the record)
  one current value per target           the service    (the target is a link; links load later)
  only the owner authors it              nowhere, deliberately (a rule about the caller)
```

**A third structural rule the inventory does not carry.** `schema.md §4.5`: **"no `about` link is legal"**, and means progress on a free topic named in `detail`. That is how `domain-design.md §1` ruling 6 - progress is independent of obligations, a topic inside a chapter can carry progress with no deliverable - survives before the `concept` kind exists. It is load-bearing and it appears in no M-number; see Orphan rulings.

**The enforcement table is the ADR's most transferable content.** "The record had asserted all three were validated at construction." A rule that ranges over more than one record cannot run at construction because a constructor sees one line. This is the same taxonomy F's M106 states from the serialization side, and the two must not diverge.

**A stale sentence that will be re-inherited if nobody says so.** `model.md §8.2` still reads "so `look_at` returns `{summary, annotations[], edges[]}`". `schema.md §4.6` withdrew that triple on 08-28 - it "was not one" (not a return contract), and reading it as complete is what made `obligation.parts` look homeless. `domain-design.md §6.2` separately still reads "fixed by **rendering null as absence**", which is exactly the position `schema.md §4.5` reverses, and `domain-design.md`'s changelog has no 08-28 entry. **Two stale sentences, on the domain side only, on the same thing.**

**Sequencing stripped.** None.

**Touched by Billy's rulings.** **#4 directly, and it is a ruling on this field.** "`progress.state` defaults to `not_started` **precisely so the agent does not keep asking 'how far along are you'**. Proactivity is written too rigidly at present and will bite; design it when needed." That is a confirmation of the 08-28 reversal and a warning about the surrounding proactivity rules, and the ADR should carry both halves - the second is a caution, not a deferral, because there is no precondition attached to it beyond "when it bites".

**Ruling 7's anchor, answering cluster A's question.** A found that "two conflicting statements must never coexist in the system" has no home among the 114 things. **In my cluster its natural anchor is `schema.md §4.5`'s `one current value per target`, enforced at the service** - the only place in the current schema where a store invariant already forbids two statements about one thing coexisting. It is one instance rather than the general rule, so it is an anchor and not a home: the general rule needs a store-invariants section that does not exist, and the shallow/deep partition (resolve-and-report versus ask-first) is a write and interaction rule that belongs with E. The write-side half of it is `write-rules.md §1.1`, which is an orphan - see below.

**Merge candidates.** **M57** (`sticky_note`) - the two annotation kinds share `origin`, both timestamps, target-is-a-link, and the `annotation` tag-not-hierarchy ruling. That shared shape is one decision and reconciliation may want an `annotation` ADR with the two kinds' field tables riding inside. I keep them separate as instructed and flag this as the second-strongest merge in my cluster. **B's M19** - "surface for confirmation, never resolve" is the third of M51's three rules and B counts four things across three clusters stating it; state it once.

**Cross-cluster.** B (M15 - `progress` as a kind must match B's list; M19 - statelessness; M22 - `annotation` is the `about` link's signature endpoint), D (M76 - `look_at`; the §4.6 render table), F (M106 - the same enforcement taxonomy; M111 - the `progress`-as-annotation move is what broke the preferences analogy), A (ruling 7).

**Zoomed.** Yes - `schema.md §4.5`, `§4.6`, `§1`, changelog 08-28; `model.md §8.2`; `domain-design.md §6.2`. **The zoom added the third rule and both stale sentences**; neither is in the inventory.

---

## M52. `status` - the three-axis field

**Destination: `ADR`, carried as a row of the graveyard ADR (M62), not as an ADR of its own.**

**Which rows.** Two: `status.completion · files · score · evaluation`, and the separately reaffirmed `status.evaluation`.

**The removing rulings.** The drop is recorded at `domain-design.md §9.1` + changelog 2026-08-25, **agent - measured, with no ruler**. `schema.md §7` supplies the ruler the drop lacked: "none of these is the system's burden. This does not contradict the finding that a three-axis status prevented two live items being erased; it **moots** it, since nothing is asserted." `status.evaluation` carries its own reaffirmation against a named challenge: *"what do I still owe attention to"* returning A2 and A9 has a hidden premise - that unread feedback is worth attention - and the only authority on that says it is not.

**Why the row is worth more than the field.** *Moots rather than contradicts* is the sharpest move in the graveyard and it generalises: a finding that a field prevented a harm is not refuted by removing the field, if removing it also removes the assertion that caused the harm. Three surveys held three pieces of this - S3 the A2/A9 evidence, S1 the unattributed drop, S2 the ruling - and the graveyard ADR is where the three land as one row.

**What goes in `CONTEXT.md` instead of an ADR.** The do-not-confuse clause: `obligation.status` is dead; `progress.state` is live, non-nullable and in both ring-0 bands. Both corpora use "status" and "state" loosely enough to invite the confusion and **no survey states the distinction**. It rides in the `progress` term's `_Avoid_` line.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine directly.

**Merge candidates.** M62 by construction.

**Cross-cluster.** D (`model.md §4`'s ring-0 list still contains `status` and is stale; `model.md` was edited 08-28 without touching it).

**Zoomed.** Yes - `schema.md §7`, `model.md §8` and `§8.1`. Confirms; `model.md §8`'s vocabulary block still types `status{completion, score, evaluation}` and is stale.

---

## M53. `workload` / `hours_estimate` / `workload-estimate` - one field, three names

**Destination: `ADR`, carried as a row of the graveyard ADR (M62).**

**Which row.** `workload` / `hours_estimate`: "the world does not supply it, it is not a unit anyone thinks in, and its null is not a gap. Size, where it matters, is observed rather than stored."

**The removing ruling.** **Billy, `domain-design.md §6.1`, ruled 2026-08-23**, verbatim: *hours_estimate 很难量化，我一般都是按照某个 assignment 的进度和 high-level 体量来判断的。* Three parts: it is not a field to be filled and its null is not a gap · size is observed ordinally · its missing-rate is retired as a guard signal, with faithfulness as the replacement guard.

**Three independent grounds at three dates, and they should all ride in the row.** Measured absent from every obligation in both courses in every source (08-22) · Billy-ruled retired (08-23) · graveyarded with a standing no-re-add rule (08-27/28). Plus the second independent falsification: Billy's own year-old Notion table has no workload column and *does* have a `target_date` (M46).

**The correction that must travel with the ruling, because the record carries it.** The claim that the third falsification differs *in kind* from the first two - the first two about the world, the third about the user - **does not hold**; the Notion evidence is already user-side. What survives is narrower and sufficient: **asking is only a remedy for a quantity the user can answer, and Billy answers ordinal comparisons, not hour counts.** That correction is what makes the graveyard row proof against "just ask him".

**The names, resolved.** Three names for one dead field: `workload-estimate` (`domain-design.md §6`'s table), `workload` (`§9.1`, `§10.5`, `model.md §8`), `hours_estimate` (`§6.1`). None goes in `CONTEXT.md` - the field does not exist. The graveyard row should list all three so a later reader recognises the field under whichever name they meet it.

**C35, closed by ruling 2.** Same closure as M49: the replacement for the removed ordinal-size mechanism is not a field but an interaction - the agent notices and asks when needed. **M49 and M53 must state this identically**; they are the two ends of one hole.

**C42, and it is worth one line.** `PLAN.md` recorded `workload` as *ruled* on 08-22 ("stated by Billy, nullable, never defaulted") under a do-not-re-litigate heading, one day after Billy deferred it and one day before Billy retired it. Under merge rule 4 it is not discounted for being unattributed; it is discounted for being wrong on content within 24 hours. Recorded as the clearest instance of an agent document promoting a deferral to a ruling.

**22 correction.** Not load-bearing.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** **#2 directly.** "Both hold: `hours_estimate` is not quantifiable, size is judged from progress and load (08-23)."

**Merge candidates.** **M49** - same trade-off (C35), and the two rows should be written together.

**Cross-cluster.** A (the faithfulness guard replaced the missing-rate guard), D (ring 0 carries no size signal of any kind).

**Zoomed.** Yes - `domain-design.md §6` and `§6.1`, `schema.md §7`. Confirms verbatim, including the in-place strike-through of the missing-rate sentence and §6's banner: "**This table is superseded by `spec/schema.md` as the field set** … read it for the rule, never for the fields."

---

## M54. `count{done, of}` and recurring obligations

**Destination: `ADR`, carried as two rows of the graveyard ADR (M62).**

**Which rows.** `count{done, of}` - "one instance in 22 (tutorial attendance, 10 of 12), and it counts attendance-as-score, which the row above covers." And **recurring / countable obligations** - "keeping them out explicitly is preferred to the complexity of representing them."

**The removing ruling.** `schema.md §7`, 2026-08-27/28. **Thirteen of the graveyard's rows have no changelog line and this is one of them**, so the removing ruling is the row's own stated reason and nothing else.

**The row that disqualifies its own evidence, in its own words.** "**Known cost, recorded rather than argued away:** the `n=1` behind not carrying `count` was measured on the two courses least likely to contain recurring items, and 2px3 was excluded throughout." And 2px3 cannot now be read: `architecture.md §4` rules that extracting the other three courses is not worth doing before the presentation tier exists.

**22 correction, and this row is the reason for it.** `architecture.md §4`: the old 22-obligation count "included **a row the graveyard forbids** (recurring tutorial attendance), so **22 is not reachable by re-running the old route**." So the row's own "one instance in 22" quotes a count that this row invalidated. That is not a contradiction - it is a number that has to be dropped from the row's reason, leaving the reason intact.

**The evidence has moved since the row was written, and it is not in any survey.** `evidence/2026-08-28-corpus/2c03/RULINGS-NEEDED.md` R1 puts three decisions on Billy's desk: hold the graveyard (tutorial attendance stays a note, and so does every lab and worksheet) · re-open by ruling · defer and decide with four courses. It records that **this is now a second instance, and 2da4's five labs plus 2px3's weekly worksheets are a third and fourth.** The n=1 the row rests on is no longer n=1. **The row still stands under the no-re-add rule** - only a new ruling lifts it, and none has been made - but the graveyard ADR must not restate "one instance in 22" as though it were current.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #1 indirectly: v1's boundary is coursework inside academics, which keeps the scope small enough that the complexity argument holds. Ruling 1 does not decide R1.

**Merge candidates.** M62 by construction. R1 is a merge candidate with nothing in the 114 - see Orphan rulings.

**Cross-cluster.** F (M102 - the acceptance criterion is where the 22-to-14 correction lives), A (the fixture's standing).

**Zoomed.** Yes - `schema.md §7`, `architecture.md §4`, `evidence/2026-08-28-corpus/2c03/RULINGS-NEEDED.md`. **The zoom changed this thing**: R1 exists, is dated 08-28, is addressed to Billy, and no survey read it.

---

## M55. `label` - is it a name, a summary, or neither

**Destination: `CONTEXT`.**

The third one-field-several-names case, and the one where the loser is the name every early record uses.

**Proposed term.**

- **`name`** - the short label a person recognises a record by, stored exactly as the source prints it. It is not the handle and nothing is derived from it.
  _Avoid_: **`label`** (`model.md §8`'s node line gives it to every node, unqualified; that line is agent-drafted and `model.md §7.1` says so in ruling it out - it "never had standing to block a ruling"), and **description** - the name is short by nature and inconsistent within a course, which is the truth of the data rather than a defect to normalise.

**The clause that makes the term true, and where it lives.** `write-rules.md §3.1`: "**There is no system-owned naming convention, and one is not owed. Write the label the source uses.**" A convention was owed only because the id used to be minted from the name; the id is now opaque and assigned, so nothing downstream depends on how a name is spelled. This is a rule dissolved rather than answered, and it is the cleanest downstream consequence of M40.

**What is not resolved here, deliberately.** Whether the one-line-per-item render is called a `label` or a `summary` is **presentation's first decision** and stays deferred. B's M14 owns `summary` and does not resolve it either; the two term entries together must leave the render's name open. `architecture.md §5` adds the ruling that narrows it: a *summary* is a written object, written only where a node's identity is content the skeleton does not hold - the artifact and nothing else - so an obligation's line is **composed from what it already stores**.

**22 correction.** `model.md §7.1`'s supporting figure "3 of 22 obligations with no artifact at all" is over the dead fixture. The argument survives; the number should not be quoted.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine directly.

**Merge candidates.** **M46**, **M47** (same shape, different trade-offs). **B's M14** is the other half of the deferred naming question and must be written so neither entry closes it.

**Cross-cluster.** B (M14), D (M76 - `look_at` returns a summary), F (M101 - the render may address however it likes, which is why the name carries no load).

**Zoomed.** Yes - `model.md §7.1` and `§7.2`, `write-rules.md §3.1`, `architecture.md §5`, `schema.md §3`, `ring-0.md §4`. Confirms. `architecture.md §5` also carries a **withdrawal** no survey quotes: the older recommendation to compose an obligation summary from `parts` + `due` + `grade_share` is withdrawn, "because it lent the artifact's vocabulary to a kind that has no ingest and so invented a drift problem that does not exist."

---

## M56. What ingest produces, and who reads each part

**Destination: `DEFER`.**

**What is deferred.** What an ingest pass writes onto an artifact node and which reader each part serves: `summary` (concise at birth, read by the coordinator) · `tags` (implies an enum set, **deliberately not settled now**, read by filtering) · `sections + pages` (explicitly not the coordinator's responsibility).

**Precondition that wakes it.** **The `artifact` kind acquires a writer** - that is, an ingest pass exists that produces candidate fields. Concretely: before anything writes `tags`, the enum set has to be settled or declared open, and that is the first decision the pass forces.

**What is settled and must travel with the deferral, so it is not re-litigated.** `domain-design.md §10.2`, Billy 08-22: "**§5 ruled out a *manual* taxonomy, not an LLM pass at ingest.**" Since a multimodal pass must run anyway for scans, `.docx` and `.pptx`, section labels are its byproduct. And "**most of P2's negative findings were artifacts of testing a method nobody had proposed.**"

**What is exposition and does not travel.** P2's extraction figures (slide-shaped 39/40 ≈ 97%, prose-shaped 12/26 ≈ 46%) are measurements of an apparatus, and the record already discounts them from two directions: the 97% is 97% of a single professor's template, and the honest verdict is "the cheap method fails on prose", not "prose extraction fails". S3's residue - P2's pre-registered second stratum never ran and no file records a decision to abandon it, while the derivation's title-scoped 2aa4 extraction was a de-facto second stratum that did work - belongs in the research record, which is where it now is.

**Sequencing stripped.** "Artifact and the whole ingest path are slice 2/3" is the entire reason the spec side is silent on this thing. Dropped; the wake-up above replaces it and is a dependency rather than an order.

**Touched by Billy's rulings.** **#6 directly.** The determinant for what is embedded is the **nature of the RAG store** - it holds semantic, decontextualized facts about course materials - and that governs whether an artifact of any form is embedded, not its file class. That resolves the source-class-versus-linearization axis (C28/E10) at the level *above* this thing and should be quoted in the deferral so the ingest cycle does not re-open it. It is B's M37 and E's M91 that carry the ruling; this deferral cites it.

**Merge candidates.** **B's M14** (`materialized summary` versus `summary` - two objects, one word) and **E's M91** (ingestion). This thing is mostly a pointer into two other clusters and reconciliation may fold it entirely.

**Cross-cluster.** B (M14, M34 - materialization is not retrieval indexing, M37), E (M91).

**Zoomed.** No. The relevant records are silent on the spec side by their own statement, and `model.md §7.2`'s table is quoted in full by S1 with the `UNRESOLVED` banner intact.

---

## M57. `sticky_note` - shape, `category`, `origin`, `body`, timestamps

**Destination: `ADR`.**

**Proposed title:** *A note is an entity that points at a node; `category` is an open string set on purpose, and provenance confers no immutability.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** The target-is-a-link decision is what lets a note hang on a course, an obligation or later a concept without a polymorphic field; unwinding it re-homes every note. The paired timestamps are what make a time-bound statement safe to store at all. |
| Surprising without context | **Yes, twice.** `category` is a **string with an open set** in a schema that otherwise types everything, and the record says the values in use are *not yet a usable vocabulary*. And an announcement-sourced note is **editable** - provenance does not confer immutability - which reverses the intuition and an explicit earlier agent draft. |
| Result of a real trade-off | **Yes.** An enumeration was the obvious move and is declined because the cases cannot be enumerated; the price is that the field stores whatever it is given and its write rule is owed. Append-only for origin-bearing notes was drafted and retracted on a false premise. |

**Body.** A `sticky_note` is an entity that points at a node rather than a property of one, so attach, detach and modify are cheap and symmetric and **maintenance happens at the read**. Its target is an `about` link, not a field. `category` is an open string set, deliberately not an enumeration. `origin` records how the annotation came to exist and **does not confer immutability**: an annotation may be edited, and an edit carries `origin` forward by default. Both `created_at` and `updated_at` are carried, because the pair plus maintenance-at-read is what makes a time-bound statement safe to store at all - an undated sentence from the start of term goes on influencing judgment forever.

**Shape that rides.**

```
sticky_note := kind · id · category · body · origin · created_at · updated_at
category : string, OPEN SET - correction, policy, erratum, ...   write rule OWED
body     : free text - the kind's ONE free-text field
origin   : the SAME field as progress.origin.  One concept, one name, both annotation kinds.
target   : an `about` link, not a field
```

**The refinement that is now the rule.** `domain-design.md §10.7` ruling 2 (Billy, 08-22) had the note attaching to the **section**. A3's 08-22 measurement found seven instances whose targets straddle all three layers, **four of the seven on a concept or an obligation rather than a section** - "refinement, not a contradiction", and the highest-value ones attach to a concept precisely because they reconcile two artifacts that disagree. The polymorphic `about` target is that refinement made structural.

**Two owed write rules, with two different bodies of evidence, and neither record cites the other.** `category` is OWED: `schema.md §4` grounds it on a distribution (across the 11 notes that exist, **one value holds 8** and the boundaries between the others do not reproduce); `write-rules.md §4` grounds it on **two independent passes producing two non-overlapping vocabularies**. `origin` is OWED for a sharper reason: the schema's prose says *how the claim was obtained* and **both passes reached for *what document class it came from***. A reader closing either item wants both grounds. Note that the `origin` gap is a definitional mismatch, not a vocabulary gap, and is the more dangerous of the two.

**The one live inconsistency inside the thing.** `schema.md §4` lists `erratum` among `category`'s example values; `write-rules.md §4.0`'s measured pass discards **every erratum about a handout revision** as the class that most consistently fails the render test. Not formally contradictory - the schema names a legal value, the write rule says when to write one - but the illustrative example should not be the discarded class. One-word fix, worth stating in the ADR so it is not read as a disagreement.

**A clause with no input in the current kind set, stated as such.** The read-time maintenance pass compares a note's date against its target's **revision date**, and that revision date belongs to a kind that does not exist yet. So the mechanism is specified and inert. That is a legal state under the rigidity rule (a reader without a writer is legal; the reverse is not) and it should be said, not discovered.

**Sequencing stripped.** "In slice 1 that comparison has no input" is a dependency, not an order, and is kept.

**Touched by Billy's rulings.** #5 - latent conflicts: the risk is the agent asking repeatedly about small conflicts or persisting them as noise, and "wait until it bites". That is a direct argument against giving `category` an enumeration prematurely, and it should be recorded as a second, later ground for a decision that was made on other grounds. #7 - `origin`'s provenance log is where an announcement that collides with held material is traced.

**Merge candidates.** **M51** - the shared `annotation` shape (`origin`, both timestamps, target-is-a-link, tag-not-hierarchy) is one decision carried by two field tables. Strongest merge candidate after M40/M41; recommend reconciliation consider one `annotation` ADR with both kinds' tables riding inside. **M58** is the *whether-to-write* rule for the same kind and is a different question (existence, not shape) - keep separate.

**Cross-cluster.** B (M22 - `annotation` is the `about` link's signature endpoint; M24 - announcements are `origin` and this is the field), E (M83, M89, M90 - the intake side of `origin`), D (M76).

**Zoomed.** Yes - `schema.md §4`, `write-rules.md §4`, `model.md §8.1`, `domain-design.md §10.7`. Confirms all of it, and `model.md §8.1` adds the two-case staleness table that the maintenance-at-read rule needs to be safe: **evidenced staleness** (a correction note whose target's `revised_at` now post-dates it) may be rewritten or detached in passing; **staleness only Billy can know** must be surfaced for confirmation and never resolved.

---

## M58. What a sticky note is worth writing - the render test

**Destination: `CONTEXT`.**

A rule that is a term, in the same sense as B's `rigidity rule`: a one-sentence test for whether a thing exists at all, invoked by name across records.

**Proposed term.**

- **the render test** - the test for whether a note is worth writing: *is it worth being written down so that every time I look at this node, the note comes with it?* A note is not a place to put things that are true; it is a thing that appears every single time its target is read.
  _Avoid_: **the note rule**, **the usefulness test**, and stating it as *is this true and relevant* - the test is about recurrence at the read, not about truth.

**What the test measurably excludes, which is the fastest way to convey it.** Measured on one course, 20 candidate notes became 12. What failed: course-wide administrative policy (an AI prohibition, a submission-naming convention, the last-day-of-classes rule, the MSAF procedure) · a restatement of what an assignment consists of · **every erratum about a handout revision**, which mattered on the day and never again.

**The companion rule, which belongs in the same entry.** `body` is a concise self-contained summary and never a quotation, **because a note renders inside the node it hangs on**. Short enough to sit in a rendered node, self-contained enough to mean something alone.

**Why this is `CONTEXT` and not `ADR`.** It is hard to reverse in effect but not in mechanism - it is a write rule, and `write-rules.md` exists precisely so a rule can be replaced under its field. What survives any rewrite is the named test, which is invoked by three records. B routed the rigidity rule the same way for the same reason, and the two entries should read as siblings.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #5 indirectly: the test is what stops small conflicts becoming persisted noise, since a note that does not earn its render is never written. #7's report-afterwards half needs a channel that is *not* a note - a resolved shallow conflict that gets written as a note fails this test on the day after.

**⟂container, and it is not cosmetic.** The test is written in the first person about a human reading: "every time **I** look at this node". In the successor container the reader is an agent, and "comes with it every time" has a different cost curve - cheap in tokens per read, expensive in aggregate across a whole projection. The rule's *form* survives; its calibration was set against a human's attention and has never been re-set against an agent's context budget. That is the same calibration question M59 defers.

**Merge candidates.** **M59** - the length bound is the quantitative form of the same question (what a rendered node can carry) and `write-rules.md §4.2` says so: "the bound follows from what a rendered node can carry, not from a number chosen in advance." Same trade-off, one qualitative and one quantitative. Recommend they be reconciled together even though one is a term and one is a deferral.

**Cross-cluster.** E (write rules are E's tier; the capture point is E's M95), B (M26 - the sibling rule-as-term).

**Zoomed.** Yes - `write-rules.md §4.0` and `§4.2`, `schema.md §4`. Confirms verbatim, and confirms the `erratum` collision at M57.

---

## M59. A length bound on notes, and on the second unbounded route

**Destination: `DEFER`.** This is the thing my zoom changed most.

**What is deferred.** The number bounding free text entering the resident skeleton, over **two** routes rather than one: `sticky_note.body`, and the ingest-written summary that `label` names.

**Precondition that wakes it.** The bound is issued **down from affordability**, and its two inputs are named: **what the coordinator can pull for five courses at once**, and **whether the real policy statements survive that budget, checked against the source material rather than against any extraction**. Concretely, it wakes when a presentation or course-level cycle has a rendered level to measure against, which is the same dependency `write-rules.md §4.2` states - the bound follows from what a rendered node can carry, not from a number chosen in advance. Its gate is `domain-design.md §9.2`'s symmetry rule: eight one-line summaries can be pulled for a comparison set, eight paragraphs cannot.

**What the deferral must carry, and this is new.** **Billy ruled on 2026-08-29 that the corpus cannot justify a length bound, and the ruling has not reached the record it invalidates.** `evidence/2026-08-29-course-level/NOTES.md §6`, Billy, verbatim in substance: `records.json` "cannot justify anything about real data, and length least of all. The note bodies are **a subagent's own compressions, produced from the schema's field definitions with no write rule to follow** - `write-rules.md` did not exist when the extraction ran." Second contamination found on checking: `write-rules.md`'s own changelog says its four rules were authored by Billy **as hand edits to that same file**, so it is agent output partly overwritten by Billy and nothing in it says which body is which. The line drawn: **the corpus is evidence about what the material contains; it is not evidence about what a record should look like.**

**Consequences that must be stated in the issue.**

| survives | does not |
|---|---|
| which obligations exist, their `due`, `grade_share`, `optional` - transcription from the real outline | every character count: **871 / 1,010 / 459 / 87-278** |
| which policies the course states (12 late days, two marking schemes, the snow-day credit) | how many notes those policies became, and how long each is |
| that 4 notes hang on the course and 7 on obligations - a placement fact | `parts`' wording and length on every row |

**And it reaches a truth record.** `model.md §10.5`'s `MEASURED 2026-08-28` banner - *"real samples are short is false; the 11 notes run 87 to 278 characters… 871 characters of course-scoped notes ahead of its first obligation row"* - stands `agent - measured` and rests entirely on the withdrawn numbers. Billy: "An unruled agent writing longer than `write-rules.md §4.2`'s worked example does not falsify *real samples are short*; it reports that the agent had no rule. **Correcting that entry is now a deliverable of this cycle, not a side note.**" **I checked `model.md §10.5` at source: the banner is still there, uncorrected.** The deferral issue should carry that correction as its first action item, because otherwise the next reader re-derives the bound from numbers Billy has already withdrawn.

**What survives the withdrawal, and it is the whole shape.** The item covers **two routes**, both corpora agree on that independently, and the number is load-bearing because it gates whether the symmetry rule is affordable. The 08-25 demotion from `[R]` to owed also survives: "No ledger anywhere supports the ruled standing, and every other record has it as *owed*."

**Sequencing stripped.** None; this is a dependency, not an order.

**Touched by Billy's rulings.** #9 indirectly - "when the instrument cannot reflect the ideal case its result is untrustworthy" is the same move as the 08-29 correction, applied to a different instrument. The 08-29 correction is effectively a tenth ruling in the same family and reconciliation should treat it as one.

**Merge candidates.** **M58** - same trade-off, qualitative versus quantitative.

**Cross-cluster.** B (M14 - the `label`/`summary` route is the second unbounded one), D (ring 0's size bound, roughly 55 obligations at five courses), A (the corpus's standing as evidence).

**Zoomed.** Yes - `model.md §10.5`, `schema.md §4`/`§9`, `write-rules.md §4.2`, `evidence/2026-08-29-course-level/NOTES.md` and `measurements.txt`. **The zoom inverted this thing**: the inventory presents the measurement as a two-corpus convergence that strengthens the item; at source it is withdrawn by Billy the day after it was written, and the record still carries it.

---

## M60. `time_point`, and "the current plan"

**Destination: `DEFER`.** Two deferrals in one thing, with two different wake-ups, both supplied by Billy's ruling 3.

**What is deferred, part 1 - `time_point`.** A kind for a moment that is not an obligation: an exam sitting, a review session, a conference are three real instances. It is separate from `obligation` because **only obligations consume the weekly hours**.

**Precondition that wakes it.** **When the time projection is designed.** `time_point` is out because its reader, the calendar projection, is out - **not because nothing reads it**, and the graveyard says so in exactly those words. Ruling 3 restates it and adds that calendar things belong on the calendar. So the wake-up is: a calendar or time surface exists and needs a moment that is not a deadline. This is **the same wake-up as B's M36's companion deferral** and I have worded it to merge; B proposes reconciliation decide whether it is one issue or two, and I would make it one, titled for the time projection, with `time_point` as its field-level consequence.

**What is deferred, part 2 - the plan.** `domain-design.md §9.1` names the projection as **obligations · time-points · the current plan**, and `domain-design.md §9.3` makes plan generation the coordinator's *only substantive work, because it is coordination*. **The plan has no representation anywhere in the corpus**, and `ring-0.md §7` says so and declines to invent one.

**Precondition that wakes it.** Billy's ruling 3, verbatim in substance: **the plan is a real requirement but is not settleable now; it needs its own grilling session and cannot be designed before schema, API and CLI shape settle.** That is the wake-up: schema, API and CLI shape settled, then a dedicated session. **B's M36 carries the same deferral and the same wake-up; I have used the same three conditions in the same order so the two can merge without drift.**

**What must not be lost.** Two of the three entities `domain-design.md §9.1` names as the projection do not exist, and `model.md §7`'s retraction of an agent draft **rests on that entity list** ("§9.1's projection was always `obligations · time-points · plan`, i.e. ring 0"). So a retraction still standing in the domain corpus is grounded on a list that is two-thirds unrepresented. That is not a reason to reopen the retraction; it is a reason the deferral issue should name it, so nobody later reads the equation as evidence that all three exist.

**Sequencing stripped.** "`time_point` is graveyarded to slice 2" is dropped as ordering. What replaces it is the dependency above, which ruling 3 states as a dependency rather than an order.

**A graveyard call I am making.** `time_point` is the **only** row in `schema.md §7` whose reason is deferral rather than removal, and the row says so. **I would not carry it as a graveyard row.** Filing a deferral under a heading that reads "do not re-add without a new ruling" mis-files it: the row's own text ("the type is out because the projection is, not because nothing reads it") contradicts the header it sits under. It belongs in this deferral issue and should be removed from the graveyard table when the graveyard ADR is written. This is the one place I am proposing to *change* the graveyard rather than transcribe it, and it is a judgment call reconciliation may reverse.

**Touched by Billy's rulings.** **#3 directly, both halves.** **#8** - content and time layers must be separate, and modelling "week N" as a node joined by edges is not right; B's M36 carries the graph-side ruling and this carries the field-side consequence.

**Merge candidates.** **B's M36** - same deferral, same wake-up, explicitly. **F's M108** (calendar goes to the calendar) is where "calendar things belong on the calendar" lands as a container fact.

**Cross-cluster.** B (M36), F (M108), D (`ring-0.md §7`).

**Zoomed.** Yes - `schema.md §7`, `ring-0.md §7`, `domain-design.md §9.1`. Confirms, including that `time_point`'s row is the graveyard's one deferral. `evidence/.../RULINGS-NEEDED.md` R3 adds a live instance: the IDEA Conference currently carries an obligation row and may be a `time_point` - "giving it an obligation row is a category error rather than a modelling choice. It was kept as an obligation only because that is the only row-bearing kind available."

---

## M61. `has-more`

**Destination: `DEFER`.**

**What is deferred.** `has-more`'s **shape**: whether it is a boolean, a count, or a set of present link kinds. What it means is settled - whether a `look_at` on this node returns anything beyond what ring 0 already holds - and it is a pure routing field.

**Precondition that wakes it.** **When something writes it**, which requires the read it optimises to exist: concretely, when `look_at` is built and the projection has to say, per row, whether the call is worth making. Its write side is application-tier work and the 08-29 cycle explicitly scoped it out on that ground. Until then it is a declared field with a named reader and no writer, which the schema record says is legal ("a reader without a writer is legal; the reverse is not").

**What must travel.** (a) The motivation, which is measured and holds: **6 of 14 obligations carry an annotation and 8 carry none**, so a `look_at` costs the same call and returns nothing new on more than half the rows. (b) The record's own honesty about it - `ring-0.md §4`'s why-column calls it "the only one here that no record has yet declared." (c) **The counts were wrong once already** (5 and 9, corrected to 6 and 14, "found by the next sitting reading the corpus rather than this record"), and the 08-29 cycle's standing instruction is **re-measure rather than re-cite**.

**Where it sits relative to M59's withdrawal.** These counts survive it. Billy's 08-29 line withdraws *length* measurements taken from an unruled agent's compressions; **6 of 14 is a placement fact**, and the 08-29 table lists placement facts explicitly on the surviving side ("that 4 hang on the course and 7 on obligations - a placement fact"). So `has-more`'s motivation is intact where M59's number is not, and the deferral should say which side of that line it is on.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #9 indirectly - no exposed CLI surface, so the read this field optimises does not exist to be measured against.

**Merge candidates.** None sharing the trade-off. It is a genuinely small, honestly-flagged open item.

**Cross-cluster.** **D owns ring 0 and this field lives in D's projection table.** If D also proposes it, D should own it and C should carry nothing - I claim it only because it is a field and my cluster is fields. Flagged as the most likely duplicate in my set.

**Zoomed.** Yes - `ring-0.md §4` and changelog, `evidence/2026-08-29-course-level/NOTES.md §1` and `§5`. The 08-29 cycle listed `has-more`'s shape as mandate item C and the record it was to produce, `records/spec/course-level.md`, **does not exist on disk**. So mandate items A-E are all still open.

---

## M62. The graveyard itself

**Destination: `ADR`.** The one ADR carrying the whole table.

**Proposed title:** *The graveyard: removed fields, their reasons, and a standing rule against re-adding them.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes** in the sense that matters: the mechanism is the corpus's only standing anti-regression device, and dropping it is unrecoverable - the reasons for sixteen removals exist nowhere else, and for thirteen of them not even in a changelog. |
| Surprising without context | **Yes.** A schema record with a section listing fields that are *not* in it, and a rule forbidding a later session from restoring them, is unusual. It reads as defensive until you know that re-adding a killed field is a thing this corpus has done. |
| Result of a real trade-off | **Yes.** The alternative is silence: delete the field and let the record be smaller. That was rejected because a later session reading an older document restores what it finds there, and the older documents are still in the repo. The price is a table whose arithmetic is now disqualified. |

**Body.** `schema.md §7` lists **sixteen** removals with the reason for each, under a standing rule: *deliberately absent - do not re-add without a new ruling; a later session reading an older document must not restore them.* **The rulings bind; the numbers do not.** Every count in the table is stated over the 22-row fixture or the two-course corpus, both of which `architecture.md §4` (08-28) supersedes and one of which `schema.md`'s own 08-27 changelog calls "a fixture that was rejected as a golden set". A later reader must apply the removals and must never re-derive them from the arithmetic.

**The caveat is the ADR's most important sentence and must not be softened.** This is the single thing a downstream reader most needs to hold: **the graveyard's rulings stand under the no-re-add rule; its evidence base is self-disqualified.** Three rows say so about themselves in their own text - `count`, `recurring obligations`, and `course.offering_term`.

**Two corrections to the inputs, from zoom.** The table has **sixteen** rows, not fifteen; and "thirteen of fifteen carry no changelog line" is over the wrong denominator and should be restated or dropped.

**Sequencing stripped.** None. The graveyard is not a slice statement, with the single exception of `time_point`, which is why I propose removing that row (M60).

**Touched by Billy's rulings.** **#1 directly** - `course.offering_term` and `course.prereq` **stay graveyarded for v1**, which is a fresh ruling on two rows whose stated reasons are respectively falsified and container-bound. See M64 and the graveyard section.

**Merge candidates.** By construction: **M52, M53, M54, M63**, and the graveyard half of **M64** are rows of this ADR. **B's M20** (`present` / `external_ref` / `backing: referenced_only`) and **B's M23** (`supersedes`) are proposed **additions** to the table, and B asks C to record them - I accept both.

**Cross-cluster.** B (M20, M23), F (M102 - the fixture's supersession is F's), A (evidence standing).

**Zoomed.** Yes - `schema.md §7` in full, `architecture.md §4`, `evidence/2026-08-28-corpus/2c03/RULINGS-NEEDED.md`. The row-count correction and R1/R4/R5's live challenges to three rows are all from this zoom.

---

## M63. `obligation.notes`, and the non-overlap rule

**Destination: `ADR`, carried as a row of the graveyard ADR (M62).**

**Which row.** `obligation.notes`.

**The removing ruling.** `schema.md §7`, 08-27/28: not carried **under the non-overlap rule** - "a **negative** definition (*'everything no mechanism reads'*) cannot be non-overlapping, and across the fixture rows it carried **six unlike purposes**. **All free text lives on annotations**, which carry `created_at`/`updated_at` and a maintenance-at-read rule."

**Why this row is more than a row.** It is the mechanism that makes M43's one-free-text-field cap tractable. There is no catch-all field, so free text has exactly one home per kind and one home overall - the annotations - and every one of those homes is dated and maintained at read. Without this removal the cap is nominal, because a `notes` field absorbs everything the cap excludes. The two should be written so each is legible from the other.

**22 correction.** "Six unlike purposes across the 22 fixture rows" - the count of purposes is the load-bearing part and does not depend on the row count; the "22" should be dropped from the sentence.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #7 indirectly: a catch-all free-text field is exactly where two conflicting statements would come to coexist unnoticed, since nothing dates or maintains it.

**Merge candidates.** **M43**'s one-free-text-field convention - same argument, two ends.

**Cross-cluster.** None outward.

**Zoomed.** Yes - `schema.md §7`, `§1`. Confirms.

---

## M64. Fields removed with no stated reason, and one with a homeless requirement

**Destination: `DEFER`.** The graveyard half goes to M62 as rows; the live half is a deferral and is what this entry is for.

**What is deferred.** `domain-design.md §0.6`'s cross-domain requirement: that the academic domain hold **course offering-terms and prerequisite structure**, because that graph gates other domains' decisions. The instance behind it: winter-only mandatory courses ruled out a winter-27 co-op and thereby set the entire recruiting target to summer 27, and no system held the fact "because no home existed for a constraint spanning academics and career." §0.6 is the strongest statement in the domain corpus that this is not a deadline tracker.

**Precondition that wakes it.** **v2, after the system proves useful and genuinely extensible.** v1's boundary is coursework inside academics, so there is no cross-domain surface for offering-term or prereq to serve. It wakes when a cross-domain requirement re-enters. **F's M109 (the PA db relationship) carries this exact wake-up and F says the two should wake together or not at all** - I have used F's wording deliberately so reconciliation can merge them into one v2 deferral rather than two that drift.

**What Billy's ruling 1 changes, and it is not a small thing.** The requirement is **not dead**. The graveyard's stated reason for `offering_term` - "another domain's need, in a domain that does not exist" - is a **container fact**, and the container has changed. Ruling 1 replaces it with a domain reason: the fields stay out for v1 because v1's boundary is coursework, and the requirement is deferred to v2 rather than removed. **The graveyard row must be re-reasoned, not merely carried**, or a later reader will find a container argument standing under a no-re-add rule.

**And the row's other stated reason is falsified at source.** `evidence/2026-08-28-corpus/2c03/RULINGS-NEEDED.md` R4: the graveyard says `prereq` is "null for both courses in the fixture". 2c03's course outline p.1 reads "Prerequisite(s): SFWRENG 2DM3". It is not null. R4's own conclusion is the right one: "The conclusion may still stand on other grounds; **the stated ground does not.**" Ruling 1 supplies the other ground.

**The three carrier fields and where each stands.** `course.offering_term` and `course.prereq` - graveyarded, reasons replaced by ruling 1. `course.manifest` - graveyarded separately and on a measurement that holds ("exactly redundant with the rows - 2c03 lists 15 and has 15, 2aa4 lists 7 and has 7"). So all three carriers are gone and **nothing in either corpus says what now holds offering-term and prereq**. This deferral is that statement.

**A second homeless item R4 surfaces, and it is not §0.6's.** `course` has four fields and **zero** free text by rule, so the outline's instructor, term boundaries, units, antirequisites and required textbook can only reach the system as annotations - and **the term boundaries are load-bearing**, because the last-day-of-classes rule depends on them. That is a live consequence of M43's cap meeting M64's `course` free-text removal, and it has no M-number. Listed under Orphan rulings.

**Sequencing stripped.** None. The deferral is scope-conditioned, not order-conditioned - F says the same about M109 and the two should read alike.

**Touched by Billy's rulings.** **#1 directly and entirely.**

**Merge candidates.** **F's M109** - same ruling, same wake-up, and F flags divergent wording between the two as a reconciliation defect. Recommend one v2 deferral issue.

**Cross-cluster.** F (M109), A (the goal function and why this is not a deadline tracker), B (M16 - `course` as a node is what the fields would hang on).

**Zoomed.** Yes - `domain-design.md §0.6` and `§6`, `schema.md §7`, `evidence/2026-08-28-corpus/2c03/RULINGS-NEEDED.md`. **The zoom changed this thing**: R4 falsifies the row's stated ground at source, and no survey read that file.

---

## M65. Where the reasoning lives - the changelog gap

**Destination: `DROP`.**

**Which kind of drop: exposition.** This is a property of the corpus, not a ruling about the system. It says how to read `records/domain/` and `records/spec/` - "check the changelog for the reasoning" works for the spec records (54 entries across five files, and S2 found every live contradiction from them) and fails for the domain records before 08-25 (11 entries, all 08-25 or 08-28; everything decided 08-21 through 08-24 has its reasoning in in-place banners). It carries no decision, no term and no deferral.

**Why dropping it is safe, and the one condition on that.** The finding's *value* was locating rulings that live only in a changelog, and both have already been re-homed: the ±1-2 week window's resolution to `today-7d .. today+14d` now lives in `ring-0.md §3` as a ruled body statement, and the reason `domain-design.md §6`'s table was flagged rather than rewritten ("rewriting the table is a schema decision and not a migration") is preserved in the research record. The finding has done its work.

**What must not be dropped with it, and it is not a `CONTEXT` or `ADR` item either.** The corpus names its own hazard three times, and the three sentences are the best available statement of the failure mode this whole classification exists to prevent: "Recorded because a plan that predates the split still reads as authority" · "a divergence between two ruled records that nobody had propagated" · "The error: the archive's §14.4 was read as the current state of the question without opening the changelog of the record that owns the field." The 08-29 cycle adds a fourth and the sharpest: **"before treating any list as exhaustive, state what question it was written to answer."** These belong in the repo's working instructions, not in `CONTEXT.md` or an ADR. Flagged for reconciliation as a homeless-but-valuable set, not as a thing I am carrying.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine.

**Merge candidates.** None.

**Cross-cluster.** All. Every cluster is reading a corpus this describes.

**Zoomed.** Yes, incidentally - I read every changelog in `records/spec/` and both in `records/domain/` for other things and the asymmetry is exactly as described.

---

# Terms cluster C owns

Gathered so clusters D and E can classify against them. B's list is upstream of this one and I have not redefined anything B claimed.

## Identity

| term | definition | _Avoid_ |
|---|---|---|
| **id** | An opaque, monotone value assigned by the system from one id space shared by every kind that can be a link endpoint. It says nothing about the record it names, is never reused, and is obtained only by reading it back. | *key* · *slug* · *handle* used for the stored value (a **handle** is what a render carries; the id is what the store holds) · any id derived from a name |
| **course** | A kind, and a node: the unit a term's obligations are owed to. Its id is the supplied course code rather than an assigned one, because the source issues a canonical unique one. | *namespace* · *scope* · treating it as a container rather than a node |

## The annotation kinds

| term | definition | _Avoid_ |
|---|---|---|
| **annotation** | A node kind whose record is a single dated claim about another node, reached by an `about` link rather than by a field. A tag over `sticky_note` and `progress`, not a type hierarchy. | *note* used for both kinds · *metadata* · treating it as a supertype with subtypes |
| **sticky_note** | An annotation carrying one free-text statement about its target, with an open-set `category` and a provenance `origin`. Cheap to attach, modify and detach, because it points at a node rather than being a property of one. | *note* (bare) · *comment* · *correction layer* · *corpus override* (the layer this killed) |
| **progress** | An annotation stating how far along its target's work is, carrying a non-nullable `state` and a prose `detail`. A target with no progress record reads as `not_started`. | *status* (that is `obligation.status`, which is dead) · *completion* · *mastery* (system-inferred mastery is forbidden) · a fifth typed row · a `sticky_note.category` value |
| **origin** | How an annotation came to exist - an announcement, someone saying so, or the system having asked. One field with one name across both annotation kinds; it does not confer immutability. | *source* · *provenance* used for the field name · a second copy of the field per kind |

## Obligation fields

| term | definition | _Avoid_ |
|---|---|---|
| **name** | The short label a person recognises a record by, stored exactly as the source prints it. It is not the handle and nothing is derived from it. | **label** · *title* · *description* |
| **due** | The moment an obligation is anchored to - the deadline for something handed in, the start for a sitting. A date without a time is the **end** of that day, `23:59`. | *deadline* as the field name · *date* · assuming a date-only value is the start of the day |
| **done_by** | The date the owner chose to have an obligation finished by. A stored value always means it was chosen; nothing computes one. | **target_date** · **finished_by** · rendering it as a *start* date |
| **grade_share** | The approximate share of the final course grade an obligation carries, in percent, held for the person to read and never as an input to a computed ranking. | **weight** · **worth_percent** · reading a column of shares as a partition of 100 |
| **parts** | The concepts an obligation's source carries, as raw strings written in canonical singular form, kept only where a concept might recur elsewhere. It carries no size, no status and no score. | *sub-items* · *components* · treating the strings as pointers to concept nodes · using it to judge how much work something is |

## One rule that is a term

| term | definition | _Avoid_ |
|---|---|---|
| **the render test** | The test for whether a note is worth writing: *is it worth being written down so that every time I look at this node, the note comes with it?* A note is not a place to put things that are true; it is a thing that appears every time its target is read. | *the note rule* · *the usefulness test* · stating it as *is this true and relevant* |
| **the graveyard** | The section of the field-set record listing removed fields with the reason each was removed, under a standing rule that no later session restores one without a new ruling. Its rulings bind; its arithmetic does not. | *deprecated fields* · *the exclusion list* · *deliberately absent* used as the section's name in prose |

**13 terms.**

## Terms cluster C depends on but does not claim

- **kind**, **layer**, **obligation**, **artifact**, **concept**, **Ref**, **link**, **summary**, **rigidity rule** - all cluster B. My `annotation`, `course`, `sticky_note` and `progress` are written to fit B's `kind` definition exactly, and `annotation` is written so B's `about` signature (`annotation → any`) holds without change.
- **ring 0**, **coordinator**, **look_at** - cluster D.
- **handle** - unclaimed. F's M101 uses it as the render-side counterpart of `id` ("every read that returns records must return their handles") and no cluster defines it. Either F or D should, or `id`'s `_Avoid_` line will be the only place the distinction is drawn.

## Where I think a cluster B claim needs adjusting

**B's M31, on where "one id space" lives.** B proposes B owns the one-id-space commitment and C owns the id's properties. At source the id space is inside `schema.md §1.1`'s definition of `id` and `Ref` is a §1 convention row that cites it. Recommend **M40 owns it, M31 cites it**. Nothing else in B's list conflicts with mine, and B's `kind` definition already names my four kinds correctly.

---

# The graveyard rows

Sixteen rows at source. Fifteen I would carry, one I would move, and four I would add.

| # | row | removing ruling | carry? |
|---|---|---|---|
| 1 | `workload` / `hours_estimate` | **Billy, `domain-design.md §6.1`, 08-23**, verbatim, with the ordinal-size replacement and the adversarial correction ("asking is only a remedy for a quantity the user can answer"). Reaffirmed by ruling 2, 08-29. | **Yes** |
| 2 | `status.completion` · `files` · `score` · `evaluation` | `schema.md §7`, no changelog line. Drop recorded `domain-design.md §9.1`, 08-25, agent-measured, no ruler; §7 supplies the ruler. The *moots-not-contradicts* clause is the row's whole value. | **Yes** |
| 3 | `count{done, of}` | `schema.md §7`, no changelog line. **Drop the "one instance in 22" figure** - it quotes a count this row invalidated. | **Yes, re-numbered** |
| 4 | `stated_in` / `source_ref` | **No reason given at all.** The only row whose why-column is bare. The no-re-add rule still binds it; nothing says why it binds. | **Yes, flagged** |
| 5 | `obligation.notes` | `schema.md §7` - the non-overlap rule; a negative definition cannot be non-overlapping. All free text lives on annotations. | **Yes** |
| 6 | release dates | `schema.md §7` - "noise". 2 of 9, printed on the acceptance screenshot itself. | **Yes** |
| 7 | per-part weights and per-part scores | `schema.md §7` - measured and knowingly given up: 2aa4 A1 splits `5/2.5/2.5/5`, A2 `3.5/3.5/5.5`; 6 of 9 2c03 assignments are two independently assessed parts. | **Yes** |
| 8 | coarse dates (*"April 2026"*) | `schema.md §7` - "a date that is not fixed is null. The term's largest obligation therefore stores a null `due`." **R5 records that both readings are defensible and the extraction went the other way**; the ruling stands and the challenge should be noted. | **Yes, flagged** |
| 9 | recurring / countable obligations | `schema.md §7`, with its own evidence self-disqualified in the same entry. **R1 now supplies a second, third and fourth instance.** Ruling stands; the n=1 must not be restated. | **Yes, re-reasoned** |
| 10 | `status.evaluation` | `schema.md §7`, reaffirmed against a named challenge, with the hidden premise identified. The strongest-reasoned row in the table. | **Yes** |
| 11 | `course.offering_term` · `course.prereq` | **Both stated reasons fail.** "Null for both courses" is falsified at source (R4: 2c03 states a prereq); "a domain that does not exist" is a container fact and the container changed. **Billy's ruling 1 supplies the replacement:** out for v1 because v1's boundary is coursework, deferred to v2. | **Yes, re-reasoned - this is the row that most needs it** |
| 12 | `course.manifest` | `schema.md §7` - exactly redundant with the rows: 2c03 lists 15 and has 15, 2aa4 lists 7 and has 7. A measurement that still holds. | **Yes** |
| 13 | `course` free-text field | `schema.md §7` - "nothing identifiable would go in it, and such material belongs on a note." **R4 identifies five things that do**: instructor, term boundaries, units, antirequisites, textbook - and term boundaries are load-bearing for the last-day-of-classes rule. The ruling routes them to annotations; the row's reason as written is too strong. | **Yes, re-reasoned** |
| 14 | `term_start` | `schema.md §7` - "one week-relative obligation in 22". **The weakest row in the table**: its whole reason is a count over the dead fixture, and R4 says term boundaries are load-bearing. | **Yes, flagged as the row most likely to need re-opening** |
| 15 | `due_precision` as a separate flag | `schema.md §7` - the distinction lives in `due`'s own type. Clean and self-evidencing. | **Yes** |
| 16 | `time_point` | **Not a removal.** The row's own text: "the type is out because the projection is, not because nothing reads it." A deferral filed under a no-re-add heading. | **No - move it to M60's deferral issue** |

**Four rows I would add, three of them on other clusters' request.**

| row | removing ruling | source |
|---|---|---|
| `present` · `external_ref` · `backing: referenced_only` | Billy `[R]`, `model.md §2` - an artifact does not need a URL or a presence flag; absence is not a field, it is the absence of store content, read as a join. | **B's M20 asks C to record it** |
| `supersedes` (link kind) | `model.md §8` - zero instances across five agents and two courses; three real shapes would be mistyped and a live document hidden; `revised_at` carries revision instead. | **B's M23 asks C to record it** |
| `weighting_scheme` | Billy, 08-23, `model.md §10.9` - rejected as over-built for one concrete weight calculation; nothing in 60 runs compared the two branches, so the ability to compare them is unevidenced. | **M48** |
| the `<course_id>-slug(name)` id scheme | Billy, 08-28, `schema.md §1.1` - a derived id is a bet on reproducing another writer's spelling. | **M40.** A killed *scheme* rather than a field, but re-deriving an id from a name is precisely the regression the no-re-add rule exists to stop, and it is the one this corpus is likeliest to make. |

---

# Orphan rulings

Real material met at source with no M-number in any cluster. Each is load-bearing and each would be lost.

**1. `write-rules.md §1.1` - an inferred value is asked about, not annotated.** Billy-derived, 08-28, authored as hand edits. Verbatim: *"When a source does not state a value and the agent infers one, it **asks the user**. It does not write the inference into a note beside the field."* And the general clause: **"An update is an update. A correction changes the field; it does not accumulate commentary beside it."** Measured instance: an extraction stored a derived final-exam date and attached a note explaining the derivation - wrong shape. **This is the write-side half of Billy's ruling 7** and it is the cleanest existing statement of "two conflicting statements must never coexist in the system". It is in no cluster. It should go somewhere - my recommendation is with E's write rules, since it is a cross-field write rule, not a field.

**2. `schema.md §4.6` - annotations arrive through their own channel.** The one thing §4.6 actually rules: *"a read that returns a node's neighbourhood must deliver `sticky_note` and `progress` **through their own channel**, never as ordinary neighbours - otherwise progress arrives in the edge list as a neighbour whose summary is the word 'in_progress'."* The inventory records §4.6 **only at D's M76, and only its withdrawal** of the `{summary, annotations[], edges[]}` triple. The withdrawal is captured; the ruling that replaced it is not. It is a rule about my two kinds and D's read verb, and either of us could hold it - I would give it to D with M76, cited from M51.

**3. `schema.md §4.5` - a progress record with no `about` link is legal.** *"**no `about` link is legal**, and means progress on a free topic named in `detail`, which is how a topic inside a chapter carries progress with no deliverable attached before concepts exist."* This is the mechanism by which `domain-design.md §1` ruling 6 (progress is independent of obligations) survives into slice 1, and no survey carries it. Folded into M51 above; listed here because if M51 is merged or trimmed it is the clause most likely to fall out.

**4. `evidence/2026-08-28-corpus/2c03/RULINGS-NEEDED.md` - five open field decisions addressed to Billy, dated 08-28, read by no survey.** The file's own framing: *"Five decisions, each with the source quote. **These block the other three courses**, because the same choices will recur there and I do not want to make them four times by default."*

- **R1** - tutorial attendance gets no row and it is 5% of the grade. Three options offered (hold / re-open / defer); **none chosen**. Supplies the second, third and fourth instances that the `count` graveyard row's n=1 lacked. → M54.
- **R2** - **`grade_share` cannot hold a bonus.** 2c03's real shares sum to 100 and the course grants two bonuses that are additive, outside the 100; storing `1` asserts something false and `optional: true` does not carry additive semantics. The file records this as new: *"Four independent spec reviews missed it, because seeing it requires the arithmetic."* → M47. **This is a live schema defect with no home in the 114 things.**
- **R3** - the IDEA Conference may be a `time_point` rather than an obligation, and currently carries an obligation row "only because that is the only row-bearing kind available." → M60.
- **R4** - **`course.prereq`'s graveyard justification is falsified by the source.** 2c03's outline p.1 states a prerequisite; the row says null for both courses. Also: `course`'s zero-free-text rule leaves instructor, term boundaries, units, antirequisites and textbook reachable only as annotations, and **term boundaries are load-bearing** for the last-day-of-classes rule. → M64, M43.
- **R5** - the final exam's date, derived or null. The extraction stored `2026-04-16` derived from an announcement; the graveyard rules the other way by name. "Both readings are defensible." → graveyard row 8.

**5. `evidence/2026-08-29-course-level/NOTES.md §6` - Billy, 2026-08-29: the corpus cannot carry a length bound, and a truth record already leans on it.** Newer than the corpus and same-day as the nine rulings I was given. It withdraws the standing of every character count taken from `records.json`, on two contaminations (the note bodies are an unruled subagent's compressions; the file is agent output partly overwritten by Billy with nothing saying which body is which), draws the line (*"the corpus is evidence about what the material contains; it is not evidence about what a record should look like"*), and names correcting `model.md §10.5`'s `MEASURED 2026-08-28` entry as **a deliverable, not a side note**. **That correction has not been made** - I checked `model.md §10.5` at source and the banner stands. Fully absorbed into M59; listed here because it is a Billy ruling with no M-number and it invalidates a `[measured]` claim that three other clusters may be quoting.

**6. Same file, §5 - four things a later sitting must not inherit without checking.** The ring-0 counts were wrong once already, so re-measure rather than re-cite · `ring-0.md §2`'s routing test is agent-drafted and unmeasured, and says so · `domain-design.md §9.2`'s judgment-change gate is an agent formulation, not separately ruled, and its one run came from an instrument that could not have detected the effect · the corpus is one course, a past term, hand-corrected, and is for judging a surface rather than Billy's data. And §3's guard, which is the sharpest sentence in the whole corpus about how to read it: **"before treating any list as exhaustive, state what question it was written to answer."**

**7. The graveyard has sixteen rows, not fifteen.** Stated in M62; repeated here because four documents carry the wrong number and the derived "thirteen of fifteen" figure travels with it.

**8. `records/spec/course-level.md` does not exist.** The 08-29 design cycle declares it as its product and its mandate items A-E - what the course level renders · the length bound · `has-more`'s shape · which layer applies `due`'s `23:59` · `look_at`'s return shape and where a node's own typed fields arrive - are therefore all still open. Three of the five are things in my cluster (M59, M61, M45). Not a ruling, but the reason three of my deferrals have the wake-up conditions they do.

---

# Summary

**Counts.** `CONTEXT` **4** (M46, M47, M55, M58) · `ADR` **16** (M40, M41, M42, M43, M44, M45, M48, M49, M50, M51, M57, M62, plus M52, M53, M54, M63 carried as rows of M62) · `DEFER` **5** (M56, M59, M60, M61, M64) · `DROP` **1** (M65). Total **26**.

**Graveyard rows.** **16 at source** (not 15). **15 carried**, one moved out (`time_point`, a deferral mis-filed as a removal), **4 proposed additions** (`present`/`external_ref`/`backing`, `supersedes`, `weighting_scheme`, the `<course_id>-slug(name)` id scheme). **Four rows need their stated reason replaced or corrected** rather than transcribed: `count`, `recurring obligations`, `course.offering_term`/`prereq`, `course` free-text - and `term_start` is flagged as the row most likely to need re-opening.

**Terms.** 13 owned, 9 depended-on-but-not-claimed, 1 unclaimed by anyone (`handle`).

**Sequencing stripped, gathered.** Slice claims dropped from M49 ("the concept layer is slice 2"), M56 ("artifact and the whole ingest path are slice 2/3"), M60 ("`time_point` is graveyarded to slice 2"). In each case a dependency replaces the ordering and is stated. **Not stripped, deliberately:** M40's and M41's "scoped to the kinds that exist" - that is a self-limit on a ruling, not an ordering, and stripping it would widen the ruling. **Not stripped, deliberately:** M57's "in slice 1 that comparison has no input" - a stated dependency on a kind that does not exist, which the rigidity rule makes legal and which should be visible.

**Least certain calls.**

1. **M58 (`the render test`) as `CONTEXT` rather than `ADR`.** It is a write rule, which `write-rules.md` exists to make replaceable, so it fails the hard-to-reverse test on mechanism - but it decides whether a whole kind's records exist, which is exactly what the rigidity rule does, and B routed that to `CONTEXT`. I followed B for consistency. A reconciler who thinks 20-notes-to-12 is a trade-off with genuine alternatives has a case for `ADR`.
2. **Moving `time_point` out of the graveyard.** This is the one place I propose changing the table rather than transcribing it. The row's own text contradicts the header it sits under, but the graveyard is a standing anti-regression device and thinning it is exactly the move it exists to prevent. If reconciliation prefers, carry it as a row **with the deferral stated in the row**, and cross-reference M60.
3. **M50 as `ADR`.** The two-layer pattern (nullable schema field, defaulting write rule) is genuinely surprising and was a real choice, but the field is small and the generalisation is explicitly OWED. It could as easily be a `CONTEXT` note on `optional` plus a deferral for §1.2. I chose `ADR` because the *pattern* is what a future kind author needs and it exists in no single record.
4. **M61 (`has-more`) being mine at all.** It is a field, so it is my cluster, but it lives in D's projection table and D may well propose the same deferral. If D proposes it, D should own it.

**Cross-cluster flags, gathered.**

| from | to | what |
|---|---|---|
| M40 | **B (M31)** | Both records claim "one id space". **Recommend M40 owns it, M31 cites it** - at source it is inside `§1.1`'s definition of `id`. B proposed the reverse. |
| M40 | **B (M30)** | Confirmed: nodes get opaque assigned ids, links get a natural key and **no surrogate id**. Deliberate asymmetry, no survey states it. Recommend it be stated in B's M30. |
| M40, M41 | **F (M101)** | F calls M101 "the other half of the opaque id". These are one decision at two tiers; merge candidate. |
| M42 | **B (M15)** | Accepted B's split: C owns the mechanism ADR, B owns the names. |
| M42, M43 | **B (M25), F (M98)** | The **five refactor triggers** should be one ADR, cited by the things that invoke them. B suspects the same; I concur. |
| M43, M47 | **B (M26), A (M10)** | The rigidity rule's **two declared exemptions** live with their fields (`added_at` in M43, `grade_share` in M47). The rule must never be stated without the exemption clause. |
| M45 | D | Which layer applies `due`'s `23:59` is open; one line, not a gate. |
| M49 | **B (M28)** | Confirmed at source: `write-rules.md §3.4`'s recurrence test **is** the concept-granularity ruling, and neither record says so. **C21 should be closed, not carried.** |
| M49, M53 | **A (E2 / C35)** | **Billy's ruling 2 closes C35.** The replacement for the removed ordinal-size mechanism is an interaction (the agent notices and asks), not a field. M49 and M53 must state it identically. This should not travel into reconciliation as an open escalation. |
| M50 | E | `write-rules.md §1.2`'s "absent is not unknown" generalisation is OWED and is a write rule, so it may belong to E. |
| M51 | **B (M19)** | "Surface for confirmation, never resolve" is M51's third rule and appears in four things across three clusters. State it once. |
| M51 | **A (ruling 7)** | The nearest anchor in my cluster is `schema.md §4.5`'s **one current value per target**, enforced at the service - the only existing store invariant forbidding two conflicting statements about one thing. An anchor, not a home. The write-side half is orphan #1. |
| M51 | **F (M106)** | The enforcement taxonomy (construction / service / nowhere) is stated in both `§4.5` and `§8`. **F should carry the serialization ADR; C carries the progress rules.** They must not state the taxonomy differently. |
| M52 | D | `model.md §4`'s ring-0 list still contains `status` and is stale. |
| M55 | **B (M14)** | `label` versus `summary` stays deferred; C owns `name`, B owns `summary`, neither entry closes the render's naming. |
| M56 | **E (M91), B (M37)** | Billy's ruling 6 (the RAG store holds semantic decontextualized facts about course materials) resolves the source-class axis above this thing; the deferral cites it. |
| M59 | **all** | **`model.md §10.5`'s `MEASURED 2026-08-28` entry is withdrawn by Billy on 08-29 and the record still carries it.** Any cluster quoting 87-278 / 871 / 1,010 / 459 is quoting a withdrawn number. |
| M60 | **B (M36)** | Same deferral, same wake-up (ruling 3). Worded to merge; recommend one issue for the time projection with `time_point` as its field consequence. |
| M61 | **D** | Most likely duplicate in my set. If D proposes it, D owns it. |
| M62 | **B (M20, M23)** | Both accepted as graveyard additions. |
| M64 | **F (M109)** | Same v2 wake-up, worded identically per F's request. Recommend one v2 deferral issue, not two. |
| M64 | **A** | `domain-design.md §0.6` is the strongest statement in the corpus of why this is not a deadline tracker; A owns the goal function and should know the requirement is deferred, not dead. |
| orphan 1 | **E** | `write-rules.md §1.1` - an inferred value is asked about, not annotated. No M-number. Ruling 7's write-side half. |
| orphan 2 | **D (M76)** | `schema.md §4.6`'s one ruling - annotations arrive through their own channel. The inventory captured only its withdrawal. |
| orphan 4 | **all** | `RULINGS-NEEDED.md`'s five open decisions, dated 08-28, read by no survey. R2 is a live schema defect; R4 falsifies a graveyard row's stated ground. |
