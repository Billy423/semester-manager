# Review 18 - draft v9, lens 2 (falsification), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v9.md` and full repository read access. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-17. Blind to the lens-1 reviewer. Told that §5b is a draft section and that findings against it are repair.

**Report, verbatim:**

---

## Findings, most severe first

### B1 - §5's `parts` cell is falsified by §6, and §6's stated route for J0's absorption input is unavailable under §2, §3 and §5

**Section:** §5 (obligation position, `parts` row) and §6 (*What serves J0 today*). **Attack:** 1 and 2.

§5 excludes `parts` from the row, and the ground it states is:

> `parts` | J0 and J1 do not need *what this is about*; that is J2's, served by the `requires` crossing once concept nodes exist (#25). `0038`'s ground for excluding it holds on the new derivation | out; returns with any `look_at`

§6 says the opposite about J0:

> **Absorption** arrives by asking Billy, which `CONTEXT.md` calls one case of dispatch, under `0039`'s rule, over the concepts the coordinator can name - today the strings in `parts`, which the row does not carry (§5), so naming them costs a resolve of its own whose obligation position carries `parts` for that judgment (§2), or a `look_at` per obligation until then

So J0 - the one judgment §5 says the resident result serves, and the judgment whose declaration §6 attributes to Billy - **does** need *what this is about*: without `parts` the coordinator cannot name the concept it must ask about. The cell's stated ground is not what decides it, and it is contradicted three paragraphs later in a section that is ruled, not draft.

Both escape routes §6 offers are closed by the record's own rulings:

- *"a resolve of its own whose obligation position carries `parts` for that judgment (§2)"*. §2 rules that a position carries *"one field set per kind … derived by the criterion **for the judgment**"*, and §3 rules that a judgment is *must* only if it rests on a ruling. §5 derived J0's obligation position and put `parts` out; §3's must-list contains no other judgment that ranges over `parts` - J2 is *"which concepts each obligation requires"*, served by `MOVE(requires, points-at)`, and §3 itself says *"no concept node exists yet (#25)"*, so J2's chain reaches nothing. There is therefore no judgment under which such a resolve may carry `parts`.
- *"a `look_at` per obligation until then"*. That is the ~55-call read `0100`'s own refusal paragraph names - *"reaching a plan's inputs across five courses one `look_at` at a time is roughly 55 calls"* - and which `0101`'s effectiveness constraint bars in terms: *"the coordinator's call count may not grow with the graph."* §6 closes by asserting *"#82's refusal to widen ring 0 to supply the plan's inputs stands"*, and then offers exactly the read that refusal was reasoned against.

