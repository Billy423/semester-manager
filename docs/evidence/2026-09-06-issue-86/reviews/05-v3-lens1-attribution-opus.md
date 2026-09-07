# Review 5 - draft v3, lens 1 (attribution), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v3.md`, full repository read access, and `docs/agents/reading-records.md` as the discipline. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-4. Blind to the lens-2 reviewer.

**Report, verbatim:**

---

## Findings

### 1. BLOCKING - §5 and §10.7: the new definition of obligation's line drops `state` and adds two fields, and `0096`'s worked example is neither repaired nor listed

**The draft's claim.** §5: *"So: obligation's line is the row's field set minus `has-more`"*, where the row is *"`id · kind · name · due · done_by · optional · course · has-more`"* and `state` sits at the progress position instead. §10 item 7 lands that sentence into `0082` (both places) and `0095`.

**The records cited, and what they say.** `0082`: *"obligation's line is ring 0's **band B** field set"*. `0095`: *"`0082` calls obligation's line 'ring 0's band plus `has-more`', and band A already carries `has-more`, so *the band* is band B."* Both are listed in §10 item 7, correctly. `0038` gives band B as `course · name · due · state`.

**The record that is not listed.** `0096` renders obligation's line concretely, with no ellipsis:

> ```xml
> <edge id="138" type="builds-on" direction="pointed-by">
>   <obligation id="51" course="2c03" name="Midterm 2" due="2026-03-13" state="not_started"/>
> </edge>
> ```

Under the draft's definition that line becomes `id · kind · name · due · done_by · optional · course`: it gains `done_by` and `optional`, and loses `state`. `0096` appears nowhere in §10 - not as a repair, not as a pointer debt - and `0095`'s ruling that *"a line is **one** field set per kind and does not vary per row"* means the line either carries `state` or does not.

**The aspect mismatch, and why the draft's hedge does not close it.** §5 continues: *"how a line inside a block carries what the row carries as the progress position - `0096`'s worked example shows `state` as an attribute - is the block's render and untouched."* That sentence defers a question §10 item 7 has already answered in the other direction: the repaired text it lands on `0082` and `0095` fixes the line's field set as the row minus `has-more`, which excludes `state`. Read as deferral, §10 item 7 lands a definition the draft says it is not making; read as ruling, it contradicts `0096` at source. Ambiguous, and the threshold resolves ambiguity to BLOCKING.

**What would demote it.** Either state that obligation's line is the obligation position's fields plus `state` and repair `0096`'s example for `done_by` and `optional`, or state that the line is the row minus `has-more` and list `0096`'s example for repair. `0093`'s repairs section records that this exact class - a landed record naming an element's contents verbatim while a later ruling changes them - was repaired at source twice rather than bannered, on `0084`'s precedent.

---

### 2. BLOCKING - §2: a relation position is said to carry `role` "as `0096` renders them", and `0096` and `0093` both enumerate the edge without `role`

**The draft's claim.** §2, under a heading that says these are ruled here: *"A relation position carries the link's fields as `0096` renders them. `id`, `type`, `direction`, and `role` where the kind has one (`0017` makes `role` a Link field; `0012` gives it to `spec`)."* §8 rests on it: *"Once a relation position carries the link's fields (§2), `MOVE(spec, points-at)[role = given]?` is a selection at the relation position."*

**What `0096` actually renders.** Three fields, and it rules the fourth out by name: *"**`type`, not `role`, for the edge's kind.** `0012` gives `spec` a `role ∈ {given, owed}`, so `role` is an occupied word naming a different thing on the same record."* Its example carries `id`, `type`, `direction`.

**A second landed enumeration, also unlisted.** `0093`'s **The names** table, row `<neighbours>` · `<edge>`: *"An edge carries `id`, `type` and `direction`; `type` rather than `role`, because `0012` gives `spec` a `role ∈ {given, owed}`."* §10 item 13 lists `0093`'s *ring 0 section and two rows of its rejected-names table* - the `attention` and `status`/`state` rows of **Rejected names**. This row is in a different table and is not covered.

