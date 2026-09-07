# Review 12 - draft v6, lens 2 (falsification), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v6.md` and full repository read access. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-11. Blind to the lens-1 reviewer.

**Report, verbatim:**

---

## BLOCKING

### B1. §5, obligation and progress positions - `kind` is admitted at a position whose step fixes it, on a ground §2 refuses one paragraph earlier (attack 2)

§2 states the membership rule and then applies it twice, in opposite directions.

Against a link's fields:

> The link's `kind` and its direction are chosen by the intent, so the coordinator holds them before the result arrives and **learns nothing from the position**; the same holds of `role` wherever a chain selects on it, which J7's does - `[role = given]` fixes the value on every path it returns, so the position cannot be what tells the coordinator whether the artifact is worth the call.

For a node's `kind`:

> **Membership at a position is the criterion's alone** … A node position carries `kind` wherever it carries an `id`, because a Ref is a kind and an id (`0018`) and the next intent cannot be formed without both.

Run the criterion, as §2 declares it is the sole rule. The standing intent is `START(obligation) · MOVE(about, pointed-by)[kind = progress]?`. At the obligation position the step is `START(obligation)`; at the progress position the step's selection is `[kind = progress]`. In both cases the coordinator wrote the step, so it holds the kind before the result arrives, and *without it, the coordinator can still form its next intent* - it composes the Ref from the id on the position and the kind it named itself. The criterion's first clause therefore does not bite, and neither does the second. §5's own progress row concedes the fact and admits the field anyway:

> | `kind` | with `id` it is the Ref the next intent is formed from (`0018`); **that the step's selection already names it** is what lets a render omit it (`0097`), which is #82's | in |

That is exactly the sentence written against `role`, with the opposite verdict attached. `0018` supports *a Ref is (kind, id)*; it does not support *the position must carry the kind*, and it is the only record cited. So this is a ruling a cited record does not support, and it is inconsistent with §2's relation-position ruling in the same section.

Consequence: `kind` is one of the two fields §5's closing sentence adds to `0038`'s seven (*"plus the handle and the discriminator `0038` left implicit"*), so the row's field set, `0038`'s repair (§10 item 4) and the repaired line (§5, §10 item 7) all move with it. The available repair is to admit `kind` only where a step reaches more than one kind - which §2 already derives for J4's second crossing - and to say so on the row rather than "wherever it carries an `id`". Verdict: **BLOCKING**.

### B2. §3 J8 against §3 J4 - the identical phrase "across courses" gets a predicate in one row and none in the other, and §1 (iv) makes the difference decide a form (attacks 3, 8)

Both rows are sourced to `0001` job 2 and both state the judgment as reaching across courses:

> | J4 | which obligations **across courses** require the same concept, and which | `0001` job 2, via `0100`'s ground | positions compared: `course ≠ start.course` | `MOVE(requires, points-at)? · MOVE(requires, pointed-by)?[kind = obligation, course ≠ start.course]` … |

> | J8 | which obligations build on this one, **across courses**; and, as a second judgment of the same shape, which this one builds on | `0001` job 2 … | positions: both obligations | two judgments, one chain each: `MOVE(builds-on, pointed-by)?` and `MOVE(builds-on, points-at)?` |

Under §1 (iv) - *"A superset that carries the discriminator does not produce the set… the test counts the set, not the affordability of a superset"* - the two readings cannot both stand:

- If "across courses" is **restrictive**, J8's chain returns every `builds-on` neighbour including same-course ones, with `course` visible on the endpoint by §5's row derivation, and the coordinator picks out the cross-course ones. That is §1 (iv)'s forbidden move, in a must-judgment's chain, one row below the rule that forbids it.
- If "across courses" is **descriptive** - *wherever they are* - then J4 needs no `course ≠ start.course` either. J4 is the only must-judgment §9 offers #88 for the position comparison (*"The forms admitted by this record: … the position comparison"*), and the form loses its ground; §1 (ii)'s whole apparatus (a judgment declares what it ranges over) then has no instance in the must-list.

