# The `records/plan/` survey - what the migration's scoping excluded

**Read in full, including changelogs:** `fall26/records/plan/backlog.md` (69 lines) · `fall26/records/plan/application-tier.md` (154 lines) · `fall26/records/plan/write-rules.md` (141 lines).

**Read only to resolve cross-references:** `fall26/records/domain/model.md` · `fall26/records/domain/domain-design.md` · `fall26/records/spec/schema.md` · `fall26/records/spec/architecture.md` · `fall26/records/spec/design.md` · `fall26/records/spec/write-rules.md` · `fall26/records/spec/ring-0.md`.

**Boundary observed.** No `records/archive/`, no `records/findings/`, no `evidence/`, no openclaw path, no other repository, and no source code. Where a `plan/` claim asserts something about `app/src/**` (B22, B23, B28, B29), the claim is reported as the record states it and marked **unverified within this boundary** - checking it would have required reading code.

**Repo state.** `fall26` is on branch `design/course-level`; `records/` is stated to be identical to `main`. `backlog.md`'s newest changelog entry is 2026-08-28; `application-tier.md`'s only changelog entry is 2026-08-27; `plan/write-rules.md`'s only changelog entry is 2026-08-26 with two in-body amendments stamped 2026-08-27.

**Nothing here is adjudicated.** Every open question is left open for Billy.

**One correction to the brief that commissioned this pass, stated up front.** The brief says *"`records/spec/schema.md` cites `records/plan/backlog.md` by item number as the home for owed items."* Partly right, and the "owed items" half is wrong in a way worth knowing. `schema.md` §9 (*Still owed*) carries five owed items and **cites `backlog.md` nowhere**; the two tiers keep separate owed lists. What actually cites `backlog.md` is four scattered references, three by item number:

| citing record | line | cites | for what |
|---|---|---|---|
| `spec/schema.md` §4.6 | 134 | `backlog.md` **B19** | `look_at`'s return shape is owed to the presentation record |
| `spec/schema.md` §8 | 194 | `backlog.md` (no item number) | the load-time construct pass is "parked at" the backlog - this is **B24** |
| `spec/architecture.md` changelog 2026-08-28 | 127 | `backlog.md` **B20** | where the withdrawn composed-summary recommendation went |
| `spec/write-rules.md` §3.4 | 98 | `backlog.md` **B27** | the empty Final Exam `parts` as the live instance of the one-off cost |

So the spec tier resolves into `plan/backlog.md` at four points, and **two of the four cite items the backlog itself marks struck through and dissolved** (B19 is live; B20 is `~~B20~~`, dissolved). The mapping below is what a reader needs.

---

## The backlog, item by item

`backlog.md`'s own header states its standing: *"conditions: none. Everything here is known and parked. Nothing here blocks the build."* and *"weaker than this directory implies: this is a list of open items, not a plan. It has no order."* The creating ruling, quoted at the top of the file, is **Billy 2026-08-28**: *"the system is not trying to model real-world course structure perfectly; whatever is undecided and unimportant goes to the backlog."*

The file has four groups. Numbering is **non-contiguous and out of order within groups** (B21 sits above B22 in the third group; B25 and B15 sit in the second group among items numbered B13-B14 and B26-B27), and four items are struck through. B16 and B17 **do not exist anywhere in the file** - the sequence runs B15, B18-B29, with no record of what B16 and B17 were. That gap is not explained by any changelog entry.

### Group 1 - "The field set cannot hold it, and that is currently fine" (B1-B12)

Twelve rows, each with *what the material states* · *why it is parked* · *what would un-park it*. All twelve are live.

| # | what it says | standing | cited by `domain/` or `spec/`? |
|---|---|---|---|
| B1 | **Recurring obligations** - 2c03 tutorial attendance (5%, 10 of 12), 2da4's five labs, 2px3's weekly worksheets. `schema.md` §7 graveyards them and `count{done, of}`; the graveyard's stated ground is `n=1` and this is a second instance | live; un-parked by a fourth course confirming the pattern, or a read that needs the count | no. `schema.md` §7 carries the graveyard row and the `n=1` caveat, but does not cite B1 |
| B2 | **A bonus is not a share** - two +1 bonuses are additive, outside the 100 the real shares sum to; storing them in `grade_share` asserts something false | live; un-parked by *"any mechanism that reads `grade_share`"* | no. `ring-0.md` §6 independently makes the same observation (*"two rows carrying 1% are bonuses added outside the 100"*) without citing B2 |
| B3 | **Location** - three obligations state a venue (`LRW B1007`, `MSU Hub Loft`); no field, a note holds it | live; un-parked by the calendar projection | no |
| B4 | **Duration / end time** - `150 minutes`, `10:30 to 11:20`, `5:00 - 9:00 PM`; `due` stores only the left edge | live; un-parked by the calendar projection or `time_point` arriving | no |
| B5 | **Raw mark totals** - `out of 80`, `MCQ /30`; `score` and per-part weights are graveyarded | live; **"nothing foreseen"** would un-park it - the only item in the file with no stated un-parking condition | no |
| B6 | **The marking-scheme mechanism** - two schemes, higher one wins; a bool says *this number is one reading*, it cannot say which readings exist or that the choice is by maximum | live; un-parked by a planner that allocates against weights | no, though `schema.md` §3's `grade_share_conditional` row is the bool it describes |
| B7 | **MSAF weight transfer** - a conditional re-allocation from one obligation to another; slice 1 has one link kind, `annotation -> any Ref`, so obligation-to-obligation cannot be expressed | live; un-parked by slice 2 | no. `design.md` §3.3's LinkKind table is the source of the one-row claim |
| B8 | **The per-assignment late cap of 3** - the course-level 12 works as a note; the per-obligation half has no home short of duplicating prose nine times | live; un-parked by a planner that models the budget | no |
| B9 | **Deliverable structure** - most assignments owe two named artifacts (`macid_a6_code.zip` with `src/q1`, `macid_a6_written.pdf`); `parts` carries concepts, not deliverables | live; un-parked by the artifact layer, slice 2 | no |
| B10 | **Course-level facts with no field** - instructor, term boundaries (`01/05/2026 - 04/07/2026`), units, prerequisites, antirequisites, the textbook; `course` has four fields and zero free text | live; term boundaries become load-bearing if read-time expiry is built | no |
| B11 | **`course.prereq`'s graveyard justification is falsified** - `schema.md` §7 does not carry it because it is *"null for both courses in the fixture"*, but 2c03 states `SFWRENG 2DM3`. *"The conclusion may stand on other grounds; the stated ground does not"* | live; un-parked by a second domain | **no, and this is the notable one.** `schema.md` §7 line 17 still reads *"`course.offering_term` · `course.prereq` - Not carried: null for both courses in the fixture"*. The falsified justification stands uncorrected in the spec |
| B12 | **Is the IDEA Conference a `time_point` rather than an obligation?** `schema.md` §7 names "a conference" as one of `time_point`'s three instances | live; un-parked by `time_point` arriving | no. `schema.md` §7's `time_point` row names the three instances; `ring-0.md` §7 repeats that `time_point` is not in slice 1 |

