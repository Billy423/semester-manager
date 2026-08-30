# 12 - the archive sweep

**What this pass is.** `records/archive/` is the last unread directory in the fall26 corpus. It is explicitly frozen and presumed superseded. The only question asked here is whether anything **live** was buried in it by accident: a ruling that exists nowhere else, an open question never re-homed, a reason a live record leans on but does not restate, a broken citation, or a contradiction with a standing record. This is deliberately **not** an inventory of the archive.

**Read in full, all four files:**

- `/Users/billywu/Documents/Projects/fall26/records/archive/build-plan-2026-08-27.md` (497 lines)
- `/Users/billywu/Documents/Projects/fall26/records/archive/changelog-2026-08-24-slice-1.md` (416 lines)
- `/Users/billywu/Documents/Projects/fall26/records/archive/slice-1-plan-2026-08-27.md` (169 lines)
- `/Users/billywu/Documents/Projects/fall26/records/archive/openclaw-registry-2026-08-25.md` (86 lines)

**Read to check carriage, all ten files:** `records/domain/{domain-design,model}.md` · `records/spec/{architecture,design,ring-0,schema,write-rules}.md` · `records/plan/{application-tier,backlog,write-rules}.md`.

**Boundary observed.** No `evidence/`, no openclaw path, no other repository. **One qualification that matters and is carried through every claim below:** `records/findings/` was outside the boundary. It holds two files, `read-cycle.md` and `ingestion-probe.md` (filenames only; contents not read). Every registry entry whose ref points at a `FINDINGS.md` therefore has a plausible live home I could not check, and I have marked those cases rather than calling them uncarried. Branch: `design/course-level`; `records/` is identical to `main`.

---

## Live material found

**Four items. One of them is a ruling with no live statement anywhere; the other three are open questions and a load-bearing reason. This is a small result and it should be read as a small result.**

### L1. The non-overlap rule - the ruling's only statement is here, and three live records depend on it by reference

`archive/changelog-2026-08-24-slice-1.md` §16.1, Billy 2026-08-25, verbatim:

> 这里所有 schema 的设计都要保证**目的唯一**，毕竟到时候真正实用的时候是 agent 根据 **definition** 操作，而不是"我想这个信息去那里"。就像 **tool definition 一样（non-overlapping definition）**，我们暴露的 verb 和 schema 都各施其职。

Also indexed at `archive/openclaw-registry-2026-08-25.md` entry 80, whose ref points into openclaw.

**What I checked.** `spec/schema.md` §7 invokes it by name in the `obligation.notes` graveyard row (*"Not carried, under the non-overlap rule"*) and states its **application** without stating the rule. `plan/write-rules.md` §1 cites *"`records/archive/changelog-2026-08-24-slice-1.md` §16.1's non-overlap rule"* as the reason the four write rules must be answered in one session, and §7 c2 makes an overlap check an acceptance criterion against it. `spec/write-rules.md` inherits that criterion. Nothing in `domain/`, `spec/` or `plan/` states the rule itself. It is not a measurement, so `findings/` is not a plausible home for it.

**Why it is live rather than a copy.** It is the authority under which a field was deleted, under which `progress.source` and `sticky_note.origin` were merged, and under which two of the four owed write rules are still gated. Three live records cite it; all three cite it **into the frozen archive**.

**Destination: `docs/adr/`, slug `non-overlapping-field-and-verb-definitions`.** All three tests hold. Hard to reverse - reversing it re-admits a catch-all free-text field and re-opens the six purposes `obligation.notes` was carrying. Surprising without context - "every field and verb has exactly one purpose" reads as a style preference until you know it comes from how an agent routes off definitions. The result of a real trade-off - the alternative on the table was a negatively defined free-text field, and its cost was measured across 22 rows.

### L2. The paused verb-shaping question - its statement exists only here, and both live pointers are slots

`archive/slice-1-plan-2026-08-27.md` §2, **[R]** Billy 2026-08-24: *"这个问题需要细致讨论，我目前无法给出定论。"* The question, stated there so it would survive a compact:

> Should the ring-0 verb surface be shaped so an allocation procedure can consume it - grouping by course, putting comparable quantities on the same footing - or should the verbs do faithful read-back only and leave every allocation semantic to a procedure outside them?

