# Evidence survey - the three earliest fall26 sittings

**What this is.** A first-hand read of the process notes for the three earliest sittings in `fall26/evidence/`, checked ruling by ruling against `fall26/records/domain/` and `fall26/records/spec/`. `evidence/` is not a record: by the project's own statement it carries *"how a sitting reached its rulings, including the ones it got wrong first"* (`evidence/README.md`). Every item below is therefore tagged with which of three kinds it is, and nothing is adjudicated.

**What I read, in full, and nothing else:**

- `/Users/billywu/Documents/Projects/fall26/evidence/README.md` - 9 lines.
- `/Users/billywu/Documents/Projects/fall26/evidence/2026-08-23-read-cycle/PROVENANCE.md` - 11 lines - and `fixture.json` - 56 lines.
- `/Users/billywu/Documents/Projects/fall26/evidence/2026-08-25-refound-and-migration/NOTES.md` - 135 lines.
- `/Users/billywu/Documents/Projects/fall26/evidence/2026-08-26-interface-contract/` - all five files, 897 lines: `NOTES.md` 185 · `decisions.md` 106 · `draft-contract.md` 244 · `migration-gaps.md` 194 · `review.md` 168.

**Read for the record check only:** `records/domain/model.md` (709 lines), `records/domain/domain-design.md` (799), `records/spec/architecture.md` (136), `design.md` (268), `ring-0.md` (104), `schema.md` (253), `write-rules.md` (180). All seven read at their headings, changelogs and every passage a finding touches; `schema.md`, `architecture.md` and `spec/write-rules.md` read whole.

**Boundary observed.** No other `evidence/` directory was opened, listed or grepped. No openclaw path. No other repo. Within `fall26/records/` I opened only `domain/` and `spec/`.

**The consequence of that boundary, stated up front because it scopes every "no home" claim below.** `records/plan/` and `records/archive/` were off limits, and `records/spec/schema.md` and `architecture.md` repeatedly cite a `records/plan/backlog.md` by item number (B19, B20, B27) as the home for owed items. **So "no home" in this document means: not carried by `records/domain/` or `records/spec/`.** Where an item looks like backlog material I say so. Nothing here should be read as proof that an item is absent from the whole repo.

**Tag legend, applied to every item.**

| tag | meaning |
|---|---|
| `[ruled]` | Billy decided it. The only kind that can be homeless in the sense this pass is looking for |
| `[abandoned]` | a step tried and dropped **inside the same sitting**, however confidently written. Not a ruling |
| `[measured]` | a fact about what was found. May or may not still stand |
| `[agent-drafted]` | an agent's proposal that was never ruled. Recorded where it is load-bearing and homeless |

**Billy's 2026-08-30 rulings are applied throughout** and are named where they settle an item. They are newer than everything in these three directories.

---

## Rulings with no home

Six items. Four are Billy's; one is half-landed; one is an agent proposal recorded because it is load-bearing and explicitly says no record carries it.

### H1. `[ruled]` The domain records are INPUTS and `records/spec/` is their output, so an upstream ruling is not automatically binding downstream

**Verbatim**, Billy, 2026-08-26 (second sitting):

> domain design / domain model 是作为输入,他们产出的是 spec schema & spec design,所以那些 ruling 是没问题的…有些 field 找不到 reader 或者缺失的原因是因为他们被记录在了其他的地方.

**Where.** `evidence/2026-08-26-interface-contract/NOTES.md` §Cycle 1 Rulings, and quoted again as the correction that opens `migration-gaps.md` §4.

**Attribution.** Billy, 2026-08-26.

**Record check.** Not carried.

- `records/spec/architecture.md` §2's table assigns `../domain/` the tier *"none - it is the material both tiers are derived from, and it predates the split."* That is a tier assignment, not a statement about which document's ruling binds.
- `records/spec/schema.md`'s changelog carries the **consequence** on 2026-08-27 (*"the readers that never migrated are restored"*), never the rule.
- `records/domain/model.md`'s header states something that reads as the opposite precedence: *"**stronger than this directory implies:** passages marked `[R]` are ruled and are not open to argument."* Under H1 that is true of the input's own standing and says nothing about whether the derived record must obey it - but read cold, by a reader who does not have H1, it licenses exactly the error the sitting made.
- `records/domain/domain-design.md` carries no equivalent qualifier at all.

**Why it matters.** This ruling is what re-sorted 7 verified "the spec states the opposite of a ruling" findings down to 5, of which only 1 was actually input-versus-output. Without it the next reader repeats the sitting's own named error: *taking provenance for authority*.

**Destination proposal: `docs/adr/`.** All three tests hold. Hard to reverse - it governs how every later reader adjudicates a disagreement between two documents. Surprising without context - an `[R]` upstream normally binds. The result of a real trade-off - authority versus derivation, and the sitting paid for getting it backwards.

*Title:* **A derived record may narrow or drop its source's ruling; provenance is not authority.** A document derived from another may legitimately narrow, drop or supersede what its source ruled, and a divergence between them is not by itself evidence that the derived one is in violation. The failure this prevents has a name in this project already - *the authorising document has become history but is still cited as authority* - and this is that failure committed in reverse.

*Container caveat, stated rather than hidden.* The `domain/` versus `spec/` layering is fall26's structure. In the successor the same relation holds between `CONTEXT.md` and an ADR, and between an ADR and the code it governs, so the principle transfers even though the directories do not. If the successor decides it will never carry two layers of document, this becomes **not carried**.

### H2. `[ruled]` A tool definition plus its parameter names is one version, and versioning is the whole discipline

**Verbatim**, Billy, 2026-08-26 (second sitting):

> 这个不是说的 tool eval 的模式吗?一个 tool def. + param name 记做一个 version.

**Where.** `evidence/2026-08-26-interface-contract/NOTES.md` §Cycle 1 Rulings.

**Attribution.** Billy, 2026-08-26.

**What it rules.** The verb-routing test does not measure a fixed apparatus that a rewrite corrupts - **the verb's description is the treatment being varied**, and changing it produces version 2 rather than destroying version 1. The pre-registered *"any mid-test rewrite voids the arm"* forbids exactly one thing: **mixing two versions' runs inside one arm's score.** Nothing forbids drafting a description, and nothing forbids running the test against the description that exists today.

