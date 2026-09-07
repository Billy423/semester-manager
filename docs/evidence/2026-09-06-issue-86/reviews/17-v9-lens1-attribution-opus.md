# Review 17 - draft v9, lens 1 (attribution), Claude Opus

**Reviewer:** a fresh blind subagent (Claude Opus), given `drafts/v9.md`, full repository read access, and `docs/agents/reading-records.md` as the discipline. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-16. Blind to the lens-2 reviewer. Told that §5b is a draft section and that findings against it are repair.

**Report, verbatim:**

---

## Verdict

**No blocking finding.** Every record, glossary entry and issue the draft cites in §0-§8 says what the draft attributes to it, for the aspect the draft uses it for. I opened all fifty-three ADRs cited, the four `CONTEXT.md` entry clusters the rulings turn on, and issues #10, #13, #14, #16, #17, #19, #20, #25, #58, #71, #79, #82, #84, #85, #86, #87 and #88 including #85's resolution comment. I found fourteen repairs: four counting or coverage gaps, one missing standing caveat, two amendment-list omissions, three attributions that name a neighbouring record or an inference the record does not itself make, and four wording items.

The draft's handling of the two hazards `reading-records.md` names hardest is the strongest part of it. §4's `0046` paragraph reads the record for the aspect it binds - delivery, not scope - and cites `reading-records.md`'s own table for that. §5's `grade_share` cell declines `0042`'s *no reader by standing exemption* clause on the ground that `0099` declines that ground, while §7 keeps the same clause standing inside `0042` for the different aspect it serves there. Those two moves are aspect discipline done correctly, and they are the moves an attribution lens exists to catch failing.

---

## Findings, most severe first

### F1 - "five seams" is matched by no enumeration in the draft · REPAIR

**Section.** ¶3, *How it was reached*.

**Claim.** "**The next four rounds found one move repeated at five seams, and that is the method finding, stated once:** a field set transferred from a render record - `0038`'s band, `0096`'s edge, `0096`'s worked example, `CONTEXT.md`'s line - onto a routing position".

**What the draft's own enumerations give.** The dash-list names **four** sources. The next sentence names **four** rules ("what a relation position carries, when `kind` rides a position, what a line's field set is, one kind at two positions"). §5b has **five** bullets, but two of them - *Position sets for the other judgments* and *`has-more`'s collapse* - are not transfers from a render record, so they do not fill the gap either.

**Aspect mismatch.** None; this is a count with no support. `reading-records.md`: "re-derive one before it becomes load-bearing", and this number is the headline of the paragraph that justifies §5b's demotion.

**Verdict: REPAIR.** Either name the fifth seam or make the count four.

### F2 - "lands on `0038`'s seven plus the handle" omits two fields `0038` never carried · REPAIR

**Section.** ¶3, and §5's closing paragraph.

**Claim.** ¶3: "The derivation lands on `0038`'s seven fields plus the handle, with `state` re-typed as a position, which is an independent confirmation of `0038`'s selection on a different ground". §5: "that it lands on the same seven is a confirmation of `0038`'s selection".

**What `0038` actually says.** "Ring 0 carries `course`, `name`, `due`, `state`, `optional`, `done_by` and `has-more`; band B drops the last three."

**The mismatch.** The derived result is `id · name · due · done_by · optional · course · has-more` at the obligation position **plus `id · state · origin · updated_at` at the progress position** - ten values, of which `origin` and `updated_at` are in no version of `0038`. The draft knows this: §4's *Width* paragraph says "every row grows by ... the progress position's `id`, `origin` and `updated_at`". But the two summary sentences say the derivation landed on `0038`'s seven, and a reader who takes them at face value gets a row that is two fields short. The confirmation claim is real for the seven; the sentence overstates it by silence about the additions.

**Verdict: REPAIR.** Say "on `0038`'s seven plus the handle, with `state` re-typed, and with `origin` and `updated_at` added at the progress position".

### F3 - the `grade_share` cell's corpus figure carries no standing caveat · REPAIR