**What I checked.** `spec/design.md` §7 item 2 carries *"Verb shaping. §3.6 separates reading as a concern but does not shape it, and the shaping itself is presentation tier. Owner: the user."* - a slot with the question removed. `plan/write-rules.md` §8 carries *"The paused verb-shaping question (`slice-1.md` §2) - Billy's, and not touched by anything here"* - a pointer to a filename that does not exist (see C3). No live record states the question, the agent recommendation, or either supporting argument.

**Two of Billy's 2026-08-30 rulings bear on it, and neither closes it.** Ruling 2 (*`grade_share` is reference only, never an input*) settles the archive's **independent** argument outright: the archive cites `openclaw:fall26/2026-08-24-slice-1-write/workspace/INPUTS-2026-08-24.md` §4.3 for *if allocation weights by `grade_share`, it is doing arithmetic on a number Billy has described as approximate*. That is now ruled rather than argued, and it removes the motive for allocation-shaped verbs. `architecture.md` §5 changes the frame again - the surface is one composable grammar, not N description-routed verbs - which the archive's phrasing predates. The question of whether the surface owes an allocation procedure a consumable shape is still unanswered.

**Destination: deferral issue.** Precondition that wakes it: the presentation cycle opening, or an allocation procedure acquiring a reader. Carry the question's text verbatim and carry ruling 2 alongside it, so whoever picks it up does not re-derive the `grade_share` branch.

### L3. The `parts` fuzzy-find reader - a live record states as settled what the archive marks as an unruled proposal

`spec/write-rules.md` §3.4 (live, Billy-ruled 2026-08-28) states: *"Two readers, and they pull the same way: the coordinator learns which concepts an obligation contains without opening anything, and the whole corpus's `parts` is the surface a corpus-wide fuzzy find would run over."*

The second reader's only statement is `archive/changelog-2026-08-24-slice-1.md` §14.6, where it is Billy's own proposal and is marked **`[intuition / proposal - needs a ruling, because it adds a row to a ruled table]`**. Four things live only there:

- Why it needs a ruling: `domain/model.md` §5's revised access table has exactly three levels (skeleton read ✅ · store by-handle ❌ · store by-query ❌). Fuzzy addressing **inside** the skeleton is a fourth, and nothing in `domain/`, `spec/` or `plan/` acknowledges it.
- Why it is on the permitted side of the purity cut: a vector search over names and parts returns **node identities**, not content, which is the cut's own criterion (*the coordinator sees what a node IS; it never sees what a node SAYS*).
- The cost measurement: ~640 nodes at one name plus about one part each is ~2,000 strings, ~12 MB at 1536-dim float32, brute-force cosine ~3M multiply-adds. No ANN index, no vector database.
- The three prohibitions: similarity is symmetric and untyped, so it cannot express `spec(role)`, `requires` or `prepares-for`; it has no meaningful transitivity, so the `requires` closure fails; and top-k is never empty, so it **structurally cannot express absence**, which is exactly what *"concepts no artifact covers"* asks. *"Similarity gives discovery; edges give assertion."*

Only the slice-1 prohibition survived migration - *do not foreclose side stores keyed by node id* - as `spec/schema.md` §8 and `spec/design.md` §5 conclusion 2.

**Destination: deferral issue.** Precondition: embeddings existing (slice 3) plus a ruling on whether a fourth access level is legal. **Second, separable item for Billy:** `spec/write-rules.md` §3.4 gives an unruled proposal the standing of a settled reader. That is a standing inflation in a live record and I have not touched it.

### L4. The blind-run hygiene rule, orphaned when its carrier was voided

`archive/slice-1-plan-2026-08-27.md` §7: *"The blind run receives a **copy** of the PNG, never a symlink, with document metadata stripped - the 2026-08-22 seal leak."* Plus *"No re-picking. A bad extraction is a finding."*

This is a remedy for a measured leak, attached to acceptance (b). `spec/architecture.md` §4 voids (b) - *"The screenshot-extraction evaluation tests an agent producing candidate facts, which is presentation"* - and re-homes nothing. No live record in `domain/`, `spec/` or `plan/` carries it.

**Destination: deferral issue**, folded into whichever issue carries the extraction evaluation. Precondition: a blind extraction run being set up. It is two sentences and it prevents a repeat of a leak that already happened once.

---

## Open questions never re-homed