**Record check.** Not carried.

- `records/spec/architecture.md` §4 records that the verb-routing evaluation is presentation tier and cannot run against an application tier with no descriptions. It says nothing about versioning.
- `records/spec/ring-0.md` lines 26-28 discuss a routing test and its null result at length and never reach the version question.
- Nothing in `records/domain/` mentions it.

The sitting also `[measured]` that the discipline was **already written into the repo and read past**: `records/plan/slice-1.md` §4.4, one sentence after *"Docstrings are design, not documentation"*, reads *"Verb descriptions are drafted deliberately and recorded verbatim as run."* That file is outside my boundary and I did not open it.

**Destination proposal: Deferral.** Billy's 2026-08-30 ruling 9 defers the hypothesis gate on exactly these grounds - no exposed CLI surface, prompt and docstring work not landed, product-facing verb names undecided. The rule has no live subject until a verb surface with descriptions exists.

*Precondition that wakes it:* the first exposed verb or CLI surface carrying descriptions, at the moment anyone proposes running a routing or tool-selection evaluation against it.

*Alternative considered:* `docs/adr/`, on the ground that the rule is settled, cheap to record and surprising (it converts a prohibition into a version stamp). Rejected in favour of deferral only because an ADR for an evaluation that cannot be run yet is a decision with no consequences to bind.

### H3. `[ruled]` "对外" means both the domain API and the agent surface, and a divergence between them is a defect in the projection - **half landed**

**Verbatim**, Billy, 2026-08-26 (second sitting):

> A 是确保这个 schema 和 model 作为权威,B 是它的投影 - agent 能看到的东西.

**Where.** `evidence/2026-08-26-interface-contract/NOTES.md` §Cycle 1 Rulings, the first entry. The session's gloss: *"the contract has one truth and one projection, not two documents of equal standing, and a divergence between them is a defect in **B** by construction."*

**Record check. The ordering landed; the defect-attribution clause did not.**

- Landed: `records/spec/architecture.md` §1 - *"A tier is designed against the tier below it, and that tier must already exist."*
- Landed: `architecture.md` §2's per-record tier assignment, and §7's re-homing of the verb set.
- **Not carried:** nowhere in `records/spec/` or `records/domain/` does any record say that when the truth and the projection disagree, the projection is wrong. `architecture.md` states the tiers and their ownership; it never states the adjudication rule for a conflict between them.

**Destination proposal: `docs/adr/`, as one added consequence to whatever ADR records the tier split** - not as an ADR of its own. It is a one-line corollary and it will not survive as a separate decision.

*Wording:* when the application tier and the presentation tier disagree about a value or a rule, the application tier is right and the divergence is a defect in the presentation tier.

### H4. `[ruled]` `annotation.origin` is a bounded tag in slice 1; the flat provenance log is deferred, and its deferral is a dated liability

**Where.** `evidence/2026-08-26-interface-contract/NOTES.md` §`sticky_note` - the five-column pass.

**Near-verbatim, as the session recorded it.** Billy, 2026-08-26 (second sitting): `annotation.origin` is a bounded **TAG** in slice 1; the flat provenance log is **deferred**, and its deferral is a **dated liability rather than a gap**. The premise that needs the log does not exist in slice 1 - *"no slice-1 annotation is an extraction from a source text the system holds"*, because announcements and handouts arrive with the artifact-reading pass in slice 2/3. **The liability comes due the moment announcements are ingested:** at that instant `records/domain/model.md`'s *"Editing a note destroys nothing"* becomes false unless the log exists.

The session's own note names the records it touches: `records/spec/schema.md` §4 and §4.5, and `records/spec/design.md` §3.0.

**Record check. Partially landed; the two load-bearing halves are not.**

- `records/spec/schema.md` §4, `origin`: *"string, nullable. **The annotation provenance field, shared with `progress` (§4.5).** How this annotation came to exist - an announcement, someone saying so (`stated`), or the system having asked (`asked`). **Provenance does not confer immutability**…"*
- **Missing 1:** the record never says `origin` is *a tag, not a text carrier*. Read cold, *"an announcement"* as a legal value reads as though the announcement could be in there.
- **Missing 2:** neither `schema.md` nor `design.md` carries the deferral or the dated liability. `design.md` §3.0 still states *"there are exactly TWO persisted things"* - the skeleton and the store - with no marker.

This is also the live void V1 below, from the other side.

**Destination proposal: Deferral.** *Precondition that wakes it:* the first annotation whose content is an extraction from a source text the system holds - in practice, the first ingestion of announcements or handouts. At that moment either the provenance log exists or the retracted rule *origin-bearing notes are append-only* comes back into force.

### H5. `[ruled]` A `progress.detail` with no state: the landing asks - and the rule is a general behaviour in a skill, not a docstring

**Where.** `evidence/2026-08-26-interface-contract/NOTES.md` §Billy's dispositions, 2026-08-27.

**Attribution.** Billy, 2026-08-27.

**Record check.** Not carried.

- `records/spec/schema.md` §4.5 carries the constraint (*`detail` is illegal without a `state`*) and its enforcement point (construction, because both fields are on the record). It says nothing about asking.
- `records/spec/write-rules.md` §5's `progress` row reads *"none yet"* for `state` · `detail` · `origin`.
- `write-rules.md` §1.1 is a **different** ask rule - *an inferred value is asked about, not annotated* - and is about a value the agent inferred, not about a missing state.

**Destination proposal: Not carried, superseded.** Two later rulings dissolve the case this rule was written for.

- `schema.md`'s changelog, 2026-08-28, Billy: `progress.state` is **no longer nullable**, and an obligation with no progress record reads as `not_started`. A `detail` with no `state` is therefore no longer a shape a writer can be stuck in.
- Billy, 2026-08-30, ruling 4: `progress.state` defaults to `not_started` **precisely so the agent does not keep asking**, and proactivity is written too rigidly now.

