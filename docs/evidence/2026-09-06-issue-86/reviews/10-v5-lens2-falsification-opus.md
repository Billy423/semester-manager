# Review 10 - draft v5, lens 2 (falsification), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v5.md` and full repository read access. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-9. Blind to the lens-1 reviewer.

**Report, verbatim:**

---

## BLOCKING 1 - §2's "every node position carries its kind's line" is falsified by §5's own derivation, and is itself the render-transfer §2 bars

**Section:** §2 (second ruling), against §5 (both tables, and the line paragraph). **Attack:** 2 and 3.

§2 rules:

> **Every node position carries its kind's line, and the criterion runs over every position.**

and then fills that in by naming lines: *"Course's line is `id` `name` `term` (`CONTEXT.md`, *the line*); `concept`'s and `artifact`'s are the debt that entry records against #17, #19 and #20, and this ruling fixes the type and not their content; `progress`'s is derived at §5, since it is a position of the standing intent."*

§5 then rules:

> **The row is `id · kind · name · due · done_by · optional · course · has-more` at the obligation position**

and, four sentences later:

> *obligation's line is the obligation position's field set, with `state` carried as `0096`'s worked example already carries it* - `id · kind · name · due · done_by · optional · course · state`

So for the one kind the record actually derives, **the position's field set and the kind's line are different sets in both directions**: the position carries `has-more` and the line does not; the line carries `state` and the position does not (it is re-typed as a second position). §5 says so in its own words - *"Row and line are two things, and only one of them carries `has-more`"* - and grounds the difference structurally: *"A ring 0 **row** is a position of the standing result and cannot list its neighbourhood"*, while *"Obligation's **line** ... sits inside a `<neighbours>` section that already lists the edges"*. That ground is sound, and it is exactly what makes §2's sentence false.

The sentence is not cosmetic. Three things rest on it:

1. **It is the only thing §2 says about what a `course`, `concept` or `artifact` position carries.** For `course` it transfers `CONTEXT.md`'s `the line` entry - a **render** record about *"the render of a node that is one `look_at` away ... inside an `<edge>`, and inside a composed section"* - onto a routing position. §2's own preceding ruling forbids exactly this: *"**Membership at a position is the criterion's alone; `0097`'s rule that a member omits what its container fixes is a render rule about restating, and it decides nothing here.**"* If `0097` decides nothing at a position, neither does `CONTEXT.md`'s `the line` entry or `0096`'s example, and course's position content is owed, not settled. This is the third round's finding - *"transferred from a render record rather than derived"* - one seam further on, at the node positions §2 thought it had closed.
2. **It mis-assigns a debt.** §2 says `concept`'s and `artifact`'s position contents are *"the debt that entry records against #17, #19 and #20"*. That entry records the **line** debt. §5 has just demonstrated that a kind's line and its position field set are not the same object, so the position debt is a *second* debt, and neither §2 nor §11 records it as one. §11 lists only *"the deciding fields of a `concept` or `artifact` position (#17, #19, #20)"* - which re-merges the two.
3. **It collides with `0101` as §2 amends it.** `0101` reads *"Each endpoint carries its own kind's deciding fields - **one set per kind** (`0095`)"*; §2 amends *endpoint* to *position*. Under §2's sentence, `obligation`'s "one set" would be its line - which §5 rules it is not.

The reverse direction is equally exposed: `progress` has **no** line by `CONTEXT.md` (*"`sticky_note` and `progress` need none"*), so §2's sentence cannot be satisfied for the standing intent's own second position. §5 fixes this by deriving the position's field set and then *naming* it a line - *"The progress position is a new line for `progress`, one ruling per kind as `0095` requires"* - which is the opposite of the direction §2 states. Position content is derived and then exported as a line; it is not a line transferred to a position.

**Repair, without changing any verdict in §5:** §2's sentence has to become a ruling about **depth and type** - a node position carries one field set per kind, of line depth, derived at that position by the criterion - with the specific lines removed from it, course's position content named as owed, and the concept/artifact position debt separated from the line debt in §11.

