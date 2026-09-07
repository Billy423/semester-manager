# Review 6 - draft v3, lens 2 (falsification), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v3.md` and full repository read access. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-5. Blind to the lens-1 reviewer.

**Report, verbatim:**

---

## BLOCKING 1 - §2, §5: the `about` relation position's `id` fails the criterion §2 itself generalises, and `0096` is cited for an aspect it does not speak about

**Attack 2** (run `0101`'s criterion over the `about` edge's fields).

§2 rules: *"A relation position carries the link's fields as `0096` renders them. `id`, `type`, `direction`, and `role` where the kind has one"*, and §5 puts *"the `about` edge's `id · type · direction`"* on every resident row.

§2 also rules that *"the criterion applies at every position and not only the last"*. `0101`'s criterion is an **iff**:

> a field belongs on a routing result's endpoint if and only if, without it, the coordinator cannot form its next intent or cannot decide whether to spend the next call.

Run it on the edge `id`:

- *Cannot form its next intent.* An intent starts at `START(K)` or `START(ref)`, and a ref is a **node**'s kind plus id (`0018`, `CONTEXT.md` *Ref*). No admitted form starts from, or references, an edge id. `0101` states the address question explicitly and leaves it open: *"Whether an edge's `id` is one turns on whether the two ids share one space, which `0025` scopes to link endpoints and no record settles."*
- *Cannot decide whether to spend the next call.* A call is `look_at(id)` on a node. `0101` §10 lists *"what `look_at` of an edge would return, which no record states"* among what is not decided.

So the edge `id` fails the criterion at both clauses, and §5 carries it.

The ground offered is `0096`. `0096`'s ground for the edge id is a **write/repair** need: *"Without it `attach` and `detach` have nothing to name."* `0101` puts precisely that outside the test's reach - *"A repair read - finding a dangling ref for `0018`'s owed validation pass, or the link a `detach` must name - is not a judgment the coordinator must make … this test does not reach them."* This is the `reading-records.md` failure by name: `0096` binds **how a neighbour is rendered inside a node's block**, not **what a routing path's relation position carries**, and the draft transfers it (*"as `0096` renders them"*) rather than deriving it.

There is one unnamed alternative ground, `0061` - *"every read that returns records must return their handles - a handle absent from the render makes the level below unreachable"* - and a link is its own record (`0016`). If that is the real ground, then a field rides a position **without** meeting `0101`'s criterion, which falsifies §2's own generalisation of the criterion to every position. The draft cannot have both: either the row carries a field the iff excludes, or the generalisation is wrong. Neither is stated.

Note also `0097`: *"A tag carrying an `id` is an addressable object … it doubles as the signal for which things can be passed to `look_at`."* Carrying the edge id on every row signals an affordance no record defines. `0097` is not in §10.

