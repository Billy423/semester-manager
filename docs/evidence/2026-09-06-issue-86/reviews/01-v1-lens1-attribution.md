# Review 1 - draft v1, lens 1 (attribution)

**Reviewer:** a blind subagent, given `drafts/v1.md`, full repository read access, and `docs/agents/reading-records.md` as the discipline. Withheld: the session transcript, its reasoning, the pre-registration. Blind to the lens-2 reviewer.

**Report, verbatim:**

---

## Method

Read in the prescribed order: `reading-records.md`, `drafts-and-rulings.md`, `CONTEXT.md`, `docs/adr/README.md`, then the draft. Every `NNNN` and `#n` the draft cites was opened (36 records, 15 issues with bodies and comments). Two sweeps were run for the contradiction check: every landed mention of the bands (since §7 dissolves them) and every landed sentence fixing the line's field set or `has-more`'s place on it. The five session rulings named in the draft's second paragraph were treated as ruled and not judged on their merits. Quotations and attributions were checked separately, per `reading-records.md`'s last section.

Thresholds as briefed: BLOCKING if a cited record does not support a claim that is a ruling, or a ruling contradicts a landed record §10 does not list; REPAIR if the fix changes an attribution, a wording or a table cell without changing a ruling; ambiguous resolves to BLOCKING.

## Findings, most severe first

### B1 - §5 and §10.6: the line as derived carries `has-more`, and two landed records not listed in §10 say it does not

**Section.** §5, the bolded conclusion, and §10 amendment 6.

**The claim.** *"The line is `id · name · due · done_by · optional · has-more`, at positions 1 and 3 course's line and progress's line."* Then: *"`0082`'s transfer clause, 'obligation's line is ring 0's band B', becomes 'obligation's line is ring 0's row'"*, and amendment 6 applies that to `0082` and `0095`, one sentence each.

**The cited records, and what they actually say.** `0082`, as repaired at #80: *"`has-more` is **not** on the line, because `<neighbours>` strictly contains it and `0024` bars stating one fact twice (`0096`)."* `0096`: *"So `has-more` has no place in a node's render at all. Its own ground in `0092` ... holds **only** where the neighbourhood cannot be listed. That is ring 0."* The draft's own §5 row for `has-more` agrees with this in its last clause - *"where it appears in ring 0's render is #82's"* - and then the bolded sentence folds it into *the line*, and amendment 6 transfers *the line* onto `0082`, where the line is what a neighbour renders as inside `<edge>`.

**The aspect mismatch.** Two things are being equated that the landed records keep apart: the field set of a ring 0 *row* (an endpoint of the standing result, which cannot list its neighbourhood, so `has-more` belongs there by `0092` and `0096`) and the field set of a *line* (a neighbour inside a block, whose `<neighbours>` context makes `has-more` a duplicated fact by `0024`). Amendment 6 as written makes a neighbour's line in a block carry `has-more`, which `0082` and `0096` rule out, and neither sentence is in §10's repair list. A second hole in the same transfer: a neighbour's line in a block has no path positions, so *"course and state as positions"* is not well-typed there - `0096`'s worked example carries them as attributes on the line (`<obligation id="51" course="2c03" ... state="not_started"/>`), and the draft does not say what a block's neighbour line does with them under the new clause.

**Verdict: BLOCKING** under (c). The fix is not a wording change: either the line is the six fields *minus* `has-more` and the row is the line plus `has-more` (which alters the bolded ruling sentence and amendment 6), or the draft says which of `0082`'s and `0096`'s sentences is being overturned and lists them in §10.

### B2 - §3: #14's evidence comment is cited as a "ruled source", and J5's must-standing rests on it alone

**Section.** §3, the *Sources* paragraph and row J5.

**The claim.** *"A judgment is must if it is derivable from a ruled source: `CONTEXT.md`'s opening sentence, `0001`'s second job as rewritten at #85, or #14's three replicated buckets."* J5 (*which items need Billy*) is then recorded as must with source *"#14 bucket 3"* and nothing else.

**What #14 actually says.** Its evidence comment is labelled *"Evidence, from the audit at #61"* and states its own standing: *"This is a count and it replicates ... It bounds acceptance item 1 without answering it: three buckets recur across runs whose key sets share nothing, so a representation that cannot express those three is contradicted by the only evidence there is. It does not say the plan is those three buckets."* It is a fall26 measurement carrying the standing caveat (which the draft correctly applies in §0 and §11). Nothing in #14 or anywhere else rules the buckets as a source of must-judgments.