**The aspect mismatch.** `0096` and `0093` speak about **what the `<edge>` element renders inside a block**. The draft is deciding **what a relation position of a routing path carries**. Those are different aspects, and the sub-claims that carry the weight - `role` is a Link field (`0017`: `Link := from · to · kind · role? · locator?`) and `spec` has one (`0012`) - are sound and are cited correctly in the parenthesis. But the sentence's authority clause, *"as `0096` renders them"*, imports a render's field list into a path's type and then exceeds it, which is `reading-records.md`'s named hazard in the `0082` row of its table (a render identity read as a field-set transfer), running the other way.

**What would demote it to REPAIR.** Re-ground the field list on `0017` and `0012` under `0101`'s criterion, say in one clause that this is the path's relation position and not the `<edge>` render, and either leave `0096`/`0093` alone on that ground or list `0093`'s names row as a pointer debt. As written the draft supplies neither, and §5's *"The `about` relation position: `id`, `type`, `direction` (§2)"* shows the two lists are being used interchangeably.

---

### 3. REPAIR - §11: `0101` decides the repair-read question the draft lists as carried from it

**The draft's claim.** §11 lists among what this ticket does not decide: *"whether a repair read is a judgment the test reaches (`0071`, carried from `0101`)"*.

**What `0101` says.** *"**A repair read** - finding a dangling ref for `0018`'s owed validation pass, or the link a `detach` must name - is not a judgment the coordinator must make, and `0071` warns that a success-path derivation provably misses such methods; this test does not reach them."*

`0101` settles that the test does not reach repair reads. What it carries forward is `0071`'s **warning** that a derivation over success paths misses repair methods, which is precisely the aspect `reading-records.md`'s table assigns to `0071` (*"a **warning** about a blind spot in a derivation"*, not a conclusion about scope). The line should carry the warning, not re-open the ruling. No ruling of the draft changes, so REPAIR.

---

### 4. REPAIR - §10 item 2 under-counts the `0101` amendment its own §7 relies on

**The draft's claim.** §10 item 2: *"**`0101`, two sentences.** The criterion's *endpoint* becomes *position* (§2); a pointer to the new record for the formalisation and the type questions."*

**What `0101` contains.** Three sentences use *endpoint* in the sense §2 amends: *"the endpoint carries what decides whether it is worth the next call"*; *"Each endpoint carries its own kind's deciding fields - one set per kind (`0095`) - and no depth"*; and the criterion itself, *"a field belongs on a routing result's endpoint if and only if…"*. The draft's own §7 reads the second of those as amended - *"`0101`: 'Each endpoint carries its own kind's deciding fields - one set per kind', endpoint read as position under §2's amendment"* - while §10 amends only the criterion. The amendment item under-states the change it lands.

---

### 5. REPAIR - §3 and §8: what `given` and `owed` mean on a `spec` link is in no landed record

**The draft's claim.** J7 is *"which artifact states this obligation's requirements"*, served by `MOVE(spec, points-at)[role = given]?`, and §3 says of the parked routes *"`spec`, whose `owed` role names the deliverable"*.

**What the records say.** `0012` gives one cell: `spec` | `obligation → artifact`, `role ∈ {given, owed}`. `0082`, `0093` and `0096` each quote that enum and none glosses either value. The only gloss anywhere is #85 §7's gap table - *"the artifacts a `spec` link marks as owed"* - which is that comment's explicitly-draft section.

The reading is the natural one and I am not disputing it. But it is the draft's own reading, not a record's, and J7's chain and §8's admission of a selection at a relation position both turn on it. Mark it as the draft's reading (or cite #85 §7's row as its only prior), so a later reader does not take `role = given` as landed vocabulary. Changes a table cell and an attribution, not a ruling.

---

### 6. REPAIR - §10 does not reach `docs/adr/README.md`

`§10` items 1, 3 and 4 change a record's title-level content: a new record is added, `0042`'s *"Title and body restated as §7"*, and `0038`'s field set restated. `docs/adr/README.md` carries each record's title verbatim as its index row - `Ring 0 carries seven routing fields…`, `Active is three independent triggers…`, `Ring 0's shape is not settled…` - and CLAUDE.md calls that index the reading path. #82's own landing comment shows the index is maintained in the same pass as the records: *"The README's `0038` row said `grade_share`'s exclusion 'is measured', a ground `0038`'s own body had already retracted; fixed while both files were open."* §10 lists `CONTEXT.md` (item 12) and thirteen other targets and omits the index.