**Section.** §5, the `grade_share` / `grade_share_conditional` row.

**Claim.** "What closes the cell is `0038`'s independent corpus argument, audited at #82 and kept at §10: a rendered column of shares reads as a partition of the grade that it is not, since one course's column sums to 95 with the missing 5% having no row."

**What the record says.** `0038`: "one course's share column sums to 95, the missing 5% has no row, and two 1% bonuses sit outside the 100." The attribution is exact. But `0100` adds, in the same breath as endorsing the audit: "That corpus was supplied on 2026-09-04 and **is not held in this repository**, so the audit is not reproducible from this checkout."

**The gap.** `docs/agents/drafts-and-rulings.md`: "State it wherever such a number is load-bearing." This number is stated by the draft to be what *closes the cell* - the criterion's own verdict for J0 is left open in the same cell - so it is load-bearing in the strongest sense. §11's *Standing of the numbers* paragraph names only "the roughly-55 figure and the 6-of-6 bucket replication".

**Verdict: REPAIR.** Add the figure to §11's standing paragraph, or caveat it in the cell.

### F4 - the *endpoint* → *position* rename stops short of three places that use the word in the amended sense · REPAIR

**Section.** §10 items 2, 13 and 14.

**Claim.** Item 2 renames *endpoint* to *position* through `0101` "wherever it is used in §2's sense", and item 7 converts `0095`'s "every endpoint is one line" to "every position is of line depth".

**What is left standing.** Three landed sentences use *endpoint* in exactly the amended sense and appear in no item of §10:

- `CONTEXT.md`, `applies`: "on a resolve's path it appears as the crossing that reached an endpoint (`0101`)". §4 quotes this entry approvingly; item 13's `CONTEXT.md` list does not include it.
- `CONTEXT.md`, `closure`: "Under `0101` it is the endpoint set of a repeated crossing; the crossing's paths are wider than the set." Also absent from item 13.
- `0102`, tenth deviation row: "`applies` is never rendered as a neighbour; on a path it appears as the crossing that reached an endpoint". Item 14 lists `0102` as a pointer debt for its **membership row** only.

**Aspect mismatch.** None of the three contradicts a ruling - they are vocabulary residue, which is why this is repair and not blocking. But `reading-records.md`'s second rule is precisely that a frozen artifact's vocabulary travels with its content, and leaving three entries speaking the retired word is how the next reader inherits it.

**Verdict: REPAIR.** Add them to item 13 and item 14.

### F5 - §10 item 14's "none contradicts it" is too strong for the `0096` entry · REPAIR

**Section.** §10 item 14.

**Claim.** "...and `0096`'s clause that `has-more`'s ground holds *only where the neighbourhood cannot be listed* (a ring 0 row now lists one selected crossing of it, which §5 records as the collapse) each describe the state this record amends and none contradicts it."

**What `0096` actually says.** "Its own ground in `0092` is that *"ring 0 cannot list a node's neighbourhood, so without this field the coordinator's next call is a gamble"*, and that ground holds **only** where the neighbourhood cannot be listed. That is ring 0" - and, two paragraphs earlier, "`<neighbours>` strictly contains that set ... so a render carrying both states one fact twice, which `0024` bars."

**The mismatch.** The other thirteen entries in item 14 are stale descriptions of an amended state. This one is a **live constraint that now bites**: on a row whose progress position is non-empty, `about` is stated by `has-more` and by the shown position, which is the `0024` bar `0096` invokes by name. The draft is not wrong to park it - it is a question of *where the field appears*, which is `0096`'s own residue and is #82's - but it is a debt owed to #82, not a pointer that merely describes. §5 and §9 both call it a collapse; item 14's blanket clause is the one place that says it contradicts nothing.

**Verdict: REPAIR.** Except the `0096` entry from "none contradicts it" and say it is homed at #82 with the collapse.

### F6 - §5b cites `0097` for a rule `0096` states · REPAIR (§5b)

**Section.** §5b, *Obligation's line*.