The same test excludes `type` and `direction` on this position - the standing intent fixes both, so the coordinator learns nothing from them - and §5 concedes exactly that (*"a relation position whose `type` and `direction` the standing intent fixes"*, `0097`'s omit-what-the-container-fixes rule) while still listing them.

**Verdict: BLOCKING.**

## BLOCKING 2 - §5, §10 item 7: *"obligation's line is the row's field set minus `has-more`"* is either not well-formed or silently changes what a neighbour's line carries, and `0096` is not in §10

**Attack 3** (construct a chain that returns something the type rulings bar, or has undefined semantics).

§5 rules: *"The row is `id · kind · name · due · done_by · optional · course · has-more`, the `about` edge's `id · type · direction`, and a progress position carrying `id · kind · state · origin · updated_at`"*, then *"So: **obligation's line is the row's field set minus `has-more`**"*, and §10 item 7 amends `0082` and `0095` in both places to *"obligation's line is ring 0's **row** minus `has-more`"*.

Two readings, and both break:

- **"The row" as the whole row** (three positions). A line is **self-closing** by `0097`: *"A pointer and a projection are not content, so a line is self-closing and what it was carrying moves onto the element that owns it."* A self-closing element cannot nest a progress position or an edge position. So *the row minus `has-more`* is not a thing a line can be. Undefined semantics under the draft's own §2 and under `0097`.
- **"The row" as the obligation position's field set alone.** Then the line becomes `id · kind · name · due · done_by · optional · course` - it **drops `state`** and **adds `done_by` and `optional`**. `0095` rules the line's field set today: *"`0082` calls obligation's line 'ring 0's band plus `has-more`', and band A already carries `has-more`, so **the band** is band B"* - band B is `course · name · due · state` (`0038`). And `0096`'s worked example, a landed record, renders the line as `<obligation id="51" course="2c03" name="Midterm 2" due="2026-03-13" state="not_started"/>`. `0096` does **not** appear in §10's amendment list (item 7 names only `0082` and `0095`; item 13's pointer-debt list names `0091`, `0092`, `0093`, `0094`).

§5's own next sentence concedes the collision and then waves it through: *"how a line inside a block carries what the row carries as the progress position - `0096`'s worked example shows `state` as an attribute - is the block's render and untouched."* If it is untouched, the line is **not** the row's field set minus `has-more`; if the amendment lands as written, `0096`'s example and `0095`'s band-B derivation are both changed without being listed.

The substantive loss is real, not clerical: under the draft's own criterion `state` is admitted to the row because it is a J0 input, and the same argument applies to a neighbour obligation inside a block; dropping it from the line removes the one field that says whether a neighbour has been started.

**Verdict: BLOCKING** (threshold (c) - contradicts `0096`, not listed in §10 - and (d) - undefined semantics under the draft's own type rulings).

## BLOCKING 3 - §5: `has-more` is ruled onto the row with its value on an `about`-crossing row left undefined, and the resolution is mis-assigned to #82

**Attacks 2 and 3.**

§5 admits `has-more` and then states: *"**Two things are #82's by name:** where it appears in the row's render, and **what it holds on a row whose path already crosses `about`** - whether `about` in the set restates the progress position or signals a `sticky_note` that position does not show."*

Under the draft's own standing intent every row carries an `about` relation position whenever a progress record exists. For any obligation whose only link kind is `about` and which has a progress record, the row then states one fact twice - `has-more = {about}` alongside a rendered `about` edge - which is exactly the `0024` bite `0096` names: *"`<neighbours>` strictly contains that set … so a render carrying both states one fact twice, which `0024` bars."* `0096` keeps `has-more` alive *"only where the neighbourhood cannot be listed"*; the draft has made ring 0 a place where **part** of the neighbourhood is listed, and has not said what the field then holds.

So a field is ruled onto every row while its value on a definable class of rows is undefined. That is a type question, not a render question.

The assignment is also wrong. #82's body: *"`has-more`'s final name and position … `0092` rules what it carries; **this rules whether and where it appears**."* `0092`: *"This record's ruling on the field's **value** is untouched; what moved is where it appears."* So *what it holds* is `0092`'s, not #82's, and the phrase *"#82's by name"* is false for the second of the two.

The repair is small - say that `0092`'s value ruling stands unchanged and that the duplication is #82's render collapse under `0097`'s omit-what-the-container-fixes rule - but as drafted the row carries a field with no defined value.

**Verdict: BLOCKING.**

## BLOCKING 4 - §4: the dangling-ref detection route uses a form §8 parks and §9 omits, and it is not "J6's form"

**Attack 9** (is the absence query as spelled a valid chain under §2?).

§4: *"Detection is a repair read: `0018`'s owed link-set validation pass, extended to Ref-typed fields, or the absence query `START(obligation) · FILTER(not exists(MOVE(course, points-at)))`, **which is J6's form**."*

Three problems, compounding:

1. `MOVE(course, points-at)` is `MOVE(field, D)` - crossing a **Ref-typed field**. §8 rules: *"Crossing a Ref-typed field from a computed set has no must-judgment today … `0102`'s membership row leaves its admission to this ticket, and **it stays open**. Parked."* §11 repeats it. §9's list of *"forms admitted by this record"* is `START(K)`, `MOVE(L, D)` optional or not, a selection at a node or relation position, the position comparison, `not`, `exists` - **`MOVE(field, D)` is not there.**
2. §1 (i) rules *"**Without it** is read over the candidate forms minus the one under test, **including inside `exists`**."* So a parked form is unavailable inside `exists` too. The absence query is therefore not expressible under the draft's own form set.
3. It is **not J6's form**. J6 is `START(concept) · FILTER(not exists(MOVE(covers, pointed-by)))` - `MOVE(L, D)` over a **link kind**. `MOVE(L, D)` and `MOVE(field, D)` are two separate rows of #85 §7's form list and two separate paragraphs of §8. Calling one the other is the attribution error `reading-records.md` warns is invisible to a quotation check.

The consequence is not cosmetic: §4's ruling - *"the dangling ref is a defect the design tolerates by `0018` and a repair read finds"* - is reassurance that the defect is findable, and one of its two offered routes is unavailable under the draft's own rulings. The surviving route, `0018`'s validation pass, is *"owed and unbuilt"* by `0018`'s own words and is extended to Ref-typed fields only by §10 item 11. And by using the parked form here, §4 decides in passing something §11 says it does not decide.

**Verdict: BLOCKING.**

## BLOCKING 5 - §6: `0039` is cited for routing size to dispatch, and `0037` row 1 rules the only available size answer into a shape `0039`'s dispatch cannot carry

**Attack 6** (is *"J0 served by dispatch for its observations"* coherent given `0039`?).

§6 rules: *"**Neither size nor absorption is a form. Each is an observation on a member.** … Size and absorption belong to `0039`'s layer - *observe anything you can afford for every member; else dispatch*"*, and *"**What serves J0 today - ruled, and it is a demotion.** … Its two observations have no record yet, so they arrive by asking Billy, which `CONTEXT.md` calls one case of dispatch, **under `0039`'s formalism**."*

`0039`'s formalism is per-member and fixes the shape of what comes back:

```
observe(X) is permitted for a judgment over set S
  iff X is affordable for every member of S
  else dispatch(X, member) -> a value in the same shape as every other member's
```

`0037` row 1 rules what a size answer can be:

> **asking is only a remedy for a quantity the user can answer, and the answers available are ordinal comparisons, not hour counts**

An ordinal comparison is a relation **between two members**, not a value **of one member**. `dispatch(size, member)` has no position for it. So for **size**, `0039`'s escape does not deliver the observation, and the ruled sentence *"what serves J0 today"* is unsupported by the record it names.

The draft sees the shape mismatch and applies it only to the parked record's shape - *"a relation between two members that a per-member field does not hold"* - never to the dispatch route it rules is what serves J0 today. So the demotion, which is otherwise stated openly and would not be a finding on its own, is contradicted by a landed record on its own cited ground.

A second-order consequence worth naming rather than ruling: if size is a relation across members rather than a property of one, then a judgment using it ranges over relations across the set, which is `0101`'s own ground for paths and `0100`'s ground for the flat-render defect - so §6's ground for putting size outside routing's domain (*"an observation on a member"*) is the sentence under strain, not merely the delivery route.

**Verdict: BLOCKING.** Reparable by restricting the dispatch claim to absorption and stating size's shape gap as an open item, or by naming the limit where §6 currently rules.

---

## REPAIR 1 - §3: *"no ruled source names a judgment over either"* is falsified by J7 three rows above it

**Attack 1.** §3's *Candidates not on the list*: *"`0012` has two further link kinds between an obligation and an artifact - `spec`, whose `owed` role names the deliverable, and `prepares-for` - and **no ruled source names a judgment over either**"*. J7, in §3's own table, is *"which artifact states this obligation's requirements"*, sourced to *"`0001`, the requirements sentence"*, served by `MOVE(spec, points-at)[role = given]?` - a judgment over `spec` from a ruled source. The paragraph half-acknowledges this (*"Parked with J7's wake"*) without fixing the sentence. It should read *over `spec`'s `owed` role or `prepares-for`*. **REPAIR.**

## REPAIR 2 - §3: *"S2 … reduces to J4's chain"* drops S2's `builds-on` reading, and `builds-on` gets neither a judgment nor a park

**Attack 1.** #85 §7 gives S2 two chain readings: *"`START(ref B) · MOVE(builds-on)`, or `· MOVE(requires) · MOVE(requires, pointed-by)` to reach A through a shared concept"*. J4's chain is the second. The reduction silently discards the first. `builds-on` is `0012`'s only `obligation → obligation` relation, `0092` records it as admissible **today** (*"`builds-on` is admissible today too, since `0012`'s signature needs neither deferred layer"*), and it is the only cross-obligation relation that exists before the concept layer lands - so it is the one relation available today for `0001`'s second job. §3 claims each candidate is either derived or parked; `builds-on` is neither. **REPAIR** (the must-list's coverage claim, not a ruling).

## REPAIR 3 - §4: `0005` is cited for an aspect it does not speak about

**Attack 8.** §4: *"`0005` describes a knowledge base that accumulates, and no record confines the skeleton to a term"*. `0005`'s title and subject are *"The store accumulates; it is never synchronised against a source"*, and its content is about there being **no correspondence to maintain** against a remote. The inference the draft needs - that the **skeleton** will hold more than one term's obligations - rests on the negative claim (*no record confines it*), which needs no citation. `0037` rows 13 and 14 are cited correctly for term boundaries being open; row 11 (`course.offering_term` deferred to v2) is the nearer record and is not cited. **REPAIR.**

## REPAIR 4 - §5: *"Two things are #82's by name"*

**Attack 5.** Carried in BLOCKING 3; recorded separately because the attribution repair stands even if the value question is resolved here rather than there. #82's body names *"`has-more`'s final name and position"* and explicitly routes the value to `0092`. **REPAIR.**

## REPAIR 5 - §9: *"Its scope is unchanged"* alongside assigning arrangement to #82

**Attack 5.** §9's #82 bullet: *"Its scope is unchanged. **Arrangement is assigned to #82**, ruled by Billy, with three inputs."* Arrangement is a **clause** of the view in `0100`'s table (*"arrangement · how rows are laid out"*), and `0100` separates clause from render: *"**What this record does not decide.** Any clause's content, and **ring 0's render, which is not one of the clauses**."* #82's own body confines it to *"how they render, never which fields they hold"*, and #85 §8 says *"#82 … its scope is unchanged."* Assigning a clause to the render ticket is a scope change; the sentence saying otherwise is the defect, not the assignment (which is one of the session rulings). **REPAIR.**

## REPAIR 6 - §8: *"a filter there is `FILTER` one position back"* is at odds with §2's optionality rule

**Attacks 3 and 7.** §2 rules: *"optionality scopes over the crossing together with any predicate on its target **or on the link** … an optional step is empty when nothing satisfies the step's whole selection, written below as `MOVE(L, D)[selection]?`"*, with the worked reason that a predicate applied **after** an optional crossing undoes the optionality. §8 then describes J7's chain - which is optional, `MOVE(spec, points-at)[role = given]?` - as *"`FILTER` one position back rather than a separate form"*. For an optional step that decomposition is exactly the one §2 forbids. The verdict is unaffected (§9 lists *"a selection at a node or a relation position"* among the admitted forms, which is the same claim stated compatibly); the phrase *"one position back"* should be replaced by §2's `[selection]` scoping. **REPAIR.**

## REPAIR 7 - §4, §7: the width bet is costed in rows, not in what the row grew by

**Attack 6.** §7 justifies dissolving the bands with *"three fields on the rows the partition would have thinned costs nothing at this width"*. But the row also gained a relation position (`id · type · direction`) and two progress fields (`origin`, `updated_at`) over `0038`'s band A, on **every** row. §4's width paragraph carries only the roughly-55 row count with `0038`'s scope clause and the fall26 caveat. #82's body holds the measurement that prices this - *"flat 6,482 characters, structured 7,598 (+17%)"*, named there as *"the affordability input #70's provisional docstring budget uses"* - and it is not cited. **REPAIR** (the bet's statement, not the bet).

---

## Attacks run that produced no finding

- **Attack 1, the must-list against `CONTEXT.md`'s opening sentence.** Tried each of its three clauses (*what is owed* → J1, *what each obligation requires you to know* → J2, *where the material that teaches it lives* → J3) and each restatement in `0001` as rewritten (reload → J1/J3, job 2 → J4, job 3 → J6, requirements sentence → J7). Every clause has a row, and each chain is one return under the admitted forms. Dissolved.
- **Attack 3, does the standing intent drop a member the must-list needs.** `START(obligation)` reaches every obligation including one whose `course` ref dangles; §2's optionality rule keeps an obligation with no progress record with an empty position; a progress with no `about` link (`0035`) is not about an obligation and is not J1's; `0035`'s *"one current value per target"* reading is stated rather than assumed silently. Dissolved.
- **Attack 3, `0043` / `0095`.** The result is bounded in depth - one line per node position - which is what `0095` requires of a resolve, and residency is by policy rather than by fetch, which is `0101`'s own threading of `0043`. Nothing returns content: `detail` is excluded, `parts` is excluded. Dissolved.
- **Attack 3, `0046` against the `about` crossing.** Tried reading `0046` as barring the progress position. `reading-records.md`'s own table names this misreading (*"`0046` … read as a **scope** rule … it actually binds a **delivery** rule"*), and `0092`'s Considered Options withdraws the same argument by name. The draft reads it correctly. Dissolved.
- **Attack 4, reasoning from `0038`'s or `0042`'s present content back to the purpose.** The nearest candidate is §5's `state` row (*"the trigger `0042` stated as `state == in_progress`"*) and §4's *"one of the three triggers Billy stated"*. Both route through §7's session ruling that the three triggers become the **coordinator's** judgment rule, not ring 0's clause, and §5 states twice that landing on `0038`'s seven is *"a confirmation … and not a transfer"*. Dissolved.
- **Attack 5, decisions belonging to #87, #88, #14, #13, #25, #71.** Checked each against its own body: #87 is left whole (S1, by-handle, chunk handles); #88 receives the form list, `closure`/`REPEAT` and J2's hop count; #14 keeps the plan's representation and §6 distinguishes input from judgment; #13 keeps what the projection holds, and *whether the time projection is resident* was assigned to #86 by #85 §10; #25 gets a comment only; #71's question is left open with the re-typing consequence named. Dissolved (the one live mis-assignment, `has-more`'s value to #82, is BLOCKING 3).
- **Attack 6, `0100`'s refusal to widen ring 0 and #82's ruling.** Ring 0 stays a resident result whose every field passed the criterion; the plan's inputs are parked rather than placed on a row; `0100`'s condition (*"ring 0 stays narrow on the condition that some cross-node read exists beside it"*) is met by `0101`'s routing. `0100`'s clause table is a declared lens whose own text says *"where the lens and a landed record disagree, the record wins"*, so §7's re-placement of `0042` as a per-row field-set partition does not contradict it. Dissolved.
- **Attack 8, the one-term assumption's wake.** `course.term` exists (`CONTEXT.md`'s *the line*, `0094`'s example), but what is held nowhere is which term is **current**, and `0037` rows 13/14 support that. The wake (*a second term's courses land*) and the instruction that the future predicate keep an undeterminable-term obligation in are both stated. Dissolved except for the `0005` citation (REPAIR 3).
- **Attack 9, the three dangling-ref production routes and *"ring 0 does not detect it"*.** All three are real: deletion is `0018`'s own cascade row (*"deleting a course does not cascade to its obligations"*); a code no course has is `0091`'s *"a coordinator can therefore name a course row it never read"* plus `0026`; landing before the course is legal because `0018` validates a link against its **signature**, not against existence. *"Ring 0 does not detect it"* is correct - the row carries `course` as a bare pointer and `0097` makes an id-carrying tag **addressable**, not existent. Dissolved except for the absence query (BLOCKING 4).
- **Attack 2, the remaining fields.** Ran the criterion over every obligation field (`id`, `kind`, `name`, `due`, `done_by`, `optional`, `course`, `parts`, `grade_share`, `grade_share_conditional`, `added_at`) and every progress field (`id`, `kind`, `state`, `detail`, `origin`, `created_at`, `updated_at`). The field lists are complete against the records, no admitted field is excluded, and the three contested inclusions - `origin` (`0056`'s loud provenance at every read), `updated_at` (`0099`'s harm), `has-more` (`0092`'s *"the next call is a gamble"*) - each have a ground the criterion's second clause can carry. `grade_share`'s exclusion is consistent with §6 keeping `0042`'s importance sentence. Dissolved at the node positions; the finding is at the relation position (BLOCKING 1).

---

## Summary

**Five blocking findings and seven repairs.** The blocking findings cluster in one place: the draft derives the two **node** positions rigorously from `0101`'s criterion and then stops deriving. The `about` **relation** position's contents are transferred from `0096`, a render record, rather than derived - and the transferred `id` fails the criterion §2 has just generalised to every position (BLOCKING 1). Downstream of that same seam, the row-versus-line amendment is either not well-formed or silently rewrites obligation's line without listing `0096` (BLOCKING 2), and `has-more` is ruled onto a row whose new `about` position leaves the field's value undefined (BLOCKING 3). The remaining two are independent: §4 offers a dangling-ref detection chain built from a form §8 parks and §9 omits, and misattributes it to J6 (BLOCKING 4); and §6's ruling that asking serves J0's observations under `0039` is contradicted for **size** by `0037` row 1, which rules the only available answer into a between-members shape `0039`'s per-member dispatch cannot carry (BLOCKING 5). The seven repairs are attribution and wording: a parking sentence its own table falsifies, a scenario reduction that drops `builds-on`, `0005` cited for the skeleton, `#82`'s scope claimed unchanged while being changed, and three smaller ones. Nothing in the must-list itself (§3) or in the standing intent's coverage of J1 (§4) broke under attack; the derivation's spine holds, and every blocking finding is reparable without moving it.