**The aspect mismatch.** The draft's own test in §3 requires a *ruled* source. The opening sentence and `0001` are ruled; #14's buckets are evidence. J1 survives because it also rests on the opening sentence. J5 rests on bucket 3 alone, so under the draft's own rule it is a candidate, not a must - unless Billy rules the buckets in as a source, which is not among the five session rulings paragraph 2 lists. The draft's *"J5's predicate is owed, not invented"* paragraph is careful about the predicate and silent about the standing of the judgment itself.

**Verdict: BLOCKING** under (a). The claim *#14 is a ruled source* is not supported by #14, and the claim it carries (J5 is must) is a ruling of deliverable 2. Fix: add *the three buckets bound the must-list* to the session-rulings list if Billy in fact ruled it, or demote J5 to *candidate, parked with #16's wake*, which is the level the evidence supports (`drafts-and-rulings.md`, *Demote to the level the evidence supports*).

### R1 - §4: `0016` cited for barring `state` on the obligation's row

**Claim.** *"The alternative - `state` copied onto the obligation's row - is what `0038` did, and it is the field-on-the-related-thing that `0016` bars."*

**What `0016` says.** *"A relation between two things is its own record, never a field on either end. A note's target is an `about` link, not a `target_id`."* It constrains how a **relation** is stored on a **persisted** record.

**Aspect mismatch.** A ring 0 row carrying a progress record's `state` value is not a relation stored as a field, and a ring 0 row is not persisted (`0019`: *"residency is an access policy over obligation nodes' fields, not a separate store"*). `0016` speaks about neither aspect. The ruling (`state` is position 3) stands on `0035` and on Billy's three-position ruling without it. **REPAIR:** drop the `0016` clause or reground it on `0035`'s *"`state` sits on `progress` and not as a field of `obligation`"*, which is the record that actually bars the copy.

### R2 - §4 and §7: "four more fields" is three

**Claim.** §4: *"the partition decides which rows carry four more fields."* §7: *"four fields on 43 more rows costs nothing at this width."*

**What `0038` says.** *"Ring 0 carries `course`, `name`, `due`, `state`, `optional`, `done_by` and `has-more`; band B drops the last three."* The table: band A seven, band B four. The difference is `optional · done_by · has-more`, three fields.

**REPAIR:** a number in a landed record misread; the argument it feeds (the practical ground Billy accepted) is strengthened, not changed.

### R3 - §8: "the one link field is `spec.role`"

**Claim.** *"The one link field is `spec.role ∈ {given, owed}` (`0012`)."*