---

### 7. REPAIR - §10 item 13's pointer-debt list drops two of the six #82 recorded, without saying they are discharged

§10 item 13 invokes #82's precedent and lists `0091`, `0092`, `0093` and `0094`. #82's landing comment listed six records owed a pointer by the same reading of ring 0: *"`0013` (its cost argument rests on the roughly-55 figure, which rests on the admission clause), `0092`, `0091`, `0044`, `0093`, and `CONTEXT.md`'s `the line` entry."*

`CONTEXT.md` is item 12, so five of six are accounted for. `0044` reads clean (it says ring 0 is resident and says nothing about bands or fields). `0013` does not: *"it loses on cost against generality over a graph bounded by ring 0 at roughly **55 obligations for five courses**"*, a figure §4 keeps but re-grounds - the range is now the standing intent's, not `0042`'s admission clause. Either list it or say the debt is discharged because the figure survives; the draft's *"none contradicts it"* is asserted only over the four it names.

I checked the three verbatim quotations in item 13 and each is accurate and each is the whole of that record's exposure: `0091`'s *"Ring 0 carries the band"* is its only band sentence; `0092`'s band mentions are exactly its opening sentence, two Considered Options paragraphs and its Source line; `0093`'s are exactly its **Ring 0 gets no product-facing name** section and two rows of **Rejected names**. That part of the count is sound.

---

### 8. REPAIR - §10 item 12 does not name the `the line` clause it changes

`CONTEXT.md`'s `the line` entry reads *"obligation's is ring 0's **band B** plus the edge's `type`"*. §5 changes both halves - band B dissolves (§7), and `0096` had already moved `type` onto the `<edge>`. Item 12 lists `the line` as gaining *"`progress`'s line as a path position and the row-versus-line distinction"* and does not name the obligation clause that has to be rewritten. Same defect class as finding 1 and a repair of the same sentence.

---

### 9. REPAIR - §3: S2's first route is not J4's chain

**The draft's claim.** *"S2 is caller-agnostic and reduces to J4's chain."*

**What #85 §7 says.** S2 is given two structural readings: *"`START(ref B) · MOVE(builds-on)`, or `· MOVE(requires) · MOVE(requires, pointed-by)` to reach A through a shared concept"*. Only the second is J4's chain. The `builds-on` route is a one-crossing chain over a link kind no ruled source names a judgment over, which is a disposition the draft makes elsewhere for `spec` and `prepares-for` but not here. *Caller-agnostic* is quoted correctly (#85: *"Routing is caller-agnostic"*). The disposition is right in substance and incomplete as written.

---

### 10. REPAIR - §5: two verdict cells lead with a ground `0099` declines

The `grade_share` cell reads *"no reader by standing exemption"* and the `added_at` cell reads *"no reader; `0099`'s ground…"*. `0099` rules the opposite lead: *"**`added_at` does not render, and this is a ruling rather than a derivation.** Not on the ground that nothing reads it - `grade_share` has no reader by standing exemption and is in the schema."* Both cells then give the correct ground (`0099`'s row-versus-node line for `added_at`, J0's actual inputs for `grade_share`), and residency is a different question from readability (`0038`, `0095`), so no verdict moves. The lead phrase is the one `0099` exists to refuse, and it should not be the first thing in the cell.

---

### 11. REPAIR - §5's provenance sentence does not cover `name` and `due`

*"The field lists were assembled from this repository's records - `obligation`'s from `0027` (`kind`), `0028` (`added_at`), `0029` (`course`), `0032`, `0033`, `0037`, `0038` (`optional`, `done_by`)…"* `name` and `due` appear in the table and in no attribution; both are in `0038`'s seven and both have `CONTEXT.md` entries. One clause fixes it. The sentence's honest headline - *"because no landed record carries a field table"* - is correct and checks out against `0082`'s Source line.

---

### 12. REPAIR - glossary: *note* used bare

§6: *"so as a note the observation is the dispatch branch"*. `CONTEXT.md`'s `sticky_note` entry lists *note* (bare) under _Avoid_, and the `annotation` entry bars *note* used for both kinds. Say *as a `sticky_note`*.

---

## Citations checked and found sound

Records, by the aspect the draft uses them for.

