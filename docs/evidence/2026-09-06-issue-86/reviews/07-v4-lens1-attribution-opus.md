# Review 7 - draft v4, lens 1 (attribution), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v4.md`, full repository read access, and `docs/agents/reading-records.md` as the discipline. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-6. Blind to the lens-2 reviewer.

**Report, verbatim:**

---

## Findings, most severe first

### 1. BLOCKING - §2's *a path may end at an empty position* contradicts `0101`'s *ending at an address*, and §10 item 2 repairs the wrong half of the sentence

**Section.** §2, *A crossing may be optional*.

**Claim.** "A path may therefore end at an empty position; every non-empty node position is addressable, and which one the coordinator spends its next call on is its judgment." This is a ruling: it is the type consequence of the optional crossing, and §4's standing intent depends on it (an obligation with no `progress` record "keeps its path with the progress position empty").

**Cited record.** `0101`, as amended by §10 item 2.

**What the record actually says.** `0101`, *Output: paths, not endpoints*:

> **Routing returns a set of paths.** A path is the chain a member arrived by - node, relation, node, … - **ending at an address**, and the endpoint carries what decides whether it is worth the next call.

and, two paragraphs on:

> **Not bare ids** … Each endpoint carries its own kind's deciding fields - one set per kind (`0095`) - and no depth.

An empty position is not an address: the draft says so itself two clauses later ("every **non-empty** node position is addressable"), and §5 has the empty progress position carrying no `id` at all (`0082`). So under this draft some paths end at something `0101` says a path never ends at.

**What §10 lists.** Item 2: "**`0101`, four sentences.** *Endpoint* becomes *position* in the three sentences that use it in §2's sense - the path's endpoint carrying what decides the next call, each endpoint carrying its kind's deciding fields, and the criterion itself; a pointer to the new record." Applying that edit to the sentence above yields *"…ending at an address, and the **position** carries what decides whether it is worth the next call."* The `endpoint → position` substitution is orthogonal to the contradiction; **`ending at an address` survives the amendment intact**, and after §10 is applied a landed record still says a path ends at an address while the new record rules it may not.

**Why this is not merely pedantic.** The draft repairs exactly this clause in the glossary and not in the record. §10 item 13: "`path` gains the empty position and the relation position" - `CONTEXT.md`'s `path` entry reads *"ending at an address whose endpoint carries what decides whether it is worth the next call"*, i.e. the same phrase, and the draft caught it there. The asymmetry is the tell that `0101`'s copy was missed rather than deliberately left.

**Verdict: BLOCKING.** The fix is small - one more clause in item 2 (*"ending at an address" becomes "ending at a position, which is an address where the position is non-empty"*, or equivalent) - but as §10 stands the ruling and the landed record disagree. Threshold (c): a ruling contradicts a landed record whose repair §10 does not list. Ambiguity (the record is named in §10, but the edit specified does not reach the contradiction) resolves to BLOCKING per the brief.

---

### 2. REPAIR - §2 attributes to `0101` an open question `0101` does not carry, and whose own source says no record states it

**Section.** §2, *A relation position carries the link's fields…*.

**Claim.** "The edge `id` fails both clauses today: no admitted form starts from or references an edge id, and **`0101` leaves open whether an edge's `id` is an address at all and what `look_at` of an edge would return**."

**Cited record.** `0101`.

**What the record actually says.** `0101`, *Input*, closing paragraph, in full:

> **An address** is a handle fetch accepts: a node's `id`. Whether an edge's `id` is one turns on whether the two ids share one space, which `0025` scopes to link endpoints and no record settles.

That is the address half, and the draft has it right. `0101` says **nothing** about what `look_at` of an edge would return. That clause comes from #85's resolution §10 - *"whether an edge's `id` is a fetch address, which turns on the id space no record settles, **and what `look_at` of an edge would return, which no record states**"* - which was a *what this ticket does not decide* item and was **not** carried into `0101` when §9.7's two records were written.

