# Review 11 - draft v6, lens 1 (attribution), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v6.md`, full repository read access, and `docs/agents/reading-records.md` as the discipline. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-10. Blind to the lens-2 reviewer.

**Report, verbatim:**

---

## Findings

### 1. BLOCKING - `0101` assigns "what a non-endpoint position carries" to the grammar, and §10 does not repair that clause

**Section:** §2, second and third bold paragraphs; §10 item 2.

**Claim:** *"Every node position carries one field set per kind, of line depth, derived at that position by the criterion; and the criterion runs over every position."* And: *"A relation position carries the link's fields that pass the same criterion, and today none does."*

**Cited record:** `0101`, via the amendment in §10 item 2.

**What the record actually says:**

> "What a non-endpoint position carries, whether a path may repeat a node, and how paths are deduplicated are the path's precise type, **which is the grammar's**."

**The mismatch.** §2 rules what a non-endpoint position carries. `0101` places that question with the grammar - and the draft honours the *other two* items of that same sentence, deferring them by name: §11 defers *"whether an obligation may carry more than one progress record"* and *"how paths are deduplicated when one step matches twice, which `0101` leaves to the grammar"*. So the draft reads that sentence, takes two of its three items as binding, and silently overrides the third. §10 item 2 amends `0101` in exactly five places - all of them the `endpoint` → `position` rename - plus "a pointer to the new record for the formalisation and the type questions". After those amendments land, `0101` still says in its own voice that a non-endpoint position's content is the grammar's, while the new record rules it. Two landed records then disagree.

**Mitigation, stated because it is real:** #86's own unblocking comment assigns this to the ticket by name - *"Two type questions #85's first application left open … **what a non-endpoint position of a path carries**, and whether a crossing may be optional"* - and #85's §8 says the same. So the ruling is authorised; it is `0101`'s wording that is stale, and item 2's "pointer … for the type questions" arguably reaches it. But the draft is elsewhere explicit about which sentence of which record is struck (item 3, item 6, item 7, item 11, item 12), and this one is not named. Under the threshold's ambiguity rule this resolves upward.

**Repair:** §10 item 2 should name the clause and say what it becomes - the three items split, *what a non-endpoint position carries* pointed at the new record, *repeat* and *deduplication* left with the grammar.

**Verdict: BLOCKING.**

### 2. REPAIR - `0037` row 11 is cited for a distinction it does not draw, and a graveyard row is worked around rather than reconciled

**Section:** §4, *"Why there is no predicate, and what that assumes."*

**Claim:** *"`course` carries a `term` today (`CONTEXT.md`'s *the line*, `0094`'s example), the term of that offering, **which is not the catalog field `course.offering_term` that `0037` row 11 defers to v2**, so the per-member value exists and only the comparand does not."*

**What `0037` row 11 actually says:**

> "| 11 | `course.offering_term` · `course.prereq` | **Reason replaced - the row that most needs it.** Both stated reasons fail … Replacement: **out for v1 because v1's boundary is coursework; deferred to v2** (`D6`) |"

