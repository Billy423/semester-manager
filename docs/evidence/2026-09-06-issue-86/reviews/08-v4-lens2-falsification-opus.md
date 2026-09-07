# Review 8 - draft v4, lens 2 (falsification), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v4.md` and full repository read access. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-7. Blind to the lens-1 reviewer.

**Report, verbatim:**

---

## Findings

### B1. §3's J8 cannot be produced in one return by the admitted forms - attack 3

**Section:** §3, row J8; and §8's `or` paragraph; and §9's #88 bullet.

**The construction.** J8 is *"which obligations this one builds on, and which build on it, across courses"*, sourced to `0001` job 2. Its served-by cell reads:

> `MOVE(builds-on, D)?` in either direction; no new form

*In either direction* is not one chain. `MOVE(builds-on, points-at)` and `MOVE(builds-on, pointed-by)` are two chains, and the draft itself rules what that costs, twice:

- §4: *"nor can a union add it back, since set operations are outside the vocabulary (`0101`) and a second chain is a second return"*
- §1 (iii): *"`or` is a form: without it, `FILTER(P or Q)` is `START · FILTER(P) ∪ START · FILTER(Q)`, a union, which the vocabulary does not contain and which is two returns"*

So J8's set - the paths from an obligation over `builds-on` in either direction - arrives in two returns, which `0101`'s premise forbids. The only forms that would produce it in one are a union over crossings, or a direction-wildcard `MOVE`. The draft admits neither: §3's *Candidates not on the list* states **"no judgment needs `or` over crossings"** and §8 parks `or` for want of a must-judgment, while the direction-wildcard was ruled at #85 to be *"exposed through `look_at`, not as its own verb"* - i.e. it is fetch's, not an intent step. §9's list of *the forms admitted by this record* contains only `MOVE(L, D)` with both named.

**The escape, and why it does not hold as J8 is written.** J8 read as starting from *one* obligation is served by `look_at(obligation)`: `0096`'s `<neighbours>` carries every edge with its `direction`, and under §5 each neighbour line carries `course`, so *across courses* is answerable in one call. But J8's cited source forbids that reading. The draft derives it from `0001` job 2, whose ground - quoted by the draft at J4 and by `0100` - is *"a statement about relations across obligations rather than about any one of them."* J4, derived from the same clause on the same page, ranges over the whole kind. Read faithfully to its source, J8 ranges over every obligation's `builds-on` relations, and `look_at` then costs one call per obligation, which the effectiveness constraint bars.

Either J8's cell is wrong (and the judgment is served by fetch, not by the chain the table names), or J8 is a must-judgment that needs a form the draft rules out. Ambiguity resolves against the draft.

**Verdict: BLOCKING.** Threshold (b).

---

### B2. §2's relation-position ruling: `role` fails §2's own fixed-by-the-intent rule, under §3's own J7 chain - attack 2

**Section:** §2, third bolded paragraph; §3 row J7; §8, second paragraph.

**The construction.** §2 rules the relation position's contents by two clauses, both stated in the same paragraph:

> `role` passes where a judgment turns on it: J7 cannot decide which `spec` artifact is worth the call without it (§3).

> The link's `kind` and its direction fail wherever the intent fixes them, which every chain written here does, and `0097`'s rule that a member omits what its container fixes applies.

Now run the second clause over J7. §3's J7 served-by cell, and §8's second paragraph, both write the chain as:

> `MOVE(spec, points-at)[role = given]?`

The selection **fixes `role = given`**. Every path in that result has `role = given` at its relation position, by construction. So by §2's own second clause - a field fails wherever the intent fixes it, and `0097` omits what the container fixes - `role` fails at exactly the position §2 admits it for.

The two clauses cannot both stand on J7. Either J7 is served by an unfiltered `MOVE(spec, points-at)?` and the position carries `role` to discriminate - which §1 (iv) forbids, since *"a superset that carries the discriminator does not produce the set"* and J7's set is the `given` links - or J7 filters, and `role` is fixed and omitted. The draft asserts the filter and then admits the field the filter fixes.

**What this changes.** §2's ruling *"and today that is `role` alone"* collapses to *no link field passes the criterion at any relation position today*, which generalises §5's *"the `about` relation position carries nothing today"* to every relation position. That is a different ruling, it is the deliverable the third review reportedly forced (the preamble: *"the relation position's contents were transferred from a render record rather than derived"*), and it is one of the two inputs §8's link-filter verdict is written on top of (*"Once a relation position carries `role` (§2)…"*).

