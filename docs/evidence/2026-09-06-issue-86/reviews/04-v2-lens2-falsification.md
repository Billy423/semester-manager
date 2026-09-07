# Review 4 - draft v2, lens 2 (falsification)

**Reviewer:** a fresh blind subagent, given `drafts/v2.md` and full repository read access. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-3. Blind to the lens-1 reviewer.

**Report, verbatim:**

---

Axis declared before reading: I read the draft as a derivation with three load-bearing joints - the must-list (§3), the standing intent's semantics under §2's type rulings (§4), and the row's field-by-field criterion run (§5) - and attacked each joint by constructing a concrete member the chain must handle, then checking whether the record cited for each step speaks about the aspect the step uses it for. Records read before the draft: `reading-records.md`, `drafts-and-rulings.md`, `CONTEXT.md`, the twenty-six ADRs named in the brief plus `0003` `0008` `0016` `0017` `0019` `0021` `0024` `0025` `0027` `0028` `0031` `0034` `0036` `0044` `0051` `0057` `0059` `0060` `0061` `0084` `0086` `0088` `0089` `0091` `0092` `0093` `0094` `0097` `0098`, the #84 and #86 bodies and #86's unblocking comment, #85's resolution, and the bodies of #10, #13, #14, #16, #25, #58, #82, #87, #88.

## Findings, most severe first

### F1 - BLOCKING (d). The standing intent's term predicate silently drops every obligation whose `course` ref dangles, which is the member §4 says the reshaping was ruled to keep

**Section:** §4, the intent and the paragraph *Why it starts from `obligation`, and what that costs*. **Attack:** 3 and 8.

**Construction.** Take an obligation landed before its course, or orphaned by a course deletion, or carrying a mis-copied code - the three routes §4 itself names. Run it through the intent as written:

```
START(obligation) · FILTER(exists(MOVE(course, points-at) · FILTER(term = current)))
                  · MOVE(about, pointed-by)[kind = progress]?
```

`MOVE(course, points-at)` finds no node, so the sub-chain inside `exists` is empty, `exists` is false, and `FILTER` drops the member. Nothing signals the drop: `0101`'s *"an empty result names what it ranged over"* is per result, not per dropped member, and the range as spelled - obligations whose course's term is current - honestly excludes it. The obligation is gone from the resident set with no trace.

**Against the draft's own text.** §4: *"starting from `obligation` keeps it, prints its `course` ref, and the ref fails loudly at the next call"*, and one sentence earlier, *"Every such obligation is owed, and a range over `course` cannot reach it."* The predicate is a range over `course`. The draft's stated consequence of the reshaping is false for the intent the draft writes down; the blind spot it attributes to the course-start is reintroduced by the predicate, and it is the omission axis of **faithfulness** the draft invoked to reject the course-start.

**The "fails loudly" half is also overstated on its own.** `0081` makes fetch name its boundary, so `look_at("2c0З")` would say *not in the skeleton*. But the next call from a row is `look_at(obligation)`, which succeeds; the dangle surfaces only on a call aimed at the course, which J0 and J1 never require. `0097` makes `<course id="…"/>` an addressable object, not an existing one. So even a kept row would not fail loudly - it would fail when someone happened to look.

**A spelling inside the admitted forms exists that does keep it:** `FILTER(not exists(MOVE(course, points-at) · FILTER(term ≠ current)))` - drop only an obligation whose course is known to be of another term. That uses `not`, `exists` and a comparison, all admitted at §8 and §9. But it changes the set the ruled sentence names (*"every obligation of the current term"*) to *every obligation not known to be of another term*, and whether an obligation of no determinable term is *of the current term* is Billy's to say. Either the predicate is respelled and the ruling's range wording adjusted, or §4's paragraph is rewritten to say the standing intent drops such an obligation until `0018`'s validation pass runs - in which case the draft's ground for preferring the obligation-start over the course-start (that one drops silently and the other does not) no longer distinguishes them. Verdict: **BLOCKING**.

### F2 - BLOCKING (c). §6's reachability constraint is the widening of ring 0 that `0100` records as rejected at #82, and §10 does not amend that paragraph

**Section:** §6, *The door is already open, and it carries a constraint this record adds*. **Attack:** 6 and 5.