**Verdict: BLOCKING.**

---

## BLOCKING 2 - §1 (iv) forbids the move §4 and §5 use to justify a vacuous predicate on `optional`

**Section:** §1 (iv) against §5's `optional` cell, §4's *Why there is no predicate*, §3's J1 row and §11. **Attack:** 1, 2, 5.

§1 (iv), ruled:

> **(iv) A superset that carries the discriminator does not produce the set.** A judgment's set is the set as the judgment defines it. If a chain that returns a wider set with the deciding field visible on every member counted as producing the judgment's set, then no `FILTER` would ever be necessary at a width the coordinator can hold ... So the test counts the set, not the affordability of a superset.

§5's `optional` cell:

> | `optional` | a J0 input: whether the obligation is to be done at all. Whether an `optional = true` obligation is *owed* is a J1 membership question this record does not decide; **it is included and the coordinator judges** | in |

That is the superset-with-the-deciding-field-visible move, applied to the one judgment - J1, *"what is owed, across five courses, dated or not"* - that §3 rules is **served by the standing intent**, and applied at the exact field whose membership question the record declines. §11 confirms the decline: *"whether an `optional = true` obligation is owed"*.

The two cannot both stand. Either

- an `optional = true` obligation is owed, in which case `START(obligation)` produces J1's set exactly and the cell should say so rather than deferring to the coordinator's judgment; or
- it is not, in which case by (iv) the standing intent **does not produce J1's set**, a `FILTER` is necessary at that boundary, and the standing intent as ruled fails the must-judgment §3 assigns to it.

The draft rules the chain adequate while declining to fix the set boundary the adequacy turns on, using the reasoning (iv) exists to forbid.

Note that this is *not* the same as the "which ones are near" case, which §4 disposes of correctly: there the ground is that **no must-judgment ranges over the active set**, so there is no narrower set for a `FILTER` to produce. For `optional` the draft concedes there may be a narrower set and declines to say.

**Two things sharpen it.** First, `0031` - *"`optional` and `grade_share_conditional` are nullable bools where **null means unknown, never the negative**"*, with *"a stored null means the writer genuinely could not tell"*. So on some rows the field the coordinator is told to judge with carries no answer at all, and `0028` requires that null render as absence. Neither §5's cell nor its field-inventory provenance list cites `0031`. Second, the same shape recurs at the term boundary (§4: *"once a second term's courses land a bare `START(obligation)` ranges over both"*) - there the draft handles it correctly, with a stated assumption, a width bet and a wake. `optional` gets neither.

**Repair:** either rule the J1 membership question (which changes what §11 lists), or state, as at the term boundary, that the standing intent produces J1's set **under the reading that optional obligations are owed**, and record that reading as an assumption with a wake, so that (iv) is not silently suspended.

**Verdict: BLOCKING.**

---

## BLOCKING 3 - §6 cites `0039` for a classification of size that §6 itself falsifies four paragraphs later

**Section:** §6 (second paragraph, against the fifth), and the second paragraph of the draft. **Attack:** 6.

§6 rules, as a heading sentence:

> **Neither size nor absorption is a form. Each is an observation on a member.**

and grounds it: *"Size and absorption belong to `0039`'s rule - *observe anything you can afford for every member; else dispatch* - which `0101` keeps separate from the one-return premise..."*. The draft's second paragraph carries the same as one of the seven session rulings: *"neither is a form; each is an owner-authored observation whose record's shape is parked whole"*.

§6's fifth paragraph then falsifies it, from landed records:

> **Size does not fit that route, and this record says so rather than ruling it in.** `0037` row 1 rules that the only answer available is an ordinal comparison, *"not hour counts"* - a relation between two members - and `0039`'s dispatch returns a value of one member in the same shape as every other's, **which has no position for a relation**.