- `0101` - the test's informal wording (verbatim); *"admits by what a form lets a chain produce"*; *"a routing result's endpoint"*; *"a judgment across obligations is a judgment about their relations"*; *"Affordability is a separate question the type does not answer … `0039`'s affordability is per-member depth"* (both fragments present, ellipsis honest); *"Each endpoint carries its own kind's deciding fields - one set per kind"*; the vocabulary containing no set operations; the width gate unruled; the cost statements for #88; the unprompted-coordinator clause; ring 0 as one routing result held resident; the refusal of an intent the system cannot serve; dispatch calls against the effectiveness constraint left undecided; `0084`'s composition as resolve entering through fetch.
- `0042` - *"it is present, it is routable"*; the three triggers and `state == in_progress`; the importance sentence; breadth never a defect; the uniform-depth defence. §7's re-reading of the record as a per-row field-set partition is consistent with `0038`'s *"band B drops the last three"* and with `0100`'s own doubt, quoted correctly.
- `0038` - the seven fields; `parts` out for *what is this about*; the roughly-55 figure with its scope clause excluding the obligation-dense course; residency not readability. The draft's row is `0038`'s seven with `state` re-typed plus `id` and `kind`, and the arithmetic is right.
- `0100` - the admission placement and *"which rows enter"*; *"a line, whose field set is band B, which is the selection clause"*; *"`0042` does not itself say that ring 0 ranges over every obligation in a semester"*; the derivation-direction diagnosis; the refusal to widen ring 0.
- `0082` - `id` and `kind` as attributes because they address; `locator` *"says where you land after walking, which does not bear on whether to walk"*; a `Ref`-typed field as a bare pointer; the defaulted `progress` carrying no `id`; `has-more` in no field table (the second exception); the transfer clause appearing in two places, which it does.
- `0095` - *"so the band is band B"*; *no rule generates a new kind's line*; one field set per kind; a line carrying no content.
- `0096` - `has-more` surviving only where the neighbourhood cannot be listed; `has-more` ruled off the line; the `<edge>` carrying `id`, `type`, `direction`; the worked example showing `state` as an attribute (accurate as a quotation - see finding 1 for the attribution).
- `0092` - the value ruling; the field's place travelling with ring 0's render.
- `0099` - *"a January answer is indistinguishable from today's"*; the row-versus-node dividing line for `added_at`.
- `0091` - *"a coordinator can therefore name a course row it never read"*, used for how a dangling `course` ref is produced.
- `0089` - a whole line per changed obligation; the ground and return shape left untouched.
- `0035` - *"one current value per target"* (flagged as *read here as* one record per target, honestly); *"`state` sits on `progress` and not as a field of `obligation`"*; absence reading as `not_started`.
- `0036`, `0028` - in-place modification and per-field update, supporting the one-record reading.
- `0037` - row 1 verbatim on both halves (*"observed rather than stored - ordinally, from `parts` and item notes first…"* and *"ordinal comparisons, not hour counts"*); rows 13 and 14 do leave term boundaries open; the no-re-add rule.
- `0033` - *"does not carry size"* and the replacement being *an interaction*. The §6 conflict between `0037` row 1 and `0033` is real, is stated as a conflict rather than resolved silently, and the repair proposed keeps the ordinal ruling.
- `0039` - symmetry scoped to the set the judgment ranges over; the observe/dispatch formalism, paraphrased in the record's own box terms (*every member of S*).
- `0046` - the own-channel sentence verbatim, and `reading-records.md`'s delivery-versus-scope correction applied in the right direction. §4's use of it is the cleanest aspect handling in the draft.
- `0018` - the dangling ref, the non-cascade on a course delete, the owed link-set validation pass.
- `0029` - `obligation.course` mandatory and monomorphic.
- `0026` - `course.id` as the supplied code, non-uniform id space.
- `0027`, `0032` - `kind` as discriminator; `grade_share_conditional` as a marker.
- `0012` - `about : annotation → any`; two `requires` signatures; `spec` and `prepares-for` as the two further obligation-artifact kinds (count correct); `role ∈ {given, owed}` (the enum only - see finding 5).
- `0017` - `role` as a `Link` field.
- `0097` - a member omits what its container fixes; the `id` as the addressability marker.
- `0041` - the order clause verbatim; nulls last for undated obligations; the grouping struck and open.
- `0040` - the method, not the ground, which is the distinction `0100` itself draws.
- `0043`, `0021`, `0005`, `0007`, `0068`, `0070`, `0081`, `0084`, `0102`, `0003`, `0010`, `0051`, `0056`, `0019` - each used for the aspect it speaks about; `0102`'s membership row does leave the Ref crossing's admission to #86, `0070` does bound the map at capabilities, `0081`'s silence rule is the negative-answer aspect and not a residency claim, and `0019`'s quoted clause is verbatim.
- `0001` - the requirements sentence verbatim; jobs two and three used as `0001` restates them, not as the retired three-parallel-premises reading.