**Aspect mismatch.** None; this is the second failure `reading-records.md` names - *"Cite the record that states the claim, not the nearest plausible one"*. The quotation-free half of the citation verifies; the attribution does not. The correct citation is #85's resolution §10, and it is worth noting that the sentence there ends *"which no record states"* - so citing a record for it is precisely what that sentence forbids.

**Verdict: REPAIR.** The ruling survives: the edge `id` is excluded on the criterion's two clauses, and the first of them ("no admitted form starts from or references an edge id") plus `0101`'s genuine address question carry it. Only the pointer changes. §11 states the same open question correctly ("whether an edge's `id` is an address, and what a relation position carries once it is (`0101`'s open question)") - there the parenthesis attaches to the address half, which `0101` does state.

---

### 3. REPAIR - §2's supporting ground reads `0096`'s edge `id` as a repair concern; `0101` names only `detach`, and `0096` names `attach` beside it

**Section.** §2, same paragraph.

**Claim.** "`0096`'s ground for the `id` is a write's need to name the link, **which is a repair concern the test does not reach** (`0101`)."

**Cited records.** `0096`, `0101`.

**What the records actually say.** `0096`: *"The edge carries an `id`. … Without it **`attach` and `detach`** have nothing to name."* `0101`: *"**A repair read** - finding a dangling ref for `0018`'s owed validation pass, or **the link a `detach` must name** - is not a judgment the coordinator must make."*

**Aspect mismatch.** `0101`'s repair-read list reaches `detach`, not `attach`. `attach` advances a success path - it is how an annotation acquires its target - so *a write's need to name the link* is half a repair concern and half not. `CONTEXT.md`'s **repair method** entry draws the same line: *"an operation that exists to correct a mistake - a retarget, a delete, a re-land - as opposed to one that advances a success path."*

**Verdict: REPAIR.** The exclusion of the edge `id` does not rest on this sentence (the draft says it "fails both clauses today" and names them), so no ruling moves. Narrow the sentence to `detach`, or drop the repair framing and rest on the two clauses alone.

---

### 4. REPAIR - §5's line ruling makes a path position a third home for a line; `CONTEXT.md`'s `the line` entry says two, and §10 item 13's enumeration does not name that clause

**Section.** §2 ("Every node position carries its kind's line"), §5 ("The progress position is a new line for `progress`").

**Claim.** A path position carries its kind's line - a ruling, and the one §5's whole second table rests on.

**Cited record.** `CONTEXT.md`, *the line*.

**What the record actually says.**

> The render of a node that is one `look_at` away … **It appears in two places: inside an `<edge>`, and inside a composed section (`0094`).**

Under this draft it appears in three: inside an `<edge>`, inside a composed section, and at a routing path's node position.

**What §10 lists.** Item 13 lists the entry and enumerates the changes: the band-B clause rewritten, "the entry gains `progress`'s line as a path position and the row-versus-line distinction, keeping *a ring 0 row is not a line*". It never names the *two places* clause, which is the sentence the ruling falsifies.

**Verdict: REPAIR.** The entry is listed for amendment and the ruling is unaffected; one clause is added to item 13's enumeration. (Contrast finding 1, where the record's own copy of the clause is not listed at all.)

---

### 5. REPAIR - §3's J7 row cites #85 §7's *gap table* for a gloss that is in §7's *forms* table

**Section.** §3, table row J7.

**Claim.** "That `given` names the artifact stating the requirements and `owed` the deliverable is this record's reading of `0012`'s enum; no landed record glosses either value, and **#85 §7's gap table is the only prior**."

**What the sources actually say.** `0012` gives `spec` a bare `role ∈ {given, owed}` with no gloss; `0096` and `0082` both quote the enum without glossing it; `CONTEXT.md` has no entry for either value. So *"no landed record glosses either value"* verifies. But #85 §7's **gap table** is the per-scenario S1-S7 table, and neither `given` nor `owed` appears in it. The only prior is in §7's **forms** table, the row *"`MOVE` with `Q` | the artifacts a `spec` link marks as **owed** | … | `0012`'s `role`"*.

