# Review 15 - draft v8, lens 1 (attribution), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v8.md`, full repository read access, and `docs/agents/reading-records.md` as the discipline. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-14. Blind to the lens-2 reviewer. Told that §5b is a draft section and that findings against it are repair.

**Report, verbatim:**

---

## Method

I read `reading-records.md`, `drafts-and-rulings.md`, `CONTEXT.md` and `docs/adr/README.md` first, then the draft, then every record the draft cites, opened individually rather than from the index. For each citation I checked the aspect separately from the quotation, per `reading-records.md`'s table. I then swept `docs/adr/`, `docs/adr/README.md` and `CONTEXT.md` for every mention of the bands (`grep -rn "band"`), of ring 0 (`grep -rln "ring 0"`), of `has-more`, of `endpoint`/`position`, of `state`'s home, and of `term`/`offering_term`, and checked each hit against §10's amendment list. I checked the draft against `CONTEXT.md`'s _Avoid_ lists by grep. I re-derived every count and cross-reference in §10, §9 and §5, and counted `0101`'s `endpoint` occurrences by hand.

**Verdict: no blocking findings. Eight repairs.** The attributions are the strongest part of this draft. Where it cites a record for an aspect, it has in almost every case said which aspect and, where it is reading rather than quoting, said so. The eight repairs below are counts, one omitted amendment locus, one omitted pointer debt, and two attributions that overstate what their record says without changing the verdict they support.

---

## Findings, most severe first

### R1 - REPAIR. §10 item 2: "`0101`, six places" matches no enumeration, and one locus that needs amending is not listed

**Section:** §10 item 2.
**Claim:** "**`0101`, six places.** *Endpoint* becomes *position* wherever it is used in §2's sense: the output paragraph's second sentence…; the definition paragraph's *"each ending at an address"*…; *"Each endpoint carries its own kind's deciding fields"*; *"every endpoint at one depth"*; and the criterion itself."
**Cited record:** `0101`.

**What the record actually contains.** `0101` uses `endpoint` in §2's sense nine times, across five locations: the section heading `## Output: paths, not endpoints`; the output paragraph's *"the endpoint carries what decides whether it is worth the next call"*, *"a set of endpoints has no position for a relation"* and *"Obligations sharing a concept, as endpoints"*; *"Each endpoint carries its own kind's deciding fields"* and *"every endpoint at one depth"*; the formalisation paragraph's *"whether two chains produce **the same set** when endpoints agree and paths differ"*; and the criterion's own two, *"**The criterion on an endpoint**"* and *"a field belongs on a routing result's endpoint"*.

The item's colon-list names **five** loci, not six. Counting all edits the item then describes - the five, plus the split of the *non-endpoint position* sentence, plus dropping the `0095` citation, plus the pointer - gives **eight**. Six matches neither.

**The substantive half.** `0101`'s last paragraph reads: *"What the standing intent is, which fields its rows carry, and **how they are banded** and arranged are downstream: `0100`'s four clauses are re-derived from this record at #86…"*. §7 dissolves the banding. That clause is not named anywhere in item 2, and it is not covered by item 2's closing *"Plus a pointer to the new record for the formalisation and the type questions"* - banding is neither. `CONTEXT.md`'s parallel wording is covered, by item 13's *"its `derivation owed` note replaced"*; `0101`'s is not.

**Aspect mismatch:** none. This is a count and a completeness gap in an amendment list.

**Why not blocking:** `0101` is listed in §10, so threshold (c) does not fire; the *banded* clause states that banding is downstream, which the answer *no bands* satisfies rather than contradicts.

**Verdict: REPAIR.** Fix the count, add the *banded* clause, and decide explicitly whether the heading and the formalisation paragraph's *"when endpoints agree"* are edited or deliberately left (the two output-paragraph uses that argue *against* endpoints-as-output are plainly meant to stay, and saying so would make the list auditable).

---

### R2 - REPAIR. §4 and §7 undercount what the progress position adds to a row

**Section:** §4 (*Width*) and §7.
**Claim (§4):** "under this record every row grows by what band B lacked - `done_by`, `optional`, `has-more` - and by the progress position's `origin` and `updated_at`".
**Claim (§7):** "three fields on the rows the partition would have thinned, **plus the progress position's two**".
**Cited record:** `0038`, against §5's own table.

