# Review 2 - draft v1, lens 2 (falsification)

**Reviewer:** a blind subagent, given `drafts/v1.md` and full repository read access. Withheld: the session transcript, its reasoning, the pre-registration. Blind to the lens-1 reviewer.

**Report, verbatim:**

---

## Axis declared before reading

I cut the draft by the seven attacks as given, and for each attack I looked for one of three things: a ruled source the must-list under-serves, a chain the draft's own type rulings let me build that loses or over-admits a member, and a record cited for an aspect it does not speak about. The five session rulings named in the draft's second paragraph are treated as ruled throughout; nothing below argues against one of them on its merits.

## Findings, most severe first

### F1 - BLOCKING. J0's ruled inputs are stored where the standing intent cannot reach them, so J0 is not served in one return

Sections: §3 (J0 row), §4 (the intent), §5 (the line), §6. Attacks 1 and 3; thresholds (b) and (d).

The draft's own text, assembled: J0 needs an obligation's size and the owner's absorption (§6, ruled in session). §6 places both as owner-authored observations whose record is an annotation, *"the default is `sticky_note` with its open `category`"*. §4's standing intent ends in `MOVE(about, pointed-by)[kind = progress]?`, which by construction drops every `sticky_note`. §5's line carries no annotation content. §3's table nevertheless says J0 *ranges over* "endpoints of J1's set, plus per-member observations (§6)" and is *served by* "the standing intent (§4)".

So under the draft's rulings the resident result contains none of J0's inputs. The ways to get them are each barred or undecided: one `look_at` per row is a call count that grows with the graph, which `0101` names as the effectiveness constraint; a second intent over `sticky_note` is a second return, and `0101` rules *"Effectiveness alone would permit a union of k fixed chains in k calls; the ruling does not"*, with `0043` as the ground that pieces fetched separately do not survive to be joined; `0039`'s `dispatch(X, member)` is one dispatch per member, and §11 leaves *"whether dispatch calls count against the effectiveness constraint"* undecided. §6's *"belong to `0039`'s layer"* names the layer without naming an operation that delivers a `sticky_note` for every member affordably, and no landed operation does.