Recorded here so that nobody finding the 08-27 disposition in isolation revives an ask that two later rulings removed the reason for.

### H6. `[agent-drafted]` The provenance log IS the store - `chunk.node_id = <sticky_note id>`

**Not a ruling.** Recorded because it is the only proposal anyone has made for where the deferred log would live, and because the sitting itself flagged it: *"No record says any of this; it is this session's derivation."*

**Where.** `evidence/2026-08-26-interface-contract/NOTES.md` §`sticky_note`, immediately after H4.

**The proposal.** `records/spec/design.md` §3.0 couples the store to the skeleton by exactly one field, `chunk.node_id`, and a `sticky_note` is a node with an id. So `chunk.node_id = <sticky_note id>` **is** a flat provenance log, the two-persisted-things claim survives, and the liability's due date becomes slice 3 when the store exists. **Cost stated by the author:** a provenance chunk carries text with no query purpose and an embedding nobody searches, which is a degenerate `Chunk`, and `design.md` §3.5 would have to say the store holds two classes of content.

**Record check.** Not carried. `design.md` §3.0 and §3.5 say nothing about two classes of store content.

**Destination proposal: Not carried, and it appears to be closed rather than merely unlanded.** Billy's 2026-08-30 ruling 6 bears directly: the determinant of RAG inclusion is **the nature of the RAG store - it holds semantic, decontextualized facts about course materials**. Raw announcement text kept for provenance is neither semantic nor decontextualized, so under ruling 6 it does not belong in the store. **I am not adjudicating this**; I am recording that the one candidate landing site for the deferred log looks closed by a ruling made four days later, which makes H4's deferral homeless in a stronger sense than the sitting knew.

### H7. `[ruled]` Two process rulings whose home is methodology, not a record

Listed for completeness so a later reader does not count them as gaps.

- Billy, 2026-08-26: *"先把 domain 层面的 schema 的每一个 field 的定义…写清楚,之后再决定暴露给 agent 的 surface 是怎样的,然后之后再跑 A/B testing. 这是 design 的活."* Field definitions first, agent surface second, routing test third. **Superseded within days** by the three-tier split, which re-homed the surface to presentation and removed the routing test from the near term (`architecture.md` §4).
- Billy, 2026-08-26: *"你先不要直接写完,先做一遍全面分析,再一步一步决定,决定完了再落档."* Analysis first, decisions one at a time, the document last.

**Destination: Not carried.** Both are how a sitting is run. Their home in the old container was `~/.claude/CLAUDE.md`, outside my boundary and outside `records/`.

---

## Voids, corrections and withdrawals

### V1. LIVE, and the most consequential finding in this pass. `records/domain/model.md` §8.1 asserts a flat provenance log that Billy deferred

**The record, uncorrected as of the `design/course-level` checkout** - `records/domain/model.md` §8.1, lines 531-535, inside a block headed `PROMOTED 2026-08-24 (ruled 2026-08-23)`:

> An earlier agent draft — *origin-bearing notes are append-only, self-authored notes are editable in place* — is **retracted**. Its premise was false: §8's merge of `announcement → node mentions` into `sticky_note.origin` keeps a **flat provenance log**, so the announcement text lives there and the note is the extracted meaning. Editing a note destroys nothing.

**The ruling that narrows it** - `evidence/2026-08-26-interface-contract/NOTES.md` §`sticky_note`, Billy, 2026-08-26 (second sitting): `annotation.origin` is a bounded tag in slice 1 and **the flat provenance log is deferred**. The session states the consequence in terms:

> **If the log does not exist, editing a note destroys the announcement text and the retracted rule's premise returns.**

**Does the record still stand uncorrected today? Yes.**

- `model.md`'s changelog (lines 697-709) carries four entries dated 2026-08-25 to 2026-08-28 and **none of them touches §8.1**. The passage is in the present tense - *"keeps a flat provenance log"* - inside a section whose header grants it ruled standing.
- `records/spec/design.md` §3.0 still reads *"there are exactly TWO persisted things"* - the skeleton and the store - with no third and no marker.
- `records/spec/schema.md` §4's `origin` entry carries *"Provenance does not confer immutability"*, which is the **conclusion** the retraction reached, while the premise that supported it is deferred and unmarked.

**How bad it is, stated precisely rather than dramatised.** The record is not wrong *today*: the sitting itself established that no slice-1 annotation is an extraction from a source text the system holds, so nothing currently relies on the log. What is wrong is the **tense and the standing**. A truth record asserts a mechanism as present, in a passage marked ruled, and uses it as the premise for a retraction; the mechanism is in fact deferred, and the sitting that deferred it wrote down the exact moment the retraction reverses. A reader arriving at slice 2 or 3 finds §8.1 saying the premise holds.

**What would fix it.** Not an edit to the retraction - the retraction is Billy's and stands. A dated condition on §8.1 saying the log is deferred, naming the ingestion of announcements as the moment it comes due. That is H4 landing.

### V2. LIVE but weaker, and adjacent to a later sitting's work. `model.md` §7.2's UNRESOLVED banner

**The record** - `records/domain/model.md` lines 409-413:

> **UNRESOLVED, and it must not be smoothed over.** §7's own table above enumerates *labels, summaries, sticky notes* as distinct things, and §4's store column lists a separate `summary`. Reading `label` **as** the ingest-written summary is the 08-23 ruling; reconciling it with §7's enumeration was never done.

**What my sitting found that bears on it** - `evidence/2026-08-26-interface-contract/migration-gaps.md` §1.1 and §2.1: `obligation.name`'s writer is contested between `model.md:391` (an LLM writes it at ingest) and `schema.md:70` (what Billy calls it), and `summary` is returned by a ruled verb while appearing in no field table in `records/spec/`.

**Standing today.** Both have moved, but by the **later** sittings, not mine. `model.md`'s changelog, 2026-08-28, Billy: *"§7.1's obligation-label question is settled: an obligation carries no ingest-written summary. The NOT SETTLED block is removed."* That closed the §7.1 block, which is the one `migration-gaps.md` §1.1 cited at `model.md:366-376`. **The §7.2 banner at lines 409-413 is a different block and is still standing.** `architecture.md` §5 (2026-08-28) rules that a summary is written only where a node's identity is content the skeleton does not hold - the artifact - which reads as the answer the §7.2 banner is waiting for.