**What the draft's own §5 says.** "**The row is `id · name · due · done_by · optional · course · has-more` at the obligation position, and `id · state · origin · updated_at` at the progress position.**" `0038`'s seven are `course · name · due · state · optional · done_by · has-more`. Relative to `0038`, the progress position contributes `state` (already in `0038`), plus `origin`, `updated_at` **and the progress `id`** - which `0038` does not carry in either band and which §5's table rules explicitly in ("addresses when the record exists, so the next call on the progress record is formed from it"). That is three new items, not two.

**Aspect mismatch:** none; an arithmetic slip against the draft's own table.

**Verdict: REPAIR.** The ruling is untouched - §4 states the 6,482/7,598 figure as "a floor and not the bet's number", and undercounting the growth only makes the floor safer - but the two sentences should say three, or say why the progress `id` is not counted.

---

### R3 - REPAIR. §10 item 14 omits `0096`'s "only where the neighbourhood cannot be listed", which §5's own collapse finding now qualifies

**Section:** §10 item 14, against §5's `has-more` cell.
**Claim:** the pointer debts are `0091`, `0092`, `0093`, `0094`'s closing sentence, `0102` and `0013`, and "each describe the state this record amends and **none contradicts it**".
**Cited record:** `0096`.

**What the record actually says.** "**So `has-more` has no place in a node's render at all.** Its own ground in `0092` is that *"ring 0 cannot list a node's neighbourhood, so without this field the coordinator's next call is a gamble"*, and that ground holds **only** where the neighbourhood cannot be listed. That is ring 0…"

Under §4's standing intent a ring 0 row now carries one crossing of the neighbourhood - the `about` crossing to `progress`. §5 names the consequence itself ("that a row whose progress position is non-empty then states `about` twice is a render collapse") and §9 tells #82 about it. But `0096` is touched in §10 only at item 7, for the line debt, which ends "`0096`'s worked example is untouched" - so a reader of §10 alone is not told that `0096`'s *only where the neighbourhood cannot be listed* sentence is now the sentence whose bite §5 records.

**Aspect mismatch:** none. `0096`'s clause is not contradicted - ring 0 still cannot list the neighbourhood, only one selected crossing of it - so this is an omission from the debt list, not a contradiction.

**Verdict: REPAIR.** Add `0096`'s clause to item 14 (or to item 7), naming §5's collapse as what qualifies it.

---

### R4 - REPAIR. §4's "`0035`… bars copying it onto the obligation" overstates the record, which #71 records as an argument

**Section:** §4, *Why it reaches `progress`*.
**Claim:** "`state` is a field of `progress`, not of `obligation`, by `0035`, which is also **the record that bars copying it onto the obligation**: *"`state` sits on `progress` and not as a field of `obligation`"*."
**Cited record:** `0035`.

**What the record actually says.** The quoted string is `0035`'s section **heading**, whose full text is "**Why `state` sits on `progress` and not as a field of `obligation`.**" The section gives two reasons - `state` and `detail` on one record "*on purpose, because 'two records would be free to drift apart, and one cannot'*", and that `state` "*separates `progress` from `sticky_note`*", so "*moving the field is closer to deleting a kind than to relocating one*". #71's body characterises this precisely: "**`0035` argues against the configuration directly**." *Argues against*, not *bars* - and #71 is open, which the draft's very next sentence acknowledges.

**Aspect mismatch:** `0035` speaks about **where the field lives in the schema**. The load-bearing half of the draft's claim - that `state` is `progress`'s field, so a chain from `obligation` must cross to reach it - is exactly that aspect and is fully supported. Only the subordinate *bars* is stronger than the record and than #71's own reading of it. (Note that `0038` already carried `state` on ring 0's row without a crossing, so `0035` cannot by itself bar a *projected* `state`; the draft does not claim it does.)

**Verdict: REPAIR.** *Argues against*, or *is the record #71 weighs against the move*, and drop the heading's use as a quoted sentence (it begins *Why*).

---

### R5 - REPAIR. §5's `grade_share` cell uses the clause `0099` declines, two cells above where it cites `0099` for declining it

**Section:** §5, obligation position, `grade_share` row.
**Claim:** "What closes it is a ruling: `grade_share` *"has no reader by standing exemption"* (`0042`, kept at §7), and a resident row would supply it one."
**Cited records:** `0042`, `0038`.