Absorption is worse than size: it is absorption *of a concept*, so its annotation hangs on a `concept` node, two further crossings from the obligation (`requires`, then `about`), and past a layer that does not exist (#25). It is not reachable from position 3 of any obligation's path under any kind filter.

The draft cannot fix this by widening position 3 to both annotation kinds: `0095` says carrying an annotation as a line *"would make the reader spend a call to learn what a note says, which is the opposite of why `0046` gave it a channel"*, and a `sticky_note`'s content is its one free-text field, which no line carries. So the draft's placement of the inputs into `sticky_note` and its standing intent are jointly unserviceable for J0. Either J0's *served by* cell is wrong and must say what does serve it, or the inputs' home is not `sticky_note`, or `0101`'s undecided dispatch question is decided here. Ambiguous which; BLOCKING.

### F2 - BLOCKING. The endpoint criterion was run over position 2 and never over the endpoint, whose line no record rules, and `0046`'s delivery aspect is left unanswered

Sections: §2, §4, §5, §10.9. Attacks 2 and 6; thresholds (a) and (c).

`0101`'s criterion is stated on *"a routing result's endpoint"*. The draft's path is `course → obligation → progress`; its endpoint is position 3. §5 runs the criterion *"field by field over `obligation`'s field table"*, which is position 2, a non-endpoint, and never runs it over `progress`'s table: `state`, `detail`, `origin`, `created_at`, `updated_at` (`0028`, `0035`, and the prototype corpus's record shape at `prototype/collection-render/corpus.py:57`). Two landed records bear on that table and are not consulted: `0056` rules that an asked answer's provenance *"is stated prominently at every read"*, which reaches `origin` on a progress record whose `origin` is the system having asked; `0099` rules the annotation timestamps load-bearing on the ground that *"a January answer is indistinguishable from today's"*, a harm that lands on a resident `in_progress` as directly as on a block. Whether the criterion admits either is exactly the question §5 exists to answer, and it is unrun.

§5's closing sentence and §2 both say position 3 carries *"progress's line"*. No record rules one. `CONTEXT.md`'s `the line` entry says *"`sticky_note` and `progress` need none"*, and `0095` says *"No rule generates a new kind's line ... the field set is one ruling per kind"*. The draft therefore cites a line that does not exist, and §10.9 amends `the line` only to *"gain the derivation"* without striking the sentence that denies progress a line. The record title §10.1 proposes, *"its rows carry one line"*, is not true of the endpoint as drafted.

Related and part of the same finding: §4 cites `reading-records.md`'s aspect table to dismiss `0046` as *"a delivery rule about a node's render and not a scope rule over routing's vocabulary"*. The table's *actually binds* column for `0046` is **delivery**, *"how they reach the reader"*. The draft answers the scope reading and not the delivery one, and a path position is precisely an ordinary-neighbour delivery: progress arrives as one more position reached by one more crossing, which is the shape `0046`'s sentence *"never as ordinary neighbours"* names. The draft may be right that a resolve's path is not *"a read that returns a node's neighbourhood"*, but it does not say so, and `0046` is not in §10's amendment list. Under threshold (a) the cited record is used for the aspect it does not settle; under (c) `0046` is contradicted or narrowed without being listed. BLOCKING.

One type wrinkle rides on this. `0101` says a path is *"ending at an address"*. With position 3 empty, the draft's path ends at a position that `0082` says carries no `id`; the address the coordinator would spend its next call on is position 2's. The draft's §2 symmetry ruling (every position carries a line) hides this, but it does not say which position is *the member* the criterion's *next call* refers to. Either the endpoint is obligation and the intent's shape is wrong, or the endpoint is progress and the criterion is unrun over it. Both readings need one sentence the draft does not have.

### F3 - BLOCKING. `START(course)` silently drops an obligation no course reaches

Section: §4, *Why it starts from `course` and not from `obligation`*. Attack 3; threshold (d).

The construction: `0029` makes `obligation.course` mandatory; `0018` makes a dangling ref legal, rules that *"deleting a course does not cascade to its obligations"* and that they survive, and says the validation pass that recovers a dangling ref is *"owed and unbuilt"*; `0090` makes `land()` a blind write, so a candidate obligation can land carrying a course code before or without a `course` node. Every such obligation is owed (J1) and is unreachable by `START(course) · MOVE(course, pointed-by)?`. The empty-result rule cannot surface it: the intent's range is `course`, and `0081`'s boundary sentence speaks for that range, not for what lies outside it.

The draft's own ground cuts symmetrically. It chose `course` because *"a range over obligations cannot speak for a course"*; a range over courses cannot speak for an obligation no course reaches, and J1 is a judgment about obligations, not about courses. Neither direction covers both losses, and a union is not in the vocabulary. The draft must name which loss it accepts and why J1 tolerates it, or add the orphan case to the width bet's wake, or find a form. It currently does none of these. BLOCKING.

### F4 - BLOCKING (ambiguous). Judgments derivable from the ruled sources that §3 omits, and one of them decides §8's verdict on `Q`

Sections: §3, §8. Attack 1; threshold (b), resolved to BLOCKING by ambiguity.

(a) `0001` as rewritten keeps the sentence *"helping model an assignment's requirements is in scope"*. The material that states an assignment's requirements is its *given* `spec` artifact (`0012`: `spec` is `obligation → artifact, role ∈ {given, owed}`), the relation `0046` records at ~53 instances as the one the walk was built for. §3 has no judgment reaching it. §8 dismisses `MOVE` with `Q` on the reading that *"*what is owed* in the opening sentence is the obligation, not its deliverable"*, which addresses the *owed* role and says nothing about the *given* one. Whether serving *which artifact states this assignment's requirements* needs `Q` turns on what a **relation** position of a path carries: if it carries the link's fields (`0096`'s `<edge>` carries `type` and `direction`; `role` is a Link field per `0017`), `MOVE(spec, points-at)` alone serves it and `Q` is correctly parked; if it carries only the kind, `Q` is needed. §2 rules what a *node* position carries and is silent on relation positions, so §8's verdict rests on an unstated type ruling.

(b) The opening sentence's *"where the material that teaches it lives"* has more than one structural route in `0012`: `requires` then `covers` (J3's chain), `prepares-for` (`artifact → obligation`), and `spec`. J3 admits one. From the same start the others are a second chain, hence a second return under `0101`'s premise, and `or` over crossings is not a form the draft admits (§8 parks `or`). Whether each route is a *must* is Billy's, but the draft claims its must-list is enumerated from the ruled sources, and nothing in any record confines *material* to `covers`.