**Claim.** "...plus whichever of `origin` and `updated_at` a neighbour's decision needs - and `0097`'s rule on a neighbour carrying another record's field is the question that decides the last part."

**What `0097` actually says.** Its three rules are: "A tag carrying an `id` is an addressable object; a tag without one is a field of the node being rendered"; "An open/close pair carries content"; "A member omits what its container already fixes." None is about a neighbour carrying another record's field.

**The record that states the claim.** `0096`, first paragraph: "`0082` had a neighbour arrive as one self-closing element carrying the target's line plus *"the link's `role`"*. That dissolves a **record into another record**: `0016` makes a relation a record rather than a field on either end, `0017` gives it a natural key ... **A field of the link cannot ride on the target and still be the link's.**"

**Aspect mismatch.** `0097` is cited for a neighbouring aspect - element shape - where `0096` is the record that rules on one record's field riding another's render. This is `reading-records.md`'s *cite the record that states the claim, not the nearest plausible one*.

**Verdict: REPAIR** (§5b is declared a draft section).

### F7 - §2's `0039` citation carries an inference `0039` does not make · REPAIR

**Section.** §2, second paragraph.

**Claim.** "`0039`'s symmetry is scoped to the set the judgment ranges over, and a judgment over paths may range over any of its positions, so the criterion applies at every node position and not only the last".

**What `0039` actually says.** "Symmetry is scoped to the set the judgment ranges over, not unconditionally to all five courses." The quotation is exact. But `0039`'s *set* is a set of **members** - five courses, eight obligations - over which one observation is or is not affordable: "observe(X) is permitted for a judgment over set S iff X is affordable for every member of S". It is not a set of path positions, and `0039` says nothing about a field-selection criterion.

**Aspect mismatch.** `0039` binds **affordability of an observation across members**; the draft uses its scoping clause to extend `0101`'s **field-selection criterion** from the endpoint to every position. The step from *members* to *positions of a path* is the draft's own. It is a good step and the ruling survives without `0039` - the same sentence gives the actual grounds, `0101`'s one-return premise for the lower bound ("one `look_at` per intermediate, which `0101`'s premise forbids") and `0043` with `0095` for the upper - but the citation as written reads as though `0039` supplied the extension.

**Verdict: REPAIR.** Mark the members-to-positions step as this record's, as §1 (ii) already does for *what a judgment ranges over*.

### F8 - §9's "#16 ... gains five readings" omits J4's wake · REPAIR

**Section.** §9, the #16 bullet.

**Claim.** "Its wake gains five readings, each a *first real decision observed by hand*: what shape the size and absorption answers took (§6); what *needing Billy* turned out to mean (§3); whether the decision turned on lecture progress (§3); whether it turned on a comment the row did not show (§3); whether an optional or a done obligation's inclusion mattered (§4)."

**What §3 also contains.** J4's cell: "Wake: the first real decision in which a same-course pair's inclusion mattered either way." That is the same shape as the five, it is in §3, and §11 carries it forward ("whether J4 ranges over same-course pairs"). It appears in neither the count nor the list.

**Verdict: REPAIR.** Make it six, or say why J4's wake is homed elsewhere.

### F9 - §3 disposes of three of #14's four buckets · REPAIR

**Section.** §0 and §3.

**Claim.** §0: "#14's evidence comment - three buckets replicating 6 of 6, a dated sequence, items owed with no date, items needing Billy - bounds what a read must supply". §3 then places buckets 1 and 2 under J1 and parks bucket 3.

**What #14's comment actually says.** Quoting `E0-RESULTS.md`: "**What does replicate is the partition, in 6 of 6:** a dated sequence · items owed with no date · items needing Billy. **A fourth, recorded open questions, appears in 4 of 6.**"

**The gap.** The draft's three-bucket figure is exact for the 6-of-6 partition and is correctly caveated. But a fourth bucket exists in the same evidence at 4 of 6 and gets no disposition anywhere in §3 - not parked, not placed, not ruled below the replication bar. `reading-records.md`: state the question a list answers before treating it as exhaustive. The draft treats the three as the whole bound without saying that the fourth was dropped for replicating at 4 of 6 rather than 6 of 6.