### Group 2 - "Decided by silence, revisit only if it bites" (B13, B14, ~~B15~~, ~~B25~~, B26, B27)

| # | what it says | standing |
|---|---|---|
| B13 | **`sticky_note.category`'s vocabulary.** Two independent passes produced two non-overlapping value sets (`policy/logistics/clarification/erratum/correction/scope/provenance` vs `policy/format/requirement`). *"No rule; the field stores what it is given"* | live. **Carried in the spec tier too**: `spec/write-rules.md` §4 marks `category` **OWED** with the same two-passes reason, and `schema.md` §9 item 2 makes it *blocking a writer* |
| B14 | **What `origin` means.** The schema's prose says *how the claim was obtained* (`stated`/`asked`/an announcement); *"both independent passes reached for what document class it came from instead. That agreement is evidence about the field's real use"* | live. **Carried**: `spec/write-rules.md` §4 marks `origin` **OWED** with the same wording |
| ~~B15~~ | **Dissolved 2026-08-28, not answered.** A naming convention was owed only because the id was minted from the name; with an opaque assigned id the name carries no addressing load | dissolved. Fully carried by `spec/write-rules.md` §3.1 and `schema.md` §1.1 |
| ~~B25~~ | see below | ruled, not parked |
| B26 | **`application-tier.md` §4's slice-3 criterion says a second current progress record is REJECTED; the implementation upserts.** *"The move to the service was right and is recorded; the change from reject to replace is not. A caller expecting a refusal it can turn into a confirmation gets a silent overwrite"* | live. **Verified inside the boundary**: `application-tier.md` §4 Slice 3 does say *"a second current record on one target"* must be rejected, while §2.2 T8 records *"pass - `setProgress` upserts"*. The two halves contradict each other inside one plan record. `schema.md` §4.5 says only *"one current value per target"* enforced at *"the service"* and does not say whether that is a refusal or a replacement - so the spec tier does not settle it either |
| B27 | **The Final Exam's `parts` is empty and the instruction to fill it was lost.** Billy left `"_note: this should carry the general concepts the exam carries"` in the corpus; the fixture stores `[]` and an acceptance test asserts that is correct. *"The instruction now lives only in an evidence file that is off the reading path"* | live, and **partially discharged**: `spec/write-rules.md` §3.4 names B27 as *"the live instance"* of the one-off cost and rules it *"becomes actionable rather than parked: an exam's concepts are the course's concepts, so they recur and the rule keeps them."* The rule now says what to write; nothing records that the row was written |

### B25 - what it says, whether it settles anything, and its date

The item, quoted whole from `backlog.md` (group 2, struck through):

> ~~B25~~ **Ruled 2026-08-28, not parked.** The Final Exam's `due` is null and the provenance note is gone: an inferred value is asked about, not stored and annotated (`write-rules.md` §1.1), and `schema.md` §7 names this row. Kept here as the record of a blocking item that was resolved rather than deferred

And its changelog entry, `backlog.md` changelog, **2026-08-28, attributed to Billy, standing `ruled`**:

> 2026-08-28 - **B25 closed by ruling rather than parked**, and the corpus's Final Exam corrected: an inferred value is asked about, not stored with a note explaining the inference. This also removes the one note that violated the write rule the same corpus was used to author. - Billy - ruled

**Does it settle anything?** It settles the same proposition as `spec/write-rules.md` §1.1, on the same date, by the same author - **it is not an independent settlement, it is the read-side record of one ruling**. §1.1 reads:

> When a source does not state a value and the agent infers one, it **asks the user**. It does not write the inference into a note beside the field. […] **An update is an update.** A correction changes the field; it does not accumulate commentary beside it.

B25 adds three things §1.1 does not carry: (a) the **coarse-date consequence** - the Final Exam's `due` stays null, which `schema.md` §7's *coarse dates* row independently states (*"a date that is not fixed is null. The term's largest obligation therefore stores a null `due`"*); (b) the observation that **the corpus used to author the write rule was itself violating it**; (c) the framing that this was a **blocking item resolved rather than deferred**.

**Its one defect, and it is a citation defect.** B25 cites `` `write-rules.md` §1.1 `` **with no directory prefix**. Read from `records/plan/`, that resolves to its own sibling `records/plan/write-rules.md`, which has a §1 (*The question, bounded*) and **no §1.1 at all**. The intended target is `../spec/write-rules.md` §1.1. B15 has the identical defect, citing `` `write-rules.md` §3.1 ``. Every other backlog cross-reference in the file is correctly prefixed (`../spec/schema.md`, `../domain/model.md`, `architecture.md`). So **two of the file's four ruling-bearing citations point at the wrong write-rules record**, and both point at the one whose name collides.

### Group 3 - "Known defects in what is built" (~~B21~~, B22, B23, B24, B18, B19, ~~B20~~, B28, B29)

Listed in the file in that order - it is not sorted.

