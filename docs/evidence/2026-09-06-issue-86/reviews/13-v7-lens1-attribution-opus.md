# Review 13 - draft v7, lens 1 (attribution), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v7.md`, full repository read access, and `docs/agents/reading-records.md` as the discipline. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-12. Blind to the lens-2 reviewer.

**Report, verbatim:**

---

## Findings

### B1 - BLOCKING. §10 item 13 lands a sentence the draft's own §2 and §5 falsify

**Section:** §10 item 13 (`CONTEXT.md` amendments), against §2 and §5.

**Claim:** item 13 proposes that `CONTEXT.md`'s `the line` entry keep its "appears in two places" clause, "gaining a routing path's node position as a third".

**What the record actually says.** `CONTEXT.md`, *the line*: "It appears in two places: inside an `<edge>`, and inside a composed section (`0094`)." Adding "a routing path's node position" as a third makes the entry assert that obligation's **line** is what a routing path's obligation position carries.

**The conflict is with the draft, not the record.** §2 rules: "A position's field set is not the kind's line: §5 derives obligation's and finds the two differ in both directions, and a line is a render (`CONTEXT.md`, *the line*), which decides nothing at a position." §5 makes the difference concrete: the obligation position is `id · name · due · done_by · optional · course · has-more`; obligation's repaired line is `id · name · due · done_by · optional · course · state`. The position carries `has-more` and the line does not; the line carries `state` and the position does not.

The same item then adds "a note that a path position carries a position's set and not a line". Both clauses cannot land: one says the line appears at a routing path's node position, the other says it does not. This is the exact seam paragraph 3 records the fifth and sixth review rounds catching ("a node position's content had still been equated with its kind's line, which §5's own row-versus-line derivation falsifies"; "the progress position's set had been called a line"), surviving one layer further out in the amendment list.

**Verdict: BLOCKING.** Repair is to strike the "as a third" clause and keep only the row-versus-line / position-versus-line note — but as written the amendment ships a contradiction into the glossary, and which of the two clauses is intended changes what §2 rules.

---

### B2 - BLOCKING. A landed record still equates a resolve's endpoint with a line, and §10 does not dispose of it