**Verdict: REPAIR.** One clause in §3 disposing of *recorded open questions*.

### F10 - §4's term-conflict paragraph over-promises its own analogy · REPAIR

**Section.** §4, *Why there is no predicate*.

**Claim.** "It is reported as §6 reports the `parts` conflict, and the wake below decides it."

**The mismatch.** §6's conflict is headed "A conflict between two landed records, found here and **to be repaired**", and §10 item 6 repairs `0037` row 1. The term conflict - `CONTEXT.md`'s `the line` and `0094`'s example give `course` a `term`, `0037` row 11 defers `course.offering_term` to v2 - is **not** repaired anywhere in §10; it is parked at §11 on a second term landing. The two dispositions are different, and the sentence says they are the same.

I verified the conflict itself and it is real: `CONTEXT.md` line 186 gives course's line as "`id` `name` `term`", `0094` prints `<course id="2c03" name="…" term="winter-2026">`, `0037` row 11 reads "**out for v1 because v1's boundary is coursework; deferred to v2** (`D6`)", and no record reconciles the two names. Reporting it rather than ruling it is the right call under *BLOCKED beats guessing*. Only the analogy is wrong.

**Verdict: REPAIR.** Say "reported and parked, unlike §6's, which is repaired".

### F11 - J4's cell asserts a position's contents and disclaims deriving them, in the same cell · REPAIR

**Section.** §3, J4.

**Claim.** "...with `course` on each end for the coordinator to compare, rather than over its cross-course instances alone" and, six clauses later, "What its obligation positions carry is derived for J4 and not here (§5b)."

**The tension.** The first clause states what J4's obligation positions carry; the second says that is not derived here. Both readings are defensible together - the judgment *ranges over* `course` at each end, which a later derivation would have to honour, without the field set being derived - but the cell does not say so. The same-course reading itself is stated openly with a wake and I do not touch its merits.

**Verdict: REPAIR.** Wording.

### F12 - §4 transfers `0036` across annotation kinds without marking it · REPAIR

**Section.** §4, first paragraph.

**Claim.** "`0035`'s *"one current value per target"* is read here as one record per target, edited in place, which `0028`'s per-field update and `0036`'s in-place modification support".

**What `0036` actually says.** "A `sticky_note` is an entity that points at a node rather than a property of one, so attach, detach and modify are cheap and symmetric". Its block is `sticky_note`'s: "`sticky_note := kind · id · category · body · origin · created_at · updated_at`".

**The mismatch.** `0036` speaks about `sticky_note`; the transfer to `progress` runs through `0034` (an annotation is a tag over two kinds) and `0035`'s note that `progress` "carries the same `origin`, the same timestamps". §5 marks the transfer in place - "`0036` (whose block is `sticky_note`'s, supplying `origin` and the timestamps across both annotation kinds)" - and §4 does not.

The underlying reading is well supported elsewhere: `0071` names "`retarget` is the method that broke *one current value per target*", which only makes sense if the invariant is record-level. The wake is stated. Only the §4 citation is unmarked.

**Verdict: REPAIR.**

### F13 - `0010` quoted with a parenthetical silently elided · REPAIR

**Section.** §6, *Absorption's target is a concept*.

**Claim.** "`0010` rules that surviving set-difference queries are *"structural, never personal"*".

**What `0010` actually says.** "Surviving set-difference queries are structural ("this concept has no artifact covering it"), never personal ("you never opened X")."

**The mismatch.** The quotation marks assert verbatim text that is not verbatim; the record's own example is dropped without an ellipsis. The substance is unchanged and the use is aspect-correct. The draft's convention elsewhere is consistent - italics-plus-quotes for verbatim, bare italics for paraphrase - which is what makes this one read as a verbatim claim.

**Verdict: REPAIR.** Ellipsis, or drop the quotes.

### F14 - the `optional` cell's "rendered as absence" reads against `0082`'s narrowing · REPAIR