**O1. The owed experiment: vary what the agent must DO, not what it can SEE.** `archive/slice-1-plan-2026-08-27.md` §5(c) names acceptance (c) as *"the natural carrier for the owed experiment"*; `archive/openclaw-registry-2026-08-25.md` entry 67 carries it as the gate on the read-side null result (*"gated-on: an experiment that varies what the agent must DO rather than what it can SEE - E8's attempt was retracted by E9"*), with the remaining suspects named as **sizing** and **the absence of an allocation procedure**. `spec/architecture.md` §4 voids (c). `spec/ring-0.md` §2 discusses the same null result and explains why the instrument could not have detected the effect, but does not carry the owed experiment or the two suspects. **Caveat: `records/findings/read-cycle.md` is the plausible home and was outside the boundary - check it before treating this as orphaned.** Note that Billy's 2026-08-30 ruling 2 speaks directly to the sizing suspect.

**O2. The second apparatus repair.** `archive/slice-1-plan-2026-08-27.md` §8: *"the faithfulness rubric does not check claims about the agent's own actions, which `calls.jsonl` can check exactly. Owed with (c), and (c) is where it becomes cheap."* Same voiding, same caveat about `findings/`. `calls.jsonl` appears in no record in `domain/`, `spec/` or `plan/`.

**O3. `skeleton by-query` as a fourth access mode.** Stated at L3. Explicitly marked as needing a ruling because it adds a row to a ruled table; never re-homed; now leaned on by a live write rule.

**O4. The paused verb-shaping question.** Stated at L2.

**O5. Meta, and it is the reason this pass existed.** `archive/slice-1-plan-2026-08-27.md` §9 item 4: *"The ~25 rulings of the 2026-08-24 design cycle are indexed only by `archive/changelog-2026-08-24-slice-1.md`. openclaw's decision-conditions registry never received them, and that registry no longer governs this project."* The archive changelog's own header repeats it: kept whole *"because it is the only index of roughly twenty-five rulings, several of which reached no other document."* That claim is now tested: of those rulings, the sweep found exactly one (L1) with no live statement. The rest are carried, mostly at `spec/schema.md` and `domain/model.md`.

---

## Reasons a live record depends on that only exist here

**R1. F4's authority.** `spec/design.md` §1 F4 states *"Sticky notes attach, detach and modify cheaply, including onto a course. The late-day budget is course-level and lives on a note"*, and §3.2 makes it forcing for slice 1 (*"course-level notes - the late-day budget, the snow-day credit, the conditional-weighting rule - must land and read back for F5 to pass"*). The live record carries no authority for it. `archive/changelog-2026-08-24-slice-1.md` R13 is the only record of where that authority sits, and it is a correction: F4's authority was **re-pointed from a bare `[R], 2026-08-24` to `INPUTS` §3**, because §7 and §13 are both `[intuition]` and §7 says outright *"must enter the scaffold as an unruled intuition, never as a premise"*. `INPUTS` §1-§13 was **not migrated** - the archive changelog's own header freezes it at `openclaw:fall26/2026-08-24-slice-1-write/workspace/INPUTS-2026-08-24.md`. So a live requirement rests on a two-hop chain whose far end leaves with openclaw. **Destination: not carried as content** - the requirement itself is already live and `plan/backlog.md` B8 tracks the unmodelled half. What is worth recording once is that F4's authority does not migrate, so nobody re-derives it as a bare `[R]`.

**R2. The provenance caveat on `design.md` §3.7's decisive reason.** `spec/design.md` §3.7 rejects inheritance for `annotation`, and its first and self-declared decisive reason is that the implementation language is not committed to Python (*"Rust and Go have no inheritance"*). `archive/changelog-2026-08-24-slice-1.md` A5 carries the standing caveat: *"that quotation appears in no ledger in this repository - only in `DESIGN.md`."* The quotation is 未来不一定是 python 语言. Two things follow. The caveat exists nowhere live. And the premise has since moved: `spec/architecture.md` §6 rules **TypeScript**, which does have inheritance, so the decisive reason is now false as written while the conclusion (a `kind` tag, not a hierarchy) is independently supported by §3.7's reasons 2 and 3. **Destination: not carried.** Worth one line to Billy because a reader repairing §3.7 should know the quotation was never sourced.

