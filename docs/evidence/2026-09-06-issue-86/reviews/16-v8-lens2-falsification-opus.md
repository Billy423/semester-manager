# Review 16 - draft v8, lens 2 (falsification), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v8.md` and full repository read access. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-15. Blind to the lens-1 reviewer. Told that §5b is a draft section and that findings against it are repair.

**Report, verbatim:**

---

## Findings, most severe first

### F1. §5, the `grade_share` cell - the ground that closes it is the ground `0099` refuses, and the draft says so itself one row down

**Section:** §5, obligation position, `grade_share` / `grade_share_conditional`. **Attacks:** 2 (a cell whose stated ground is not what decides it), 4 (reasoning from `0042`'s present content), 6 (§5 against §6).

The cell reads:

> J1 does not turn on a share, and J0's stated inputs are size and absorption - what Billy said is hard to do without, not an exhaustive list, so **the criterion alone does not close this cell. What closes it is a ruling: `grade_share` *"has no reader by standing exemption"* (`0042`, kept at §7), and a resident row would supply it one.** `0038`'s corpus argument - a column of shares reads as a partition it is not - is kept beside it (§10)

Three things break it.

**(a) `0099` refuses exactly this ground, and names exactly this field as the reason.** `0099`:

> **`added_at` does not render, and this is a ruling rather than a derivation.** Not on the ground that nothing reads it - `grade_share` has no reader by standing exemption and is in the schema.

`0099` cites the `grade_share` exemption *as the counterexample* that disqualifies *no reader* as a ground for keeping a field out of a read. §5 turns that same clause into the closer for keeping a field out of a read. `0099` is a landed record and is **not listed in §10** - threshold (c).

**(b) The draft asserts the refusal itself, two rows later.** The `added_at` cell reads: *"`0099` excludes it from a block on a ground of its own, and **no reader is the ground `0099` declines**"*. The record therefore states that `0099` declines the no-reader ground and then uses the no-reader ground as a cell's closer. One of the two cells is wrong on its face.

**(c) The inference is backwards against the rule the clause belongs to.** *Standing exemption* is `CONTEXT.md`'s **the rigidity rule**: *"a field is typed if and only if some mechanism reads it. It admits declared exemptions (`grade_share`, `added_at`)"*. The exemption permits the field to exist **without** a reader; it does not forbid it acquiring one. *"A resident row would supply it one"* is stated as though supplying a reader were a harm, when under the rigidity rule having a reader is the ordinary case and having none is the exception being excused. Nothing follows from it.

**(d) §5 and §6 read the same `0042` sentence two incompatible ways.** §6 rules:

> **So the `0042` sentence #82 authorised this ticket to overturn - *the system holds no notion of an obligation's importance* - is not overturned.** It bars a rule that promotes rows by importance; J0 is Billy deciding, with the system supplying inputs.

If the sentence bars only *a rule that promotes rows by importance*, it cannot also bar a field from a row - a row is not a promotion rule. §7 then binds the two together (*"the sentence barring a notion of importance (§6), with its clause that `grade_share` has no reader by standing exemption (§5)"*), so the incoherence is carried into the amendment list.

**Attack 4 also lands here.** `0101` rules that *"no clause's present content constrains routing"* and that `0100`'s clauses are re-derived at #86. This cell is the one place in §0-§8 where a verdict is closed by `0042`'s present content rather than by the criterion, and it is the cell the record itself says the criterion does not close.

**What survives.** The verdict *out* is rescuable: `0038`'s independent corpus argument - *"one course's share column sums to 95, the missing 5% has no row, and two 1% bonuses sit outside the 100"* - is a real ground, audited at #82 and kept at `0100`. The repair is to promote it from *kept beside it* to the closer, drop the `0042`/no-reader sentence, and state honestly that the criterion's verdict on `grade_share` for J0 is open (which is what `0042`'s own overturn note anticipates: *"the sentence most likely to move is the one below barring a notion of importance, because an obligation's size is one of the inputs that ruling was made without"*).

**Verdict: BLOCKING** - thresholds (a) and (c).

---

### F2. §3 J4 and §8 - the same-course case is admitted as the superset move §1 (iv) exists to police, on a contested reading of `0001` job 2, with no wake

**Sections:** §3 (J4's *served by* cell), §8 (*The position comparison has no must-judgment today*). **Attacks:** 8 (primary), 1.

§1 (iv) rules:

> **A superset that carries the discriminator does not produce the set.** ... If a chain that returns a wider set with the deciding field visible on every member counted as producing the judgment's set, then no `FILTER` would ever be necessary at a width the coordinator can hold ... **Its discipline on this record:** wherever the standing intent returns a member the coordinator then judges out, this record either **shows no must-judgment ranges over the narrower set** or **states the reading under which the member is in and wakes it**.

§3 then admits the same-course case into J4:

> the same-course case stays in, since **the ruled source models the relation and not only its cross-course instances**, and #85 §7's S6 predicate `course ≠ start.course` is dropped for that reason

and §8 parks the form on that basis:

> Its one instance was S6's `course ≠ start.course`, and **J4 as derived from `0001` job 2 does not exclude the same-course case**, so the judgment ranges over what the chain produces without the comparison.

The ruled source is `0001`'s second job, and its own words are:

> *Manage cross-course information in the background* says that **cross-course relations** are modelled by the knowledge base, and that **coordination over them is the coordinator's work** (#14).

The judgment the sentence names is coordination over **cross-course** relations. Under that reading J4's set is the cross-course pairs, a chain returning every pair with `course` visible on each member is precisely the superset (iv) says does not produce the set, and the position comparison has its must-judgment. The draft's escape - *"the ruled source models the relation and not only its cross-course instances"* - is an assertion about `0001`, not a quotation of it; the only text supporting the wider reading is `0100`'s downstream restatement, *"a statement about relations across obligations rather than about any one of them"*, which `0001` carries as a ground for a **different** claim (why a flat ring 0 is a defect).

So J4 is a remaining case of the superset move that is **neither shown** to have no must-judgment over the narrower set (the source's own first words name it) **nor stated as a reading with a wake** (as §4 does for `optional` and `done`). §8's wake - *"a must-judgment from a ruled source that excludes a member by a value at an earlier position"* - is arguably already fired by `0001` job 2 itself, which is what makes the parking self-undermining rather than merely thin.

This is (iv)'s own failure mode, one seam over from where (iv) was written to catch it, and §11 does not carry it.

**Repair, if the wider reading is the intended one:** state it in J4's row as a reading, with a wake in the form §4 uses - *the first real decision in which a same-course pair's inclusion mattered* - and say in §8 that the position comparison's parking rests on that reading rather than on the source.

**Verdict: BLOCKING** - threshold (a); and ambiguous-resolves-to-blocking on the reading of `0001` job 2.

---

### F3. §3 - *"Parked with J7's wake"* names a wake the record never states, against `0007`

**Section:** §3, *Candidates not on the list*. **Attack:** 5, 1.

> *Material reached by another route than `covers`*: `0012` has two further link kinds between an obligation and an artifact - `spec`, whose `given` role J7 uses, and `prepares-for` - and no ruled source names a judgment over `spec`'s `owed` role or over `prepares-for` ... **Parked with J7's wake.**

J7 is a must-judgment, not a parking, and no wake for it appears anywhere in the draft (I grepped every occurrence of *wake*: §3 has wakes for bucket 3, for Billy's comments and for lecture progress; §4 has three; §6 has one; §8 has three; none is J7's). J7's row does flag the exposure that would need one - *"That `given` names the artifact stating the requirements and `owed` the deliverable is this record's reading of `0012`'s enum; no landed record glosses either value"* - but no condition is named.

`0007` is unambiguous: *"a question cheaper to park than to answer goes on a list, and **every item names what would un-park it**"*. A park whose wake is a dangling forward-reference does not comply.

**Repair:** state J7's wake explicitly - the obvious one is *a landed record or a real instance that glosses `spec`'s `given` / `owed`* - and point the `prepares-for` / `owed` parking at it. Nothing else changes.

**Verdict: REPAIR** (additive; no ruling moves).

---

### F4. §6 - `0037` row 1 is not silent on the answer's shape, and the withdrawal is stated more strongly than the record supports

**Section:** §6, second paragraph. **Attack:** 6.

> whether the ordinal answer is a per-member value ... or **a comparison between two members**, which neither holds, **the row does not say**. Earlier drafts read it the second way and ruled on that reading; the reading is not the record's, so the ruling is withdrawn and the question is the wake's.

`0037` row 1 uses the word twice:

> Size, where it matters, is **observed rather than stored** - ordinally, from `parts` and item notes first, **then by asking for a relative comparison**. Adversarial correction ... **asking is only a remedy for a quantity the user can answer**, and the answers available are **ordinal comparisons**, not hour counts

*Asking for a relative comparison* and *ordinal comparisons* both name a between-members shape. The row is not silent; it leans, and it leans the way the earlier drafts read it. *"The row does not say"* overstates the ambiguity.

This does not overturn the outcome - leaving size's route open is the weaker claim, and `docs/agents/drafts-and-rulings.md` prefers the weaker claim - but the stated ground is wrong about the record, and the same paragraph is the one repairing `0037` row 1 elsewhere (§6's `parts` conflict), so a reader will check it.

**Repair:** say that the row's wording leans to *between members*, that the contrast it actually draws is ordinal-versus-cardinal, and that the route is left open because the row was not written to answer *which shape a stored or dispatched answer takes* - `reading-records.md`'s own rule about stating a list's question before treating it as exhaustive, applied to a row.

**Verdict: REPAIR** (the ruling - route open - stands).

---

### F5. §6 - absorption's dispatch names concepts from `parts`, which §5 rules off the row, and no read is named that supplies them

**Section:** §6, *What serves J0 today*. **Attacks:** 6, 1.

> **Absorption** arrives by asking Billy ... under `0039`'s rule, **over the concepts the coordinator can name - today the strings in `parts`, since no concept node exists** - and *how far along are you with X* is a per-member answer

§5 rules `parts` **out** of the row: *"out; returns with any `look_at`"*. So the coordinator holding the standing result cannot name a single concept. Getting them by `look_at` is one call per obligation - roughly 55 - which is the growth `0101`'s effectiveness constraint bars (*"the coordinator's call count may not grow with the graph"*), and those are fetches, not dispatch calls, so §6's escape hatch (*"whether dispatch calls count against the effectiveness constraint"* is undecided) does not cover them.

The gap is closable inside the draft's own apparatus - §2 rules that a position's field set is *"derived by the criterion for the judgment"*, so a separate resolve `START(obligation)` for the absorption judgment can carry `parts` at the obligation position in one return - but the record never says this, and as written §6's sentence and §5's `parts` cell do not compose.

**Repair:** one clause in §6 naming the read that supplies the concept names (a resolve of its own, whose position set is derived for that judgment), or state that until the concept layer lands the naming is `look_at`'s and is one of the costs the parking carries.

**Verdict: REPAIR** (J0's *set* still arrives in one return; only the observation's input path is unstated).

---

### F6. §4 / §5 - the progress `id`'s second ground is `0082`'s clause about a defaulted record in a block, which §2's empty-position ruling displaces

**Sections:** §4 (*Why it reaches `progress`* / the intent paragraph), §5 (progress position, `id`). **Attack:** 2.

§4: *"An obligation with no progress record keeps its path with the progress position empty, which `0035` reads as `not_started` and **`0082` renders without an `id`**."*
§5: *"a defaulted `progress` carries none, and **`0082` reads that absence as the signal**"*.

`0082`'s clause is: *"**A defaulted `progress` carries no `id`, and that absence is the signal.** `0035` makes absence carry `not_started`; a default is not a record, so `0061` asks no handle of it."* That is about an element for a defaulted `progress` **inside a node's block** - an element that is present and id-less.

Under §2 the ring 0 case is a different object: the crossing is optional, so what the path carries is an **empty position** that *"names the relation it ranged over"*. There is no id-less progress element; there is no progress element at all. The signal is the empty position, which is §2's own ruling, not `0082`'s. This is precisely the aspect slip `reading-records.md` warns about - a record about **how a render behaves** used for **what a path position is**.

The `in` verdict survives on the cell's first ground (*"addresses when the record exists, so the next call on the progress record is formed from it"*), which is thin but standard under `0061`'s *every read must return handles*.

**Repair:** drop the `0082` half of both sentences and cite §2's empty position as the signal; keep `0035` for what the emptiness means.

**Verdict: REPAIR** (table cell / wording; the verdict does not move).

---

### F7. §5 - the line debt is homed at #82 on a ground §5 itself refutes

**Section:** §5, *Row and line are two things*. **Attack:** 7.

> **#82 is the nearest open ticket that renders lines in ring 0's own element**, so the debt is homed there as a comment and not as a scope change.

The same paragraph opens with *"A ring 0 **row** is a position of the standing result"* and *"**Row and line are two things**"*, `CONTEXT.md`'s `the line` entry says *"a ring 0 row is not a line (`0082`)"*, and §10 item 9 changes `0089`'s noun from *line* to *row* precisely so that nothing about ring 0 is called a line any more. After this record #82 renders **rows**; it renders no lines at all.

The rest of the demotion is sound and I could not break it: `0082` (*"obligation's line is ring 0's band by a transfer of the field set"*), `0095` (*"so the band is band B"*) and `CONTEXT.md` (*"obligation's is ring 0's band B plus the edge's `type`"*) all name band B as the transfer's source; §7 dissolves band B's reduced field set; the transfer therefore has no source; the field set is owed; `0096`'s worked example stands as the landed shape. That is the demotion `drafts-and-rulings.md` asks for, and §10 item 7 carries it to all three records coherently.

**Repair:** home it on a ground that holds - #82 is the nearest open render ticket over `obligation` and the one that inherits `0089`'s corrected noun - or home it at #80's successor / a new obligation-line item and tell #82 only that its *must not be re-opened* entry moved.

**Verdict: REPAIR** (an attribution for where a debt lives; the debt's standing - owed - is unchanged).

---

### F8. §9 - #82's body reserves *whether* `has-more` appears, and §9 returns only its name and position

**Section:** §9, #82 bullet. **Attack:** 5.

§5 rules `has-more` **in**, *"as the row's one non-field item"*. #82's body says of that orphan:

> **`has-more`'s final name and position.** ... `0092` rules what it carries; **this rules whether and where it appears.**

§9 tells #82 that two items in its *must not be re-opened* list moved (`0038`'s two bands, obligation's line), and separately says *"`has-more`'s name and position stay its own"* - but never says that **whether** it appears has been settled here. #82 will still read *whether* as its own.

The move itself is right: #82's own body also says *"This ticket decides how they render, never which fields they hold"*, and membership of a routing result's position is selection, which is #86's. It is the notice that is missing.

**Repair:** one clause in §9's #82 bullet: *whether* is settled by §5 under `0101`'s criterion; only the name, the position and the `0024` collapse remain.

**Verdict: REPAIR.**

---

### F9. §3 - *"S5 is J1 · J2 · J6 composed and needs no new form"* composes a bare `FILTER` onto an optional crossing, which §2 does not define

**Section:** §3, *Candidates not on the list*, last sentence. **Attack:** 3.

S5 is *the concepts required by this term's obligations that no artifact covers*, written at #85 §7 as `START(obligation) · FILTER(P) · MOVE(requires, points-at) · FILTER(not exists(MOVE(covers, pointed-by)))`.

§2 rules two things about emptiness: an optional step *"is empty when nothing satisfies the step's whole selection"*, and *"a step from an empty position yields an empty position with the member kept"*. Both are about **steps**. A **standalone `FILTER`** applied to a path whose endpoint is an empty position has no defined truth value under either rule: `not exists(MOVE(covers, pointed-by))` evaluated at an empty concept position is neither shown to keep the member nor to drop it.

Under the draft J2's crossing is optional, so every obligation with no `requires` link reaches S5's second `FILTER` with an empty position. The composition claim therefore rests on semantics the record does not supply.

This is not threshold (d) - S5 is a candidate disposition, not a must-judgment's chain, and no chain in §3's *served by* column puts a bare `FILTER` after an optional step (J4 and J7 use selections **scoped over** their crossings, which §2 does define; J6 starts from `START(concept)` where no position can be empty). But *"needs no new form"* is a ruling in §0-§8 that cannot be checked without the missing rule.

**Repair:** either add the one-line rule (a predicate at an empty position is false, or the member is kept - the draft's own `0081` argument for optionality points at *kept*), or weaken the sentence to *S5 composes admitted forms; how a predicate reads an empty position is the grammar's* and add it to §11 beside *how a step from an empty position is written*.

**Verdict: REPAIR** (a disposition sentence, not a must-chain).

---

### F10. §11 - the one-progress-record reading is listed without a wake and without a home

**Section:** §11 / §4. **Attack:** 3.

§4 relies on the reading: *"`0035`'s **'one current value per target'** is read here as one record per target, edited in place"*. If it is wrong, the standing intent returns two paths for one obligation and §5's *row* stops being a unit, which `0089`'s per-obligation refresh (as renamed at §10 item 9) depends on.

§11 lists it - *"whether an obligation may carry more than one progress record, on which §4 relies on a reading of `0035`"* - but with neither a wake nor an owning ticket, unlike every other reading the record states. Under `0007` and under §1 (iv)'s own discipline (*state the reading and wake it*), that is the one stated reading in the draft with no condition attached.

The reading is well-supported on the merits - no field marks currency, so *one current value* has to mean one record - which is why this is repair and not blocking.

**Repair:** give it a wake (*a second progress record is observed on one obligation*) or home it at #71, which already owns where `state` lives.

**Verdict: REPAIR.**

---

### F11. §6 - *"unaffordable for fifty-five members in one return"* re-imports the premise the same paragraph says was wrongly imported

**Section:** §6, *How the two inputs enter*. **Attack:** 6.

The paragraph above it corrects exactly this move: *"The second draft turned the premise into a constraint on the observation's record, and review showed that was the premise read for an aspect it disclaims"*, quoting `0101`'s *"Affordability is a separate question the type does not answer … `0039`'s affordability is per-member depth."*

Then: *"as a `sticky_note` the observation is the dispatch branch, **unaffordable for fifty-five members in one return**"*. The substance is `0039`'s (*"eight one-line summaries can be pulled for a comparison set, eight paragraphs cannot"*) and is correct; the phrase *in one return* is the one-return premise, which `0101` says does not answer affordability.

**Repair:** *"unaffordable for fifty-five members at once"* or *"unaffordable for every member of J1's set (`0039`)"*.

**Verdict: REPAIR** (wording; the branch assignment is right).

---

## What each attack tried, where it produced nothing

**Attack 1 (a must-judgment omitted, or unservable in one return).** I re-derived the list from the ruled sources independently. `CONTEXT.md`'s opening sentence yields exactly J1, J2, J3; `0001` job 2 yields J4 and J8; job 3 yields J6 via `0003`; the requirements sentence yields J7; job 1's *"a chain that reaches the material in one return is what collapses it"* is J2·J3 composed, as §3 says. I checked `0012`'s nine rows for a cross-obligation route the list misses - `spec`/`prepares-for` are parked in §3 - and checked each *served by* chain against `0012`'s signatures and `0096`'s directions: J8's `pointed-by` / `points-at` are the right way round, J3's `covers, pointed-by` reaches the artifact, J4's second crossing genuinely needs its `[kind = obligation]` because `requires` has a `concept → concept` signature. `START(obligation)` drops nothing (`0018`'s dangling refs are the case §4 is built around), and the optional crossing with its whole-selection scoping keeps an obligation that has a `sticky_note` and no `progress`. Every *served by* cell is one chain. The only unservability I could construct is F2's (J4 under the narrow reading) and F5's (absorption's concept names).

**Attack 2 (the criterion re-run).** I re-assembled both field lists from the records independently and cross-checked them against `prototype/collection-render/settled.py`, whose `FIELDS` are `obligation: course, name, due, done_by, grade_share, parts, optional` plus `id`, `added_at` and the `grade_share_conditional` qualifier, and `sticky_note`/`progress` from `0035` and `0036`. Nothing is missing from §5's tables, so the derivation is not blind to a field. Running the criterion myself I reached §5's verdicts on `id`, `name`, `due`, `done_by`, `optional`, `course`, `has-more`, `parts`, `added_at`, the conditional-rule pointer, and on `state`, `detail`, `origin`, `created_at`, `updated_at`, `kind` and progress's `has-more`. `origin` survives independently on `0056` (*"provenance is stated prominently at every read"* against a resident `state` read every turn), which is stronger than the criterion clause the cell leads with. Two cells fell out: F1 and F6.

**Attack 3 (break a chain).** Nothing in the must-list drops a member or exceeds `0043`/`0095`. `0095`'s bound is about a block; `0101` already rules a resolve *"bounded in depth ... unbounded in width"*, and §4 records the width as an open bet rather than claiming it settled. `0043` is not engaged because `0101` rules the standing result resident by policy rather than fetched. The undefined semantics I found are F9's, and they sit in a disposition sentence rather than a must-chain; F10 is the one type assumption carried without a condition.

**Attack 4 (reasoning from `0038`'s or `0042`'s present content, or from #85 §7's scenarios, back to the purpose).** This produced no independent finding beyond F1, which is its one instance. Everywhere else the direction is right and the record says so: `parts`'s exclusion is decided by the criterion with `0038` noted as agreeing afterwards; `0038`'s seven are described as *"an independent confirmation ... and not a transfer"*; the roughly-55 and the 6,482/7,598 figures are used as cost inputs with `0038`'s scope clause and the fall26 caveat attached, not as grounds; `0042`'s *"it is present, it is routable"* is used as agreement with a range derived from J0/J1, not as its source; §3 uses #85's S1-S7 as candidates to be dispatched to a ruled source or parked, which is the discipline §3 declares.

**Attack 5 (§11 against §2, §4, §6, §8).** §2's rulings (optional crossings, whole-selection scoping, a step from an empty position, a position's field set per kind at every position) are all inside #86's assignment by both #86's unblocking comment item 3 and #85 §8; §11 correctly keeps only their *spelling*. §4's time-projection ruling is assigned to #86 by #85 §10 by name and does not touch #13's *what it holds*. §6 parks the size/absorption record whole and leaves `progress`-targets-`concept` to #25. §8's three parkings are all in §11. The only ownership slip is F8's, and the only park missing its wake is F3's.

**Attack 6 (§6's consistency).** Absorption's placement under `0039` is quoted accurately from `0101`, `0033`'s *"not another field"* and `0037` row 1's no-re-add rule are read correctly against a candidate ordinal field, and `0010` is read correctly in both halves (owner-authored, and *structural never personal* barring a stored value from becoming a set-difference subject). The `0033` / `0037` row 1 conflict the draft reports is real and I verified both sides. I pushed hardest on whether deriving §5's row from **J0** - *"what to do next, across five courses"*, the plan's judgment - reopens `0100`'s *"Ring 0's responsibility sentence is not widened"*, which §10 item 5 says stands as written. It dissolves: `0100`'s refusal is conditioned (*"Ring 0 stays narrow on the condition that some cross-node read exists beside it"*, now satisfied by `0101`), its reason was that *the plan* is undefined (§0 leaves it undefined at #14 and takes only *which reads its inputs require*), the only genuinely new items on the row are progress's `origin` and `updated_at`, both admitted on a *whether to spend the next call* ground rather than a plan ground, and #82's permission plus Billy's session ruling of J0 cover the rest. Findings: F4, F5, F11.

**Attack 7 (the line's demotion, §2's position ruling).** The demotion is coherent and correctly sourced; see F7 for the one defect, which is in the debt's home and not in the demotion. §2's position ruling holds against `0097` (a non-empty position carries an `id` and is therefore an addressable object; `course` as a bare pointer is `0097`'s other case), against `0095` (`0101`'s *one set per kind* citation of `0095` is dropped at §10 item 2 precisely because a position's set is not a line, and `0095`'s surviving *one field set per kind, does not vary per row* is what §2's *one kind at two positions* rests on), and against `0096`, whose worked example is left untouched as the landed shape. `CONTEXT.md`'s *the line* entry is amended in §10 item 13 in a way that keeps *a ring 0 row is not a line*.

**Attack 8 (§1 (iv) over every included-then-judged member).** I enumerated them: undated obligations (shown - no ruled source names *the active ones* as a set, and `0042`'s *"it is present, it is routable"* agrees); `optional = true` (reading stated, waked); `done` (reading stated, waked, with the expressible alternative named and rejected on a real ground - membership would change with a progress write); the dangling-`course`-ref obligation (Billy's ruling, with both blind spots compared); a second term's obligations (assumption stated, waked, and the width bet recorded against it); obligations that require nothing, kept by the optional crossing (shown - `0081`'s silence is the ground, and the set *is* the judgment's); J7's `owed` links (excluded by a selection, so not a superset at all); J8's two directions (two judgments, each exact). One case remains, and it is F2's.

---

## Summary

**Two blocking, nine repair.** The two blocking findings are not the derivation's spine: F1 is one table cell whose verdict survives on `0038`'s corpus argument once the `0042`/no-reader sentence - which `0099` explicitly refuses, and which the draft's own `added_at` cell says `0099` refuses - is dropped as the closer; F2 is one row of §3 and one paragraph of §8 where the same-course case is admitted on an assertion about `0001` job 2 that the job's own words (*cross-course relations*) do not carry, without the reading-and-wake §1 (iv) requires of exactly this move, and where the fix is either a stated reading with a wake or admitting the position comparison. Both are the record's own instruments turned on the record - (iv) at F2, the criterion's ground-stating discipline at F1 - which is the honest reading of a draft that spent four rounds finding one repeated move at five seams: this is a sixth and a seventh instance of *a ground borrowed from a record that speaks about a neighbouring aspect*, not a new class of defect. The nine repairs are a missing wake (F3), two overstated record readings (F4, F6), two unstated compositions (F5, F9), one un-waked assumption (F10), one misplaced debt-home (F7), one missing notice to a sibling (F8) and one loose phrase (F11). Everything the ticket was given - the formalisation, the two type questions, the must-list, the standing intent, the row's field set, size and absorption, and `0042`'s re-placement - survives falsification with those repairs applied.