| # | what it says | standing | cited by `domain/` or `spec/`? |
|---|---|---|---|
| ~~B21~~ | **Dissolved 2026-08-28.** The defect was that an id freed by a delete could be re-minted and silently adopt links still pointing at the old record. `spec/schema.md` §1.1's id is now monotone and never reused, a delete included. *"The fix landed as a property of the scheme rather than as the retired-id set this item proposed"* | dissolved | no, but `schema.md` §1.1 carries the fix verbatim (*"It is never reused, a delete included"*) |
| B22 | **`flush()` rewrites both files whole on every service call**, so landing a course is O(n²) in bytes. 27 records is 54 full writes. Un-parked by a batch caller: `land()` over a pasted screenshot is 22 rewrites | live. **Unverified within this boundary** (code claim) | no |
| B23 | **The temp-and-rename write is not concurrency-safe.** Fixed `${path}.tmp`, so two processes flushing at once share it; no fsync before rename. *"Un-parked the moment the CLI can be run twice, which is what its own docstring names"* | live. **Unverified within this boundary** | no |
| B24 | **A load-time construct pass.** `schema.md` §8 no longer claims validation happens at load, but nothing performs it: *"a malformed line loads clean and survives the next flush."* Belongs to the application tier since persistence has no field meaning. Un-parked by the composition root, the CLI | live | **yes, reciprocally.** `schema.md` §8 line 194 ends *"it is parked at `../plan/backlog.md`"* - without the item number, so a reader must scan the file to find B24 |
| B18 | **The store has no tier.** `architecture.md` §1's table has three rows and none is the store, yet the purity cut is a boundary against it. Slice 3 | live | no. `architecture.md` §6 does say the store *"may be Python without crossing a tier boundary"*, which sharpens the gap rather than closing it |
| B19 | **`look_at`'s return shape has no home.** `schema.md` §4.6 no longer states one; the shape is now stated **nowhere**, *"which is correct but not free: it is owed to the presentation record, along with where a node's own typed fields arrive"* | live | **yes, twice.** `schema.md` §4.6 line 134 and `schema.md`'s changelog line 217 both cite B19 by number |
| ~~B20~~ | **Dissolved 2026-08-28, not parked.** There is no summary object at the obligation level; `architecture.md` §5's recommendation was withdrawn, so its "broken inputs" were never inputs to anything. *"Kept as the record of a question removed rather than answered"* | dissolved | **yes.** `architecture.md`'s changelog line 127 cites B20 by number as where the withdrawn recommendation went |
| B28 | **The code has `progress.state` nullable; the spec no longer does.** `app/src/application/kinds.ts:153` is `ProgressState \| null`, `kinds.ts:200` rejects a `detail` with no `state`, `annotations.test.ts:66` asserts null-with-detail throws - *"all correct against the old rule."* Under `spec/schema.md` §4.5 there is no unknown state at all, so the null arm goes and absence carries `not_started`. Un-parked by the next build cycle touching the application tier | live. **Code claim unverified within this boundary**; the spec half is verified - `schema.md` §4.5 says `state` is *"not nullable"* and *"There is no unknown state"* | no |
| B29 | **`ids.ts` still implements the retired `<course>-slug(name)` scheme.** `slug`, `mintId`'s collision suffix and `mint`'s `coursePrefix` seed all belong to the scheme `spec/schema.md` §1.1 replaced. *"The counter has to live somewhere persistence can hand out monotonically, which is a decision this ruling did not make"* | live, and it **contains an undischarged decision**, not just a defect. **Code claim unverified within this boundary** | no |

### Group 4 - Graveyard

*Empty.* Nothing has been removed from `backlog.md`.

---

## Rulings that landed only here

Nine. Each is quoted, dated, attributed, and followed by the `domain/`+`spec/` sections checked.

### 1. The backlog's own creating ruling - the disposition rule

> *"the system is not trying to model real-world course structure perfectly; whatever is undecided and unimportant goes to the backlog."* - `backlog.md` header, **Billy, 2026-08-28**, standing `ruled`

**Checked:** `schema.md` §7 (the graveyard) and §9 (still owed) · `architecture.md` §3 (what the split rules) · `domain/model.md` and `domain/domain-design.md`. The graveyard carries per-field *not carried* verdicts; **no record in `domain/` or `spec/` carries the general disposition rule** that produced them. This is the most reusable thing in the directory and the one most likely to be lost with it: it is the rule that makes a corpus of parked items legitimate rather than a symptom of avoidance.

### 2. The ordering ruling, in Billy's own wording

> **[R] Billy, 2026-08-26:** *"write 规则要在 build 前，因为 verb 的 docstring / param def. 什么的都要按照 write 规则设计，这是 agent 直接会看到的."* - `plan/write-rules.md` §2.1

**Checked:** `architecture.md` §4 carries the *consequence* - *"The 2026-08-26 ruling that write rules precede the build still holds and its target changed: they precede the presentation tier, not the application tier"* - and `spec/write-rules.md` says the mandate is *"frozen at `../plan/write-rules.md`"*. **The sourced wording, and the reason inside it (a docstring is what the agent directly sees), exist only in `plan/write-rules.md` §2.1.** The section is explicitly titled *"kept for its wording"*.

### 3. A link has no update; update is detach plus attach

> *"**A link has no update**, and this is derived rather than chosen: its identity is the whole tuple `(from, to, kind, role, locator)` (`design.md` §3.3), so changing any part of it produces a different link. Update is detach plus attach."* - `application-tier.md` §2.1, agent-drafted 2026-08-27

**Checked:** `design.md` §3.3 states the natural-key identity and rejects a surrogate id, but **never states the consequence for the method set**. `architecture.md` §7's re-homing table does not cover links-as-CRUD. The derivation exists only here.

### 4. Delete is a plain delete, and the applied cascade cases

> *"**Delete is a plain delete and dangling is legal.** […] So deleting a course does not cascade to its obligations, and deleting an obligation does not remove notes about it; the recovery is the validation pass over the link set that §3.2 already owes."* - `application-tier.md` §2.1

**Checked:** `design.md` §3.2 property 3 carries the general principle (*"A ref may name something that is not there, so a ref is not a foreign key and deleting a record does not have to cascade"*) and owes the validation pass. **The two concrete cases** - course→obligations, obligation→notes - **are stated only here.**

### 5. The two derivations' shared hole - neither route can produce a repair method

> *"**The hole this names:** Route A enumerates over fields and Route B's eleven traces are all success paths. Neither generates a correction, a deletion, a re-land, or a crash - so between them they cannot produce a method that exists to repair a mistake. Every entry above is one."* - `application-tier.md` §2.4b, agent-drafted

With the sharpest instance named in the same table:

> *"`annotations.retarget` - **neither.** […] **This is the method that broke the one-current-value-per-target invariant** - exactly what this rule exists to catch"*

**Checked:** `architecture.md` §7 · `schema.md` §4.5 (which states the invariant and where it is enforced) · `design.md` §3.4. **No record outside `plan/` carries the finding that success-path derivation systematically omits repair operations**, nor that `retarget` was the method that broke the invariant. This is a methodological finding about how the method set was derived, and it generalises past this project.

### 6. Read-back counts only through the service methods

> *"**Read-back counts only through the service methods.** A test that reads the JSONL directly, or that reaches the repository past the service, does not satisfy any criterion."* - `application-tier.md` §5

**Checked:** `architecture.md` §4 says *"landed and read back through the operations rather than hand-written"* and defines *"Landed"*. It does **not** rule out reading the JSONL directly in a test, nor reaching past the service to the repository. The stricter form is plan-only.

### 7. A row that does not fit is a spec failure, not a fixture patch

> *"**The fixture migration happens before the build and is then frozen.** Discovering mid-build that a real row does not fit the field set is **not** a fixture patch: it means the spec is wrong, and the correct move is to close this cycle and open a design one."* - `application-tier.md` §5

**Checked:** `schema.md` §7's header (*"do not re-add without a new ruling"*) governs re-adding fields; nothing in `domain/` or `spec/` states what happens when real material does not fit. This is a **constraint on how a build cycle terminates**, dressed as a plan pre-registration.