**The mismatch.** Row 11 defers `course.offering_term` - that half of the attribution is sound. It says nothing that distinguishes a *catalog* term field from an *offering* term field; "catalog" is the draft's word, and the distinction is the draft's own reading, presented as the record's. `0037`'s header rule is that its rulings bind and that a removed field does not return without a new ruling, so a claim that `course` carries a `term` today needs to be marked as a reading - the draft does mark exactly this kind of thing elsewhere (J7's `given`/`owed` gloss: *"this record's reading of `0012`'s enum; no landed record glosses either value"*).

There is also a latent conflict here the draft does not surface: `CONTEXT.md`'s `the line` entry (*"course's is `id` `name` `term`"*) and `0094`'s worked example (`term="winter-2026"`) assert a `term` on `course` while `0037` row 11 sits in the graveyard. §10 lists `0037` row 1 for repair and §11 lists rows 13 and 14; neither reaches this. §6 found and repaired the exactly analogous `0037` row 1 / `0033` conflict, which is the standard this one falls short of.

**No ruling turns on it** - the conclusion (*the predicate is not written*) survives either way, and is if anything strengthened if the field does not exist.

**Verdict: REPAIR.**

### 3. REPAIR - §7's *What survives of `0042`* is an exhaustive-looking list that drops the sentence §4 leans on

**Section:** §7, final paragraph; §10 item 3.

**Claim:** *"**What survives of `0042`:** the three triggers, as the coordinator's judgment rule for *near*; the sentence barring a notion of importance (§6); the ruling that breadth is never a defect. **What dissolves:** the partition as a property of ring 0, the band names, and band B's reduced field set."*

**What the record actually says**, in the sentence neither list disposes of:

> "An undated obligation is in band B and that is not a hazard: **it is present, it is routable**, and its detail is one call away."

**The mismatch.** §4 cites that sentence approvingly and load-bearingly - *"`0042` says the same of an undated obligation: *"it is present, it is routable"*"* - as agreement with the standing intent's range. But its subject is band B, which §7 dissolves, and §10 item 3 restates `0042`'s body as §7 with "the partition and band B struck", which takes the sentence with it. The survivors list reads as exhaustive (`reading-records.md`'s first discipline), and the reader who repairs `0042` from item 3 will delete the one sentence §4 used as support without being told what replaces it.

**Repair:** name it - it survives as *every obligation is in the standing intent's range, dated or not*, which is what §4 rules, or say it is subsumed by the range and struck.

**Verdict: REPAIR.**

### 4. REPAIR - §10 item 8 asserts a repaired title for `0038` that item 4 does not produce

**Section:** §10 items 4 and 8.

**Claim:** item 8 - *"`0038`'s, `0042`'s, `0089`'s and `0100`'s rows restated to match their repaired titles."*

**What item 4 says:** *"**`0038`, repaired in place.** Band B struck; the field set restated as the row with `state` as the progress position; the ground replaced by the derivation; the exclusions' arguments kept as arguments; the sizing paragraph kept with its scope clause and the width bet named."* No title repair.

**The mismatch.** `0038`'s title is *"Ring 0 carries seven routing fields; `parts` and `grade_share` are excluded, and `grade_share`'s exclusion rests on a corpus argument"*. Under §5 it no longer carries seven - it carries eight at the obligation position with `state` re-typed to a second position - so the title must move. The three sibling items say so in their own text (item 3 *"Title and body restated"*; item 9 *"its title and two sentences"*; item 5 *"the record's *not settled* standing updated to *derived at #86*"*, which is `0100`'s title). Item 4 is the one that does not, and item 8 assumes it did.

**Verdict: REPAIR.**

### 5. REPAIR - #79's blockers are stated as two when four are on record

**Section:** §9, fourth bullet.

**Claim:** *"**#79 (tool descriptions).** Still blocked on #87 and #88."*

**What the records say.** #82's body: *"It blocks #79 … That is a third upstream of #79, alongside #70 and #64."* #84's *What this map blocks*: *"**#79** … A fourth upstream alongside #70, #64 and #82."* #79's own body: *"Blocked by #70."*

**The mismatch.** The draft unblocks #82 in the bullet above this one, but #82 does not thereby close, and #70 and #64 are untouched here. The sentence reads as #79's whole blocker set. It inherits #85 §8's phrasing (*"Still blocked on #86-#88"*), which was scoped to this map - so the fix is one qualifier, "within this map", not a new claim.

**Verdict: REPAIR.**

### 6. REPAIR - "no landed record carries a field table" is contradicted by two of the records the same sentence cites

**Section:** §5, the sourcing paragraph.

**Claim:** *"The field lists were assembled from this repository's records … and `progress`'s from `0028`, `0035`, `0036` and `CONTEXT.md`'s `origin` entry - **because no landed record carries a field table**."*

**What `0036` actually says:**

> "```sticky_note := kind · id · category · body · origin · created_at · updated_at```"

and `0017`:

> "```Link := from: Ref · to: Ref · kind: LinkKind · role?: string · locator?: string```"

**The mismatch.** `0036` carries `sticky_note`'s field table, and the draft's own derivation of `progress`'s fields runs through it (`0035`: `progress` *"carries the same `origin`, the same timestamps and its own free-text field"* as a sticky note). The claim is true of `obligation`, which is what it is doing work for; as written it is a claim about the whole repository and the same sentence falsifies it.

**Verdict: REPAIR.**

### 7. REPAIR - `0099` treats `created_at`/`updated_at` as a pair, and §5 splits them without saying so

**Section:** §5, the progress-position table.

**Claim:** `created_at` → *"when the record entered; no judgment changes on it | out"*; `updated_at` → in, on `0099`'s harm.

**What `0099` actually says:**

> "`schema.md` §4: the pair *"is what makes a time-bound statement safe to store at all"* - *"an undated sentence from the start of term goes on influencing judgment forever"*."

**The mismatch.** `0099`'s title is *"the first selection cut is the timestamps"* and its ruling keeps the annotation pair *together* in a block on a joint ground, while striking `added_at`. §5 borrows one half of the pair's harm (*"a January answer is indistinguishable from today's"*, correctly attributed) and drops the other half without addressing that `0099` argues them jointly. The aspect defence is available and is not made: `0099`'s scope is a **block's** render and §5's is a **path position**, which are different questions. Say so in the `created_at` row.

**Verdict: REPAIR.**

### 8. REPAIR - *the agent* (bare) is on `CONTEXT.md`'s `_Avoid_` list

**Section:** §3, bucket 3.

**Claim:** *"its predicate has three structural readings no record picks between: a conflict **the agent** may not close itself (`0051`) …"*

**What `CONTEXT.md` says**, under `coordinator`:

> "_Avoid_: master session · *the agent* (bare) · orchestrator · …"

**The mismatch.** The word arrives from `0051`, which does use it (*"A shallow collision the agent may resolve itself"*) - which is `reading-records.md`'s *"an artifact hands over its vocabulary along with its content"* in miniature, one landed record instead of a frozen one. This is the draft's only `_Avoid_` hit in a full sweep of the glossary's avoid lists; `mastery`, `reachability`, `layer`, `validation`, `row` and `edge` were each checked and each is used in the sanctioned sense.

**Verdict: REPAIR.**

## Citations checked and found sound

**Quotations, verbatim against source.** `0101`'s test wording, *"admits by what a form lets a chain produce"*, *"a judgment across obligations is a judgment about their relations"*, *"a routing result's endpoint"*, *"Each endpoint carries its own kind's deciding fields - one set per kind"*, *"Affordability is a separate question the type does not answer … `0039`'s affordability is per-member depth"*, the criterion, the refusal-not-empty clause, and the undecided dispatch-call question. `0100`'s *"which rows enter"*, *"which is the selection clause"*, and *"`0042` does not itself say that ring 0 ranges over every obligation in a semester"*. `0042`'s *"it is present, it is routable"*. `0082`'s *"says where you land after walking, which does not bear on whether to walk"*, its second exception, its defaulted-`progress`-carries-no-`id`, and its transfer clause in both of the two places §10 item 7 says it appears. `0095`'s *"so the band is band B"* and its section-opening transfer sentence. `0091`'s *"a coordinator can therefore name a course row it never read"*. `0099`'s *"a January answer is indistinguishable from today's"* and its decline of *no reader* as a ground. `0056`'s *"provenance is stated prominently at every read"*. `0010`'s *"structural, never personal"*. `0018`'s *"owed and unbuilt"*. `0037` row 1's *"observed rather than stored - ordinally, from `parts` and item notes first, then by asking for a relative comparison"* and *"ordinal comparisons, not hour counts"*. `0033`'s *"does not carry size"* and *"not another field"*. `0001`'s *"helping model an assignment's requirements is in scope"*. #14's *"if size is judged from progress and load rather than stored as a number, then the plan is where that judgment gets written down, or nowhere"*. #84's *"expose every necessary operation, never a workflow per imagined scenario"* and *"which is what `sticky_note` was designed for"*. #82's body for *"flat 6,482 characters, structured 7,598"*, the 21%-of-rows scope clause and 2px3.

**Attributions, checked separately from the quotations.** `0046` used as a **delivery** rule and not a scope rule, with `reading-records.md`'s own table cited for the misreading - correct on both halves. `0039` used for the observe/dispatch formalism at member grain, and explicitly *not* used for size, on the ground that its dispatch returns a per-member value with no position for a between-members relation - a correct aspect separation. `0018` for a dangling ref and no cascade; `0029` for `obligation.course` being mandatory; `0026` for `course.id` being supplied. `0035` for `state`'s home and for barring the copy onto `obligation`, with the *"one current value per target"* reading flagged as a reading in §11. `0092` for `has-more`'s value and `0096`/`0092` for the ground that survives only where a neighbourhood cannot be listed. `0097` used as a render rule about restating and explicitly denied decisive force at a position. `0012` for `about: annotation → any`, for `requires`'s two signatures, for `spec`'s `role ∈ {given, owed}`, and for `builds-on` being the one cross-obligation relation before the concept layer. `0102`'s membership row leaving the Ref crossing's admission to this ticket. `0084` for `look_at(course)`'s composition and `0101` for calling it resolve-through-fetch. `0070` bounding the map at capabilities. `0013`'s roughly-55 and its `0038` scope clause. `0021` for the time projection and for the coarse grouping. `0093`'s ring 0 section, its two band rows, its edge-carries-`id`-`type`-`direction` row. #85's §7 (the three provisional answers, the `MOVE` with `Q` row, the `nodes_without`/`covered` case, the field-comparison row's *no crossing reaches a date* ground, S1-S7) and its §10 (the time projection assigned to #86 by name; *what `look_at` of an edge would return, which no record states*). #82's *must not be re-opened* list - the draft correctly identifies **two** of its four items as moved, and correctly identifies both of its orphans. #86's own body for the four deliverables and the three-bucket bound.

**Divergence from an issue body, and the draft is right.** The draft attributes the `0042` overturn permission to **#82**; #86's body says #84. `0042` (*"ruled at #82 (Billy, 2026-09-04)"*), `0100` and `CONTEXT.md`'s `band A / band B` note all say #82. The draft's attribution is the correct one; #86's body is the stale one.

**Numbers, counts and cross-references, re-derived.** Seven session rulings named in paragraph two, seven found (§0, §6, §7, §4-intent, §9-arrangement, §3-bucket-3, §4-dangling-ref). Three formalisation questions from `0101`/#86 plus one from the reviews = the four in §1, and the (i)/(ii)/(iii) numbering matches `0101`'s own order. `0038`'s seven, minus `state`, plus `id` and `kind` = the eight-item obligation position, as §5 states. Band B (`course · name · due · state`) against the repaired line adds exactly `done_by` and `optional`, which is what §10 item 7 tells `0096`'s example to gain. §10 item 2's five `0101` places all exist and all carry the word or the phrase named. §10 item 7's two `0082` sentences, three `0095` sentences and one `0096` example all exist. §10 item 14's *"six #82 listed"* is right - `0013`, `0092`, `0091`, `0044`, `0093`, `CONTEXT.md`'s `the line` - and the draft disposes of all six, with `CONTEXT.md`'s `the line` correctly pointed at item 13. §10 item 13 covers all three of `CONTEXT.md`'s band mentions (`ring 0`, `band A`/`band B`, `the line`). §9's ten bullets match §10 item 15. `0100`'s clause table has the admission, selection, arrangement and refresh rows item 5 names.

**Sweep for landed contradictions, per the lens's second instruction.** Every mention of the bands across `docs/adr/` and `CONTEXT.md` (`0038`, `0042`, `0082`, `0091`, `0092`, `0093`, `0094`, `0095`, `0100`, `CONTEXT.md` ×3) is either amended in §10 or listed as a pointer debt. Every mention of `has-more` (`0038`, `0082`, `0091`, `0092`, `0093`, `0094`, `0095`, `0096`, `0101`) likewise; `0093`'s criterion-4 example is untouched by the draft and needs nothing. `state`'s home: `0035`, `0038`, `0071`, `0092` - the draft keeps `0035`'s placement, re-types it as a position rather than moving it, and lists #71's re-typing in §11. What a path ends at: both `0101` sentences carrying *"ending at an address"* are in §10 item 2 and `CONTEXT.md`'s `path` entry is in item 13; `CONTEXT.md`'s `closure` entry uses *endpoint* in the terminal sense and needs no change. What an edge carries: `0096`, `0093`, `0017`, `0082` - the draft separates the path's relation position from the `<edge>` element explicitly and leaves the element's contents alone. `0044` does read clean, as §10 item 14 claims: its *"never deepens"* is about accumulation, not about the fixed intent's second position. `0019` is correctly caught as needing its *"obligation nodes' fields"* clause widened once a `progress` position is resident.

## Summary

**One blocking finding and seven repairs.** The blocking one is a single unlisted sentence: `0101` says what a non-endpoint position carries is the grammar's, the draft rules it - with #86's own body authorising the ruling - and §10 amends `0101` in five places, none of them that sentence. Everything else is wording, a stated-as-record reading that should be stated as a reading (`0037` row 11 and `course.term`), an exhaustive-looking survivors list that drops a sentence §4 relies on, and four small inconsistencies of count or scope. Across roughly ninety citations checked - forty-odd verbatim quotations and the attributions checked separately from them, per `reading-records.md` - the quotations are clean without exception, the aspect discipline is honoured in the two places it has previously failed on this ticket's records (`0046` as delivery, `0039` as per-member affordability), and the draft twice demotes its own claims where the evidence is weaker than the assertion (size's classification, the `0035` multiplicity reading). One divergence from an issue body is in the draft's favour.
