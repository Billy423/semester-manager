# Review 3 - draft v2, lens 1 (attribution)

**Reviewer:** a fresh blind subagent, given `drafts/v2.md`, full repository read access, and `docs/agents/reading-records.md` as the discipline. Withheld: the session transcript, its reasoning, the pre-registration, reviews 1-2. Blind to the lens-2 reviewer.

**Report, verbatim:**

---

## Method

Every `NNNN` record, every `CONTEXT.md` entry and every `#n` issue the draft cites was opened and read whole (bodies and comments for issues). For each citation I checked, separately: (1) the quotation, where there is one; (2) the attribution - whether the record actually states the claim it is attached to; (3) the aspect - whether the record speaks about the thing the draft is deciding, per the four-row table in `reading-records.md`; (4) the number, where one is taken from a record. I then grepped `docs/adr/` for `band` and `ring 0` to find landed records the draft's §7 dissolution reaches that §10 does not list. The six session rulings and the three-position-to-two-position reshaping are treated as ruled.

Findings are ordered most severe first. Verdicts: BLOCKING under threshold (a) or (c); REPAIR otherwise.

## Findings

### F1 - `0095`'s band-B sentence contradicts §5's line ruling and is not in §10 - BLOCKING (c)

**Draft, §5 and §10 item 7.** *"obligation's line is the row's field set minus `has-more`"*, to be recorded in the new record and written into `0082`'s transfer clause; `0095` gets one sentence, the one about `progress`'s line being *"the first line derived under `0101`'s criterion"*.

**`0095`, its own paragraph, verbatim:** *"What **is** decided: a line is **one** field set per kind and does not vary per row. `0082` calls obligation's line "ring 0's band plus `has-more`", and band A already carries `has-more`, so *the band* is band B. A line that picked each row's own band would import `0038`'s **residency** computation into a **read**."* And earlier in the same record: *"`0082` sets obligation's line by a **transfer** - `0038` chose that field set for **residency**"*.

**Mismatch.** Under §5 the line is `id · kind · name · due · done_by · optional · course` (plus `state` at position 2, however a block carries it) - seven-plus fields. Band B is `course · name · due · state` - four. `0095`'s *"the band is band B"* is a ruling on the line's field set, not a pointer, and it is contradicted outright once band B dissolves (§7). §10 item 7 amends `0095` for a different sentence; item 13's pointer-debt list names `0091`, `0092`'s Source line, `0093`'s ring 0 section and `0094`'s closing sentence, and not `0095`. So a ruling in the draft contradicts a landed record's own ruling and neither the repair list nor the debt list carries it. The fix is one more sentence in item 7; the omission is what makes it blocking, not the size of the repair.

### F2 - `0035` cited for *"a non-obligation target"* when it says *no target* - REPAIR

**Draft, §6.** *"Absorption is of a concept, so its record is a `progress` on a `concept` node - `0012`'s `about` signature admits any target, and `0035`'s *progress on a free topic* already contemplates a non-obligation target."*

**`0035`, verbatim:** *"no `about` link is legal -> means progress on a free topic named in `detail`"*.

**Mismatch (attribution, not quotation).** `0035`'s free topic is a `progress` record with **no `about` link at all**, its subject named in free text. That is not a non-obligation target; it is no target. The claim survives on `0012` alone (`about`: `annotation → any`), so nothing is lost by dropping the `0035` clause - but as written the record is cited for an aspect it does not speak about. Not blocking because paragraph two parks the observation's shape rather than ruling it, and §9's proposed #25 comment carries the claim as a derivation; if the caller reads *"its record is a `progress` on a `concept` node"* as ruled, this rises to (a).

### F3 - `0100`'s doubt quoted with its scope cut off, then declared settled by `0042` - REPAIR

**Draft, §4.** *"its own sentence that "`0042` does not itself say that ring 0 ranges over every obligation" was a doubt about the range, which `0042`'s "it is present, it is routable" settles."*

**`0100`, verbatim:** *"**`0042` does not itself say that ring 0 ranges over every obligation in a semester**; the nearest statement is `CONTEXT.md`'s `obligation` entry, "the same nodes ring 0 is a projection of", and `0038`'s sizing figure rests on that premise without citing anything."*