The link-filter verdict itself survives - a predicate ranges over the vocabulary (`0101`: *"predicates over the vocabulary that may join"*), and `0017` puts a link's fields in it, so the selection is admissible whether or not the position carries the field. But §8's stated ground is the conditional, and the conditional is false.

**Verdict: BLOCKING.** Threshold (d) by analogy and (a) on §8's stated ground; a ruling in §2 that the draft's own rule falsifies.

---

### B3. §5's line ruling transfers `state` from a render record and drops `origin` and `updated_at` the same criterion clause admitted - attack 7

**Section:** §5, final paragraph (*Row and line are two things*); §10 item 7.

**The construction.** §5 admits `origin` and `updated_at` at the progress position on the criterion's second clause:

> `origin` … whether to spend a call re-confirming an `in_progress` depends on how it came to exist … `0056` is why the harm is real
> `updated_at` … whether to spend a call re-confirming a stale `in_progress` is the criterion's second clause

Then it rules obligation's line:

> **obligation's line is the obligation position's fields, `id · kind · name · due · done_by · optional · course`, plus `state` carried as an attribute**, which is how `0096`'s worked example already shows it - `state` is a J0 input on a neighbour exactly as on a row, and it is the one field that says whether a neighbour has been started.

The stated criterion for a line is the same one - `CONTEXT.md`, *the line*: *"carrying only what decides whether it is worth that call"*, which `0082`'s transfer clause says is the reason the transfer is legitimate at all (*"`ring-0.md` §1 states the same criterion … for both"*). If `state` transfers to the line because it decides whether a neighbour is worth a call, then `origin` and `updated_at` transfer for the identical reason the draft gave one paragraph earlier: a stale or merely-said `in_progress` on a neighbour is exactly as undecidable as on a row. Three of the five fields the criterion put at the progress position are dropped from the line, and the only reason offered is **"which is how `0096`'s worked example already shows it"**.

That is a transfer from a render record in place of a derivation - the move the draft's own preamble says the third review found and the fourth draft repaired at the relation position - and it is selective, since §10 item 7 simultaneously proposes to **change** `0096`'s example (*"`0096`'s worked example gains `done_by` and `optional`"*).

A real ground may exist: `0097` makes a tag without an `id` a field of the node being rendered, so `origin="…"` on `<obligation>` would read as obligation's own field, which is false. But that ground bites `state` identically, and the draft does not state it or answer it.

**Verdict: BLOCKING.** Threshold (a): `0096` does not support the field selection it is cited for; the line's field set is a ruling of this record (§10 item 7 rewrites `0082` and `0095` on it) and it is not derived.

---

### B4. §2 and §5 give the same ground ("fixed by the step's selection", `0097`) opposite verdicts at node and relation positions - attack 2

**Section:** §2, second and third bolded paragraphs; §5, both tables, `kind` rows.

**The construction.** §2, on node positions:

> A position's `kind` is fixed by the step's selection where the step names one, and `0097`'s rule that a member omits what its container fixes applies.

§2, on relation positions:

> The link's `kind` and its direction fail wherever the intent fixes them, which every chain written here does, and `0097`'s rule that a member omits what its container fixes applies.

Identical ground, identical citation. At the relation position the verdict is **fails**. At the node position §5 rules:

| `kind` | the discriminator (`0027`); `0082` makes it the element name because it addresses | **in, structurally** |
| `kind` (progress) | fixed by the step's selection; `0097` applies | **in, structurally** |

The progress cell states the ground for exclusion and returns *in*. Both positions of the standing intent have their kind named by their step (`START(obligation)`, `[kind = progress]`), so under the relation-position rule both `kind`s fail; under the node-position rule both are in.

**What is actually being conflated.** `0097`'s omission rule is a *render* rule about what a member restates (*"Inside `<obligations>` under a course, no row restates its `course`; inside `<neighbours>`, which is heterogeneous, every row keeps it"*), not a membership verdict under `0101`'s criterion. The draft uses it as a membership verdict at the relation position and as a render note at the node positions, without saying so. The correct general rule is visible in the draft's own material and is not stated: a position carries `kind` where its step does **not** fix one - which is J4's second crossing, `MOVE(requires, pointed-by)`, reaching both obligations and concepts by `0012`'s two `requires` signatures.