**What the records say.** `0012` does give `spec` its `role`. But `0017`: *"`locator` is part of it"* (a link's natural key); `0102`: *"typed directed links with fields (`role`, `locator`)"*; `CONTEXT.md` has a `locator` entry. Links carry two fields.

**Aspect.** The verdict - *MOVE with Q has no must-judgment today, parked* - survives, because no ruled source names `locator` in a judgment either, and `0082` already says of it that it *"says where you land after walking, which does not bear on whether to walk"*. **REPAIR:** state both fields and dismiss `locator` on `0082`'s ground, so the parking's wake condition covers it.

### R4 - §3: `0056` cited for "an asked answer awaiting him"

**Claim.** J5's three candidate readings include *"an asked answer awaiting him (`0056`)"*.

**What `0056` says.** *"An answer the system asked for is stored, with its timestamp and its provenance, and the provenance is stated prominently at every read."* It governs an answer already given and kept. A question asked and not yet answered is a different state, and `0056` does not speak about it; #10 (*Asking - unprompted speech, confirmation, and asking at the read*, per #16's body) is where asking lives.

**REPAIR:** the list is explicitly of candidates with no record picking one, so no ruling moves; reattribute to #10 or mark the candidate as unrecorded.

### R5 - §1(iii): `0003` cited for exclusivity it does not state

**Claim.** *"`not exists` is the only way a chain tests absence on one member (`0003`)."*

**What `0003` says.** *"The third job is served by subtraction over the graph ... returns nodes that have no link of the named kind in the named direction."* It defines the set-difference query; it says nothing about which forms of a chain can express it or that one form is the only way.

**Aspect.** The exclusivity comes from §1(i)'s own reading over the candidate forms, not from `0003`. The ruling (`not` and `exists` are each a form) does not change. **REPAIR:** cite `0003` for the instance that requires absence-testing and let (i) carry the exclusivity.

### R6 - §1: "§7" refers to #85's §7, and the draft has its own §7

**Claim.** *"§7's provisional reading is confirmed"*, *"§7's connectives as one form is replaced"*, *"The concrete case #85 §7 named"*.

**Check.** The first two are #85's resolution §7 (*"the connectives taken as one form"*; *"without it was read over the forms listed above minus the one under test"*), and the quotations verify there. The draft's own §7 is *What `0042` was*. Only the third reference is qualified. **REPAIR:** qualify all three as *#85 §7*; a reader arriving via the draft's table of contents lands on the wrong section.

### R7 - §5: "obligation's field table (`0028`, `0032`, `0033`, `0037`)" is not a table any landed record carries

**Claim.** *"Applied field by field over `obligation`'s field table (`0028`, `0032`, `0033`, `0037`)."*

**What the records carry.** `0028` carries the timestamp convention (`added_at`), `0032` one field pair, `0033` one field, `0037` removed fields. None carries the table. `0082`'s Source line names where it lives: *"the field tables it derives over are `fall26:records/spec/schema.md` §2-§4.5"* - provenance only. `reading-records.md`'s first rule applies: before a list is run over as exhaustive, state what list it is and what question it answered. The draft's enumeration (`id`, `name`, `due`, `done_by`, `optional`, `course`, `parts`, `grade_share`, `grade_share_conditional`, `added_at`) matches what this repository's records name for `obligation`, with one omission: `kind`, which `0082` makes an attribute *"because it addresses"* and which the line carries as its element name. **REPAIR:** say the list was assembled from those four records plus `0029` (`course`) and `0038` (`optional`), and add a `kind` row (*in, as the element name*), so the exhaustiveness claim is auditable.

### R8 - §5: `0099` cited for `added_at` not rendering, which it rules for a block

**Claim.** *"`added_at` | no reader; `0099` rules it does not render | out."*

**What `0099` says.** *"`added_at` does not render, and this is a ruling rather than a derivation"* - and its ground: *"`look_at`'s purpose is to say what the **node** is, not what the **row** is."* It rules a node's render. `0100` says `0082`'s rules *"do not reach a collection at all"*, and ring 0 is not a node's render.

**Aspect.** The verdict stands on the draft's own criterion (no reader, does not form the next intent). **REPAIR:** cite `0099` as the same ground applied one render over, not as the record ruling ring 0's row.

### R9 - §9: `0041`'s order restated without its middle clause

**Claim.** *"`0041`'s order stands, `due` ascending, nulls last, ties by the handle, never array order."*

**What `0041` says.** *"Order by `due` ascending, nulls last; among nulls by `done_by`; ties broken by the handle."* The among-nulls rule is dropped. Since the sentence says the order *stands*, the omission is a wording gap, but it is the input #82 will read. **REPAIR:** restore *among nulls by `done_by`*.

### R10 - §2, §3, §11: the concept-position debt is homed at two different issue sets

**Claim.** §2: *"`concept`'s and `artifact`'s are the debt that entry records"* - the `the line` entry, which names #20, #19 and #17. §3 J2: *"no concept nodes exist yet (#25)"*. §11: *"the deciding fields of a `concept` or `artifact` position (#25, #19, #20)"*.

**Check.** `CONTEXT.md` and `0101` both home the deciding-fields debt at #17, #19, #20. #25 (the concept layer's origin and refinement, wake: *"the `concept` kind exists and something writes into it"*) is a defensible citation for *no concept nodes exist yet*, but §11 substitutes it into the debt list, so the draft disagrees with the glossary and with itself. **REPAIR:** use #17/#19/#20 in §11 to match the entry the draft cites in §2, and keep #25 for J2's existence claim if that is intended.

### R11 - Paragraph 2 and §7: "the window" used for the three-trigger rule

**Claim.** Paragraph 2: *"`0042`'s band partition dissolves and its window becomes the coordinator's judgment rule."* §7, last sentence: *"the window is now its own rule, so it can widen it in an exam week."*

**Glossary.** `band A` / `band B`, _Avoid_: *"the active window for band A - the window is one of three triggers, not the partition."* §7's own summary line gets it right (*"the three triggers, as the coordinator's judgment rule for near"*); the two sentences above use *window* for the whole rule, which is the conflation the entry names. **REPAIR:** say *its three triggers become the coordinator's judgment rule*; *widen the window* is correct usage only for the date trigger and should say so.

### R12 - §10: landed records that carry the bands as a live premise and are not in the repair list

The band sweep over `docs/adr/` and `CONTEXT.md`. Amended by §10: `0038`, `0042`, `0082`, `0095`, `0100` (admission row and standing), `CONTEXT.md`. Not amended, and still carrying the bands:

| record | sentence | status |
|---|---|---|
| `0100`, refresh paragraph | *"what a refresh **returns** is a line, whose field set is band B, which is the selection clause"* | a live premise; §10.4 touches only the admission row and the record's standing |
| `0100`, selection paragraph | *"neither half of the clause is settled while its re-derivation from routing has not run"* | settled by §5; §10.4's *derived at #86* may be meant to cover it but does not name the row |
| `0091` | *"Ring 0 carries the band and excludes `parts` and `grade_share` (`0038`)"* | a live premise for its field-grain argument; already on #82's *owed, not done* list |
| `0092`, Source | *"The field's membership in band A is `0038`'s"* | stale attribution, not a contradiction |
| `0093`, ring 0 section and two rejected-names rows | *"band A and band B are ordinary words"*; `attention` and `status` *"for the band"* | stale, harmless |
| `0094`, closing | *"the band's representation ... travel with it"* | stale, harmless |

None of these contradicts a ruling in the draft; each describes the state §10 amends. **REPAIR:** name `0100`'s refresh paragraph and selection row in amendment 4, and list `0091`, `0092`, `0093`, `0094` as pointer debts per #82's precedent, so the judgment that they are non-blocking is visible rather than silent.

### R13 - §5 and paragraph 3: "the same seven" is `0038`'s seven plus `id`

**Claim.** *"The derivation lands on `0038`'s seven fields"*; *"that it lands on the same seven is a confirmation of `0038`'s selection."*

**Check.** `0038`'s seven are `course · name · due · state · optional · done_by · has-more`. The draft's set is those seven (two re-typed as positions) plus `id`, marked *in, structurally*. `0038` leaves `id` implicit because `0025` and `0061` make every read return handles. **REPAIR:** say *`0038`'s seven plus the handle `0038` left implicit*, so the confirmation claim is exact.

### R14 - §5: "`0101` §1" - the record has no numbered sections

**Claim.** *"`0101` §1 names it as the in-band carrier of which vocabulary applies here."*

**Check.** The sentence exists in `0101` (*"`0092`'s `has-more` lists a row's link kinds wherever ring 0's render places it"*), under the paragraph *Routing is not prompt-driven*. The §1 numbering is #85's resolution comment. **REPAIR:** cite the record's paragraph or the comment's section, not both under one label.

## Citations checked and found sound

Listed by draft section, with the aspect each was used for.

- **Header and paragraph 3.** #86 body items 1-4 as the four deliverables (verified against the body). `0038`'s seven as the landing point (see R13 for the `id` wording).
- **§0.** `0070` for *capabilities, not shapes* (*"Interaction requirements decide which capabilities must exist, never what a method looks like"*). #14's comment for the three buckets and for *bounds without saying what the plan is* (*"It does not say the plan is those three buckets"*). #58's *Out of scope* line on the plan. The fall26 caveat applied.
- **§1.** `0101` for *"admits by what a form lets a chain produce"* and *"a judgment across obligations is a judgment about their relations"* (both verbatim). #85 §7 for the three provisional readings and for `nodes_without` as `START · FILTER(not exists(MOVE))`. #88's *covered* disposition interacting with the formalisation (#88's comment says so in the same words). `0101`'s instrument standing (*"A finding there that it admits what it should not, or excludes what it should not, revises it"*).
- **§2.** `CONTEXT.md`'s opening sentence for *what each obligation requires you to know*. `0081` for a negative answer naming its boundary, used for the not-held / not-found distinction, which is its aspect. `0101`'s one-return premise. `0012`'s `about` signature `annotation → any`. `0039`'s symmetry *"scoped to the set the judgment ranges over"*. `0043` and `0095` for depth not travelling in a return. `CONTEXT.md` *the line* for course's `id name term` and for the concept/artifact debt.
- **§3.** `0001` as rewritten at #85 (job 2 and job 3 sentences verified). #84's acceptance standard (*"exposes every necessary operation ... never a workflow per imagined scenario"*). `0100` as the ground routing job 2 into a relation statement. `0003` as J6's derivation source. `0051` for a conflict the agent may not close (*"asks before resolving"*). `0010` for a surfaced-and-unconfirmed claim. `0101` for *refused, never returned empty*. `0007` for parking with a wake. `0041` for nulls last. `0021` for the time axis being out and a course's coarse grouping deliberately unmodelled. #85's S1-S7 dispositions (S1 *"#87's whole"*, S2 caller-agnostic, verified).
- **§4.** `0101` for *"an unprompted coordinator needs somewhere to stand"* and for ring 0 as one result held by policy. `0029` for `course` as a Ref-typed field; `0101` for Ref-typed fields being crossable. `0035` for one current value per target, absence as `not_started`, and `state` living on `progress`. `0082` for a defaulted `progress` carrying no `id`. `0046` read as a delivery rule, with `reading-records.md`'s table and `0092`'s *Considered Options* both saying so. `0100`'s admission row and its *"`0042` does not itself say that ring 0 ranges over every obligation"* (verbatim; the draft's gloss that this half-saw the depth reading is a fair reading of a sentence about range, noted rather than faulted). `0038`'s scope clause on the roughly-55 figure. `0101` leaving width unruled. `0021` and `0101` for the time projection as a routing result. `0089` for whole lines per changed obligation.
- **§5.** `0101`'s endpoint criterion (verbatim). `0082` for `id` as an addressing attribute and for the second exception (`has-more` in no field table). `CONTEXT.md` *id* for *"says nothing about the record it names"*. `0092` for `has-more`'s value; `0096` for it surviving only where the neighbourhood cannot be listed. `0038`'s ground for excluding `parts`. `0042` and the rigidity rule for `grade_share`'s standing exemption. `0070` and `0100` for the derivation direction `0038` did not run. `0082`'s transfer clause quoted correctly as *band B* (the problem is what it becomes, B1).
- **§6.** `0042`'s importance sentence as the one #82's permission most reaches (`0042`: *"The sentence most likely to move is the one below barring a notion of importance"*). `0039`'s observe-or-dispatch layer. `0033` for the replacement being *an interaction*. `0010` for owner-authored absorption. `0056` for a kept answer with loud provenance (sound here; the misuse is R4). `CONTEXT.md` *sticky_note* for the open category. `0068` for reading the instance first. #14's ruling-2 sentence (verbatim). `0037` row 1 and `0033` quoted verbatim, and the conflict between them is real: both cannot stand, and the draft's repair direction follows `0033` and `CONTEXT.md`'s `parts` entry.
- **§7.** `0042`'s defence quoted correctly (*"computed from material facts plus one rule applied identically ... carries no interaction history"*) and correctly placed against `0039`. `0043` for the discard. What survives and what dissolves matches `0042`'s text, including *"Breadth is never treated as a defect"* and the note that the permission does not reach the triggers' correctness.
- **§8.** `0102`'s membership row leaving admission to #86 (*"whether the crossing is admitted is #86's"*). `0101` for the cost statements #88 needs.
- **§9.** `0040`'s method transferring and not its ground (`0100` says exactly this). #82's two orphans. #85 §8 for #79's blockers.
- **§11.** `0071` carried from `0101` on repair reads; `0101` on dispatch calls and the effectiveness constraint being undecided.