**Mismatch.** The quotation drops *"in a semester"*, which is precisely the scope the draft's own predicate (`term = current`) is about. `0042`'s *"it is present, it is routable"* is said of *an undated obligation* and settles that undated rows enter; it says nothing about which term's obligations ring 0 ranges over, so it does not settle what `0100` doubted. The range is ruled in session (two-position intent over every obligation of the current term), so no ruling rests on this; the sentence should quote `0100` whole and attribute the settlement to Billy's session account (§7's *"ring 0 was assumed to hold every obligation"*), not to `0042`.

### F4 - `0005` is the store's record, used for the skeleton's term scope - REPAIR

**Draft, §4.** *"`0005` rules the store accumulates and is never synced, so nothing confines the skeleton to one term; a bare `START(obligation)` ranges over every term ever landed."*

**`0005`, title and body:** *"The store accumulates; it is never synchronised against a source"* / *"it is a knowledge base that accumulates: things enter, stale or wrong things leave"*.

**Mismatch (aspect).** The title names the store; `CONTEXT.md` keeps store and skeleton strictly apart. The body's *"knowledge base that accumulates"* is the sentence that reaches the skeleton, and even that says nothing about terms - the inference *"nothing confines the skeleton to one term"* is the draft's, not the record's. Cite the body sentence and own the inference. The predicate itself is ruled in session; only the ground is mis-hung.

### F5 - `0089`'s *trigger* is not a date - REPAIR

**Draft, §4.** *"compared to the current term, a value the system holds the way it holds today's date for `0042`'s triggers and `0089`'s trigger."*

**`0089`:** *"`0044` already states the behaviour without saying who triggers it ... and this record supplies the trigger."* `0101`: *"the coordinator only triggers its re-execution (`0089`'s trigger for `refresh()`)"*.

**Mismatch.** `0089`'s trigger is the coordinator's call of `refresh()`; no date is held for it. `0042`'s triggers do use *today*. Drop `0089` from the analogy.

### F6 - `0018`'s owed pass is the *link-set* validation pass; the draft has it repairing a field ref - REPAIR

**Draft, §4 and §11.** *"a dangling `course` ref is a defect the design tolerates by `0018` and the validation pass that record owes repairs"*; *"the validation pass that finds a dangling `course` ref (`0018`)"*.

**`0018`, verbatim:** *"A dangling ref is legal and is recovered by the link-set validation pass, which is **owed and unbuilt**."* Its cascade table does contemplate *"delete `course` -> its obligations survive"*.

**Mismatch (scope).** `obligation.course` is a Ref-typed **field** (`0029`), not a link. `0018` names the pass over the link set and does not say it reaches field refs, though its cascade row implies the case exists. The tolerance half of the ruling is `0018`'s; the repair half is an extension the draft should state as one (*"the pass `0018` owes, extended to Ref-typed fields"*) rather than attribute.

### F7 - `0010` and the `mastery` *Avoid* read as already excluding owner-authored absorption - REPAIR

**Draft, §6.** *"That is owner-authored, which `0010` permits, and it is not the *mastery* `progress`'s *Avoid* list bars, which is the system inferring it."*

**`0010`, verbatim:** *"The modelling layer records no state about the owner: it presents concepts and leaves judgment to him ... An agent may surface a progress claim for confirmation but may never resolve one."* **`CONTEXT.md`, `progress` *Avoid*:** *"completion · mastery · a `sticky_note.category` value"* - unqualified. **#84 body:** *"**absorption** (`mastery` is on `progress`'s `_Avoid_` list, and `concept`'s `_Avoid_` list bars "a thing the student understands or does not" as a retracted definition). Both were deferred rather than overlooked"* and travel with the overturn permission.

**Mismatch.** `0010` permits owner authorship only by implication (the surface-for-confirmation sentence); its first sentence, that the modelling layer *records no state about the owner*, is the nearest text to a bar on a `progress` sitting on a `concept` node, and the draft does not meet it. The glossary's `mastery` is not qualified as *system-inferred*; that qualifier is `0010`'s title, imported. #84 records that absorption is unfrozen **by the permission**, which is the honest ground: say the permission is what opens the door, not that the door was never shut.

### F8 - `0089` returns *lines*; under §5 what it returns is a *row* - REPAIR

**Draft, §4 and §5.** Refresh reports *"a change to that obligation's row"*; *"Row and line are two things, and only one of them carries `has-more`"*; §10 item 8 gives `0089` one pointer, on the progress position.

**`0089`, verbatim:** *"What `refresh()` returns is a whole **line** per changed obligation, plus an explicit marker for a row that is gone."* `0100`: *"what a refresh **returns** is a line, whose field set is band B"*.

**Mismatch.** Once row and line are distinguished and only the row carries `has-more`, `0089`'s *line* names the wrong object: a refresh that returned lines would drop `has-more` from the resident rows. `0089` is in §10, so this is not (c), but item 8's pointer should say what the return is now called, and `0100`'s refresh paragraph (item 5) should not stop at *"whose field set is the row's"* while the noun stays *line*.

### F9 - `0082` carries the transfer in two places; item 7 repairs one sentence - REPAIR

`0082` states the transfer twice: *"What survives is the transfer itself - obligation's line is ring 0's **band B** field set"* and, in its closing paragraph, *"obligation's line is ring 0's band by a **transfer of the field set, not of a render**: `0038` chose that field set for residency"*. §10 item 7 says *"one sentence each"*. Both need the repair, or the second stays quotable against the first.

### F10 - pointer debt in `0092` and `0093` is wider than item 13 names - REPAIR

Item 13 lists *"`0092`'s Source line"* and *"`0093`'s ring 0 section"*. `0092`'s body opens *"`0038` puts `has-more` among band A's routing fields"* and its Considered Options has *"shipping band A with six fields"*; `0093`'s rejected-names table has two rows *"for the band"*. Same class of debt, same fix; list the whole record rather than one line of it so a reader arriving by quotation is not told the debt is narrower than it is.

### F11 - `0101` paraphrased with the draft's own amendment - REPAIR

§7: *"`0101`: each position carries its own kind's deciding fields, one set per kind"*. `0101` says *"Each endpoint carries its own kind's deciding fields - one set per kind (`0095`)"*. §2 amends *endpoint* to *position* and §10 item 2 lists it; §7 should quote the record as it stands and say *as amended at §2*. Same in §8: *"`0101` names the crossing in either direction as one form"* - `0101` names Ref-typed fields *"in either direction"* as crossable relations and never uses *form* for it; the one-form reading is #85 §7's `MOVE(field, D)` line.

### F12 - `0012` *"three further routes"* is a count the record does not state - REPAIR

§3: *"`0012` gives three further routes from an obligation to an artifact"*. `0012`'s table has two rows joining obligation and artifact directly - `spec` (`obligation → artifact`, `role ∈ {given, owed}`) and `prepares-for` (`artifact → obligation`). Three is reachable only by counting `spec`'s two roles as two routes, or by counting the two-crossing route through `concept`. State the enumeration; a reader cannot re-derive *three* from the table.

### F13 - §10 item 5 says *three places* and lists four - REPAIR

*"`0100`, three places"*: the relabel of `0042`; the admission and selection rows of the clause table; the refresh paragraph; the *not settled* standing. Four edits, or state which two are one.

### F14 - J5 is missing from §3's table - REPAIR

The table runs J0, J1, J2, J3, J4, J6, J7. Nothing explains the gap, and *"S5 is J1 · J2 · J6 composed"* later reads as if a J5 once existed. Renumber, or say what J5 was and where it went.

### F15 - *note* used bare for `sticky_note` - REPAIR (glossary *Avoid*)

§6: *"so a note **fails** the constraint"*. `CONTEXT.md`, `sticky_note` *Avoid*: *"*note* (bare)"*; `annotation` *Avoid*: *"*note* used for both kinds"*. Write `sticky_note`. (The glossary's own `render test` entry uses *note* bare, so the term has precedent inside the glossary; the *Avoid* still stands.) No other *Avoid* term is used with the barred sense: *row* is the glossary's own word for a ring 0 row and the draft keeps it distinct from *line*; *edge* appears only as the surface element `<edge>`; *the projection* is never bare.

### F16 - #71 is open on `state`'s residence and §4 rests on `0035` without naming it - REPAIR

§4: *"`state` ... is a field of `progress`, not of `obligation`, by `0035`, which is also the record that bars copying it onto the obligation"*. `0035` does argue that (*"two records would be free to drift apart, and one cannot"*), but #58's comment of 2026-09-01 opened **#71, *whether `state` moves onto `obligation`***, and #58's Out of scope keeps it live. The draft's position-2 derivation depends on `0035`'s placement holding; §11 should list #71 as a wake that would re-type position 2, since `0035` is the sole ground and an open ticket sits on it.

## Citations checked and found sound

Listed by section, with the aspect verified in brackets where the check was non-trivial.

- **Paragraphs 1-3.** #86 body (the four deliverables, #85 §7 as draft input) · #85 resolution (§7's three provisional answers, *"connectives as one form"*, S1-S7, `MOVE` with `Q`, `MOVE(field, D)` verdicts) · `0018` (a ref may dangle) · `0090` (`land()` is blind) · `0001` (the requirements sentence) · `0038` (seven fields; `state` among them).
- **§0.** #58 Out of scope (the plan, gated at #14) · #14's evidence comment (6 of 6, three buckets, *"the buckets are real; the labels are noise"*) · #84 body (the scoping point carried into #86; *"exposes every necessary operation ... never a workflow per imagined scenario"* as the map's acceptance standard; the raw decomposition incl. lecture progress and absorption) · `0070` [capabilities, not shapes - the aspect #82 and #84 both use it for].
- **§1.** `0101` (*"admits by what a form lets a chain produce"*; *"a judgment across obligations is a judgment about their relations"*; affordability separate; the test's instrument standing; one-return premise) · `0003` (set difference = no link of the kind in the direction) · #85 §7 (`FILTER` admitted on *"no crossing reaches a date"*; `nodes_without` as `START · FILTER(not exists(MOVE))`; #88's *covered* disposition removing `exists`'s ground) · #88 comment (same).
- **§2.** `CONTEXT.md` opening sentence · `0081` [negative answer names its boundary - used for the silence an optional crossing avoids] · `faithfulness` entry (omission axis) · `0012` (`about`: `annotation → any`; `spec` `role`) · `0039` (symmetry scoped to the judgment's set) · `0043` · `0095` (a line carries no content; one field set per kind, one ruling per kind) · `CONTEXT.md` `the line` (course's `id name term`; the #17/#19/#20 debt; `progress` needs none as a neighbour) · `0017` (`role` a `Link` field) · `0096` (edge carries `id`, `type`, `direction`) · `0082` (*"says where you land after walking, which does not bear on whether to walk"*).
- **§3.** `0001` as rewritten (jobs 2 and 3; the requirements sentence) · `0100` (*"a statement about relations across obligations"* as job 2's ground) · `CONTEXT.md` `covers` (the teaching relation) · #25 (no concept writer yet) · `0041` (nulls last) · `0042` (*"it is present, it is routable"* - for the undated case, see F3 for the scope) · `0051` (deep conflict asks first) · #10 (asking) · `0056` (asked answer kept) · `0010` (surface, never resolve) · #16 wake (first real decision, observed by hand) · `0021` (coarse grouping not modelled) · `0007`.
- **§4.** `0101` (*"somewhere to stand"*; ring 0 one result held by policy; a predicate may contain a chain; a judgment made *with* operations; width unruled; time projection a result) · `0035` (one current value per target; the *why `state` sits on `progress`* heading and the drift ground) · `0082` (defaulted `progress` carries no `id`; a `Ref`-typed field is a bare pointer answering *which one*) · `0026` · `0029` (mandatory) · `0018` cascade table · `0090` · `0037` rows 13 and 14 (term boundaries open) · `0046` [delivery rule; `reading-records.md` row 3 names the scope misreading] · `CONTEXT.md` `applies` (on a resolve's path, the crossing that reached an endpoint) · `0100` (admission = *which rows enter*; refresh returns band B, *"which is the selection clause"*) · `0038` scope clause on the 55 · `0089` (whole lines per changed obligation).
- **§5.** `0027` · `0028` (`added_at` on course/obligation; `created_at`/`updated_at` on annotations) · `0029` · `0032` · `0033` · `0037` · `0038` (`optional`, `done_by`, `parts` exclusion ground) · `0036` · `CONTEXT.md` `origin` · `0082` (`id` and `kind` address; second exception for `has-more`) · `CONTEXT.md` `id` (*says nothing about the record it names*) · `0101` spontaneity paragraph (`has-more` in-band) · `0092` (value) · `0096` (survives only where the neighbourhood cannot be listed; the worked example's `state` attribute; `has-more` off the line) · `0099` (`added_at` about the row; the January-answer harm, carried from schema.md) · `0056` (*"stated prominently at every read"*) · `0070` · `0100` (`0038` filtered, not derived) · `0082` as repaired at #80 (`has-more` not on the line). Count check: `0038`'s seven minus `state` plus `id` and `kind` = the eight-item row; correct.
- **§6.** `0039` formalism · `0042` importance sentence and *"the sentence most likely to move"* · #82 ruling (overturn permission; size and absorption travel with it) · `0033` (*"an interaction"*) · `0056` · `CONTEXT.md` rigidity rule · `0037` row 1 (*"ordinal comparisons, not hour counts"*; *"from `parts` and item notes first"*) · `0033` (*"does not carry size"*) · `CONTEXT.md` `parts` *Avoid* - the conflict §6 reports is real and both quotations verify · #14 (*"the plan is where that judgment gets written down, or nowhere"*) · `0068`.
- **§7.** `0042` (the uniform-depth defence; three triggers; breadth never a defect; the permission does not reach the triggers' correctness) · `0043` · `0101` output type (one set per kind) - see F11 for the noun.
- **§8.** `0102` membership row (*"whether the crossing is admitted is #86's"*) · #85 §7 (`MOVE` with `Q`; S7) · `0017` (`locator`).
- **§9.** `0041` order clause verbatim · `0100` (`0040`'s method transfers, not its ground; `0041` and `reload` never read together) · #58 comment of 2026-09-03 (the two orphans #82 carries) · #85 §8 (#79 blocked on #86-#88; #87's whole = S1 as stated).
- **§10.** `0019` (*"residency is an access policy over obligation nodes' fields"*) · `0091` (*"Ring 0 carries the band"*) · `0092` Source line · `0093` ring 0 section (*"band A and band B are ordinary words"*) · `0094` closing sentence · #82 comment (*"Owed, not done"* precedent).
- **Numbers.** Six session rulings (counted in paragraph two: six) · 6 of 6 (#14) · roughly 55 with `0038`'s scope clause and the fall26 caveat, stated · `0037` sixteen-plus-four rows, rows 1, 13, 14 as cited · three type rulings in §2 · three formalisation questions plus a fourth · seven scenarios S1-S7.

## Summary

One BLOCKING finding: `0095`'s own ruling that obligation's line *is* band B contradicts §5's line ruling, and `0095` is in §10 for a different sentence and absent from the pointer-debt list (F1). Fifteen REPAIR findings, none of which moves a ruling: two mis-hung attributions on the absorption paragraph (F2, F7), a truncated `0100` quotation that overstates what `0042` settles (F3), an aspect stretch on `0005` (F4), `0089`'s trigger mistaken for a held date (F5), `0018`'s link-set pass extended to a field ref without saying so (F6), `0089`'s *line* noun left standing against the row/line distinction (F8), incomplete repair and debt lists on `0082`, `0092` and `0093` (F9, F10), `0101` paraphrased as already amended (F11), three unsupported or wrong counts (F12, F13, F14), one *Avoid* term (F15), and an open ticket (#71) sitting under `0035`'s load-bearing use that §11 does not name (F16). Every quotation the draft marks as one verified against its source; the defects are attributions, scopes and counts, which is the class `reading-records.md` says a quotation check will not find.