**What the records actually say.** `0042`: "**The system holds no notion of an obligation's importance** - `grade_share` has no reader by standing exemption - so a rule promoting 'important' undated rows would assert a judgment the system is ruled not to make." The quotation is exact. But `0099` uses the identical clause to *refuse* it as a ground for keeping a field out of a read: "Not on the ground that nothing reads it - **`grade_share` has no reader by standing exemption and is in the schema.**" The draft cites `0099` for exactly that move two cells later, in the `added_at` row: "*no reader* is the ground `0099` declines."

**Aspect mismatch:** `0042`'s clause is a premise inside an argument about **importance-based promotion**, not a selection rule about residency. The draft's bridge - "a resident row would supply it one" - is the draft's own inference and is not in `0042`; a standing exemption from the rigidity rule is not violated by a field acquiring a reader.

**Why not blocking:** the cell's verdict (*out*) is over-determined - the cell keeps `0038`'s independent corpus argument ("a column of shares reads as a partition it is not"), which is the residency-selection record's own ground for excluding `grade_share`, and §10 item 4 preserves it. The ruling does not move.

**Verdict: REPAIR.** Lead the cell with `0038`'s corpus argument as what closes it, and demote the `0042` clause to what it is - the record that bars a promotion rule, kept at §7 - or say in one clause why the *no reader* ground works here where `0099` declined it.

---

### R6 - REPAIR. §5's provenance sentence for the field lists does not cover `id` or `progress.kind`, which both tables carry

**Section:** §5, the paragraph introducing the two tables.
**Claim:** "The field lists were assembled from this repository's records - `obligation`'s from `0027` (`kind`), `0028` (`added_at`), `0029` (`course`), `0031`, `0032`, `0033`, `0037`, `0038` (`name`, `due`, `optional`, `done_by`) and `CONTEXT.md`'s `name` and `due` entries, and `progress`'s from `0028`, `0035`, `0036` and `CONTEXT.md`'s `origin` entry… **A field named in none of them would be invisible to the derivation.**"

**What is missing.** Both tables carry an `id` row and a `kind` row. Neither list names a source for `id` - that is `0025` ("one id space shared by every kind that can be a link endpoint") and `CONTEXT.md`'s `node` entry ("A record with a `kind`, an id in the single id space, and that kind's declared field set"). The `progress` list names no source for `kind` at all; `0027` is named only for `obligation`. `0036` is cited for `progress` but its field block is `sticky_note`'s (`kind · id · category · body · origin · created_at · updated_at`), which supplies `origin` and the timestamps across both annotation kinds but is not `progress`'s table.

**Aspect mismatch:** none. The paragraph's own standard - a field named in none of the sources is invisible - is what makes the gap worth fixing: as written, `id` and `progress.kind` were derived from sources the paragraph does not name.

**Verdict: REPAIR.** Add `0025` / `CONTEXT.md`'s `node` entry for `id`, and `0027` for `kind` at both positions.

---

### R7 - REPAIR. §1 (iii) calls `or` "a form" in the same breath as two forms the record admits, without marking the grain/admission distinction

**Section:** §1 (iii).
**Claim:** "`or` **is a form**: without it, `FILTER(P or Q)` is `START · FILTER(P) ∪ START · FILTER(Q)`, a union, which the vocabulary does not contain and which is two returns. `not` and `exists` are each a form…"

