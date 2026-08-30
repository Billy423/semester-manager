# Survey — the three latest evidence sittings (2026-08-28 corpus, 2026-08-28 ring 0, 2026-08-29 course level)

**What I read, all in full.**

- `/Users/billywu/Documents/Projects/fall26/evidence/README.md` (9 lines)
- `/Users/billywu/Documents/Projects/fall26/evidence/2026-08-28-corpus/2c03/RULINGS-NEEDED.md` (71) · `REPORT.md` (83) · `LABELING.md` (108) · `records.json` (87)
- `/Users/billywu/Documents/Projects/fall26/evidence/2026-08-28-ring-0/NOTES.md` (72) · `corpus-counts.txt` (28) · `render-candidates.py` (47) · `render-candidates.txt` (100)
- `/Users/billywu/Documents/Projects/fall26/evidence/2026-08-29-course-level/NOTES.md` (89) · `measure.py` (40) · `measurements.txt` (20)

**Read only to check whether a ruling reached a record:** `records/domain/model.md`, `records/domain/domain-design.md`, `records/spec/schema.md`, `records/spec/ring-0.md`, `records/spec/write-rules.md`, `records/spec/architecture.md`, `records/spec/design.md`. Plus `git log`, `git status` and `git show 63612df` to establish state and attribution.

**Boundary observed.** No other `evidence/` directory, no `records/plan/`, no `records/findings/`, no `records/archive/`, no `app/`, no openclaw path, no other repo. Where an item turns on `records/plan/backlog.md` (B19, B25, B27) I saw those entries only inside the diff of `63612df` and say so at the point of use. `app/tests/fixtures/2c03.json`, which `render-candidates.py` actually reads, was NOT opened; where the fixture and `records.json` differ I say the difference is inferred from `corpus-counts.txt` and not verified.

**State.** Branch `design/course-level`; `git diff main -- records/` is empty, so every record quoted here is also main's. `evidence/2026-08-29-course-level/NOTES-plain.md` is committed in `9d4298a` and shows as ` D` in `git status`: **it is not on disk and I did not recover it.** It is described by its own commit subject as "a plain-English restatement of NOTES 4-6", so its content is presumed a restatement of material I did read; that presumption is untested.

**What these files are.** `evidence/README.md`: *"Conclusions go into a record; the material that produced them stays here and is never deleted."* Nothing below is a truth record and nothing below is adjudicated. Every item is tagged **[RULING]**, **[ABANDONED]** or **[OBSERVATION]**.

---

## The five open decisions

`RULINGS-NEEDED.md` opens: *"Five decisions, each with the source quote. **These block the other three courses**, because the same choices will recur there and I do not want to make them four times by default."*

**One standing caveat over all five.** `records/spec/architecture.md` §4 (line 59) already rules that *"extracting the other three courses is not worth doing before the presentation tier exists"*, because *"every contested field ... needs a write rule, and a write rule is derived from what a value must be for a node to render well"*. So the file's own "these block the other three courses" urgency is partly overtaken: the other three are blocked anyway. What is NOT overtaken is that four of the five name a defect in a record that is standing today.

**Nothing since 2026-08-28 has read this file.** It is referenced from `REPORT.md` F1/F2/F13 and from nowhere in `records/`.

---

### R1. Tutorial attendance gets no row, and it is 5% of the grade — **OPEN**

**The decision.** Hold the recurring-obligation graveyard, re-open it, or defer and decide with four courses' worth of instances.

**Verbatim, the options as the file states them:**

> - **(a)** hold the graveyard - tutorial attendance stays a note, and the same for every lab and worksheet
> - **(b)** re-open it - a recurring obligation kind, or `count`, comes back by ruling
> - **(c)** defer - mark it unresolved, keep collecting instances across the other three courses, decide with four

**What turns on it.** A 5% graded, *required* obligation is invisible to ring 0. `records/spec/schema.md` §7 graveyards `count{done, of}` on *"one instance in 22"*, and the same row records its own weakness verbatim: *"the `n=1` behind not carrying `count` was measured on the two courses least likely to contain recurring items, and 2px3 was excluded throughout."* The file reports the instance count is now four, not one: *"This is now a second instance, and 2da4's five labs plus 2px3's weekly worksheets are a third and fourth."* Those two further instances are asserted by the file and are not verifiable inside my boundary.

**Downstream already.** `records/spec/architecture.md` §4 (line 59) has taken option (a) as fact: the acceptance criterion's obligation count moved from 22 to 14 partly because *"the old count included a row the graveyard forbids (recurring tutorial attendance)"*. So (a) is the de-facto state of a truth record while the decision is formally open.

**What has moved since 2026-08-28.** Billy 2026-08-30 ruling 2: *"the work need not be a functional one-pass: the agent sees the skeleton and ring 0, notices, and asks when needed."* This bears on R1 in both directions and the file does not settle which: an agent can only notice what ring 0 shows it, and under (a) tutorial attendance is not in ring 0 at all. Ruling 1 (v1 is coursework inside academics) does not exclude tutorials, which are coursework.

---

### R2. `grade_share` cannot hold a bonus — **OPEN, and reported as a live undiscovered schema defect**

**The decision.** How an additive bonus is represented, given that `grade_share` is defined as a share of a total that already sums to 100.

**Verbatim, with its sources:**

> "I'm offering a 1% course bonus for attendance at this conference" (announcement, Jan 6)
> "I'm willing to give you a +1 bonus on your final grade ... if you fill in my Attendance Survey" (Mar 20)
>
> `grade_share` is defined as *"Approximate share of the final course grade, in percent"*. The course's real shares already sum to 100 (5 tutorials + 45 assignments + 50 exams). Both bonuses are **additive, outside the 100**. Storing `1` asserts something false; `optional: true` is the only signal separating them and it does not carry additive semantics.
>
> **This one is new.** Four independent spec reviews missed it, because seeing it requires the arithmetic.