### 8. An ambiguous outcome resolves against the proposition

> *"**An ambiguous outcome resolves against the proposition.** 'It basically round-trips' is a fail."* - `application-tier.md` §5

**Checked:** no equivalent anywhere in `domain/` or `spec/`. Plan-only.

### 9. Migrated fixture is code, not evidence

> *"The migrated copy is a test input and therefore **code, not evidence**; `evidence/2026-08-26-slice-1-build/fixture.json` is never edited and stays as the provenance."* - `application-tier.md` §6

**Checked:** no equivalent in `domain/` or `spec/`. The evidence/code distinction for a derived fixture is stated only here.

### Near-misses, checked and found to be carried elsewhere

Recorded so the "only here" list is not padded:

- **B25's ruling** - carried by `spec/write-rules.md` §1.1, same date, same author. See above.
- **"我不想对分项建模"** (`plan/write-rules.md` §3) - carried by `schema.md` §7's *per-part weights and per-part scores* row, with the measurement.
- **"Provenance does not confer immutability"** (`plan/write-rules.md` §3) - carried by `schema.md` §4 line 88 verbatim, and by `domain/model.md` line 527 as the original `[R]` Billy 2026-08-23.
- **`sticky_note.kind` is an open set, deliberately not an enum** - carried by `schema.md` §9 item 2 and `spec/write-rules.md` §4.
- **`parts` carries concepts** - ruled and carried by `spec/write-rules.md` §3.4 and `schema.md` §9 item 1; `plan/write-rules.md` §9 records the *pre-ruling* two positions, which is history, not a live ruling.

---

## Owed items and who owes them

Twelve, plus the B-series un-parking conditions already tabled above. Ordered by whether Billy's 2026-08-30 rulings discharge them.

### Discharged, wholly or in part, by Billy's rulings of 2026-08-30

| owed item | source | who owed it | discharged by |
|---|---|---|---|
| **`sticky_note.body`'s length bound - a measured number** | `plan/write-rules.md` §3 (*"the number has never been measured, and the number is Billy's"*), §6, acceptance **c3**; `schema.md` §9 item 3 | **Billy**, on a measurement an agent produces | **Not discharged.** Ruling 9 defers the hypothesis gate, and `spec/write-rules.md` §4.2 has since reframed the bound as following *"from what a rendered node can carry, not from a number chosen in advance"* - which changes the method, not the owing. Still live, still Billy's |
| **B12 - is the IDEA Conference a `time_point`?** | `backlog.md` B12 | un-parked by `time_point` arriving | **Discharged as dormant** by ruling 3: `time_point` is out because its reader, the calendar projection, is out. The item cannot wake until the projection does |
| **B3, B4 - location, duration/end time** | `backlog.md` | un-parked by the calendar projection | **Same.** Ruling 3 keeps the projection out, so all three stay parked with a named precondition rather than an open question |
| **B2 - the bonus/share falsehood** | `backlog.md` B2 | un-parked by *"any mechanism that reads `grade_share`"* | **Discharged as dormant** by ruling 2: *`grade_share` is reference only, never an input.* No mechanism reads it, so the false assertion still has no reader |
| **B28 - `progress.state`'s null arm** | `backlog.md` B28 | the next build cycle touching the application tier | **Reinforced, not discharged**, by ruling 4: `not_started` is the default *precisely so the agent does not keep asking*. The rationale is now stronger than when B28 was written; the code change is still owed |
| **`hours_estimate` / size** | `schema.md` §7 graveyard row; `backlog.md` does not carry it | - | **Ruled** by 2026-08-30 ruling 2: not quantifiable, judged from progress and load. Confirms the graveyard row rather than reopening it |

### Still live and undischarged

| owed item | source | who owes it | what would discharge it |
|---|---|---|---|
| **Is `obligation.course` updatable?** | `application-tier.md` §7.1 - *"**Recommended:** set at create, not updatable […] Needs a ruling before slice 2 closes"* | **Billy** | A ruling. **This is the sharpest live one**: `spec/write-rules.md` §3 line 55 explicitly points back at it - *"still open at `../plan/application-tier.md` §7.1 as a recommendation with no ruling. The code implements the recommendation; this record does not decide it"*. The spec tier has deliberately refused to hold the answer and delegated it to the excluded directory. **If `plan/` does not migrate, this question has no home at all.** |
| **Is `parts` updated as a whole list, or per element?** | `application-tier.md` §7.2 - *"**Recommended:** whole-list replacement"* | Billy or the next build cycle | A ruling. §7's header says both *"surfaced from §2.1 and neither blocks slice 0 or 1"* |
| **B29's undischarged decision - where the id counter lives** | `backlog.md` B29 - *"The counter has to live somewhere persistence can hand out monotonically, **which is a decision this ruling did not make**"* | the next build cycle, but the placement is a design choice | A ruling on placement. `schema.md` §1.1 rules the id is *"opaque, monotone, and assigned by the system"* and says nothing about where the counter lives |
| **B26 - reject or replace on a second current progress record** | `backlog.md` B26 | Billy, or whoever closes the contradiction | A ruling. Neither `application-tier.md` (which contradicts itself) nor `schema.md` §4.5 settles it. Bears directly on ruling 7 (*two conflicting statements must never coexist*) - a silent overwrite is the write-side of persisting a conflict as noise |
| **B19 - `look_at`'s return shape, and where a node's own typed fields arrive** | `backlog.md` B19; cited by `schema.md` §4.6 and its changelog | the presentation record, which does not exist | The presentation record. **Blocked by ruling 9**, which defers the hypothesis gate on the grounds that there is no exposed CLI surface and product-facing verb names are undecided |
| **B18 - the store has no tier** | `backlog.md` B18 | slice 3 | An `architecture.md` §1 table row |
| **B24 - the load-time construct pass** | `backlog.md` B24; `schema.md` §8 defers to it | the composition root, i.e. the CLI | The CLI existing. Also blocked by ruling 9 |
| **B27 - the Final Exam's empty `parts`** | `backlog.md` B27; `spec/write-rules.md` §3.4 | whoever re-extracts the row | §3.4 has made it actionable; **nothing records that the row was actually written**. This is a live, cheap, undischarged item |
| **The four write rules in the mandate's acceptance §7 (c1-c7)** | `plan/write-rules.md` §7 | the session that executes the mandate | Two of four are now landed by `spec/write-rules.md` (`parts` §3.4, `body` §4.2 in shape if not in number); `category` and `origin` remain **OWED** in both records |
| **The presentation-tier home for the three how-to-write rules** | `plan/write-rules.md` §7 Output - *"there is nowhere to put them yet because the presentation tier has no records. Whoever executes this mandate creates that home"* | the presentation cycle | **Partly overtaken by events**: `spec/write-rules.md` exists and holds `parts`, `name`, `optional`, `body` rules, marked *"presentation tier"* in its own condition line. So the home was created **at the exact path the mandate ruled out**. See the comparison below |
| **`architecture.md` §5's content split - is the course level worth a call?** | `ring-0.md` §7 - *"Unruled, and it is the presentation cycle's question"* | the presentation cycle | Named here because `plan/` is the only place a presentation cycle is scheduled, and the schedule is the part that does not migrate |
| **B5 - raw mark totals** | `backlog.md` B5 | - | **"nothing foreseen."** The only item in the corpus parked with no wake condition. Worth surfacing: an item with no precondition is not a deferral, it is a rejection that has not been written as one |