**Section.** §5, obligation position, `optional`.

**Claim.** "a nullable bool whose null means unknown (`0031`), rendered as absence (`0028`)".

**What the records say.** `0028`: "`null` means **no record**, never a default, and must render as absence." Verbatim correct. But `0082` narrows what *absence* means at the render: "**Absence is written, never omitted.** `done_by=""` rather than a missing attribute: the reader is a token stream, so an omitted attribute is invisible rather than visibly empty."

**The mismatch.** As phrased, "rendered as absence" invites the reading `0082` exists to bar - a missing attribute. Since `optional`'s verdict is *in* either way, nothing turns on it.

**Verdict: REPAIR.** Wording.

---

## Citations checked and found sound

Quotation and attribution were checked separately, per `reading-records.md`. Every item below verified as accurate **for the aspect the draft uses it for** unless named above.

**`CONTEXT.md`.** The opening sentence as the source of J1/J2/J3 (§3). `id` - "an id says nothing about the record it names" (§5). `node`, `kind`, `Ref` (§5's field-list assembly). `origin`'s three values (§5). `parts`'s *Avoid* barring "using it to judge how much work something is" (§6). `dispatch` - "asking the owner is one case of dispatch" (§6). `applies` - "on a resolve's path it appears as the crossing that reached an endpoint" (§4). `progress` - "how far along its target's work is", correctly noted as not yet covering a concept target (§6). `the line` - `progress` needs none, and the band B transfer (§5, §10.13). `covers` as the teaching relation (§3, J3). `holder`, `routing`, `path`, `ring 0`'s derivation-owed note (§4, §10.13). **No term is used in a sense `CONTEXT.md` bars.** The only two hits from an *Avoid* sweep are "assignment" inside a verbatim quotation of `0001` and "a thing with a deadline", which is `CONTEXT.md`'s own definition of `obligation`, not *deadline* used as the noun. "row" is not a violation: `CONTEXT.md`'s own `ring 0` note says "A ring 0 row is not a line", and the draft's §5 keeps the two apart by name.

**`0001`** - the second job's "cross-course relations are modelled by the knowledge base" (J4), the third job as `0003`'s derivation source (J6), "helping model an assignment's requirements is in scope" (§3), and the first job naming no judgment of its own because "a chain that reaches the material in one return is what collapses it". All four exact and aspect-correct.

**`0003`** - `nodes_without` as the ruled instance of absence on one member (§1, J6).

**`0007`** - parking with a wake (§3).

**`0010`** - owner-authored, surface but never resolve, "a rule about the caller", the stateless opening sentence (§6). Aspect-correct; see F13 on one quotation.

**`0012`** - `about: annotation → any` (§2, §5, §6); both `requires` signatures, which is what forces J4's `[kind = obligation]` (§3); `builds-on: obligation → obligation` as the one cross-obligation relation before the concept layer (J8, with `0092` confirming); `spec`'s `role ∈ {given, owed}` and `prepares-for` (§3 candidates, J7). Every signature checked against the nine-row table.

**`0013`** - roughly-55 as ring 0's bound (§10.14).

**`0017`** - the link's fields `from · to · kind · role? · locator?` (§5b), and the link's fields being in routing's vocabulary (§8).

**`0018`** - a ref may dangle; deleting a course does not cascade; the link-set validation pass "owed and unbuilt" (§4, §10.12). The cascade table's `course` row does imply the Ref-typed reach item 12 proposes.

**`0019`** - "residency is an access policy over obligation nodes' fields" (§10.11), and the bar on a third persisted thing.

**`0024`** - one purpose per field, cited for the `has-more` collapse (§5, §5b).

**`0025`, `0026`, `0027`** - the one id space; `course.id` supplied by the material; `kind` as required discriminator (§4, §5).

**`0028`** - per-field update, `added_at` on `course` and `obligation`, annotation timestamps (§4, §5).

**`0029`** - `obligation.course` mandatory, single-valued, monomorphic (§4).

**`0031`, `0032`, `0033`** - null means unknown; the conditional-weight pointer made optional with "the narrowing must not be smoothed"; `parts` does not carry size and its replacement is "an interaction" (§5, §6).

**`0035`** - `state` on `progress` not `obligation`, with both arguments against the move; "one current value per target"; absence reads `not_started` (§4, §5). The record-level reading is stated with a wake and is corroborated by `0071`.

**`0037`** - row 1's "observed rather than stored - ordinally, from `parts` and item notes first, then by asking for a relative comparison" and "ordinal comparisons, not hour counts"; row 11's v2 deferral; rows 13 and 14 leaving term boundaries open (§4, §6, §11). The draft's refusal to treat row 1 as exhaustive on the answer's *shape*, and its explicit withdrawal of an earlier draft's ruling on that reading, is `reading-records.md` applied to the draft's own prior work.

**`0038`** - the seven; the exclusions' arguments; "excluded from the projection is not unreadable"; the roughly-55 scope clause (§4, §5, §7, §10.4).

**`0039`** - the scoping clause and the observe/dispatch formalism (§6). Aspect-correct in §6; see F7 for §2.

**`0040`** - method, not ground, transferred (§9). Matches `0100`'s own reading of it.

**`0041`** - `due` ascending, nulls last, among nulls by `done_by`, ties by the handle, never array order; the struck grouping (§9).

**`0042`** - the three triggers; "it is present, it is routable"; breadth never a defect; the importance sentence with its `grade_share` clause; the #82 permission (§4, §6, §7, §10.3). The draft's split - the importance sentence survives in `0042` while §5 declines to use it as a selection ground because `0099` declines that ground - is two different aspects handled correctly.

**`0043`, `0044`** - discard; residency in the conversation's context (§2, §4, §10.14's "`0044` reads clean", which I confirmed: nothing in `0044` fixes a field set).