**Not chased, by instruction.** This sits inside the 08-28 work another agent is reading. Flagged so the two passes meet: **if the 08-28 sitting believes it closed the label-versus-summary question, `model.md` §7.2's banner is the one that did not get the memo.**

### V3. Effected. `records/plan/write-rules.md` §7's "a NEW record, NOT an edit to `spec/schema.md`"

`evidence/2026-08-26-interface-contract/NOTES.md` §Cycle 1 records that §7's three arguments all rested on a premise Billy removed, and recommends rewriting `schema.md` in place, *"Billy's call."*

**Outcome: the void took.** `records/spec/schema.md`'s changelog, 2026-08-27, Billy: *"the body is rewritten as pure statements."* The record was rewritten in place rather than duplicated. No further action.

### V4. Effected, and unverifiable inside my boundary. `records/plan/write-rules.md` §2's docstring block

The sitting flagged §2's *"§4.4 and §4.5 are blocked entirely"* as **agent-drafted inference over-stating a narrower Billy ruling**, and explicitly *"flagged for Billy, not edited."* It then retracted its own first reading of it (see A2 below).

**Standing today.** `records/spec/architecture.md` §4 carries the surviving form: *"The 2026-08-26 ruling that write rules precede the build **still holds and its target changed**: they precede the *presentation* tier, not the application tier."* And `records/spec/write-rules.md`'s header records that the abstract mandate *"stalled for two months"* and is **frozen** at `../plan/write-rules.md`. **`records/plan/write-rules.md` is outside my boundary and I did not open it**, so I cannot say whether §2 was ever corrected in place. Reported as probably moot, not as verified.

### V5. Withdrawn by Billy, and landed. The mandatory-note rule on `grade_share_conditional`

The 08-26 draft made a note **required** whenever the flag is true. Billy, 2026-08-27, under *"the system must not chase the agent"*: the worked example *"the midterm is worth at least 30%"* stores `grade_share = 30` and **optionally** a one-line note; *"the mandatory-note rule this session drafted is over-strict and is withdrawn."*

**Landed.** `records/spec/schema.md` §3: *"The rule **may optionally** be left on a one-line sticky note; requiring one is not a rule, because a schema rule that manufactures a conflict nobody would care about is a defect in the rule."* Changelog entry 2026-08-27, Billy, ruled. No residue.

### V6. Withdrawn by Billy on form, and landed. The fifth column

The sitting produced a field document whose fifth entry per field was *the ruling that caused it*, arguing that a birth reason is not history but a live constraint on whether a field may be removed. Billy withdrew it **on form**: *"a document whose body is citations and standings is an audit trail, not a canonical spec."*

**Landed as split rather than as deletion.** `records/spec/schema.md` header: *"The body carries no standing tags, no attributions and no history. Those, and the record of what changed and when, live at the end of this file."* The content survives as rules in the body; the citations moved to the changelog. Every spec record now follows it. No residue.

### V7. Retracted inside the sitting, recorded so it is not revived

`NOTES.md` §Cycle 1 carries an entry explicitly marked `[retracted - superseded by the tool-eval ruling below]`. Its content - that drafting the verb descriptions was blocked - is **not a ruling and was never true**. The sitting named its own error as a move: **treating the treatment as the instrument.** Anyone reading that bullet without reading its own tag will re-block work that H2 unblocked.

### V8. Uncorrected in `records/spec/`, and never dispositioned. Five blind-review findings whose subject is still standing

These come from `evidence/2026-08-26-interface-contract/review.md` §4, the "smaller, but each has a bad failure mode" list. Billy's 2026-08-27 dispositions do not reach them, and I found no record carrying them. **`records/plan/backlog.md` is the plausible home and is outside my boundary**, so these are reported as unchecked-there, not as absent from the repo.

| finding | `review.md` | what `records/spec/` says today | still open? |
|---|---|---|---|
| Timestamps have **no timezone, no precision, no clock authority**. ISO 8601 admits four conformant renderings of one instant; a UTC `added_at` and a local `due` cannot be ordered | §4 bullet 1 | `schema.md` §1: *"timestamps \| ISO 8601"* and nothing more | yes |
| **`term` is justified as a key and has no enumerated vocabulary.** *"Fall 2026"* becomes `fall-2026` or `autumn-2026`; grouping splits into two non-empty buckets and nothing looks broken | §4 bullet 2 | `schema.md` §2: *"`term` \| string \| The term it is taken in - `winter-2026`"*. An example, not a vocabulary | yes |
| **`updated_at` "gates" currency with no threshold.** *"A progress answer asked nine days ago is current, or not, on a coin flip"* - and this is the load-bearing half of the ask-at-read mechanism | §4 bullet 4 | `schema.md` §4.5 `origin` carries the prominence rule and no threshold | yes |
| **`schema_version` mismatch behaviour** | §3-adjacent; `migration-gaps.md` §3 lists it as a genuine absence found by both sweeps | `schema.md` §8 says a version exists and why. It does not say what a reader does when it does not match | yes |
| **A one-hop walk over a deliberately dangling `to`** returns *"the far endpoint"* for an endpoint that does not exist, and nothing says what. If null, a dangling link is indistinguishable from an orphaned note - which the maintenance rule may then detach | §4 bullet 6 | `schema.md` §1 rules that a `Ref` *"may name something not present"*; `design.md` §3.2 costs that case. Neither says what the walk returns | yes |

**Destination proposal for all five: Not carried as ADRs - they are build-time specification gaps, not decisions.** Each is one line in whatever the successor uses for owed implementation detail. The only one with an argument for `docs/adr/` is the timestamp one, because a clock-and-zone authority is hard to reverse once data exists; if the successor persists any timestamp before deciding it, it has decided it by accident.

---

## Open questions addressed to Billy

### The file of them: `evidence/2026-08-26-interface-contract/decisions.md`