### F5 - REPAIR. §4 misattributes `0100`, and *depth partition* contradicts the `0042` sentence §7 says stands

Sections: §4 last paragraph, §7. Attack 7.

The draft quotes `0100`'s *"`0042` does not itself say that ring 0 ranges over every obligation"* as `0100` having *"half-saw"* that every row enters. The sentence says the reverse: it doubts that `0042` establishes an every-obligation range. The substantive reading is nevertheless supported by `0042` itself (*"An undated obligation is in band B ... it is present, it is routable"*), so the ruling stands and only the attribution moves.

Two wording repairs on the same passage. `0100` had already placed band B's field set under **selection** (*"what a refresh returns is a line, whose field set is band B, which is the selection clause"*), so *mislabelled* is half right: `0100` split `0042` across two clauses rather than putting it in the wrong one. And §7 calls `0042` *"a depth partition"* while saying `0042`'s defence *"was never refuted and is not refuted here"*; that defence is the sentence *"Two bands do not violate uniform depth"*. The draft cannot both keep it and call the bands a depth partition. *A per-row field-set partition* is what `0038`'s text describes and what `0100` already called it.

### F6 - REPAIR. `has-more`'s admission cites a ground the draft's own ring 0 half-removes

Section: §5, `has-more` row. Attack 4.

`0096`: `has-more` *"survives only where the neighbourhood cannot be listed, and that is ring 0"*, because `<neighbours>` *"strictly contains that set"* and `0024` bars stating one fact twice. The draft's ring 0 row now lists one link kind's neighbours, the `about` crossing to progress. On a row whose position 3 is non-empty, `about` in `has-more` restates the path; on the same row it cannot say whether a `sticky_note` also exists. `0092`'s ground, *"ring 0 cannot list a node's neighbourhood"*, is now true of every kind except `about`. The row's citation of `0101` §1 and `0092` is reasoning from those records' assumption of `0038`'s placement. Say what `has-more` holds on a row that already shows an `about` edge, or hand that to #82 by name rather than only its position.

### F7 - REPAIR. §9 pre-decides the arrangement it assigns to #82

Section: §9, #82. Attack 5.

The third input, *"position 1 of the path is available as a grouping key and is not a default"*, fixes a value on the grouping question. `0041`'s grouping was struck at #82 for *"fixing a value on `0039`'s symmetry rule rather than deriving it"*; fixing the opposite value without derivation is the same move. *No default is set here* carries the same information without ruling.

### F8 - REPAIR. *Four* fields is three

Sections: §4 (*"four more fields"*), §7 (*"four fields on 43 more rows"*). `0038`: *"band B drops the last three"* - `optional`, `done_by`, `has-more`. Re-typing `course` and `state` as positions does not change the difference.

### F9 - REPAIR. §5's table: `kind` missing, one non-discriminating ground, one asserted verdict, position 1 unrun

Section: §5. Attack 2.

`kind` is a field on every node (`0027`) and an addressing attribute (`0082`); it is absent from the table. `done_by`'s second clause, *"off the row it costs one `look_at` per obligation"*, is true of every excluded field and so discriminates nothing; the row's working ground is *a direct J0 input*, and only that. `optional`'s verdict, *"decides directly whether a call is worth spending"*, is asserted and not tied to J0 or J1; the stronger ground is that an `optional = true` obligation is arguably not *owed*, which bears on J1's membership and which the draft's empty predicate silently includes. Position 1's `term` is inherited from `CONTEXT.md` and never run through the criterion for J0 and J1.

### F10 - REPAIR. Two landed sentences become false and are not in §10

Section: §10. Attack 6.

`0019`: *"residency is an access policy over **obligation nodes' fields**"*. `CONTEXT.md` `obligation`: *"the same nodes ring 0 is a projection of"*. Under the draft ring 0 holds `course`'s `name` and `term` and `progress`'s `state`. Neither sentence is listed. This is REPAIR and not threshold (c) because `0019`'s ruling, two persisted things, is untouched; only its descriptive clause moves. The `obligation` entry belongs in §10.9's list beside `ring 0`.

### F11 - REPAIR. The width bet assumes one term and does not say so