Both quotations verify. `0037` row 1: *"the answers available are ordinal comparisons, not hour counts"*. `0039`: *"`dispatch(X, member)` -> a value in the same shape as every other member's"*. Together they say that **size is not an observation on a member**, and therefore does not belong to `0039`'s rule at all - which is what the second paragraph asserts and cites `0039` for. §6 even names the alternative: *"the instance may show that size is a relation across the set rather than an observation on a member, which would put it nearer `0101`'s ground for paths than to `0039`'s layer"*.

This meets threshold (a): `0039` is cited for a classification it cannot carry for size. It is load-bearing rather than cosmetic, because that classification is the whole reason size is placed outside the necessity test's reach (*"This is not a failure of the necessity test, which admits forms and not observations"*). If size is a relation between two members of J1's set, then `0101`'s own ground for returning paths rather than endpoints - *"a judgment across obligations is a judgment about their **relations**"*, and *"a set of endpoints has no position for a relation"* - is the ground that says a between-members answer belongs on a **path**, i.e. inside routing's domain, where the test does reach it. The draft notices this and declines to run it (*"that is noted for the wake and not ruled"*), which is a defensible parking of the **answer** - but not of the **classification**, which is stated as ruled and is what forecloses the question.

The consequence is that J0 - a must-judgment on Billy's own session ruling - is unservable by any route today, and the record's stated reason for that (an observation without a record) is not the reason its own §6 establishes (an answer shape that neither `0039` nor a per-member field can hold).

I am aware the seven session rulings are to be treated as ruled. This is reported under the stated exception: **two landed records, `0037` row 1 and `0039`, contradict one of them**, and `docs/agents/drafts-and-rulings.md` requires the claim be demoted to what the evidence supports rather than the higher standing defended.

**Repair:** split the classification. Absorption is an owner-authored per-member observation and `0039` carries it. Size's shape is **open**, and §6 should say that the reason it is open is that no landed record supplies a home for a between-members answer - not that it is an observation whose record does not exist yet. The second paragraph's ruling sentence changes with it.

**Verdict: BLOCKING.**

---

## REPAIR 1 - three membership cells in §5 are decided by render records, against §2's own ruling

**Section:** §5, obligation table. **Attack:** 2.

§2 rules *"Membership at a position is the criterion's alone"*. Three cells decide membership on a render record instead:

- `added_at`: the entire "under the criterion" column is *"`0099`'s ground - it is about the row, not the node - applies one render over"*. **The criterion is never run on this field.** Worse, `0099`'s ground is a `look_at` ground - *"`look_at`'s purpose is to say what the **node** is, not what the **row** is"* - and §4 rules that under this record **the unit is the row** (*"under this record the unit is the row (§5)"*). Transferred verbatim, `0099`'s distinction argues *for* `added_at` on a ring 0 row, not against it. The verdict `out` survives the criterion easily (nothing about when a record entered decides whether to spend the next call); it is the ground that has to be replaced.
- `id`: *"the address fetch accepts; **`0082` makes it an attribute because it addresses**"*. The first clause is criterion-grounded; the second is `0082`'s placement rule.
- `kind`: *"the discriminator (`0027`); with `id` it is the Ref the next intent is formed from (`0018`), and **`0082` makes it the element name because it addresses**"*. Compare the progress table's `kind` cell, which handles the same field correctly - it cites `0097` only to route render-omission to #82. The asymmetry is the fourth round's finding (*"`kind` judged by a render rule at one position and by the criterion at another"*) surviving in the obligation table.

No verdict changes. **Verdict: REPAIR.**

## REPAIR 2 - §3's Sources list silently drops `0001`'s first job

**Section:** §3, *Sources*. **Attack:** 1.

> A judgment is *must* if it rests on a ruling: `CONTEXT.md`'s opening sentence, `0001` as rewritten at #85 - **its second job, its third job**, and its sentence that *"helping model an assignment's requirements is in scope"* - or a ruling Billy makes in session