**Why it is load-bearing.** §5's bottom line - *"The row is `id · kind · name · due · done_by · optional · course · has-more`"* - is the deliverable handed to #82 and to the new record (§10 item 1, §9's #82 bullet). If `0097` decides it, `kind` is off both positions of the row and #82 receives a contradictory input.

**Verdict: BLOCKING.** Threshold (c) is ambiguous - `0097` is not listed in §10 at all, and it is the record the draft cites on both sides - and ambiguity resolves to BLOCKING.

---

### B5. §3 never disposes of one candidate its own standard requires it to dispose of - Billy's own comments - and §5 shows the consequence - attacks 1 and 3

**Section:** §3, *Sources* and *Candidates not on the list*; §5, the `has-more` cell; §4's standing intent.

**The construction.** §3 sets its own standard:

> Billy's raw decomposition in #84's body and #85's S1-S7 are candidates: **each is either derived from a source below or parked with a wake** (`0007`).

#84's raw decomposition, quoted in #86's own body, has two halves: *"Objective: each course's lecture progress … and each obligation's subject matter, size and progress. **Subjective: Billy's own comments, which is what `sticky_note` was designed for.** The two together are scheduling's necessary inputs."*

§3's *Candidates not on the list* disposes of three items - *lecture progress*, *absorption*, *material reached by another route than `covers`* - and S1-S7. **The subjective half is never mentioned.** It is neither derived nor parked, and no wake is named for it.

**The consequence the draft surfaces and does not follow.** The standing intent is `START(obligation) · MOVE(about, pointed-by)[kind = progress]?`, whose predicate deliberately excludes `sticky_note`. §5's `has-more` cell then records what that costs:

> on a row whose progress position is non-empty, `about` in the set says an annotation exists, which the position also shows for one kind, and **whether a `sticky_note` exists besides is not something a set of kinds ever claimed**

So an obligation carrying both a progress record and one of Billy's comments shows nothing on the row that distinguishes it from one carrying progress alone - on precisely the rows most likely to carry a comment. The draft is right that `0092`'s value ruling never claimed otherwise; that is why the gap needs a parking sentence rather than an observation. This is the omission axis of **faithfulness** operating inside the one result held resident, and §3's own standard obliges either a derivation or a park.

**Verdict: BLOCKING.** Ambiguous between (b) - if Billy's comments are a must-input, the standing intent cannot serve a judgment over them - and a stated-standard failure repairable by one parked wake; ambiguity resolves to BLOCKING. The repair may well be one sentence.

---

### B6. §3's J3 chain runs a second step from a position whose behaviour §2 parks - attack 3

**Section:** §2, first bolded paragraph, last sentence; §3 rows J2 and J3; §11.

**The construction.** §2 rules optionality and then withholds the composition rule:

> A path may therefore end at an empty position … **What a step from an empty position does is the grammar's.**

§3 then serves J3 - *where the material that teaches those concepts lives*, a must straight from `CONTEXT.md`'s opening sentence - with a two-crossing chain:

| J3 | … | `· MOVE(covers, pointed-by)?`; the artifact layer is #20's; inherits J2's hop question |

composed onto J2's `MOVE(requires, points-at)?`. An obligation with no `requires` link reaches an empty position at step 2, and step 3 runs from it. Whether that member survives with two empty positions, or is dropped, is exactly what §2 declines to say - and it is the same question §2 answered at one crossing, on the ground that dropping the member is *"the silence `0081` forbids and the omission axis of **faithfulness** names."* The draft rules the one-crossing case and parks the two-crossing case while claiming the two-crossing chain serves a must-judgment.

**A second, smaller inconsistency in the same place.** §2 parks the **behaviour** (*"what a step from an empty position does"*); §11 parks only the **spelling** (*"how an optional step … and a step from an empty position are **written**"*). The behaviour is therefore parked in §2 and not listed as undecided in §11.

**Verdict: BLOCKING.** Threshold (d) read over chains rather than only the standing intent, as attack 3 directs; the standing intent itself has one crossing and is unaffected.

---

### R1. §3's J0 cell says both observations are served by asking; §6 rules that size is not - attack 6

**Section:** §3 row J0, *served by* column; §6.

§3: *"its set by the standing intent; **its observations** by asking until their record exists (§6)."* §6: *"**Size does not fit that route**, and this record says so rather than ruling it in … So how size reaches J0 today is open."* The preamble gets it right (*"absorption reaches the coordinator by asking … and how size reaches it is open"*), so the table cell is the outlier.