**`0046`** - the own-channel sentence as a **delivery** rule (§4), with `reading-records.md`'s table and `0092`'s Considered Options both confirming. This is the draft's best-executed citation.

**`0051`, `0056`** - conflict depth; "provenance is stated prominently at every read"; `origin`'s owed write rule (§3, §5, §6, §11).

**`0061`** - "every read that returns records must return their handles" (§5).

**`0068`, `0070`, `0071`** - build the instance; capabilities not shapes; the success-path blind spot (§0, §5, §6, §11).

**`0081`** - the silence a negative answer must not leave (§2).

**`0082`** - the four rules place and do not select; the second exception covering `has-more`; a Ref-typed field is a bare pointer; `locator` "says where you land after walking"; the transfer clause **in both places it appears**, which I confirmed (lines 20 and 30); the Source line pointing at the fall26 schema (§5, §5b, §10.7).

**`0084`** - `look_at(course)` composing `obligations.list(course)` (§8).

**`0089`** - whole lines per changed obligation; "what element a ring 0 line uses is open" (§4, §9, §10.9).

**`0092`** - the value is the set of link kinds, not a boolean and not a count; the ground about ring 0 not listing a neighbourhood; band A in its opening sentence, its Considered Options and its Source line, all three correctly listed at §10.14 (§5, §5b).

**`0093`** - the ring 0 section, **two** rejected-name rows (`attention` for the band; `status`/`state` for the band), and the names row giving an edge `id`, `type` and `direction`. All three counts confirmed exactly (§10.14).

**`0094`** - the composed-section example printing `term="winter-2026"`; the closing sentence carrying the band's representation (§4, §10.14).

**`0095`** - the transfer sentence, "so *the band* is band B", "A line that picked each row's own band…", "no rule generates a new kind's line" untouched, "every endpoint is one line" (§5, §10.7). All four locations verified.

**`0096`** - the worked example printing `state`; the edge's `id` for `attach` and `detach`; `type` not `role`; the "only where the neighbourhood cannot be listed" clause (§5b, §10.7, §10.14; see F5).

**`0097`** - the self-closing line and a pointer not being content (§6). Aspect-correct there; see F6 for §5b.