The draft never chooses. J4's predicate is inherited verbatim from #85 §7's S6 row (`FILTER(kind = obligation and course ≠ start.course)`) rather than derived from `0001` job 2, which is the vocabulary-travels-with-content hazard `docs/agents/reading-records.md` names; J8 was derived fresh and came out the other way. Ambiguous, and the ambiguity decides whether a form enters the capability list #88 checks coverage over. Verdict: **BLOCKING**.

### B3. §5 and §10 item 7 - the progress position's field set is called `progress`'s **line** and landed into `0095` as one, which §2 rules a category error (attack 7)

§2 rules:

> A position's field set is **not** the kind's line: §5 derives obligation's and finds the two differ in both directions, and a line is a render (`CONTEXT.md`, *the line*), which decides nothing at a position.

§5 then writes, of the same object:

> The progress position is **a new line for `progress`**, one ruling per kind as `0095` requires; `CONTEXT.md`'s *the line* entry says `progress` needs none, which stays true of a neighbour in a block … and is **qualified for a path position** (§10).

and §10 item 7 lands it:

> `0095`'s … *no rule generates a new kind's line* gains **`progress`'s as the first line derived under `0101`'s criterion**.

with §10 item 13 adding to `CONTEXT.md` "the entry gaining `progress`'s line as a path position". So the equation §2 forbids - position content = the kind's line - is asserted for `progress`, and it is the version that gets written into two landed records. It is also the equation the draft's own third paragraph says the sixth draft repaired (*"a node position's content had still been equated with its kind's line, which §5's own row-versus-line derivation falsifies"*): the residue survives at the second position.

Two further consequences make this more than wording. `CONTEXT.md`'s `the line` entry gives the reason `progress` needs none - *"they arrive through their own channel rather than as neighbours"* - which is `0046`'s delivery rule, and §4 spends a paragraph arguing that a path position is **not** that read; if it is not, then nothing about `0046` is "qualified", because `progress` still has no line and what the path carries is a position. And `0095`'s *"No rule generates a new kind's line: … the field set is one ruling per kind"* is being satisfied by a set derived for one intent's position, which is the transfer 0100 diagnosed in `0038` re-run one seam on. Verdict: **BLOCKING**.

### B4. §3, J0's *ranges over* cell - as declared, a must-judgment ranges over a set that cannot arrive in one return (attack 1)

§1 (ii) makes the column formal: *"the relative reading … makes each must-judgment declare what it ranges over, which is a column of §3's table"*. J0's declaration reads:

> | J0 | what to do next, across five courses | Billy, in session (§6); #14's buckets bound its inputs | **J1's set with each member's `state` (§4), plus size and absorption (§6)** | its set by the standing intent; absorption by asking until its record exists; how size reaches it is open (§6) |

`0101`'s premise is *"A judgment ranges over a set, and the set arrives in one return."* If J0 ranges over J1's set **plus size and absorption**, that set does not arrive in one return and cannot: §6 rules that size has no record and no home (*"no landed record gives such an answer a home today"*), and that absorption *"is two crossings from an obligation (`requires`, then `about`) and behind a layer that does not exist (#25), so it is unreachable today whatever its shape."* A must-judgment from a ruled source (Billy's session ruling, which §3's own source paragraph admits as a source of *must*) whose declared set is unproducible is threshold (b).

§6 states the correct framing - *"J0 ranges over J1's set; routing's obligation ends at delivering that set in one return"* - and `0039` supplies the distinction the cell needs (a judgment ranges over a set S; an observation is made *about each member of S*). The two statements are not the same and the formal one is the table's. Verdict: **BLOCKING**, repairable by moving size and absorption out of the *ranges over* cell into the *served by* cell as observations, where §6 already puts them.

### B5. §2 against §7 - J4's chain puts one kind at two positions of one result and the two rulings disagree about its field set (attacks 2, 3)

§2: *"**Every node position carries one field set per kind**, of line depth, **derived at that position by the criterion**"*.

§7: *"**Under `0101` a result carries one field set per kind**, and ring 0 carries one. `0101`: *"Each endpoint carries its own kind's deciding fields - one set per kind"*, endpoint read as position under §2's amendment."*