**R3. What acceptance (c) actually measured, and why the docstring ordering ruling exists.** `plan/write-rules.md` §2.1 preserves Billy's 2026-08-26 ordering ruling and quotes the archive for its sourced form: `slice-1.md` §4.4's *"Docstrings are design, not documentation. The read cycle measured a docstring rewrite taking arm-A calls from 1 to 9 with data availability held constant"* and §6 expectation 7's *"any mid-test rewrite voids the arm"*. This one is **checked and fine**: the live record quotes the archive rather than pointing at it, `spec/architecture.md` §5 restates the 1-to-9 measurement independently, and `plan/write-rules.md` §2 records that the argument is now void with the ruling's target changed. No action.

**R4. `domain-design.md` §10.2's correction target.** Live §10.2 corrects a claim it attributes to *"§5 of the build spec"* - that section headings come at zero annotation cost - and records Billy's correction that §5 ruled out a **manual** taxonomy, not an LLM pass at ingest. The corrected claim is restated in the live record, so the dependency is satisfied. What lives only in `archive/build-plan-2026-08-27.md` §5 is the grouped-retrieval mechanism itself (`course > week > file > section`, retrieval always inside a group, the equation-chunking worry dissolved rather than solved). That is slice-3 corpus design with no live reader and no ruling behind it. **Destination: not carried.** It should be re-derived against Billy's 2026-08-30 ruling 6 rather than inherited, because ruling 6 changes the inclusion determinant, and because ruling 8 rejects the `week` node the same section's C5 depends on.

---

## Broken or ambiguous citations

Seven defects. **C1 is the serious one, and it points from a live record into the archive.**

**C1. `domain/model.md` line 16 presents the frozen build plan as the plan of record.** Its companion block reads: *"plan of record [`docs/superpowers/specs/2026-08-21-fall26-build-spec.md`](../archive/build-plan-2026-08-27.md) (**§9 first**)"*. The link target is the archive file, whose own first line reads **"FROZEN 2026-08-27 … Cite this document; do not follow its order"**, and the repo's rule is that there is no plan of record. The link **resolves**, the anchor text is the dead openclaw path, and the instruction *§9 first* sends a reader into a superseded schedule as authority. This is exactly the silent-resolution failure class already found three times elsewhere in this corpus. Nothing else live points at the archive as authority: `plan/application-tier.md` §3 gets it right (*"the two frozen plans in `../archive/` are cited, never followed"*).

**C2. `plan/build-plan.md` does not exist, cited twice.** `archive/slice-1-plan-2026-08-27.md` §5(b) (*"The test is weaker than the one `plan/build-plan.md` §10.4 names"*) and §8 (*"The graph, the concept and artifact layers, the store, RAG (`plan/build-plan.md` §10.4)"*). `records/plan/` holds `application-tier.md`, `backlog.md`, `write-rules.md` and nothing else. The **section** is real - §10.4 of `archive/build-plan-2026-08-27.md` is the slice-1 section - so the ref is a correct pointer at a stale path, created when the build plan moved into `archive/` on 2026-08-27 and its citers were not updated.

**C3. `slice-1.md` does not exist, cited four times, resolvable once.** `plan/write-rules.md` §2.1 (twice) and §8 refer to `slice-1.md` §2 / §4.2 / §4.4 / §4.5. Only the first occurrence carries a link (`[slice-1.md](../archive/slice-1-plan-2026-08-27.md)`); the rest are bare. §8's occurrence is the **only live pointer to the paused verb-shaping question** (L2), so the corpus's single thread to a Billy-owned open question hangs on a filename that does not resolve by grep.

**C4. Two citation conventions inside one archive file.** `archive/slice-1-plan-2026-08-27.md` uses proper relative links in some places (`../spec/architecture.md`, `../spec/design.md`) and bare `records/`-relative refs in others (`domain/domain-design.md` §6.1, `domain/model.md` §10 item 9, `spec/schema.md` §1.1, `archive/changelog-2026-08-24-slice-1.md` §14.2). From `records/archive/` the latter do not resolve as paths. Same pattern in `archive/build-plan-2026-08-27.md` §10. Readable, not resolvable.

**C5. `openclaw:` used as a URL scheme in a markdown link.** `archive/slice-1-plan-2026-08-27.md` §3 and §5(b) render `[openclaw:fall26/…/HANDOFF.md](openclaw:fall26/…/HANDOFF.md)` and the same for `2c03-obligations-and-edges.md`. These are declared-unresolvable refs written as live links, so a reader gets a broken link rather than a visible "elsewhere" marker. `archive/build-plan-2026-08-27.md` §10 does the same for `FINDINGS.md`.