**Verdict: REPAIR** (one table cell; the ruling in §6 stands).

### R2. §6 states the size-by-asking route twice more, including as the ground for the `0037` repair - attack 6

**Section:** §6, second and last paragraphs.

Second paragraph: *"Composed: **both** are things Billy is asked, answers, and the system remembers."* Last paragraph: *"**Under this record size enters by asking**, so `0037` row 1 is repaired to drop `parts` as a first source."* Both contradict §6's own gap paragraph. The repair's conclusion survives without the failed ground - the conflict is between `0037` row 1's *"ordinally, from `parts` and item notes first"* and `0033`'s *"does not carry size"* plus `CONTEXT.md`'s `parts` *Avoid* line, which is sufficient on its own.

**Verdict: REPAIR** (two wordings; the `0037` repair stands on the conflict alone).

### R3. §3's *Sources* sentence does not admit the source J0 actually has - attack 5

**Section:** §3, *Sources*.

> A judgment is *must* if it is derivable from a ruled source: `CONTEXT.md`'s opening sentence, or `0001` as rewritten at #85 …

J0's own source column reads *"Billy, in session (§6)"*, which is neither. The distinction the paragraph needs to draw - and does draw correctly against J5, whose *"only source is evidence"* - is between a ruling and evidence, not between two records. As written the standard excludes the judgment the whole of §4 is derived from.

**Verdict: REPAIR** (one wording; no ruling moves).

### R4. §3's J4 cell omits the kind predicate `0012` forces, and the hop question it inherits - attack 2

**Section:** §3 row J4.

J4's served-by is *"the position comparison"* with `course ≠ start.course`. `0012` gives `requires` two signatures - `obligation → concept` and `concept → concept` - so `MOVE(requires, pointed-by)` from a concept reaches concepts as well as obligations, and #85 §7's S6 carries `FILTER(kind = obligation and course ≠ start.course)` for that reason. J3's cell says it *"inherits J2's hop question"*; J4's does not, though the same second signature raises it there.

**Verdict: REPAIR** (one table cell).

### R5. §3 derives an admission constraint from `0041`'s present content - attack 4

**Section:** §3, *Bucket 1 and bucket 2 are J1 with `0041`'s order*.

> items owed with no date are J1's members with a null `due`, **which `0041` places last and which the standing intent may therefore not exclude**

`0041` is `0100`'s **arrangement** clause. `0100` records that its order *"owes nothing to routing"*; it says nothing about which rows enter. Deriving *the standing intent may not exclude them* from where the order puts them is a clause's present content reaching back into the purpose - the one move `0101` forbids (*"no clause's present content constrains routing"*). The conclusion is already carried by the first half of the same sentence, from the opening sentence and bucket 2.

**Verdict: REPAIR** (one *therefore*; the conclusion stands on the ruled source).

### R6. §11 lists as undecided two things §4 and §8 decide - attack 5

**Section:** §11.

§11 carries *"a multi-source start, which is a union and outside the vocabulary"* among what the ticket does not decide, while §4's bolded ruling ends *"and **a multi-source start is a union**"* - and §11's own clause states the ruling it is listing as open. Same shape for *"whether a Ref-typed field's crossing is admitted (§8, parked)"*: under the test's biconditional, §8's finding that no must-judgment needs it is a verdict of *not admitted today*, which §8 states as *"it stays open."* §9's #88 bullet gets this right - neither form appears in *the forms admitted by this record*.