**Why it needs a word.** (iii) answers *at what grain a form is counted*, so "`or` is a form" there means *`or` is one form and not a spelling of another*. But `not` and `exists` in the very next sentence are forms the record **admits** (§9's #88 bullet lists them), while `or` is **parked** (§8: "`or` has no must-judgment after §7… Parked; wake: a must-judgment from a ruled source that ranges over a union"). `0101`'s test is a biconditional over must-judgments, so *being a form* and *belonging in the domain* are two questions; §1 (iii) is answering only the first and does not say so at the point where it lists three forms of which one is later parked.

**Cited record:** `0101` - "The test admits by what a form lets a chain produce, so two spellings that produce the same thing are one form to it". The draft's use is faithful; the risk is a reader taking §1 (iii) as an admission list.

**Verdict: REPAIR.** One clause: *(iii) counts forms; whether each is admitted is §8's.*

---

### R8 - REPAIR (against §5b, per standing). §5b's relation-position bullet is sound on its records but the section is not reachable from §10

**Section:** §5b, first bullet.
**Claim:** "A link's fields, besides its endpoints, are `kind`, `role` where the kind has one, and `locator` (`0017`), plus the `id` `0096` gave the edge for `attach` and `detach` to name."
**Cited records:** `0017` - "`Link := from: Ref · to: Ref · kind: LinkKind · role?: string · locator?: string`" ✓. `0096` - "**The edge carries an `id`.** … Without it `attach` and `detach` have nothing to name." ✓. `0082` - "`locator` is not on either: it says where you land after walking, which does not bear on whether to walk." ✓. `0093` - "An edge carries `id`, `type` and `direction`" ✓.

Every citation in this bullet checks out. The repair is narrower: §5b says it "is kept because the row's derivation is not auditable without it", and §10 item 1 says "§5b is not carried into it", but §10 carries no instruction for where §5b goes - §9's #88 bullet says only "§5b is input to it and to the grammar". A reader of the landed record and its amendments would have no path to §5b at all. Add it to item 15's issue comments (a #88 comment naming the evidence file) so the row's derivation stays auditable.

**Verdict: REPAIR** (against §5b, therefore repair by standing regardless).

---

## Citations checked and found sound

Every one of these I opened and read against the aspect the draft uses it for.

**`0101`** - the test's wording *"admits by what a form lets a chain produce"* (§1); the paths ground *"a judgment across obligations is a judgment about their relations"* (§1 ii); the criterion stated on *"a routing result's endpoint"* and *"What a non-endpoint position carries… is the grammar's"* (§2); *"Each endpoint carries its own kind's deciding fields - one set per kind"* (§7); *"Affordability is a separate question the type does not answer … `0039`'s affordability is per-member depth"* (§6); "a judgment is made *with* operations and is never an element of an operation set" (§4); "an intent the system cannot yet serve is refused, never returned empty" (§3, §4); "The vocabulary contains no set operations" (§4); the unprompted-coordinator clause (§4); the in-band `has-more` clause in the spontaneity paragraph (§5); "no landed record bounds a result's width" (§4); "resolve entering through fetch" (§8); Ref-typed fields crossable in the vocabulary (§8); the edge-`id`/id-space open question (§5b, §11); the time projection's residency left undecided (§4); the repair read placed outside the test's reach with `0071`'s warning (§4, §11).

**`0100`** - `0042` placed as **admission**, *which rows enter* (§4); the refresh clause *"a line, whose field set is band B, which is the selection clause"* (§4, §10.5); the doubt *"`0042` does not itself say that ring 0 ranges over every obligation in a semester"* (§4); `0038` not derived, run bottom-up (§5); `0041` and `CONTEXT.md`'s `reload` never read together, `0040`'s **method** only (§9).

**`0042`** - *"it is present, it is routable"* of an undated obligation (§3, §7); the uniform-depth defence "computed from material facts plus one rule applied identically" (§7); breadth never a defect (§7); the importance sentence and its `grade_share` clause (§6, §7); overturnable, ruled at #82 (§6, opening) - and the draft is **right** to say #82 where #86's own unblocking comment loosely says #84: `0042`, `0100`, #82's comment and #84's body all record the permission as ruled at #82.

**`0038`** - the seven fields and band B dropping the last three (§5, §7); `parts` out because it answers *what is this about* (§5); the corpus argument and its non-derivation standing (§5); roughly 55 obligations with the scope clause excluding the obligation-dense course (§4).

**`0039`** - symmetry scoped to the set the judgment ranges over (§2); the observe-or-dispatch formalism over set S (§6); its per-member affordability (§6).

**`0035`** - `state` non-nullable, absence reads `not_started` (§4, §5); *"one current value per target"* (§4, correctly flagged as a **reading** and parked at §11); `detail` beside `state` so the two cannot drift (§5).

**`0018`** - a ref may dangle, deleting a course does not cascade to its obligations, the link-set validation pass *"owed and unbuilt"*, `Ref := (kind, id)` (§4, §5, §10.12).

**`0029`** - `obligation.course` mandatory, single-valued, monomorphic (§4). **`0026`** - `course.id` supplied by the material (§4, §5, §8). **`0091`** - *"A coordinator can therefore name a course row it never read"*, and "Ring 0 carries the band" as the pointer debt (§4, §10.14).

**`0012`** - `about : annotation → any` (§2, §6); `requires` with both signatures (§3 J2, J4); `spec` with `role ∈ {given, owed}` (§3 J7); `builds-on : obligation → obligation` (§3 J8). And the draft's claim that **no landed record glosses `given` or `owed`** is correct - I grepped `docs/adr/` and `CONTEXT.md`; the four hits are the signature itself and three re-statements of it.

**`0017`** - the natural key and the link's field list (§5b, §8). **`0028`** - per-field CRUD/partial update, null renders as absence, timestamps (§4, §5). **`0031`** - nullable bool means unknown (§4, §5). **`0032`** - the pointer optional, "the narrowing must not be smoothed" (§5). **`0033`** - `parts` does not carry size, the replacement is *an interaction* (§5, §6). **`0027`** - `kind` a required discriminator (§5). **`0036`** - in-place modification, `origin` confers no immutability (§4, §6).

**`0037`** - row 1's *"observed rather than stored - ordinally, from `parts` and item notes first, then by asking for a relative comparison"* and *"ordinal comparisons, not hour counts"* (§6); row 11's deferral of `course.offering_term` (§4, §11); rows 13 and 14 leaving term boundaries open (§4, §11); the no-re-add rule (§6). The **conflict §6 reports is real**: `0037` row 1 names `parts` as a first source of ordinal size, while `0033` and `CONTEXT.md`'s `parts` entry both bar it. So is the **term conflict §4 reports**: `CONTEXT.md`'s `the line` gives course's line as `id name term`, `0094`'s worked example prints `term="winter-2026"`, and `0037` row 11 defers `course.offering_term` to v2. Both are correctly reported rather than silently resolved.

**`0082`** - a `Ref`-typed field is a bare pointer answering *which one is this* (§4, §5); `has-more` and `role` as the second exception, from no field table (§5); "A defaulted `progress` carries no `id`, and that absence is the signal" (§4, §5); `locator` says where you land, not whether to walk (§5b, §8); the transfer clause in **both** the places it appears (§10.7 - verified, there are exactly two); the Source line pointing at the fall26 schema for the field tables (§5).

**`0095`** - the three band sentences named in §10.7 all exist and are exactly three; *"no rule generates a new kind's line"*; *"every endpoint is one line"*; the criterion is one ruling per kind (§5, §10.7). **`0096`** - the worked example prints a neighbour with `state` as an attribute; the edge's `id` for `attach`/`detach`; `id`/`type`/`direction` (§5, §5b). **`0097`** - a tag with an `id` is addressable; a line is self-closing; a member omits what its container fixes (§4, §6). **`0099`** - *no reader* declined as a ground; the `updated_at` harm *"a January answer is indistinguishable from today's"*; the pair kept on a joint ground (§5).

**`0046`** - "A read that returns a node's neighbourhood must deliver `sticky_note` and `progress` through their own channel, never as ordinary neighbours." §4's handling is the **most careful passage in the draft**: it names the delivery-versus-scope distinction, cites `reading-records.md`'s own table for it, and amends the record rather than reading around it (§10.10). `0092`'s Considered Options independently confirms the reading ("`0046` is a **delivery** rule … and it does not bar signalling that one exists").

**`0092`** - the value ruling (set of link kinds, not a boolean, not a count) and the three band loci named in §10.14 (opening sentence, Considered Options, Source line) all verified. **`0093`** - the ring 0 section's "band A and band B are ordinary words", the two rejected-names rows (`attention` for the band, `status`/`state` for the band) and the names row on the edge - exactly as §10.14 says. **`0094`** - the closing sentence carrying "the band's representation"; the `term="winter-2026"` example. **`0089`** - the title plus four sentences calling ring 0's unit a line: verified by count.

**`0019`** - *"residency is an access policy over obligation nodes' fields"* (§10.11). **`0013`** - the roughly-55 cost argument with `0038`'s scope clause (§10.14). **`0021`** - query-by-time-period a separate projection, coarse grouping deliberately unmodelled (§3, §4). **`0043`**, **`0044`** (reads clean, as claimed), **`0051`**, **`0056`** (*"provenance is stated prominently at every read"*, `origin`'s write rule owed), **`0010`** (owner-authored; *structural, never personal*; the stateless opening), **`0003`**, **`0001`** (the three jobs as rewritten at #85, including *"helping model an assignment's requirements is in scope"*), **`0007`**, **`0024`**, **`0060`**, **`0068`**, **`0070`** (*capabilities not shapes*), **`0071`**, **`0081`**, **`0084`**, **`0102`** (the membership row leaving the Ref crossing's admission to #86) - all check out for the aspects used.

**`CONTEXT.md`** - the opening sentence and its three clauses mapped to J1/J2/J3; `covers` as the teaching relation; `applies` on a resolve's path; `dispatch` covering asking the owner; `the line`'s field sets and its *a ring 0 row is not a line*; `path`'s "ending at an address" (correctly listed for amendment at §10.13); `id`, `handle`, `holder`, `faithfulness`, `parts`, `progress`, `reload`.

**Issues** - #86's body and unblocking comment (the four deliverables and the scoping point); #85's resolution §7 (`START(ref)` as a spelling, the three provisional answers, the forms block, the gap table, S1-S7), §8 (#86's assignment of the two type questions; S1 as #87's whole), §10 (what `look_at` of an edge returns stated nowhere; the time projection's residency); #84's *Destination* and its acceptance standard *"exposes every necessary operation … never a workflow per imagined scenario"*, and its record that `mastery` and `concept`'s retracted definition "were deferred rather than overlooked"; #82's body (the 6,482/7,598 measurement with its 21%/2px3 scope clause; the four-item *must not be re-opened* list; the two orphans) and its comment (the six pointer debts - `0013`, `0092`, `0091`, `0044`, `0093`, `CONTEXT.md`'s `the line` - which the draft's "of the six #82 listed" accounting matches exactly); #14's evidence comment (three buckets, 6 of 6, "It bounds acceptance item 1 without answering it") and its size-judgment sentence; #16's wake; #58's *Out of scope* line on the plan and its "Deferred at #20, #19, #17" line, which supports §3's placement of the artifact layer; #13; #71; #25's wake; #10; #17/#19/#20 titles.

**_Avoid_ check (CONTEXT.md).** Clean. I grepped for `edge`, `entity`, *the projection*, *the corpus*, *the graph*, `search`, `retrieval`, `navigation`, *materialized view*, *node type*, `label`, *foreign key*, `delegate`, `spawn`, *context switch*, *catching up*, *transitive closure*, *master session*, `orchestrator`, *resident projection*. Every `edge` hit is the `<edge>` surface element or `0096`'s edge, which `CONTEXT.md`'s `link` entry itself licenses. `row` is used throughout for ring 0's unit, which is the glossary's own word under `ring 0` ("A ring 0 row is not a line") - the `_Avoid_: row` under `the line` bars calling a **line** a row, and the draft's §5 makes that distinction its own subheading. "Asking Billy" is explicitly named as one case of dispatch, per the `dispatch` entry.

**Counts re-derived and correct.** §10's "six" pointer debts (six listed, and the "of the six #82 listed" reconciliation is exact); `0095`'s "three band sentences"; `0089`'s "title and four sentences"; `0092`'s three loci; `0093`'s "two rows of its rejected-names table"; `0082`'s transfer clause "in both places it appears"; `0100`'s "four places"; §9's "#16's wake gains five readings" (five, covering §4's two stated wakes as one reading); §5's row statement against both tables; "`0038`'s seven with `state` re-typed … plus the handle"; §3's nine judgments J0-J8 and the S1-S7 disposition; §1's (i)-(iv) labels against `0101`'s and #85 §4's (i)-(iii).

---

## Summary

**Zero blocking, eight repair.** No cited record fails to support the ruling it is cited for in §0-§8, and no landed record contradicts a ruling that §10 does not already carry for repair or as a pointer debt - I swept `docs/adr/`, the README and `CONTEXT.md` for the bands, ring 0, `has-more`, `state`'s home, path endpoints, edges and `term`, and every hit is either amended (items 2-13), listed as a pointer debt (item 14), or unaffected. The eight repairs are: a count and one omitted locus in §10's `0101` amendment (R1); a two-versus-three undercount of the progress position's cost in §4 and §7 (R2); `0096`'s *only where the neighbourhood cannot be listed* missing from the pointer-debt list (R3); *bars* overstating `0035` where #71 records it as an argument (R4); the `grade_share` cell resting on the clause `0099` declines, though its verdict is carried independently by `0038` (R5); `id` and `progress.kind` not covered by §5's own provenance sentence (R6); §1 (iii) listing `or` beside two admitted forms without marking grain from admission (R7); and §5b unreachable from §10's amendments (R8, repair by standing). Two of these - R4 and R5 - are the classic aspect slip `reading-records.md` names, and in both the draft's own verdict survives on a second, correctly-cited ground, which is why neither reaches blocking.
