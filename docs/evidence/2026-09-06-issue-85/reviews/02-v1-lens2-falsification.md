# Review 2 - draft v1, lens 2 (falsification)

**Reviewer:** a blind subagent (Claude Sonnet), given `drafts/v1.md`, full repository read access, `docs/agents/drafts-and-rulings.md` as the standard. Withheld: the session transcript, its reasoning, the pre-registration. Blind to the lens-1 reviewer.

**Brief, in summary:** four attacks - a judgment the four generators cannot serve; a generator wrongly admitted or excluded under §4's test run cold; derivation direction (`0100`'s diagnosis of `0038`, `0070`); scope leaks against §10 and the sibling tickets. Thresholds: blocking for an unserved must-judgment, a contradicted record, or a decision the draft says it does not make; repair otherwise; ambiguous resolves to blocking.

**Report, verbatim:**

---

Reading is complete. Axis declared before opening: the four attacks as given, records before issues, and a finding only where a draft sentence collides with a quoted record or with another draft sentence. Below is the report.

## Findings, most severe first

**1. `blocking` (attack 1, attack 4). §6: "a ring 0 row **is** a line" and "select 〈the line's fields〉".**
Collides with three landed records and decides #86's selection content while §10 says it does not.
- `0038`: band A is `course · name · due · state · optional · done_by · has-more`; band B drops the last three. `0082` (repaired at #80): obligation's line is band B. So a band A row carries three fields no line carries.
- `0096`: has-more "survives **only** where the neighbourhood cannot be listed, and that is ring 0"; `0082`: "`has-more` is **not** on the line". A ring 0 row carries what the line by ruling does not.
- `CONTEXT.md` *the line*: "Per kind it is **one** field set that does not vary per row." If a row is a line, selection is fixed to band B and #86 has nothing left to decide on selection; if selection is #86's (§10), a row is not a line. The draft asserts both.

**2. `blocking` (attack 1; attack 3 for its cause). §6: ring 0 is "one standing routing result" with intent "obligation where 〈admission〉, select …, order by `due`", and `0021`'s time projection is "another standing routing result". Neither intent is in the domain §2 defines.**
§2: the intent vocabulary is "kind, link kind, direction, field = value"; the only unanchored predicate generator is `(kind, field = value)`. `0042`'s admission is `due ∈ [today-7d, today+14d] OR done_by ∈ [...] OR state == in_progress`: two range predicates and a disjunction. `0021`'s projection is "query-by-time-period": a range. No generator expresses a range, no composition operator is defined for union, and no generator projects or orders. §2 itself says `0043` bars assembling. So under the draft's own test, a range/disjunction generator satisfies (a) and (b) and is missing from the list, or else ring 0 and the time projection are not routing results. Cause (attack 3): §6 reads "predicate, projection, order, refresh" off `0100`'s clause table and fits the query to it (`0100`: "not claimed to be exhaustive"); §2's algebra has no projection or order because they were never derived from §1. That is the `0038` move on a different artifact.

**3. `blocking` (attack 1, attack 2). §2 "closed under composition" and §7 S5 "filter ∘ one-hop ∘ absence, one call": composition is never defined, and the absence generator's admission flips on the definition.**
S5 needs the concepts reached by one-hop from band-A obligations *restricted to* those with no covering artifact. The absence generator is unanchored, "(kind, link kind, direction)", scanning a layer. Restricting requires either intersection with the one-hop result, or an anchored absence predicate per element. Neither is one of the four. Two branches, both break a ruling: (i) if set operations count as composition, then `absence(concept, covers, pointed-by)` = `filter(concept)` minus the flat-map of `one-hop(covers, points-at)` over `filter(artifact)`, so absence fails clause (a) and §4's "The test generates all four" and #84's charting check ("The routing test must generate it") are false; (ii) if set operations do not count, S5 is unserved by any composition and `0043` bars assembling it, which is the blocking threshold verbatim. Ambiguous resolves to blocking.

**4. `blocking` (attack 2). §4 clause (b) has no stated criterion and the draft applies it both ways.**
Transitive is admitted because "N one-hops, and `0043` bars holding them". §7 S1 says the opposite for the same mechanism: "two `look_at` calls … holding an id between calls is a handle, not depth." A closure by repeated one-hops holds only ids (a frontier), which S1's reading permits. `0043`'s text is "what is fetched is rendered, used and dropped, never accumulated"; it draws no line between an id and a render. Under S1's reading transitive fails (b) and, in the draft's own words, "Without (b) the transitive generator falls out." The test that is deliverable 3 cannot be applied as written.

**5. `blocking` (attack 2). §4 clause (a) is applied over a different universe for the exclusion than for two admissions; and §8 labels a ruled record a defect.**
The wildcard is excluded because "`look_at`'s `<neighbours>`" serves it (§2: "one fact under two names (`0024`)"). Fetch is not a generator, so this is not clause (a)'s wording; it is a `0024` argument. Applied uniformly: anchored one-hop's cited judgment ("which of X's neighbours are worth a look") is served by `look_at(X)`'s `<neighbours>`, a superset (`0096`); unanchored filter's cited judgment ("which obligations are in course C") is served by `look_at(course)`'s composed section, ruled at `0084`. Either fetch counts in (a) and both rows lose their judgment, or it does not and the wildcard exclusion is ungrounded. §8 then calls `0084`'s composition "the first leak the test would have caught" while `0084` is ruled ("So `look_at(course)` composes `obligations.list(course)`") and §9 does not amend it.

**6. `blocking` (attack 2, attack 4). §4 exclusion table, by-content row: "who serves it: dispatch, by `0046`".**
The test as worded has no "over the skeleton" precondition; Billy's S1 ("which lecture was it mentioned in") is a judgment the coordinator must make, no composition of generators resolves it, and it cannot be assembled, so by the test's own clauses it passes. The exclusion rests on an unstated precondition. The cell also decides #87: `0046` says "does not search the corpus"; it names no dispatch. The dispatch route is `0039`'s, and only under its affordability formalism. #87's body: "Three records meet at that step and none of them decides ownership." §8 says "who calls a by-query one" stays #87's; §4 has already answered dispatch. Decides what it says it does not.

**7. `blocking` (attack 4, attack 3). §9.1 rewrites `0001` beyond the map's authorization and removes the derivation the absence generator stands on.**
#84 "What this map is authorised to overturn" names `0042` only. The rewrite demotes job 3 to "too vague to be an objective and survives only as what `0081` and the absence generator serve" and re-grounds `0003` on `0081`. `0081` is a rule about a negative answer to a question that was asked naming its boundary ("not held from not found"); job 3 is about what was not asked. §4's absence row cites exactly this misread: "`0081` requires the negative to be stateable." #84's charting comment: `nodes_without` "is derived top-down from `0001`'s job 3, so it lacks a surface and not a derivation." The draft strikes that derivation and leaves absence grounded circularly (job 3 exists as what absence serves; absence is generated by a record that does not say so). `0100` also grounds its grouping defect on job 2 ("manage cross-course information in the background"); the rewrite recasts job 2 as "not an activity the system performs" without checking what that does to `0100`'s ground.

**8. `blocking` (attack 4, attack 3). §2's parameter tuples, §4's "signature for signature", and "both are covered as generators" decide shapes and #88's coverage, which §10 and §4 say are not decided.**
§10: "Any generator's shape or spelling (`0070`)" is not decided. §2 gives each generator a parameter tuple; §4 declares `nodes_without` "the absence generator, signature for signature" and `closure` "the transitive generator". A parameter signature copied from a function signature is a shape. #88's question is "Does the derived capability list cover `closure` and `nodes_without`"; the draft answers yes for both and leaves #88 only the name. And the "landed as" column is the bottom-up move: the four generators are one-for-one `0046`, `0084`, `0003`, `0013`, then the test is run to confirm them. #88's own body: "asking it first would derive the surface from two reads that happen to exist, which is the bottom-up move `0100` diagnosed in `0038`."

**9. `repair` (attack 2). §2: "ring 0 … is a set of lines and not a node, so it is necessarily unanchored."**
Every line carries an `id` (`0096`'s example; `0025`: "every read that returns records must return their ids"), so an intent formed from a ring 0 row can be anchored. The inference is false; the conclusion survives on S3 and `0084`.

**10. `repair` (attack 1). §7 S1 answers coverage, Billy asked for mention.**
`CONTEXT.md` `covers`, _Avoid_: "using `covers` for a mention - full-text finds mention, title-scoped finds coverage"; `applies` "is never rendered". The step "concept X `covers`⁻¹→ artifact" does not resolve "which lecture was it *mentioned* in". "none in routing" is a finding about a different question; the scenario as stated is by-content whole, not "only on their content half" (§8).

**11. `repair` (attack 1). Anchored transitive or one-hop over `applies` returns `<edge type="applies">` lines (§3), and `CONTEXT.md` `applies` is "never rendered".**
Either the domain carries a restriction the draft does not state, or the term needs repair; neither appears in §9.

**12. `repair` (attack 4). §2: "An anchored intent may be anchored on an edge" is vacuous under the draft's own generators.**
One-hop and transitive follow a link kind from the source; a link is "between two refs" and a node is "anything that can be an endpoint of a link" (`CONTEXT.md`), so an edge has no link kinds to follow. Drop it, or re-home it with the edge-id-space item it already points at.

**13. `repair` (attack 4). §6 "arrangement is its order" versus §9.4 re-homing `0041`'s grouping to #86 "as the standing query's arrangement".**
`0100`: arrangement is order ruled plus grouping open. The draft says both in one comment.

**14. `repair` (attack 1). §1 says routing returns "the addresses that satisfy it"; §3 says "Routing returns lines".**
A line is a render carrying an address. One of the two sentences is wrong as written.

**15. `repair` (attack 4). §9 items 1, 2 and 4 are marked "authorized at #85" while item 6 is "proposed and not authorized".**
An agent draft choosing which of its own amendments Billy has authorized is the self-lock `docs/agents/drafts-and-rulings.md` bars. All six are proposals until the comment is posted.

**16. `repair` (attack 3). §7 S3-S5 are constructed one per generator.**
#85 method step 3: "Scenarios are test cases, not the spec." Test cases written from the answer cannot evidence that "the test generates all four"; S4 is `0010`'s own example verbatim. Third instance of the pattern the draft says it avoided (with findings 2 and 8).

**17. `repair` (attack 4). §6 "The patch dissolves into #66" and "its holder question is #66's unchanged".**
#84 licenses dissolving if the lens is removed, so the dissolve is in scope; but #84 places the patch "upstream of #66 rather than parked there", and #66's question is whether faithfulness spans a second holder, not whether a layer exists. The residue is mislocated.

## What did not break, per attack

1. **Judgments the generators cannot serve.** Every anchored judgment over a single link kind (`requires`, `covers`⁻¹, `builds-on`, `part-of`, `prepares-for`), every filter reachable through an annotation via `about` composition (in-progress obligations, noted obligations), and every structural absence resolve under a pipeline reading of composition; `0010`'s structural-never-personal line holds for all of them.
2. **Wrong admission or exclusion.** Filter's clause (a) over generators alone holds (`0016`, `0029`: no hop reaches a course's obligations); the wildcard verdict is defensible on `0024` even though the draft's test does not state that ground; by-content genuinely cannot be composed from the four.
3. **Derivation direction.** §1's boundary ruling (system holds resolve, coordinator holds intent) is argued from `0010` and `0046`, not from an artifact; §5's deviation table is quotation-accurate against `0017`, `0018`, `0019`, `0021`, `0029`, `0062`; §1's "mechanistic reachability is the schema's" is consistent with `0012`.
4. **Scope leaks.** Ruling #16's second test is inside #85's stated scope (body item 1); #82's render, #14's representation and #66's wake are untouched; `0062`'s repair is the repair-at-source practice `0084` set for `0029`.