**Record text.** `0100`, *What this record does not decide*: *"**Ring 0's responsibility sentence is not widened.** Making it *supply what the plan needs* was argued at #82 and rejected: *the plan* is undefined, and reaching a plan's inputs across five courses one `look_at` at a time is roughly 55 calls … `0039` does not bar such a read; its formalism routes it to **dispatch**. Ring 0 stays narrow on the condition that some cross-node read exists beside it."* #86's body, *What binds it*: *"`0043` - a plan's inputs cannot be made resident by widening ring 0; #82 refused that."*

**The draft.** §6: *"whatever record holds the answer must be reachable by the standing intent in one return, because J0 ranges over the whole resident set and `0101`'s premise forbids assembling its inputs member by member."* J0 is *what to do next across five courses* - the plan's judgment, by the draft's own §0 and §6 (*"the plan is where that judgment gets written down"*). The constraint therefore says: ring 0's rows must carry the plan's inputs. That is the sentence `0100` records as rejected, and its ground - *the plan is undefined* - still holds under §0, which keeps the plan's representation at #14.

**The derivation step that produced it reads `0101` for an aspect it disclaims.** `0101`'s premise is *"a judgment ranges over a set, and the set arrives in one return"*; per-member observations are `0039`'s, and `0101` says so in place: *"Affordability is a separate question the type does not answer … `0039`'s affordability is per-member depth."* Applying the one-return premise to per-member inputs rather than to the set is the move `reading-records.md` names - a rule about how a mechanism behaves read as a rule about how far it reaches.

I treat the constraint as ruled per the brief. What I report is the landed record contradicting it: `0100`'s paragraph is untouched by §10 item 5's three amendments, and #86's binding line is untouched by §9. If Billy stands by the constraint, `0100`'s paragraph and #86's line need an amendment saying why the rejection's ground no longer applies (the cross-node read now exists, and the inputs ride on a position of the standing result at zero extra calls). Verdict: **BLOCKING**.

### F3 - BLOCKING (c). A size field on `progress` re-adds a graveyarded field against `0033` and `0037`'s no-re-add rule with no ruling proposed, and narrows a shape the session ruling parked

**Section:** §6, the constraint's application (*"a typed field on `progress` **passes** it"*), §9's #16 and #25 lines, §11's *"the type of the size field on `progress`"*. **Attack:** 6 and 5.

**Record text.** `0033`: *"It does not carry size: the replacement for the removed ordinal-size mechanism is **not another field but an interaction**."* `0037` row 1: `workload · hours_estimate · workload-estimate` removed, under the header rule *"deliberately absent - do not re-add without a new ruling"*, and *"Size, where it matters, is **observed rather than stored**."* The draft's own second paragraph records the session ruling as *"each is an owner-authored observation whose **shape is parked** under a constraint stated here."*

**Three things go wrong at once.**