J4's chain is `MOVE(requires, points-at)? · MOVE(requires, pointed-by)?[kind = obligation, course ≠ start.course]` over an implicit `START(obligation)`. Kind `obligation` occupies position 0 and the endpoint of **one** result. §7's reading of `0101` requires both to carry the same field set. §2 requires each to be derived at its own position by a judgment-relative criterion, and J4 does not need `due`, `done_by`, `optional` or `has-more` at either position to decide whether the endpoint is worth a call - only `course` (which the predicate already fixes as different) and `name`. So the two rulings return different sets for one result, and the draft never says which governs. §11 lists *"the deciding fields of a `concept`, `artifact` or `course` position"* as owed, one entry per kind, which suggests the per-kind reading; §2's "derived at that position" states the per-position one.

Undefined semantics under the draft's own type rulings, in a must-judgment's chain. Verdict: **BLOCKING**.

### B6. §4 - `course.term` is asserted to exist against `0037` row 11, on a distinction no record makes (attacks 1, 3)

> `course` carries a `term` today (`CONTEXT.md`'s *the line*, `0094`'s example), the term of that offering, **which is not the catalog field `course.offering_term` that `0037` row 11 defers to v2**, so the per-member value exists and only the comparand does not.

The two cited sources support only that a `term` attribute appears on a course render: `CONTEXT.md`'s `the line` says *"course's is `id` `name` `term`"*, and `0094`'s worked example prints `term="winter-2026"`. Neither says the field is distinct from the graveyard's. `0037` row 11 reads:

> | 11 | `course.offering_term` · `course.prereq` | **Reason replaced - the row that most needs it.** … Replacement: **out for v1 because v1's boundary is coursework; deferred to v2** (`D6`) |

under `0037`'s standing rule *"deliberately absent - do not re-add without a new ruling"*. *Offering term* and *the term of that offering* are the same words in a different order; no landed record separates a v1 `course.term` from the v2 `course.offering_term`, and `0037` row 13 puts *term boundaries* in the same open-decision bucket. This is the same shape as the `parts` conflict §6 finds and reports honestly - two landed records that cannot both stand - and here the draft resolves it by assertion instead of reporting it, which `docs/agents/drafts-and-rulings.md`'s *demote to the level the evidence supports* bars.

It is load-bearing: §4's term wake is *"a second term's courses land; what wakes then is the predicate and its held value"*. If `course.term` does not exist, what wakes is a graveyard re-add plus a held comparand, which is a different and larger wake, and §11's entry (*"the term predicate and where a current-term value would be held (`0037` rows 13 and 14)"*) understates it by exactly that field. Verdict: **BLOCKING**, repairable by stating the field's existence as an assumption with its own wake, as §4 already does for one term and for `optional`.

## REPAIR

### R1. §10 item 7 - the amendment as worded puts `has-more` back on obligation's line (attack 5)

§5 states the repaired line correctly and gives the field list: *"`id · kind · name · due · done_by · optional · course · state`"*, i.e. the obligation position's set **minus `has-more`** plus `state`, and says so in the preceding paragraph (*"`0082` as repaired at #80 and `0096` both rule `has-more` off it"*). §10 item 7 then compresses it to:

> `0082`'s transfer clause, in both places it appears, becomes *obligation's line is **the obligation position's fields plus `state`***, with the derivation behind it.

The obligation position's fields include `has-more` (§5 admits it there as *"the row's one non-field item"*). §10 is what Billy's posting rules, and as written it would land a sentence contradicting `0096` (*"So `has-more` has no place in a node's render at all"*) and `0082` as repaired at #80 - neither of which §10 amends on that point (item 7 touches `0096`'s example only, to add `done_by` and `optional`). Wording, no ruling changes. **REPAIR**.

### R2. §10 item 2 - `0101` is under-listed in two places §2 overturns (attack 5)

Item 2 changes *endpoint* to *position* in five named places plus "a pointer". Two sentences that §2 rules against are not among them:

- *"What a non-endpoint position carries, whether a path may repeat a node, and how paths are deduplicated are the path's precise type, **which is the grammar's**."* §2 rules what a non-endpoint node position and a relation position carry; §11 keeps only the *spelling* with the grammar. Left as written, `0101` goes on assigning the question elsewhere.
- *"Each endpoint carries its own kind's deciding fields - one set per kind **(`0095`)**."* The citation points at the record that defines a **line**; §2 severs position from line and §5 shows obligation's two differ. The citation is stale under the draft's own ruling.

Wording of an amendment list. **REPAIR**.

### R3. §5, `due` - the cell grounds membership on evidence §0 rules is not a source (attack 2)

> | `due` | **J1's dated sequence** does not exist without it | in |

J1 is *"what is owed, across five courses, **dated or not**"*; it has no dated sequence. The dated sequence is #14's bucket 1, which §0 rules is *"evidence, not a ruling, and §3 uses it as a bound"*, and §3 repeats *"#14's three-bucket evidence bounds the must-list and is not a source of it"*. Ordering is also arrangement (#82), not a criterion clause. `due` passes the criterion under J0 - §4 says so in its own words, *"Which obligations are near is a judgment the coordinator makes with the set, using `due`, `done_by` and `state` against today"* - so the verdict survives on a different ground. Attribution. **REPAIR**.

### R4. §5, `grade_share` - the exclusion treats a "hard to do without" statement as an exhaustive input list (attack 2)

> | `grade_share`, `grade_share_conditional` | **J0's inputs Billy named are size and absorption, not a grade share**, and J1 does not turn on one; that it has no reader by standing exemption is why nothing else admits it | out |

§6 states what Billy actually said: *"deciding what to do next across five courses is **hard to do without** an obligation's size and his own absorption of a concept"*. That answers *what is hard to do without*, not *what all of J0's inputs are*, and `docs/agents/reading-records.md`'s first rule bars using it as exhaustive (*"Before treating any list as exhaustive, state what question it was written to answer"*). The fallback ground offered, *no reader by standing exemption*, is a rigidity-rule fact about the field's existence and not the criterion. The verdict survives on `0038`'s independent corpus argument - *"one course's share column sums to 95, the missing 5% has no row, and two 1% bonuses sit outside the 100"* - which §10 item 4 explicitly keeps and which this cell does not cite. Attribution. **REPAIR**.

### R5. §5, `detail` - excluded by render rules §2 rules decide nothing at a position (attack 2)

> | `detail` | the kind's one free-text field; **a line is self-closing and carries no content (`0097`; `0095` bounds it to one line)**, and the content arrives through `look_at`'s channel | out |

§2: *"Membership at a position is the criterion's alone; `0097`'s rule … is a render rule about restating, and it decides nothing here."* And *"a line is a render … which decides nothing at a position."* The ground actually available is §2's own clause that a position is **of line depth**, which is a type bound rather than a render rule and which free text fails. Note the criterion alone would not obviously exclude `detail`: `0035` puts `state` and `detail` on one record *"on purpose, because two records would be free to drift apart"*, and a `detail` reading *half done* bears on whether to spend the next call as directly as `origin` does, which §5 admits on that clause. Attribution, verdict unchanged. **REPAIR**.

### R6. §5 - one obligation field candidate never runs the criterion (attacks 2, 4)

The assembled field list is stated with its sources - *"`obligation`'s from `0027` (`kind`), `0028` (`added_at`), `0029` (`course`), `0032`, `0033`, `0037`, `0038` … because no landed record carries a field table"* - which is the right disclosure. `0032` is cited, and it names two things: `grade_share_conditional`, which the table disposes of, and *"the pointer to the rule"*, which was *"later made optional"* and which no row of §5's table mentions. Under `0032`'s own warning - *"The narrowing must not be smoothed: the pointer was half of what made the marker actionable"* - it is a field candidate, and the claim that the derivation is *"an independent confirmation of `0038`'s selection"* is weakened by a candidate that was never run. Expected verdict `out`; a row is owed. **REPAIR**.

### R7. §1 (iv) - the illustration cites a judgment §4 rules is not a must (attacks 5, 8)