**C6. Load-bearing archive refs into unmigrated openclaw files.** `archive/changelog-2026-08-24-slice-1.md` depends on `INPUTS` §1-§13 (R13's F4 authority, per R1 above), `INCONSISTENCIES.md` items 2 and 12, and `PLAN.md` §5.1. `archive/slice-1-plan-2026-08-27.md` §2 depends on `INPUTS-2026-08-24.md` §4.3 for the paused question's independent argument. `archive/openclaw-registry-2026-08-25.md` is 100% openclaw refs and says so in its header, which is the honest form of the same fact. **Separately, and outside the archive:** the live records make 18 openclaw citations of their own - `domain/model.md` 13, `spec/design.md` 2, `domain/domain-design.md` 1, `spec/ring-0.md` 1, `spec/schema.md` 1 - including `model.md` §7.2's only pointer for an unresolved conflict (`INCONSISTENCIES.md`) and `ring-0.md` §2's instrument critique (`CAVEATS.md` §1 and §7). Same defect class, and it will bite this migration too.

**C7. The corpus's only line-number citation, and it resolves.** `spec/schema.md`'s changelog entry for the `23:59` resolution attributes it *"- Billy 2026-08-24 via `archive/changelog-2026-08-24-slice-1.md:241` - ruled"*. Line 241 is the `due` row of §14.2 and carries exactly that ruling. Acceptable only because the target is frozen; it breaks the section-citation convention every other entry follows, and it will not survive a reformat.

---

## Contradictions with standing records

**X1. `done_by`'s null semantics. The archive says the default applies; the live record says no record. Live wins on date, and nothing records the reversal.** Three archive locations agree with each other: `slice-1-plan` §3 (*"`target_date` = `due − 7 days`, overridable, **resolved at read time**"*), `build-plan` §10.9 item 4 (*"a stored value always means Billy chose it, null always means the default applies"*), and `openclaw-registry` entry 41 (the same, plus the anxiety-removal reason). `spec/schema.md` §3 now reads: *"Null means no record; a planner wanting a work-back date computes `due − 7 days` as a **derived** value under its own name, and computes nothing when `due` is null."* The read-time default is gone. The live record wins on date (rewritten 2026-08-27, amended 2026-08-28), and I am saying so rather than assuming it. What is missing is any changelog entry recording the change: `schema.md`'s 2026-08-27 entry covers only the `finished_by` → `done_by` rename. Anyone migrating from the archive's three concurring statements would restore the read-time default.

**X2. The registry gives an agent draft the standing of a ruling.** `archive/openclaw-registry-2026-08-25.md` entry 23 is marked `[settled]` and reads *"fall26 is NOT an enterprise RAG - goal is anxiety-removal · background cross-course management · surfacing details Billy does not know to ask about; **tune for recall over precision**"*. The live source it points at splits: `domain/domain-design.md` §10.7 ruling 4 is Billy's and carries the first three clauses; *"Tune for recall, not precision"* sits in **§10.8, titled "Agent drafts, not ruled"**. The registry fused a ruling and a draft into one `[settled]` line. It is frozen, so this cannot be fixed in place - it is a warning about reading the registry as a rulings index.

**X3. `build-plan` C5's week node is rejected by Billy's 2026-08-30 ruling 8, and the archive never marks it.** C5 reads: *"for `corpus_profile = woven`: a weekly announcement names its resources, so ingestion **materialises a week node** linking them."* Ruling 8 says content and time layers must be separate and *"Week N as a node joined by edges is not right modelling"*. `domain/model.md` §9 already retracted the same shape in 2026-08-22 (*"`time-anchor` as a node field. Retracted - a renamed `week` … the graph has no time axis; time lives only in the obligation layer"*). C5 survives both §9 and §10 of its own document **unmarked**, so a migrator reading §3's component table finds a live-looking component. Nothing in `domain/`, `spec/` or `plan/` carries `corpus_profile`, `woven` or assembly nodes.

**X4. `build-plan` §8 is titled "The rule that governs all of it" and is superseded in half.** It reads: *"Only the facts layer may be rewritten. Everything else is append-only or read-only."* It is written in the five-type facts-layer vocabulary that its own §10 dissolved, and the append-only half was retracted for annotations: `domain/model.md` §8.1, **[R]** Billy 2026-08-23, *provenance does not confer immutability* - an agent may rewrite or detach a note whose staleness is evidenced, and an earlier agent-drafted append-only rule for origin-bearing notes was retracted the same day. What survives of §8 lives as the store boundary (`spec/design.md` §3.5) and as `spec/schema.md` §1's *every field is individually CRUD-able*. The section title is the hazard.

**X5. The portal screenshot's primacy is stated categorically in a live record and was corrected to course-specific here.** `domain/model.md` §10 item 7 concludes *"The portal screenshot is not an enrichment path for ring 0 - it is the primary one, and the handouts are primary only for `requires` and `spec`."* `archive/openclaw-registry-2026-08-25.md` entry 40 carries the correction: **"COURSE-SPECIFIC, not categorical (corrected 2026-08-23): 2aa4's handouts carry their own due dates"** (A1 02-06 · A2 03-05 · A3 03-20), and adds that the ruling holds unrestricted only for `status`, `score` and evaluation state - all three of which are now graveyarded (`spec/schema.md` §7), so the unrestricted residue is empty. The live record's evidence sentence is correctly scoped to 2c03; its conclusion is not. **Caveat:** the registry's ref for this is a derivation `FINDINGS.md`, so `records/findings/` may carry the correction. Worth one check.

**X6. The "22 obligations" number, noted because the archive is where it is stated most confidently.** `slice-1-plan` §5(a) and `build-plan` §10.4 both fix acceptance (a) at 22 real obligations, 15 from 2c03 and 7 from 2aa4. `spec/architecture.md` §4 amended that on 2026-08-28 to **one course's real obligations**, recording that a fresh extraction found **14** for 2c03 and that *"22 is not reachable by re-running the old route"* because the old count included a graveyarded recurring row. The live corpus has not propagated it: `plan/application-tier.md` §1, §2.2 T4, §3 and §4 still build to 22, and `spec/design.md` F5 and `spec/schema.md` §3/§6/§7 still count against 22. That is a live-versus-live divergence and I am not adjudicating it. It matters here only as a migration instruction: **do not carry the archive's 22 as a criterion**, because the record that supersedes it is `architecture.md` §4.

---

## Confirmed superseded

One line per major block, so the presumption is on the record as checked rather than assumed.

| block | verdict |
|---|---|
| `build-plan` §1-§8 (scope, DoD, components C1-C6, the W1/W2/W3 schedule, grouped retrieval, risks, the §7 decisions, the governing rule) | **Superseded**, and the document says so from line 15. The three §7 decisions are ruled in §9.1 and carried onward at `spec/design.md` §5. §8 is superseded in half, see X4. §5's mechanism has no live reader, see R4. |
| `build-plan` §9 (displacement after Step -1 and Step 0) | **Superseded.** Its content lives at `domain/domain-design.md` §10.3-§10.7 with the rulings marked. Nothing found that is not carried. |
| `build-plan` §10 (the re-plan: cost probe → slices 1-4) | **Sequencing. Not carried by design.** The slice subjects survive as subjects; the order does not. §10.4's two still-open items are carried (`domain/model.md` §10.9 for the late-day budget, `plan/backlog.md` B8; the snow-day credit at `spec/design.md` §3.2). §10.9's H1 and H3 gates are carried at `domain/model.md` conditions header and §10 item 6. |
| `build-plan` §0 (why it exists, the cross-domain requirement, the winter-27 co-op instance) | **Carried in full** at `domain/domain-design.md` §0.6, and confirmed live by Billy's 2026-08-30 ruling 1 (deferred to v2, not dead). The archive copy is a copy. |
| `slice-1-plan` §1, §4, §5, §6, §7 (mission, build order, three acceptances, pre-registration, anti-cheat) | **Sequencing and execution criteria. Not carried**, and `spec/architecture.md` §4 voids (b) and (c) explicitly. Two owed items fell out with them, see O1 and O2, and one hygiene rule, see L4. |
| `slice-1-plan` §3 (what is settled and must not be re-litigated, eleven items) | **All eleven carried**, at `spec/schema.md` §1.1/§3/§4.5/§7, `domain/model.md` §7.1/§8.2/§8.3, `spec/design.md` §3.2/§3.3. One diverges: `done_by`'s null semantics, see X1. |
| `slice-1-plan` §9 (carried forward, four items) | **All four carried.** The `parts` birth rules at `spec/schema.md` §6/§9 and ruled at `spec/write-rules.md` §3.4; the sticky-note bound at `spec/schema.md` §9 item 3 and `domain/model.md` §10.5; the dead grain replaced by `spec/ring-0.md`; item 4 is the meta-fact at O5. |
| `changelog` §14 (the field-set rulings, §14.1-§14.7) | **Carried**, almost entirely at `spec/schema.md` §1-§8. Two exceptions: §14.6 is L3; §14.4's two-reader question was ruled 2026-08-27 and `spec/write-rules.md`'s own changelog records that reading the archive as current state caused an error there. |
| `changelog` §15 (identity and C19) | **Carried and partly superseded.** C19 at `spec/schema.md` §2 and `spec/design.md` §3.2. §15.1's mechanism was replaced on 2026-08-28 by the opaque monotone id; `spec/schema.md` §1.1 records the reversal at both ends. |
| `changelog` §16 (the review-response rulings) | **Carried** at `spec/schema.md` §7's graveyard and §3's `optional` and `due` rows, except §16.1, which is L1. |
| `changelog` R1-R17, I1-I5, A1-A7, V1-V6, B1-B6, D1 (the document-change ledgers) | **Carried where they still bind**, at `spec/schema.md` and `spec/design.md` §3.3/§3.4/§3.7/§5. R13 leaves a dangling authority, see R1. A5 leaves an unsourced quotation, see R2. B4's lifetime correction is already applied here and at `spec/design.md` §5 conclusion 1 - **no archive plan reasons from a long-running process**, which is the one thing Billy's correction to carry warned about, and it does not apply. |
| `openclaw-registry` entries 15-39 (build/scope/derivation era) | **Carried or dead.** The design-side entries are carried at `domain/domain-design.md` §10 and `domain/model.md` §2-§8. The Postgres/MCP/Notion entries are superseded by `spec/architecture.md` §5-§6. Entry 23 over-states a standing, see X2. |
| `openclaw-registry` entries 40-71 (2026-08-23 cycle) | **Mostly carried.** Entry 40 has an uncarried correction, see X5. Entries 42-45 and 67 (cost probe, vendor property, long reference works and `pack()`, PNG container, the read-side gate) are **not in `domain/`, `spec/` or `plan/`** and their refs point at `FINDINGS.md` files - `records/findings/ingestion-probe.md` and `read-cycle.md` are the plausible homes and were outside the boundary. **Not reported as uncarried; check them.** |
| `openclaw-registry` entries 72-86 (the 2026-08-24 write cycle) | **Carried**, at `spec/design.md` §2-§5 and `spec/schema.md`, except entry 80, which is L1. Entry 51 (replay course → 2da4, because 2c03 is no longer blind and 2px3 lost a third of its timestamps) is sequencing and not carried; the underlying fact that **2c03 is no longer blind** is the part that would constrain a future blind evaluation, and it is worth one line wherever L4 lands. |

---

## Coverage

**Read in full:** all four archive files, 1,168 lines total. Every cross-reference each of them makes was followed and checked, and every reference into the archive that is visible from `records/domain/`, `records/spec/` and `records/plan/` was followed in the other direction (nine such references; results at C1, C2, C3, C7 and in the superseded table).

**Checked against, in full:** the ten live records in `domain/`, `spec/` and `plan/`, including their changelogs, which is where the reversals live.

**Not read, and this bounds four claims:** `records/findings/` (two files, names only), `records/evidence/`, every `openclaw:` path, and every other repository. The affected claims are O1, O2, X5 and the registry 42-45/67 row, each marked in place. A five-minute read of `records/findings/read-cycle.md` and `ingestion-probe.md` would close all four.

**What I did not do.** I did not adjudicate. Nothing was written into any fall26 record, no ordering was migrated, and no inventory of the archive was made. Where the archive and a live record disagree I said which wins and on what ground rather than assuming the later date settles it.

**The honest summary of the result.** The archive is very close to what it claims to be. Of roughly twenty-five rulings it indexes, **one** (L1) has no live statement anywhere. Three open items were left behind (L2, O1/O2 pending the `findings/` check, O3), one of them because the tier split voided their carrier without re-homing them, and one hygiene rule went with them (L4). Two live records lean on archive-only reasoning (R1, L3), one of them at inflated standing. Seven citation defects, of which one is a live record pointing at a frozen plan as the plan of record (C1). Five contradictions, of which one is stated three times in the archive against a single live reversal that was never written down (X1). **Nothing here overturns the presumption that the archive is superseded.** With L1 through L4 lifted out and C1 fixed, it can be treated as frozen and left alone.