**Twelve items, self-contained, ordered by blast radius**, written to Billy. Extracted in full below with each one's status checked against `records/spec/` and against Billy's 2026-08-27 dispositions and 2026-08-30 rulings. **Seven are answered. Five are live, and one of those has grown.**

| # | the question, as `decisions.md` states it | status |
|---|---|---|
| 1 | **What gets an obligation row.** One syllabus, two agents: 12 weekly readings become 12 rows or 0; a project with a proposal, a draft and a final becomes 1 row or 3. *"The repo names 'what counts as a part' as an owed item in four separate records; it has never once named 'what counts as an obligation'."* Recommendation: owed, with an owner and a due slice, and forbid bulk ingestion until it exists | **Answered behaviourally, still open definitionally.** Billy 2026-08-27: *an agent never auto-adds anything unless it is clear the user wants it; what gets a row is what the user wants tracked, and the user triggers it* - landed at `architecture.md` §3. Billy 2026-08-30 ruling 1 sets the outer boundary: coursework inside academics. **What neither reaches is the row-count question for material the user does want tracked** - the proposal/draft/final case. `schema.md` §9 item 5 carries the residue as *the domain boundary* |
| 2 | **May a write rule refer to the source at all.** Six write rules are of the form *"the value must be what the source stated"*, and nothing in the system carries a source - `stated_in` and `source_ref` are graveyarded | **Answered.** Billy 2026-08-27: *a write rule never refers to the source. Never.* Landed at `architecture.md` §3 and as the governing condition of `spec/write-rules.md`, whose own 2026-08-28 changelog corrects the absolute phrasing to *the direction a rule is derived from* |
| 3 | **How two names are judged to be the same thing.** No distance function, no threshold. `A10` is one edit from `A1` so A10 can never be created; *"Reading Response"* in twelve weeks mints the same id twelve times, which is not a near match at all | **Answered.** `schema.md` §1.1: *"This tier performs no near-match matching. Deciding that two records name the same thing happens above it."* The id is opaque and assigned, so neither failure has an input any more |
| 4 | **The annotation id scheme is broken - ratify the fix.** Construction-order deadlock, ordinal collision on retarget, unparseable open-set `<kind>` | **Answered, by removal.** `schema.md` §1.1, ruled 2026-08-28: the id is an opaque monotone serial in one id space. The scheme the question is about no longer exists |
| 5 | **`optional` and `grade_share_conditional` cannot say "unknown"** | **Answered.** Both nullable, null means unknown - `schema.md` §3, ruled 2026-08-27 |
| 6 | **Is a correction ever applied, or only attached.** *"The midterm has moved to Oct 25"* - two agents take opposite actions and each cites a rule. Read literally, *"every corrected deadline stays wrong in the record with a note sitting next to it"* | **Answered**, in the direction `decisions.md` recommended. `spec/write-rules.md` §1.1: *"**An update is an update.** A correction changes the field; it does not accumulate commentary beside it"* |
| 7 | **A progress detail with no state** | **Answered, then mooted.** Billy 2026-08-27 chose (b), the landing asks. `progress.state` became non-nullable on 2026-08-28, which removes the shape. See H5 |
| 8 | **What happens when the material does not supply a required field.** A forwarded *"the midterm is Monday, bring a calculator"* names no course, and `course` is not nullable and set once, so a guess is permanent. A syllabus stating *"there will be a final examination during the last week of term"* states no handle. *"The essay is due Friday"* is a day, so `due`'s null branch does not cover it. Recommendation: **landing may decline a field and report what it could not determine** - *"this makes what a landing may refuse to do part of the contract, which nothing currently says"* | **LIVE.** No record in `records/domain/` or `records/spec/` says a landing may decline a field. `spec/write-rules.md` §1.1 covers an **inferred** value (ask the user) and §1.2 is an OWED slot for *absent is not unknown when a person would not hesitate*. Partly parked by `architecture.md` §7, which takes `land()` out of the first build |
| 9 | **`grade_share` - whose share, and which arm.** *"Homework: 40% (six assignments)"* puts 40 on six rows and the corpus asserts **240%**; and for `10/10/30 or 0/0/50` both 30 and 50 are legal, so two corpora differ by 20 points with both flagged true. Recommendation: a stated share covering a group is **not** this field's value - store null, put the group rule on a note - and name the arm rule explicitly, with *the arm that is worst for you* as the honest default | **LIVE, and Billy's 2026-08-30 ruling does not reach it.** Ruling 2 settles the **reader** (`grade_share` is reference only, never an input). Neither the scope rule nor the arm rule is in `schema.md` §3, `spec/write-rules.md` §3 (the `grade_share` row reads *"none yet"*), or anywhere in `records/domain/`. The 240% failure is still reachable |
| 10 | **What name does a resolved `due` come back under.** `23:59` is the most common **stated** deadline time in a university course, so a resolved value is wire-identical to a stated one and a later landing carrying a real time is rejected as an illegal promotion | **Half answered.** `schema.md` §3: *"A `Date` resolves to `23:59` at read time; **which surface applies that resolution is presentation tier**, and the stored value is always returned raw."* Returning raw closes the storage half. **The name the resolved value comes back under is still unnamed**, and it is now presentation's to name |
| 11 | **`finished_by` or `done_by`** | **Answered:** `done_by`, ruled 2026-08-27 on the measured `finish 17 : start 1` |
| 12 | **What the node-kind discriminator is called** | **Answered:** it is `kind`, and `sticky_note.kind` was renamed `category`. Ruled 2026-08-27 |

`decisions.md` also carries a closing list headed **"Fixed without a ruling - reported so nothing is changed silently"** - eight drafting faults the session corrected on its own authority, including the `progress.state` prose inversion (*started / doing / finished* against `not_started | in_progress | done`) and the false claim that `grade_share` is the only unread field. Those are corrections to a withdrawn draft, not to a record, and none needs anything now.

### Also addressed to Billy, from the same sitting's Handoff

> **Owned by Billy:** `grade_share`'s name · the length bound's number · the domain boundary.