1. The draft decides the location - a typed field on `progress`, and for absorption a `progress` on a `concept` node - and parks only the type. That is not a parked shape; it is a chosen shape with a parked type. §11 then lists *"the type of the size field on `progress`"* as if the field's existence and home were settled.
2. A size field on `progress` is the field `0037` row 1 removed, at a different address. The no-re-add rule binds *"regardless"* (`0037` row 4's wording of the same rule), and §10 amends row 1 only to drop `parts` as a source. `0033`'s *"not another field"* is not amended at all. No new ruling is proposed, so the draft would land a record whose consequence two standing records forbid.
3. The rigidity-rule step is false by this repository's own usage. §6: *"the rigidity rule's condition is met - the standing intent is the mechanism that reads it at every refresh."* The standing intent does not read size; it carries it. Carriage is not a reader here: `grade_share` is carried in full by every block (`0095`, *own fields in full*) and is still *"no reader by standing exemption"* (`0038`, `0099`), and the draft's own §5 excludes it on exactly that ground. Size on the row has the same status.

Two further weaknesses, stated but not counted separately: `0037` row 1's ruling that *"the answers available are ordinal comparisons"* describes a relation between two members, which a per-member field on one `progress` record cannot hold without a further design; and `0035`'s drift ground (*state* and *detail* on one record because *"two records would be free to drift apart"*) does not transfer - size does not drift against state - so the analogy in §6 is decorative.

Either demote §6 to *would pass* / *the candidate that passes*, keeping the shape parked as the session ruled, and strike §11's presupposition; or rule the location now and add `0033` and `0037` row 1 to §10 with the new ruling the graveyard requires. Verdict: **BLOCKING**.

### F4 - BLOCKING (b), self-declared. J0, a must from a ruled source, is not served in one return by the standing intent plus the admitted forms

**Section:** §3 row J0, §6 last paragraph. **Attack:** 1.

The draft says it: *"Its two observations do not exist as fields, so until they do they arrive by asking Billy."* Asking is per member, `0101` leaves *"whether dispatch calls count against the effectiveness constraint"* undecided, and the draft keeps it open. By the letter of threshold (b) this is blocking; I record it as such because the brief's thresholds are the instrument, and because the draft's §3 table shows J0 as *served by* the standing intent, which it is only for its set. What discharges it is a ruling, not a repair: that J0's observation inputs are dispatch-served under `0039`'s formalism until #16's wake, and that this is not a failure of the necessity test because observations are not forms. The draft has the sentences for this in §6 and does not mark them as a ruling. Verdict: **BLOCKING** by threshold; one sentence from being a stated demotion.

### F5 - REPAIR. `origin` is admitted *"not by the criterion"* against a criterion the draft states as an iff

**Section:** §5, position 2, `origin`. **Attack:** 2.

§5 opens: *"a field belongs on a routing result's position **if and only if**, without it, the coordinator cannot form its next intent or cannot decide whether to spend the next call."* Then: *"`origin` | not by the criterion; by `0056` … | in, on `0056`."* The *only if* excludes it; the row admits it. `0056` does support loud provenance at every read of an asked answer, and a resident `state` the coordinator reads every turn is such a read, so the verdict is right. The ground is wrong: `origin` passes clause two on the same argument `updated_at` uses one row down - whether to spend a call re-confirming an `in_progress` depends on how it came to exist (asked, said) as much as on when. Re-ground it under the criterion with `0056` as the reason the harm is real. If Billy instead wants `0056` to override the criterion, `0101` needs a second amendment §10 item 2 does not carry. Verdict: **REPAIR**.

### F6 - REPAIR. J7's chain in §3 is the construction §2 says defeats optionality, and §8 spells the same chain without the `?`

**Section:** §3 row J7; §8 second paragraph. **Attack:** 3.

§3: `MOVE(spec, points-at)? · FILTER(role = given)`. §2's own constraint: *"if a kind predicate is applied after an optional crossing … the optionality has done nothing"*, ruling *"an optional step is empty when nothing satisfies the step's whole selection."* Construct: an obligation with one `owed` spec and no `given` one keeps a non-empty position through the optional step and is dropped by the filter, so the reader cannot tell *no given spec recorded* from *out of range* - the `0081` silence §2 was written to prevent; an obligation with no spec at all reaches `FILTER` at an empty relation position, and the draft defines no semantics for a filter over an empty position. §8 writes `MOVE(spec, points-at) · FILTER(role = given)` with no `?`, so the two sections disagree. Under §2 the selection is `MOVE(spec, points-at)[role = given]?`. The ruling - a filter at a relation position is admitted, by J7 - is unchanged. Verdict: **REPAIR**.

### F7 - REPAIR. The standing path has a relation position that §5's row omits

**Section:** §4 *"A two-position path"*; §5. **Attack:** 3.

§2 rules *"A relation position carries the link's fields as `0096` renders them"* - `id`, `type`, `direction`. `0101`: a path is *"node, relation, node, …"*. The standing path is obligation - `about` - progress; §4 calls it two-position and §5 derives nothing for the `about` edge. Either the row carries the edge's `id · type · direction` (which `0096` gave the edge so that `detach` can name it) or §2's rule has an exception for the standing result that the draft does not state. Applying §2 consistently is the repair; how the render collapses it is #82's. Verdict: **REPAIR**.

### F8 - REPAIR. *"at most one per target (`0035`)"* is not what `0035` says

**Section:** §4 *Why it reaches `progress`*. **Attack:** 3.

`0035`: *"one current value per target -> enforced by the service."* *One current value* is compatible with superseded records kept beside the current one. If the service keeps them, the crossing yields one path per record and no field on `progress` says which is current, so the row duplicates. The draft's reading (one record per target, edited in place per `0036`) is the natural one and is probably right; state it as a reading of `0035`'s wording rather than as its text. Verdict: **REPAIR**.

### F9 - REPAIR. One sentence in §4 settles admission's range from `0042`'s present content

**Section:** §4, *What this changes in `0100`'s clause table*. **Attack:** 4.

*"its own sentence that `0042` does not itself say that ring 0 ranges over every obligation was a doubt about the range, which `0042`'s *it is present, it is routable* settles."* The range is derived two paragraphs earlier from J0 and J1 and the opening sentence; this sentence re-derives it from the clause being overturned. *Settles* should be *agrees with*. Verdict: **REPAIR**.

### F10 - REPAIR. `kind` is listed structurally at position 1 and omitted at position 2

**Section:** §5, both tables and the row sentence. **Attack:** 2.

§2 rules *"Every node position carries its kind's line"* and `0082` makes `kind` the element name because it addresses. Position 1's table carries `kind` *in, structurally*; position 2's carries no `kind` row and the row sentence gives position 2 as `id · state · origin · updated_at`. Add it, or say the `[kind = progress]` selection fixes it and `0097`'s *a member omits what its container fixes* applies. Verdict: **REPAIR**.

### F11 - REPAIR. The predicate's target field, `course.term`, has no record declaring it and sits next to a graveyard row

**Section:** §4, §5's sources paragraph. **Attack:** 1 and 2.

§5 lists the records each `obligation` and `progress` field was assembled from and cites nothing for `course.term`. Its only grounds in this repository are `CONTEXT.md`'s *the line* entry (`id` `name` `term`) and `0094`'s example render (`term="winter-2026"`); no ADR declares `course`'s field table. `0037` row 11 graveyards `course.offering_term`. Cite the two grounds and say in one clause that `term` is the instance's term and not row 11's catalog field. Verdict: **REPAIR**.

### F12 - REPAIR. Absorption's record: `0035` is cited for a target it does not contemplate, and `CONTEXT.md`'s `progress` entry is left unqualified

**Section:** §6, *Absorption passes the same constraint*; §9 #25; §10 item 12. **Attack:** 5.

`0035`: *"no `about` link is legal -> means progress on a free topic named in `detail`."* That is a progress with **no** target, not one targeting a concept node; the draft reads it as *"already contemplates a non-obligation target."* The ground that actually admits a concept target is `0012`'s `annotation → any`. Separately, `CONTEXT.md`'s `progress` entry is *"how far along its **target's work** is"* - a concept has no work - and §10 item 12 does not list the entry. (`0010`'s first sentence, *"The modelling layer records no state about the owner"*, was tested and dissolves: annotations are not in a layer by `0027`, and `0010`'s last sentence permits an owner-authored claim.) Verdict: **REPAIR**.

### F13 - REPAIR. J2's range - one hop or the `requires` closure - is decided by default and not named as #88's closure candidate

**Section:** §3 row J2; §8 *`REPEAT` is #88's*. **Attack:** 1.

`0012` gives `requires` a `concept → concept` signature with three real instances. *What each obligation requires you to know* does not say one hop; if concept A requires concept B, the obligation requires B. The draft writes J2 as `MOVE(requires, points-at)?` and hands `REPEAT` to #88 with only its cost statements. #85 §8 assigns #88 *"whether any judgment ranges over a closure"* - a must-list question - and #88's body says the list must exist before coverage over it can be judged. If the list says J2 is one hop, #88 has nothing to cover. Name J2 (and J3 through it) as the candidate judgment for #88's closure question in §3 and §11. Verdict: **REPAIR**.

### F14 - REPAIR. Two attributions in §4's dangling-ref paragraph

**Section:** §4. **Attack:** 8.

*"`0090` lands a candidate fact blind"* - `0090`'s blindness is the extractor's; matching is *"an agent, at the surface"*. The record that says an obligation can be given a course that was never read is `0091`: *"A coordinator can therefore name a course row it never read."* That one sentence carries both the landed-before-its-course route and the mis-copied-code route; `0018` carries the orphan route. The routes are real; the citation is the neighbour. Verdict: **REPAIR**.

### F15 - REPAIR. *"the five course lines are one on-demand `START(course)` away"*

**Section:** §4. **Attack:** 3.

By the draft's own argument two paragraphs later (`0005`, nothing confines the skeleton to one term), a bare `START(course)` ranges over every course ever landed. `START(course) · FILTER(term = current)`. Verdict: **REPAIR**.

### F16 - REPAIR. §4 decides the time projection's content while §11 says it decides less

**Section:** §4 *The time projection is not resident*; §11. **Attack:** 5.

Residency is #86's by #85 §10, so *not resident* is in remit. But §4 also gives its content - `START(obligation) · FILTER(due ∈ range)` - and #13's question is *"whether a time projection over the skeleton is built at all, and if so what it holds"*, including `time_point`, location and duration. Say *expressible today as*, and point at #13 for what it holds. Verdict: **REPAIR**.

## Attacks run that produced no finding

- **Attack 1, coverage of the ruled sources.** Mapped the opening sentence's three clauses and `0001`'s three restated jobs plus its requirements sentence onto J1-J7; each clause has a row. Tested `builds-on` as a job-2 judgment: served by `MOVE(builds-on, D)`, no new form. Tested query-by-time-period: `0021` is a projection, not a judgment source. Only J2's hop count survived (F13).
- **Attack 2, the criterion over every field.** Ran it over `obligation`'s eleven fields (`id kind name due done_by optional course parts grade_share grade_share_conditional added_at`) and `progress`'s seven (`id kind origin created_at updated_at state detail`). Every verdict agrees with §5; only the grounds for `origin` (F5) and the missing `kind` (F10) differ. `created_at` out and `updated_at` in is consistent with `0099`'s quoted harm, which names `updated_at` specifically.
- **Attack 3, the optional `about` crossing with the kind selection.** Under §2's whole-selection rule an obligation with a `sticky_note` and no `progress` keeps an empty position 2 - correct. Two optional steps chained (J2 then J3) leave *MOVE from an empty position* undefined, but nothing is dropped and the semantics is the grammar's by §11.
- **Attack 4, reasoning from `0038`/`0042`'s content.** Checked `parts`, `state`, `done_by`, `optional`, and §7's partition argument; each rests on the criterion or a session ruling, with `0038`/`0042` cited as agreement. Only the *settles* sentence (F9).
- **Attack 5, sibling ownership.** #82: render items are deferred by name, `has-more`'s two questions handed over, arrangement ruled to it. #87: untouched. #88: `nodes_without`'s naming left to it; the *covered* disposition is pre-empted only for the formalisation, which #85 made #86's. #14: representation untouched. #25: a comment only. Time projection's residency is #86's by #85 §10 (F16 is about its content).
- **Attack 7, the superset principle.** Re-ran #85 §7's nine rows under (iv): no verdict changes; the *field comparison* row's ground is strengthened (START(K) with `due` visible is a superset, which (iv) says does not produce the set) rather than changed. (iv) is consistent with `0101`'s width paragraph, which it defers to. It does not bite §7's *the coordinator judges which members are near* because *near* is not on the must-list.
- **Attack 6, `0010` against absorption.** Dissolves as stated under F12.
- **Attack 8, the three production routes.** All three are real; see F14 for the citation and F1 for the *fails loudly* claim.

## Summary

Four blocking findings and twelve repairs. The blocking ones share one shape: a consequence the draft asserts is not the consequence its own construction yields. F1 - the term predicate is a chain over `course`, so the dangling-ref obligation the reshaping was ruled to keep is dropped silently by the intent as written. F2 - the reachability constraint is the widening `0100` records as rejected, and the amendment list does not reach that paragraph. F3 - the size field's location is decided while the session ruling parked the shape, and it re-adds a graveyarded field against `0033` and `0037` with no ruling proposed; the rigidity-rule step that justifies it is false by the repository's own treatment of `grade_share`. F4 - J0 is not served in one return and the draft says so; it needs one sentence marking the demotion as a ruling. The repairs are attributions (`0035` twice, `0090` for `0091`, `0056` for the criterion), two spelling defects the draft's own §2 diagnoses (F6, F7), and scoping notes (F13, F16).