---

## Voids, corrections and withdrawals

Five. Two are `plan/` correcting `spec/`; **three are `spec/` having voided `plan/` without `plan/` being updated** - and the third of those is the whole reason the record is unsafe to read as current.

### V1. `application-tier.md`'s sole criterion has been overwritten, and the plan still asserts the old one

**`application-tier.md` §1**, written 2026-08-27:

> *"The application tier and the persistence tier, built until **22 real obligations** go in through the write methods and come back out through the read methods. That is `architecture.md` §4's surviving criterion, **and it is the only one**."*

The 22 recurs in §4 Slice 2 (*"All **22** obligations"*), §4 The whole, §6, and trace T4.

**`architecture.md` §4**, amended **2026-08-28, Billy, ruled**:

> *"**What survives unchanged as an application-tier test:** the field set holds **one course's real obligations** […] **Why one course and not the 22 across two that this criterion used to name.** The 22 came from a transcription that has since been superseded: a fresh extraction from source found **14** for 2c03, and the old count included a row the graveyard forbids (recurring tutorial attendance), so **22 is not reachable by re-running the old route**."*

**Does the other record still stand uncorrected?** Yes - `application-tier.md` carries **no changelog entry after 2026-08-27** and still states 22 in five places. The plan's own framing (*"and it is the only one"*) means its single criterion is now unmeetable as written. Anyone following this plan would be building to a number the ruling that created it has retired.

### V2. `application-tier.md`'s slice-0 criterion is voided by the packaging reversal

**`application-tier.md` §3 Slice 0** requires *"three packages with the dependency direction in their manifests"*, and **§4 Slice 0** makes it a pass criterion: *"Presentation's manifest does not list persistence, and an import of persistence from presentation fails to resolve."*

**`architecture.md` §6**, reversed **2026-08-28, Billy, ruled**:

> *"**The tiers are directories under one source root** […] The original ruling was *packages, not directories* […] **That ground turned out to be false under npm:** workspace dependencies are hoisted to the root, so any package resolves any other whether or not it declares it, and a manifest states an intent it cannot refuse. What actually refuses is `app/tests/boundary.test.ts`."*

**Does the other record still stand uncorrected?** Yes. And the failure compounds: `application-tier.md`'s **condition line** reads *"this plan is executable only while `../spec/architecture.md` §5-§7 stand."* **§6 is inside that range and no longer stands.** The plan states its own precondition, the precondition broke two days later, and the plan does not say so. It is the exact failure mode the plan's §4 header warns of - *"Recorded because a plan that predates the split still reads as authority"* - happening to the record that wrote the warning.

### V3. `plan/write-rules.md` §7's output instruction is contradicted by the record that now exists

**`plan/write-rules.md` §7 Output, CORRECTED 2026-08-27:**

> *"**`obligation.parts`, `sticky_note.category` and `annotation.origin`** are how-to-write knowledge […] **They do not land in `records/spec/` at all**, and there is nowhere to put them yet because the presentation tier has no records. Whoever executes this mandate creates that home; **it is not `records/spec/write-rules.md`**, which this section used to name and **which would have put presentation-tier rules inside the application tier**."*

**`spec/write-rules.md`** was created **2026-08-28, Billy, ruled**, at exactly that path, and holds a `parts` rule (§3.4). Its own condition line reads *"these are **presentation tier** (`architecture.md`)"* - so it acknowledges the tier and lands there anyway.

**Which stands?** The later record wins on date and on standing (Billy-ruled 08-28 beats an agent-drafted correction of 08-27), and it defuses the objection by labelling itself rather than by moving. But **the mandate's reasoning is not answered, only overridden**: `records/spec/` is the application tier per `architecture.md` §2, and a presentation-tier record now lives inside it. `plan/write-rules.md` §7 stands uncorrected and would tell a fresh reader that `spec/write-rules.md` should not exist.

### V4. B11 - `plan/` falsifies a standing justification in `schema.md` §7

**`schema.md` §7**, uncorrected:

> *"`course.offering_term` · `course.prereq` | Not carried: **null for both courses in the fixture**, and `offering_term`'s justification is another domain's need, in a domain that does not exist"*

**`backlog.md` B11:**

> *"**`course.prereq`'s graveyard justification is falsified** - §7 does not carry it because it is 'null for both courses in the fixture'; **2c03 states `SFWRENG 2DM3`**. The conclusion may stand on other grounds; the stated ground does not"*

**Does the other record still stand uncorrected?** Yes - `schema.md` §7 still prints the falsified ground with no marker. B11 is careful not to overreach (*"the conclusion may stand on other grounds"*), and Billy's 2026-08-30 ruling 1 supplies those other grounds: `course.prereq` **stays graveyarded for v1**, with the cross-domain requirement deferred to v2. So the **conclusion is now independently ruled and the false justification is still printed underneath it**. That is a live correction owed to `schema.md`, not to the successor.

### V5. B26 - `plan/` records a divergence between two of its own sections that `spec/` cannot adjudicate

Covered above. Recorded here because it is the one void whose two sides are **both inside `application-tier.md`**: §4's slice-3 criterion says reject, §2.2's T8 verdict says upsert. `schema.md` §4.5 states the invariant without ruling the failure mode, so nothing in `spec/` corrects either side.

---

## The two write-rules records compared

Two records, same filename, different tiers, different jobs, twelve days apart in origin. **Neither supersedes the other in general**, and the migration must not treat the name collision as a duplicate.

