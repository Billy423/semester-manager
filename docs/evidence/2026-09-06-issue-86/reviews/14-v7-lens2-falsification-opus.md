# Review 14 - draft v7, lens 2 (falsification), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v7.md` and full repository read access. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-13. Blind to the lens-1 reviewer.

**Report, verbatim:**

---

## BLOCKING 1 - §3 J1, §4, §1 (iv): a completed obligation is never disposed of, and the standing intent is then the superset move

**Section:** §3 (J1's *ranges over*), §4 (*Why there is no predicate*), §1 (iv). **Attack:** 8, and 1.

The draft asks its §1 (iv) question of exactly one field. §3's J1 cell: *"the obligation position; whether an `optional = true` obligation is owed is read as yes (§4)"*. §4: *"**One reading is assumed and stated:** an `optional = true` obligation is owed - it is a thing with a deadline the course offers - so `START(obligation)` produces J1's set exactly rather than a superset with the deciding field visible, which §1 (iv) would not accept"*, with a wake attached, and §11 carries it as undecided.

It never asks the same question of `state = done`. `0035` rules `state : not_started | in_progress | done`, and J1 is *what is owed*, whose source is `CONTEXT.md`'s opening sentence. If an obligation whose progress record says `done` is not owed - which is the plain reading, and at least as plain as the `optional` reading the draft felt obliged to state - then `START(obligation)` returns exactly what §1 (iv) forbids: *"a chain that returns a wider set with the deciding field visible on every member"*. The deciding field is visible on every member, at the progress position the same intent reaches, by §5's own row (`state` in).

Three things make this a defect rather than a gap in coverage.

The draft's own §4 disposes of the neighbouring case, *the active ones*, on the ground that *"No ruled source names a judgment that ranges over the active ones as a set: the opening sentence says what is owed"*. That ground is unavailable here, because the opening sentence's *what is owed* is precisely the judgment at issue.

The admitted forms can express the narrower set in one return, so this is not a forms gap: `START(obligation) · FILTER(not exists(MOVE(about, pointed-by)[kind = progress and state = done])) · MOVE(about, pointed-by)[kind = progress]?` uses `not`, `exists` and a selection at a node position, all admitted by §1 (iii) and §9. Because the set is producible, threshold (b) is not what fires; what fires is that §4's ruling *"`START(obligation)` produces J1's set exactly"* is asserted on the `optional` reading alone and is false under the `done` reading, which the draft neither states nor wakes.

A predicate inside the optional crossing cannot substitute. §2 rules *"an optional step is empty when nothing satisfies the step's whole selection"*, so `MOVE(about, pointed-by)[kind = progress and state ≠ done]?` keeps the done obligation with an empty progress position rather than dropping it - the draft's own optionality rule makes the obvious spelling silently wrong.

**The repair is the one the draft already knows how to make:** state the reading (a done obligation is still owed, or is not), give it a wake as `optional` has one, and add it to §11. What may not stand is silence, because §1 (iv) was written to forbid exactly the move that silence licenses.

**Verdict: BLOCKING.**

## BLOCKING 2 - §2 vs §3: `kind` is admitted at the one position whose step fixes it

**Section:** §2 (the field-set-per-kind paragraph), §3 (J4's *served by*). **Attack:** 2.

§2 rules: *"The same rule that keeps a link's kind off a relation position keeps a node's `kind` off a node position whose step fixes it… `kind` passes only where a step reaches more than one kind - J4's second crossing does, since `requires` has two signatures (`0012`) - and there it is what tells the positions apart."*

§3 writes J4's chain as `MOVE(requires, points-at)? · MOVE(requires, pointed-by)?[kind = obligation]`, and glosses it *"the second crossing reaches concepts too by `0012`'s second signature, so the selection names the kind"*.

The selection fixes the value. §2 states that rule itself, one paragraph down, for `role`: *"the same holds of `role` wherever a chain selects on it, which J7's does - `[role = given]` fixes the value on every path it returns, so the position cannot be what tells the coordinator whether the artifact is worth the call."* Substitute `kind` for `role` and J4's second position for J7's relation position and the argument is unchanged. The coordinator wrote `[kind = obligation]`; it holds the kind before the result arrives; the position cannot tell it anything. So `kind` is out at J4's second position by §2's own rule, and §2's stated exception names no instance at all.

Two consequences confirm it. Run the rule over every chain in §3: the standing intent selects `[kind = progress]` (§5's progress table says `kind` out *"fixed by the step's selection"*, correctly); `START(obligation)` fixes obligation; `requires` points-at from an obligation reaches `concept` only; `covers` pointed-by from a concept reaches `artifact` only; `spec` points-at reaches `artifact` only; `builds-on` reaches `obligation` only. Under the draft's own rules no position in any listed chain carries `kind` today. And if `kind` did pass at J4's end position it would not pass at J4's start, which `START(obligation)` fixes - falsifying §2's other clause in the same paragraph, *"One kind at two positions of one result - J4's `obligation` at its start and its end - carries one set, derived for that judgment, at both."*

Paragraph 3 records the seventh draft as repairing precisely this seam - *"`kind` passes only where a step reaches more than one kind, one set per kind per result"*. The repair reached the rule and not J4.

**Verdict: BLOCKING.**

## BLOCKING 3 - §2, §5 vs `0095`: the sentence "every endpoint is one line" is contradicted and is not in §10

**Section:** §2 (position content), §5 (the progress position), §10 items 2 and 7. **Attack:** 7.

§2 rules *"A position's field set is not the kind's line"*; §5 rules *"The progress position's set is a position's set and not a line"*; §10 item 2 accordingly drops `0101`'s citation of `0095` for *one set per kind*, *"since a position's set is not a line"*.

`0095` states, in its consequence section and not in its line-field-set section:

> **This is true of a block.** A resolve's return (`0101`) is bounded in depth - every endpoint is one line - and unbounded in width; what gates that width is not yet ruled.

That is the same claim the draft strikes from `0101`, in a landed record `0095`, said of a resolve's return in so many words. §10 item 7 announces *"`0095`, three sentences"* and reaches only into the *"The line's field set is not derivable"* section: *"`0095`'s 'so the band is band B' and its opening sentence of the same section"* are replaced, and *"its no rule generates a new kind's line is untouched"*. The consequence sentence is in a different section and is untouched by any item in §10.

So `0095` continues to say that a routing result's endpoint is one line while §2 and §5 rule that it is not. Threshold (c).

**Verdict: BLOCKING.**

## BLOCKING 4 - §2's "membership is the criterion's alone" is falsified by two of §5's own cells

**Section:** §2 (membership), §5 (`grade_share`, and the progress `id`). **Attack:** 2.

§2 rules: *"**Membership at a position is the criterion's alone;** `0097`'s rule that a member omits what its container fixes is a render rule about restating, and it decides nothing here."* It reinforces this twice more, that a render *"decides nothing here"* and that a line *"is a render (`CONTEXT.md`, the line), which decides nothing at a position"*.

§5's `grade_share` cell decides membership by something else, and says so: *"J1 does not turn on a share, and J0's stated inputs are size and absorption - a statement of what is hard to do without, not an exhaustive list, **so the deciding ground is `0038`'s independent corpus argument**, which §10 keeps: a rendered column of shares reads as a partition of the grade that it is not."* The cell concedes that the criterion does not decide the field, and then decides it by a **render** harm - what a *rendered column* does to a reader - which is exactly the class of ground §2 rules out at a position, and which is #82's by the draft's own §9 and §11.

§5's progress `id` cell does the same in the other direction: *"addresses when the record exists; a defaulted `progress` carries none and that absence is the signal (`0082`)"*, verdict *"in, structurally"*. The absence-as-signal ground is `0082`'s, not the criterion's, and the hedge *structurally* concedes it.

The field verdicts themselves may well survive - a ruled ground for keeping `grade_share` off a resident row is available and unused, namely `0042`'s surviving sentence that *"`grade_share` has no reader by standing exemption"*, which §6 and §7 both keep, and putting the field on a resident row supplies it a reader. What does not survive is §2's ruling. Either the criterion is not membership's sole ground and §2 must say what the other grounds are, or these two cells are not derived.

**Verdict: BLOCKING.** (The verdicts do not move; the ruling in §2 does, which is why this is not a REPAIR.)

## BLOCKING 5 - §5 rules the line in the sentence after saying it does not

**Section:** §5 (*Row and line are two things*), §10 item 7, §11. **Attack:** 5.

§5: *"**This record rules the row and does not derive the line.**"* Two clauses later it rules the line: *"the clause is repaired to the least that keeps it true: obligation's line is the obligation position's field set minus `has-more`, with `state` carried as `0096`'s worked example already carries it - `id · name · due · done_by · optional · course · state`… and `0096`'s example is repaired to carry them (§10)."* §10 item 7 amends `0082` in two places, `0095`, and `0096`'s worked example to match.

Three things make this more than a wording problem.

The criterion that decides a line is declared unrun in the same paragraph: *"Whether the criterion, run over a neighbour as §5 ran it over a row, also transfers `origin` and `updated_at`… is the line's own question, **owed and not run here**"*, and §11 repeats it. A field set fixed without the criterion that decides it is a transfer, which is the defect `0100` names against `0038` (*"An argument that stands is still not a derivation"*) and which `0082` confesses about the line in the first place (*"obligation's line is ring 0's band by a transfer of the field set, not of a render"*). The draft replaces one transfer with another and calls the source repaired.

`0095` rules that a line's field set *"is one ruling per kind"*. This is such a ruling, made for `obligation`, at a ticket whose §5 says it does not derive the line and whose §11 lists the line's field set as owed.

The `state` component is carried by a **worked example** in `0096`, which the same item amends - the record is cited as authority for one field and repaired for two others in one sentence. Paragraph 3 records the fifth review round catching *"the line's field set transferred from `0096`'s example rather than derived"*; the transfer is still doing load-bearing work.

The demotion `docs/agents/drafts-and-rulings.md` asks for is one sentence: band B dissolves, so obligation's line's field set is **owed** pending the criterion-run, and `0082`, `0095` and `0096` are pointed at that debt rather than at a new field set.

**Verdict: BLOCKING.**

## BLOCKING 6 - §6 and §11: `0037` row 1 does not rule that an ordinal answer cannot be a per-member value

**Section:** §6 (both size paragraphs), §11, and the draft's paragraph 2. **Attack:** 6.

The draft's whole size ruling turns on one reading of one row. §6: *"Size is not placed under `0039` at all: `0037` row 1 rules that the only answer available is an ordinal comparison, **a relation between two members**, and neither `0039`'s per-member dispatch nor a per-member field holds one."* And again: *"`0037` row 1 rules that the only answer available is an ordinal comparison, 'not hour counts' - a relation between two members - and `0039`'s dispatch returns a value of one member in the same shape as every other's, which has no position for a relation."* And §11: *"how size reaches J0 before that record exists, since the ordinal answer `0037` allows is not a per-member value (§6)"*. Paragraph 2 states it as one of the seven session rulings.

`0037` row 1, in full:

> The world does not supply it, it is not a unit anyone thinks in, and its null is not a gap. Size, where it matters, is **observed rather than stored** - ordinally, from `parts` and item notes first, then by asking for a relative comparison. Adversarial correction, attached the same day and part of the ruling: **asking is only a remedy for a quantity the user can answer, and the answers available are ordinal comparisons, not hour counts**

The contrast the row draws is **ordinal against cardinal** - *"ordinal comparisons, **not hour counts**"* - and not per-member against relational. An ordinal scale (small / medium / large, or a rank within the set) is a per-member value, and it is exactly what *not hour counts* permits and what *not a unit anyone thinks in* asks for. The row's own first-named sources are `parts` and item notes, both per-member. The one phrase that carries the draft's reading, *"asking for a relative comparison"*, is a description of how the answer is obtained, not a type constraint on what is stored, and the row's subject sentence is *observed rather than stored* - which is `0039`'s dispatch branch by name.

This is `reading-records.md`'s named failure: a record about **how a value is obtained** read as a rule about **what type the value is**. If the weaker reading holds, size falls under `0039` beside absorption, §6's stated gap (*"how size reaches J0 today is open"*) closes, §11's clause is wrong, and paragraph 2's ruling is stated wider than its evidence. The reading is at minimum ambiguous, and the record does not support the ruling it is cited for.

I note the draft's own hedge - *"the instance may show that size is a relation across the set… and that is noted for the wake and not ruled"* - which is the right posture and is contradicted by the flat assertions above it.

**Verdict: BLOCKING** (threshold (a); ambiguity resolves this way by the review's own rule).

## REPAIR 7 - §4 and §5 ground `state` as a J0 input on `0042`'s present content

**Section:** §4 (*Why it reaches `progress`*), §5 (`state`), §3 (J0's *ranges over*). **Attack:** 4.

§4: *"`state` is J0's input - in-progress work is one of the three triggers Billy stated"*. §5: *"J0's input; the trigger `0042` stated as `state == in_progress`"*. §3's J0 cell sources its *ranges over* to §4.

The three triggers are `0042`'s content, which `0100` diagnoses as an un-derived clause and which `0101` bars from constraining the derivation (*"no clause's present content constrains routing"*), and which §7 of this same draft dissolves as a property of ring 0 while re-importing it here as the ground for the standing intent's second position. §6's record of what Billy actually said in session is *"an obligation's size and the owner's absorption"* - `state` is not among them, and §5 itself calls that list *"not an exhaustive list"*, which is not a source.

The ruled ground available and not taken is the opening sentence's *what is owed*, since whether an obligation is owed plainly turns on whether it is done. Taking it forces BLOCKING 1's question, which is presumably why it was not taken.

**Verdict: REPAIR** (an attribution; the progress position survives on the better ground).

## REPAIR 8 - §5 over-reads `0012` for the progress position's `has-more`

**Section:** §5 (progress table, `has-more`). **Attack:** 2.

The cell reads: *"a `progress` node's only link is the `about` the path just crossed, so the set is fixed by the step and tells the coordinator nothing."* `0012`'s signature is `about : annotation → any`, and `any` includes a `progress` node, so a `sticky_note` may point at a progress record and the set is not fixed by the step. The verdict `out` survives on the criterion; the stated ground does not survive `0012`.

**Verdict: REPAIR.**

## REPAIR 9 - §3's chains for J2, J3, J4, J7 and J8 have no start

**Section:** §3 (*served by*), §9 (#88's admitted-forms list). **Attack:** 3.

J2 is *"`MOVE(requires, points-at)?`"*, J4 *"`MOVE(requires, points-at)? · MOVE(requires, pointed-by)?[kind = obligation]`"*, J7 *"`MOVE(spec, points-at)[role = given]?`"*, J8 two bare `MOVE`s. None names a start, so the set each produces is undetermined: J2's judgment says *each obligation*, which needs `START(obligation)`; J4's, J7's and J8's say *this obligation*, which needs a start by ref. §1 (ii) makes each judgment declare what it ranges over and §1 (iv) counts the set, and neither can be run against a chain whose first position is unstated.

`START(ref)` is not in §9's admitted-forms list and is disposed of nowhere. §1 (iii)'s grain rule would do it in one clause - it is a spelling of `START(K) · FILTER(id = X)`, both admitted - and #85 §7 flagged it as the grammar's to keep or drop. One sentence closes it.

**Verdict: REPAIR.**

## REPAIR 10 - §3's dismissal of `0001`'s first job rests on a composition that returns nothing

**Section:** §3 (*Sources*). **Attack:** 3.

§3: *"its first job, the reload, names no judgment of its own, since a chain that reaches the material in one return is J1 composed with J2 and J3."*

J1's *served by* is *"the standing intent (§4)"*, whose last position is `progress`. Composing J2 onto it crosses `requires` from a `progress` position; `0012` gives `requires` no signature from `progress`, so under §2's optionality rule the step is empty for every member, J3's step from an empty position is empty again, and the composed chain returns every obligation with no concept and no artifact. The claim is true only if J1 contributes `START(obligation)` alone, which §4's own linear-path argument (*"the linear path type is why obligation cannot both be the start and sit between `course` and `progress`"*) makes a different chain from J1's served-by.

The dismissal of job 1 is probably right; as written its ground does not hold, and the ground is what carries a ruled source off the must-list.

**Verdict: REPAIR.**

## REPAIR 11 - §11 lists one of §8's three parkings

**Section:** §11 against §8 and §9. **Attack:** 5.

§8 parks three things in the same words and calls parking a verdict: *"under the test's biconditional no must-judgment needs it is the verdict **not admitted today**, which is what parking means here"* - the Ref-typed-field crossing, the position comparison, and `or`. §9's #88 bullet lists all three. §11 lists only *"the position comparison's admission (§8, parked)"*. Either parking is a decision and none of the three belongs in *what this ticket does not decide*, or it is not and all three do.

**Verdict: REPAIR.**

## REPAIR 12 - §6 says `0010` permits an owner-authored absorption record; §11 says it needs a ruling against `0010`

**Section:** §6 (*Absorption's target is a concept*) against §11. **Attack:** 6.

§6: *"Owner-authored, which `0010` permits; not the system-inferred mastery `0010` bars."* §11: *"…and one on a `concept` against `0010`'s stateless clause besides."*

`0010`'s first sentence is wider than its title: *"The modelling layer records no state about the owner: it presents concepts and leaves judgment to him."* A stored absorption value on a `concept` node is state about the owner in the modelling layer, whoever authored it. §11 is right and §6 overstates the permission.

**Verdict: REPAIR.**

## REPAIR 13 - §6's absorption route is typed over a set it does not range over, and contradicts §6's own reachability sentence

**Section:** §6. **Attack:** 6.

§6: *"**Absorption** arrives by asking Billy, which `CONTEXT.md` calls one case of dispatch, under `0039`'s rule: how far along are you with concept X is a per-member answer, which is the shape `dispatch(X, member)` returns."* Two paragraphs earlier: *"It is two crossings from an obligation (`requires`, then `about`) and behind a layer that does not exist (#25), so it is **unreachable today** whatever its shape."*

Both cannot be read flat. And `0039` scopes its formalism to *"the set the judgment ranges over"*: J0 ranges over J1's set, which is obligations, while absorption is a per-**concept** value. `dispatch(absorption, member)` over J0's set is not typed, which is a variant of the objection §6 raises against size, unaddressed for absorption. Say which set the dispatch runs over, and reconcile *arrives by asking* with *unreachable today*.

**Verdict: REPAIR.**

## REPAIR 14 - §8's `or` paragraph contradicts §3's J8 cell

**Section:** §8 (*`or` has no must-judgment*) against §3 (J8). **Attack:** 5.

§3: *"no judgment ranges over both directions at once, so no union and no new form."* §8: *"J8's two directions are served the same way when both are wanted at once."* If no judgment wants both at once, the sentence describes nothing; if one does, it is a union and `or`'s disposal needs the argument. The intended reading is presumably the wildcard crossing through `look_at`, ruled at #85; say so.

**Verdict: REPAIR.**

## REPAIR 15 - §2 requires a field set per kind per judgment and §11 lists only three of the debts

**Section:** §2, §3 (J4's *ranges over*), §11. **Attack:** 5.

§2: *"A result carries one field set per kind… **derived for the judgment** by the criterion… One kind at two positions of one result - J4's `obligation` at its start and its end - carries one set, **derived for that judgment**, at both."* §5 derives the obligation position's set *"for J0 and J1, which are the judgments the resident result serves"* and for no other judgment. J4's and J8's obligation-position sets are therefore owed, and §3's J4 cell already asserts part of one - *"with `course` on each end"* - without deriving it.

§11 lists position debts only for `concept`, `artifact` and `course`. Add the obligation position's set for the judgments other than J0 and J1, or say why it transfers.

**Verdict: REPAIR.**

## REPAIR 16 - §10 item 7 announces three sentences of `0095` and names two

**Section:** §10 item 7. **Attack:** 5.

*"`0082`, two sentences; `0095`, three sentences; `0096`, one example"*, then two `0095` sentences are named and a third is declared untouched. Name the third or change the count. (BLOCKING 3 is the candidate for the missing one, and would change the section as well as the count.)

**Verdict: REPAIR.**

---

## Attacks that produced no finding

**Attack 1, the must-list's completeness against the ruled sources.** I re-derived the list from `CONTEXT.md`'s opening sentence and `0001` as rewritten: the opening sentence's three clauses give J1, J2 and J3; job 2 gives J4 and J8; job 3 gives J6 through `0003`; the requirements sentence gives J7; job 1 is the reload. I looked for a fourth judgment in the requirements sentence - *helping model an assignment's requirements* also reaches `spec`'s `owed` role, the deliverable - and found it parked with J7's wake in §3's *candidates not on the list*, with the enum reading disclosed as this record's own. I checked every *served by* cell against `0012`'s signature table and every direction against `0096`'s `points-at` / `pointed-by`, and found all seven chains well-typed and each a single chain. The only cell that is not one chain is J0's, which the draft states openly and lists in §11. The residue of this attack surfaced instead as BLOCKING 1 (J1's own set) and REPAIR 9 and 10 (chains without starts, and job 1's composition).

**Attack 3, a chain that drops a member or returns what `0043` / `0095` bar.** I ran the standing intent against an obligation with a `sticky_note` and no `progress` (kept, by §2's whole-selection rule, which the draft derives correctly), against a dangling `course` ref (kept, which is §4's whole ground for starting at `obligation`), and against J3's second optional crossing from an empty first position (kept, by the step-from-empty rule). I checked what each position carries against `0043`'s discard and `0095`'s depth bound: `detail` is excluded on the line-depth type rather than on the criterion, which is the right order, and `origin` is not a free-text field under `0028`'s one-per-kind cap, so nothing unbounded reaches a position. The two multiple-progress-records and deduplication hazards are parked in §11 with the reading they rest on named. What this attack did produce is REPAIR 10.

**Attack 4, reasoning from `0038`'s or `0042`'s present content or from #85 §7's scenarios back to the purpose.** `0038` is used in §5 only for the existence of fields in `obligation`'s table, which is the one use `0100` leaves open, and §5 states that use and its blind spot. #85 §7's scenarios are disposed of one by one in §3 and S6's predicate is explicitly dropped from J4, with J8 derived the same way. The one live instance is `0042`'s triggers standing as the ground for `state`, which is REPAIR 7.

**Attack 6, size and absorption against `0100`, #82 and `0010`.** `0100`'s refusal to widen ring 0 - *"Making it supply what the plan needs was argued at #82 and rejected"* - looked like a live contradiction, because J0 is the plan's judgment and four row fields are admitted as J0's inputs. It dissolves: `0100`'s refusal was refusing size and load onto the row, §6 declines to put either there, and the fields admitted for J0 (`due`, `done_by`, `optional`, `course`) were already in `0038`'s band A. §6's treatment of `0042`'s importance sentence is consistent with §7 and with `0042`'s own overturn note, and the demotion is stated rather than hidden. What this attack produced is BLOCKING 6 and REPAIR 12 and 13.

**Attack 7, the position / line / row trichotomy.** §2's ruling that a position's set is not a line, §5's derivation that obligation's row and line differ in both directions (`has-more` one way, `state` the other), and §5's handling of `CONTEXT.md`'s *`progress` needs no line* are consistent with each other, with `0097`'s self-closing rule and with `0082`'s *a ring 0 row is not a line*. `0096`'s `<edge>` carrying `id`, `type` and `direction` is correctly separated from a path's relation position, and `0093`'s names row is listed as a pointer debt. The trichotomy is applied consistently at both node positions and at the relation position. What this attack produced is BLOCKING 3, which is a missed amendment rather than an inconsistency in the trichotomy itself.

---

## Summary

**Six blocking, ten repair.** The blocking findings cluster at one seam and one habit. The seam is that §2's rulings are stated as general and then falsified by the very cells §3 and §5 write under them: `kind` is admitted at the one position whose selection fixes it (BLOCKING 2), and membership is declared the criterion's alone and then decided twice by something else (BLOCKING 4). The habit is that the draft's method - state the reading, attach a wake, demote to what the evidence supports - is applied to `optional`, to the term, to the width bet and to `0035`'s one-record reading, and is not applied at three places where the same move is owed: a completed obligation's membership in *what is owed*, which leaves the standing intent as exactly the superset §1 (iv) forbids (BLOCKING 1); obligation's line, which §5 says it does not derive and then rules by a fresh transfer while declaring the deciding criterion unrun (BLOCKING 5); and `0037` row 1's ordinal clause, read as a type constraint the row does not state and made load-bearing on the whole size ruling (BLOCKING 6). BLOCKING 3 is a single missed sentence in `0095` that now says the opposite of §2 and appears in no §10 item. None of the six requires a new derivation: four are one stated reading or one amendment line each, and two ask the draft to apply its own rule where it already applies it elsewhere.
