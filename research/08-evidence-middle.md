# The two middle evidence sittings - 2026-08-26 slice-1-build and 2026-08-27 tier-recut

**What I read, in full and in the original.** `fall26/evidence/README.md` · `fall26/evidence/2026-08-26-slice-1-build/` (`NOTES.md`, `ROUTING.md`, `fixture.json` - three files, not the two the brief predicted) · `fall26/evidence/2026-08-27-tier-recut/` (`NOTES.md`, `PREREGISTRATION.md`, `derivations/README.md`, `derivations/L1-material.md`, `derivations/L2-lifecycle.md`, `derivations/L3-surface.md`, `derivations/L4-invariants.md`).

**The boundary I observed.** To check whether a ruling reached a record I read only `fall26/records/domain/` (`model.md`, `domain-design.md`) and `fall26/records/spec/` (`architecture.md`, `schema.md`, `design.md`, `ring-0.md`, `write-rules.md`), all seven in full. I opened no other evidence directory, no openclaw path, no other repo. **`records/plan/` and `records/archive/` were NOT read** - I listed their filenames only. This matters for every "no record carries it" claim below: several items are cited by `spec/` as parked at `../plan/backlog.md`, and I could not confirm or deny that parking. Where that is the case I say so per item rather than asserting a gap.

**A dangling artifact, recorded first because it frames everything else.** `evidence/2026-08-27-tier-recut/derivations/README.md` ends: *"These are the reports as returned, unedited. The adjudication is in `../ADJUDICATION.md`."* **That file does not exist.** `find` over the whole checkout returns nothing named `ADJUDICATION*`. Across all seven records in `spec/` and `domain/`, the four derivations are cited **exactly once** - `spec/ring-0.md` §5 cites `L3-surface.md` for the missing cross-course read. So roughly ninety derived capabilities and forty-odd stated contradictions were produced by a pre-registered exercise, and one of them has a traceable landing in the two record directories I can see. This is the single largest reservoir of unadjudicated material in the two sittings.

**The three kinds of sentence.** Every item below is tagged `[RULING]`, `[ABANDONED]` or `[MEASURED]`. A derivation's "capability" is by construction an agent's derivation, never a Billy ruling; I tag those `[MEASURED]` where they carry evidence and name them as agent-derived where they do not.

---

## Rulings with no home

Ordered by consequence. "Checked" names the record and section I actually opened.

### R1. `[RULING]` Billy, 2026-08-26 - the re-transcription is not a golden set

**Verbatim**, `evidence/2026-08-26-slice-1-build/NOTES.md` §Cycle 2 Rulings: *"那些只能作为 dated fixture 怎么 map 到现在的 fixture 上，而不能说这个 fixture 就是完全合规完全正确的."* The sitting's own gloss: *"Cycle 1's a1-a5 verdicts stand for what they measured - conformance of the output to the field set - and none of them was ever evidence of fidelity to the material."*

**Attribution:** Billy, tagged `[ruled]` in the source. **Date:** 2026-08-26.

