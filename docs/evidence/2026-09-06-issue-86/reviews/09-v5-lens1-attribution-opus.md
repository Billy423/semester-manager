# Review 9 - draft v5, lens 1 (attribution), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v5.md`, full repository read access, and `docs/agents/reading-records.md` as the discipline. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-8. Blind to the lens-2 reviewer.

**Report, verbatim:**

---

## BLOCKING

### B1. `0095`'s transfer sentence states what §5 overturns, and §10 item 7 does not list it

**Section:** §5 (*Row and line are two things*), §9 (#82), §10 item 7.

**Claim:** *"`0082`'s transfer clause, stated twice there, and `0095`'s "so the band is band B" are repaired to the sentence above"* (§5), and to #82: *"obligation's line is no longer a transfer from `0038`'s residency set"* (§9). §10 item 7 scopes the `0095` edit to **two sentences**: the band sentence, and the *no rule generates a new kind's line* sentence.

**What the record actually says.** `0095` §*The line's field set is not derivable* opens:

> `0082` sets obligation's line by a **transfer** - `0038` chose that field set for **residency**, and it is reused for *is this worth one call* because `ring-0.md` §1 states the same criterion for both.

That is a third sentence, and it is the one that states the thing §9 tells #82 is no longer true. It is not the band sentence and it is not the *no rule* sentence, so item 7's enumeration leaves it standing. Once item 7 repairs `0082`'s transfer clause, this sentence also becomes a false report *about `0082`* - it names a clause that will no longer read that way.

Two further `0095` sentences in the same section ride on the same reading and are unlisted: *"The transfer is sound here and reaches no further"*, and *"A line that picked each row's own band would import `0038`'s residency computation into a read"* (vestigial once band B dissolves - harmless, but it is a band mention the §10 sweep did not catch).

**Aspect mismatch:** none - the sentence is squarely on the aspect §5 rules. The defect is enumerative, not interpretive.

**Verdict: BLOCKING.** The fix is small - item 7 becomes *`0095`, three sentences* and names the transfer sentence - but as written a landed record keeps asserting the transfer §5 dissolves.

### B2. `course` carries a `term` in two landed records, and §4 argues from `0037` row 11 as though it did not

**Section:** §4 (*Why there is no predicate, and what that assumes*), against §2.

**Claim (§4):** *"no record confines the skeleton to a term - `0037` row 11 defers `course.offering_term` to v2 on the ground that v1's boundary is coursework - so once a second term's courses land a bare `START(obligation)` ranges over both"*, and *"the value it compared against, the current term, is held nowhere - `0037` rows 13 and 14 leave term boundaries open."*

**What `0037` row 11 says:**

> | 11 | `course.offering_term` · `course.prereq` | … Replacement: **out for v1 because v1's boundary is coursework; deferred to v2** (`D6`) |

**What two other landed records say.** `CONTEXT.md`, *the line*:

> Per kind it is **one** field set that does not vary per row: obligation's is ring 0's **band B** plus the edge's `type`, **course's is `id` `name` `term`**.

`0094`'s worked example renders it:

> `<course id="2c03" name="…" term="winter-2026">`

So `course` carries a term today in the glossary and in a landed render, and `0037` row 11 rules `course.offering_term` out for v1. The draft relies on **both sides in two different sections**: §2 cites `CONTEXT.md`'s `the line` for *"Course's line is `id` `name` `term`"*, and §4 cites `0037` row 11 for the absence that makes the term predicate unwritable.

**Why it is load-bearing rather than cosmetic.** If `course.term` exists, the term predicate's **per-member** value is available and only the **comparand** (the current term) is missing - which is a different wake from the one §4 and §11 record. §11 parks *"the term predicate and where a current-term value would be held (`0037` rows 13 and 14)"*, which is the comparand half only; nothing parks or repairs the `course.offering_term` / `course.term` conflict itself. §10 lists no repair for it, and §6 sets the precedent that this draft repairs exactly this class of conflict when it finds one (`0037` row 1 against `0033`).

**The ruling survives.** *No predicate* stands on its independent and decisive ground - the second draft's chain over `course` dropped the dangling-ref obligation (§4, on `0018` + `0091`). What needs repair is the paragraph's supporting citation and a §10 entry naming the conflict.

**Verdict: BLOCKING** (ambiguous-resolves-to-blocking: a landed record contradicts a landed record the draft leans on, in a paragraph whose ruling depends on the reading, and §10 lists neither for repair).

---

## REPAIR

### R1. `0089`'s title and its README row still say the refresh returns **lines**

**Section:** §4 (*What `refresh()` reports*), §10 items 8 and 9.

**Claim:** *"`0089` returns a whole line per changed obligation; under this record the unit is the row (§5) … its noun and one pointer are owed (§10)"*; item 9 is *"`0089`, one sentence."*

**What the record says.** `0089`'s **title** is *The read side is two verbs, and the refresh returns whole lines rather than a delta*, and its body says *"What `refresh()` returns is a whole **line** per changed obligation"* and *"what element a ring 0 **line** uses is open"*. `docs/adr/README.md` reproduces the title verbatim as `0089`'s row.

Under §5 (*Row and line are two things*) and `CONTEXT.md`'s `ring 0` entry (*"A ring 0 row is not a line"*), a title saying *whole lines* names the wrong object. §10 item 8's README restatement list is *"`0038`'s, `0042`'s and `0100`'s rows"* - `0089` is not in it, and item 9's *one sentence* does not reach a title.

**Also in item 8:** `docs/adr/README.md`'s group heading for the observation contract is a number range - *"`0038`–`0046` · `0082`–`0085` · `0089` · `0092` · `0094`–`0101`"* - which has to admit the new record's number, not only gain a row.

**Verdict: REPAIR.** Add `0089` (title, body noun, README row) to item 8; extend the group-heading range.

### R2. §10 item 2's *five sentences* of `0101` mis-slices the endpoint→position edit

**Section:** §2, §10 item 2.

**Claim:** *"`0101`, five sentences. Endpoint becomes position in the three sentences that use it in §2's sense - the path's endpoint carrying what decides the next call, each endpoint carrying its kind's deciding fields, and the criterion itself; "ending at an address" becomes ending at a position…; a pointer to the new record."*

**What `0101` actually contains.**

- *"the path's endpoint carrying what decides the next call"* and *"ending at an address"* are **one sentence**: *"A path is the chain a member arrived by - node, relation, node, … - ending at an address, and the endpoint carries what decides whether it is worth the next call."* Two of the five items land on the same sentence.
- *"ending at an address"* occurs a **second** time, in the definition paragraph: *"**Resolve** takes an intent the caller can state in the skeleton's structural vocabulary and returns the paths that satisfy it, each ending at an address."* The item names it once.
- One sentence using *endpoint* in exactly §2's sense is **unlisted**: *"**The set is symmetric**: every endpoint at one depth, and where paths differ in shape that asymmetry comes from the material."* §2 rules the criterion runs at every position, so symmetry has to be over positions too.

**Verdict: REPAIR.** Re-cut the enumeration; the ruling (endpoint → position) is unaffected.

### R3. *"`0033` is the later ruling"* is not supported by either record

**Section:** §6 (*A conflict between two landed records*).

**Claim:** *"Both cannot stand, and `0033` is the later ruling; `0037` row 1 is repaired to drop `parts` as a first source."*

**What the records say.** `0033`'s Source line: *"fall26:records/spec/write-rules.md §3.4 (Billy, 2026-08-28); fall26:records/spec/schema.md §3 and changelog ×2 2026-08-27"*. `0037`'s Source line: *"fall26:records/spec/schema.md §7 (header and all sixteen rows) and §9 item 4…"* - **no date for §7**. Nothing in either record dates row 1 against `0033`, so *later* is asserted rather than derived. `docs/agents/reading-records.md` puts re-deriving a load-bearing number or ordering before it is used exactly here.

**The repair does not need it.** The same paragraph already cites the current glossary - `CONTEXT.md`'s `parts` entry, *"Avoid: … using it to judge how much work something is"* - which is a standing statement rather than a dating argument, and `0033`'s own title (*does not carry size*) is the ruling. Drop the *later* clause or replace it with the glossary ground.

**Verdict: REPAIR.**

### R4. §3 J3 assigns *the artifact layer* to #20 alone

**Section:** §3, J3's *served by* column: *"the artifact layer is #20's"*.

**What the records say.** `0101`: *"for `concept` and `artifact` it is the debt #17, #19 and #20 carry."* `CONTEXT.md`, *the line*: *"the debt for `artifact` and `concept` travels with their layers, deferred at #20, #19 and #17."* #58's *Out of scope*: *"The artifact and concept layers, and the vector store. Deferred at #20, #19, #17."* No record assigns the artifact layer to one of the three; #20's own title is *The materialization pass*.

**Aspect mismatch:** an issue that owns **one pass over artifacts** is being cited for ownership of **the layer**. §2 and §11 get this right (*"#17, #19 and #20"*); J3 is the one place it narrows.

**Verdict: REPAIR.**

### R5. *"a line carries no content"* is `0097`'s statement, not `0095`'s

**Section:** §5 (`detail` row), §6 (*What record holds the answer is parked whole*).

**Claim:** *"the kind's one free-text field; a line carries no content (`0095`)"*, and *"a `sticky_note`'s content is its one free-text field, which no line carries (`0095`)"*.

**What `0095` says:** *"**Anything reachable, one line**, because `0060` fixes the cost of depth"* and *"the only unbounded thing in a return is the node itself; everything reachable from it is bounded to a line."* It bounds a line's **depth**; it never says a line carries no content.

**What `0097` says:** *"**An open/close pair carries content.** A pointer and a projection are not content, so a line is self-closing and what it was carrying moves onto the element that owns it."* That is the sentence the draft needs, and §5 already cites `0097` correctly for *"A line is self-closing (`0097`) and has no positions"* two paragraphs later.

**Aspect mismatch:** a rule about a section's **depth** used for what a line's **element shape** admits. `reading-records.md`'s *cite the record that states the claim* is the discipline; the conclusion is right either way.

**Verdict: REPAIR.** Cite `0097` (or both).

### R6. *"the projection"* bare, in a record whose subject is ring 0

**Section:** §4 (*The time projection is not resident*): *"What the projection holds beyond that - `time_point`, location, duration - is #13's."*

`CONTEXT.md`'s `ring 0` entry lists *"the projection (bare)"* under **_Avoid_**, and `0100` states the reason in place: *"Projection is deliberately not reused: `0089`, `0094` and `0021` all use it for the whole of ring 0."* The antecedent here is the time projection and it is one sentence away, but the surrounding record is about ring 0, which is what the _Avoid_ exists to prevent.

**Verdict: REPAIR.** Write *the time projection*.

### R7. §2 over-reads its own §1 (ii)

**Section:** §2 (*Every node position carries its kind's line*): *"a judgment over paths ranges over every position (§1 (ii))"*.

§1 (ii) rules: *"Two chains produce the same set for a judgment if and only if they differ only at positions the judgment does not range over."* That presupposes some positions a judgment does **not** range over; it does not yield *every judgment ranges over every position*.

The ruling does not depend on it: the load-bearing ground in the same paragraph is the cost argument - *"a position carrying only an id would make which concept in job 2 cost one `look_at` per intermediate, which `0101`'s premise forbids"* - which is #85 §7's own reasoning (*"if only an id, which concept in job 2's judgment costs one `look_at` per intermediate, which §4's premise forbids"*) and is sound.

**Verdict: REPAIR.** Drop or re-word the `(§1 (ii))` support.

### R8. `0102`'s membership row is a pointer debt §10 item 14 does not list

**Section:** §8, §10 item 14.

`0102`'s deviation table, membership row: *"For routing a Ref-typed field is crossable in the vocabulary; **whether the crossing is admitted is #86's**"*. §8 answers it (*not admitted today*, parked with a wake). The row is not wrong - it points at the ticket, and the ticket now carries the answer - but item 14 exists for exactly this class (*"each describe the state this record amends and none contradicts it"*), and `0102` is the one record with a live open pointer at #86 that item 14 omits.

**Verdict: REPAIR.**

### R9. §2's list of a link's fields omits its endpoints

**Section:** §2: *"A link's fields are `kind`, `role` where the kind has one, and `locator` (`0017`; `0012` gives `role` to `spec`)."*

`0017`: `Link := from: Ref · to: Ref · kind: LinkKind · role?: string · locator?: string`. `from` and `to` are the path's adjacent node positions, so nothing follows from the omission - but `reading-records.md`'s first rule asks that a list state the question it is complete for. One clause (*besides its endpoints*) closes it.

**Verdict: REPAIR** (lowest severity).

---

## Citations checked and found sound

**Records, by the aspect the draft uses them for.**

- `0101` - the informal test and *"admits by what a form lets a chain produce"* (§1 iii); the ground for paths, *"a judgment across obligations is a judgment about their relations"* (§1 ii); the criterion, verbatim to the word except *endpoint* (§2, §5); *"Each endpoint carries its own kind's deciding fields - one set per kind"* (§7); *"Affordability is a separate question the type does not answer … `0039`'s affordability is per-member depth"* (§6) - and correctly used **against** the second draft's reading of the one-return premise; the one-return premise (§2, §4); *"an intent the system cannot yet serve is refused, never returned empty"* (§3); the vocabulary containing no set operations (§4); the spontaneity paragraph naming `has-more` as the in-band carrier (§5); repair reads outside the test's reach (§4, §11); the edge-id/id-space open question (§2); the unruled width gate (§4); resolve entering through fetch at `look_at(course)` (§8); *"an unprompted coordinator needs somewhere to stand"* (§4).
- `0100` - `0042` placed as **admission** and the refresh return as *"a line, whose field set is band B, which is the selection clause"* (§4); the doubt, *"`0042` does not itself say that ring 0 ranges over every obligation in a semester"* (§4); the refusal to widen ring 0 (§6); `0041`'s struck grouping and `CONTEXT.md`'s `reload` never read together, and `0040`'s **method** rather than its ground (§9).
- `0042` - *"it is present, it is routable"* for the undated case (§3, §4); `state == in_progress` as a trigger (§5); the three triggers, the importance sentence and the breadth sentence as what survives (§7); the defence *"computed from material facts plus one rule applied identically"* argued against `0039` (§7); and the draft is **right against #86's own body**, which attributes the overturn permission to #84 - `0042` and `0100` both name **#82**.
- `0038` - the seven fields and band B dropping the last three (§4, §5, §7); `parts`'s exclusion ground and *"excluded from the projection is not unreadable"* (§5); the roughly-55 figure with its scope clause excluding the obligation-dense course (§4).
- `0082` - `id`/`kind` as attributes *because they address* (§5); the `Ref`-typed field as a bare pointer answering *which one* (§4, §5); `locator` *"says where you land after walking, which does not bear on whether to walk"* (§2); `has-more` and `role` as the second exception, in no field table (§5); *"`has-more` is not on the line"* as repaired at #80 (§5); the transfer clause stated twice (§5); a defaulted `progress` carrying no `id` (§4, §5); the Source line pointing at the fall26 schema for the field tables (§5).
- `0096` - the `<edge>`'s `id` existing so `attach`/`detach` can name it (§2); `<edge>` carrying `id`, `type`, `direction` (§2); `has-more` having no place in a node's render (§5); and the worked example is exactly band B plus `id`, so *"gains `done_by` and `optional`"* (§5, §10 item 7) is arithmetically right.
- `0095` - *"so the band is band B"* (§5); *"no rule generates a new kind's line … one ruling per kind"* (§5, §10 item 7); a line is one field set per kind that does not vary per row (§5).
- `0097` - a line is self-closing (§5); *a member omits what its container fixes* correctly scoped as a **render** rule that decides nothing about membership (§2) - this is the aspect discipline applied correctly, and it is the draft's best single move.
- `0092` - the value ruling (the set of link kinds on the node, not a count) untouched (§5); the four band mentions all fall inside the three locations §10 item 14 names (opening sentence, Considered Options, Source line).
- `0093` - the `<edge>` names row; **exactly two** rows of the rejected-names table mention the band (`attention`, `status`/`state`), which is the count §10 item 14 states; the ring 0 section.
- `0094` - the closing sentence carrying *the band's representation* (§10 item 14).
- `0099` - `added_at` as *about the row, not the node*, and *no reader* as the ground `0099` declines (§5); the `updated_at` harm, *"a January answer is indistinguishable from today's"* (§5).
- `0091` - *"a coordinator can therefore name a course row it never read"*, used for exactly its own aspect (§4); *"Ring 0 carries the band"* (§10 item 14).
- `0046` - read as a **delivery** rule and explicitly not as a scope rule, with `reading-records.md` cited for the misreading (§4); annotations reaching the coordinator through their own channel (§3).
- `0018` - a ref may dangle, deleting a course does not cascade, the link-set validation pass *"owed and unbuilt"* (§4); `Ref := (kind, id)` (§2, §5).
- `0035` - *"one current value per target"*; `state` on `progress` and not on `obligation`; absence reading as `not_started` (§4, §5).
- `0037` - row 1's *"observed rather than stored - ordinally, from `parts` and item notes first…"* and *"ordinal comparisons, not hour counts"* (§6); row 11 (§4, quotation exact); rows 13 and 14 on term boundaries (§4, §11).
- `0033` - *"not another field but an interaction"*; *does not carry size* (§6).
- `0039` - the observe/dispatch formalism and the return coming back in the same shape as every other member's (§6); symmetry scoped to the set the judgment ranges over (§2).
- `0010` - an agent may surface a progress claim but never resolve one; *structural, never personal* (§6).
- `0056` - *"provenance is stated prominently at every read"* (§5); the asked answer kept (§6); `origin`'s write rule owed (§11).
- `0001` - *"helping model an assignment's requirements is in scope"*; job 2 via `0100`'s ground; job 3 via `0003` (§3).
- `0003` - `nodes_without` as the set-difference query (§1, §3 J6, §9).
- `0012` - `about: annotation → any`; `spec: obligation → artifact, role ∈ {given, owed}`; `requires` with **two** signatures; `builds-on: obligation → obligation` (§2, §3).
- `0017` - the natural key, `role` and `locator` as link fields, no update (§2, §8).
- `0026`, `0027`, `0028`, `0029`, `0032`, `0036` - the field provenances §5 lists; `obligation.course` mandatory; per-field CRUD; the one-free-text-field cap; `origin` across both annotation kinds.
- `0021` - query-by-time-period as a separate projection; the coarse grouping deliberately not modelled (§3, §4).
- `0089` - whole lines per changed obligation; the trigger (§4).
- `0019` - *"residency is an access policy over obligation nodes' fields"* (§10 item 11).
- `0013` - the roughly-55 cost argument (§10 item 14).
- `0102` - the membership row placing the Ref crossing in the vocabulary and its admission at #86 (§8).
- `0070`, `0071`, `0081`, `0007`, `0043`, `0044`, `0041`, `0040`, `0051` - capabilities not shapes; the success-path warning; the *not held vs not found* silence; parking with a wake; the discard; residency in the conversation; the order ruling and the struck grouping; the method not the ground; conflicts.
- `0044` **does read clean** against this record, as §10 item 14 asserts.

**`CONTEXT.md`** - the opening sentence as the source of J1-J3; `id` (*says nothing about the record it names*); `handle`; `Ref`; `covers` as the rendered/teaching relation; `applies` on a resolve's path; `the line` (course's fields, the `progress`/`sticky_note` clause, the #17/#19/#20 debt, *a ring 0 row is not a line*); `ring 0` (governs residency, not readability); `parts`'s _Avoid_; `progress`'s *how far along its target's work is* not yet covering a concept; `dispatch` including asking the owner. **No term from any _Avoid_ list is used in a barred sense**, with the single exception at R6.

**Issues** - #86's four deliverables and its scoping point; #85's resolution §7 (the three provisional answers (i)/(ii)/(iii) mapped to the same numbers, the forms block, the `nodes_without` case, the *no crossing reaches a date* row, the `MOVE` with `Q` row, S1-S7 each disposed to the right home), §8 (#87 owns S1 as stated) and §10 (the time projection assigned here by name; `look_at` of an edge stated by no record); #82's body (**flat 6,482 characters, structured 7,598**, and the 21%-in-one-course scope clause - both verbatim in its *Material* section; the four-item *must not be re-opened* list, of which **exactly two** move; the two orphans) and its closing comment (the **six** pointer debts, of which the draft accounts for all six); #84's acceptance standard, Billy's raw decomposition, and the size/absorption unfreezing; #14's evidence comment (three buckets, 6 of 6) and its body sentence on where the **judgment** lands; #16's by-hand wake; #58's *Out of scope* bullet on the plan; #71, #25, #13, #10, #88, #87, #79.

**Counts and cross-references re-derived and correct:** *seven* session rulings in ¶2; *three inputs* to #82 in §9; *two* items moved on #82's must-not-re-open list; *six* pointer debts accounted for; *two* rows of `0093`'s rejected-names table; *four* answered formalisation questions in §1 with #85's own numbering; nine judgment rows J0-J8; the row as eight items and the progress position as five, both matching their tables; `0038`'s seven minus `state` plus `id` and `kind`; band B's three dropped fields matching §4's *what band B lacked*; §10 items 1-15 all present and each referenced section existing. The fall26 standing caveat is attached where it is load-bearing (§0, §4, §11).

---

## Summary

**2 blocking, 9 repair.** The derivation itself holds up under attribution: every quotation I checked is verbatim or a fair paraphrase, and the harder discipline - citing the record that *states* the claim, and using a record only for the aspect it speaks about - is honoured in the places it usually fails, notably `0046` as delivery rather than scope, `0097` as render rather than membership, `0099` as row-versus-node, `0091` for how a dangling ref arises, and `0082`'s transfer named as a decision made at `0082` rather than as something `0038` says. Both blocking findings are in §10's sweep rather than in the reasoning: `0095` keeps a third sentence asserting the `0038`-residency transfer that §5 dissolves and §9 tells #82 is gone, and the `course.term` that `CONTEXT.md`'s `the line` and `0094`'s worked example both carry is unreconciled with the `0037` row 11 absence §4 argues from - a conflict of exactly the class §6 repairs when it finds one, and one that changes what the parked term predicate's wake has to supply, though not the *no predicate* ruling itself. The repairs are enumerative or single-citation swaps; none touches a ruling.