> Re-run over #85 §7's table, (iv) changes no verdict and **strengthens the field-comparison row's ground**.

That row of #85 §7 is *"field comparison, connectives | obligations due before a date | no crossing reaches a date | in | `0042`'s triggers"*. §4 then rules *"No ruled source names a judgment that ranges over *the active ones* as a set"* and §7 dissolves `0042`'s partition, so the judgment the row stands on is not in §3's must-list. (iv) itself survives on its first clause, and the field comparison survives via the `kind = progress` and `kind = obligation` selections, so no verdict moves; the sentence pointing at a lapsed row does. Wording. **REPAIR**.

### R8. §6 and §11 - `0010` is cited for permitting a record its first clause speaks to (attack 6)

> Owner-authored, which `0010` permits; not the system-inferred mastery `0010` bars.

`0010`'s body opens *"The modelling layer records no state about the owner: it presents concepts and leaves judgment to him"*, and its title carries both clauses - **stateless**, and system-inferred mastery forbidden. The draft's sentence is defensible for authorship (`0010`'s *"An agent may surface a progress claim for confirmation but may never resolve one"*) and by parity with `progress`, which records owner state as an annotation rather than as a field of the obligation layer. It is not defensible for the location: §11 says *"a field would need a ruling against `0033` and `0037` row 1"*, and a field on `concept` would need one against `0010`'s stateless clause as well - which is the constraint that actually forces the record to be an annotation rather than a field. Adding `0010` to that list is the fix; no ruling moves. **REPAIR**.

## Attacks that produced no finding

- **Attack 4 (reasoning from `0038`'s or `0042`'s present content back to the purpose).** I checked every place `0038` and `0042` are cited: §4's re-placement of `0042` in `0100`'s clause table, §5's field-list assembly, §5's `state` row, §5's closing arithmetic, §7's account of what `0042` was, §6's refusal to overturn the importance sentence, and §4's width paragraph. In each the record is used either as an inventory of what exists, as corroboration after a conclusion is reached on other grounds, or as the object being repaired - never as a premise about ring 0's purpose. §5's closing sentence runs the right way (*"that it lands on the same seven is a confirmation"*), and the candidate set was wider than `0038`'s seven, so the agreement is not manufactured. The only residue is R6, which is an incompleteness in the inventory rather than a bottom-up inference.
- **Attack 3, the `optional` reading and the standing intent's own semantics.** I tried to break `START(obligation) · MOVE(about, pointed-by)[kind = progress]?` three ways: an obligation carrying a `sticky_note` and no `progress` (kept, because §2 scopes optionality over the step's whole selection, which is the constraint §2 derives for exactly this case); a `progress` with no `about` link, which `0035` legalises (does not reach the chain, which starts from obligations); and a dangling `course` (kept, and §4 derives the choice against the `START(course)` shape that drops it). The multi-`progress` case is a real hole in the row-per-obligation unit and in `refresh()`'s return, and §11 names it in terms - *"whether an obligation may carry more than one progress record, on which §4 relies on a reading of `0035`"* - so it is a stated assumption, not a silent drop. J3's and J7's chains type-check against `0012`'s signatures and neither drops a member `0081` would want kept.

## Summary

**Six BLOCKING, eight REPAIR.** The blocking findings cluster on one seam and one habit. The seam is the position/line/row trichotomy §2 introduces: it is applied correctly to the obligation position and then not applied to the progress position (B3), not applied to `kind` (B1), and left undecided when one result carries one kind at two positions (B5). The habit is a declaration made in one section and contradicted by the section that formalises it - J0's *ranges over* cell against §6's own framing (B4), and J8's chain against J4's for the same phrase from the same source (B2), which is the only place the draft's must-list produces a superset of the shape §1 (iv) forbids and which decides whether the position comparison keeps its must-judgment before §9 hands the form list to #88. B6 is a different failure: a landed-record conflict resolved by assertion where §6 shows the draft knows how to report one. All eight repairs are attributions, table cells or amendment wording; none of them moves a verdict, but R1 and R2 would land wrong sentences into `0082` and `0101` if §10 is posted as written.