**Status.** The length bound and the domain boundary are both carried as owed at `schema.md` §9 items 3 and 5. **`grade_share`'s name is not in that list and I found it nowhere else in `records/domain/` or `records/spec/`** - the 08-25 sitting had recorded the same item as *"`domain/model.md` §10 item 9 calls one field three names - `weight`, `worth_percent`, and the schema's `grade_share`"*, deliberately not renamed *"because the name itself is unruled and Billy's."*

### One more, and it is a whole fact type

`migration-gaps.md` §2.1 reports, from a sweep this session did not open in the original: **`plan` and `preference` are two whole fact types** at `records/domain/domain-design.md:299-300`, *"in neither the kinds list, the graveyard, nor the not-built list."*

**I verified this in `records/`.** `domain-design.md` line 300 defines `preference` with a field set (`id · scope (global | course) · updated_at`) and a reader (M4), and §8 argues it at length: *"Preferences are not a new layer - they are a fact type. Structurally it is identical to `progress`."* Neither `plan` nor `preference` appears in `records/spec/schema.md`'s kind set, in its §7 graveyard, or in `design.md` §3.1's slice-1/slice-2 kind lists.

- **`plan` is answered by Billy's 2026-08-30 ruling 3:** a real requirement, not settleable now, needs its own grilling session, cannot be designed before schema, API and CLI shape settle. **Destination: Deferral**, precondition = schema, API and CLI shape have settled.
- **`preference` is answered by nothing.** It is neither carried nor graveyarded, which is the exact state `migration-gaps.md` §2.1 flags as worse than either: *"a reader cannot tell whether it is deliberately absent or overlooked."* **This is a question for Billy that no record and no ruling reaches.**

---

## Abandoned steps

Recorded so nobody later mistakes one for a ruling. Each was written confidently inside the sitting that dropped it.

**A1. The operation-first mandate (2026-08-26, Cycle 1).** The cycle opened with an ordering that specified the operations first. Billy's *"field definitions first"* ruling **replaced it before anything was produced**. The sitting named why the original was wrong: *"An ordering whose **first** operation cannot be specified without the field-level answer has the dependency backwards"* - the move being **specifying the projection before the thing projected**.

**A2. Reading *"any mid-test rewrite voids the arm"* as a total block on drafting.** Written as a confident `[retracted]`-tagged entry in the same Rulings list as real rulings. Superseded by H2 within one exchange. See V7.

**A3. Criterion d2 - the four owed fields may remain named holes.** Passed as written, then **superseded mid-cycle** by Billy's amendment requiring every field's mechanism complete and independently verified. Both the criterion and its supersession are in `NOTES.md`; only the second is current.

**A4. The five-column field document.** Produced, then withdrawn on form. See V6.

**A5. `draft-contract.md` itself, as a specification.** 244 lines, all 31 fields written. The blind review plus Billy's dispositions established that it **conflates the application and presentation tiers** - *"six of its write rules are agent-behaviour rules that do not belong in a schema at all"* - and by its own §0 test (*a rule with no rejecting test is not a rule*) roughly half its entries were not rules. **The whole file is an abandoned step.** Its individual sentences must not be quoted as contract.

**A6. Position A on `obligation.parts`** - that the field's target is size, with concepts a by-product. Closed toward Position B by Billy, 2026-08-27 (*"`parts` carries the CONCEPTS the obligation's source carries"*) and again 2026-08-27 (*"parts 的序数估体量目前先不显性设计"*). Landed at `schema.md` §3 and `spec/write-rules.md` §3.4.

**A7. The annotation id scheme `<target-id>-<kind>-<n>`.** Ruled by Billy on 2026-08-26 (*"先这么定,我也想不到更好的机制"*), found broken three ways by the blind review the same sitting, patched by `decisions.md` #4, and then **removed entirely** by the 2026-08-28 opaque-serial ruling. A ruling that was superseded is not an abandoned step in the strict sense - but the *scheme* is dead and the sitting's derived consequence (that `land()`'s contract differs by node kind, because annotation landing must read existing state to assign an ordinal) died with it.

**A8. Uniqueness on `(obligation_id, course_id)`.** Billy proposed it on 2026-08-27; Cycle 2 rejected it with reasons and Billy ratified the rejection the same day. Recorded because a reader finding Billy's proposal alone would take it as ruled.

**A9. *"Obligation objects are attached to a course through typed edges."*** Billy's own supposition, prefixed *"if I'm correct"*; Cycle 2 established that as of the current design he was not, and he ratified `obligation.course` staying a field.