| | `records/plan/write-rules.md` | `records/spec/write-rules.md` |
|---|---|---|
| **What it is** | *"The write rules - **the mandate for a separate, independent session**"* | *"WRITE RULES - what an agent puts in a field whose legal values cannot be enumerated"* |
| **Written** | 2026-08-26, by the slice-1 build session, *"deliberately not the session that executes it"*; in-body amendments 2026-08-27 | 2026-08-28; changelog runs to 2026-08-28 |
| **Standing** | *"this is a **mandate**, not an answer. **Nothing in it is a write rule.**"* §2's ordering is Billy-ruled; everything else agent-drafted | *"every section marked OWED is a slot with no rule in it yet."* Four rules Billy-ruled, two owed |
| **Tier claim** | three of four fields are presentation, `body`'s bound is application (§2) | *"these are **presentation tier**"* (condition line) |
| **Contains** | the question · the tier assignment · the ordering ruling in Billy's Chinese · what is already ruled about four fields · a reading prohibition (§4) · the material bound (§5) · a two-stage procedure (§6) · seven acceptance criteria (§7) · out-of-scope (§8) · a broken seal (§9) holding two pre-ruling positions on `parts` | rules partitioned by kind and field, mirroring `schema.md`: §1.1 inferred-value · §1.2 OWED · §3.1 `name` · §3.4 `parts` · §3.5 `optional` · §4.0 render test · §4.2 `body` · plus OWED slots for `category` and `origin` |
| **Method** | derive in the abstract, from source material, by an independent cold session | *"Billy editing one course's extracted records by hand: the rule is what he did, and the before-and-after is the evidence"* |

### Where they agree

1. **The same four fields are the problem set.** `plan` §1 names `obligation.parts` · `sticky_note.kind`(→`category`) · `sticky_note.body` · `annotation.origin`. `spec` carries a rule or an OWED slot for each.
2. **`category` and `origin` are still unanswered, in both.** `plan` §3 says `kind` needs *"a discipline a writing agent applies, never a list"*; `spec` §4 marks both **OWED** with the two-non-overlapping-passes reason. `backlog.md` B13/B14 is the third copy of the same pair.
3. **A rule must be usable in a docstring.** `plan` §7 c6: *"Every rule is written so `land()`'s docstring can be drafted from it directly. If a rule cannot be said in a docstring, it is not finished."* `spec`'s rules are all written in that form.
4. **`body`'s bound follows from rendering.** `plan` §3 ties it to *"`domain/domain-design.md` §9.2's symmetry rule"*; `spec` §4.2 says *"the bound follows from what a rendered node can carry, not from a number chosen in advance."*
5. **The bound's number is Billy's.** `plan` c3 (*"The number itself is Billy's and must be left to him"*); `spec` §4.2 leaves it as owed; `schema.md` §9 item 3 keeps it owed.

### Where they diverge, and which is later on each point

| point of divergence | `plan/write-rules.md` | `spec/write-rules.md` | later, and standing |
|---|---|---|---|
| **What `parts` carries** | §9 SEALED: *two positions, neither ruled, neither authority* - Position A (size judged ordinally, agent-drafted) vs **Position B, Billy 2026-08-26 `[intuition]`**: *"很明显的是 parts 应该承载的是概念"* | §3.4 ruled: *"A part is a **concept worth capturing because it might occur elsewhere in the system**"*, with a kept/dropped table and a measurement (50 candidate strings → 28) | **`spec` is later** - Billy-ruled 2026-08-28, and its changelog notes the ruling was actually made 2026-08-27 in `schema.md`. `plan` §9 is now **history**: the record of the two positions before the adjudication |
| **Where the output lands** | §7: *"They do not land in `records/spec/` at all"*, and explicitly *"it is not `records/spec/write-rules.md`"* | exists at that path, self-labelled presentation tier | **`spec` is later** (08-28 vs 08-27) and wins by existing. `plan`'s objection is unanswered - see V3 |
| **How a rule is obtained** | §6: a cold independent session derives from nine handouts, writes stage 1 down before opening §9 | header: *"Writing them in the abstract **stalled for two months** - that mandate is frozen at `../plan/write-rules.md`"*; the rules came from Billy's hand edits | **`spec` is later, and it is a method reversal, not a refinement.** The mandate's whole independence apparatus (§4's reading prohibition, §6's two stages, §9's seal) was bypassed rather than executed |
| **`name`** | not in the problem set; `backlog.md` B15 owed a naming convention | §3.1: *"There is no system-owned naming convention, and one is not owed. Write the label the source uses."* | **`spec` is later**, Billy-ruled 2026-08-28, and it dissolves B15 |
| **`optional`, and whether to write a note at all** | absent from the mandate entirely | §3.5 (`optional` defaults to false unless a source states otherwise) and §4.0 (the render test: *"Is it worth being written down so that every time I look at this node, the note comes with it?"*, 20 candidate notes → 12) | **`spec` only.** Two rules the mandate never anticipated, both Billy-ruled 2026-08-28 |
| **The inferred-value rule** | **absent.** `plan/write-rules.md` carries no §1.1 and no cross-field section at all | §1.1: *"an inferred value is asked about, not annotated […] **An update is an update.**"*, Billy 2026-08-28 | **`spec` only.** Directly answering Billy's 2026-08-30 ruling 7: the write-side half exists **only** in `spec/write-rules.md` §1.1 and in `backlog.md` B25's summary of it. The `plan/` copy does **not** carry it, and the two backlog citations that appear to point at the `plan/` copy are the unprefixed-path defect described above |
| **The ordering ruling's wording** | §2.1, Billy 2026-08-26, in Chinese, with the destroyed-experiment reasoning | absent | **`plan` only.** This is divergence in `plan`'s favour and is listed in *Rulings that landed only here* #2 |
| **The seal** | §9 was sealed; the header says **the seal is BROKEN** - *"The 2026-08-26 build session read the sealed material during its own opening gate"* | n/a | `plan` only, and it is a process finding: the independence device failed on the same day the session that built it opened |

### The one-line summary a reader needs

**`plan/write-rules.md` is a frozen mandate that was never executed as written; `spec/write-rules.md` is the answer that arrived by a different route.** The mandate's *questions* are still the right questions - two of its four fields are still OWED in the record that superseded it - but its *procedure* has been overtaken and its *output instruction* contradicted. Migrating both without this note would present a reader with two live-looking records that disagree about where write rules belong.

---

## Sequencing, set aside

Listed rather than silently dropped. Each of these is ordering, slice assignment, or a criterion whose content is *when* rather than *what*. Per fall26's own instruction - *"there is no plan of record […] cite them, do not follow their order"* - none of it migrates.

**From `application-tier.md`:**

1. **§1's scope statement and its Not-covered list** - what is in this build versus deferred to a later one. The *reasons* attached to three items are structural and are handled under Destination proposals; the in/out assignment is sequencing.
2. **§2.2's eleven traces T1-T11 with their pass/partial verdicts** - a build-time completeness audit of a method set at one moment. The *findings* from doing it twice (§2.3, §2.4b) are not sequencing; the verdict table is.
3. **§2.1's coverage table with its per-kind pass/untested verdicts** - `name`'s update untested, `grade_share_conditional`'s update untested, `category`'s update untested. These are a snapshot of one codebase's test coverage.
4. **§2.4's freeze rule** - *"Frozen at the start of the build. Every row carries a verdict at the close."* This is a procedure for running this table in this build.
5. **§3's entire build order** - slices 0-3, *"vertical by entity, not horizontal by tier"*, and the record counts per slice. This is the single largest block of pure sequencing in the directory.
6. **§4's per-slice criteria** - Slice 0/1/2/3 acceptance sentences. The *rules* embedded in them (dangling refs reported not crashed, nulls read back as absent never as a default, `due` round-trips as stored with no resolution applied, progress's three construction rules) are already carried by `schema.md` §3, §4.5 and §8 or are proposed below; the slice attachment is not.
7. **§6's fixture-migration rename list** - `finished_by`→`done_by`, `kind_of_node`→`kind`, `kind`→`category`. A one-time migration of a file that does not migrate. `schema.md` carries the post-rename names.
8. **§7's "neither blocks slice 0 or 1"** - the *scheduling* half of the two open questions. The questions themselves are owed items and are carried above.