`0001` as rewritten has three restated jobs, and the first - *"Remove the anxiety of not finding information is the reload, this record's own ground, and a chain that reaches the material in one return (`0101`) is what collapses it"* - is not in the list and is nowhere disposed of. It is very likely subsumed by the opening sentence's third clause (J3), but `docs/agents/reading-records.md` requires that a list be shown to answer the reader's question before it is treated as exhaustive, and this list is the record's bound on the entire must-list. One clause saying why job 1 generates no judgment of its own.

**Verdict: REPAIR.**

## REPAIR 3 - §3's *ranges over* column under-states J0 and mis-states J1, which is where §1 (ii) does its work

**Section:** §3's table, against §1 (ii) and §4. **Attack:** 1, 2.

§1 (ii) is what makes the necessity argument run: *"The relative reading ... makes each must-judgment declare what it ranges over, **which is a column of §3's table**."* Two cells then fail to declare what §4 relies on:

- **J0**: *ranges over* = *"J1's set, plus two per-member observations (§6)"*. §6's two observations are size and absorption. But §4 justifies the entire `about` crossing on a third input: *"**`state` is J0's input** - in-progress work is one of the three triggers Billy stated"*. On §3's own record, therefore, **no must-judgment declares that it ranges over the progress position**, and by §1 (ii) `START(obligation)` alone produces the same set as the standing intent for every judgment as declared. The substance is argued in §4; the column that §1 (ii) makes load-bearing does not carry it.
- **J1**: *ranges over* = *"endpoints"*. After §2 amends `0101` from *endpoint* to *position*, the standing intent's endpoint is the **progress** position, not the obligation position. J1 ranges over the obligation position. The word is stale in exactly the vocabulary §2 just repaired (and the same stale word sits in J6's cell, where it happens to be harmless because start and endpoint coincide).

**Verdict: REPAIR.**

## REPAIR 4 - §5 asserts `has-more`'s ground intact, but the standing intent narrows it and leaves `0024`'s bite in the ruled row

**Section:** §5, `has-more` cell. **Attack:** 2, 3.

> A ring 0 **row** is a position of the standing result and cannot list its neighbourhood, which is `0092`'s and `0096`'s ground for `has-more` living there.

`0096` states that ground with an explicit scope: *"that ground holds **only** where the neighbourhood cannot be listed. That is ring 0"*. Under this record ring 0's row **does** list one edge - the `about` crossing to `progress` - so the ground is narrowed rather than intact, and the `0024` collision `0096` used to strip `has-more` from a node's render (*"a render carrying both states one fact twice, which `0024` bars"*) is now live inside the row for the `about` member of the value.

§5 sees the duplication and routes it to #82: *"That a row then shows one fact twice is a render collapse, and **where the field appears and how the duplication collapses are #82's by name**"*. That is the right destination for the collapse, but §5 has ruled the **row's content**, not a render, and the row's content is where the fact now appears twice. The cell should record that `0096`'s ground survives for the eight link kinds the row does not list, and that `about` is redundant on the row and elided by #82 - rather than asserting the ground unqualified.

**Verdict: REPAIR.**

## REPAIR 5 - §5 parks as owed a question it has just answered for `state`

**Section:** §5, line paragraph, against §11. **Attack:** 7.

The repaired transfer rules obligation's line to be `id · kind · name · due · done_by · optional · course · **state**`. `state` is `progress`'s field (`0035`), so obligation's line carries another record's field. Two sentences later:

> Whether the criterion ... also transfers `origin` and `updated_at` - **and whether `0097` lets a neighbour carry a field that is another record's** - is the line's own question, owed and not run here (§11).

As written the second clause is over-broad: it is already answered in the affirmative for `state`, by `0096`'s landed worked example, which the repair leans on. The demotion is coherent - *"repaired only to what dissolving band B forces"* is the right principle, and keeping `state` because `0096` already prints it is the right application - but the owed question has to be narrowed to *additional* other-record fields, or §11 reads as parking a question §5 relies on having settled.

Two smaller things in the same paragraph verify clean and are worth recording as such: dropping *"plus the edge's `type`"* from `CONTEXT.md`'s `the line` entry is right, because `0096` puts `type` on the `<edge>` and not on the line; and the "against band B adds `done_by` and `optional`" arithmetic is right against what `0096`'s example actually prints.