**Confirmed at source.** `records/spec/schema.md` §3 defines the field exactly as quoted. `records.json` stores `grade_share: 1` on both bonus rows. `evidence/2026-08-28-ring-0/corpus-counts.txt` prints `grade_share sum over all rows: 97`, and `render-candidates.txt`'s own header names the consequence: *"the share column sums to 97 and reads as a partition of 100 that it is not"*. The file states the arithmetic as 5 + 45 + 50 = 100 for the *stated* shares; the stored rows sum to 97 because tutorials (5) have no row and the two bonuses (+2) are outside the total.

**No record carries it.** `schema.md` §7's graveyard has no bonus row; `schema.md` §9's "Still owed" has five items and none is this; `write-rules.md` §3's table gives `grade_share · grade_share_conditional` the line *"none yet"*.

**What has moved since 2026-08-28.** Billy 2026-08-30 ruling 2: *"`grade_share` is reference only, never an input."* `schema.md` §3 already says this verbatim and calls it *"a standing EXEMPTION ... no mechanism reads it, and the exemption is the point"*. That bounds the blast radius (no computation can be corrupted by the false value) without making the stored `1` true; the reader harmed is a human or an agent reading the field for reference, which is the field's only declared purpose. Whether that changes the answer is Billy's call, not mine.

---

### R3. The IDEA Conference may be the wrong kind entirely — **OPEN**

**The decision.** Whether a conference belongs in the obligation set at all, given `time_point` is out of slice 1.

**Verbatim:**

> `schema.md` §7 names `time_point`'s three fixture instances as *"an exam sitting, a review session and **a conference**"* - and says the type is out of slice 1 because its reader, the calendar projection, is.
>
> If that conference is this conference, giving it an obligation row is a category error rather than a modelling choice. It was kept as an obligation only because that is the only row-bearing kind available and it carries a stated grade consequence.

**Confirmed at source.** `records/spec/schema.md` §7's `time_point` row reads verbatim: *"**Not in slice 1.** The type is real - an exam sitting, a review session and a conference are three fixture instances ... Its reader is the **calendar projection**, which is itself out of slice 1; the type is out because the projection is, not because nothing reads it."*

**What turns on it.** The obligation count of 14 and, with it, `architecture.md`'s acceptance criterion. `REPORT.md` names this openly: *"Whether the two bonus items belong in the obligation set at all. They were included; the count of 14 is a result of that judgment, not of a target."* Its counter-argument, also verbatim from `REPORT.md`, is `schema.md` §3's own justification for `optional`: *"Without it a plan ranks a +1% survey among required work purely by date"*.

**What has moved since 2026-08-28.** Billy 2026-08-30 ruling 3 restates §7's ground exactly: *"`time_point` is out because its reader, the calendar projection, is out."* That confirms there is no alternative kind to move the conference to in v1, which narrows R3 to a binary: keep the row as an obligation, or drop it. It does not choose.

---

### R4. `course.prereq`'s graveyard justification is falsified by the source — **the row's REASON is open; the field is settled**

**The decision.** Whether the graveyard row's recorded ground is corrected, and separately, where the outline's course-level facts go.

**Verbatim:**

> "Prerequisite(s): SFWRENG 2DM3" (course outline, p.1)
>
> `schema.md` §7 does not carry `prereq` because it is *"null for both courses in the fixture"*. It is not null here. The conclusion may still stand on other grounds; the stated ground does not.
>
> Same paragraph, same problem: `course` has four fields and **zero** free text by rule, so the outline's instructor, term boundaries, units, antirequisites and required textbook can only reach the system as annotations. The term boundaries are load-bearing - the last-day-of-classes rule depends on them.