**Verdict: REPAIR** (§11's wording).

### R7. §9's #82 bullet does not tell #82 that two of its *must not be re-opened* items have moved - attack 5

**Section:** §9, first bullet.

#82's body lists under *What is settled and must not be re-opened*: **"`0038` fixes both bands' field sets"** and **"The line's field set for `obligation` is a transfer from `0038`'s residency set."** §7 dissolves the bands and §5 re-derives the line, so both are now false. §9's bullet tells #82 about arrangement, `has-more`'s collapse, the band's dissolution as an orphan, and the empty relation position, but does not say that its settled-list needs two entries struck.

**Verdict: REPAIR** (one issue comment).

### R8. §5's field lists are used as exhaustive without the caveat `reading-records.md` requires - attack 2

**Section:** §5, first paragraph.

The lists are assembled from `0027`, `0028`, `0029`, `0032`, `0033`, `0037`, `0038`, `0035`, `0036` and `CONTEXT.md` - records written to answer other questions - *"because no landed record carries a field table"*. `reading-records.md`: *"Before treating any list as exhaustive, state what question it was written to answer … If you cannot say what question it answered, you may not treat it as exhaustive."* A field-by-field pass is worthless if the candidate set is short, and the draft states its sources without stating the limit.

I checked it: against #80's `prototype/collection-render/settled.py` fixture, `obligation` carries `id · kind · course · name · due · done_by · optional · grade_share · grade_share_conditional · parts` and `progress` carries `state · origin · created_at · updated_at · detail`, plus `added_at` from `0028`. The draft's lists are complete. The prototype is not a record (its own `BANNER.txt`: *"nothing should be built from it"*), so this verifies the list without supplying the caveat.

**Verdict: REPAIR** (one clause).

### R9. §4's reading of `0035` decides the row's cardinality and appears in neither §10 nor §11 - attack 3

**Section:** §4, second paragraph.

> `0035`'s *"one current value per target"* is **read here as** one record per target, edited in place

If an obligation could carry two progress records, the optional crossing yields two paths for it and ring 0's row count stops equalling the obligation count - the whole *row* framing of §5 and §9 depends on this. The reading is defensible (`0028`'s per-field update, `0036`'s in-place modification, `0035`'s enforced-by-the-service line), but it is presented as a reading, is load-bearing, and is listed neither as a ruling in §10 nor as open in §11.

**Verdict: REPAIR** (list it in §10, or state it as a ruling in §4).

### R10. §6 fixes absorption's target while parking its record whole, and does not carry `0010`'s query constraint into the wake - attack 6

**Section:** §6, third and fourth paragraphs; §11.

§6 rules *"**What record holds the answer is parked whole - its kind, its location and its type**"* and then rules *"Absorption's target is a concept, so its record hangs on a `concept` node - `0012`'s `about` signature admits any target."* A target reached by an `about` link presupposes an annotation kind, which is the half §6 parks; the same paragraph keeps a typed field on a position live as the other branch, and a field has no `about` link. §11 lists *"whether a `progress` may target a `concept`"* as undecided, which is the same question.

Separately, `0010`'s second sentence is not carried into the wake: *"Surviving set-difference queries are structural ('this concept has no artifact covering it'), **never personal** ('you never opened X')."* A stored absorption value on a concept makes *which concepts have I not absorbed* a personal set-difference query, which is what `0010` bars - a constraint on the record's shape that the wake should carry alongside `0033` and `0037` row 1. §6 cites only `0010`'s surface-but-never-resolve clause.

**Verdict: REPAIR** (one clause in §6, one sentence on the wake; the parking stands).

### R11. Two smaller attribution slips - attacks 2 and 5

- **§5, the `about` relation position.** *"`about` has no `role`; its kind and direction are fixed by the intent; its `id` is not an address"* enumerates a link's fields and omits `locator`, which `0017` puts on every link. §2 disposes of `locator` generally, so nothing changes; the enumeration is incomplete where it is stated as one.
- **§2, the edge `id`.** *"`0096`'s ground for the `id` is a write's need to name the link, which is a repair concern the test does not reach (`0101`)."* `0101` names *"the link a `detach` must name"* as a repair read; `0096`'s own sentence is *"Without it `attach` and `detach` have nothing to name"*, and `attach` at landing is a success-path write, not a repair. The conclusion is unaffected - a write's needs are not judgments the test ranges over either way - but the ground is one record wider than `0101` supports.
- **§4, the time projection.** *"The time projection is not resident."* `0101` left this open (*"whether it is resident is not decided"*) and assigned it to nobody; #13 owns the projection. Deciding it here is defensible - residency is ring 0's neighbourhood - but it is not among the clauses `0101` sends to #86, and §11 lists only *what the time projection holds* as #13's.

**Verdict: REPAIR** (attributions and one scope note).

---

## Attacks that produced no finding