**A10. The internal-versus-external field axis (Cycle 2's question D).** Refused with a reason: it is presentation leaking into the application tier.

**A11. From the 08-25 sitting - pre-creating the next session's file.** The approved plan called for it; the sitting deviated, because *"a session file is opened by the session that runs it."* The 2026-08-24 TASK sheet became `records/plan/slice-1.md` instead.

**A12. From the 08-23 read cycle - the *"eighteen days before launch"* defence.** `PROVENANCE.md` records it as a retraction worth keeping in view: the 2c03-rich / 2aa4-empty asymmetry *"was defended during that session as 'what a course looks like eighteen days before launch'. It is not - it is an artifact of the deleted page, and it was sold as a feature before being caught."*

---

## Measurements and their standing

### From `evidence/2026-08-23-read-cycle/`

| measurement | standing today |
|---|---|
| The fixture holds **2 courses, 22 obligations (15 from 2c03, 7 from 2aa4), 3 time points** (`PROVENANCE.md`) | **Superseded.** `architecture.md` §4, ruled 2026-08-28: *"a fresh extraction from source found **14** for 2c03, and the old count included a row the graveyard forbids (recurring tutorial attendance), so 22 is not reachable by re-running the old route."* The acceptance criterion moved from 22-across-two to one course's real obligations |
| **19 of 22 obligation rows and both course rows carry `notes` content** with no destination in the current schema (`PROVENANCE.md`; independently recomputed by the 08-25 citation check) | Stands as a fact about that fixture. Its consequence - the re-transcription being judgment rather than transcription - was overtaken when the fixture was superseded |
| **Three of six launch-shaped values are synthesized, not observed**, all tracing to one accident: 2aa4's Avenue page was deleted after the fact (`PROVENANCE.md`) | **Stands, and is the reason the fixture is not a golden set.** `schema.md`'s changelog, 2026-08-27, records the fixture being *"rejected as a golden set"* |
| The fixture is written to a schema that no longer holds: `status`, `workload`, `count`, `source_ref`, `manifest`, `offering_term`, `prereq`, `obligation.notes` - every one in `schema.md` §7, the graveyard | Stands. Verified: all eight are in `schema.md` §7 today, under a do-not-re-add rule. `offering_term` and `prereq` are reaffirmed by Billy's 2026-08-30 ruling 1 for v1, with the cross-domain requirement deferred to v2 |

### From `evidence/2026-08-25-refound-and-migration/`

All are measurements about the repo's own mechanics rather than about the domain, so none has a home in `records/domain/` or `records/spec/` by construction.

- **72 registry entries moved; openclaw's validator went from 113 to 41 and exits clean.** It failed once first, *"on exactly the ref this migration was predicted to break."*
- **Five citations sampled and read at the source: 0 wrong, against the project's own measured baseline of 4 wrong in 20.**
- **`records/` was a negative definition** - built by asking *is this durable?* - and *"the cost was countable: 4 of 9 records carried `standing: mixed`, a label that cannot be acted on."* Named as the same shape as `obligation.notes`, which the non-overlap rule killed. That shape argument **did** reach a record: `schema.md` §7's `obligation.notes` row carries it.
- **The purge would have destroyed one fact outright** - the do-not-present-a-generated-description-as-a-quotation finding existed only in `CLAUDE.md`, and `findings/ingestion-probe.md` was created to hold it. `records/findings/` is outside my boundary.
- **A cold-start subagent found six defects, every one real**, in a repo that had just passed its own five acceptance criteria.
- **The mechanism's first finding about itself:** *"'Closed' must mean the sitting ended, not that a unit of work did."*

**One measurement here has standing that outlives the container**, from `evidence/README.md`: *"**Most of this project's measured numbers are NOT auditable from this checkout.** The evidence behind them stayed in the openclaw checkout by ruling… That is a weaker property than auditable-here, and a reader who wants to check a number has to go there."* Any successor inherits this. It is not a term and not a decision, so it has no destination among the four - but it is the correct caveat on every number quoted from fall26.

### From `evidence/2026-08-26-interface-contract/`

| measurement | standing today |
|---|---|
| **The field inventory: 31 fields on four entries; 2 have all four; 21 of 31 have no write rule; 7 write-rule holes on nobody's list; 4 direct contradictions; 4 ruled invariants with no enforcement point; 9 of 31 fields no mechanism reads** | **Largely superseded.** The field set changed shape (opaque ids, `kind` discriminator, `category` rename, nullable bools, `done_by`), and `spec/write-rules.md` now exists as a real record. The **method** survives and is what this pass is built on |
| **Two independent sweeps returned 54 and 51 findings; this session opened 9 passages itself and compared them character by character; all 9 matched at the reported line numbers** | Stands as the strongest verification in the three sittings. It is why `migration-gaps.md` §1 can be relied on |
| **`records/spec/` stated the opposite of a ruling in 7 verified places**, then re-sorted under H1: **1 dissolves, 1 softens, 5 survive - and only 1 of the 5 is input-versus-output** | **Superseded by repair.** All five have since been dispositioned in `schema.md`'s changelog: `progress.state`'s vocabulary and per-kind rendering (2026-08-28), `parts` (2026-08-27), `finished_by` → `done_by` (2026-08-27), `obligation.name` (2026-08-28 via `model.md` §7.1). Recorded because the **re-sort** is the durable part, not the list |
| **The dominant failure mode is the one this project already named: standing upgraded by placement.** Verified in both directions - `closure` and `nodes_without` `[R]` in the ledger and agent-drafted in the spec; the JSONL format *"agent proposal, not ruled"* with **SQLite considered and set aside**, and neither the standing nor the rejection migrated | **The failure mode stands and recurs.** `spec/write-rules.md`'s own 2026-08-28 changelog catches itself doing it: *"Sitting in a `records/spec/` table was giving an agent recommendation `ruled` standing by placement."* The **SQLite rejection** is still in no graveyard I can see: `schema.md` §7 does not carry it and `architecture.md`'s graveyard is empty |
| **Blind review: implementability lens 17 findings, 4 blocking; writing-and-reading-agent lens 31 findings, 6 blocking; eight defects reached independently by both** | Stands as the sitting's method result. The eight are all dispositioned or superseded except the V8 five |
| **The largest finding is an absence: nothing anywhere defines what gets an obligation row.** *"What counts as a part"* appears **four times** across four records as a named owed item; **"what counts as an obligation" appears zero times** | **Stands definitionally**, answered behaviourally. See decisions.md #1 above |
| **The three `sticky_note` category values do not survive their own data.** Over the 11 notes in `evidence/2026-08-26-slice-1-build/fixture.json`: `policy` **8** · `format` **2** · `requirement` **1**. The ruled value `correction` has **zero** instances; `erratum` zero | **Landed.** `schema.md` §4 and §9 item 2 both carry it: *"across the 11 notes that exist, one value holds 8 of them and the boundaries between the others do not reproduce."* **Hazard worth naming:** at least two different eleven-note sets are now in play - this one, and the 2c03 corpus counted in `ring-0.md` §7 (4 hang on the course, 7 on obligations) and `model.md`'s 2026-08-28 changelog (87-278 characters). `schema.md` §4's *"one value holds 8"* traces to **this** sitting's fixture. A later reader should not assume the two sets are the same |
| **The strongest pattern in the 11 is not a topic taxonomy at all: 8 of 11 are footnotes on a typed field that could not carry the whole statement.** The weight-bound note because `grade_share = 30` is a bound read as a number · the weighting note because *10/10/30 or 0/0/50* is not a scalar · the snow-day and tutorial-attendance notes because `count` was dropped · the team-formation note because `due` is null and week-relative. Reported over n=11, single author; **no mechanism proposed from it** | **HOMELESS and live.** I found nothing carrying this in `records/domain/` or `records/spec/`. It bears directly on two live things: `sticky_note.category`'s owed write rule (`schema.md` §9 item 2), whose failure to find a topic taxonomy this observation explains, and Billy's 2026-08-30 ruling 7 - *two conflicting statements must never coexist in the system* - because a footnote-on-a-field is the shape in which a second statement about one value gets stored. **Destination: not an ADR and not a term; it is an observation that should reach whoever writes the `category` rule.** Carried here rather than proposed as a mechanism, exactly as its author left it |
| **There is no corpus of real sticky notes to measure the length bound against** - the only sample is 11 notes written by one agent from a field that had already been deleted | **Superseded.** `model.md`'s 2026-08-28 changelog measures real notes at 87-278 characters and falsifies §10.5's *real samples are short* premise |
| **Ten things neither sweep could find anywhere, called genuine absences rather than migration losses** | Five are now answered (`course.id` supplied · annotation ids by assignment · id-follows-rename by *minted once* · read-time default owner = presentation · `land()`'s place in the build). **Five remain**: `schema_version` mismatch behaviour · absent-key versus present-and-null · `Diff`'s shape · an enforcement point for *a stored `done_by` always means he chose it* · a measured number for the length bound. The last is `schema.md` §9 item 3; the other four are V8-class |

---

## Likely superseded by later sittings

Mine are the earliest three sittings. Where a finding looks overtaken by the 08-27 or 08-28 work another agent is reading, it is named here rather than chased.

| finding of mine | what would overtake it |
|---|---|
| The annotation id scheme, and every consequence drawn from it - the construction-order deadlock, the ordinal collision, *"`land()`'s contract differs by node kind"* | The **opaque monotone serial** ruling, `schema.md` changelog 2026-08-28. Already visible in the record; named here only because the 08-26 material reads as current |
| The whole `parts` Position A / Position B apparatus, and the sealed §9 of `plan/write-rules.md` | Billy 2026-08-27 (concepts) and `spec/write-rules.md` §3.4 (2026-08-28), which supplies the actual test: *a concept worth capturing because it might occur elsewhere*. 50 candidate strings became 28 on one real course |
| The `progress.detail`-with-no-state deadlock and H5's ask | `progress.state` becoming non-nullable, 2026-08-28, plus Billy's 2026-08-30 ruling 4 |
| The fixture's 22 obligations as an acceptance target | `architecture.md` §4, 2026-08-28: one course, 14 obligations |
| `migration-gaps.md` §2.1's `summary` gap, and V2's `model.md` §7.2 banner | `architecture.md` §5 and `model.md` §7.1's 2026-08-28 settlement. **The banner itself is what may not have been overtaken** - flagged, not chased |
| The blind review's finding that no node-kind discriminator exists | Ruled `kind` on 2026-08-27; landed on all four kinds |
| The 08-25 sitting's entire methodology layer - cycles, the four modes, the 200-line cap, `standing: mixed`, the record classification by what-can-change-it | The container itself. These are properties of a standalone repo run by a human. **Destination for all of them: Not carried** |
| H2's versioning rule | Billy's 2026-08-30 ruling 9, which defers the hypothesis gate outright |
| H6's *the log IS the store* | Billy's 2026-08-30 ruling 6 on the nature of the RAG store, which appears to close it. Not adjudicated |

---

## Coverage

**Read in full, in the original:** all four target paths, every file in them, including the non-markdown `fixture.json`. 1,108 lines total against the brief's stated 1,043; the difference is `fixture.json`, which the brief counted as part of an 11-line directory.

**Record check performed against:** `records/domain/model.md`, `records/domain/domain-design.md`, `records/spec/architecture.md`, `records/spec/design.md`, `records/spec/ring-0.md`, `records/spec/schema.md`, `records/spec/write-rules.md`. For every "no home" claim I name the record **and the section** I checked, not merely that a grep failed.

**What I could not check, and it scopes the results.**

- `records/plan/` and `records/archive/` were outside the boundary. `schema.md` and `architecture.md` cite `records/plan/backlog.md` by item number as the home for owed items, so several V8-class findings plausibly live there. **Every "no home" claim in this document means *not carried by `records/domain/` or `records/spec/`*.**
- `records/findings/` was outside the boundary. The 08-25 sitting created `findings/ingestion-probe.md` to rescue one fact from deletion; I could not confirm it.
- `STATUS.md` was outside the boundary. The 08-25 Handoff says *"Open and owned by Billy: the five items in `STATUS.md`"* and I cannot list them. The 08-26 Handoff's three Billy-owned items are listed above and two of the three are traceable to `schema.md` §9.
- `records/plan/write-rules.md` §2 and §7, which two of my voids concern, were outside the boundary. V3's effect is verifiable from `schema.md`'s changelog; V4's is not.
- `evidence/2026-08-26-slice-1-build/`, the **other** sitting on 2026-08-26, was outside the boundary. Its `fixture.json` is the source of the 11 notes, and my sitting's own Entry section records that it read that sitting's `NOTES.md` whole - which is what destroyed its eligibility to be the independent write-rules session.

**One contamination the source itself declares, carried forward.** `evidence/2026-08-26-interface-contract/NOTES.md` opens with it: the sitting's opening gate read **three of the five things** `plan/write-rules.md` §4 named as forbidden, before its mandate was opened. *"So this session cannot be the independent write-rules session."* What is lost is **corroboration value**, not the derivations themselves; what is unaffected is any **measurement**, since a measurement is not framed by having read a definition. Every `[measured]` item above is on the unaffected side of that line.

**Counts.** 6 rulings with no home (4 Billy, 1 half-landed Billy, 1 agent proposal). 2 live voids of standing records, of which 1 is squarely mine and 1 is adjacent to a later sitting. 5 uncorrected review findings whose subject still stands. 5 live questions addressed to Billy from `decisions.md`, plus 1 unruled fact type (`preference`) and 1 unlisted Billy-owned item (`grade_share`'s name). 12 abandoned steps recorded so none is mistaken for a ruling.