**Checked:** `spec/schema.md` §6 and its full changelog (which the ruling's own "Touches" line names) · `spec/design.md` §1 F5 and §7 · `spec/architecture.md` §4. **Not carried as a ruling anywhere.** The nearest thing is `spec/schema.md`'s 2026-08-27 changelog line dropping the `optional` tally, whose stated reason includes *"counted a fixture that was rejected as a golden set"* - which presupposes R1 without ever stating it. `spec/architecture.md` §4 (amended 2026-08-28) says *"The 22 came from a transcription that has since been superseded"*, again presupposing it. **A reader of `records/` can find two consequences of this ruling and not the ruling.** Given that `evidence/2026-08-26-slice-1-build/fixture.json` is still named as provenance by a plan record, the ruling that it is not a correctness claim is load-bearing.

**Destination:** `docs/adr/`. Hard to reverse (it voided a completed five-criterion PASS), surprising without context (the fixture reads as authoritative and its own header asserts compliance), and a real trade-off (the alternative was patching Cycle 1).

### R2. `[RULING]` Billy, 2026-08-26 - write rules come before the build, and the build-mode signal rule

**Verbatim**, same file, §Cycle 2 Rulings: *"verb 的 docstring / param def. 什么的都要按照 write 规则设计，这是 agent 直接会看到的."*

**Attribution:** Billy, tagged `[ruled]`. **Date:** 2026-08-26.

**Checked:** `spec/architecture.md` §4, which carries **only the re-targeting**: *"The 2026-08-26 ruling that write rules precede the build still holds and its target changed: they precede the presentation tier, not the application tier."* The ruling is referenced but never quoted, and its **ground** - that a docstring and a parameter definition are what an agent sees directly, so they are design and not documentation - appears in no record I read. `spec/write-rules.md`'s header states the tier and the direction rules are derived from, not this.

**A second, sharper form was measured beside it and has no home at all.** `[MEASURED]`, same section: `plan/slice-1.md` §6 expectation 7 read *"(c) passes at >= 80% without any docstring being rewritten between runs. Falsified below 80%, and any mid-test rewrite voids the arm."* The consequence drawn: drafting `land()`'s docstring over an undefined `parts` / `category` / `origin`, running (c), then rewriting when the write rules land, **destroys the arm rather than requiring a re-run**. This makes the ordering ruling a claim about a voided experiment rather than about elegance. `land()` has since left the first build (`spec/architecture.md` §7) and `plan/slice-1.md` is archived, so the specific instance is dead - but the general form, *a description rewritten mid-arm voids the arm*, is a live constraint on any future verb-routing evaluation, and `spec/architecture.md` §4 names exactly such an evaluation as still owed to presentation.

**Destination:** `docs/adr/` for the ruling. Deferral for the voids-the-arm constraint, precondition: the first presentation-tier evaluation being designed.

### R3. `[RULING]` Billy, 2026-08-27 - derivation is top-down, construction is bottom-up

**Near-verbatim**, `evidence/2026-08-27-tier-recut/NOTES.md` §"The frame was corrected four times", correction 2. Billy asked *"how we would know the method set is complete and that the tier above will find what it needs, and whether the design should be reverse-derived from interaction requirements."* Answer adopted: **derivation is top-down, construction is bottom-up**, with the coverage table derived by two mechanical routes and unioned. The boundary that keeps it honest: **"interaction requirements decide which capabilities must exist, never what a method looks like."** The discriminating test: **"if the method changes when the surface changes, the surface has leaked down."**

**Attribution:** Billy asked the question, the answer was adopted in the sitting; the source does not tag it `[R]`, so treat the method as agent-drafted under a Billy question. **Date:** 2026-08-27.

**Checked:** `spec/architecture.md` §1, which carries the adjacent rule *"A tier is designed against the tier below it, and that tier must already exist"* - **the opposite direction, and not the same claim**. §1 says construction order; R3 says derivation order, and the two together are the actual method. `spec/architecture.md` §7 and `spec/design.md` §3.4 carry the re-homing this method produced, not the method. **The discriminating test appears nowhere**, and it is the operative part: it is what identified `look_at` and `land`+`Diff` as leaked. Anyone re-doing that classification without it has no test.

**Destination:** `docs/adr/`. It is the reasoning that produced the whole re-cut and is currently recoverable only from evidence.

### R4. `[RULING]` Billy, 2026-08-27 - the objection is to a surface shape, not a transport

**Near-verbatim**, same file, correction 4: Billy argued for a CLI over MCP tools. **One of his premises was wrong and was corrected in the sitting** - an MCP tool result can carry rendered text, not only JSON - *"and correcting it sharpened the conclusion: the objection is to N single-purpose description-routed verbs, which is a surface shape, not a transport."*

**Checked:** `spec/architecture.md` §5, which **does** carry the conclusion (*"What is rejected is a shape, not a protocol"*, and the one-tool-with-a-command-string counterexample). **The conclusion landed; the correction did not.** What is absent from every record is that the CLI ruling survived its own author's premise being falsified. That is exactly the class of thing `evidence/README.md` says these directories exist to hold, and it is also the strongest available answer to a future reader who re-opens the CLI decision by re-asserting the JSON premise.

**Destination:** Not carried as a separate item; it belongs as one clause inside whatever ADR records the surface decision. Flagged because it is the highest-value non-obvious sentence in the sitting.

### R5. `[RULING]` Billy, 2026-08-27 - "OOP native" is the wrong label for the language requirement

**Verbatim**, same file, correction 3: *"Also corrected: 'OOP native' is the wrong label for the requirement, since `design.md` §3.7 spends a whole section rejecting inheritance. The requirement is algebraic data types plus exhaustiveness plus enforceable module boundaries."*

**Checked:** `spec/architecture.md` §6, which argues from *"a compiler that can refuse"*, names the discriminated union and its exhaustiveness check, and prices Rust and Go. **It never states the requirement in the three-part form**, and it never records that the requirement was first mis-stated as OOP-nativeness. The three-part form is the thing a future language re-opening would need; §6's prose reconstructs it each time.

Also unlanded from the same correction: the agent's **two self-named counts against its own first recommendation** - it treated `fall26/ingest.py` (a script, in no tier) as architectural evidence, and it never checked the design's enforcement claims against the language's enforcement capability. `spec/architecture.md`'s changelog records the reversal and its ground, not the two errors.

**Destination:** the three-part requirement to `docs/adr/` as part of the language decision. The two errors: **not carried** (process, correctly evidence-only).

### R6. `[RULING]` Billy, 2026-08-26 - the write rules go to a separate session, and what independence means

`[intuition - Billy's, and this session's recommendation sharpens it]`, `evidence/2026-08-26-slice-1-build/NOTES.md` §Cycle 2 Rulings. The sharpening: *"the independence that is worth having is independence from this session's analysis, not from the material - a cold session cannot derive birth rules, and a session given this session's findings inherits its framing."*

**Checked:** `spec/write-rules.md` header, which states a **different and later** method: *"These came from Billy editing one course's extracted records by hand: the rule is what he did, and the before-and-after is the evidence,"* and it names the abstract mandate as frozen. So the seal mechanism is superseded in outcome. **What has no home is the principle** - independence-from-analysis rather than independence-from-material - which is a reusable rule about how to brief a blind agent, and which the tier-recut sitting then applied again (`derivations/README.md`: four subagents *"blind to each other and blind to `records/plan/application-tier.md` and `STATUS.md`"*, with predictions pre-registered).

**Destination:** `docs/adr/`, as one decision covering the blind-derivation method: what a blind agent is withheld, and why the withholding is scoped to analysis rather than to material.

### R7. `[MEASURED]` The pre-registration rule for reading a blind exercise

`evidence/2026-08-27-tier-recut/PREREGISTRATION.md` §"The rule for reading this afterwards": *"A predicted item that is found does not count as the exercise working; it counts as the table having a known hole I had not fixed. The exercise works if items not on this list appear."* And §"What I expect to be wrong about": *"That the yield concentrates in L2 and L4. If L1 or L3 produces the most, my model of where prose-derived coverage fails is wrong, and that is worth more than the individual findings."*

**Checked:** no record in `spec/` or `domain/` states a method for reading a blind derivation. Not found.

**Note on standing:** the prediction was **not scored**, because the adjudication does not exist. Reading L1 and L3 against the twelve predicted items, my own count is that the great majority of both files' findings are unpredicted - which under the file's own rule is the exercise working and the lead's stated expectation being wrong. **I am not adjudicating this**; I record that the scoring is owed and that the material to do it is complete.

**Destination:** `docs/adr/` for the method. The scoring itself: an open question below.

### R8. `[RULING]` Billy, 2026-08-26 - `origin` carries a provenance category, never a page cite

`[agent-drafted]`, `evidence/2026-08-26-slice-1-build/NOTES.md` §Cycle 1 Rulings, and it is the origin of the whole `origin` vocabulary problem: *"A page reference in `origin` would re-add graveyarded `source_ref` through the annotation."*

**Attribution:** agent, not Billy.

**Checked:** `spec/schema.md` §4, which defines `origin` as *"How this annotation came to exist - an announcement, someone saying so (`stated`), or the system having asked (`asked`)"* - the **incompatible** vocabulary. `spec/write-rules.md` §4 marks `origin` **OWED** and states the collision precisely: *"the schema's prose says how the claim was obtained; both passes reached for what document class it came from."* So the collision is booked as owed. **What is not carried is the reason the second vocabulary exists**: it was a deliberate choice made to keep a graveyarded field from re-entering through free text. A write-rule author reading `write-rules.md` §4 alone would see two passes drifting, not a ruled constraint the document-class vocabulary was satisfying.

**Destination:** the constraint belongs in `docs/adr/` or as a line under the owed `origin` rule: whatever `origin`'s vocabulary becomes, it may not carry a locator, because that re-admits `source_ref`.

### R9. `[RULING]` Billy, 2026-08-26 - the transcription's output is candidate facts, not a store

`[agent-drafted]`, same section: *"no node carries `added_at` and no annotation carries `created_at`/`updated_at`. `land()` assigns them; a transcription that stamped them would be fabricating the moment material entered a system that does not exist yet."*

**Checked:** `spec/schema.md` §1 conventions (which now says `added_at` on `course` and `obligation`, and `created_at`/`updated_at` on the annotation kinds) and its 2026-08-28 changelog. **The candidate-versus-record distinction is nowhere in `spec/`,** and `land()` - the only stated assigner - has been removed from the first build by `spec/architecture.md` §7 **with no replacement named**. This is `L1-material.md` capability 9 word for word: *"the only stated assigner of the four required timestamps has been removed from the build, and no replacement is named."* Two independent derivations reached it. `schema.md` §8's changelog discusses lazy construction and a load-time pass parked at `plan/backlog.md`; whether the timestamp assigner is parked there too, I could not check.

**Destination:** `CONTEXT.md` for the term **candidate fact** - a fact extracted but not yet landed, carrying no system timestamps. It is project-specific, it is one sentence, and `spec/design.md` §3.6 already uses the phrase without defining it.

---

## Voids, corrections and withdrawals

**Seven records still stand uncorrected against something in these two sittings or against a ruling one of them produced. Each is quoted on both sides.**

### V1. `domain/domain-design.md` header banner - LIVE, and it is a banner

**The record says**, line 3, the standing conditions banner: *"**conditions:** §9.1's projection grain is dead and **no replacement is ruled**; §6's fact-type table lists six graveyarded fields and is superseded by `spec/schema.md`."*

**The same record's own body and changelog say otherwise.** §9.1: *"**The replacement lives at [`spec/ring-0.md`](../spec/ring-0.md)** - the membership test, the two bands and the field set are there, not here."* Changelog, 2026-08-28: *"**§9.1's dead grain has a replacement, and it is not here.**"*

**Status: still uncorrected today.** The banner is the first thing a reader of that record sees and it is the wrong half of a fact the record itself corrected in the same edit. The vacuum it announces is exactly what `L3-surface.md` gap 5 named - *"The first level's field grain is unruled, and both records that used to carry one say so"* - and `ring-0.md`'s own header cites §9.1's vacuum as its reason for existing. So the fix landed and the banner announcing the hole did not move.

### V2. `domain/model.md` §8.3 versus `spec/schema.md` §3 - the date convention, LIVE

**`model.md` §8.3 says**, under a PROMOTED banner that carries standing: *"Normalised to end-of-day. ... A date without a time needs an explicit convention **at the schema level, not at the parser's discretion**."*

**`spec/schema.md` §3 says:** *"A `Date` resolves to `23:59` **at read time**; **which surface applies that resolution is presentation tier**, and the stored value is always returned raw."*

**Both derivations found it independently.** `L1-material.md`, Contradictions: *"two records give opposite instructions, and the data followed the loser"* - the 2026-08-26 fixture holds ten rows normalised at write, so `2c03-a1`'s `T23:59` is byte-identical to `2c03-midterm-1`'s genuinely stated `T10:30`, destroying the `Date | DateTime` distinction in the only real dataset. `L4-invariants.md` capability 11 states it as a tier disagreement and adds the sting: *"`schema.md` §3 relocates its application to presentation, and `architecture.md` §5 anticipates two surfaces"* - which is per-surface discretion under a different name, the precise thing §8.3 forbids.

**Status: `model.md` §8.3 is uncorrected.** Its changelog has no entry touching it. `schema.md`'s 2026-08-27 changelog restores the number `23:59` and says *"Where the resolution is applied is presentation tier"* without noting that it is overturning a promoted `model.md` passage. **A record that carries a standing banner and is wrong is the worst case in this pass.**

### V3. `domain/model.md` §10.9 versus `spec/schema.md` §3 - the pointer to the rule, LIVE

**`model.md` §10.9 says**, marked `[R]` Billy: *"`worth_percent` keeps its value and gains a `conditional` marker **plus a pointer to the rule**, so no reader can take the stored number for a stated fact."*

**`spec/schema.md` §3 says:** *"The rule **may optionally** be left on a one-line sticky note; **requiring one is not a rule**, because a schema rule that manufactures a conflict nobody would care about is a defect in the rule."* Changelog, 2026-08-27, Billy, ruled.

**`L1-material.md` capability 5 states the operational cost:** three obligations carry `grade_share_conditional: true` and the rule lives in a note whose only link is to the **course**, so *"An agent holding `2c03-midterm-2` sees `conditional: true` and must scan every note on the course to find out conditional on what."* Its Contradictions entry adds that the pointer *"was dropped without a changelog entry"* on the `model.md` side.

**Status: uncorrected.** Two Billy rulings, five days apart, in opposite directions, with the older one carrying `[R]` and no supersession marker. Billy's 2026-08-30 ruling 7 - *two conflicting statements must never coexist in the system* - is a rule about the system's data, and this is the same defect one level up, in its records.

### V4. `domain/domain-design.md` §6.1 item 2 versus the 2026-08-27 `parts` ruling - LIVE

**`domain-design.md` §6.1 says**, under `[R]` Billy 2026-08-23: *"**Size is observed ordinally** - from `parts` and item notes first, then by asking for a relative comparison."*

**`spec/schema.md`'s 2026-08-27 changelog says**, Billy, ruled: *"**`parts` carries concepts only; the ordinal size-judgment reader is not designed.** It is deferred until a size-judgment need actually arises."* `spec/write-rules.md` §3.4: *"**`parts` carries concepts, and it does not carry size.**"* `spec/ring-0.md` §4 excludes `parts` from the projection partly on that ground.

**This is directly attributable to my sittings.** `evidence/2026-08-26-slice-1-build/NOTES.md` §Cycle 2 Rulings is where the two-position question was sharpened - `[intuition - Billy's, and it diverges from the record]`, Billy 2026-08-26: *"很明显的是 parts 应该承载的是概念"* - and `evidence/2026-08-27-tier-recut/NOTES.md` §Handoff of the prior sitting records the answer: *"**`obligation.parts` carries concepts** - ruled 2026-08-27."*

**Status: `domain-design.md` §6.1 is uncorrected**, and it still names `parts` as the first input to a size judgment. **Billy's 2026-08-30 ruling 2 settles the substance** - size is judged from progress and load, not from `parts` and not from `hours_estimate` - so what is owed is the propagation, not a decision.

### V5. `domain/domain-design.md` §6.2 versus `spec/schema.md` §4.5 - null-as-absence, LIVE

**`domain-design.md` §6.2 says:** *"The earlier demotion to a sticky-note kind rested on *the ordinal invited invention* and *no mechanism reads progress at all*. The first is a **defaulting** fault, **fixed by rendering null as absence**."*

**`spec/schema.md` §4.5 says** `progress.state` is *"**not nullable**"* and *"An obligation with no progress record reads as `not_started`."* `domain/model.md`'s changelog, 2026-08-28, Billy, ruled: *"§8.2's fix for the *ordinal invited invention* fault is restated: the fault is fixed by a **DEFINED default**, not by rendering absence."*

**Status: `model.md` §8.2 was corrected on 2026-08-28; `domain-design.md` §6.2 carries the identical sentence and was not.** One of two twinned passages moved. **Billy's 2026-08-30 ruling 4 rests on the corrected version** - *`progress.state` defaults to `not_started` precisely so the agent does not keep asking* - so the uncorrected record now contradicts a live ruling.

**`L4-invariants.md` capability 10 predates the fix and is worth keeping for its residue:** null-as-absence was *"stated in an application-tier record"* while *"the act it constrains is rendering"*, with **no presentation record existing**. That half is still true of every other null in the field set.

### V6. `spec/design.md` §1 Constraints versus `spec/architecture.md` §6 - the language, LIVE

**`design.md` §1 says:** *"**Constraints** - **directly-callable Python**, no MCP, no Postgres, no `PA_SOURCE`."*

**`architecture.md` §6 says:** *"**TypeScript**, and the tiers are directories under one source root ... **Python cannot refuse**: any module may import any other, so the purity cut degrades into discipline."*

**Status: uncorrected.** `design.md`'s changelog records the 2026-08-27 re-scoping and the 2026-08-28 `Ref` change and never touches §1. The language reversal is exactly the tier-recut sitting's third frame correction (`evidence/2026-08-27-tier-recut/NOTES.md`), and `design.md` is the record `architecture.md` §2 assigns to the application and persistence tiers - so the record that owns the tiers being built still names the language ruled against.

### V7. `spec/design.md` §1 F5 versus `spec/architecture.md` §4 - the 22 obligations, LIVE

**`design.md` §1 F5 says:** *"Ring 0 holds **all 22 real obligations** with no free-text escape hatch."*

**`architecture.md` §4 says**, changelog 2026-08-28, Billy, ruled: *"§4's criterion is amended from **22 obligations across two courses to one course's real obligations**. The 22 came from a superseded transcription and **included a graveyarded recurring row**; a fresh extraction found 14 in one course."*

**Status: uncorrected**, and F5 is a numbered functional requirement, which is the form most likely to be read as a target. The 22 is my sittings' number: `evidence/2026-08-26-slice-1-build/ROUTING.md` §Counts, *"obligations | 22 - 15 `2c03`, 7 `2aa4`"*, and the graveyarded row is `2c03-tutorial-attendance`, which that sheet routes in detail while `spec/schema.md` §7 graveyards *"recurring / countable obligations (weekly labs, quizzes, tutorial participation)"*. **So the fixture that both sittings built on contains a row the graveyard forbids, and neither sitting noticed.**

### V8. `spec/design.md` §3.7 versus `spec/schema.md` §4.6 - the `look_at` triple, LIVE

**`design.md` §3.7 says:** *"`look_at(node_id, question) -> { summary, annotations[], edges[] }`, each annotation carrying its kind."*

**`schema.md` §4.6 was corrected on 2026-08-28** precisely to stop quoting that triple: *"the `{ summary, annotations[], edges[] }` it used to quote was not one [a return contract] ... read as complete, it makes `obligation.parts` look homeless when the field is simply returned by whatever reads the obligation."* And `architecture.md` §7 re-homed `look_at` to presentation on 2026-08-27.

**Status: uncorrected in `design.md`, and in `domain/model.md` §7.1 as well**, which carries the same signature in a fuller form (`{ summary, sticky_notes[], edges: [...] }`) under a PROMOTED banner. `L3-surface.md` gap 8 named this before the `schema.md` fix: *"`look_at`'s contract is written into an application-tier record after being re-homed to presentation."* One of the three sites was fixed. Two remain, one of them banner-protected.

### Not a void, recorded so it is not mistaken for one

`spec/architecture.md` §5's composed-summary recommendation was **withdrawn** on 2026-08-28 (*"it lent the artifact's vocabulary to a kind that has no ingest and so invented a drift problem that does not exist"*). That withdrawal moots `L1-material.md` capability 15 and Contradiction *"`architecture.md` §5's composed summary and the field set disagree about what exists"*, and it moots `L3-surface.md` gaps 9 and 10 in their stated form. **`domain/model.md` §4.1's banner - *"What a Node summary is for - NOT RULED ... Nothing in this subsection is settled"* - remains correct** for the Node summary as a written object, because `model.md` §7.1's 2026-08-28 ruling settles only where a summary is written (the artifact, and nothing else), not what a good one contains.

---

## What the tier re-cut moved

Source: `evidence/2026-08-27-tier-recut/NOTES.md` §The mandate and §"The frame was corrected four times". The landed form is `spec/architecture.md` §7 and its 2026-08-27 changelog line; `spec/design.md` §3.4 is marked in place rather than deleted.

| before the re-cut | after | amended to match? |
|---|---|---|
| `get(ref)` - a slice-1 skeleton operation, `design.md` §3.4 | **persistence**, fetch by key | Yes - `architecture.md` §7 table; `design.md` §3.4 carries an in-place banner |
| `links(ref, link_kind?, direction?)` | **persistence**, a scan of the adjacency index | Yes, same two places |
| `nodes(kind, course?)` | **not one operation** - two service reads, `courses.list()` and `obligations.list(course)` | Yes, same two places |
| `closure`, `nodes_without` | application, **slice 2** | Yes |
| `look_at(node, question)` | **presentation** - a composed view | Partly. `architecture.md` §7 and `design.md` §3.4's banner say so; **`design.md` §3.7 and `model.md` §7.1 still specify its return shape** (V8) |
| `land(candidates) -> Diff` | application but **not a primitive**; a batch composition over CRUD; `Diff`'s conflict question is a **presentation** adjudication; **not in the first build** | Yes in `architecture.md` §7/§4. **But nothing replaces what it assigned** - see R9 and the F2 item below |
| the application tier's contents = a graph-generic operation list | **CRUD at field grain, per kind**, translating `schema.md` §1's *every field is individually CRUD-able* into a method set for the first time | Yes - `architecture.md` §7 |
| write rules precede **the build** (2026-08-26, R2) | write rules precede **the surface**; three of the four owed fields are presentation tier | Yes - `architecture.md` §4; `spec/write-rules.md` exists as a presentation-tier record |
| Python, *"directly-callable Python, no MCP"* | **TypeScript**, tiers as directories under one source root (packaging reversed again 2026-08-28) | `architecture.md` §6 yes. **`design.md` §1 still says Python** (V6) |
| N single-purpose description-routed verbs | **one composable grammar with progressive disclosure**; the surface is a CLI; an agent-protocol adapter is at most a thin shell | Yes - `architecture.md` §5 |
| `records/plan/slice-1.md` §4.2 as the next build step | **void**; that record frozen to `records/archive/` | Confirmed by filename: `records/archive/slice-1-plan-2026-08-27.md` |
| acceptance: 22 obligations across two courses | one course's real obligations (14), amended 2026-08-28 | `architecture.md` §4 yes. **`design.md` §1 F5 still says 22** (V7) |
| `design.md` §4's *"nothing in slice 1 is blocked by label-versus-summary"* | **withdrawn** - a navigational surface renders a line at every level | Yes, and it is the one finding the sitting names as validating its method: *"That was the first trace attempted"* |

**Two things the re-cut moved that no record states as a move.**

**(a) `schema.md` §1's *every field is individually CRUD-able* was a dead clause for the whole prior design.** `evidence/2026-08-27-tier-recut/NOTES.md` correction 1: *"the recognition that `schema.md` §1's clause every field is individually CRUD-able **had never been translated into a method set**."* `architecture.md` §7 states the conclusion; the finding that the clause sat unread through three cycles is only in evidence, and it is the diagnosis, not the fix.

**(b) The named error class.** Same file: *"**The agent's actual error, named:** it took an operation list written *before* the three-tier split existed as the tier's contents. `design.md`'s own header says its bounded question predates `architecture.md`. **A frozen artifact's vocabulary set the plan's units.**" That error class recurs across this corpus - it is the same shape as V6, V7 and V8, where a record frozen before a ruling still supplies vocabulary. No record states it.

**Destination for (b):** `docs/adr/` is wrong (it is not a decision). **`CONTEXT.md` is the fit if a term is wanted**; otherwise it belongs as a one-line rule in the repo's own working instructions, which is outside this pass's four destinations. Flagged rather than proposed.

---

## Records still speaking in pre-re-cut terms

Distinct from the voids above: these are records whose **frame** predates the re-cut, where the defect is not one wrong sentence.

1. **`domain/model.md` §7.1, the `question` parameter.** *"the parameter is **required** so it is enforced **at the tool surface** rather than requested in a prompt"*, `[R]` Billy 2026-08-23. The tool surface is gone: `architecture.md` §5 rules a CLI grammar and demotes an agent-protocol adapter to "may never be built". `L3-surface.md` gap 11 states it exactly: *"The `question` parameter did not survive the shape change and nobody re-homed it ... a level-based grammar has no obvious slot for it, and its retirement condition is defined in terms of `look_at` call statistics that grammar does not produce."* **Uncorrected.** Its retirement condition lives in `model.md` §4.1 and is stated in `look_at` call percentages, so the condition is now unmeasurable by construction. **Billy's 2026-08-30 ruling 9 puts the whole surface behind the hypothesis gate**, which makes this dormant rather than urgent - but it is a `[R]` ruling whose enforcement point no longer exists.

2. **`domain/model.md` §4.1's retirement threshold** - *"across one full three-run arm, >= 80% of `look_at` calls have their stated question answered"*. Same defect, same cause. Also interacts with R2's voids-the-arm constraint: the threshold is an arm.

3. **`spec/design.md` §5 and `spec/ring-0.md` §1, residency.** `L3-surface.md` gap 12: *"'Resident' has no referent under a CLI. Every passage keyed to 'ring 0's resident projection' describes an execution model the CLI does not have, and the two records disagree without noticing."* `L4-invariants.md` goes further, listing **the coordinator invariants as a class** - residency, the symmetry rule, expansions discarded not sedimented, disposability - all four constraining *a long-running process*, against `architecture.md` §5's CLI and `design.md` §5's *"every call may be a new process"*: *"the invariants either became vacuous or moved to an unwritten presentation record, and no record says which."* **Partly addressed and honestly so:** `ring-0.md` §7 (2026-08-28) names the tension in its own terms - *"the missing term is that ring 0 is resident for the coordinator and for nobody else - a person at the surface holds nothing"* - and books it as the presentation cycle's question. `design.md` §5 still asserts *"the load is cheap enough that per-invocation and resident are indistinguishable"* without reconciling the four invariants. **The class-level question is unanswered in any record I read.**

4. **`domain/domain-design.md` §0.6, offering-term and prereq.** *"the academic domain **must** hold course offering-terms and prerequisite structure, since that graph gates other domains' decisions. This is **the single most concrete design input** carried in the originating dispatch."* `schema.md` §7 graveyards both. `L2-lifecycle.md` states it as a contradiction: *"`schema.md` §7 graveyards both **on a fixture-null argument that does not answer §0.6's reader**."* **Billy's 2026-08-30 ruling 1 resolves it** - graveyarded for v1, cross-domain requirement **deferred to v2, not dead**. So the substance is settled and the propagation is owed: §0.6 currently reads as a live mandate and §7 reads as a dismissal, and neither says "v2".

5. **`domain/domain-design.md` §7, *"Where `workload` estimates come from. Tilt: Billy states a rough number, revisable."*** Reversed inside the same record by §6.1 (`[R]` Billy 2026-08-23, *"`hours_estimate` is not a field to be filled"*) and again by `schema.md` §7. **Uncorrected within its own document.** Billy's 2026-08-30 ruling 2 closes it a third time.

6. **`domain/domain-design.md` §4, publication time.** *"the system does not need to know how a source arrived, but it does need the source's **publication** time, not the ingestion time. Dumping three notices on Sunday in the wrong order would otherwise let an older fact silently overwrite a newer one."* §4 carries a SUPERSEDED banner covering **the operations model**, not this clause. `L4-invariants.md`, Invariants with no stated enforcement point: *"No field carries it, and **it is not in §7's graveyard either, so it was neither kept nor rejected**."* `L2-lifecycle.md` capability 7 supplies the concrete scenario. **Confirmed absent** from `schema.md` §2-§5 field tables and from §7's graveyard. This is a genuine third state - not carried, not rejected - and it is the cleanest example in the corpus of a requirement lost to a banner's scope being wider than its subject.

---

## Open questions addressed to Billy

Phrased as decisions still owed, with who is asking.

**Q1. The `parts` grain, and whether the 12 copied values are a change set.** `evidence/2026-08-26-slice-1-build/NOTES.md` §Cycle 1, `[marked]`: *"`parts` is COPIED from the source fixture on 12 rows, never produced ... if the birth rules land differently these 12 values are the change set."* The birth rules **did** land differently: `write-rules.md` §3.4 turns *50 candidate strings into 28* on one course and explicitly drops `Monte-Carlo`, `A5Tree`, `Life on the River` - three of which are in the 2026-08-26 fixture verbatim. **The change set was predicted and, as far as `spec/` and `domain/` show, never reconciled.** Owed: is the 2026-08-26 fixture retired outright, or migrated?

**Q2. The `2c03-a7` optionality case - partly answered, and the answer may be wrong.** `[agent-drafted]`, same file: A7 as an obligation is required, only its third part is optional, per-part modelling is ruled out, so `optional = false` and the optionality survives inside the `parts` string `Part 3 (OPTIONAL - no extra marks)`. `L1-material.md` capability 18 attacks exactly this: *"the row's typed answer to *is any of this skippable* is `false`, and the true answer is inside a string the only declared reader treats as a concept."* **`write-rules.md` §3.4 has since made that string illegal** - it is paper structure, dropped as noise - so the escape hatch closes and the fact is lost entirely, with no note possible below obligation grain (*"a part is a raw string, not a node"*). Owed: where does a part-grain qualification live, or is losing it accepted? The `optional` tally that flagged this was dropped from `schema.md` on 2026-08-27, which removed the symptom.

**Q3. The blind exercise's scoring.** `PREREGISTRATION.md` is falsifiable on purpose and was never scored, because `ADJUDICATION.md` does not exist. Owed: score it, or retire the exercise and say the ninety capabilities are evidence-only. **This is the decision that gates everything else in the tier-recut directory.**

**Q4. The snow-day note's attachment.** `ROUTING.md` course rows: routed course-level *"**although its content is entirely about one obligation**. Following the authority; the tension is recorded in the session file"*, and `NOTES.md` §Outcome lists it as one of two decisions **flagged to Billy and not acted on**. `L1-material.md` capability 6 re-derived it independently and priced it: *"a one-hop read of `2c03-tutorial-attendance` returns the earning rule (10 of 12) and **not the credit that changes the answer to 9**."* **Checked `spec/design.md` §3.2, `spec/schema.md` §4/§5, `spec/ring-0.md` §7: no record decides it.** Owed: does a note reach a node it is about but not attached to, or does attachment follow content rather than the course-level rule?

**Q5. F2 - conflict detection has no home in the first build.** `architecture.md` §7 removes `land()`; `design.md` §1 F2 still requires *"Landing is idempotent and **detects conflicts instead of overwriting**"*. Three derivations converge: `L3-surface.md` capability 15 (*"the only write path is field CRUD, and if that write returns nothing about the prior value, the tier holding the adjudication has nothing to adjudicate. **F2 is unimplementable at the surface**"*), `L2-lifecycle.md` capability 16 and 17, `L4-invariants.md` capability 14 (*"**F2 has no home in the first build**"*). **Billy's 2026-08-30 ruling 7 is now the governing statement** - two conflicting statements must never coexist; shallow conflicts the agent resolves and reports, deeper ones it asks about first - which makes F2's mechanism a live requirement rather than a dormant one. Owed: does a field update return what it replaced?

**Q6. Whether the CLI probe settled anything ruling 9 now reopens.** `L3-surface.md`'s add-on probe is explicitly labelled *"a probe, not a design. Nothing above depends on it, nothing should be built from it,"* and lists its own four invented holes. It nonetheless names a grammar (`courses` / `course <id>` / `show <id>` / `set` / `progress` / `note add`, `--json` for the machine branch). **Billy's 2026-08-30 ruling 9 defers exactly this: no exposed CLI surface, product-facing verb names undecided.** So: nothing in the probe is settled and ruling 9 does not reopen anything, **but ruling 9 presupposes the level-based grammar** that `architecture.md` §5 rules, since "verb names undecided" presumes verbs. The probe is the only worked instance of that grammar over real fields and is the natural input when the gate opens. Owed only as a pointer: does the probe survive as evidence for that cycle, or is it disposed of as its own banner says?

**Q7. The tier-recut sitting's own two unanswered questions.** `NOTES.md` §What was NOT produced: *"The two questions in the plan's §7 are unanswered - `obligation.course` updatability and `parts` update grain. Both have recommendations, neither has a ruling."* `spec/write-rules.md` §3 confirms the first is still open (*"still open at `../plan/application-tier.md` §7.1 as a recommendation with no ruling. **The code implements the recommendation**; this record does not decide it"*). **Code now implements an unruled recommendation.** The second, `parts` update grain, is `L2-lifecycle.md`'s "could not determine" item *"Whether `parts` elements are individually addressable"* and is unanswered in `spec/` and `domain/`.

---

## Abandoned steps

**Recorded so no later reader promotes one to a ruling.** These are category (2): written confidently inside a sitting, then abandoned or superseded by the same or the next sitting.

- **`evidence/2026-08-26-slice-1-build/NOTES.md` §Cycle 1, ids re-minted from `name` under `<course_id>-slug(name)`.** Five ids were changed under the rule (`2c03-final` to `2c03-final-exam`, and four others). **The whole scheme is retired**: `schema.md` §1.1, 2026-08-28, Billy - an id is an opaque monotone serial and *"nothing derives one from the material"*. The five renames are now an artifact of a dead scheme. `write-rules.md` §3.1 records the second-order consequence: the `name` convention was owed **only because** the id was minted from the name, so it dissolved rather than being answered.
- **`evidence/2026-08-26-slice-1-build/NOTES.md` §Cycle 1, annotation ids follow `<target-id>-<kind>-<handle>`.** Self-labelled *"Drafted, not ruled; nothing depends on it yet."* Dead with the scheme above. `L4-invariants.md` still lists *"how an annotation's id is minted"* as undetermined; under the opaque serial it is answered by construction.
- **`evidence/2026-08-26-slice-1-build/NOTES.md` §Cycle 2, "Cycle 2's earlier Track A was cut on the wrong line".** The sitting names its own abandoned cut: *"The correcting error was classifying by artifact type instead of by consumer, one paragraph after quoting `slice-1.md` §4.4's Docstrings are design, not documentation."* **The corrected version - the seam is mechanism versus interface, not code versus document - was itself then superseded** by the tier re-cut, which re-targeted the whole ordering ruling. Two layers of abandonment on one question.
- **`evidence/2026-08-26-slice-1-build/NOTES.md` §Handoff, the seal on `records/plan/write-rules.md` §9.** *"The seal ... is broken. The next sitting's opening gate read the withheld material before the mandate was opened, so the independence it protected is spent."* The whole independence apparatus for that mandate is abandoned; the method that replaced it is `spec/write-rules.md`'s header (Billy hand-editing one course).
- **`evidence/2026-08-26-slice-1-build/NOTES.md` §Cycle 2, the two-position `parts` question sealed pending an independent session.** Sealed, then ruled directly on 2026-08-27 without the independent session. The seal is not a standing constraint.
- **`evidence/2026-08-27-tier-recut/NOTES.md` correction 1, increments named after `design.md` §3.4's operation set.** The first plan frame, rejected by Billy at the unit rather than the order. Anything that reads as a build sequence over `kinds / persistence / land() / get,nodes,links / acceptance` is this abandoned frame.
- **`evidence/2026-08-27-tier-recut/NOTES.md` correction 3, Python as the recommendation.** Abandoned by the agent's own reversal, on stronger ground than Billy offered.
- **`evidence/2026-08-27-tier-recut/NOTES.md` correction 4, the JSON-only premise for rejecting MCP.** Corrected in the sitting: an MCP tool result can carry rendered text.
- **`derivations/L3-surface.md` §ADD-ON, the whole CLI probe.** Self-labelled disposable, with four named invented holes (sort order, top-level column set, summary composition, ids in the human render). **Not a design.**
- **`derivations/L1-material.md`, `L2-lifecycle.md`, `L4-invariants.md` capability lists as a whole.** These are **derivations under an assigned lens by agents blind to the plan**, dispatched to test a coverage table. They are not proposals and were never adjudicated. Treat any single "capability N" as an argument with evidence attached, never as a decision.

---

## Measurements and their standing

| measurement | source | standing today |
|---|---|---|
| 39 units of routed content across 21 rows; 11 to a sticky note, 28 dropped, 4 dropped by an existing ruling | `ROUTING.md` §Counts | **Stands as a description of that transcription.** The transcription itself is not a golden set (R1) and its 22-row basis is superseded (V7) |
| 22 obligations - 15 `2c03`, 7 `2aa4`; 2 courses; 11 `about` links, 3 to a course | `ROUTING.md` §Counts, `NOTES.md` §Raw material | **Superseded.** `architecture.md` §4: a fresh extraction found **14** for 2c03 and the 22 included a graveyarded recurring row. Still cited as fact by `design.md` §1 F5 (V7) |
| ids changed under the minting rule: **4** | `ROUTING.md` §Counts | **Wrong, and wrong within its own sitting.** `NOTES.md` §Cycle 1 lists five and says so explicitly: *"(five, not four)"*. Moot under the opaque-serial ruling, recorded because the two files disagree |
| `evidence/2026-08-23-read-cycle/PROVENANCE.md` describes a different artifact than the file beside it | `NOTES.md` §Cycle 2, `[measured]`, checked value by value against a sheet read in the original | **Stands, and is uncorrected at its source.** The 2026-08-26 `fixture.json` header **repeats the false claim**: *"three of the launch-shaped values in the source fixture are synthesized and that carries over unchanged."* The sitting that measured the claim false did not fix the file it wrote in the same cycle |
| `parts` carries three mutually incompatible grains across 12 rows; 7 of 12 smuggle per-part marks into free text | `NOTES.md` §Cycle 2, `[measured]` | **Stands and is now acted on.** `write-rules.md` §3.4 drops paper structure as noise and drops one-off local items; `L1-material.md` capability 17 restates the graveyard breach independently |
| Cycle 1's a1 graveyard check **scanned field names, not field values** | `NOTES.md` §Cycle 2, `[measured]` | **Stands, and generalises.** `L4-invariants.md`: *"Every graveyard entry about **content** rather than about a **field name** has no enforcement point."* No record I read states this |
| `import fall26` fails - `fall26/__init__.py` re-exports from a nonexistent `src` package | `NOTES.md` §Cycle 1, `[measured]`, verified by running | **Unverifiable from my boundary** and probably moot: `architecture.md` §6 makes the build TypeScript and puts `fall26/ingest.py` *"in no tier"* |
| rewording one docstring moved a verb's call count from **1 to 9** with data availability held constant | cited in `evidence/2026-08-27-tier-recut/NOTES.md` correction 4, from `design.md` §3.6 | **Stands and is load-bearing.** It is the surviving empirical argument for `architecture.md` §5's rejection of description-routed verbs |
| the one-line-summary trace: Billy's own example CLI render carries `What it is: <one line summary>` and **no field can produce it** | `evidence/2026-08-27-tier-recut/NOTES.md` §"The finding that validated the method" | **Half stands.** The gap was real and landed (`design.md` changelog 2026-08-27, `architecture.md` §5). The **remedy** was then withdrawn on 2026-08-28: there is no composed summary at the obligation level, a level shows fields, and a summary is written only for the artifact |
| 11 notes, `category` distribution `policy` 8 / `format` 2 / `requirement` 1 | `L1-material.md` §"handled well" | **Stands and landed.** `schema.md` §4 and §9 item 2 use exactly this - *"one value holds 8 of them and the boundaries between the others do not reproduce"* - as the ground for the owed write rule |
| 2c03's `grade_share` column sums to **102**, 2aa4's to **45** with three nulls | `L1-material.md` §"handled well" | **Stands, and independently re-derived.** `ring-0.md` §6 reaches the same conclusion from a fresh corpus (95, with the missing 5% having no row) and treats it as decisive without measurement |
| 3 of 22 obligations have no artifact at all; 3 rows carry null `due`, null `grade_share` and empty `parts` | `L1-material.md` capabilities 15/18, `L3-surface.md` capability 11 | **Superseded in its numbers, alive in its shape.** `ring-0.md` §4 measures the current corpus at **6 of 14 carrying an annotation, 8 carrying none**, and `ring-0.md`'s own changelog corrects an earlier miscount of the same statistic. The `has-more` field exists because of it |
| 18 `about` instances measured, **zero at course level in the material** | `design.md` §3.3, quoted against my sittings | **In tension with the fixture**, which produced 11 `about` links, **3 to a course**. Different corpora (source graphs versus the re-transcription), so not a contradiction - but `design.md` §3.2's *"the course case comes from the late-day budget living on a note"* is now understating an observed pattern |
| the free-text cap of one field per kind is already broken on `obligation` | `L1-material.md` and `L4-invariants.md`, independently | **Stands, uncorrected.** `schema.md` §1 still states the cap flatly; §9 item 3 names *"two routes, not one"* without identifying the second. `model.md` §10.5 identifies the second as `label`, **which no longer exists**, so the item is undecidable from the records - `L4-invariants.md`'s exact wording |
| no write cost, no atomicity rule, no index-invalidation rule anywhere, against a commitment to field-grain partial update on JSONL | `L2-lifecycle.md` capabilities 12/13, `L4-invariants.md` capability 21 | **Confirmed absent.** I grepped `spec/` and `domain/` for atomicity, fsync, temp-file, lock: **zero hits**. `design.md` §5's persistence facts are all read-side. Possibly parked at `plan/backlog.md`, which I could not read |
| the link-set validation pass is owed by `design.md` §3.2 and appears in no tier's method set | `L4-invariants.md` capability 5, `L2-lifecycle.md`, and predicted in `PREREGISTRATION.md` item 2 | **Confirmed still absent.** `design.md` §3.2 and §6 call it *"a real operation the design owes, not a hand-wave"*; it is in no operation table in `architecture.md` §7 and no phase in `schema.md` §8 |

---

## Coverage

**Read in full:** all three files in `evidence/2026-08-26-slice-1-build/` and all seven in `evidence/2026-08-27-tier-recut/`, including `derivations/L3-surface.md` end to end. `evidence/README.md`.

**Checked against:** `records/domain/model.md`, `records/domain/domain-design.md`, `records/spec/architecture.md`, `records/spec/schema.md`, `records/spec/design.md`, `records/spec/ring-0.md`, `records/spec/write-rules.md` - all seven read in full, plus targeted greps across both directories for atomicity, dangling refs, migration, publication time, duplicate links, retarget, cycle checks and orphaned annotations. Branch confirmed `design/course-level`.

**Not read, and every gap claim is scoped accordingly:** `records/plan/` (`application-tier.md`, `backlog.md`, `write-rules.md`) and `records/archive/`. `spec/` cites `plan/backlog.md` by item number at least four times (B19, B20, B27, the load-time construction pass), so **items I report as having no home may be parked there.** The ones most likely to be: the `look_at` return shape (B19), the empty Final Exam `parts` (B27), the load-time validation pass, and possibly the timestamp assigner from R9.

**Not attempted, by instruction:** any adjudication. Every conflict above is stated with both sides quoted and left open.

**What I could not determine.**

- Whether `ADJUDICATION.md` was ever written and lost, or never written. `derivations/README.md` refers to it in the present tense.
- Whether the ninety-odd derived capabilities were reviewed at all. One citation exists in `ring-0.md` §5; whether the rest were read and rejected, or never opened, is not recoverable from the records.
- Whether the 2026-08-26 fixture is still a live test input. `plan/application-tier.md` names a migration of it (I saw this only in a grep line, not in context) while `architecture.md` §4 retires the 22-row criterion the fixture serves.
- The standing of `evidence/2026-08-23-read-cycle/PROVENANCE.md`, which the 2026-08-26 sitting measured as mislabelled. It is outside my read boundary and another agent's sitting.
