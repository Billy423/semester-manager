# Reconciled residue - everything real in the corpus that the inventory never captured

**What this is.** The other half of the migration. The 115 inventoried things are being reconciled elsewhere and are not here. This document takes the four later surveys - which read the seven `evidence/` sittings and `records/plan/`, both excluded from the inventory's scoping - and gives a destination to what they found: rulings with no home, records standing wrong, decisions addressed to Billy sitting in unread files, and broken cross-references.

**Scope rule applied throughout.** Where an item is already one of the 115, it is named and dropped with a pointer. Where I am unsure, it is included and marked `POSSIBLE OVERLAP` with the M-number I suspect. Nothing is adjudicated. No ADR numbers are assigned; slugs only.

## Counts

**In.** Four surveys read in full - `08-evidence-early.md` (387 lines), `08-evidence-middle.md` (310), `08-evidence-late.md` (399), `09-plan-records.md` (429). Four `## Orphan rulings` sections read - `07-classification-C.md` (8 items), `07-classification-D.md` (7), `07-classification-E.md` (3); `07-classification-B.md` **has no such section**, and its one reconciliation hand-off is carried anyway (see ADR 19). Roughly **205 distinct residue items** examined: 22 rulings-with-no-home across the three evidence surveys, 27 backlog items plus 9 plan-only rulings plus 12 owed items from `records/plan/`, 20 voids and corrections, 24 uncorrected record sites, 31 abandoned steps, 40-odd measurements with their standing, and 18 orphan rulings.

**Out.**

| destination | count |
|---|---|
| Open decisions for Billy - primary, from the two unread files | **9** |
| Open decisions for Billy - secondary, owed from elsewhere and otherwise homeless | **8** |
| Records standing wrong today | **24 sites** across **9 records** |
| `CONTEXT.md` terms | **3** proposed, **3** rejected with reasons |
| `docs/adr/` | **20** ADRs, plus **3** riders on ADRs the inventoried half owns |
| Deferrals | **26** |
| Merges performed | **4** |
| Merges rejected | **4** |
| Not carried | **6 classes**, covering 31 abandoned steps and the whole methodology and sequencing layer |
| Broken or ambiguous citations | **12** |
| `POSSIBLE OVERLAP` flags | **11** |

**Verified at source rather than relayed.** Nine claims were checked directly in `/Users/billywu/Documents/Projects/fall26/` because something load-bearing turned on them: `ring-0.md` §7's 1,881 / 871 sentence, `model.md` §8.1's flat provenance log, the three unprefixed `write-rules.md` citations in `backlog.md`, `spec/write-rules.md` §3's table-versus-body contradiction, `preference`'s total absence from `records/spec/`, `schema.md` §7's `prereq` row, the section indices of both `write-rules.md` records, the current branch (`design/course-level`), and whether `ADJUDICATION.md` has ever existed. It has not: `git log --all --diff-filter=A --name-only` over the whole checkout returns nothing matching `ADJUD*` in any branch's history.

---

# Open decisions for Billy

Nine primary, consolidated from the two files nobody had read. Each gives the decision asked for, the options as stated, what turns on it, and whether the 2026-08-30 rulings have settled or narrowed it. **None is answered here.**

Five come from `evidence/2026-08-28-corpus/2c03/RULINGS-NEEDED.md`, whose own opening reads *"Five decisions, each with the source quote. These block the other three courses, because the same choices will recur there and I do not want to make them four times by default."* Four come from the twelve in `evidence/2026-08-26-interface-contract/decisions.md`; seven of those twelve are answered and one was answered then mooted.

**One caveat over the whole first group.** `records/spec/architecture.md` §4 already rules that extracting the other three courses is not worth doing before the presentation tier exists, so the file's stated urgency is partly overtaken. What is not overtaken is that four of the five name a defect in a record standing today.

---

### 1. Tutorial attendance gets no row, and it is 5% of the grade - OPEN, narrowed in two directions that pull apart

**Asked for.** Hold the recurring-obligation graveyard, re-open it, or defer.

**Options as stated** (`RULINGS-NEEDED.md` R1): **(a)** hold the graveyard - tutorial attendance stays a note, and the same for every lab and worksheet · **(b)** re-open it - a recurring obligation kind, or `count`, comes back by ruling · **(c)** defer - mark it unresolved, keep collecting instances across the other three courses, decide with four.

**What turns on it.** A 5% graded, required obligation is invisible to ring 0. `records/spec/schema.md` §7 graveyards `count{done, of}` on `n=1` and records its own weakness in the same row: the `n=1` was measured on the two courses least likely to contain recurring items, and 2px3 was excluded throughout. The file reports the instance count is now four. `records/spec/architecture.md` §4 has already taken option (a) as fact - the acceptance count moved from 22 to 14 partly because *"the old count included a row the graveyard forbids (recurring tutorial attendance)"* - so **(a) is the de-facto state of a truth record while the decision is formally open**.

**Effect of the 08-30 rulings.** Ruling 1 does not exclude tutorials, which are coursework inside academics. Ruling 2 pulls both ways and the file cannot settle which: the agent *"sees the skeleton and ring 0, notices, and asks when needed"* - but under (a) tutorial attendance is not in ring 0 for it to notice. **Narrowed, not settled.** If Billy picks (c), deferral 9 below becomes live; if (a) or (b), it does not.

*Source: `08-evidence-late.md` §The five open decisions R1; `07-classification-C.md` orphan 4; `records/plan/backlog.md` B1.*

### 2. `grade_share` cannot hold a bonus - OPEN, blast radius bounded but the falsehood remains

**Asked for.** How an additive bonus is represented, given `grade_share` is defined as a share of a total that already sums to 100.

**Options as stated.** None offered. The file states the defect and stops: *"Storing `1` asserts something false; `optional: true` is the only signal separating them and it does not carry additive semantics."* It flags itself as new - *"Four independent spec reviews missed it, because seeing it requires the arithmetic."*

**What turns on it.** `records.json` stores `grade_share: 1` on both bonus rows; `corpus-counts.txt` prints the sum over all rows as **97**; `ring-0.md` §6 independently reaches the same observation from a fresh corpus (95 stated, with the missing 5% having no row) and treats it as decisive for excluding the share column from ring 0.

**Effect of the 08-30 rulings.** Ruling 2 - *`grade_share` is reference only, never an input* - **bounds the blast radius without making the stored value true**. `schema.md` §3 already carries this as *"a standing EXEMPTION ... no mechanism reads it, and the exemption is the point"*. The reader harmed is a human or an agent reading the field for reference, which is the field's only declared purpose. **Narrowed, not settled.**

*Source: `08-evidence-late.md` R2; `records/plan/backlog.md` B2; `07-classification-C.md` orphan 4.*

### 3. The IDEA Conference may be the wrong kind entirely - OPEN, narrowed to a binary

**Asked for.** Whether a conference belongs in the obligation set at all.

**Options as stated.** Keep the obligation row, or do not. It carries one *"only because that is the only row-bearing kind available and it carries a stated grade consequence."*

**What turns on it.** The obligation count of 14, and with it `architecture.md` §4's acceptance criterion. `REPORT.md` says so openly: *"the count of 14 is a result of that judgment, not of a target."* The counter-argument is `schema.md` §3's own justification for `optional`: *"Without it a plan ranks a +1% survey among required work purely by date."*

**Effect of the 08-30 rulings.** Ruling 3 restates §7's ground exactly - `time_point` is out because the calendar projection is out - which **confirms there is no alternative kind to move it to in v1**. That narrows R3 to a binary. It does not choose.

*Source: `08-evidence-late.md` R3; `records/plan/backlog.md` B12.*

### 4. `course.prereq`'s graveyard reason is falsified, and the outline's course-level facts have no home - the FIELD is settled, the REASON and the second half are open

**Asked for.** Two things the file states in one paragraph. (a) Whether the graveyard row's recorded ground is corrected. (b) Where the outline's course-level facts go.

**Options as stated.** None. The file is careful: *"The conclusion may still stand on other grounds; the stated ground does not."*

**What turns on it.** `records/spec/schema.md` §7 line 174 reads, verbatim and uncorrected today, *"`course.offering_term` · `course.prereq` | Not carried: null for both courses in the fixture"* - and the 2c03 outline states *"Prerequisite(s): SFWRENG 2DM3"*. A later reader inherits a false ground under a correct conclusion. The second half is sharper and no ruling reaches it: `course` has four fields and zero free text by rule, so instructor, term boundaries, units, antirequisites and the required textbook can reach the system only as annotations - and **the term boundaries are load-bearing, because `REPORT.md` F7's last-day-of-classes rule depends on `Course Dates: 01/05/2026 - 04/07/2026`**.

**Effect of the 08-30 rulings.** Ruling 1 settles the field: `course.prereq` stays graveyarded for v1, cross-domain deferred to v2, not dead. **The reason is still wrong and the second half is untouched.** Note that `domain-design.md` §0.6 is the corpus's strongest statement of why prerequisite structure matters and is not marked against §7's graveyard in either direction.

*Source: `08-evidence-late.md` R4; `09-plan-records.md` V4 and B11; verified at source.*

### 5. The final exam's date - derived or null - APPARENTLY SETTLED; confirm and close

**Asked for.** Whether a date derived from an announcement (*"See you in the exam today!"*, Apr 16) may be stored, or whether it stays null.

**Options as stated.** *"Both readings are defensible. Reverting is a one-field CRUD, and the reasoning is already on a note."*