**`0099`** - "`0082` places a field; it does not select one"; the `updated_at` harm quotation; the pair kept together on a joint ground; *no reader* declined as a ground; `added_at` excluded on a ground of its own (§5).

**`0100`** - the four-clause table; `0042` under admission; refresh returning "a line, whose field set is band B, which is the selection clause"; "`0042` does not itself say that ring 0 ranges over every obligation in a semester"; the refusal to widen ring 0; `0070`'s direction (§4, §5, §7, §10.5).

**`0101`** - I checked every one of the eleven occurrences of *endpoint* in the record against §10 item 2's rename list and found the list complete for that record. Also verified: "admits by what a form lets a chain produce"; "Each endpoint carries its own kind's deciding fields - one set per kind"; the affordability sentence with its ellipsis; the repair-read exclusion; "how they are banded and arranged are downstream"; the grammar sentence quoted verbatim for splitting; the `0095` citation for *one set per kind*; the spontaneity paragraph naming `has-more` as the in-band carrier; the id-space question left open for an edge's `id`; the cost statements for `REPEAT`; a judgment made *with* operations; an unserveable intent refused rather than returned empty.

**`0102`** - the membership row leaving the Ref-crossing's admission to #86 (§8, §10.14).

**Issues.** #86's unblocking comment - all four deliverables map to the sections the draft assigns them. #85's resolution - §7's forms block, the `START(ref)` spelling, "connectives as one form", the (i) provisional reading, the `nodes_without` / `covered` case, the "no crossing reaches a date" ground for `FILTER`, the `MOVE` with `Q` row, S1-S7 and each one's disposition, §8's #87 line "S1 as stated is entirely this ticket's", §10's edge-`id` and time-projection residues. #82 - the 6,482 / 7,598 measurement with its scope clause, the **two** orphans, and the *must not be re-opened* list, of which the draft correctly reports **two of four** items as moved. #84 - the acceptance standard, Billy's raw decomposition, the *sticky_note* clause, the size and absorption exclusions. #58 - the *Out of scope* line on the plan, quoted accurately as gated at #14. #14 - the 6-of-6 comment and its "it does not say the plan is those three buckets" (see F9 for the fourth bucket). #71, #16, #13, #25, #17, #19, #20, #10, #87, #88, #79 - each named for what it holds.

**Coverage sweep for §10.** I grepped every mention of *band*, *ring 0*, *endpoint*, *term* and the line's field set across `docs/adr/`, `docs/adr/README.md` and `CONTEXT.md`. Every record that mentions a band, ring 0's field set, `has-more`'s place, `state`'s home or the line's field set appears in §10: `0013`, `0018`, `0019`, `0038`, `0042`, `0046`, `0082`, `0089`, `0091`, `0092`, `0093`, `0094`, `0095`, `0096`, `0100`, `0101`, `0102`, `README.md` and `CONTEXT.md`. `0021`, `0037` row 9, `0039`, `0044`, `0081` and `0001` mention ring 0 and say nothing the draft's rulings contradict. The only gaps the sweep found are F4's three *endpoint* residues.

---

## Summary

Fourteen findings, **zero blocking and fourteen repair**. No cited record fails to support the claim it is cited for in §0-§8, and no landed record contradicts a ruling in the draft that §10 does not already list - the §10 sweep came back complete for the bands, ring 0's field set, the line's field set, `has-more`'s place, `state`'s home, what a path ends at, and what a position carries, with only three retired-vocabulary residues (F4) unlisted. The repairs cluster in three places: counts and cross-references that do not tie out (F1, F2, F8, F9), a caveat and two amendment-list omissions that weaken the record's auditability rather than its rulings (F3, F4, F5), and three citations that name a neighbouring record or an inference the record does not itself make (F6, F7, F12), of which one is in the declared draft section. The remaining four are wording. Nothing here should hold the comment; F1, F2 and F3 are the three I would fix before posting, because each is a claim about the draft's own evidence rather than about the design.