**Verdict: REPAIR.**

## REPAIR 6 - §2 pre-decides what §11 parks about the edge `id`

**Section:** §2 (relation position), against §11. **Attack:** 5.

§2: *"**It enters a relation position on the day an edge id becomes an address.**"* §11: *"whether an edge's `id` is an address, **and what a relation position carries once it is** (`0101`'s open question)"*. The second half of §11's item is precisely what §2's sentence decides. `0101` leaves both open (*"Whether an edge's `id` is one turns on whether the two ids share one space, which `0025` scopes to link endpoints and no record settles"*), and #85 §10 adds that *"what `look_at` of an edge would return ... no record states"* - so there is no basis today for saying the id *will* enter. Make it conditional-and-unruled, or drop the second half of §11's item.

**Verdict: REPAIR.**

## REPAIR 7 - §8's disposal of `or` is stated as exhaustive and is not

**Section:** §8, against §3 and #85 §7. **Attack:** 8.

> **`or` has no must-judgment after §7.** **Its one candidate was `0042`'s disjunction as a standing intent**, and that intent is not standing.

§3 disposes of a second candidate in its own words - *"or over any union of routes with J3's; each would be a chain of its own, so no judgment needs `or` over crossings"* - so "its one candidate" is false on the draft's own page. And #85 §7 carries a third, which the draft never disposes of anywhere: the wildcard crossing row, whose *without it* column reads *"nine chains, one per kind, and their union is not a chain"*, for the judgment *which of X's neighbours are worth a look*. That judgment is union-shaped and was ruled **in** by Billy at #85, with its exposure through `look_at`. The disposal is available and short - the wildcard crossing is a form of its own, and the judgment is served by fetch (`0094`'s `<neighbours>`), not by a resolve needing `or` - but it has to be written, because §9's #88 bullet lists *"the forms admitted by this record"* without it and a reader will take the two lists together.

The same paragraph's J8 disposal - *"two judgments, one chain each ... no judgment ranges over both directions at once, so no union and no new form"* - reads clean under §1 (iii), and its unstated support is the same #85 ruling: a both-directions neighbourhood read is `look_at`'s. Saying so once would carry both.

**Verdict: REPAIR.**

## REPAIR 8 - §5's field inventory omits `0031` and states no question for the lists it draws on

**Section:** §5, the provenance sentence. **Attack:** 4.

> The field lists were assembled from this repository's records - `obligation`'s from `0027` (`kind`), `0028` (`added_at`), `0029` (`course`), `0032`, `0033`, `0037`, `0038` (`name`, `due`, `optional`, `done_by`) ... - because no landed record carries a field table

Two things. `0031` is missing, and it is the record that **types** two of the fields in the table (`optional` and `grade_share_conditional`) as nullable bools where null means unknown; its absence is what leaves the `optional` cell silent on the null case (BLOCKING 2). And the sentence takes candidates for `name`, `due`, `optional` and `done_by` from **`0038`'s selection** - the clause `0101` bars as a constraint - without stating the question that list was written to answer, which `docs/agents/reading-records.md` requires before a list is used as a bound.

I re-derived the inventory independently against `0027`, `0028`, `0029`, `0030`, `0031`, `0032`, `0033`, `0037` and `CONTEXT.md` and found **no field the draft's list misses**, so this does not change a verdict. It is the method, not the result, that needs the sentence: as written, a field that exists on `obligation` and appears in no cited record is invisible to the derivation, and the record does not say so.

**Verdict: REPAIR.**

## REPAIR 9 - §11 omits path multiplicity, which the row-per-obligation unit rests on

**Section:** §11, against §4 and `0101`. **Attack:** 3, 5.