**Settled where.** `records/plan/backlog.md` B25, struck through, **Billy, 2026-08-28, standing `ruled`**: *"B25 closed by ruling rather than parked, and the corpus's Final Exam corrected: an inferred value is asked about, not stored with a note explaining the inference."* I read this at source. It is not an independent settlement; it is the read-side record of the same ruling as `spec/write-rules.md` §1.1, same date, same author. B25 adds three things §1.1 does not carry: the coarse-date consequence (the term's largest obligation stores a null `due`), the observation that **the corpus used to author the write rule was itself violating it**, and the framing that this was a blocking item resolved rather than deferred.

**Why it is still on this list.** `records.json` still stores `"due": "2026-04-16"` and was never synced (`2026-08-29-course-level/NOTES.md` §4). The ruling exists in `records/plan/`, which the migration was scoped to exclude, and its only citation into it is one of the broken ones (citation 3 below). **Confirm and close** rather than decide.

*Source: `08-evidence-late.md` R5; `09-plan-records.md` §B25; verified at source.*

### 6. What gets an obligation row - answered behaviourally, still open definitionally

**Asked for.** `decisions.md` #1. One syllabus, two agents: 12 weekly readings become 12 rows or 0; a project with a proposal, a draft and a final becomes 1 row or 3.

**Options as stated.** The file recommends making it owed with an owner and a due slice, and forbidding bulk ingestion until it exists. Its supporting measurement: *"The repo names 'what counts as a part' as an owed item in four separate records; it has never once named 'what counts as an obligation'."*

**What turns on it.** Every count in the corpus, including the 14 that `architecture.md` §4's acceptance criterion rests on.

**Effect of the 08-30 rulings.** Billy 2026-08-27 answered the **trigger** - an agent never auto-adds anything unless it is clear the user wants it - landed at `architecture.md` §3. Ruling 1 sets the **outer boundary** - coursework inside academics. **Neither reaches the row-count question for material the user does want tracked**, which is the proposal/draft/final case. `schema.md` §9 item 5 carries the residue as *the domain boundary*. **Narrowed twice, still open.**

*Source: `08-evidence-early.md` §decisions.md #1.*

### 7. May a landing decline a field - LIVE, untouched by any ruling

**Asked for.** `decisions.md` #8. What happens when the material does not supply a required field.

**Options as stated.** The recommendation: **a landing may decline a field and report what it could not determine** - and the file names the cost itself, *"this makes what a landing may refuse to do part of the contract, which nothing currently says."*

**What turns on it.** Three worked cases the file supplies. A forwarded *"the midterm is Monday, bring a calculator"* names no course, and `course` is not nullable and set once, so a guess is permanent. A syllabus stating *"there will be a final examination during the last week of term"* states no handle. *"The essay is due Friday"* is a day, so `due`'s null branch does not cover it.

**Effect of the 08-30 rulings.** None reaches it. `spec/write-rules.md` §1.1 covers an **inferred** value (ask the user); §1.2 is an OWED slot for *absent is not unknown when a person would not hesitate*. Partly parked by `architecture.md` §7 taking `land()` out of the first build - which parks the mechanism, not the contract question.

*Source: `08-evidence-early.md` §decisions.md #8.*

### 8. `grade_share` - whose share, and which arm - LIVE, and ruling 2 does not reach it

**Asked for.** `decisions.md` #9. Two sub-rules: the **scope** rule (does a share stated over a group become that group's members' value?) and the **arm** rule (when two marking schemes exist, which one is stored?).

**Options as stated.** The recommendation: a stated share covering a group is **not** this field's value - store null and put the group rule on a note - and name the arm rule explicitly, with *the arm that is worst for you* as the honest default.

**What turns on it.** Two measured failures that are still reachable. *"Homework: 40% (six assignments)"* puts 40 on six rows and the corpus asserts **240%**. For `10/10/30 or 0/0/50` both 30 and 50 are legal, so two corpora differ by 20 points with both flagged `grade_share_conditional: true`.

**Effect of the 08-30 rulings.** Ruling 2 settles the **reader** (reference only, never an input) and nothing else. Neither the scope rule nor the arm rule is in `schema.md` §3, in `spec/write-rules.md` §3 (whose `grade_share` row reads *"none yet"*), or anywhere in `records/domain/`. **Untouched.** Note this compounds with decision 2: the 97 sum and the 240% failure are two different arithmetic defects in one field.

*Source: `08-evidence-early.md` §decisions.md #9.*

### 9. What name does a resolved `due` come back under - HALF ANSWERED, and the open half moved tiers

**Asked for.** `decisions.md` #10. `23:59` is the most common **stated** deadline time in a university course, so a resolved value is wire-identical to a stated one, and a later landing carrying a real time is rejected as an illegal promotion.

**Effect of the 08-30 rulings.** None directly. `schema.md` §3 closed the storage half - *"A `Date` resolves to `23:59` at read time; which surface applies that resolution is presentation tier, and the stored value is always returned raw."* **The name the resolved value comes back under is still unnamed, and it is now presentation's to name**, which puts it behind ruling 9's gate. It is also mandate item D of the record that does not exist (deferral 20).

*Source: `08-evidence-early.md` §decisions.md #10.*

---

## Also owed to Billy, from outside those two files

Eight more, listed because each needs a ruling and none has a home once `fall26` becomes a citation rather than a container. They are separated from the nine above because they are not from the two unread files.

| # | the decision | what turns on it | 08-30 effect |
|---|---|---|---|
| 10 | **`grade_share`'s name.** The 08-26 Handoff lists three items as *"Owned by Billy"*; the other two are carried at `schema.md` §9 items 3 and 5. This one is in no owed list anywhere. `domain/model.md` §10 item 9 calls one field three names - `weight`, `worth_percent`, `grade_share` - and the 08-25 sitting deliberately did not rename it *"because the name itself is unruled and Billy's"* | a field name that three records spell differently | none |
| 11 | **`preference` - carried or graveyarded.** A whole fact type, defined at `domain-design.md` line 300 with a field set and a reader, argued at §8 (*"Preferences are not a new layer - they are a fact type. Structurally it is identical to `progress`"*). I confirmed **zero occurrences in all of `records/spec/`** - not in the kind set, not in §7's graveyard, not in `design.md` §3.1's slice lists | `migration-gaps.md` §2.1 names this state as worse than either outcome: *"a reader cannot tell whether it is deliberately absent or overlooked"* | none. Routed below |
| 12 | **Is `obligation.course` updatable?** `application-tier.md` §7.1 recommends *set at create, not updatable* and says *"Needs a ruling before slice 2 closes"*. `spec/write-rules.md` §3 line 55 points back at it and explicitly refuses to hold the answer: *"The code implements the recommendation; this record does not decide it"* | **Code implements an unruled recommendation.** If `records/plan/` does not migrate, this question has no home at all | none |
| 13 | **Is `parts` updated as a whole list, or per element?** `application-tier.md` §7.2 recommends whole-list replacement. `L2-lifecycle.md` lists it as a could-not-determine | the shape of every `parts` write | none |
| 14 | **B26 - reject or replace on a second current progress record.** `application-tier.md` §4's slice-3 criterion says REJECTED; §2.2 T8 records *"pass - `setProgress` upserts"*. Two halves of one plan record contradict each other; `schema.md` §4.5 states the invariant without ruling the failure mode | *"A caller expecting a refusal it can turn into a confirmation gets a silent overwrite."* Bears directly on **ruling 7** - a silent overwrite is the write-side of persisting a conflict as noise | ruling 7 makes this urgent rather than settling it |
| 15 | **Where the id counter lives.** `backlog.md` B29 names it as *"a decision this ruling did not make"*. `schema.md` §1.1 rules the id is opaque, monotone and assigned, and says nothing about where the counter is handed out | placement is a tier decision, not a defect fix | none |
| 16 | **B5 - raw mark totals, parked with no wake condition.** The only item in the whole corpus whose un-parking condition is *"nothing foreseen"* | **By this migration's own definition an item with no precondition is not a deferral, it is a rejection nobody has written as one.** Billy's call which it is, before it is filed either way | none |
| 17 | **Score the blind exercise, or retire it.** Routed in full below | roughly ninety derived capabilities and forty-odd stated contradictions, cited once across seven records | none |

---

# Records standing wrong today

**Twenty-four sites across nine records.** These do not migrate - they are facts about `fall26`. They matter because the plan is to **cite `fall26` as provenance rather than copy it**, and a citation into a wrong record poisons whatever cites it.

Ranked by how much rests on each: how many other passages, decisions or open cycles depend on the wrong sentence.

## Tier 1 - load-bearing right now

| # | record and section | what it says | what contradicts it | dates | still uncorrected |
|---|---|---|---|---|---|
| 1 | **`records/spec/ring-0.md` §7, line 88** | *"all 11 notes in one call is **1,881 characters**, while the 4 course-scoped ones alone are **871** plus a table ring 0 already holds resident"* - the stated ground for the record refusing to establish that the course level is worth a call | Billy voided exactly those two totals: *"the corpus is evidence about what the material contains; it is not evidence about what a record should look like."* 871 + 1,010 = 1,881 is precisely `measurements.txt`'s two voided figures | asserted 2026-08-28, voided 2026-08-29 | **Yes.** Verified at source on `design/course-level`. `git diff main -- records/` is empty, so main carries it too |
| 2 | **`records/domain/model.md` §8.1** | present tense, inside a block headed `PROMOTED 2026-08-24 (ruled 2026-08-23)`: *"§8's merge of `announcement → node mentions` into `sticky_note.origin` keeps a **flat provenance log**, so the announcement text lives there and the note is the extracted meaning. Editing a note destroys nothing"* - used as the premise for **retracting** *origin-bearing notes are append-only* | Billy deferred the log on 2026-08-26. The sitting recorded the exact trigger: *"If the log does not exist, editing a note destroys the announcement text and the retracted rule's premise returns"* | asserted 2026-08-23, deferred 2026-08-26 | **Yes.** Verified at source. `model.md`'s changelog carries four entries 08-25 to 08-28 and none touches §8.1 |
| 3 | **`records/domain/model.md` §10 item 5 body (lines 643-647)** and **4. its changelog line 701** | a `MEASURED 2026-08-28` banner falsifying *real samples are short*, on 87-278 / ~90 / 871 characters | same void as #1. An unruled agent writing longer than §4.2's worked example does not falsify *real samples are short*; it reports that the agent had no rule | 2026-08-28 vs 2026-08-29 | **Yes, in both places.** Billy named correcting the first *"a deliverable of this cycle, not a side note"*; the cycle's commits touch only `evidence/` |
| 5 | **`records/plan/application-tier.md` §1, §4 Slice 2, §4 The whole, §6, trace T4** | *"built until **22 real obligations** go in through the write methods and come back out ... That is `architecture.md` §4's surviving criterion, **and it is the only one**"* | `architecture.md` §4, amended 2026-08-28, Billy, ruled: one course's real obligations; *"22 is not reachable by re-running the old route"* | 2026-08-27 vs 2026-08-28 | **Yes**, in five places. No changelog entry after 08-27. **The plan's single criterion is unmeetable as written** |
| 6 | **`records/plan/application-tier.md` condition line, §3 Slice 0, §4 Slice 0** | *"this plan is executable only while `../spec/architecture.md` §5-§7 stand"*, and slice 0 requires *"three packages with the dependency direction in their manifests"* | `architecture.md` §6, reversed 2026-08-28, Billy, ruled: tiers are directories under one source root, because npm hoists workspace dependencies so *"a manifest states an intent it cannot refuse"* | 2026-08-27 vs 2026-08-28 | **Yes**, and it compounds: **§6 is inside the range the plan names as its own precondition.** The plan states its precondition, the precondition broke two days later, and the plan does not say so |

**Item 1 is the one to act on first.** It is a different record from the two everyone has been pointing at, its sentence is the stated ground for an open question, and Billy is on the `design/course-level` branch now. Item 2 is second: it is a truth record asserting a deferred mechanism as present, in a passage marked ruled, as the premise for a retraction - and the log's one proposed home (`chunk.node_id = <sticky_note id>`, `08-evidence-early.md` H6) looks closed by ruling 6, because raw announcement text kept for provenance is neither semantic nor decontextualized.

## Tier 2 - a wrong statement in a record that governs live work

| # | record and section | what it says | what contradicts it | dates | still uncorrected |
|---|---|---|---|---|---|
| 7 | `records/spec/schema.md` §7, line 174 | `course.prereq` not carried because *"null for both courses in the fixture"* | the 2c03 outline states *"Prerequisite(s): SFWRENG 2DM3"* | 2026-08-27 vs 2026-08-28 | **Yes**, verified at source. Ruling 1 keeps the field out, so only the ground is wrong - and it is printed under a now-independently-correct conclusion |
| 8 | `records/spec/design.md` §1 Constraints | *"directly-callable **Python**, no MCP, no Postgres"* | `architecture.md` §6: **TypeScript**, because *"Python cannot refuse: any module may import any other, so the purity cut degrades into discipline"* | 2026-08-26 vs 2026-08-27, re-packaged 08-28 | **Yes.** `design.md` is the record `architecture.md` §2 assigns to the application and persistence tiers, so **the record that owns the tiers being built names the language ruled against** |
| 9 | `records/spec/design.md` §1 F5 | *"Ring 0 holds **all 22 real obligations** with no free-text escape hatch"* | `architecture.md` §4's amendment, as #5 | 2026-08-26 vs 2026-08-28 | **Yes**, and F5 is a numbered functional requirement, the form most likely to be read as a target |
| 10 | `records/spec/write-rules.md` §3 field table, line 58 | ``name`` \| `§3.1 - **OWED**` | §3.1's own heading and body: *"There is no system-owned naming convention, and **one is not owed**"* | both written 2026-08-28 | **Yes**, verified at source. An internal contradiction inside one record, one screen apart. This is a defect, not a decision |
| 11 | `records/spec/write-rules.md` §3.4 and §4.0 | *"50 candidate strings became **28**"* and *"20 candidate notes became **12**"* | both figures count one of Billy's own `_note` instruction strings as data; the corpus holds **27** and **11**. `LABELING.md` L1 enumerates **54** candidates, not 50 | 2026-08-28 | **Yes.** The `parts` count is the number the rule's own effect is stated in, and it is not covered by the 08-29 void |
| 12 | `records/domain/model.md` §8.3 | under a PROMOTED banner: *"Normalised to end-of-day ... A date without a time needs an explicit convention **at the schema level, not at the parser's discretion**"* | `schema.md` §3: resolved *"at read time"*, and *"which surface applies that resolution is presentation tier"* - which is per-surface discretion under a different name | 2026-08-24 vs 2026-08-27 | **Yes.** Two independent derivations found it. `schema.md`'s changelog overturns a promoted `model.md` passage without noting that it does |
| 13 | `records/domain/model.md` §10.9 | `[R]` Billy: *"`worth_percent` keeps its value and gains a `conditional` marker **plus a pointer to the rule**"* | `schema.md` §3, Billy, ruled 2026-08-27: *"The rule **may optionally** be left on a one-line sticky note; **requiring one is not a rule**"* | 2026-08-23 vs 2026-08-27 | **Yes.** Two Billy rulings five days apart in opposite directions, the older carrying `[R]` with no supersession marker. `L1-material.md` capability 5 prices the residue: three obligations carry `conditional: true` and the rule's only link is to the course |

## Tier 3 - a stale frame or a superseded sentence, dormant but inheritable

| # | record and section | what it says | what contradicts it | still uncorrected |
|---|---|---|---|---|
| 14 | `records/spec/design.md` §3.7 | `look_at(node_id, question) -> { summary, annotations[], edges[] }` | `schema.md` §4.6, rewritten in `63612df`: the triple *"was not"* a return contract | **Yes**, and scoped only by §3.4's own re-homing banner |
| 15 | `records/domain/model.md` §7.1, line 356 | the same triple in a fuller form, under a PROMOTED banner | same | **Yes**, and **not** scoped by any banner. One of three sites was fixed |
| 16 | `records/domain/domain-design.md` header banner, line 3 | *"§9.1's projection grain is dead and **no replacement is ruled**"* | the same record's own §9.1 body and its 2026-08-28 changelog: *"§9.1's dead grain has a replacement, and it is not here"* - it is `spec/ring-0.md` | **Yes.** The first thing a reader of that record sees is the wrong half of a fact the record corrected in the same edit |
| 17 | `records/domain/domain-design.md` §6.1 item 2 | `[R]` Billy: *"**Size is observed ordinally** - from `parts` and item notes first"* | `schema.md` changelog 2026-08-27: *"`parts` carries concepts only; the ordinal size-judgment reader is not designed"*; `spec/write-rules.md` §3.4 | **Yes.** Ruling 2 settles the substance a third time; the propagation is what is owed |
| 18 | `records/domain/domain-design.md` §6.2 | the *ordinal invited invention* fault is *"fixed by **rendering null as absence**"* | `model.md` §8.2 was corrected on 2026-08-28 to *"a **DEFINED default**, not by rendering absence"*; `schema.md` §4.5 makes `state` non-nullable | **Yes.** One of two twinned passages moved. **Ruling 4 rests on the corrected version**, so the uncorrected twin now contradicts a live ruling |
| 19 | `records/domain/domain-design.md` §0.6 | *"the academic domain **must** hold course offering-terms and prerequisite structure ... the single most concrete design input carried in the originating dispatch"* | `schema.md` §7 graveyards both | **Yes.** Ruling 1 resolves the substance - v1 out, v2 deferred, not dead - and **neither passage says "v2"**: §0.6 reads as a live mandate, §7 as a dismissal |
| 20 | `records/domain/domain-design.md` §7 | *"Where `workload` estimates come from. Tilt: Billy states a rough number, revisable"* | reversed inside its own record by §6.1 (`[R]` Billy 2026-08-23, *"`hours_estimate` is not a field to be filled"*), again by `schema.md` §7, and a third time by ruling 2 | **Yes**, uncorrected within its own document |
| 21 | `records/domain/model.md` §7.2, lines 409-413 | the `UNRESOLVED, and it must not be smoothed over` banner on label-versus-summary | `model.md`'s own 2026-08-28 changelog closed §7.1's twin; `architecture.md` §5 rules a summary is written only where a node's identity is content the skeleton does not hold | **Yes.** If the 08-28 sitting believes it closed the label-versus-summary question, **§7.2's banner is the one that did not get the memo** |
| 22 | `records/domain/model.md` §7.1 (`question` required *"at the tool surface"*) and §4.1 (retirement at *">= 80% of `look_at` calls"*) | `[R]` Billy 2026-08-23 | `architecture.md` §5 rules a CLI grammar and demotes an agent-protocol adapter to *"may never be built"* | **Yes.** A `[R]` ruling whose enforcement point no longer exists, and whose retirement condition is stated in a statistic the ruled surface cannot produce. Dormant behind ruling 9 |
| 23 | `records/domain/model.md` lines 608-610 | *"The real axis is **whether meaning survives linearization**"* | **Ruling 6**: the determinant is the nature of the RAG store, which *"replaces both the source-class rule and the linearization axis"* | **Yes.** Newest contradiction in the set - the record is one day behind a ruling that names it |
| 24 | three changelog entries added by `63612df` (`schema.md` 217, `spec/write-rules.md` 169, `backlog.md`) | standing `agent - measured` | `2026-08-29-course-level/NOTES.md` §2 rounds 3 and 4 record both as **rejected by Billy** | **Yes.** The substance is right and the standing is understated - **two of Billy's rulings are recorded at agent standing.** Note the same commit dates every entry 2026-08-28 while the commit itself is `Sat Aug 29 14:38:33 2026`: the records' internal dates run one day behind the commits for this whole run |

**Two more, recorded but not counted as records** because they sit in `evidence/`, which is by its own definition not a truth record. `evidence/2026-08-26-slice-1-build/fixture.json`'s header repeats the false synthesized-values claim that the same sitting measured false in its own Cycle 2 - the sitting that measured it did not fix the file it wrote in the same cycle. And `records/plan/write-rules.md` §7 states *"it is not `records/spec/write-rules.md`"* of a record that now exists at exactly that path; the later record wins on date and standing, but **the mandate's reasoning is overridden rather than answered**, and it would tell a fresh reader that `spec/write-rules.md` should not exist. I count that one as a record site under #10's record but list it here because the fix is a note, not an edit.

---

# The term set

Three terms, in the same format as the classified half: what it **IS**, one or two sentences, no implementation detail, one name chosen.

### candidate fact

A fact extracted from source material but not yet landed, carrying none of the system timestamps that landing assigns.

*Source:* `08-evidence-middle.md` R9, from `evidence/2026-08-26-slice-1-build/NOTES.md` §Cycle 1 - *"a transcription that stamped them would be fabricating the moment material entered a system that does not exist yet."* `records/spec/design.md` §3.6 **already uses the phrase without defining it**, which is the strongest argument for the entry. Independently reached by `L1-material.md` capability 9.

_Avoid_: extraction output · pre-landing record · staged fact.

### dissolved item

A parked question that ceased to exist because a ruling elsewhere removed the condition that created it, as distinct from one that was answered.

*Source:* `09-plan-records.md`, from `backlog.md`'s treatment of B15, B20 and B21 and its changelog - *"Three items closed by removing the question. None was closed by answering it."* The distinction is load-bearing because a dissolved item and an answered one leave different residue: B15's dissolution is contested by N1 precisely because dissolving on addressing grounds did not touch the presentation half of the same question.

_Avoid_: closed item · retired item · obsoleted question.

### repair method

An operation that exists to correct a mistake - a retarget, a delete, a re-land - as opposed to one that advances a success path.

*Source:* `09-plan-records.md` ruling 5, from `application-tier.md` §2.4b. Named because no success-path derivation produces one, and the one method that broke a system invariant (`annotations.retarget`) came from neither of two independent derivation routes. The term rides on ADR 7.

_Avoid_: corrective operation · recovery method · maintenance method.

## Terms rejected, with reasons

- **backlog item** and **mandate**, both proposed by `09-plan-records.md`. Rejected: they are generic software vocabulary, and `CONTEXT.md` is for concepts specific to this project. What is project-specific about a backlog item is the **rule** that every one carries a wake condition, and that is ADR 13, not a term. Coining the term as well would put the same content in two destinations.
- **write rule**, proposed by `09-plan-records.md`. Rejected as **`POSSIBLE OVERLAP`** - cluster E owns the write-rules material and this is near-certainly among the 115. Not re-classified here.

---

# The ADR set

Twenty. Slug, title, body of one to three sentences, any shape riding inside, and the source. **No numbers assigned.**

### 1. `derived-record-may-narrow-its-source`

**A derived record may narrow or drop its source's ruling; provenance is not authority.**

A document derived from another may legitimately narrow, drop or supersede what its source ruled, and a divergence between them is not by itself evidence that the derived one is in violation. The failure this prevents already has a name in this project - *the authorising document has become history but is still cited as authority* - and this is that failure committed in reverse.

*Trade-off:* authority versus derivation. The rejected alternative is treating an upstream `[R]` as binding downstream, which is what the 08-26 sitting did and paid for: it re-sorted 7 verified "the spec states the opposite of a ruling" findings down to 5, of which only 1 was actually input-versus-output.

*Container caveat:* the `domain/` versus `spec/` layering is fall26's. In the successor the same relation holds between `CONTEXT.md` and an ADR, and between an ADR and the code it governs. If the successor decides it will never carry two layers of document, this becomes not carried.

*Source: `08-evidence-early.md` H1; Billy 2026-08-26, `evidence/2026-08-26-interface-contract/NOTES.md` §Cycle 1 Rulings.*

### 2. `fixture-is-not-a-golden-set`

**A conformance verdict over a transcription is not a fidelity claim about the material.**

The 2026-08-26 re-transcription's five passing criteria measured the output's conformance to the field set, and none of them was ever evidence of fidelity to the source material. Verdicts that measured conformance stand for what they measured and for nothing more.

*Trade-off:* the rejected alternative was patching the completed five-criterion PASS rather than voiding what it was taken to mean. Hard to reverse because it voided a finished acceptance run; surprising because the fixture's own header asserts compliance.

*Source: `08-evidence-middle.md` R1; Billy 2026-08-26, `evidence/2026-08-26-slice-1-build/NOTES.md` §Cycle 2 Rulings. Two records already carry consequences of this ruling and neither carries the ruling.*

### 3. `derived-fixture-is-code-not-evidence`

**A migrated fixture is a test input and therefore code; the original is never edited and stays as provenance.**

*Trade-off:* duplication of identical rows, accepted in exchange for a provenance chain that survives migration. The rejected alternative was editing the original in place, which is invisible once taken.

*Source: `09-plan-records.md` ADR-g, from `application-tier.md` §6.*

### 4. `docstrings-are-design-not-documentation`

**Write rules precede the build, because a verb's docstring and parameter definitions are what the agent sees directly.**

A docstring is not documentation of a decision made elsewhere; it is the surface the agent reads at call time, so it is designed under the write rules rather than written after them. The ruling's target has since moved - write rules precede the *presentation* tier, not the application tier - and its ground has not.

*Trade-off:* the rejected alternative was building first and documenting after, which is cheaper and was the sitting's opening position.

*Source: `08-evidence-middle.md` R2 and `09-plan-records.md` ruling 2, both from Billy 2026-08-26. The sourced wording survives only at `records/plan/write-rules.md` §2.1, a section explicitly titled "kept for its wording"; `architecture.md` §4 carries the re-targeting and never the ground.*

### 5. `a-write-rule-must-fit-a-docstring`

**A write rule that cannot be said in a docstring is not finished.**

The rule's audience is the agent reading a tool description at call time, so a rule with no room in that description has no delivery mechanism regardless of how well it is argued elsewhere.

*Trade-off:* expressiveness against deliverability. The rejected alternative was a write rule of any length living in a record the agent never reads.

*Source: `09-plan-records.md` ADR-h, from `plan/write-rules.md` §7 c6; consistent with `architecture.md` §3's "how to produce one lives in the tool description or the bundled skill".*

### 6. `derivation-top-down-construction-bottom-up`

**Derivation runs top-down and construction runs bottom-up, and interaction requirements decide which capabilities must exist, never what a method looks like.**

The discriminating test is the operative half: **if the method changes when the surface changes, the surface has leaked down.** That test is what identified `look_at` and `land`+`Diff` as leaked, and anyone re-doing that classification without it has no test.

*Trade-off:* the rejected alternative was reverse-deriving the design from interaction requirements outright, which Billy asked about directly. `architecture.md` §1 carries the adjacent rule - *"A tier is designed against the tier below it, and that tier must already exist"* - which is **construction order, the opposite direction, and not the same claim**. The two together are the method; only one is recorded.

*Source: `08-evidence-middle.md` R3, `evidence/2026-08-27-tier-recut/NOTES.md` correction 2. Attribution: Billy asked, the answer was adopted in the sitting and is not tagged `[R]`.*

### 7. `success-path-derivation-omits-repair`

**A method set derived only from success paths cannot produce a repair method, so completeness over success paths is not completeness.**

Two independent derivations of one method set - a closure over the field set, and eleven real interaction traces - between them produced zero corrections, deletions, re-lands or crash paths. The method that actually broke a system invariant, `annotations.retarget`, came from neither.

*Shape riding inside, because it encodes the finding more precisely than the prose:* Route A enumerates over fields · Route B's eleven traces are all success paths · `retarget` ∉ A ∪ B, and `retarget` is the method that broke *one current value per target*.

*Trade-off:* the rejected alternative was accepting a two-route union as a completeness argument, which is what the plan record was written to assert. `09-plan-records.md` flagged this rather than proposing it, on the ground that a finding is not a decision. I propose it as an ADR because it is the decision *not to trust* a completeness argument the project had already made, and it is the strongest methodological result in the whole corpus.

*Source: `09-plan-records.md` ADR-i, from `application-tier.md` §2.4b.*

### 8. `blind-derivation-withholds-analysis-not-material`

**A blind agent is withheld the analysis, not the material.**

The independence worth having is independence from a session's framing, not from the facts: a cold session cannot derive birth rules at all, and a session handed the prior session's findings inherits its conclusions.

*Trade-off:* corroboration value against derivability. The rejected alternative - withholding the material - was tried, and it is why the abstract write-rules mandate stalled for two months and was never executed as written.

*Source: `08-evidence-middle.md` R6, Billy 2026-08-26 sharpened in-sitting; applied again by `evidence/2026-08-27-tier-recut/derivations/README.md`, whose four subagents were "blind to each other and blind to `records/plan/application-tier.md` and `STATUS.md`".*

### 9. `preregistered-prediction-scored-on-unpredicted-yield`

**A blind exercise is scored on what it finds that was not predicted; a predicted item that is found is a known hole, not evidence the method works.**

*Trade-off:* the rejected alternative is the obvious one - scoring recall against the prediction list - which measures the predictor rather than the instrument. The pre-registration also names what its author expected to be wrong about, and the expectation was *"worth more than the individual findings."*

*Standing note:* the prediction was never scored, because `ADJUDICATION.md` does not exist. The rule is recorded here; the scoring is decision 17.

*Source: `08-evidence-middle.md` R7, `evidence/2026-08-27-tier-recut/PREREGISTRATION.md` §"The rule for reading this afterwards".*

### 10. `origin-carries-no-locator`

**Whatever `origin`'s vocabulary becomes, it may not carry a locator, because a page reference re-admits the graveyarded `source_ref` through the annotation.**

*Trade-off:* the rejected alternative was letting `origin` name where a claim came from in the source, which is what two independent passes reached for and what the field's real use wants. The document-class vocabulary exists to satisfy this constraint.

*Why it matters:* `spec/write-rules.md` §4 books the two-vocabulary collision as OWED and states it as *"both passes reached for what document class it came from"* - **as drift between two passes, not as a ruled constraint one of them was satisfying.** A write-rule author reading §4 alone cannot tell that one side of the collision is load-bearing.

*Source: `08-evidence-middle.md` R8, `evidence/2026-08-26-slice-1-build/NOTES.md` §Cycle 1 Rulings. `POSSIBLE OVERLAP` with M57 - the field is inventoried; this constraint on it may not be.*

### 11. `corpus-bounds-content-not-record-shape`

**Corpus measurements bound what the material contains, never what a record should look like.**

Measurements over `evidence/2026-08-28-corpus/2c03/records.json` are admissible for what the source material states and where a fact hangs, and inadmissible for how long a record should be or how many records a statement becomes. The bodies measured are an unruled subagent's compressions, partly overwritten by Billy's hand edits with nothing saying which body is which, and `write-rules.md` did not exist when the extraction ran.

*Shape riding inside, because the partition is the ruling:*

| survives | does not |
|---|---|
| which obligations exist, their `due`, `grade_share`, `optional` | every character count - 871 / 1,010 / 459 / 1,881 |
| which policies the course states | how many notes those policies became, and how long each is |
| that 4 notes hang on the course and 7 on obligations - a placement fact | `parts`' wording and length on every row |

*Trade-off:* the rejected alternative was keeping the numbers, which is circular - it canonises an unruled agent's output as the target. Hard to reverse: re-adopting the corpus as a shape argument means re-running the extraction under write rules. Surprising: the corpus is the project's only real data and three record passages already lean on it.

*Source: Billy 2026-08-29, `evidence/2026-08-29-course-level/NOTES.md` §6, verified verbatim at source by `08-evidence-late.md` finding 4. The corollary N5 - **a length bound is issued down from affordability, not read up from samples** - is the same ruling seen from the other end and is folded in here rather than carried separately.*

***`POSSIBLE OVERLAP`, and it is the important one.*** `07-classification-C.md` orphan 5 says this is *"fully absorbed into M59"*; `07-classification-D.md` orphan 4 says it has **no M-number in any cluster** and calls it *"highest-value orphan in this list"*. The two classifying agents disagree. Included here rather than dropped on an assumption, because it is the single most consequential item in the residue and dropping it on C's word would lose it if D is right.

### 12. `renderer-truncation-is-asymmetry`

**Renderer-introduced truncation is asymmetry, so a fixed-width table is not the course level's shape.**

A fixed column width forces per-row truncation, and truncation introduced by the renderer is asymmetry introduced by the renderer, which `domain-design.md` §9.2's symmetry rule rules out.

*Trade-off:* a table is the obvious first shape and rejecting it removes the default with no replacement designed. The ground is not readability - it is the symmetry rule applied to the renderer rather than to the observer. The table was rendered over real data first and rejected on what it showed.

*Fallback if this is judged too close to a presentation record that does not exist yet:* deferral, precondition = the presentation record gaining a shape.

*Source: `08-evidence-late.md` N7, Billy 2026-08-28, `render-candidates.txt` header and `2026-08-28-ring-0/NOTES.md`. A grep for `truncation` across `records/domain` and `records/spec` returns one hit, and it is a different claim about a different thing.*

### 13. `park-with-a-wake-condition`

**Undecided and unimportant questions are parked with the condition that would wake them, not answered.**

The system is not trying to model real-world course structure perfectly; a question cheaper to park than to answer goes on a list, and every item names what would un-park it.

*Trade-off:* the rejected alternative is answering everything, which is what produced two months of stall on the write rules. Hard to reverse because the disposition of the whole corpus depends on it and un-parking retroactively means re-deriving a dozen fields' worth of justification. Surprising because a schema with a dozen known gaps reads as incomplete rather than as ruled.

*Source: `09-plan-records.md` ADR-a; Billy 2026-08-28, `backlog.md` header. Note the one live violation: B5 is parked with "nothing foreseen", which this ADR forbids - decision 16.*

### 14. `a-link-has-no-update`

**A link has no update; changing any part of one is detach plus attach.**

A link's identity is its whole tuple `(from, to, kind, role, locator)`, so changing any component produces a different link rather than a modified one.

*Trade-off:* stated at `design.md` §3.3 - a surrogate id was considered and rejected because idempotent re-landing needs the natural key regardless. Hard to reverse: it is the shape of every link-touching call site.

*Source: `09-plan-records.md` ADR-b, from `application-tier.md` §2.1 derived over `design.md` §3.3. `design.md` states the natural-key identity and never states the consequence for the method set.*

### 15. `delete-does-not-cascade`

**Deleting a course does not cascade to its obligations, and deleting an obligation does not remove notes about it; a dangling ref is legal and is recovered by the link-set validation pass.**

*Trade-off:* explicit at `design.md` §3.2 - the material requires a ref that names something absent, so the cost is that nothing enforces target existence. Surprising because it looks like a bug.

*Source: `09-plan-records.md` ADR-c, from `application-tier.md` §2.1. `POSSIBLE OVERLAP` with **M31** (`Ref`, one id space, and refs that dangle) - the schema property is near-certainly inventoried. **The two concrete cascade cases are stated only in `records/plan/`**, so the body above is narrowed to that half.*

### 16. `read-back-only-through-service-methods`

**A test that reads the store directly, or reaches the repository past the service, satisfies no criterion.**

*Trade-off:* slower and more coupled tests, in exchange for the criterion measuring the thing it names. The rejected alternative - reading the file - is the obvious cheap check. Hard to reverse once a suite exists.

*Source: `09-plan-records.md` ADR-d, from `application-tier.md` §5. `architecture.md` §4 defines "landed" and does not rule out either shortcut; the stricter form is plan-only.*

### 17. `misfitting-row-is-a-spec-failure`

**A real row that does not fit the field set is a spec failure, not a fixture patch: close the build cycle and open a design one.**

*Trade-off:* the rejected alternative - patching the fixture so the build can continue - is invisible once taken and destroys the evidence that the spec was wrong. The cost is that a build cycle can be terminated by one row.

*Source: `09-plan-records.md` ADR-e, from `application-tier.md` §5. Nothing in `domain/` or `spec/` states what happens when real material does not fit.*

### 18. `ambiguous-outcome-resolves-against-the-proposition`

**An ambiguous outcome resolves against the proposition: "it basically round-trips" is a fail.**

*Trade-off:* cheap to state, expensive in practice, and it is the rule that makes every other acceptance criterion mean anything. The rejected alternative is the default - reading a partial pass as a pass.

*Source: `09-plan-records.md` ADR-f, from `application-tier.md` §5. No equivalent anywhere in `domain/` or `spec/`.*

### 19. `closure-is-single-source-reachability`

**`closure` is single-source reachability from one node, not an all-pairs matrix.**

*Trade-off:* cost against generality, over a graph whose size is bounded by ring 0 at roughly 55 obligations for five courses.

*Source: `07-classification-B.md` explicitly hands this to reconciliation - *"the ruling that `closure` is single-source reachability, not an all-pairs matrix has no M-number in any cluster and is at risk of being lost - flagged for reconciliation as an orphan ADR candidate"*, repeated in its own summary table. Cluster B has **no `## Orphan rulings` section**; I met this line while locating one and carry it because B asked for it by name.*

***`POSSIBLE OVERLAP` with M22 and M5.*** B says it is in no cluster; the operation is read by M5 (`nodes_without`) and rides near M22's LinkKind table. Included on B's own instruction, flagged so the other reconciliation can claim it. I also note the hedge honestly: this may be a scoping definition rather than a decision, in which case it is a `CONTEXT.md` line and not an ADR.

### 20. `extraction-landing-reading-are-three-concerns`

**Extraction, landing and reading are three concerns and they change for unlike reasons.**

*Trade-off:* three seams to maintain against one ingestion pipeline. This is the record that resolves the `ingestion` word collision, and it is the ruling that makes **candidate fact** a coherent term.

*Source: `records/spec/design.md` §3.6, surfaced by `07-classification-E.md` orphan 3: cited by four inventory entries (M84, M85 and two in cluster F) and **no entry is about it**, so it has no carrier. E offers it to cluster B or F as a small ADR "if reconciliation prefers". `POSSIBLE OVERLAP` - four M-numbers cite it and none holds it, which is exactly the state that loses a ruling.*

---

## Riders - clauses that belong inside an ADR the inventoried half owns

Three. Each is one sentence, each dies as a standalone ADR, and each is the highest-value non-obvious sentence in its sitting. **Not counted in the twenty.**

1. **On whatever ADR records the tier split:** when the application tier and the presentation tier disagree about a value or a rule, the application tier is right and the divergence is a defect in the presentation tier. *Nowhere in `records/spec/` or `records/domain/` does any record state the adjudication rule for a conflict between the tiers; `architecture.md` §1 and §2 state the tiers and their ownership only. Source: `08-evidence-early.md` H3, Billy 2026-08-26.*
2. **On whatever ADR records the CLI surface decision:** the objection is to N single-purpose description-routed verbs, which is a **surface shape, not a transport** - and the ruling survived its own author's premise being falsified in the sitting, since an MCP tool result can carry rendered text and not only JSON. *`architecture.md` §5 carries the conclusion (*"What is rejected is a shape, not a protocol"*) and not the correction. The correction is the strongest available answer to a future reader who re-opens the CLI decision by re-asserting the JSON premise. Source: `08-evidence-middle.md` R4.*
3. **On whatever ADR records the language decision:** the requirement is **algebraic data types plus exhaustiveness plus enforceable module boundaries**, and "OOP native" was the wrong label for it. *`architecture.md` §6 argues from "a compiler that can refuse" and reconstructs the requirement in prose each time; the three-part form is what a future language re-opening would need. Source: `08-evidence-middle.md` R5, Billy 2026-08-27.*

---

# Merges performed

Four. Each states the shared trade-off, or for a deferral the one shared wake-up condition.

### 1. `08-evidence-late.md` N9-F7 + `backlog.md` B7 - obligation-to-obligation weight transfer

**One deferral.** These are the same item seen from two files: `REPORT.md` F7 is the finding (*"the weight of that exam will be moved to the final exam"* - a conditional re-allocation from one obligation to another, and slice 1 has one link kind, `about`, signature `annotation -> any Ref`) and B7 is its parked form.

**Shared wake-up condition:** the first mechanism that needs to relate one obligation to another - the allocation planner - which requires a second link kind. B7's stated wake is *"slice 2"*; per fall26's own instruction that slice labels do not travel, that resolves to the same condition F7 names.

### 2. `backlog.md` B3 + B4 - location, and duration or end time

**One deferral.** B3: three obligations state a venue (`LRW B1007`, `MSU Hub Loft`) and no field holds it. B4: *"Examination Duration: 150 minutes"* · *"10:30 to 11:20"* · *"5:00 - 9:00 PM"*, and `due` stores only the left edge.

**Shared wake-up condition:** the calendar projection is built - itself deferred by ruling 3, which keeps it out because `time_point`'s reader is out.

### 3. `backlog.md` B13 + B14 - `sticky_note.category`'s vocabulary and what `origin` means

**One deferral.** Both are OWED slots in `spec/write-rules.md` §4, both carry the identical stated reason (two independent passes produced non-overlapping value sets), and `schema.md` §9 item 2 makes the first blocking to a writer.

**Shared wake-up condition:** the cycle that fills `spec/write-rules.md` §4's OWED slots. *`POSSIBLE OVERLAP` with M57 - the fields are inventoried; the paired deferral and its wake may not be.*

### 4. `07-classification-C.md` orphan 8 + `07-classification-D.md` orphan 5 - the course level

**One deferral.** C8: `records/spec/course-level.md` does not exist, though the 08-29 design cycle declared it as its product, so its mandate items A-E are all still open. D5: `ring-0.md` §7's *"What this record does NOT establish ... that the course level is worth a call"*, named in the record itself as unruled and as the presentation cycle's question.

**Shared wake-up condition:** the presentation cycle convening - which is ruling 9's gate. The justification and the record that would carry it wake together and cannot wake apart.

---

# Merges rejected

Four, each with the test it failed. All four share a subject, a field or a file, which the merge criterion does not count.

### 1. `fixture-is-not-a-golden-set` + `derived-fixture-is-code-not-evidence`

**Failed: different rejected alternatives, different reasons.** The first rejects patching a completed acceptance run, on the ground that conformance to a field set was never evidence of fidelity to the material. The second rejects editing the original fixture in place, on the ground that a provenance chain must survive migration, and pays duplication for it. They share the fixture and nothing else.

### 2. `docstrings-are-design-not-documentation` + `a-write-rule-must-fit-a-docstring`

**Failed: same premise, different decisions.** Both rest on the docstring being the agent-facing surface. But the first rejects *build first and write rules after* and binds an **ordering**; the second rejects *a write rule of any length* and binds a **rule's form**. Reversing one does not reverse the other. Recorded because the shared premise should be stated once, in whichever lands first, and cited by the other.

### 3. `derivation-top-down-construction-bottom-up` + `success-path-derivation-omits-repair`

**Failed: the second falsifies the confidence the first produces; that is a sequence, not a shared trade-off.** The first rejects reverse-deriving a design from interaction requirements. The second rejects trusting a two-route union as a completeness argument. Merged, the body would need to state both the method and its known blind spot, and would not fit in three sentences - which by the criterion's own test means they were two decisions. ADR 7 should cite ADR 6.

### 4. `blind-derivation-withholds-analysis-not-material` + `preregistered-prediction-scored-on-unpredicted-yield`

**Failed: two halves of one method are not one decision.** The first rejects withholding the *material* from a blind agent, because a cold session cannot derive birth rules. The second rejects scoring a blind exercise by predicted-item recall, because a found prediction is a known hole. What to withhold and how to score are different questions with different rejected alternatives. They are the strongest merge candidate in the set and they still fail the strict test.

---

# The deferral set

Twenty-six, after the four merges. Each carries the precondition that would wake it. Anything without one is not here - it is decision 16.

## From the evidence sittings

| # | deferral | wake-up condition | source |
|---|---|---|---|
| 1 | **A description rewritten mid-arm voids the arm.** A tool definition plus its parameter names is one version; changing the description produces version 2 rather than destroying version 1, and the pre-registered prohibition forbids exactly one thing - mixing two versions' runs inside one arm's score | the first exposed verb or CLI surface carrying descriptions, at the moment anyone proposes running a routing or tool-selection evaluation against it | `08-evidence-early.md` H2 + `08-evidence-middle.md` R2's second form. Billy 2026-08-26. **Ruling 9 defers the hypothesis gate on exactly these grounds**, so the rule has no live subject yet. An ADR was considered and rejected: a decision binding an evaluation that cannot be run has no consequences to bind |
| 2 | **The flat provenance log for `annotation.origin`.** In slice 1 `origin` is a bounded tag, and the log is deferred as *"a dated liability rather than a gap"* | the first annotation whose content is an extraction from a source text the system holds - in practice, the first ingestion of announcements or handouts. At that moment either the log exists or the retracted rule *origin-bearing notes are append-only* comes back into force | `08-evidence-early.md` H4, Billy 2026-08-26. **This is record-standing-wrong #2 from the other side.** Its one proposed home - `chunk.node_id = <sticky_note id>`, making the store the log - looks **closed by ruling 6**, since raw announcement text is neither semantic nor decontextualized. Not adjudicated; recorded so the deferral is known to be homeless in a stronger sense than the sitting knew |
| 3 | **`obligation.name`'s system-owned convention.** Billy, in `records.json`: *"the `name` should follows a system-owned convention, not be inherited from the source that provides it. The 'convention' should be designed when doing the presentation layer"* | the presentation cycle producing any presentation record, which is where Billy's note put the convention. Carry the quote with it | `08-evidence-late.md` N1. **The record says the opposite** (`spec/write-rules.md` §3.1: *"one is not owed"*), and the two are about different things - the dissolution's ground is addressing load, Billy's note is about presentation. Whichever way it goes, §3's table line and §3.1's body must be made to agree; that half is record-standing-wrong #10, a defect and not a decision |
| 4 | **An ask-frequency governor on `spec/write-rules.md` §1.1.** §1.1 as written is unconditional and has no frequency governor | ruling 2's ask-frequency acceptance item becoming measurable, which ruling 2 states is *"only after the system is roughly built"* | `08-evidence-late.md` N2. Ruling 4 says *"proactivity is written too rigidly now and will bite"*, so the defect is named and its measurement is not yet possible |
| 5 | **The late-day budget conflict: the outline says 12, the student's own `assignments/README.md` says 8.** A concrete, dated, primary-source instance of the class ruling 7 governs | ruling 5's *"wait until it bites"* - the first live run where an agent must choose between 8 and 12 | `08-evidence-late.md` N8, from `REPORT.md` "Read by accident, disclosed". **This is the first recorded thing that bit.** `REPORT.md` F14 records a second two-source disagreement on the same corpus (portal *"11:59 PM"* vs outline *"up to 11:59:59 pm that day"*), **silently resolved by the extraction in favour of the portal with no rule behind the preference** |
| 6 | **Obligation-to-obligation weight transfer** (merge 1) | the first mechanism needing to relate one obligation to another - the allocation planner - which requires a second link kind | `08-evidence-late.md` N9-F7 + `backlog.md` B7 |

## The five specification gaps the blind review left, each with a real wake

`08-evidence-early.md` V8 proposed these as not-ADRs, as *"build-time specification gaps"*. I disagree on the destination and not on the substance: each is a decision deliberately not made and each has a precondition, which is the definition of a deferral. Filing them as owed implementation detail loses the precondition.

| # | deferral | wake-up condition |
|---|---|---|
| 7 | **Timestamp precision, timezone and clock authority.** `schema.md` §1 says *"timestamps \| ISO 8601"* and nothing more; ISO 8601 admits four conformant renderings of one instant, and a UTC `added_at` cannot be ordered against a local `due` | **before the first timestamp is persisted.** This is the one with an ADR argument: if the successor persists any timestamp before deciding this, it has decided it by accident and the decision is then hard to reverse because data exists |
| 8 | **`term`'s vocabulary.** `schema.md` §2 gives an example (`winter-2026`), not an enumeration. *"Fall 2026"* becomes `fall-2026` or `autumn-2026`, grouping splits into two non-empty buckets, and nothing looks broken | the second term's data entering the system |
| 9 | **`updated_at`'s currency threshold.** It *"gates"* currency with no number: *"A progress answer asked nine days ago is current, or not, on a coin flip"* - and this is the load-bearing half of the ask-at-read mechanism | the ask-at-read mechanism being built. Compounds with deferral 4 |
| 10 | **`schema_version` mismatch behaviour.** §8 says a version exists and why, and not what a reader does when it does not match | the first schema change after data exists |
| 11 | **What a one-hop walk returns for a deliberately dangling `to`.** `schema.md` §1 rules a `Ref` may name something not present and `design.md` §3.2 prices that case; neither says what the walk returns. If null, a dangling link is indistinguishable from an orphaned note, which the maintenance rule may then detach | the walk being implemented. Rides on ADR 15 |

## From `records/plan/backlog.md`

Twelve, with the wake conditions the backlog itself states, corrected where a 08-30 ruling moved one.

| # | deferral | wake-up condition |
|---|---|---|
| 12 | **Recurring and countable obligations (B1)** | a fourth course confirming the pattern, or a read that actually needs the count. **Conditional on decision 1:** this deferral exists only if Billy takes option (c) |
| 13 | **Location, duration and end time (B3 + B4, merge 2)** | the calendar projection is built |
| 14 | **Is the IDEA Conference a `time_point` (B12)** | `time_point` arriving, which needs the calendar projection. Shares deferral 13's wake; kept separate because it is a kind question and not a field gap. **Decision 3 asks whether to keep the row now, which is a different question** |
| 15 | **The marking-scheme mechanism (B6).** A bool says *this number is one reading*; it cannot say which readings exist or that the choice is by maximum | a planner that allocates against weights |
| 16 | **The per-assignment late cap of 3 (B8).** The course-level 12 works as a note; the per-obligation half has no home short of duplicating prose nine times | a planner that models the budget |
| 17 | **Deliverable structure, separate from concepts (B9).** Most assignments owe two named artifacts; `parts` carries concepts | the artifact layer |
| 18 | **Course-level facts with no field (B10)** - instructor, term boundaries, units, prerequisites, antirequisites, textbook | term boundaries becoming load-bearing, i.e. read-time expiry or the last-day-of-classes rule being built. **This is decision 4's unaddressed second half** |
| 19 | **`course.prereq` (B11)** | a second domain. **Reinforced by ruling 1**: deferred to v2, not dead |
| 20 | **`sticky_note.category`'s vocabulary and what `origin` means (B13 + B14, merge 3)** | the cycle that fills `spec/write-rules.md` §4's OWED slots |
| 21 | **The store has no tier (B18).** `architecture.md` §1's table has three rows and none is the store, yet the purity cut is a boundary against it | the store being built |
| 22 | **`look_at`'s return shape, and where a node's own typed fields arrive (B19)** | a presentation record existing. **Blocked by ruling 9** |
| 23 | **A load-time construct pass (B24).** *"a malformed line loads clean and survives the next flush"* | the composition root, which is the CLI. **Blocked by ruling 9** |

## Structural

| # | deferral | wake-up condition |
|---|---|---|
| 24 | **Where the id counter lives (B29's residue).** Named in the backlog as *"a decision this ruling did not make"* | the next build cycle touching persistence. **Also decision 15** - listed in both because it is a parked item that contains an undischarged ruling, and Billy may prefer to rule it rather than let it wake |
| 25 | **The course level: whether it is worth a call, and the record that would carry it** (merge 4, C8 + D5). `records/spec/course-level.md` does not exist though the 08-29 cycle declared it as its product; its mandate items A-E are what the course level renders · the length bound · `has-more`'s shape · which layer applies `due`'s `23:59` · `look_at`'s return shape | the presentation cycle convening - ruling 9's gate. **Note that the ground `ring-0.md` §7 gives for leaving it unruled is record-standing-wrong #1** |
| 26 | **`plan` as a fact type.** Defined at `domain-design.md` line 300 and named by `ring-0.md` §7 as having *"no representation anywhere"* | **ruling 3**: schema, API and CLI shape have settled, and the plan gets its own grilling session. `POSSIBLE OVERLAP` with **M75b**, which cluster D says holds the plan with a conflict number and no M-number |

---

# The drop set

Six classes. Each with its reason and its kind.

### 1. Abandoned steps - 31 of them. Kind: abandoned step

Not carried, individually or as a class. Each was written confidently inside the sitting that dropped it, each is tagged as abandoned by the survey that met it, and the tags are respected here. **The whole point of listing the class is that no later reader promotes one to a ruling.**

- **`08-evidence-early.md` A1-A12:** the operation-first mandate · reading *"any mid-test rewrite voids the arm"* as a total block on drafting · criterion d2 (owed fields may remain named holes) · the five-column field document · **`draft-contract.md` itself as a specification** - 244 lines, all 31 fields, and by its own §0 test roughly half its entries were not rules; **its individual sentences must not be quoted as contract** · Position A on `obligation.parts` · the annotation id scheme `<target-id>-<kind>-<n>` · uniqueness on `(obligation_id, course_id)` · *"obligation objects are attached to a course through typed edges"* · the internal-versus-external field axis · pre-creating the next session's file · the *"eighteen days before launch"* defence.
- **`08-evidence-middle.md`, nine:** ids re-minted from `name` · annotation ids under `<target-id>-<kind>-<handle>` · Cycle 2's Track A cut on artifact type instead of consumer (two layers of abandonment on one question) · the seal on `plan/write-rules.md` §9 · the sealed two-position `parts` question · increments named after `design.md` §3.4's operation set · Python as the recommendation · the JSON-only premise for rejecting MCP · **`derivations/L3-surface.md`'s CLI probe**, self-labelled disposable with four named invented holes.
- **`08-evidence-late.md`, ten:** the `<course>-slug(name)` handle · the one-row-per-item table, variants A/B/C · variant C's ordinal handle · the `share` column in every variant · *"`obligation.parts` is homeless"* · *"the coordinator is not a caller"* · *"the course level is ring 0's complement, and that is why it exists"* · `seam` as the 08-29 cycle's axis · the three dissolutions of 2026-08-28 · the ring-0 sitting's four agent corrections.
- **`records/plan/write-rules.md` §9's two positions on `parts`** - superseded by a ruling; it is the history of an adjudication, not a live question.

**One qualification carried, not resolved.** `derivations/L1-material.md`, `L2-lifecycle.md` and `L4-invariants.md`'s capability lists are dropped **as proposals** and not as evidence: they are derivations under an assigned lens by agents blind to the plan, never adjudicated. Treat any single "capability N" as an argument with evidence attached, never as a decision. Their fate is decision 17.

### 2. The 08-25 methodology layer and the seal mechanism. Kind: old-container artifact

Cycles, the four modes, the 200-line cap, `standing: mixed`, the record classification by what-can-change-it, and the whole independence apparatus (`plan/write-rules.md` §4's reading prohibition, §6's stage gating, §9's seal). These are properties of a standalone repo run as an app by a human who convened separate cold sessions. **The successor is components an agent uses**, and the independence device failed here anyway - the seal was broken on the same day the session that built it opened.

### 3. Sequencing. Kind: old-container artifact

Everything in `09-plan-records.md` §Sequencing, set aside: the build order slices 0-3 · per-slice acceptance sentences · the eleven trace verdicts · the coverage snapshot · the freeze rule · the fixture rename list (`finished_by`→`done_by`, `kind_of_node`→`kind`, `kind`→`category`) · the mandate's procedure and out-of-scope list · un-parking conditions phrased as slice numbers. Per fall26's own instruction: *"there is no plan of record ... cite them, do not follow their order."* The **dependency** each slice label encodes is preserved inside its deferral; the label is not.

### 4. Code specifics of a repository that is not migrating. Kind: old-container artifact

B22's `flush()` O(n²), B23's `${path}.tmp` concurrency, B28's `kinds.ts:153` nullable `ProgressState`, B29's `ids.ts` slug scheme, and `application-tier.md` §2.4b's method inventory (`listUntargeted`, `listAll`, `hasId`, `nodesOfKind`, `allLinks`, `danglingLinks`, `IntegrityService.dangling`). The **decisions** inside B26 and B29 are carried as decisions 14 and 15; the file-and-line claims are not.

### 5. Two superseded rulings and one closed proposal. Kind: exposition

- **A `progress.detail` with no state: the landing asks** (`08-evidence-early.md` H5, Billy 2026-08-27). Not carried, **superseded twice**: `progress.state` became non-nullable on 2026-08-28, so the shape a writer could be stuck in no longer exists, and ruling 4 makes `not_started` the default *precisely so the agent does not keep asking*. Recorded so nobody finding the 08-27 disposition in isolation revives an ask that two later rulings removed the reason for.
- **The provenance log IS the store, `chunk.node_id = <sticky_note id>`** (`08-evidence-early.md` H6). Never a ruling - the sitting flagged it as its own derivation. Not carried, and it looks **closed rather than merely unlanded** by ruling 6. Its cost was stated by its own author: a provenance chunk carries text with no query purpose and an embedding nobody searches.
- **Two process rulings whose home is methodology** (`08-evidence-early.md` H7): field definitions first, agent surface second, routing test third - superseded within days by the three-tier split; and *analysis first, decisions one at a time, the document last*. Their home in the old container was `~/.claude/CLAUDE.md`.

### 6. Measurement-instrument warnings already stated where they warn. Kind: exposition

`ring-0.md` §2's routing test is agent-drafted and unmeasured, and §2 says so. `domain-design.md` §9.2's judgment-change gate is marked in §9.2 itself as *"agent formulation ... not separately ruled"*, and its one run came from an instrument that could not have detected the effect. Both are already carried by the records they qualify; repeating them creates a second copy that can go stale independently.

## A fifth kind the drop reasons do not cover, flagged rather than forced

Three items are **working-practice rules for agents**, not decisions about the semester, not terms, and not container-specific enough to call old-container artifacts. Forcing them into one of the three stated reasons would misfile them.

1. **"Before treating any list as exhaustive, state what question it was written to answer"** (`2026-08-29-course-level/NOTES.md` §3). Stated after two agent errors that were the same reasoning move - an agent argued for two rounds against a ruling it had not read. `07-classification-D.md` orphan 3 reaches the same conclusion: *"it belongs wherever this repo keeps its agent instructions."*
2. **"An artifact hands over its vocabulary along with its content"**, and its named instance, **"a frozen artifact's vocabulary set the plan's units"** (`2026-08-27-tier-recut/NOTES.md`, `2026-08-28-ring-0/NOTES.md`). This error class recurs across the corpus: it is the shape of records-standing-wrong #8, #9, #14 and #15, where a record frozen before a ruling still supplies vocabulary.
3. **`evidence/README.md`'s standing caveat:** *"Most of this project's measured numbers are NOT auditable from this checkout. The evidence behind them stayed in the openclaw checkout by ruling."* Not a term and not a decision, but it is **the correct caveat on every number quoted from fall26**, and any successor that cites fall26 as provenance inherits it.

**Proposal:** these belong in the successor's `CLAUDE.md` or its agent-skill documents, which is a fifth destination outside this migration's four. Flagged for Billy rather than dropped silently, because item 3 in particular attaches to the migration's own core plan - citing rather than copying.

---

# Broken citations

Twelve. Ordered by how badly the reader is misled, worst first. The first three are the class the brief named, and there are **three of them, not two**.

## Silent mis-resolution - the citation resolves to something real and wrong

`records/plan/` contains a `write-rules.md`. Any unprefixed `write-rules.md` citation written from inside `records/plan/` therefore resolves to that sibling instead of `../spec/write-rules.md`. Verified at source: `plan/write-rules.md` has §1, §2, §2.1, §3-§9 and **no §1.1 and no §3.1**.

| # | citation | in | resolves to | intended target | severity |
|---|---|---|---|---|---|
| 1 | ``write-rules.md`` **§1** | `backlog.md` **B9** (*"`parts` carries concepts, not deliverables"*) | **`plan/write-rules.md` §1, "The question, bounded" - a real section that says something else** | `../spec/write-rules.md` §3.4 | **Worst in the set.** The only one that resolves to an existing section, so it fails silently in both directions: a reader following it lands on a live section and has no signal anything is wrong. **Not previously reported by any survey** |
| 2 | ``write-rules.md`` **§1.1** | `backlog.md` **B25** | `plan/write-rules.md`, which has no §1.1 | `../spec/write-rules.md` §1.1 | **Load-bearing.** B25 is the ruling that settles decision 5, and §1.1 is *"an inferred value is asked about, not annotated"* - the write-side half of ruling 7 |
| 3 | ``write-rules.md`` **§3.1** | `backlog.md` **B15** | `plan/write-rules.md`, which has §3 but no §3.1 | `../spec/write-rules.md` §3.1 | B15 is the dissolution N1 contests |

**Why it is exactly these three.** Every other backlog cross-reference to a record in another directory is correctly prefixed (`../spec/schema.md`, `../domain/model.md`). The three failures are all to the one record whose filename collides across two directories.

## Unprefixed and dangling - the citation resolves to nothing

Lower severity because it fails visibly rather than silently, but it is the same defect and it is pervasive.

| # | citation | in | should be |
|---|---|---|---|
| 4 | ``schema.md`` (B1, B24), ``architecture.md`` (B18), ``schema.md`` §4.6 (B19), ``schema.md`` §4.6 (changelog) | `records/plan/backlog.md` | `../spec/schema.md`, `../spec/architecture.md` |
| 5 | ``schema.md`` §6 | `records/plan/write-rules.md` line 131 | `../spec/schema.md` §6 |
| 6 | ``design.md``, ``schema.md``, ``architecture.md`` - throughout §2.1, §2.2's trace table, §2.4b, §4, §5 | `records/plan/application-tier.md` | `../spec/*` |

## Imprecise, stale or unreachable targets

| # | citation | problem | fix |
|---|---|---|---|
| 7 | `records/spec/schema.md` §8 line 194: *"it is parked at `../plan/backlog.md`"* | **no item number**, so a reader must scan a file with a non-contiguous numbering scheme to find it | the target is **B24** |
| 8 | `evidence/2026-08-27-tier-recut/derivations/README.md`: *"The adjudication is in `../ADJUDICATION.md`"* | **the target has never existed in any branch's history.** I verified with `git log --all --diff-filter=A --name-only` over the whole checkout: no path matching `ADJUD*` was ever added | routed below |
| 9 | `records/spec/architecture.md` changelog line 127 cites `backlog.md` **B20** | B20 is **struck through and dissolved**. A live record names a dissolved item as the home of a withdrawn recommendation | either re-home the recommendation or mark the citation as pointing at a closed item. Note `schema.md` §4.6 and its changelog cite **B19**, which is live and correct |
| 10 | `records/plan/application-tier.md` condition line: *"executable only while `../spec/architecture.md` §5-§7 stand"* | **§6 no longer stands** - the packaging ruling was reversed 2026-08-28. The plan cites its own precondition and does not know the precondition broke | records-standing-wrong #6 |
| 11 | `records/plan/backlog.md` numbering: the sequence runs B15, then B18-B29 | **B16 and B17 do not appear anywhere in the file** and no changelog entry explains their absence. Any external citation to either resolves to nothing | reported as a gap, not resolved |
| 12 | `records/domain/model.md` §4.1's retirement threshold: *">= 80% of `look_at` calls have their stated question answered"* | a citation to an **unmeasurable instrument**: `architecture.md` §5 rules a CLI grammar, which does not produce `look_at` call statistics. The condition cannot be evaluated by construction | records-standing-wrong #22 |

---

# `ADJUDICATION.md` and `preference`

## `ADJUDICATION.md`

**The facts, verified at source.** `evidence/2026-08-27-tier-recut/derivations/README.md` ends *"These are the reports as returned, unedited. The adjudication is in `../ADJUDICATION.md`"* - in the present tense. The directory holds `NOTES.md`, `PREREGISTRATION.md` and `derivations/`, and nothing else. `git log --all --diff-filter=A --name-only` over the whole checkout returns no path matching `ADJUD*` in any branch's history: **it was never written, not written and lost.** Behind the missing file sit four blind derivations (`L1-material`, `L2-lifecycle`, `L3-surface`, `L4-invariants`) under a pre-registered falsifiable prediction, producing roughly ninety derived capabilities and forty-odd stated contradictions. Across all seven records in `domain/` and `spec/` they are cited **exactly once** - `ring-0.md` §5, for the missing cross-course read.

**What is at stake, stated precisely.** Two things, and they are separable.

1. **The prediction was never scored.** `PREREGISTRATION.md` states its own reading rule (ADR 9) and its own expected error - *"That the yield concentrates in L2 and L4. If L1 or L3 produces the most, my model of where prose-derived coverage fails is wrong, and that is worth more than the individual findings."* `08-evidence-middle.md` reports, without adjudicating, that reading L1 and L3 against the twelve predicted items suggests the great majority of both files' findings are unpredicted - which under the file's own rule is the exercise working and the lead's stated expectation being wrong.
2. **The ninety capabilities have never been dispositioned.** Whether they were read and rejected or never opened is not recoverable from the records. Several were independently re-derived later and turned out to be right: `L1-material.md` capability 9 is the timestamp-assigner gap that `08-evidence-middle.md` R9 reached separately; `L4-invariants.md` capability 14's *"F2 has no home in the first build"* is now governed by ruling 7.

**Routing proposal: `Needs Billy`, as decision 17 above, not a deferral.** A deferral needs a wake-up condition, and there is no future event that makes this cheaper or more decidable - the material is complete now and decays as the design moves under it. The decision is binary and Billy's:

- **Score it.** Roughly a sitting's work over material that is all on disk, producing the one thing the exercise was built to produce - a measured answer about where prose-derived coverage fails, which is a claim about method that outlives this project.
- **Retire it.** Declare the four derivations evidence-only, mark `derivations/README.md`'s dangling reference as never-written, and accept that ninety capabilities and forty contradictions are searchable material rather than a reviewed set.

**What must not happen is the third option, which is the current state:** a live record referring in the present tense to an adjudication that does not exist, over material that four surveys have now each partially re-derived by hand. `08-evidence-middle.md` names this *"the single largest reservoir of unadjudicated material"* and `08-evidence-middle.md` Q3 calls it *"the decision that gates everything else in the tier-recut directory."* I agree with both and add one observation neither makes: **the cost of retiring it is not zero and is not recoverable** - the derivations were produced blind, and once anyone has read the plan they cannot be re-run.

## `preference`

**The facts, verified at source.** `records/domain/domain-design.md` line 300 defines `preference` in §6's fact-type table with a field set (`id · scope (global | course) · updated_at`), a free-text column (*"the preference itself"*) and a named reader (M4). §8 argues it at length: *"Preferences are not a new layer - they are a fact type. Structurally it is identical to `progress`"*, with a precedent named (`memory/calibration.md` as a preference store with a write discipline). I grepped all of `records/spec/`: **zero occurrences.** Not in `schema.md`'s kind set, not in §7's graveyard, not in `design.md` §3.1's slice-1 or slice-2 kind lists. It is neither carried nor graveyarded, which `migration-gaps.md` §2.1 names as worse than either: *"a reader cannot tell whether it is deliberately absent or overlooked."*

**Why it does not route the way `plan` does.** `plan` is in the identical state - a fact type in the same table, absent from the same spec - and **ruling 3 disposes of it**: a real requirement, not settleable now, needing its own grilling session after schema, API and CLI shape settle. That is a wake-up condition, so `plan` is deferral 26. **No ruling reaches `preference` at all.** Ruling 1 does not exclude it (a coursework preference is coursework), ruling 6 does not touch it (it is a fact type, not RAG content), and ruling 9's gate is about the surface rather than the fact set.

**Routing proposal: `Needs Billy`, as decision 11 above, and the ask is one question with three answers.** The question is *which of these is true of `preference` in v1*, and each answer has a different destination:

- **It is v1 scope.** Then it is a schema gap of the same weight as any missing kind, and `schema.md` needs a row. This is the answer §8's own argument implies - *structurally identical to `progress`*, and `progress` is in slice 1.
- **It is out for v1, deferred.** Then it needs a wake-up condition, and the natural one is the same as `plan`'s, because §8 pairs them: a preference has no reader until something plans against it. That would make it deferral 27 and merge cleanly with 26 under one wake.
- **It is out, full stop.** Then it goes in `schema.md` §7's graveyard with a stated ground, under the same do-not-re-add rule as the other rows.

**My recommendation, offered as the start of a discussion.** The second. §8's own argument is that a preference is *"exactly what one never thinks to record"*, which is a claim about a **capture** mechanism, and capture has no surface until the CLI exists - so the wake is ruling 9's gate rather than the plan's. Against that: §8 also says preferences are *"nearly all free text, so it carries no rewrite danger and needs no confirmation"*, which is an argument that adding the row is cheap and safe now. I do not think that settles it, because a cheap row with no reader is exactly what `grade_share` is, and decision 2 is what that costs. **Billy's call; not made here.**

---

# Possible overlap with the inventoried 115

Eleven flags. Each is included in this document rather than dropped, on the brief's instruction to include where unsure. **None is resolved, and none is a re-classification.**

| item | destination proposed here | suspected M-number | why the doubt |
|---|---|---|---|
| **`corpus-bounds-content-not-record-shape`** (ADR 11) | `docs/adr/` | **M59** | The two classifying agents contradict each other. `07-classification-C.md` orphan 5 says *"fully absorbed into M59"*; `07-classification-D.md` orphan 4 says it has **no M-number in any cluster** and calls it the highest-value orphan. **This is the most consequential item in the residue and must not fall through the disagreement** |
| `closure-is-single-source-reachability` (ADR 19) | `docs/adr/` | **M22, M5** | `07-classification-B.md` explicitly says it has no M-number in any cluster and hands it to reconciliation; the operation is nonetheless read by M5 and adjacent to M22's table |
| `extraction-landing-reading-are-three-concerns` (ADR 20) | `docs/adr/` | **M84, M85, and two in cluster F** | `07-classification-E.md` orphan 3: four entries cite `design.md` §3.6 and **no entry is about it**. Cited-by-four-and-held-by-none is the exact state that loses a ruling |
| `origin-carries-no-locator` (ADR 10) | `docs/adr/` | **M57** | The field is certainly inventoried. The **constraint that its vocabulary may not carry a locator** is not visible in the survey material |
| `delete-does-not-cascade` (ADR 15) | `docs/adr/` | **M31** | The `Ref`-may-dangle property is inventoried. The two concrete cascade cases are stated only in `records/plan/`, so the body is narrowed to that half |
| The tier-split rider (rider 1) | rider on an inventoried ADR | the tier-split thing in cluster B or F | The tiers are certainly inventoried; the **adjudication rule for a conflict between them** is in no record |
| The CLI-surface rider (rider 2) | rider on an inventoried ADR | the surface-shape thing | `architecture.md` §5's conclusion is inventoried; the falsified-premise correction is not |
| The language rider (rider 3) | rider on an inventoried ADR | the language thing | §6's argument is inventoried; the three-part form of the requirement is not |
| `preference` and `plan` deferral wake (deferral 26, decision 11) | deferral / `Needs Billy` | **M75b** for `plan` | `07-classification-D.md` orphan 6 says the plan is carried at M75b but flags it as *"an inventory completeness gap"* with a conflict number C49 and no M-number |
| **write rule** as a term | rejected as a term | cluster E's write-rules set | Rejected outright rather than proposed, because E owns this material |
| B13 + B14 merged deferral (deferral 20) | deferral | **M57** | The fields are inventoried; the paired deferral and its single shared wake condition may not be |

## Items I confirmed are NOT mine, recorded so the scope rule is auditable

Four orphan rulings from the classification files are routed **into the inventoried half by the classifying agents themselves**, so they are out of scope here. They are listed because in each case the routing is a recommendation and not a completed move, which means each could still fall between the two reconciliations.

1. **`spec/write-rules.md` §1.1 - "an inferred value is asked about, not annotated. An update is an update."** `07-classification-C.md` orphan 1 recommends it go with cluster E's write rules; `07-classification-E.md` orphan 1 recommends adopting it into M85's ADR and explicitly says *"do not create a separate thing"*. **Both route it inward. Not mine.** Recorded because it is **ruling 7's invariant already written at field level, eight days before ruling 7**, in the one place a write actually happens - and because two of the three broken citations above point at it.
2. **`schema.md` §4.6 - annotations arrive through their own channel.** *"a read that returns a node's neighbourhood must deliver `sticky_note` and `progress` through their own channel, never as ordinary neighbours."* C orphan 2 gives it to D with M76. The inventory currently records §4.6 only at M76 and only its **withdrawal** of the `{summary, annotations[], edges[]}` triple: **the withdrawal is captured and the ruling that replaced it is not.** Not mine, and at risk.
3. **`schema.md` §4.5 - a progress record with no `about` link is legal**, meaning progress on a free topic named in `detail`. C orphan 3 folds it into M51 and warns it *"is the clause most likely to fall out"* if M51 is merged or trimmed. Not mine.
4. **`schema.md` §4's two-tier maintenance rule** - *"a target revised later than the note is evidenced staleness the agent may act on in passing, while anything else may be surfaced for confirmation and never resolved."* E orphan 2 carries it at M85, distinction 2. Not mine, and worth naming loudly: it is **the corpus's only existing shallow-versus-deep conflict policy and the only place an agent is currently allowed to resolve silently**, which is exactly where ruling 7 anchors.

Also not mine, and each already routed inward by its own classifier: *"ring 0 governs residency, not readability"* (D orphan 1, carried into M66/M67), *"`look_at(course)` is a call"* (D orphan 2, carried into M75), the graveyard's sixteen-versus-fifteen row count (C orphan 7, stated in M62), and the ~55-obligation figure's real home at `design.md` §8 (D orphan 7, a correction to M11's assumption).

---

# Coverage

## Read in full

- `/Users/billywu/Documents/Projects/semester-manager/research/08-evidence-early.md` - 387 lines
- `/Users/billywu/Documents/Projects/semester-manager/research/08-evidence-middle.md` - 310 lines
- `/Users/billywu/Documents/Projects/semester-manager/research/08-evidence-late.md` - 399 lines
- `/Users/billywu/Documents/Projects/semester-manager/research/09-plan-records.md` - 429 lines

## Read in part, by instruction

The `## Orphan rulings` sections only of `07-classification-C.md` (lines 928-955, 8 items), `07-classification-D.md` (lines 521-534, 7 items) and `07-classification-E.md` (lines 511-524, 3 items). **`07-classification-B.md` has no `## Orphan rulings` section** - I confirmed by listing its headings, then grepped it for `orphan` to see whether the material was elsewhere. It is: two lines, at §M22's cross-cluster note and in its summary table, both handing the `closure` ruling to reconciliation by name. Those two lines are the only content I read from B. No other part of any `07-*` file was opened.

## Zoomed to source, to settle and not to re-derive

Nine checks in `/Users/billywu/Documents/Projects/fall26/`, each because a claim was load-bearing and disputed or previously unverified:

| what | where | outcome |
|---|---|---|
| the 1,881 / 871 sentence | `records/spec/ring-0.md` §7 | confirmed verbatim; it is the stated ground for the record refusing to establish the course level's worth |
| the flat provenance log premise | `records/domain/model.md` §8.1 (lines ~529-535) | confirmed verbatim, present tense, inside the `[R]` retraction |
| the three unprefixed `write-rules.md` citations | `records/plan/backlog.md` B9, B15, B25 | confirmed, and **one more found than the brief named** - B9, which resolves to a real wrong section |
| section indices of both `write-rules.md` records | `records/plan/write-rules.md`, `records/spec/write-rules.md` | confirmed `plan/` has §1 and §3 but no §1.1 and no §3.1, which is what makes B9 the worst of the three |
| `name` OWED versus not owed | `records/spec/write-rules.md` §3 table line 58 vs §3.1 | confirmed, one screen apart in one record |
| `preference`'s absence | grep over all of `records/spec/` | **zero occurrences**; definition confirmed at `records/domain/domain-design.md` line 300 and §8 |
| `course.prereq`'s falsified ground | `records/spec/schema.md` §7 | confirmed uncorrected |
| whether `ADJUDICATION.md` ever existed | `git log --all --diff-filter=A --name-only` over the whole checkout | **never added in any branch's history** |
| repo state | `git branch --show-current` | `design/course-level`, as the surveys report |

**Not opened**, and the boundary was observed: no openclaw path, no other repository, no `app/` source, no `~/Documents/McMaster/`, no `records/archive/`, no `records/findings/`, no `evidence/` file beyond what the surveys quote.

## What I could not account for

1. **The fifth live item in `decisions.md`.** `08-evidence-early.md` states *"Seven are answered. Five are live"* and its own twelve-row table yields four unambiguously live items - #1, #8, #9 and #10, which are decisions 6-9 above. #7 is tabled as *"Answered, then mooted"*, which is not live. The fifth is either #7 counted differently or the Handoff's `grade_share`-name item counted into the same total; I carry the latter separately as decision 10 rather than guess. **Reported as an arithmetic discrepancy in the source, not resolved.**
2. **`evidence/2026-08-29-course-level/NOTES-plain.md`.** Committed in `9d4298a`, deleted in the working tree, not recovered by `08-evidence-late.md` and not chased here. Described by its own commit subject as a plain-English restatement of NOTES §4-§6, so its content is presumed to duplicate material that was read. **The presumption is untested.**
3. **`records/plan/backlog.md` B16 and B17.** They exist in no version of the file and no changelog explains the gap. Any external citation to either is unresolvable. Carried as broken citation 11.
4. **The exact residue-item total.** The four surveys overlap partially and count differently - the same void appears as `08-evidence-early.md` V1 and as `08-evidence-late.md`'s record #2 with different framings. The ~205 figure is a count of distinct items after de-duplication by subject, and it is approximate. The **destination counts** in the header are exact.
5. **Two counts in the brief that came out higher.** The brief said *"about eighteen"* records standing wrong; I reach **24 sites across 9 records**, because the four surveys' lists overlap only partly and `09-plan-records.md`'s V1 and V2 add two record-sites nobody else had. The brief said *"at least two"* broken ruling-bearing citations; I reach **three** of that exact class, plus nine other broken or ambiguous references.
6. **Anything `records/archive/` holds.** Four files (`build-plan-2026-08-27.md`, `changelog-2026-08-24-slice-1.md`, `openclaw-registry-2026-08-25.md`, `slice-1-plan-2026-08-27.md`) were outside the boundary and outside all four surveys' boundaries too. Three citations in `records/plan/` point into it and could not be followed. **No survey has read `records/archive/`**, and if the migration intends to cite `fall26` as provenance, that is an unswept corner.