**Attack 8 - §4's dangling-ref paragraph and §8's parking, against `0018`, `0029`, `0084`, `0091`, `0097`, `0101`, `0102`.** I ran every citation and the withdrawal. `0029`'s *"single-valued, mandatory and monomorphic"*, `0018`'s cascade table and its *"owed and unbuilt"* pass, `0091`'s *"a coordinator can therefore name a course row it never read"*, `0097`'s addressable-not-existent marker, `0101`'s exclusion of set operations and of repair reads, and `0102`'s membership row leaving the crossing's admission to #86 all say what they are cited for. The three production routes for a dangling `course` ref are each supported. The paragraph is internally consistent now that the absence query is withdrawn: the withdrawn query is `START(obligation) · FILTER(not exists(MOVE(course, points-at)))`, its `MOVE(field, D)` is the form §8 parks, and §1 (i) reads *without it* inside `exists`, so the parking reaches the query and the withdrawal is not a gap. §10 item 12 lists the `0018` extension to Ref-typed fields, and `0018`'s own cascade row (`delete course` → *its obligations survive*) does imply it, so the amendment is not a widening. The only residue is cosmetic: §8's heading says *from a computed set* while §4's use is a forward crossing from a start-by-kind, and §8's wake sentence covers both.

**Attack 4 (largely).** Beyond R5 I found no step reasoning from `0038`'s or `0042`'s present content back to the purpose. `0042`'s *"it is present, it is routable"* is used as agreement and labelled as agreement; §7 rests on Billy's session account of what `0042` **was**, not on its text; §5's landing on `0038`'s seven is flagged in advance as *"an independent confirmation … and not a transfer from it"*; the Width paragraph uses `0038`'s figure with its own scope clause and the fall26 caveat. The one structural worry - that §5's candidate set is drawn partly from `0038`, so the table is *filtering an existing field table against a criterion*, which is `0100`'s diagnosis of `0038` verbatim - dissolves because §6 supplies the other direction, asking what J0 needs that no field holds and finding two things. It is run for J0 only, which is enough, since J1's needs are all field-backed.

**Attack 6 (the size/absorption consistency check itself).** Setting aside R1, R2 and R10, §6 checks out against every record named. `0033`'s *"not another field but an interaction"*, `0037` row 1's *"ordinal comparisons, not hour counts"* and its no-re-add rule, `0039`'s `observe`/`else dispatch` formalism, `0101`'s *"Affordability is a separate question the type does not answer … `0039`'s affordability is per-member depth"*, `0042`'s importance sentence with its own `grade_share` gloss, and `0100`'s *"Ring 0's responsibility sentence is not widened"* (with §10 item 5 leaving that paragraph as written) are each used for the aspect they speak about. The stated gap on size is coherent as a gap: `0037` row 1's only available answer is a comparison between two members, `0039`'s dispatch returns one member's value in the shape of every other's, and no third route is invented. `0100`'s condition on ring 0 staying narrow - *"on the condition that some cross-node read exists beside it"* - is met by the on-demand chains §3 admits. Nothing on the row is a plan input the criterion did not admit, so #82's refusal stands as §6 claims.

---

## Summary

**Six blocking findings and eleven repairs.** The blocking six are, in order: J8's served-by cell needs a union or a direction-wildcard that the record rules out, so a must-judgment from `0001` job 2 does not arrive in one return; §2's admission of `role` at a relation position is falsified by §2's own fixed-by-the-intent rule applied to §3's own J7 chain, which collapses *"`role` alone today"* to *nothing today*; §5's line takes `state` from `0096`'s worked example while dropping `origin` and `updated_at`, which the same criterion clause admitted one position over, repeating at the line the transfer-from-a-render-record the fourth draft repaired at the relation position; §2 and §5 give one ground - *fixed by the step's selection*, cited to `0097` - opposite verdicts at node and relation positions, so the row handed to #82 carries a `kind` that `0097` says a member omits; §3 never disposes of the subjective half of Billy's raw decomposition, and §5's own `has-more` cell shows a sticky note going invisible on any row that also carries progress; and §3's J3 chain runs its second crossing from an empty position whose behaviour §2 explicitly parks, while claiming the chain serves a must-judgment from the opening sentence. Four of the six are repairable inside §2, §3 and §5 without moving a ruling in §4, §6, §7 or §8; B1 and B5 may each need one ruling - a bidirectional crossing or a split of J8, and a derivation or a park for Billy's comments. The eleven repairs are table cells, two contradicted wordings inside §6, one improper *therefore* from `0041`, §11's two over-listings, one issue comment #82 is owed, and four attributions. Attack 8 found nothing: the dangling-ref paragraph is consistent as it now stands, and the withdrawal of the absence query is what makes it so.