**Section:** §2 and §5 (a position's set is not a line), against `0095` and `CONTEXT.md`'s `the line`.

**Claim:** §2 - "A position's field set is not the kind's line". §10 item 2 acts on this by dropping `0101`'s citation of `0095`: "Its citation of `0095` for *one set per kind* is dropped, since a position's set is not a line."

**What `0095` actually says**, in its discard section (`docs/adr/0095-each-section-carries-its-own-depth.md`):

> **This is true of a block.** A resolve's return (`0101`) is bounded in depth - **every endpoint is one line** - and unbounded in width; what gates that width is not yet ruled.

That sentence is a landed record saying a resolve's endpoint **is** one line. It was added to `0095` by #85's own §9.3 amendment, so it post-dates the routing definition and is current.

**Aspect mismatch, stated fairly.** `0095`'s sentence sits in the *depth* section and its subject is depth-boundedness; on a depth-only reading ("bounded to one line's depth") it survives the draft untouched, and §2's "of line depth" agrees with it. On its plain reading it is a field-set identity, and §5 falsifies it in both directions.

**Why it is blocking rather than a stylistic residue.** The draft removes this equation everywhere it finds it - it drops `0101`'s `0095` citation for precisely this reason, and §5 argues at length that the progress position's set "is a position's set and not a line". §10 item 7 touches `0095` only at its two band-B sentences and explicitly declares "its *no rule generates a new kind's line* is untouched, since a position's set is not a line" - so `0095` was read for this question and this sentence was not disposed of. It is not in §10 item 14's pointer-debt list either.

The same ambiguity sits in `CONTEXT.md`'s `the line` note, which §10 item 13 also leaves standing: "A line is what a path's endpoint renders as inside a block (`0101`)." Under B1's repair this sentence needs an explicit disposition (it is defensible only if "inside a block" restricts it to resolve entering through fetch, `0084`/`0094`).

**Verdict: BLOCKING** by threshold (c) - a ruling in the draft contradicts a landed record that §10 does not list. The minimal repair, if Billy takes the depth-only reading, is to move `0095`'s sentence and `CONTEXT.md`'s note into item 14's pointer debts rather than into item 7.

---

### R1 - REPAIR. §10 item 7's "`0095`, three sentences" names two

**Section:** §10 item 7.

**Claim:** "`0082`, two sentences; `0095`, three sentences; `0096`, one example."

**What it then enumerates for `0095`:** "so the band is band B" and "its opening sentence of the same section, *'`0082` sets obligation's line by a transfer - `0038` chose that field set for residency'*" - two sentences replaced - plus "its *no rule generates a new kind's line* is untouched", which is named as **not** amended.

**What `0095` actually carries as a third band sentence**, unnamed in item 7:

> A line that picked each row's own band would import `0038`'s **residency** computation into a **read**.

Band A and band B dissolve at §7, so this sentence needs the same treatment as the other two. Either it is the missing third and should be named, or the header count should be two.

**Verdict: REPAIR** (a wording/count fix; no ruling changes).

---

### R2 - REPAIR. §10 item 9's "`0089`, its title and two sentences" under-enumerates the record's "line" sentences

**Section:** §10 item 9.

**Claim:** "*Whole lines* becomes *whole rows* in the title; its return is a row, and a change at the progress position is a change to the row."

**What `0089` actually carries.** Beyond the title and the return sentence, three more sentences call ring 0's unit a line:

- "**what element a ring 0 line uses is open**, because ring 0's own render is not decided"
- "A whole line is readable on its own, so losing the baseline costs *what did not change* rather than everything."
- "Made useful, it must carry what decides whether a node is worth one `look_at`, and that is the line."

The first is the sentence #82 and #85 both quote as `0089`'s live residue, and §9's #82 bullet inherits it. Under §5 ring 0's unit is a row, so "two sentences" is short by at least one, and the residue sentence in particular should be named so that #82 inherits the corrected noun.

**Verdict: REPAIR.**

---

### R3 - REPAIR. §9's #79 bullet omits #82 as an upstream

**Section:** §9, the #79 bullet.

**Claim:** "**#79 (tool descriptions).** Within this map, still blocked on #87 and #88 - #70 and #64 are its other upstreams and are untouched".

**What the record actually says.** #82's body: "## It blocks #79. `refresh()` returns ring 0's lines, so its tool description cannot be written while the element is undecided. **That is a third upstream of #79, alongside #70 and #64.**" #82's resolution comment and #58's own comment repeat it, and #84's *What this map blocks* calls itself "A fourth upstream alongside #70, #64 and #82."

#82 is open, is unblocked rather than resolved by this record (§9's first bullet), and still owns the element `refresh()` returns. Listing #70 and #64 as #79's "other upstreams" while omitting #82 makes the enumeration incomplete against the record that created the edge.

**Verdict: REPAIR.**

---

### R4 - REPAIR. `0091` is cited for an aspect it does not bind

**Section:** §4, "Why it starts from `obligation`".

**Claim:** "`0018` lets a ref dangle and rules that deleting a course does not cascade to its obligations, and `0091` records that *'a coordinator can therefore name a course row it never read'*, so an obligation whose `course` names no node is produced three ways - landed before its course, orphaned by a deletion, or **carrying a code no course has**."

**What `0091` actually says**, in full context:

> **Read-before-write is structural for every kind but `course`.** It rests on an id being opaque and obtained only by reading it back, and `0026` supplies `course.id` from the material. A coordinator can therefore name a course row it never read.

**The aspect mismatch.** `0091` binds the **read-before-write discipline** - whether a writer has seen the held value before overwriting it. The row it names may exist perfectly well. The draft uses the sentence for **referential validity** - that the named course may not exist at all. That conclusion is available, but it rests on `0026` (the id is supplied, not read back) composed with `0018` ("a ref may name something that is not there"), with `0091` as corroboration for the mechanism rather than as the record making the claim.

The quotation is exact; the attribution is one aspect over, which is the failure `reading-records.md` §"Cite the record that states the claim" exists to catch. The ruling it supports - that the intent starts from `obligation` and tolerates the dangling ref - stands on `0018` alone, so this is a citation repair rather than a hole in the ruling.

**Verdict: REPAIR.**

---

### R5 - REPAIR. §10 item 2 mislocates the first of `0101`'s five places

**Section:** §10 item 2.

**Claim:** "the output paragraph's first sentence, which also carries *'ending at an address'* and becomes *ending at a position, which is an address where it is non-empty*".

**What `0101` actually says.** The output paragraph reads: "**Routing returns a set of paths.** A path is the chain a member arrived by - node, relation, node, … - ending at an address, and the endpoint carries what decides whether it is worth the next call."

The first sentence is "Routing returns a set of paths." and carries neither *endpoint* nor *ending at an address*; both phrases are in the **second** sentence. The count of five places is correct - I verified all five exist in `0101` verbatim ("each ending at an address"; "Each endpoint carries its own kind's deciding fields"; "every endpoint at one depth"; the criterion; plus this one) - but the locator is off by one sentence and the amendment as written would edit the wrong sentence.

**Verdict: REPAIR.**

---

### R6 - REPAIR. §9's #16 bullet says "three readings" and the draft attaches five wakes to that condition

**Section:** §9, the #16 bullet.

**Claim:** "**#16.** Its wake gains three readings: what shape the size and absorption answers took when Billy gave them (§6), what *needing Billy* turned out to mean (§3), and whether the first real decision turned on lecture progress (§3)."

**What the draft actually parks against the same condition.** #16's wake is "has a real semester decision been made and observed by hand?" Five of the draft's wakes are of exactly that form:

1. §6 - "the first real decision observed by hand (#16's wake)" - size and absorption
2. §3 bucket 3 - "the first real instance of an item needing him, observed by hand (#16's wake)"
3. §3 lecture progress - "wake: the first real decision that turns on it"
4. §3 *Billy's own comments* - "wake: the first real decision that turned on a comment the row did not show"
5. §4 `optional` - "Wake: the first real decision in which an optional obligation's inclusion mattered"

Items 4 and 5 are not among the three the #16 bullet names, though both are listed in §11 as undecided. Either they belong in #16's comment or the bullet should say why they are routed elsewhere.

**Verdict: REPAIR.**

---

### R7 - REPAIR. §5 conflates `0038`'s corpus argument with the claim it supports

**Section:** §5, the `grade_share` row.

**Claim:** "the deciding ground is `0038`'s independent corpus argument, which §10 keeps: a rendered column of shares reads as a partition of the grade that it is not".

**What `0038` actually says.** The partition sentence is the *claim*: "`grade_share` is out because a rendered column of shares reads as a partition of the grade that it is not". The **independent corpus argument** is the separate evidence `0038` falls back on after retracting the measurement: "one course's share column sums to 95, the missing 5% has no row, and two 1% bonuses sit outside the 100." `0038` states the distinction in its own words - "**The exclusion's surviving ground is the independent corpus argument below, not these numbers.**"

The draft's colon reads the two as one thing. Nothing turns on it, and §10 item 4's "the exclusions' arguments kept as arguments" preserves both, so this is wording only.

**Verdict: REPAIR.**

---

## Checked and found sound

**Records.** `0001` (three jobs restated; the requirements sentence; job 1 names no judgment of its own; job 2 via `0100`'s ground; job 3 as `0003`'s derivation source, cited "via `0003`" rather than as an objective) · `0003` (`nodes_without`'s signature and its role as J6's chain) · `0007` (parking with a wake) · `0010` (owner-authored, may surface never resolve; "structural, never personal") · `0012` (the nine-row table; `about : annotation → any`; `requires`' two signatures; `spec`'s `role ∈ {given, owed}`; `builds-on` as the one obligation→obligation relation; `prepares-for`) · `0013` (roughly-55 and its scope clause, correctly listed as a pointer debt) · `0017` (a link's fields; `locator` in the natural key) · `0018` (a ref may dangle; no cascade; the "owed and unbuilt" validation pass; `Ref := (kind, id)`) · `0019` ("residency is an access policy over obligation nodes' fields" verbatim) · `0021` (query-by-time-period as a separate projection; the coarse grouping kept out) · `0024` · `0026` (`course.id` supplied) · `0027` (`kind` as required discriminator) · `0028` (`added_at` on `course` and `obligation`; per-field CRUD; null renders as absence) · `0029` (`obligation.course` mandatory, single-valued, monomorphic) · `0031` (nullable bool means unknown) · `0032` (the pointer made optional; "the narrowing must not be smoothed") · `0033` ("not another field but an interaction"; `parts` does not carry size) · `0035` ("one current value per target"; "Why `state` sits on `progress` and not as a field of `obligation`"; absence reads `not_started`; `detail` beside `state` so they cannot drift) · `0037` (row 1 verbatim on both halves; row 11 `course.offering_term` deferred to v2; rows 13 and 14 on term boundaries; the no-re-add rule) · `0038` (the seven, band A / band B; `parts`' exclusion ground; the roughly-55 sizing paragraph and its 2px3 scope clause; the corpus argument) · `0039` ("symmetry is scoped to the set the judgment ranges over"; the observe/dispatch formalism, whose "every member" wording comes from the formalism block rather than the prose - the draft's italicised rendering is faithful) · `0040` (method only, not ground) · `0041` (order; the struck grouping; never array order) · `0042` (three triggers; "it is present, it is routable"; the importance sentence; breadth never a defect; the uniform-depth defence; the overturn permission ruled at #82) · `0043` · `0044` (correctly declared clean among #82's six) · `0046` (the delivery sentence, and `reading-records.md`'s own table row naming the scope-rule misreading) · `0051` · `0056` ("provenance is stated prominently at every read"; `origin`'s write rule owed) · `0068` · `0070` (capabilities not shapes) · `0071` · `0081` · `0082` (the four rules; the second exception for `has-more` and `role`; `Ref`-typed field as a bare pointer; `locator` "says where you land after walking"; a defaulted `progress` carries no `id`; the transfer clause in both of the two places it appears; the Source line pointing at the fall26 schema for the field tables) · `0084` (`obligations.list(course)` composed into `look_at(course)`) · `0089` (whole lines per changed obligation; the delta ground) · `0092` (the value ruling; band A membership as `0038`'s; the Considered Options and Source line correctly listed as pointer debts) · `0093` (the ring 0 section, exactly two rejected-names rows referencing the band, and the names row giving an edge `id`, `type`, `direction`) · `0094` (the term="winter-2026" example; the closing sentence correctly listed as a pointer debt) · `0095` (the transfer paragraph; "so the band is band B") · `0096` (the `<edge>`; the worked example's five attributes, and the arithmetic that adding `done_by` and `optional` reaches §5's seven-field line; `has-more` off a node's render) · `0097` (a member omits what its container fixes; a line is self-closing) · `0099` (`added_at`'s ground; "no reader" declined; the `updated_at` harm quotation) · `0100` (the four-clause table; the admission/selection split; the "`0042` does not itself say that ring 0 ranges over every obligation" doubt; the refresh paragraph's "band B, which is the selection clause") · `0101` (the criterion on an endpoint; "admits by what a form lets a chain produce"; the paths ground; the affordability paragraph; the one-return premise; the empty-result rule; the repair-read exclusion; the open edge-id question; the five endpoint sites for item 2) · `0102` (the membership row deferring the Ref crossing's admission to #86).

**`CONTEXT.md` entries.** opening sentence · `id` · `handle` · `Ref` · `link` / `link kind` · `obligation` · `progress` · `sticky_note` · `annotation` · `parts` · `covers` / `applies` · `ring 0` · `band A` / `band B` · `the line` (all clauses except the two named in B1/B2) · `path` · `routing` · `the walk` · `the block` · `dispatch` · `holder` · `faithfulness` · `reload`.

**Issues.** #86 body and unblocking comment (the four deliverables; the scoping point; the size/absorption exclusions) · #85's resolution §3, §4, §7, §8, §10 (the three formalisation questions and their labelling; the provisional answers; "connectives as one form"; "no crossing reaches a date"; the nine-chain wildcard; the `nodes_without` fixed-point case; S1-S7's dispositions; the `MOVE`-with-`Q` row; the time-projection assignment; the edge-`id` open question) · #82 body (the four *must not be re-opened* items, of which exactly two move; the two orphans; "flat 6,482 characters, structured 7,598"; the 21% / 2px3 scope clause) and its resolution comment (the six pointer debts - `0013`, `0092`, `0091`, `0044`, `0093`, `CONTEXT.md`'s `the line` - all six accounted for by items 13 and 14) · #84 (the acceptance standard; Billy's raw decomposition; the `mastery` / retracted-`concept` deferral; *Destination*; Decisions-so-far) · #14 (the 6-of-6 three-bucket evidence and its "does not say the plan is those three buckets"; the "or nowhere" sentence, quoted exactly) · #58 (*Out of scope*'s plan line) · #16 (the wake) · #10 · #13 · #25 · #71 · #87 · #88 (the two dispositions).

**Counts and cross-references re-derived.** Paragraph 2's "Seven" session rulings - seven are enumerated. §1's three formalisation questions plus a fourth, with (i)/(ii)/(iii) matching #85 §4's own numbering. §5's obligation position: seven fields in the table's *in* column, seven in the stated row. §5's progress position: four and four. §5's "`0038`'s seven with `state` re-typed, plus the handle" - arithmetic holds. §5's repaired line against band B "adds `done_by` and `optional`" - holds against `0038`'s band B and `0096`'s example. §7's "three fields on the rows the partition would have thinned, plus the progress position's two" - holds. §9's "three inputs" to #82 - three are listed. §10 item 2's "five places" in `0101` - five exist (locator error at R5). §10 item 5's "four places" in `0100` - four are identifiable. §10 item 14's "six #82 listed" - six, all disposed of. §10's items run 1-15 with no gaps. Every §N and issue cross-reference inside the draft resolves to the section or ticket it names.

**No `_Avoid_` violations.** I grepped the draft against every `_Avoid_` list in `CONTEXT.md`. The only hits are `deadline` (used in `obligation`'s own glossary sense, "a thing with a deadline", not as `due`'s field name), `validation` (in `0018`'s own phrase "link-set validation pass", not in the write-rule sense the glossary bars), and `mastery` (quoting `progress`'s *Avoid* list itself). `row` is used throughout but only for a ring 0 row, never for a line, and the draft's §5 makes the row/line distinction explicitly - `the line`'s *Avoid* bars calling a line a row, which the draft does not do. `edge` appears only for `0096`'s `<edge>` element and for an edge's `id`, which is `0101`'s own wording. `search`, `retrieval`, `view`, `entity`, `metadata`, `proposal`, `summary`, `the projection` (bare) do not appear.

**One observation outside this lens**, offered without a verdict: §3's must-list is a ruling (which judgments are *must*, and that *which items need Billy* is not) and §10 item 1 gives the new record §1, §2, §4, §5 and §7 but not §3. If the must-list is meant to bind - §4, §5 and §8 all derive from it - it has no home in `docs/adr/` and no open issue, which is the third case `drafts-and-rulings.md` says does not exist.

---

## Summary

**2 blocking, 7 repair.** Both blocking findings are the same seam at two removes: the draft rules that a routing path's position carries a derived field set and *not* the kind's line, and demonstrates in §5 that obligation's two sets differ in both directions - but §10 item 13 would land a `CONTEXT.md` clause asserting the line appears at a routing path's node position (B1, self-contradictory with the note the same item adds), and `0095`'s landed "A resolve's return (`0101`) is bounded in depth - every endpoint is one line" is disposed of nowhere in §10, though the draft cut `0101`'s citation of that very sentence for precisely this reason (B2). The seven repairs are all attribution or enumeration: `0091` cited one aspect over for the dangling-ref route (R4), three sentence/reading counts that name fewer items than their headers claim (R1, R2, R6), one amendment locator off by a sentence in `0101` (R5), one omitted upstream on #79 (R3), and one conflation of `0038`'s corpus argument with the claim it supports (R7). No quotation in the draft is inaccurate - every quoted sentence I checked against its record matched verbatim or as a faithful ellipsis - and no `_Avoid_` term is used in its barred sense. The attribution failures are all of the kind `reading-records.md` predicts: not misquotation, but a record cited for a neighbouring aspect, and a list read as exhaustive when it was written to answer a narrower question.