**From `plan/write-rules.md`:**

9. **§2's "this mandate runs when the presentation tier is designed, which is after the application tier is built"** - a scheduling claim, now doubly stale: the mandate did not run and the rules landed anyway.
10. **§4's reading prohibition** - the list of evidence files a cold session must not open before §7 is satisfied. It governs a session that will never convene, and it names paths outside this survey's boundary.
11. **§5's material bound** - *"One course: 2c03. Not five, not two"* with the verified-present file inventory of nine handouts and the exam skeleton. Local to that session's inputs. **One line inside it does not migrate as sequencing and is flagged**: *"**No midterm skeleton PDF is on disk**, contrary to what an older record assumes. Say so rather than inferring one"* - that is an instance of the inferred-value rule and it is already carried by `spec/write-rules.md` §1.1.
12. **§6's two-stage procedure and §7's acceptance c1-c7** - how the session runs and how it is judged. c6 (docstring-sayable) is a general criterion and is proposed below; c1-c5 and c7 are procedure.
13. **§8's out-of-scope list** - four exclusions scoped to a session that did not run.

**From `backlog.md`:**

14. **The un-parking conditions phrased as slice numbers** - B7 (*"slice 2"*), B18 (*"Slice 3"*), B9 (*"the artifact layer, slice 2"*). The *dependency* each states is real and is preserved in the item; the slice label is this project's ordering and does not travel.

**One thing that looks like sequencing and is not**, called out so it is not swept up: `application-tier.md` §5's four pre-registrations read as build procedure but three of them are constraints on how any build cycle terminates (rulings #6, #7, #8 above). Only the fourth - *"Progress cases are authored, and that is declared here rather than discovered later"* - is local.

---

## Destination proposals

Proposals only. Nothing is created; every one of these is Billy's to rule.

### `CONTEXT.md` - terms

| term | proposed one-or-two-sentence entry | source |
|---|---|---|
| **Backlog item** | A question that is known, parked, and cheaper to leave open than to answer, carrying the condition that would wake it. It is not a to-do and not an oversight. | `backlog.md` header + creating ruling |
| **Parked with no wake condition** | *(Flagged, not proposed.)* B5 is parked with *"nothing foreseen"*. Worth Billy's ruling on whether such an item is a deferral or an unwritten rejection, before the term is coined either way. | `backlog.md` B5 |
| **Dissolved item** | A parked item that ceased to exist because a ruling elsewhere removed the condition that created it, as distinct from one that was answered. B15, B20 and B21 are the instances. | `backlog.md` B15, B20, B21 and its changelog |
| **Repair method** | An operation that exists to correct a mistake - retarget, delete, re-land - as opposed to one that advances a success path. Named because no success-path derivation produces one. | `application-tier.md` §2.4b |
| **Write rule** | An instruction to the agent writing a field, stating what a legal value is and what the writer must be holding to produce one, for a field whose legal values cannot be enumerated. Distinct from the field's type, which says what a legal value *is*. | `spec/write-rules.md` header; `plan/write-rules.md` §1 |
| **Mandate** | A record that states a question and the conditions for answering it, and is explicitly not an answer - so nothing in it has ruling standing. | `plan/write-rules.md` condition line |

Deliberately **not** proposed as terms: *slice*, *ring 0*, *trace*, *coverage table*, *route A / route B*. The first two belong to records outside this survey; the last three are artifacts of one build's audit method.

### `docs/adr/` - decisions

Each meets all three tests - hard to reverse · surprising without context · a real trade-off.

**ADR-a. Undecided and unimportant questions are parked with a wake condition, not answered.**
The system does not try to model real-world course structure perfectly; a question that is cheaper to park than to answer goes on a list, and each item names what would un-park it. Hard to reverse because the entire disposition of the corpus depends on it and un-parking retroactively means re-deriving twelve fields' worth of justification. Surprising because a schema with a dozen known gaps reads as incomplete rather than as ruled. *(Source: `backlog.md` header, Billy 2026-08-28.)*

**ADR-b. A link has no update; changing any part of a link is detach plus attach.**
A link's identity is its whole tuple `(from, to, kind, role, locator)`, so an update would produce a different link. Hard to reverse - it is the shape of every link-touching call site. The trade-off is stated in `design.md` §3.3: a surrogate id was considered and rejected because idempotent re-landing needs the natural key regardless. *(Source: `application-tier.md` §2.1, derived from `design.md` §3.3.)*

**ADR-c. Delete is a plain delete; a dangling ref is legal and is recovered by a validation pass.**
Deleting a course does not cascade to its obligations; deleting an obligation does not remove notes about it. Surprising - it looks like a bug. The trade-off is explicit in `design.md` §3.2: the material requires a ref that names something absent, and the cost is that nothing enforces target existence. *(Source: `application-tier.md` §2.1 + `design.md` §3.2.)*

**ADR-d. Read-back counts only through the service methods.**
A test that reads the store directly, or reaches the repository past the service, satisfies no criterion. Hard to reverse once a test suite exists; surprising because reading the file is the obvious cheap check; the trade-off is slower, more coupled tests in exchange for the criterion measuring the thing it names. *(Source: `application-tier.md` §5.)*

**ADR-e. A real row that does not fit the field set is a spec failure, not a fixture patch.**
The correct move is to close the build cycle and open a design one. Hard to reverse because the alternative - patching the fixture - is invisible once taken and destroys the evidence that the spec was wrong. *(Source: `application-tier.md` §5.)*