§11 discloses one half: *"whether an obligation may carry more than one progress record, on which §4 relies on a reading of `0035`"*. It omits the other. `0101` leaves *"whether a path may repeat a node, and **how paths are deduplicated**"* to the grammar, and §2's type rulings cover only the **empty** case, never the **multi-match** case. Two `about` links from one `progress` to one `obligation` differing in `locator` are two distinct links by `0017`'s natural key, and nothing in `0035` ("one current value per **target**") bars them - it bars two progress records, not two links. Under multi-match the standing intent returns two paths for one obligation, and the unit §4 and §9's `0089` amendment both call "the row" stops being one per obligation.

`0035`'s *"one current value per target - enforced by the service"* makes the reading §4 takes a sound one, so I do not think this reaches BLOCKING. But §11 should list path multiplicity and deduplication beside the `0035` reliance, since the row unit rests on both.

**Verdict: REPAIR.**

## REPAIR 10 - "`0033` is the later ruling" is not auditable from this checkout

**Section:** §6, final paragraph. **Attack:** 6.

The conflict §6 finds between `0037` row 1 and `0033` is real and both quotations verify. The tiebreak is not: *"Both cannot stand, and `0033` is the later ruling"*. Neither ADR carries a ruling date in its body; the only dates are inside `fall26:` source lines - `0033`'s *"write-rules.md §3.4 (Billy, 2026-08-28)"* against `0037`'s reference to a *"schema.md changelog 2026-08-27"* that is cited for a different purpose (the self-disqualification of the evidence base, not the row's ruling). ADR number is not chronology. The available and stronger ground is that `CONTEXT.md`'s current `parts` entry bars *"using it to judge how much work something is"* - which is the vocabulary the repository holds today, and which `docs/agents/reading-records.md` makes the deciding authority over a frozen record's wording.

**Verdict: REPAIR.**

## REPAIR 11 - the criterion is not run at the progress position for `has-more`

**Section:** §5, progress table. **Attack:** 2.

§2 rules *"the criterion runs over every position"*, and §5 says its tables apply it *"field by field"*. The progress table has seven rows and `has-more` is not one of them - neither *in* nor *out*. It is excluded only by an aside in the obligation table's cell, *"in, as the row's one non-field item"*, which asserts uniqueness without deriving it. The right answer is almost certainly *out* (a `progress` node's only link is the `about` the path just crossed, so the set is fixed by the step and tells the coordinator nothing - the same ground §2 uses to keep the link's `kind` off a relation position), but it should be a row in the table.

**Verdict: REPAIR.**

## REPAIR 12 - "a line carries no content" is `0097`'s, not `0095`'s

**Section:** §5's `detail` cell and §6's `sticky_note` sentence. **Attack:** 7.

Both cite `0095` for *"a line carries no content"*. `0095` contrasts `<annotations>` full text with `<neighbours>` one line, which is suggestive; the record that **states** it is `0097`: *"A pointer and a projection are not content, so **a line is self-closing** ... An element with a text field and no sections closes itself too: a `progress` with no `detail` is `<progress id="70" state="done" …/>`, not an empty pair."* A self-closing element cannot carry a free-text field, which is `0082`'s rule 3's position. Cite `0097` (with `0095` for the depth).

**Verdict: REPAIR.**

---

## Attacks that produced no finding

**Attack 3, on J3, J4, J7, J8 and the standing intent's chains.** I ran each chain against §2's three type rulings and could not construct a silent drop. `START(obligation)` is a start by kind and reaches every obligation including the dangling-`course` one §4 rules must be kept; the optional crossing plus §2's *"an optional step is empty when nothing satisfies the step's **whole selection**"* correctly keeps an obligation that has a `sticky_note` and no `progress` (I checked `0012`'s `about | annotation → any` signature and `0034`'s tag-not-hierarchy ruling: the selection is genuinely needed and its placement inside the step is what saves the member); the new empty-propagation rule saves the no-`requires` obligation at J3's and J4's second step; and J4's `[kind = obligation, course ≠ start.course]` needs the kind predicate for the reason given, because `0012` gives `requires` two signatures. Nothing returns a block or accumulates a neighbourhood, so `0043` and `0095` are not bitten - the row is 13 bounded items across two positions. The one semantic gap I could construct is path multiplicity, reported at REPAIR 9 rather than here because `0035`'s service-enforced *one current value per target* holds it closed.

**Attack 4 - reasoning from `0038`'s or `0042`'s present content back to the purpose.** I found none. §5 frames the coincidence in the right direction and says so - *"that it lands on the same seven is a **confirmation** of `0038`'s selection"*, and the *how it was reached* paragraph calls it *"an independent confirmation of `0038`'s selection on a different ground and not a transfer from it"*. §7's re-placement of `0042` rests on Billy's session account of what `0042` was for, not on `0042`'s text. §4's width paragraph uses #80's measured figure as a **floor** for a bet it explicitly declines to rule. The only residue is the field **inventory** drawing candidates from `0038`, which is an existence claim rather than a constraint on routing; it is at REPAIR 8 for its method, and I verified it misses no field.

**Attack 5, for over-listing beyond what is reported.** Most of §11 checks out against §4 and §8. The width gate, the term predicate, J2's hop count, the arrangement, the render, `has-more`'s name and position, the time projection's contents, `closure`/`REPEAT`, by-handle, the concept/artifact debts, dispatch against the effectiveness constraint, the repair reads, `state`'s home, lecture progress, *which items need Billy*, `origin`'s write rule and the plan's representation are all genuinely undecided in the body and land on the right tickets by those tickets' own bodies. #82's body confines it to *"how they render, never which fields they hold"*, so §5's membership rulings are not #82's; #14's *"the plan is where that judgment gets written down"* is about the judgment, and §6's input/judgment split is the correct reading of it; #71's `state` question is left open and the re-typing consequence is recorded rather than pre-empted; #25 gets absorption's target as a comment and not a ruling about concept origin. Three over-listings survived and are at REPAIR 5, REPAIR 6 and BLOCKING 2. One item is under-listed rather than over-listed: §11 says *"what the time projection holds (#13)"*, where #13's body owns *"whether a time projection over the skeleton is built **at all**, and if so what it holds"* - §4 only rules residency, which #85 §10 assigns here, so this is a wording narrowing rather than a trespass, and I did not raise it separately.

**Attack 8, on Billy's own comments.** The `sticky_note` disposal reads clean. The stated ground is *"no ruled source names a judgment that ranges over them as a set"* - which is the right ground, since #84's raw decomposition is candidate material by #86's own body (*"explicitly not the target"*) - and `0046` is used only for **delivery** (*"they reach the coordinator through their own channel at `look_at`"*), which is the aspect `docs/agents/reading-records.md` says it binds, not the scope aspect it warns against. The parked wake is concrete and observable. Its interaction with `has-more` is honestly stated and is the same collapse reported at REPAIR 4.

---

## Summary

**Three blocking, twelve repair.** The blocking findings are one structural and two citational. The structural one is §2's *"every node position carries its kind's line"*, which §5's own row-versus-line derivation falsifies for the only kind the record derives, and which imports a render record's field set onto a position that §2 has just ruled the criterion alone decides - carrying with it a mis-merged debt for the `concept` and `artifact` positions. The two citational ones are §1 (iv) being suspended for `optional`, where the standing intent is ruled adequate for J1 while the J1 membership question that decides its adequacy is declined; and §6's *"each is an observation on a member"*, which `0037` row 1 and `0039` together falsify inside §6's own text, and which is the classification that keeps size outside the necessity test's reach. All three are repairable without re-running the derivation: the first by restating §2's sentence as a ruling about depth and separating the position debt from the line debt, the second by stating the optional reading as an assumption with a wake in the way §4 already does for the term, the third by splitting size from absorption in the classification and demoting the session ruling to what `0037` and `0039` support. The twelve repairs are attributions, table cells and two lists stated as exhaustive that are not; none of them moves a verdict, and the `0037`-row-1-versus-`0033` conflict the draft found is real and correctly repaired apart from its tiebreak ground.