**Confirmed at source, and the record is standing wrong today.** `records/spec/schema.md` §7, line 174, verbatim and uncorrected: *"`course.offering_term` · `course.prereq` | Not carried: null for both courses in the fixture, and `offering_term`'s justification is another domain's need, in a domain that does not exist"*. The 2c03 outline states a prerequisite, so *"null for both courses in the fixture"* is false as the ground for `prereq`. `schema.md` §2 confirms the second half: four fields, and *"Four fields beyond the discriminator, and no free text."* `REPORT.md` F12 lists the casualties, including *"Course Dates: 01/05/2026 - 04/07/2026" (which F7's last-day rule depends on)*.

**What has moved since 2026-08-30.** Billy ruling 1: *"`course.offering_term` and `course.prereq` stay graveyarded for v1. The cross-domain requirement is deferred to v2, not dead."* So the field does not return. **The open question is narrower and still open: the row's recorded reason is false, and a later reader will inherit it.** Note that `domain-design.md` §0.6 is the strongest statement in the corpus of why prerequisite structure matters (*"the academic domain must hold course offering-terms and prerequisite structure, since that graph gates other domains' decisions"*), and it is not marked against §7's graveyard in either direction.

**Second half, unaddressed by any ruling I can see:** the term boundaries have no home. `model.md` §10 item 9 keeps the late-day budget open, and the last-day rule depends on `Course Dates`, which `course` cannot hold.

---

### R5. The final exam's date: derived, or null — **APPARENTLY SETTLED, but the settlement is outside my boundary**

**The decision, verbatim:**

> outline: "EXAM PERIOD (Final Exam)" - no date
> exam paper: "April 2026 Final Exams" - no date
> announcement, Apr 16 2026 7:59 AM: "See you in the exam today!"
>
> The extraction stored `2026-04-16`, derived from that announcement, and labelled it derived. `schema.md` §7 rules the other way by name: *"coarse dates (April 2026, the Final Exam) ... a date that is not fixed is null. The term's largest obligation therefore stores a null `due`."*
>
> Both readings are defensible. Reverting is a one-field CRUD, and the reasoning is already on a note.

**Confirmed at source.** `schema.md` §7's coarse-dates row is verbatim as quoted.

**Evidence that it was settled the null way.** `measure.py`'s own docstring names *"the Final Exam's non-null `due` (B25)"* as a pre-ruling artifact, and excludes *"the provenance note B25 removed"*. `corpus-counts.txt` (2026-08-28) prints `due null: ['Final Exam']` while `records.json` still stores `"due": "2026-04-16"`. The two disagree because `corpus-counts.txt` and `render-candidates.py` read `app/tests/fixtures/2c03.json` and `measure.py` reads `records.json`. **`records.json` was never synced** (`NOTES.md` §4). I did not open the fixture or `backlog.md` B25, so "settled" here rests on `measure.py`'s and `NOTES.md`'s reports, not on the ruling itself.

**What did land, and it is bigger than R5.** `records/spec/write-rules.md` §1.1, *"An inferred value is asked about, not annotated"*, was written from exactly this case and quotes Billy's `records.json` `_note` verbatim. See "Rulings with no home" below for why one half of that note may not have made it.

---

## Verification of the four reported findings

### 1. The withdrawal of every note-length measurement — **CONFIRMED, and the damage is wider than reported**

`2026-08-29-course-level/NOTES.md` §6, verbatim:

> **Billy, 2026-08-29, after §4 was written and committed:** `records.json` cannot justify anything about real data, and length least of all. The note bodies are **a subagent's own compressions, produced from the schema's field definitions with no write rule to follow** - `write-rules.md` did not exist when the extraction ran.

And its second ground:

> **Second contamination, found on checking:** `write-rules.md`'s changelog says its four rules were authored by Billy **as hand edits to this same file**. So the file is agent output partly overwritten by Billy, and nothing in it says which body is which. The lengths are mixed-provenance as well as unruled.

I verified the second ground independently: `records/spec/write-rules.md` changelog, last entry, verbatim: *"2026-08-28 - created. Four rules authored by Billy as hand edits to `evidence/2026-08-28-corpus/2c03/records.json`, plus two owed."* And `records.json` visibly carries those hand edits as `_note` strings in Billy's own voice (*"I put `optional` = false because those assignments are clearly not optional"*).

The consequence for the banner, verbatim from §6:

> **It reaches a truth record.** `model.md` §10.5's 2026-08-28 changelog entry - *"§10.5's premise real samples are short is falsified by the corpus"*, standing `agent - measured` - rests on exactly these numbers. An unruled agent writing longer than `write-rules.md` §4.2's worked example does not falsify *real samples are short*; it reports that the agent had no rule. **Correcting that entry is now a deliverable of this cycle, not a side note.**

**The banner's current state, checked directly. It stands uncorrected in THREE places, not one.**

1. `records/domain/model.md` §10 item 5, body, lines 643-647: *"**MEASURED 2026-08-28, and it corrects this item's own premise.** *Real samples are short* is false. The 11 notes of the 2c03 corpus run **87 to 278 characters**, against the **~90** that `spec/write-rules.md` §4.2's worked compression produces, and rendering the course level puts **871 characters** of course-scoped notes ahead of its first obligation row."
2. `records/domain/model.md` changelog, line 701, the same claim restated, standing *"agent - measured"*.
3. **Not reported by anyone: `records/spec/ring-0.md` §7, line 88** rests on the same voided numbers. Verbatim: *"Measured on the corpus, both readings are uncomfortable: all 11 notes in one call is **1,881 characters**, while the 4 course-scoped ones alone are **871** plus a table ring 0 already holds resident."* The arithmetic is 871 + 1,010 = 1,881, i.e. exactly `measurements.txt`'s two totals. That sentence is the stated ground for ring-0.md §7's refusal to establish that the course level is worth a call.

So the ledger is: **two truth records, three passages, all standing uncorrected as of 2026-08-30.**

### 2. "Ring 0 governs residency, not readability", landed in `63612df` — **CONFIRMED in substance, with two caveats**

`NOTES.md` §2 round 4, verbatim: *"`obligation.parts` is homeless - agent | **rejected by Billy.** ring 0 governs **residency**, not readability; `parts` returns with any read of the record. Landed as `63612df`"*.

**Where the records now say it.** `records/spec/ring-0.md` §4's field table, `parts` row, as rewritten by `63612df`: *"**Excluded from the projection is not unreadable:** it is an ordinary field of the obligation and comes back with any read of that record - which level renders it is the presentation cycle's question"*. Also `records/spec/schema.md` §4.6, rewritten in the same commit: *"read as complete, it makes `obligation.parts` look homeless when the field is simply returned by whatever reads the obligation."*

**Caveat A, attribution.** `NOTES.md` says Billy rejected it. All three changelog entries the commit added say **`agent - measured`**, not `Billy - ruled` (`schema.md` line 217, `write-rules.md` line 169, and the `backlog.md` entry visible in the commit diff). A ruling of Billy's is recorded in the records at agent standing.

**Caveat B, dates.** The commit is dated `Sat Aug 29 14:38:33 2026`; every changelog entry it adds is dated `2026-08-28`. The records' internal dates are one day behind the commits for this whole run.

**Caveat C, the phrase.** The words *"residency, not readability"* appear nowhere in `records/`. The ruling they compress is `domain-design.md` §9.2's 2026-08-23 Billy ruling, which `NOTES.md` §3 quotes and which I confirmed verbatim: *"**Ring 0 returns to being the layer that is RESIDENT, not the definition of what is observable.**"*

### 3. `look_at(course)` is a coordinator call; §9.3 restricts materials — **CONFIRMED**

`NOTES.md` §2 round 3, verbatim: *"the coordinator is not a caller, so the two-reader split dissolves - agent, from `domain-design.md` §9.3 | **rejected by Billy.** `look_at(course)` is a call and the coordinator must be able to see what a course is, or plan generation is blind"*. And §3: *"`§9.3`'s *"no corpus retrieval, no file reads, no fact writes"* is a purity restriction on **materials**. It was read as a complete enumeration of the coordinator's reads."*

**The clause, checked directly.** `records/domain/domain-design.md` §9.3, verbatim: *"**Derived tool surface for the coordinator:** read the fact projection · write plans · dispatch. No corpus retrieval, no file reads, no fact writes (all facts arrive through ingestion)."* The three prohibited items are all **material** access. The same section's table gives *"**plan generation** | **coordinator** | everything - its only substantive work, because it *is* coordination"*. The reported reading holds: the list restricts what materials reach the coordinator; it does not enumerate its reads, and it does not make the coordinator a non-caller.

**And the record already said so.** `records/domain/model.md` §7.1 is titled **"The coordinator's material verb — `look_at(node_id, question)`"** and marks the walk row ✅ for the coordinator against search ❌. So Billy's correction restored what a truth record already carried; the agent argued against a record it had not opened. **No record was edited to carry the correction**, and nothing in `records/` warns a future reader that §9.3's list is not exhaustive.

### 4. "The corpus is evidence about what the material contains, not about what a record should look like" — **CONFIRMED verbatim, and it has no home**

`NOTES.md` §6, verbatim: *"**The line this draws:** the corpus is evidence about **what the material contains**. It is not evidence about **what a record should look like**. Everything in §4's character columns is the second kind."*

The file states the partition explicitly as a table:

| survives | does not |
|---|---|
| which obligations exist, their `due`, `grade_share`, `optional` - transcription from the real outline | every character count: 871 / 1,010 / 459 |
| which policies the course states (12 late days, two marking schemes, the snow-day credit) | how many notes those policies became, and how long each is |
| that 4 hang on the course and 7 on obligations - a placement fact | `parts`' wording and length on every row |

**Its scope, precisely.** It voids *length* arguments and *how many notes a policy became*. It explicitly preserves the placement fact 4-on-course / 7-on-obligations, which is what `ring-0.md` §7 and §4 and `architecture.md` §4 line 59 rely on for counts. So the reported summary "voids every length argument drawn from `records.json`" is accurate and does not over-reach.

**Nothing in `records/` states this rule.** `grep` for `871`, `1881`, `87-278`, `459`, `1,010` across `records/domain` and `records/spec` returns only the three uncorrected passages above.

**Destination proposal — `docs/adr/`.** Title: *Corpus measurements bound what the material contains, never what a record should look like.* All three tests hold: it is hard to reverse (it retires the only real dataset as a source of shape arguments, and re-adopting it means re-running the extraction under write rules); it is surprising without context (the corpus is the project's only real data, and three record passages already lean on it); it is a real trade-off (the alternative was to keep the numbers, which is circular, since it canonises an unruled agent's output as the target). One-to-three sentences: *Measurements taken over `evidence/2026-08-28-corpus/2c03/records.json` are admissible for what the source material states and where a fact hangs, and inadmissible for how long a record should be or how many records a statement becomes. The bodies measured are an unruled subagent's compressions, partly overwritten by Billy's hand edits, and `write-rules.md` did not exist when the extraction ran. A length bound is therefore issued down from affordability, not read up from samples.*

---

## Rulings with no home

Every item here is checked against `records/domain/` and `records/spec/` and against `git log`; `records/plan/` was outside my boundary and is named where it might be the home.

### N1. **[RULING]** Billy, 2026-08-28, in `records.json`: `obligation.name` should follow a system-owned convention, designed at the presentation layer

`records.json`, obligations `_note` (c), verbatim:

> "the `name` should follows a system-owned convention, not be inherited from the source that provides it. The 'convention' should be designed when doing the presentation layer"

**The record says the opposite.** `records/spec/write-rules.md` §3.1, titled *"`name` - store what the material prints"*: *"**There is no system-owned naming convention, and one is not owed.** Write the label the source uses."* Its changelog entry is attributed **`Billy - ruled`**, same date, 2026-08-28, and grounds the dissolution on the id no longer being minted from the name.

**The two are not about the same thing, and that is the problem.** The dissolution's ground is *addressing load*: the id is now opaque, so the name need not make a good locator. Billy's `_note` is about *presentation*: what the reader is shown. `evidence/2026-08-28-ring-0/NOTES.md` records the dissolution as one of "three things that dissolved rather than being answered" and gives the same addressing ground: *"**B15 / write-rules §3.1**, `obligation.name`'s convention. Owed only because the id was minted from the name; with an assigned id the name carries no addressing load."* Neither artifact mentions the presentation half of Billy's note.

**And the record contradicts itself on it.** `write-rules.md` §3's field table, line 58, still reads **``name`` | §3.1 - **OWED****, while §3.1's own heading and body say a convention *"is not owed"*. One of those two lines is wrong today.

**Destination proposal — deferral.** Precondition that wakes it: the presentation cycle producing `records/spec/course-level.md` or any presentation record, which is where Billy's note put the convention. Carry the quote with it. Also, whichever way it goes, `write-rules.md` §3's table line and §3.1's body must be made to agree; that is a defect, not a decision.

### N2. **[RULING]** Billy, 2026-08-28, in `records.json`: an inferred date is asked about, and the obligation's field is changed, not annotated

`records.json`, the Final Exam provenance note's `_note`, verbatim:

> "Bad example for production. When the annoucement about an actual date & time come, the final agent should change the time for that obligation, not to attach a note saying that a time is inferred. Even if the time if inffered, the agent should ask the user for clarification"

**Half landed.** `records/spec/write-rules.md` §1.1 carries the ask-the-user rule and quotes the middle sentence. **The last clause is the one to check:** *"Even if the time is inferred, the agent should ask the user for clarification."* §1.1 does state *"When a source does not state a value and the agent infers one, it **asks the user**"*, so this one is **homed**, and I record it only because it is the direct upstream of Billy 2026-08-30 rulings 2 and 4 (*"asks when needed"*, and *"proactivity is written too rigidly now and will bite"*). §1.1 as written is unconditional and has no frequency governor; ruling 4 says the rigidity will bite. **Destination proposal — deferral**, precondition: ruling 2's ask-frequency acceptance item, *"measurable only after the system is roughly built"*.

### N3. **[RULING]** Billy, 2026-08-28, in `records.json`: a note's body carries the summary, not the source paragraph

`records.json`, notes `_note`, verbatim: *"the agent who write this seems to be citing the original paragraph, but the system should carries the summary, do that the body is concise, because every `notes` are rendered within a Node, so long paragraphs is a disaster to read. The rules is the body should be concise and short enough but self contained"*. **Homed** at `write-rules.md` §4.2, near-verbatim. No action.

### N4. **[RULING]** Billy, 2026-08-28, in `records.json`: the render test for whether a note is worth writing

`records.json`, the late-day note's `_note`, verbatim: *"A note is somthing that is rendered together with the Node it is attached to, so the rule for deciding something is worth a note is really: 'Is it worth being written done so that everytime I look_at this Node, the note comes together'"*. **Homed** at `write-rules.md` §4.0. No action.

### N5. **[RULING]** Billy, 2026-08-29: the length bound is issued down from affordability, not read up from samples

`2026-08-29-course-level/NOTES.md` §6, verbatim:

> **What it does to item B.** The bound is no longer read **up from samples** - that is circular in the way Billy named, since it would canonise an unruled agent's output. It is issued **down from affordability**, which is what `schema.md` §4 already says: *"The primary lever is the prompt that writes the note, not a truncation."* Its two inputs are both outside `records.json`: what the coordinator can pull for five courses at once, and whether the **real** policy statements survive that budget - a check against `~/Documents/McMaster/2c03`, the source, not the extraction.

**Checked.** `records/spec/schema.md` §4 does say *"The primary lever is the prompt that writes the note, not a truncation"* and §9 item 3 keeps the bound owed. **But `model.md` §10.5's banner says the opposite direction is settled** (*"The bound's input is what a rendered level can carry, so it is owed out of the presentation cycle"* is compatible; *"the 11 notes ... run 87 to 278 characters"* as its evidence is not). No record states that the sample route is closed. **Destination proposal — folded into the ADR at finding 4** rather than carried separately; the direction-of-derivation is the same ruling seen from the other end.

### N6. **[RULING]** Billy, 2026-08-28: `look_at(course)` is a call the coordinator makes, and §9.3's list is not an enumeration of its reads

Quoted in full under finding 3. **`model.md` §7.1 already carries the positive half.** What has no home is the negative half: that `domain-design.md` §9.3's *"no corpus retrieval, no file reads, no fact writes"* is a materials restriction and has now twice been read as a complete enumeration. `NOTES.md` §3 records that an agent *"argued for two rounds with a ruling it had not read"*. **Destination proposal — not carried as an ADR** (it is a clarification of an existing record, not a decision with a trade-off). The right form is a one-line scope marker inside `domain-design.md` §9.3 saying what question that list answers, exactly as `NOTES.md` §3's guard prescribes. That is an edit to an existing record and I am not proposing it as a new artifact.

### N7. **[RULING]** Billy, 2026-08-28, on the table shape and the ordinal handle

`render-candidates.txt` header, verbatim:

> * the table shape itself - a fixed column width forces per-row truncation, and truncation is asymmetry introduced by the renderer, which `domain-design.md` 9.2 rules out
> * variant C's ordinal handle - unsafe for writes

Corroborated by `NOTES.md` (ring 0): *"the one-row-per-item table was rejected outright: a fixed column width forces per-row truncation, and truncation is asymmetry introduced by the renderer, which `domain-design.md` §9.2 rules out."*

**No record carries either.** `grep truncation` across `records/domain` and `records/spec` returns only `schema.md` §4's *"the primary lever is the prompt that writes the note, not a truncation"*, which is a different claim about a different thing. There is no presentation record for it to live in.

**Destination proposal — `docs/adr/`.** Title: *Renderer-introduced truncation is asymmetry, so a fixed-width table is not the course level's shape.* Hard to reverse: a table is the obvious first shape and rejecting it removes the default. Surprising without context: the ground is not readability, it is `§9.2`'s symmetry rule applied to the renderer rather than to the observer. A real trade-off: the table was rendered over real data first and rejected on what it showed, and the alternative shape does not exist yet. If instead this is judged too close to a not-yet-written presentation record, the fallback is **deferral**, precondition: the presentation record gaining a shape.

### N8. **[OBSERVATION with a ruling attached]** The student's own file contradicts the outline on the late-day budget

`REPORT.md`, "Read by accident, disclosed", verbatim:

> listing the assignments directory printed `assignments/README.md` to the terminal. It is the student's own file and states **"You have 8 late days total across all assignments"**, which **contradicts the outline's 12**. It was not used as a source for any value.

**No record carries this instance.** `model.md` §10 item 9 keeps the late-day budget open as a *conditional-rule* problem (*"12 late days, at most 3 per assignment"*), not as a *conflicting-sources* problem.

**Why it matters now.** It is a concrete, dated, primary-source instance of exactly the class Billy 2026-08-30 ruling 7 governs: *"Two conflicting statements must never coexist in the system. Shallow conflicts the agent may resolve itself but must report afterwards; deeper ones it must ask about before resolving."* And ruling 5 says *"the risk is repeated asking about small conflicts ... wait until it bites."* This is the first recorded thing that bit.

**Destination proposal — deferral**, carrying the quote and both sources. Precondition that wakes it: ruling 5's *"wait until it bites"*, i.e. the first time an agent has to choose between 8 and 12 in a live run. Also relevant: `REPORT.md` F14 records a *second* two-source disagreement on the same corpus (*"The portal prints '11:59 PM'; the outline prints 'up to 11:59:59 pm that day'"*), resolved by preferring the portal. Two instances, one of them silently resolved by the extraction with no rule behind the preference.

### N9. **[OBSERVATION]** Findings from `REPORT.md` that no graveyard row covers

`schema.md` §7 covers F5 (per-part scores), F9 (release dates), F11 (portal state), and F1 partly (`count`). **Four do not appear in any record I read:**

- **F3, no location field.** *"Three obligations state a venue; all three pushed onto notes."* Quotes: `"Test 1, Feb 6 (10%), LRW B1007"`, `"WHERE: MSU Hub Loft (4th Floor)"`.
- **F4, no duration or end time.** *"'Examination Duration: 150 minutes' · '10:30 to 11:20' · '5:00 - 9:00 PM'. `due` stores only the left edge."*
- **F7, MSAF weight transfer between obligations.** *"'the weight of that exam will be moved to the final exam'. A conditional re-allocation from one obligation to another; slice 1 has one link kind, `about`, signature `annotation -> any Ref`, so an obligation-to-obligation relation cannot be expressed at all."*
- **F10, deliverable structure.** *"`parts[]` carries no status and no score, so which artifact is owed for which part has no representation."*

**Destination proposal — not carried, except F7.** F3, F4 and F10 are consequences of the field set that a note absorbs, and Billy 2026-08-30 ruling 1 (v1 is coursework inside academics) does not reach them. F7 is different in kind: it names a **structural** limit, that slice 1 has no obligation-to-obligation link, and `model.md` §10 item 9 already keeps the late-day half of the same MSAF policy open without naming the link limit. **Deferral for F7**, precondition: the first mechanism that needs to move weight from one obligation to another, which is the allocation planner.

---

## Voids, corrections and withdrawals

Each entry gives both sides and says whether the record still stands uncorrected.

### V1. Billy 2026-08-29 voids the note-length measurements. **THREE PASSAGES STAND UNCORRECTED.**

Both sides quoted in full under finding 1. Standing wrong today: `model.md` §10 item 5 body, `model.md` changelog line 701, `ring-0.md` §7 line 88. Billy named the first a deliverable of the 08-29 cycle; the cycle's own commits (`7ffeaf9`, `9e6aa84`, `9d4298a`) touch only `evidence/`, and `git diff main -- records/` is empty.

### V2. `63612df` withdraws `schema.md` §4.6's return shape. **Landed.**

Before: *"`look_at` returns `{ summary, annotations[], edges[] }`"*. After: *"**It does not state the return shape, and the `{ summary, annotations[], edges[] }` it used to quote was not one.**"* The record now says the shape is stated **nowhere**, which the commit message calls *"correct but not free"*. `model.md` §7.1 line 356 and `design.md` line 167 still print the triple; §4.6's new text explains why the triple was never a contract, but neither of the other two carries a marker. **Partial: the withdrawal landed in the owning record, and two other records still print the withdrawn shape without a note.** `design.md` line 167 is at least scoped by its own §3.4 re-homing banner; `model.md` §7.1 line 356 is not.

### V3. `0194827` withdraws *"the complement is a reason the course level exists"*. **Landed.**

`NOTES.md` §2 round 2 records it; `ring-0.md` §7's closing paragraph now says verbatim: *"**What this record does NOT establish, and must not be read as establishing: that the course level is worth a call.** *Ring 0's complement* says what would be in it, which is a **negative definition** and not a justification."* Landed. **But the same paragraph's supporting arithmetic is V1's casualty** (1,881 / 871), so a correction landed on top of an instrument that was voided the next day.

### V4. `ring-0.md`'s own 2026-08-28 changelog corrects §4's counts. **Landed.**

Verbatim: *"the counts were **6 of 14 carrying an annotation, 8 without** - not 5 and 9, and not *two rows in three*."* `NOTES.md` §5 warns explicitly: *"**The counts in `ring-0.md` §4 were wrong once already** (5/9, corrected to 6/14). Re-measure rather than re-cite."* `measurements.txt` independently reproduces `obligations carrying one   6 of 14`. Landed and reproduced. Under `NOTES.md` §6 this is a **placement** fact and survives the void.

### V5. `NOTES.md` (ring 0) withdraws the render-candidates' two premises the day they were rendered. **Landed in the evidence, correctly, with a banner.**

`render-candidates.txt` lines 1-26 carry a stop-banner: *"REJECTED THE SAME DAY IT WAS RENDERED. Read this before reading anything below."* and *"It is a record of what was seen. It is not a design, and nothing should be built from it."* `render-candidates.py`'s docstring says the same. This is the one place in my material where a void was applied to the artifact itself at the moment it happened. No record action needed.

### V6. **[OBSERVATION]** `write-rules.md` §3.4 and §4.0 both count Billy's own `_note` annotations as data.

`write-rules.md` §3.4: *"Effect on one real course: 50 candidate strings became 28."* Counting `records.json`'s `parts` arrays gives 1+1+3+2+4+1+2+2+3+4+4+1+0+0 = **28**, and the `1` on the Final Exam row is Billy's instruction string `"_note: this should carry the general concepts the exam carries, like 'Graph', 'Trees', etc"`. `measure.py` excludes it by name (*"B27: the Final Exam's only `parts` entry is Billy's instruction, not data"*), which gives **27**.

`write-rules.md` §4.0: *"Measured on one course: 20 candidate notes became 12."* `records.json`'s `notes` array has **12** elements, of which one is a `_note` pseudo-record and not a note. `corpus-counts.txt` prints `notes: 11` and `measurements.txt` prints 4 + 7 = 11.

So both counted figures in a truth record are one high, by the same mechanism, in the same file. The candidate side is shakier still: `LABELING.md` L1's candidate table enumerates **54** strings, not 50, by my count of its twelve rows (36 across A1-A9, 12 across the two midterms, 6 on the Final). I cannot reconstruct where 50 comes from.

**Record still stands uncorrected.** Note that under V1 the *note* count in §4.0 is in the "does not survive" column anyway (*"how many notes those policies became"*), but the `parts` count in §3.4 is not obviously covered by that void, and it is the number the rule's effect is stated in.

### V7. **[OBSERVATION, outside my directories]** Billy 2026-08-30 ruling 6 supersedes `model.md`'s linearization axis.

Ruling 6: *"the determinant is the **nature of the RAG store** ... This replaces both the source-class rule and the linearization axis."* `records/domain/model.md` lines 608-610 state: *"The real axis is **whether meaning survives linearization** — a property of the materialization pass, not of the file."* I saw this only because I was checking §10.5 in the same file. It is not from my evidence directories, and it is another agent's or Billy's to place; I record it so it is not lost. **Standing uncorrected.**

---

## Records standing wrong today

Ordered by how badly a reader is misled.

| # | record and location | what it asserts | why it is wrong | who voided it |
|---|---|---|---|---|
| 1 | `records/domain/model.md` §10 item 5, body (lines 643-647) | a `MEASURED 2026-08-28` banner falsifying *real samples are short*, on 87-278 / ~90 / 871 characters | the bodies are an unruled subagent's compressions partly overwritten by Billy, written before `write-rules.md` existed | Billy, 2026-08-29, `2026-08-29-course-level/NOTES.md` §6 |
| 2 | `records/domain/model.md` changelog, line 701 | the same claim, standing `agent - measured` | same | same |
| 3 | `records/spec/ring-0.md` §7, line 88 | *"all 11 notes in one call is **1,881 characters**, while the 4 course-scoped ones alone are **871**"*, as the ground for refusing to establish the course level's worth | 871 + 1,010 = 1,881 is exactly `measurements.txt`'s voided totals | same. **Not reported by any earlier survey.** |
| 4 | `records/spec/schema.md` §7, line 174 | `course.prereq` is not carried because it is *"null for both courses in the fixture"* | the 2c03 outline states `"Prerequisite(s): SFWRENG 2DM3"` | `RULINGS-NEEDED.md` R4, 2026-08-28. Billy's 08-30 ruling 1 keeps the field out, so only the reason is wrong |
| 5 | `records/spec/write-rules.md` §3 field table, line 58 | ``name`` is `§3.1 - **OWED**` | §3.1's own body says *"one is not owed"* | internal contradiction inside one record, both written 2026-08-28 |
| 6 | `records/spec/write-rules.md` §3.4 and §4.0 | *"50 candidate strings became 28"* and *"20 candidate notes became 12"* | 28 and 12 each count one of Billy's `_note` annotations as data; 27 and 11 are what the corpus holds. 50 does not reconcile with `LABELING.md` L1's 54 | arithmetic over `records.json`, `corpus-counts.txt` and `measurements.txt` |
| 7 | `records/spec/schema.md` §4.6 vs `records/domain/model.md` §7.1 line 356 | §4.6 says the return shape is stated nowhere; §7.1 still prints `look_at(node_id, question) -> { summary, sticky_notes[], edges: [...] }` | the triple was withdrawn in `63612df` as never having been a contract | `63612df`, partially applied |
| 8 | three changelog entries added by `63612df` (`schema.md` 217, `write-rules.md` 169, `backlog.md`) | standing `agent - measured` | `NOTES.md` §2 rounds 3 and 4 record both as **rejected by Billy** | attribution gap; the substance is right, the standing is understated |

Item 3 is the one to act on first: it is a *different* record from the two everyone has been pointing at, and its sentence is load-bearing for the course-level cycle that is currently open on this branch.

---

## Abandoned steps

Recorded so nobody mistakes one for a ruling. Each is **[ABANDONED]**.

1. **The `<course>-slug(name)` handle**, `2c03-assignment-1` and the thirteen like it, printed across `corpus-counts.txt`, `render-candidates.py` and all three variants in `render-candidates.txt`. Retired the same day by `schema.md` §1.1. The file says so itself.
2. **The one-row-per-item table**, variants A, B and C. Rejected outright the day they were rendered. See N7 for the *reason*, which is a ruling and does survive.
3. **Variant C's ordinal handle** (`#` 1-14). *"unsafe for writes."*
4. **The `share` column in every variant.** *"`grade_share` is excluded from ring 0"* (`ring-0.md` §6).
5. **"`obligation.parts` is homeless"** (`NOTES.md` §2 round 3, agent). Rejected by Billy. It is the *error* that produced ruling N/finding 2, not a position.
6. **"the coordinator is not a caller, so the two-reader split dissolves"** (`NOTES.md` §2 round 3, agent). Rejected by Billy.
7. **"the course level is ring 0's complement, and that is why it exists"** (`NOTES.md` §2 round 1). Replaced: a negative definition is not a justification.
8. **`seam` as the 08-29 cycle's axis.** *"The axis was declared and then replaced once, deliberately: `seam` ... → `reader × affordability`. Under `seam` the two-reader term is invisible."*
9. **The three dissolutions of 2026-08-28** (`NOTES.md`, ring 0): B20 (the composed summary's broken inputs), B15 / write-rules §3.1 (`obligation.name`'s convention), B21 (a freed id re-minted). *"Three items closed by removing the question. None was closed by answering it."* B15's dissolution is contested by N1 above; the other two are clean and are already in `backlog.md`'s changelog.
10. **The four agent corrections of the ring-0 sitting** (`NOTES.md` §"Corrections the agent took"): treating a null result as a refutation; reifying *two obligations carry the same concept* into *they point at the same concept node*; manufacturing a distinction with no consequence in use; hardening three illustrations into contracts. These are method, not domain. **Destination — not carried.** The one with the widest reach is the fourth, *"an artifact hands over its vocabulary along with its content"*, and its 08-29 successor, *"before treating any list as exhaustive, state what question it was written to answer"* (`NOTES.md` §3). Neither is a claim about the semester, so neither is CONTEXT.md or ADR material; if they belong anywhere it is a working-practice document, and I am not proposing one.

---

## Measurements and their standing

| measurement | source | value | standing today |
|---|---|---|---|
| obligations in the 2c03 corpus | `corpus-counts.txt`, `measurements.txt` | **14** | **STANDS.** Transcription from the real outline. Load-bearing for `architecture.md` §4 line 59's acceptance criterion. Contingent on R3 (whether the two bonus rows belong at all) |
| notes | `corpus-counts.txt`, `measurements.txt` | **11** | **STANDS as a count of what the file holds.** `write-rules.md` §4.0's "12" is one high (V6) |
| notes hanging on the course vs on obligations | `measurements.txt` | **4 / 7** | **STANDS.** Explicitly preserved by `NOTES.md` §6 as *"a placement fact"*. This is what corrected `ring-0.md` §4's old 5/9 |
| obligations carrying at least one annotation | `corpus-counts.txt`, `measurements.txt` | **6 of 14** | **STANDS.** The stated motivation for `has-more` (`ring-0.md` §4) |
| progress records | `corpus-counts.txt` | **0** | **STANDS**, and it is why `ring-0.md`'s `state` column is *"untestable on this corpus"* |
| `grade_share` sum over all rows | `corpus-counts.txt` | **97** | **STANDS.** Arithmetic over stored values. The ground for `ring-0.md` §6 and for R2 |
| rows named `Assignment N` | `corpus-counts.txt` | **9** | **STANDS**, but under a name convention the ring-0 sitting then dissolved |
| course-scoped note bodies | `measurements.txt` | 4 notes, `[241, 215, 265, 150]`, **871** chars | **VOID.** Billy 2026-08-29 |
| obligation-scoped note bodies | `measurements.txt` | 7 notes, `[105, 127, 126, 91, 278, 87, 196]`, **1,010** chars | **VOID.** Same |
| `parts` inline over all rows | `measurements.txt` | **459** chars, max 119, empty on 3 | **VOID.** *"`parts`' wording and length on every row"* is named in the does-not-survive column |
| the derived total in `ring-0.md` §7 | `ring-0.md` line 88 | **1,881** | **VOID**, and standing in a truth record. 871 + 1,010 |
| note bodies run 87-278 against §4.2's ~90 | `model.md` §10.5 | — | **VOID**, and standing in a truth record, twice |
| id lengths under the retired scheme | `corpus-counts.txt` lines 14-28 | 14-22 chars | **MOOT.** The scheme is retired (`schema.md` §1.1) |
| `records.json` vs the fixture on the Final Exam's `due` | `corpus-counts.txt` says `due null: ['Final Exam']`; `records.json` stores `2026-04-16` | — | **BOTH ARE REAL.** They are two different files. `NOTES.md` §4: *"`records.json` is the PRE-RULING extraction and was never synced."* I did not open the fixture; this reconciliation is `measure.py`'s, not mine |
| the `1259 − 249 = 1010` reconciliation | `NOTES.md` §4 | — | Arithmetic **checks**, and the exclusion is named in `measure.py` line 27. It reconciles a **void** figure, so it inherits the void |

**Two measurement-instrument warnings the 08-29 sitting leaves, both worth carrying:**

> **`ring-0.md` §2's routing test is agent-drafted and unmeasured**, and §2 says so.

> **§9.2's own gate** - *an observation earns its place iff a judgment demonstrably changes when it is present* - is marked in §9.2 as **agent formulation, not separately ruled**, and the one run of it returned nothing from an instrument that could not have detected the effect.

I verified the second against `domain-design.md` §9.2, which does mark the gate *"agent formulation, obtained by lifting the rigidity rule one level, **not separately ruled**"*. **Destination — not carried**; both are already stated in the records they warn about.

---

## Coverage

**Read in full and accounted for:** all 12 files listed in the header. Nothing sampled, nothing skimmed.

**Not on disk:** `evidence/2026-08-29-course-level/NOTES-plain.md`, committed in `9d4298a`, deleted in the working tree. Not chased, per instruction. If it says anything §4-§6 does not, this survey misses it.

**Not opened, and where that limits me:**

- `records/plan/backlog.md`. B19, B25, B27, B28, B29 are load-bearing for R5's apparent settlement and for `write-rules.md` §3.4's empty-Final-Exam cost. I saw B19, B20, B23, B24, B28 and B29 only as they appear inside `git show 63612df`. **B25 and B27 I have never seen**; every statement about them here is `measure.py`'s or `NOTES.md`'s report.
- `app/tests/fixtures/2c03.json`, which `render-candidates.py` and therefore `corpus-counts.txt` actually read. The fixture-vs-`records.json` divergence is inferred, not verified.
- Every other `evidence/` directory, `records/findings/`, `records/archive/`, openclaw, `~/Documents/McMaster/2c03`.

**Claims I could not verify and have marked as such:** R1's assertion that 2da4 has five labs and 2px3 weekly worksheets; the two midterm rows violating `write-rules.md` §3.4's canonicalisation (`Tree ADT, tree traversal`) in the *fixture* as opposed to `records.json`, where I did confirm them; `write-rules.md` §3.4's "50 candidate strings"; and whether `NOTES-plain.md` added anything.

**Where I contradict an earlier survey, I win on date** for the three sittings above only. The three findings other agents reported and I confirmed are confirmed at source, not relayed. The one I add is `ring-0.md` §7's 1,881 / 871.

**Created nothing.** No `CONTEXT.md`, no ADR, no issue, no edit to any record. Every destination proposal above is a proposal.