**ADR-f. An ambiguous outcome resolves against the proposition.**
*"It basically round-trips" is a fail.* Cheap to state, hard to reverse in practice, and it is the rule that makes every other criterion mean something. *(Source: `application-tier.md` §5.)*

**ADR-g. A derived fixture is code, not evidence; the original is never edited.**
The migrated copy is a test input; the untouched original stays as provenance. Surprising because they hold the same rows. The trade-off is duplication in exchange for a provenance chain that survives migration. *(Source: `application-tier.md` §6.)*

**ADR-h. A write rule must be sayable in a docstring, or it is not finished.**
The rule's audience is the agent reading a tool description at call time, so a rule that cannot fit there has no delivery mechanism. *(Source: `plan/write-rules.md` §7 c6; consistent with `architecture.md` §3's *"how to produce one lives in the tool description or the bundled skill"*.)*

**Candidate flagged rather than proposed - ADR-i. Success-path derivation cannot produce a repair method.**
`application-tier.md` §2.4b is the strongest methodological finding in the directory: two independent derivations of a method set - a closure over the field set, and eleven real traces - between them produced zero corrections, deletions, re-lands or crash paths, and the one method that broke a system invariant (`annotations.retarget`) came from neither. It is not a decision, so it fails the ADR test as written; it is a **finding about how to derive a method set**, and it may deserve a home the successor does not yet have. Billy's ruling.

### Deferral - decisions deliberately not made, with the precondition that wakes them

| deferral | precondition | source |
|---|---|---|
| Recurring / countable obligations (B1) | a fourth course confirming the pattern, or a read that needs the count | `backlog.md` B1 |
| Location, duration and end time (B3, B4) | the calendar projection - itself deferred by 2026-08-30 ruling 3 | `backlog.md` B3, B4 |
| The marking-scheme mechanism (B6) | a planner that allocates against weights | `backlog.md` B6 |
| Obligation-to-obligation weight transfer (B7) | a second link kind | `backlog.md` B7 |
| The per-obligation late cap (B8) | a planner that models the budget | `backlog.md` B8 |
| Deliverable structure, separate from concepts (B9) | the artifact layer | `backlog.md` B9 |
| Course-level facts with no field (B10) | term boundaries become load-bearing if read-time expiry is built | `backlog.md` B10 |
| `course.prereq` (B11) | a second domain. **Reinforced by 2026-08-30 ruling 1**: deferred to v2, not dead | `backlog.md` B11 + ruling 1 |
| Is a conference a `time_point`? (B12) | `time_point` arriving, which needs the calendar projection | `backlog.md` B12 + ruling 3 |
| `sticky_note.category`'s vocabulary (B13) | a write rule; currently OWED in three records | `backlog.md` B13, `spec/write-rules.md` §4, `schema.md` §9 |
| What `origin` means (B14) | same | `backlog.md` B14, `spec/write-rules.md` §4 |
| `look_at`'s return shape (B19) | a presentation record. **Blocked by 2026-08-30 ruling 9** | `backlog.md` B19 |
| Where the id counter lives (B29's residue) | the next build cycle touching persistence | `backlog.md` B29 |
| Reject-or-replace on a second current progress record (B26) | a ruling; currently contradictory | `backlog.md` B26 |

### Not carried

- **Everything in *Sequencing, set aside*** - ordering, slice assignment, per-slice criteria, the trace verdicts, the coverage snapshot, the fixture rename list, the mandate's procedure and reading prohibition.
- **`plan/write-rules.md` §9's two positions on `parts`** - superseded by a ruling; it is the history of an adjudication, not a live question. Keep only if the successor wants the provenance.
- **The seal mechanism (§4, §6 stage gating, §9)** - an artifact of the old container: a standalone repo where a human convened separate cold sessions. The successor is components an agent uses, and the independence device failed here anyway.
- **B22, B23, B28, B29's code specifics** - defects in `app/src/**` of a repository that is not migrating. The *decisions* inside B26 and B29 are carried above; the file-and-line claims are not.
- **`application-tier.md` §2.4b's individual method rows** (`listUntargeted`, `listAll`, `hasId`, `nodesOfKind`, `allLinks`, `danglingLinks`, `IntegrityService.dangling`) - a method inventory of a codebase that does not migrate. The finding they support does.
- **The `n=1` / 22-obligations / 14-obligations counting history** - superseded by `architecture.md` §4's amendment and by 2026-08-30 ruling 1's scope boundary.

---

## Coverage

**Read in full:** all three files, all sections, both graveyards (`backlog.md`: empty; `application-tier.md`: empty; `plan/write-rules.md`: *"Empty. Nothing has been removed from this mandate"*), and all three changelogs (`backlog.md`: 6 entries, 2026-08-28 · `application-tier.md`: 1 entry, 2026-08-27 · `plan/write-rules.md`: 1 entry, 2026-08-26).

**Backlog items accounted for:** 27 of 27 present in the file (B1-B15, B18-B29). **B16 and B17 do not appear and are not explained** - reported as a gap, not resolved.

**Cross-reference checks performed against `domain/` and `spec/`**, by grep and by reading the cited section: `backlog`/`plan/`/item-number citations (4 found) · `time_point` · `hours_estimate` · `count{done,of}` · `course.prereq` · `grade_share` · immutability/provenance · dangling/cascade · link update · cold start / load-time validation · fixture migration · `obligation.course` updatability · conflict · RAG / semantic. Sections read in full: `schema.md` §1.1, §4.5, §4.6, §6, §7, §8, §9 · `architecture.md` §3, §4, §6, §7, changelog · `design.md` §3.2, §3.3, §3.4 · `ring-0.md` §6, §7 · `spec/write-rules.md` entire.

**Not verified, and why:**

- **B22, B23, B28, B29's code claims** (`app/src/application/kinds.ts`, `annotations.test.ts`, `ids.ts`, `flush()`, the temp-and-rename path) - source code is outside the stated boundary. The spec-side half of B28 was verified (`schema.md` §4.5 does make `state` non-nullable with no unknown state).
- **Anything in `records/archive/`, `records/findings/`, or `evidence/`** - outside the boundary. This affects three citations that could not be followed: `plan/write-rules.md` §2.1's quotes from `archive/slice-1-plan-2026-08-27.md` §4.4/§6, §5's `changelog-2026-08-24-slice-1.md` R7, and `ring-0.md` §6's `findings/read-cycle.md` §5 figures. Each is reported as the citing record states it.
- **The 2026-08-30 rulings themselves** - taken as given from the commissioning brief; they postdate every file read here and appear in no record in `fall26/records/`.

**Adjudicated:** nothing. Every conflict, void and owed item above is left open for Billy.