Issues.

- #86's body - the four deliverables and the three formalisation questions, answered in the body's own order.
- #85 - §7's provisional (i) confirmed and (iii) replaced, both quoted accurately; the `nodes_without` / `covered` case named as the first concrete instance; the field-comparison row's ground *no crossing reaches a date*; `MOVE` with `Q`; S1, S3, S4, S5, S6, S7 dispositions (S2 excepted, finding 9).
- #84 - the acceptance standard verbatim; the raw-decomposition items; `mastery` and `concept`'s retracted definition as deferred and unfrozen; the *Destination* placement of the grammar.
- #82 - the refusal to widen ring 0; the overturn permission. The draft says *"the `0042` overturn #82 authorised"*, which is right: `0042`, `0100`, `CONTEXT.md` and #84 all record #82 as the authorising ruling, while #85 §8 and #86's own body say *#84 authorised*. The draft follows the records over the two issue comments and is correct to; a one-clause note would make that deliberate rather than silent.
- #14 - the three buckets and *6 of 6* verbatim, marked as evidence and not a ruling and carrying the fall26 caveat; the *"the plan is where that judgment gets written down, or nowhere"* sentence verbatim, and the input-versus-judgment distinction drawn on it holds.
- #58 - the *Out of scope* line on the plan exists and reads as §0 says; #84 records the same recommended reading.
- #16, #25, #10, #13, #71, #87, #88, #79, #17/#19/#20 - each wake and each disposition matches the issue. #16's wake is the by-hand observation of the first real semester decision; #25's is a writer for `concept`; #71 holds `state`'s residence; `0101` assigns #16's first membership test back to #16 and the draft does not claim it.

Numbers and counts, all re-derived: seven session rulings in paragraph two (seven are listed); two reshapings in paragraph three (two are described); `0038`'s seven; the row's eight items reconciling to seven minus `state` plus `id` and `kind`; three triggers; three buckets and 6 of 6; roughly 55 and fifty-five members; `0100`'s four clauses; `0012`'s two further obligation-artifact link kinds; `0037` rows 1, 13, 14; three structural readings of *needing Billy*; three inputs to #82's arrangement; three readings added to #16's wake; `0093`'s two rejected-name rows. The two fall26 figures - roughly 55 and 6 of 6 - are flagged at §0, §4 and the closing standing note, which is what `drafts-and-rulings.md` requires.

Glossary check: no _Avoid_ term is used in an avoided sense except finding 12. *edge* appears only as the surface element `<edge>`, which `CONTEXT.md`'s `link` entry sanctions; *row* is used for a ring 0 row and never for a line, and §5 draws the distinction explicitly; *projection* appears only for the time projection and inside quotations; *view*, *search*, *retrieval*, *status*, *metadata*, *entity* do not appear.

## Summary

Two blocking findings and ten repairs. Both blocking findings are the same shape and both sit at the seam between a render and a routing path: §5's redefinition of obligation's line changes three fields against `0096`'s landed worked example without listing it in §10, and §2's relation position takes its field list from how `0096` renders an `<edge>` and then adds `role`, which `0096` and `0093` both exclude by name. The ten repairs are attributions, amendment scopes and one glossary slip; none of them moves a ruling, and the largest are §10's coverage gaps - `docs/adr/README.md`, `0013`'s pointer debt, `0101`'s second and third *endpoint* sentences, and the `the line` clause in `CONTEXT.md`. The draft's handling of `0046`, `0100`, `0038` and `0042` is unusually careful about aspect, and its two hardest attributions - the delivery-versus-scope reading of `0046` and the #82-not-#84 authorisation - are both correct against the records.