**Verdict: REPAIR.** Wrong table inside the right section; the ruling (J7's must-judgment, and the `[role = given]` selection) is untouched.

---

### 6. REPAIR - §10 item 14's cross-reference points at item 12; `CONTEXT.md` is item 13

**Section.** §10 item 14.

**Claim.** "Of the six #82 listed, `0044` reads clean and **`CONTEXT.md`'s `the line` is item 12**."

**What the draft actually contains.** Item 12 is `0018`; `CONTEXT.md` is item 13.

**Cross-check of the substance, which is sound.** #82's closing comment lists six: `0013`, `0092`, `0091`, `0044`, `0093`, and `CONTEXT.md`'s `the line`. §10 item 14 carries four of them (`0091`, `0092`, `0093`, `0013`) plus `0094`'s closing sentence, declares `0044` clean, and routes `CONTEXT.md` to the amendment list. All six are accounted for.

**Verdict: REPAIR.** A pointer, not a ruling.

---

### 7. REPAIR - the opening attributes to #86's *body* four things that are in #86's *comment*

**Section.** Opening paragraph, *What this comment is*.

**Claim.** "**The four things the body asked for**, under the definition `0101` landed: the necessity test's formalisation (§1), the two type questions … (§2), which judgments the coordinator must be able to make (§3) … and whether crossing a Ref-typed field from a computed set and filtering on a link's own fields have a must-judgment (§8). **Plus the two things the body carried in**: the plan's scoping point (§0) and the `0042` overturn #82 authorised (§6, §7)."

**What #86 actually contains.** #86's **body** asks one question ("What do *course information* and *the plan* contain, read as routing's inputs?"), carries the scoping point and the overturn - so the second half of the sentence is right. The numbered four are in #86's single **comment**, *"Unblocked by #85's resolution (2026-09-06) - and given a first task by it. … What this ticket decides, under that definition: 1. First, the test's formalisation. 2. Which judgments the coordinator must be able to make. 3. Two type questions #85's first application left open… 4. Whether crossing a Ref-typed field from a computed set, and filtering on a link's own fields, have a must-judgment."*

`CLAUDE.md` draws the line the sentence crosses: *"Updates go in comments, not in body edits. The body is the current statement; the comments are its history."*

**Verdict: REPAIR.** Say *the four things this ticket was given* or *the four in #86's comment*; the two body-carried items stay as written.

---

### 8. REPAIR - §5 names `grade_share` as *weight*, which `CONTEXT.md` lists under _Avoid_

**Section.** §5, obligation position table, `grade_share` row.

**Claim.** "J0's inputs Billy named are size and absorption, **not weight**, and J1 does not turn on a share."

**What the glossary says.** `grade_share`: *"The approximate share of the final course grade an obligation carries, in percent… _Avoid_: **weight** · worth_percent · reading a column of shares as a partition of 100."*

The same row then uses the endorsed word ("J1 does not turn on a share"), so the sentence carries both the avoided term and its replacement. Note that `0032`'s own title (*A conditional grade weight gets a marker*) predates the glossary entry, which is exactly the vocabulary-travels-with-content hazard `reading-records.md` names; it is not a licence to reuse the word.

**A second, weaker instance in the same class.** §6 twice writes *"`0039`'s layer"* ("Size and absorption belong to `0039`'s layer") in a paragraph that also uses **layer** in the glossary's sense ("behind a layer that does not exist (#25)"). `CONTEXT.md`'s `layer` entry reserves the word for the three strata and lists three misuses under _Avoid_; a reader meets two senses in one section. Recommend *`0039`'s rule* or *`0039`'s formalism*, which the same section already uses elsewhere.

**Verdict: REPAIR** for both. No ruling moves.

---

## Sweep required by the lens, item 2: landed records touching the bands, ring 0's field set, the line's field set, `has-more`, `state`'s home, and what an edge or relation carries

I read every mention across `docs/adr/`, `docs/adr/README.md` and `CONTEXT.md`. **Every one is either consistent with the draft or listed in §10.** Specifically:

| mention | where | §10 coverage |
|---|---|---|
| `0082`'s transfer clause, both occurrences (lines 20 and 30) - *"obligation's line is ring 0's **band B** field set"* and *"obligation's line is ring 0's band by a transfer of the field set"* | `0082` | item 7, which names "in both places it appears" - correct, there are exactly two |
| `0095` - *"`0082` calls obligation's line "ring 0's band plus `has-more`", and band A already carries `has-more`, so *the band* is band B"* and *"No rule generates a new kind's line"* | `0095` | item 7, both |
| `0091` - *"Ring 0 carries the band and excludes `parts` and `grade_share` (`0038`)"* | `0091` | item 14, pointer debt |
| `0092` opening (*"`0038` puts `has-more` among band A's routing fields"*), two Considered Options rows (*"shipping band A with six fields"*, *"anything beyond the band's own fields"*), Source line (*"membership in band A is `0038`'s"*) | `0092` | item 14, "its opening sentence, its Considered Options, and its Source line" - all four mentions fall inside those three |
| `0093`'s ring 0 section (*"band A and band B are ordinary words"*) and two rejected-names rows (`attention` for the band; `status`/`state` for the band) | `0093` | item 14, named exactly |
| `0094`'s closing section - *"Its render, the band's representation and `has-more`'s surface name all travel with it"* | `0094` | item 14, "closing sentence" |
| `0019` - *"residency is an access policy over **obligation nodes' fields**"*, which the progress position falsifies | `0019` | item 11 |
| `0089` - *"a whole **line** per changed obligation"* | `0089` | item 9 |
| `0042`'s own overturn paragraph, which repeats `0100`'s admission placement | `0042` | item 3 |
| `0038`'s band block and *"band B drops the last three"* | `0038` | item 4; and the draft's "every row grows by what band B lacked - `done_by`, `optional`, `has-more`" is exactly those three |
| `0100`'s clause table, its refresh paragraph (*"a line, whose field set is band B, which is the selection clause"*), its *not settled* standing | `0100` | item 5, four places |
| `CONTEXT.md` `ring 0`, `band A` / `band B`, `obligation`, `path`, `the line` | `CONTEXT.md` | item 13 (with the gap at finding 4) |
| `0013`'s roughly-55 cost argument | `0013` | item 14 |
| `0035` - `state` on `progress`, not `obligation` | - | not contradicted; the draft reaches `state` by a crossing rather than copying it, and defers the move to #71 |
| `0096`'s `<edge>` with `id`, `type`, `direction`; `0093`'s names row saying the same | - | not contradicted; §2 explicitly separates the path's relation position from the `<edge>` element and leaves both records standing, with `0093`'s row listed at item 14 |
| `0044` - *"holds ring 0 in its conversation context… depth is just enough to triage"* | - | the draft's "reads clean" judgment holds: `0044` is about not holding the skeleton, and the progress position is a path position rather than depth (`0101`) |

The one gap the sweep found is finding 1 (`0101`'s *ending at an address*), which is not a band/field-set mention and so falls outside this table.

---

## Citations checked and found sound

Records, checked for the aspect the draft uses each for:

`0001` (the requirements sentence, job 2, job 3 - all three present in the post-#85 rewrite) · `0003` (`nodes_without`, set difference) · `0007` (park with a wake) · `0010` (surface a progress claim, never resolve one; the rule is about the caller) · `0012` (`about : annotation → any`; `requires` with two signatures; `spec` with `role ∈ {given, owed}`; `builds-on : obligation → obligation`; `prepares-for`) · `0013` (roughly-55, and its scope clause recorded in `0038`) · `0017` (`Link := from · to · kind · role? · locator?`) · `0018` (a ref may dangle; deleting a course does not cascade; the link-set validation pass is "owed and unbuilt") · `0019` (the quoted residency clause) · `0021` (query-by-time-period is a separate projection; a course's coarse grouping deliberately not modelled) · `0026` (`course.id` is the supplied code) · `0027` (`kind` as required discriminator) · `0028` (per-field CRUD; one free-text field per kind; annotation timestamps) · `0029` (`obligation.course` mandatory, single-valued, monomorphic) · `0032`/`0033` (`parts` carries no size; the replacement is "an interaction", not a field) · `0035` (`not_started` by absence; "one current value per target"; *why `state` sits on `progress` and not as a field of `obligation`*) · `0036` (in-place modification; `origin` confers no immutability) · `0037` (row 1's *"ordinal comparisons, not hour counts"* and *"observed rather than stored - ordinally, from `parts` and item notes first"*; row 11's v2 deferral of `course.offering_term` on the coursework-boundary ground; rows 13 and 14 leaving term boundaries open; the no-re-add rule) · `0038` (the seven; the roughly-55 and its 2px3 scope clause; the `parts` exclusion ground) · `0039` (symmetry scoped to the judgment's set; `observe … else dispatch(X, member)` returning a value in the same shape as every other member's) · `0040` (its **method**, not its ground - correctly distinguished, as `0100` requires) · `0041` (`due` ascending, nulls last, among nulls by `done_by`, ties by the handle, never array order; the struck grouping) · `0042` (three triggers; `state == in_progress`; *"it is present, it is routable"*; the uniform-depth defence; breadth never a defect; the importance sentence and the live overturn permission) · `0043` (discard) · `0044` (residency) · `0046` (the delivery ruling, quoted correctly and used as a delivery rule, with `reading-records.md`'s own table cited against the scope misreading) · `0051` (shallow/deep) · `0056` (*"provenance is stated prominently at every read"*) · `0070` (capabilities not methods) · `0071` (the blind-spot warning, used as a warning and not as a scope conclusion) · `0079`/the fall26 caveat · `0081` (a negative answer names its boundary) · `0082` (four rules; `id`/`kind` address; the `locator` ground *"says where you land after walking, which does not bear on whether to walk"*; the second exception covering `has-more` and `role`; a defaulted `progress` carries no `id`; the Source line pointing at the fall26 schema for the field tables) · `0084` (`look_at(course)` composes `obligations.list(course)`) · `0089` (whole lines, and its ground) · `0091` (*"a coordinator can therefore name a course row it never read"*, used for the write aspect it speaks about) · `0092` (the value is a set of link kinds; ring 0 cannot list a neighbourhood) · `0093` (an edge carries `id`, `type`, `direction`) · `0094` (sections cut by source) · `0095` (each section's depth; one field set per kind, not varying per row) · `0096` (the `<edge>`; `has-more` off the line; the worked example's five attributes, which do lack `done_by` and `optional` as item 7 says) · `0097` (an `id` marks an addressable object; a member omits what its container fixes) · `0099` (`added_at` is about the row; *"no reader"* declined as a ground; *"a January answer is indistinguishable from today's"*) · `0100` (the four clauses; the admission placement; the refresh paragraph; the *"does not itself say that ring 0 ranges over every obligation"* doubt; the `0038` diagnosis) · `0101` (definition; vocabulary and its lack of set operations; the one-return premise; the test's informal wording; *"admits by what a form lets a chain produce"*; the endpoint criterion; the *"judgment across obligations is a judgment about their relations"* ground; *"Affordability is a separate question the type does not answer … `0039`'s affordability is per-member depth"*; the undecided dispatch-call question; the unruled width gate; the time projection as a routing result; the repair-read exclusion) · `0102` (the membership row leaving the Ref crossing's admission to #86).

Glossary entries: `link`, `link kind`, `id`, `Ref`, `handle`, `closure`, `kind`, `layer`, `obligation`, `progress`, `sticky_note`, `annotation`, `origin`, `parts`, `name`, `due`, `done_by`, `grade_share`, `covers`, `applies` (including the resolve-path clause `0101` landed), `ring 0`, `band A`/`band B`, `coordinator`, `holder`, `the walk`, `the block`, `the line`, `routing`, `path`, `dispatch`, `faithfulness`, `reload`, the rigidity rule and its declared exemptions, the render test, the graveyard, `repair method`, `dissolved item`.

Issues: #10 (*Asking*), #13 (`time_point`, location, duration - all three are #13's), #14 (body's *"the plan is where that judgment gets written down, or nowhere"*; the comment's *"6 of 6"* three buckets, and its own *"It does not say the plan is those three buckets"*), #16 (its wake is the first real semester decision observed by hand; its two membership tests), #17/#19/#20 (the artifact/concept line debt, cited the way `0095` and `CONTEXT.md` cite it; #20's gate is *the artifact layer acquires a writer*), #25 (the concept layer), #58 (the *Out of scope* line on the plan, quoted in substance), #71 (does `state` move onto `obligation`), #79, #82 (the responsibility sentence not widened; *"flat 6,482 characters, structured 7,598"* at 55 rows, with the scope clause that band A is 21% of rows in one course and 2px3 would move it - verbatim from #82's *Material* section; the six pointer debts), #84 (the acceptance standard *"expose every necessary operation … never a workflow per imagined scenario"*; Billy's raw decomposition in the body; the two deferrals unfrozen by the overturn permission; *Destination* placing the grammar later), #85 (§7's three provisional answers, the connectives-as-one-form reading, the `FILTER` row's *"no crossing reaches a date"*, the `nodes_without` case, S1-S7's dispositions, the S7 Ref-crossing gap), #87, #88.

**Numbers and counts, each re-derived:**

- *roughly 55 obligations for five courses* - `0038`, with the 2c03/2aa4 evidence base and 2px3 excluded. Draft states it as a fall26 number carrying the standing caveat, in §0/§4/§11. **Sound, and the scope clause is carried at both mentions.**
- *flat 6,482 characters, structured 7,598* at 55 rows - #82's *Material* section, verbatim, with its band-A-21% scope clause. **Sound.** The draft's inference that the figure is now "a floor" follows from band B's three missing fields plus the progress position's two, which matches `0038`'s band block.
- *three buckets replicating 6 of 6* - #14's comment, verbatim, including its own "It bounds acceptance item 1 without answering it". Draft calls it evidence and not a ruling, and flags the fall26 caveat. **Sound.**
- *`0038`'s seven* - `course · name · due · state · optional · done_by · has-more`; the draft's row is those seven with `state` re-typed plus `id` and `kind`, giving eight at the obligation position. **Arithmetic checks.**
- *band B drops the last three* - `optional`, `done_by`, `has-more`; §4's "every row grows by what band B lacked - `done_by`, `optional`, `has-more`". **Matches.**
- *the six #82 listed* - `0013`, `0092`, `0091`, `0044`, `0093`, `CONTEXT.md`'s `the line`. All six dispositioned (see finding 6 for the item-number slip). **Sound.**
- *`0082`'s transfer clause stated twice* - two occurrences, confirmed by grep. **Sound.**
- *seven session rulings* - the second paragraph enumerates seven distinct items. **Count checks.**
- *`0012` has two further link kinds between an obligation and an artifact* - `spec` and `prepares-for`. **Checks against the nine-row table.**

---

## Summary

**1 blocking, 7 repair.** The blocking finding is narrow and cheap to fix: §2's ruling that a path may end at an empty position contradicts `0101`'s *"ending at an address"*, and §10 item 2's enumeration - which names the very sentence the phrase sits in - repairs only the word *endpoint* within it, leaving the contradiction standing after the amendments are applied; the draft caught the identical phrase in `CONTEXT.md`'s `path` entry (item 13) and missed the record's own copy. The seven repairs are attribution and pointer corrections that move no ruling: an open question sourced to `0101` that lives in #85's resolution §10 and that says of itself *"which no record states"*; `0096`'s edge `id` read as wholly a repair concern when `0101` names only `detach`; `CONTEXT.md`'s *the line appears in two places* clause unnamed in an amendment item that does list the entry; a gloss sourced to #85 §7's gap table that is in §7's forms table; an item-number cross-reference off by one; four items attributed to #86's body that are in #86's comment; and `weight` used for `grade_share` against that entry's own _Avoid_ list, with a weaker instance of `layer` used for `0039`'s rule. Every other citation I opened - fifty-one records, thirty-eight glossary entries and twenty issues - says what the draft attributes to it, for the aspect the draft uses it for, and every number and count re-derives.