Run `0101`'s criterion, as §5 itself states it, over `parts` for J0: without it the coordinator cannot form the dispatch it must form, and its next call is forced to be n `look_at`s rather than chosen. Either the cell's verdict changes (and with it §5's ruled row, and the claim that the derivation *"lands on `0038`'s seven fields"*), or §6's route must change and J0's absorption input has no route at all. The record cannot hold both as written.

**Verdict: BLOCKING.** (Threshold (b) if the criterion admits `parts`; threshold (a)/(d) on the cell's stated ground either way. Ambiguous resolves to BLOCKING.)

---

### B2 - J4's chain returns its own start obligation, and the reading that drops `course ≠ start.course` does not cover it

**Section:** §3 (J4), §8 (position comparison). **Attack:** 3 and 8.

J4's chain, with the implicit `START(ref)` §3's preamble supplies:

```
START(ref A) · MOVE(requires, points-at)? · MOVE(requires, pointed-by)?[kind = obligation]
```

`requires` carries `obligation → concept` (`0012`). Crossing forward from A reaches the concepts A requires; crossing `pointed-by` back from each concept reaches every node that requires it - **including A itself**, which requires it by the link the first step just crossed. The `[kind = obligation]` selection does not exclude A; nothing else does either.

#85 §7's S6 carried `FILTER(kind = obligation and course ≠ start.course)`, and that predicate excluded the self-pair as a side effect (A's course equals A's course). §3 drops it:

> #85 §7's S6 predicate `course ≠ start.course` is dropped on that reading, and §8's parking of the position comparison rests on it

and §8 confirms *"J4 as derived from `0001` job 2 does not exclude the same-course case, so the judgment ranges over what the chain produces without the comparison."* The stated reading and its wake cover the same-**course** case only - *"Wake: the first real decision in which a same-course pair's inclusion mattered either way"* - and say nothing about the same-**obligation** case the drop also admits.

Whether A is returned is undefined under the draft's own type rulings. §2 rules two type questions (optional crossings, position field sets) and rules neither path simplicity nor node repetition; §11's grammar list carries *"how paths are deduplicated when one step matches twice"* but not *whether a path may repeat a node*, which `0101` leaves to the grammar and #85 §7's first application had provisionally answered *simple* - the answer that would have excluded A, and which this draft does not adopt. So a must-judgment's chain returns a member the coordinator must judge out, on semantics the record leaves open, with no reading and no wake - the exact failure §1 (iv) writes a discipline against.

**Verdict: BLOCKING** (threshold (d)). The repair is one sentence, either adopting simplicity for this chain or stating the reading with a wake.

---

### R1 - §11 homes the line debt at #82; §9 and §10 item 15 home it at a new deferred issue

**Section:** §9, §10 item 15, §11. **Attack:** 5 and 7.

§9: *"the debt itself is homed as one new deferred issue (§10), since no open ticket renders a line."* §10 item 15: *"**One new deferred issue** for obligation's line's field set."* §11: *"obligation's line's field set (owed, §5, **homed at #82**)."*

These are two different homes for one debt in one comment. §9's reason is correct - #82 renders ring 0's rows, not a line, and no open ticket renders a line - so §11 is the error.

**Verdict: REPAIR** (an attribution, no ruling changes).

---

### R2 - J4 and J8 are written with an implicit `START(ref)`, which under-states `0001` job 2 and makes both fetch rather than resolve

**Section:** §3 (J4, J8). **Attack:** 1.

§3's preamble rules *"A chain written without a start below starts from *this obligation*, `START(ref)`."* J4's title is *"which obligations require the same concept **as this one**"*, and its *ranges over* column is *"this obligation, the concept, the other obligation"*; J8's is *"which obligations build on **this one**"*.

Both cite `0001` job 2, whose ground `0001` preserves verbatim from `0100`: *"a statement about relations across obligations **rather than about any one of them**."* #85 §7's S6, the prior for J4, started by kind - `START(obligation) · MOVE(requires) · MOVE(requires, pointed-by) · FILTER(…)` - which produces every cross-obligation concept-sharing relation in one return. Anchored to one obligation, the same judgment over the whole set costs one resolve per obligation, which the effectiveness constraint bars.

The second half is sharper: anchored to a ref, J4 and J8 are a single node's neighbourhood, and `0096` already delivers that inside `look_at` - `<edge type="builds-on" direction="pointed-by">` with the obligation's line inside it. So as written they are served by **fetch**, not resolve, and add nothing to the must-list they are on. §8 half-notices this for J8: *"a `builds-on` neighbourhood in both directions at once is read [through `look_at`]."*

No form verdict moves - J2 already carries `MOVE(L, D)` from a start by kind, and admitting same-course pairs removes the need for a position comparison either way - so this changes cells, not rulings.

**Verdict: REPAIR**, but close to the line: §1 (ii) makes each judgment's declared range the input to the test, and these two declarations are narrower than their sources.

---

### R3 - "lands on `0038`'s seven fields plus the handle" is not what the derivation lands on

**Section:** paragraph 7 of the preamble (*How it was reached*). **Attack:** 2.

> The derivation lands on `0038`'s seven fields plus the handle, with `state` re-typed as a position, which is an independent confirmation of `0038`'s selection

It lands on `0038`'s seven, plus the obligation's handle, **plus `origin`, `updated_at` and the progress record's `id`** - three items `0038` never carried. §4's width paragraph states this correctly (*"and by the progress position's `id`, `origin` and `updated_at`"*), and §5's own summary line lists `id · state · origin · updated_at` at the progress position. The preamble's summary overstates the coincidence with `0038` and therefore the strength of the "independent confirmation" claim.

**Verdict: REPAIR** (a wording; §4 and §5 already carry the accurate statement).

---

### R4 - §5's `detail` cell decides on a step §2 does not rule, and leans on the channel §4 has just ruled out of this read

**Section:** §5 (progress position, `detail`). **Attack:** 2.

> `detail` | the kind's one free-text field, and a position is of line depth by §2's type ruling, which free text fails; the content arrives through `look_at`'s channel. Under the criterion alone it would be arguable … and the type bound is what decides it

§2's type ruling says a position carries *"one field set per kind, of line depth"* and that *"a position carrying a block would carry depth the discard (`0043`) and `0095` bar."* It nowhere says free text fails line depth. What actually bars free text from a line is `0082` rule 3 (the one free-text field is the element's **text content**) plus `0097` (*"a line is self-closing"*, and *"an element with a text field and no sections closes itself too"*) - two **render** records, applied to a routing position; and the cell's second clause (*"the content arrives through `look_at`'s channel"*) is `0046`, which §4 has just ruled *"is not the read it governs"*.

The verdict is right - `0035` keeps `detail` beside `state` for a reason that is about the stored record, not the resident row - but the deciding ground as written is not established, and it is an instance of the transfer-from-a-render-record move the preamble's method finding says this draft stopped making.

**Verdict: REPAIR** (the verdict does not change).

---

### R5 - §1 (iv)'s discipline is unmet for two supersets the standing intent returns, one of them a live, dated distortion

**Section:** §1 (iv), §4. **Attack:** 8.

§1 (iv) binds itself: *"wherever the standing intent returns a member the coordinator then judges out, this record either shows no must-judgment ranges over the narrower set (§4, *the active ones*) or states the reading under which the member is in and wakes it (§4, `optional` and `done`)."* §4 discharges this for the active window, `optional`, `done`, the undated obligation, the dangling-`course` obligation and the term. Two remaining cases are discharged neither way:

- **The mis-shaped conference row.** #13's body: a conference *"currently carries an obligation row **only because that is the only row-bearing kind available**"* and *"That is a known, dated distortion in the stored corpus, not a hypothetical."* #80's own fixture carries it (`("IDEA Conference", "in_progress", …)` in `prototype/collection-render/corpus.py`). `START(obligation)` puts it in the resident result; J1 is *what is owed* and a conference sitting is not owed; the coordinator judges it out on every read and no field on the row tells it to. The right disposition is available - the distortion is #13's and #48's - but the record does not say so.
- **A dropped course's obligations.** #85's S7 (*"the obligations of the courses Billy annotated 'dropped'"*) is disposed of in §3 as *"§8's"*, i.e. as a question about the Ref-field crossing form. Its membership half is untouched: those rows are in the resident set, they are not owed, and the row shows neither the course's annotation nor anything else that would say so. Here the first branch of (iv)'s discipline is satisfiable and cheap - nothing in the model represents *dropped*, `category` is an open string set with an owed write rule (`0036`), so no ruled source names a judgment over the narrower set - but the record does not state it.

**Verdict: REPAIR** (each is one sentence; neither changes the intent).

---

### R6 - §6 applies `0039` to a set that is not the judgment's set

**Section:** §6. **Attack:** 6.

`0039`: *"observe(X) is permitted for a judgment over set S iff X is affordable for every member of S, else dispatch(X, member)"*, and *"Symmetry is scoped to the set the judgment ranges over."* §3 declares J0's set to be J1's set - obligations. §6 then routes absorption *"over the concepts the coordinator can name"* and calls *"how far along are you with X"* a per-member answer *"which is the shape `dispatch(X, member)` returns"* - where the member is a **concept**, not a member of the set J0 ranges over.

The mismatch is not fatal to the ruling, but it leaves `0039`'s actual bite unaddressed: symmetry over J1's ~55 obligations means asking about every obligation's concepts or none, and `0037` row 1's adversarial correction (*"asking is only a remedy for a quantity the user can answer"*) plus #10's ask-frequency measurement bear on whether that is affordable. §6 parks only the adjacent question - *"whether dispatch calls count against the effectiveness constraint"* - and §11 repeats it.

**Verdict: REPAIR** (one sentence naming the set the observation is per-member over, and its relation to J0's set).

---

### R7 - §5's `due` cell's only stated ground routes through `0042`'s present content

**Section:** §5 (obligation position, `due`); §4, §7. **Attack:** 4.

> `due` | J0's input: which obligations are near is the coordinator's judgment against today, made with `due`, `done_by` and `state` (§4) | in

*Near* is `0042`'s three triggers; §7 re-homes them as *"the coordinator's judgment rule"* and §4 attributes them to Billy in session, but the field's admission still runs through the clause `0100` says was never derived. `done_by` and `state` each carry a second, independent ground in their own cells (*"Billy's chosen target date"*; *"what is owed turns on it (J1)"*); `due` carries none. Independent grounds are available and unused - `CONTEXT.md`'s `obligation` entry (*"A thing with a deadline"*), so *what is owed* is not statable without it, and `0041`'s order over the row.

**Verdict: REPAIR** (the verdict does not change; the ground should not be the one record the ticket exists to re-derive).

---

### R8 - §5 settles `has-more`'s *whether*, which #82's body claims by name

**Section:** §5 (`has-more`), §9. **Attack:** 5.

#82's body, on its first orphan: *"`0092` rules what it carries; **this rules whether and where it appears**."* §5 rules it in and §9 says so plainly - *"`has-more`'s *whether* is settled here … and its name and position stay #82's own"*. The draft is on defensible ground, because #82's own *must not be re-opened* list says #82 *"decides how they render, **never which fields they hold**"*, and selection is #86's. But that is a conflict internal to #82's body, and the draft resolves it silently rather than naming it as one.

**Verdict: REPAIR** (say that #82's body contradicts itself here and which half is being kept).

---

### R9 - §10 item 7 removes `0095`'s stated ground for a ruling it leaves standing

**Section:** §10 item 7. **Attack:** 7.

The three `0095` sentences to be replaced include *"A line that picked each row's own band would import `0038`'s **residency** computation into a **read**."* That sentence is the ground for the sentence immediately before it, which item 7 leaves in place: *"a line is **one** field set per kind and does not vary per row."* Replacing it with the line-debt pointer leaves a surviving ruling with no reasoning attached, in a record whose own subject is that a line's field set is not derivable.

**Verdict: REPAIR** (restate the ground without the band vocabulary rather than deleting it).

---

### R10 - `0092`'s opening sentence is left as a listed pointer debt, against `0084`'s own discipline

**Section:** §10 item 14. **Attack:** 7.

`0092` opens *"`0038` puts `has-more` among **band A's** routing fields without saying what it holds"*, and its Source line closes *"The field's membership in band A is `0038`'s."* After §10 item 4 there is no band A. The draft lists this as a pointer debt *"listed rather than fixed, per #82's precedent"*. `0084` set the opposite precedent on the same kind of clause and gave the reason: *"a wrong number left in place gets cited; a banner is not read by the reader who arrives via a quotation"* - and struck the clause at source. Two sentences in `0092` are cheap to repair and are the first thing a reader arriving at `has-more` by quotation will read.

**Verdict: REPAIR.**

---

## Attacks that produced nothing further

**Attack 1 (a missing must-judgment).** I ran `CONTEXT.md`'s opening sentence clause by clause (*what is owed* → J1, *what each obligation requires you to know* → J2, *where the material that teaches it lives* → J3), `0001`'s three jobs (job 1 → no judgment, argued; job 2 → J4, J8; job 3 → J6 via `0003`) and its requirements sentence (→ J7). The candidates I built that are not on the list all dissolved into stated parkings with wakes: `prepares-for` and `spec`'s `owed` role as second routes to material, `sticky_note`s as a set, lecture progress, and *which items need Billy*. A judgment over `course` nodes dissolved too - nothing ruled names one, and §4 says so. The one survivor is R2's narrowing, and B1's input gap.

**Attack 2 (the criterion over both field sets).** I rebuilt obligation's field inventory from `0025`, `0027`, `0028`, `0029`, `0031`, `0032`, `0033`, `0037`, `0038` and `CONTEXT.md`, and progress's from `0028`, `0035`, `0036`, and checked both against `prototype/collection-render/corpus.py`. §5's lists are complete; nothing is admitted that §5 omits except `parts` (B1). `created_at`'s exclusion looked like a candidate - `0099` calls the pair jointly *"what makes a time-bound statement safe to store at all"* - but `0099` attaches *"that silent influence is **the actual harm**"* to `updated_at` alone, so the cell quotes the right half and the split holds. `grade_share`'s cell dissolved as a finding: the record openly demotes the criterion's verdict to open and closes the cell on `0038`'s corpus argument, which speaks about the same aspect (what ring 0 holds) and which `0100` records as surviving audit; §11 carries the open half.

**Attack 3 (break a chain).** I walked the standing intent and J2, J3, J4, J7, J8 against `0012`'s signatures and directions; all are well-formed, and §2's two consequences (optionality scoping over the whole selection, and an empty position propagating with the member kept) correctly close the `sticky_note`-only case and the no-`requires` case that would otherwise drop members. The `done` alternative filter §4 writes is well-formed under the admitted forms. `0035`'s *"no `about` link is legal"* progress record is unreachable from the intent, but no must-judgment needs it. Only J4's self-return survived (B2).

**Attack 4 (reasoning from `0038`'s or `0042`'s present content, or from #85 §7's scenarios).** §3's disposition of S1-S7 is clean - each is derived from a listed source or parked - and §5's use of `0038` as an **inventory** of obligation's fields is declared in place (*"A field named in none of them would be invisible to the derivation"*), which is the honest form of that dependency. `0038`'s ground for excluding `parts` is asserted to hold *"on the new derivation"* rather than borrowed, and `0038`'s corpus argument is used as an independent argument with the criterion's verdict left open. Only `due`'s cell (R7) reasons from `0042` without a second ground.

**Attack 5 (decisions §11 or a sibling owns).** I checked §11 line by line against §0, §2, §4, §6 and §8 and found them consistent except R1's double homing. #13, #14, #25, #71 and #87 are each touched only by a comment or a pointer, and the time projection's residency is #85 §10's explicit assignment to this ticket. #88 keeps *whether `nodes_without` is separately named*. Only #82's `has-more` orphan (R8) is a real overlap.

**Attack 6 (size and absorption).** The reading of `0037` row 1 as non-exhaustive on the answer's shape is `reading-records.md`'s own rule applied correctly, and the withdrawal of the earlier between-members ruling is the demotion `drafts-and-rulings.md` asks for. Declining the `0042` importance permission is consistent - the sentence's own consequence is about *a rule promoting rows*, not about an input Billy supplies. `0010`, `0033`, `0056` and `0100`'s refusal are each cited for what they say. The `parts` conflict between `0037` row 1 and `0033`/`CONTEXT.md` is real and correctly resolved on the glossary's side. Only the set mismatch (R6) survived, plus B1's route.

**Attack 7 (the line paragraph and §2's position ruling).** `0082`'s transfer really is sourced on band B, `0095` really does read *the band* as band B, and both really do lose their source when band B dissolves; `0096`'s worked example printing `state` on an obligation line was already true before this draft and is correctly left as the landed shape; `0097`'s `id`-marks-an-object rule is what makes the progress position addressable and its absence the `not_started` signal, which §5 uses correctly; `CONTEXT.md`'s *"`progress` needs no line"* survives, and the *"A line is what a path's endpoint renders as inside a block"* note is correctly qualified. Only R1, R9 and R10 survived.

**Attack 8 (§1 (iv) over every included member).** The standing intent's included-and-judged-out cases are the active window, `optional`, `done`, the undated obligation, the dangling-`course` obligation, a second term's obligations, a `sticky_note`-only obligation and a multi-progress obligation; each is discharged by one branch of (iv)'s discipline. The two that are not are R5's. J4's self-return is B2.

---

## Summary

**2 blocking, 10 repair.** The two blocking findings are both about a member or a field the record's own machinery admits and its own text then treats as absent: §5 rules `parts` out on a ground §6 falsifies, while §6's only routes to J0's absorption input are a resolve §2 and §3 make unavailable and a per-obligation `look_at` that `0100` and `0101`'s effectiveness constraint were written to refuse; and J4's chain, once #85's `course ≠ start.course` predicate is dropped, returns the start obligation as its own answer under semantics the draft leaves to the grammar, with no reading and no wake. Neither reaches the standing intent itself, which survives every construction I could put to it - the `obligation` start, the optional `about` crossing with its whole-selection scope, and the empty-position signal are sound against `0012`, `0018`, `0026`, `0029`, `0035` and `0091`. The ten repairs are concentrated in three places: grounds borrowed from render records or from `0042` where an independent ground was available (R4, R7), the two-way homing and scope notes for the line debt and `has-more` (R1, R8, R9, R10), and cases §1 (iv)'s own discipline reaches but the record does not discharge (R5, R6, R2, R3).