Section: §4, *Width*. Attack 3.

`course` carries `term` (`0094`'s render, the prototype corpus); `0005` rules the store accumulates and is never synced; no record confines the skeleton to one term. `START(course)` with an empty predicate therefore ranges over every course ever landed, and the roughly-55 figure is one term's. The opening sentence says *"five **concurrent** courses"*. State the one-term assumption as part of the bet, or admit `term` to the predicate and say which ruled judgment carries it.

### F12 - REPAIR. *Lecture progress* is parked on a bottom-up ground

Section: §3, *Candidates not on the list*. Attack 4.

The stated ground is *"no structure carries *where a course has got to*"*, which decides a must by what the model holds - the direction `0070` and `0100` diagnose. Parking is permitted because Billy's decomposition is unruled; the admissible ground is *not derivable from a ruled source*, with `0021` as why the structure is absent rather than as why the judgment is.

## Attacks run that produced no finding

- **Attack 3, duplicate paths at position 3.** Tried: a superseded progress record surviving beside the current one, giving two paths per obligation. Dissolved: `0035` rules *"one current value per target -> enforced by the service"* and `0028` makes every field CRUD-able in place, so a state change is a `set`, not a second record.
- **Attack 3, position 2 admitting artifacts or concepts.** Tried: a later layer's kind carrying a `course` Ref, entering ring 0 through the unfiltered second crossing. Dissolved: `0029` makes `course` *"a property of `obligation` rather than of every node"*.
- **Attack 4, §5's field-by-field pass as `0038`'s construction repeated.** Tried: the pass is literally a filter over the existing field table. Dissolved: the instrument `0101` rules is itself a per-field criterion on the endpoint, and #86's comment assigns exactly that application here; the admission of `done_by` and `state` rests on the session ruling that the window becomes the coordinator's judgment rule, not on `0042`'s content as such. What survives is F9's wording and F2's wrong position.
- **Attack 5, the time projection.** Tried: §4 rules it not resident while #13 holds it. Dissolved: #85 §10 assigns *"whether the time projection is resident"* to #86 by name.
- **Attack 5, the `0102` cell and §0.** Dissolved: #86's comment item 4 gives the Ref-crossing verdict to this ticket; §0 is a session ruling and treated as ruled.
- **Attack 5, §6's repair of `0037` row 1.** Tried: an out-of-scope edit. Dissolved: the conflict is real (`0037` row 1, *"from `parts` and item notes first"*, against `0033`, *"does not carry size"*, dated 2026-08-28 and later than the graveyard row, and `CONTEXT.md`'s `parts` *Avoid*), and the repair direction follows the later ruling.
- **Attack 6, `holder`, `coordinator`, `0044`.** Tried: three positions making something new a holder, or ring 0 resident for someone else. Dissolved: nothing in the draft keeps state anywhere but the coordinator's context; `0044`'s *"resident for the coordinator and for nobody else"* is untouched.
- **Attack 7, the substance.** Tried: `0042` as a genuine admission clause. Dissolved: *"it is present, it is routable"* and *"Two bands do not violate uniform depth"* both place every row inside ring 0. Only the attribution and the label move (F5).
- **Attack 1, #14 bucket 3 and `0001` job 3.** Tried: J5 and J6 as under-served. Dissolved: J5 is correctly must-with-predicate-owed and refused rather than returned empty under `0101`; J6 is `0003`'s query and `nodes_without` is a spelling of it under §1(iii).
- **Attack 2, `parts`, `grade_share`, `added_at`.** Tried: the criterion admitting one of them for J0 or J1. Dissolved for `parts` (J2's, not J0's) and `added_at` (`0099`'s row-versus-node line); `grade_share` is out on *no reader* plus the session ruling naming size and absorption as J0's inputs, which is an argument and is stated as one.

## Summary

Four BLOCKING findings and eight REPAIR findings. The four blocking ones share one root: the standing intent's third position was designed to carry `state` and nothing else was checked against it - the judgment whose inputs live in `sticky_note` (F1), the endpoint criterion and `0046`'s delivery aspect at that position (F2), the range the first position silently excludes (F3), and the relations from an obligation that the must-list never enumerates (F4). None of the twelve contests a session ruling; F1 and F2 are the two that change what the record §10.1 proposes would say.