**Term check.** No _Avoid_ term is used in its avoided sense except *window* (R11). *Row* is used for a ring 0 member, which `CONTEXT.md` itself does (*"A ring 0 row is not a line"*); the draft's *"obligation's line is ring 0's row"* is framed as a field-set transfer, which is the reading `reading-records.md` row 4 requires, but amendment 9 should keep the glossary's *a ring 0 row is not a line* note since render stays #82's. *Mastery* is not used; the draft routes absorption to `sticky_note` rather than to `progress`, which respects `progress`'s _Avoid_ list, and the adjacency is worth one sentence there.

## Summary

Two BLOCKING findings and fourteen REPAIR findings. B1: the derived line carries `has-more` and amendment 6 transfers it onto `0082` and `0095`, where `0082`'s #80 repair and `0096` both say `has-more` is not on the line, and neither sentence is in §10; the same transfer is untyped for a block's neighbour line, which has no positions. B2: #14's evidence comment is cited as a ruled source, and J5's must-standing rests on it alone, failing the draft's own §3 test. The repairs are attributions for a neighbouring aspect (`0016`, `0099`, `0056`, `0003`), a number misread from `0038` (three, not four), an incomplete link-field claim (`locator`), a dropped clause of `0041`'s order, two internal inconsistencies (#25 versus #17; #85's §7 versus the draft's), a glossary term used in its avoided sense (*window*), and a list of band-carrying records that need pointers rather than repairs. Every quotation checked verified; the defects found are in what the quotations were attached to, which is the failure `reading-records.md` says a quotation check will not catch.
