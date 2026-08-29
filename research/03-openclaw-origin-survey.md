# Origin survey - openclaw `fall26/` step-minus-1 and derivation (2026-08-22)

**What this is.** An inventory of the origin ideas in the two oldest work batches of the fall26 design effort, and of the questions they were reaching for. It feeds a wayfinder map. It is **not** a summary of conclusions, and nothing here should be read as a ruling.

**Why the split matters.** This is the oldest material in the effort. It holds the origin ideas, which is why it is in scope; it is also the least credible as conclusion, because later sessions (which I did not read and cannot see) revised and in places reversed it. Every item below is therefore tagged:

- **INTENT** - a want, a problem statement, a rejection of an alternative, a question being reached for.
- **CONCLUSION** - a decision or ruling *this session reached on this date*. Carries a heavy comparison burden against later material. Never read as "what is true".

**What I read, in full:**

- `openclaw:fall26/2026-08-22-step-minus-1/` - `TASK.md` (125 lines), `FINDINGS.md` (289), `p4-segmentation/TASK.md` (75), `p5-induction/TASK.md` (86), `p6-channel-or-knowledge/TASK.md` (72). **647 lines.**
- `openclaw:fall26/2026-08-22-derivation/` - `BRIEF.md` (72), `TASK.md` (140), `FINDINGS.md` (324), `agents/` ×5 (1,051), `per-course/{2c03,2aa4}/{inventory,counts}.md` (711), `apparatus/README.md` (29). **2,327 lines.**
- `openclaw:fall26/README.md` and `openclaw:fall26/MOVED.md`, for orientation only.

**Boundary observed.** I read nothing else. Specifically not read: `2026-08-23-slice-1/`, `2026-08-24-slice-1-write/`, `2026-08-23-cost-probe/`, `2026-08-22-modeling/` (including `MODEL.md` and `PLAN.md`, which the derivation scores against and cites constantly), `devlog/ideas/2026-08-21-fall26-domain-design.md`, `docs/superpowers/specs/2026-08-21-fall26-build-spec.md`, anything else in `openclaw/`, and the whole of `~/Documents/Projects/fall26/`. Non-markdown artifacts inside the two in-scope directories (`.json`, `.py`, `.txt`) were listed but not read; the markdown accounts for them.

**Attribution convention used below.** `[Billy]` = explicitly attributed to the human in the source, by name, a `[R]` ruling marker, or "per Billy". `[main-session agent]` = the prose of `TASK.md` / `BRIEF.md` / `FINDINGS.md` / `per-course/*`, which is agent-drafted coordination writing, not the human speaking. `[A1]`…`[B2]` = one of the five derivation subagents' own reports. `[unclear]` where I cannot tell. **The overwhelming majority of these 2,974 lines is agent prose.** I count roughly eleven passages in the whole corpus that are explicitly the human's own words or rulings; they are listed in full under *Origin intent*.

---

## Origin intent

### The thing being built, as stated here

**INTENT** - *`derivation/BRIEF.md` §"What is being built"* `[main-session agent]`. The clearest single statement of purpose in the corpus, and it is agent-written, not quoted from Billy:

> "A model of a university course as a **layered graph**, so that a personal knowledge-base system can hold the whole picture across five concurrent courses."

Three node kinds are given there: **obligation** (a thing with a deadline), **concept** (a thing the student understands or does not), **artifact** (a thing that exists on disk and is opened independently).

**INTENT** - *`derivation/BRIEF.md` §"What is being built"* `[main-session agent]`. The motivating dissatisfaction, stated as the point of the graph:

> "a lecture PDF and a tutorial PDF exist and are used independently, yet both describe one concept - which a folder tree cannot express."

**The folder tree is the rejected alternative.** It is rejected in that sentence, and independently vindicated three times by the material: `project 01` is shared by A1 and A2 in 2c03, so any tree must file it under one and lie about the other (*`agents/2c03-obligations-and-edges.md` J9*, `[A3]`); the midterm's material lives in a Week-5 deck *and* a Week-4 handout (*`agents/2c03-concepts-weeks-1-6.md` §"One thing MODEL gets right"*, `[A1]`); T5/X5/N5 are three files, one question set, three independent uses (same section, `[A1]`).

### The goal function, as this corpus reports it secondhand

**INTENT** - the purpose is repeatedly named as **anxiety removal** and **allocation planning**, but always by citation to a design doc outside my scope, never quoted from Billy here:

- *`agents/2c03-obligations-and-edges.md` J1* `[A3]`: "'what should I be studying' is exactly the anxiety this is built to remove" - cited to design §2's goal function.
- *`agents/2aa4-tutorials-assignments-artifacts.md` §edges, `spec` conflation* `[B2]`: "the single most obviously-wanted query in a KB whose stated purpose is anxiety removal".
- *`agents/2c03-obligations-and-edges.md` J5, J7* `[A3]`: "surface details Billy does not know to ask about" and "the allocation planner - the thing design §10.7 ruling 4 names as the product".

**I cannot verify any of these against their source.** They read as faithful citation, but the design doc is out of scope. Treat as *reported intent*, not confirmed intent.

### What a semester actually looks like to him

Assembled from scattered observation, mostly agent-recorded rather than Billy-stated:

**INTENT / material fact** - *`step-minus-1/TASK.md` §Fixture* `[main-session agent]`: four real 2025-26 courses at `~/Documents/McMaster/` - `2aa4`, `2c03`, `2px3`, `2da4`. "Each is a git repo Billy maintains by hand, **with no consistent naming convention across courses**."

**INTENT / material fact** - the courses are structurally unalike, and the corpus names the axis: `woven` (2px3 - the weekly-announcement-pointing-outward shape) vs `flat`. *`step-minus-1/p5-induction/TASK.md` §Input* `[main-session agent]`: 2px3 is "the `woven` profile … **the hardest case routing must survive.** A `flat` course would validate less per unit of effort."

**Material fact** - *`derivation/TASK.md` §Courses*: **2aa4 has no announcements at all** (verified on disk 2026-08-22). 2c03 has a full 55-item announcement timeline. 2px3 has 39. So the delivery channel a course exposes varies from "the central mechanism" to "structurally absent".

**Material fact** - *`derivation/per-course/2aa4/inventory.md` §lecture set* `[B1 via main-session agent]`: 2aa4 has **zero "Week N" markers in 687 KB of lecture text** and no announcement stream, so it has no time signal at all except PDF creation dates.

**Material fact - how Billy actually works, recorded as evidence:**

- He **copy-pastes announcements out of the Avenue portal** into a flat `.txt` with no format, no delimiters, no markup. *`step-minus-1/p4-segmentation/TASK.md` §Input.*
- He **commits course material in retroactive bulk** - 2c03's four most recent commits all land 2026-04-12 carrying weeks 4-13, so git dates record tidying, not arrival. *`step-minus-1/TASK.md` §P3.*
- He keeps a **hand-maintained Notion table** of 2px3's obligations, "kept for a year", which has **no workload column** and **does** have a `target_date`. *`derivation/TASK.md` §Courses; `derivation/FINDINGS.md` §3.*
- He **renames folders mid-semester as naming a concept becomes necessary**: 2c03's `resources/week-01..03` carry no topic suffix, `week-04-stack-queue-list` … `week-12-MST` do. *`derivation/TASK.md` §3; `derivation/FINDINGS.md` §5.*
- He **writes concept edges by hand, in ink, unprompted**: TUT7 p3 carries "This question tests: ① MAD compression ② linear probing insertion ③ probe counting" over an exercise, in a form with no text layer. *`agents/2c03-concepts-weeks-7-13.md` J11* `[A2]`.
- He **writes a hand-made end-state synthesis**: `2AA4-Final-Exam-Study-Guide.md`, whose opening paragraph records the professor's expected UML style contradicting what he did on the midterm. *`derivation/TASK.md` §3.*
- His own artifacts carry his MacID (`wu897`) in the filename; his reports are dated **7-13 days ahead of each due date**. *`step-minus-1/FINDINGS.md` §P2 sub-question 2; `per-course/2c03/inventory.md` §"Billy's own submissions".*

### The eleven passages that are explicitly the human's

This is the complete set of Billy-attributed statements in 2,974 lines. Everything else is agent draft.

1. **INTENT** - *`step-minus-1/TASK.md` §P3; repeated `step-minus-1/FINDINGS.md` §P3.* The build spec had retired the "announcement streams may be inaccessible" risk on 2026-08-21. "**Billy's own look on 2026-08-22 was that the picture is not clear**, particularly without direct portal access for an agent." The risk is un-retired on his say-so. *This is the human overruling an agent's own risk retirement.*

2. **INTENT** - *`step-minus-1/TASK.md` §P3.* "Scope for a first pass: **1-2 courses, per Billy 2026-08-22** - enough to see the real shape before committing effort to four." *A deliberate scoping-down.*

3. **INTENT** - *`step-minus-1/p4-segmentation/TASK.md` §Input.* "Announcement structure, **per Billy 2026-08-22**": `<title line>` / `<date line>` / `<body…>`, with the date line as the reliable anchor and the title as the line immediately above it. *His model of the export's shape. P4 then found it holds only two-thirds of the time.*

4. **Artifact** - *`step-minus-1/p4-segmentation/TASK.md` §"The candidate anchor".* **Billy's own regex**, tested verbatim: `^(Jan|Feb|Mar|Apr|May|Sep|Oct|Nov|Dec) [1-9]?[0-9], 202(5|6) [1-9]?[0-9]:[1-9]?[0-9] (A|P)M$`. *The only literal artifact of his in the corpus. It matched 19 of 39.*

5. **INTENT (deferral)** - *`step-minus-1/p5-induction/TASK.md` §Reduction targets.* Whether `ephemeral` is a fourth route or a disguised `insert` on `progress` is "**Billy's to rule**", so every `ephemeral` instance is listed individually with full text "so the ruling is made on real instances rather than on this one hypothetical". *A stated discipline: the human rules on instances, not on hypotheticals.*

6. **INTENT** - *`derivation/TASK.md` §H2.* "**Reframed by Billy, 2026-08-22**, before any extraction ran." An earlier H2 gated on total N + E against a fixed token budget. He ruled that wrong: "disclosure is progressive by design philosophy, only ring 0 is resident, and nothing requires a CLI fetch to render the whole graph. **The gate moves from *total size* to *expansion cost*.**"

7. **INTENT** - *`derivation/TASK.md` §2 anti-cheat rule 3.* "**Folder structure is not taxonomy.** Billy's folders are admissible **only** as evidence of the organization *he reaches for under pressure*, and must be tagged as such - never cited as the course's structure. (**Billy, 2026-08-22**.)" *He warned against his own folders being trusted. The agent then argued back - see Internal contradictions §C4.*

8. **CONCLUSION** - *`derivation/FINDINGS.md` §2.* "**[R]** Billy, 2026-08-22: a concept appearing in two places is **the truth of the data, not a rendering bug**. The model may not cut edges to force a tree. How rendering handles it is a CLI/UX decision, deferred."

9. **CONCLUSION** - *`derivation/FINDINGS.md` §5.* "**[R]** Billy, 2026-08-22: **the modelling layer is stateless.** It does not record what he has learned, understands, or does not; it presents the concepts and leaves judgment to him." Adopted consequences (agent-drafted from the ruling): the concept definition is rewritten from "a thing Billy understands or does not" to "**a unit of subject matter the course teaches, independently addressable**"; **system-inferred mastery is forbidden**; Billy-stated progress remains a ring-0 row and never a property of a concept node; the surviving set-difference queries are **structural** ("this concept has no artifact covering it") and never **personal** ("you never opened X").

10. **CONCLUSION** - *`derivation/FINDINGS.md` §5.* "**[R]** Billy, 2026-08-22: an artifact does **not** need a URL or a `present` flag - the resources exist on the portal, and knowing what a name refers to is sufficient; **he does not want everything stored locally**." Consequence adopted: "absence is not a field, it is the absence of store content" (a JOIN). `external_ref` and `present` both dropped. *This directly overrides an agent proposal - see §C1.*

11. **INTENT (standing discipline)** - *`step-minus-1/p5-induction/TASK.md` §"Explicit non-goals".* Findings are "surfaced for Billy to rule, per the repo's standing discipline that **agents draft and never self-lock**". Echoed by `derivation/BRIEF.md` rule 5 ("**BLOCKED beats guessing** … A blocked agent that asks a sharp question is worth more than a finished one that assumed") and rule 6 ("**You may judge the model** … A finding that overturns the model is the most valuable thing you can return").

### The questions these sessions were reaching for

**INTENT - step -1 (`step-minus-1/TASK.md`, `p4/p5/p6 TASK.md`).** Six propositions, each pre-registered before any file content was opened:

- **P1** - can the managed Supabase instance host pgvector, so the corpus layer needs no second store?
- **P2** - do section titles and slide headings extract reliably enough that `course > week > file > section` grouping costs zero manual annotation?
- **P3** - is the historical announcement stream reachable at all, and what is the *minimum usable export*?
- **P4** - can the announcement stream be segmented mechanically?
- **P5** - *"What would this announcement require the system to do?"* - does every operation reduce to insert / rewrite / file over the five fact types?
- **P6** - *"Are announcements a delivery channel, or a body of knowledge?"* Decided per announcement by: *"Would anyone ever retrieve this announcement by its content?"*

**INTENT - derivation (`derivation/TASK.md` §1).** Four hypotheses:

- **H1 (unification)** - is course type per-layer *density* rather than *structure*? Falsified if either course needs a node kind or edge kind the other does not.
- **H2 (graph shape)** - what does one expansion cost? Is there an unbounded hub that kills progressive disclosure?
- **H3 (concept layer)** - from only what the real system would hold at ingest, can a usable concept partition be induced?
- **H4 (edge survival)** - which of eight candidate edges survive a bar of ≥3 real instances **and** a nameable query? "Expected to lose members; a table where all eight survive should be treated as a symptom of over-modelling, not a success."

**INTENT - two open design holes carried in from outside, named as D1 and D2** (*`step-minus-1/p5-induction/TASK.md` §Measurements*):

- **D1** - where a fact stops applying, is it superseded **at write** by a newer statement, or does it simply expire and need filtering **at read**? Noted as an existing contradiction: "the design doc says write-time and both summaries say read-time".
- **D2** - what happens when classification or target resolution fails? "The largest open design hole and currently has no rule at all."

---

## Concrete things

### 1. Vector store / pgvector

- **CONCLUSION** `[main-session agent]` - *`step-minus-1/FINDINGS.md` §P1.* **PASS.** pgvector 0.8.0 on PostgreSQL 17.6; extension installed, cosine-distance query returned correct ordering, **HNSW index built**. The Week 1 fallback (local vector store with application-layer joins) is not needed.
- **INTENT** `[main-session agent]` - *`step-minus-1/TASK.md` §P1.* Why it was probed at all: the spec rated it `low` severity, "which is a rating of *likelihood*, not of blast radius", and grep over the repo returned zero references to pgvector anywhere. **The intent is the anti-hype discipline, not the answer.**
- **CONCLUSION (incidental)** `[main-session agent]` - *`step-minus-1/FINDINGS.md` §P1.* `OPENCLAW_DB_DSN` lives only in the deployed runtime env, not the source repo's `.env`; the two are not interchangeable.

### 2. Structural extraction from PDFs (free section labels)

- **INTENT** `[main-session agent]` - *`step-minus-1/TASK.md` §P2.* The want: `course > week > file > section` grouping at **zero manual annotation cost**. The stated stake: if it fails, grouped retrieval degrades to course-wide and week-wide search with no section labels.
- **INTENT (pre-registered failure preference)** `[main-session agent]` - same section. "A **silent wrong** label is worse than no label, because it mislabels a group." PASS required both ≥80% hit rate *and* a visible failure mode.
- **CONCLUSION** `[main-session agent]` - *`step-minus-1/FINDINGS.md` §P2.* Slide-shaped: 39/40 (~97%). Prose-shaped: 12/26 (~46%). Explicitly self-limited: "**97% is real, but it is 97% of a single template**" - the lexicographic sampling rule spent all three slide-shaped slots on one course (`2px3`), one professor's deck.
- **CONCLUSION** `[main-session agent]` - same section. The honest verdict is **not** "prose extraction fails" but "**the cheap method fails on prose**". "First non-empty line" discards font size and position, which is where a heading lives in prose. Week 2 chooses: pay for font-aware extraction, or let prose live without section labels.
- **CONCLUSION** `[main-session agent]` - same section. The named silent-wrong instance: `2aa4/assignments/assignment-01/Assignment 1.pdf` returns `"Course code: SFWRENG 2AA4"` for **all six pages** - "Non-empty, confident, plausible, wrong."
- **Not run** - a second stratum was pre-registered ("from each of `2aa4`, `2c03`, `2da4`, take the first 4 PDFs from any subdirectory whose name contains `lecture`, `slide`, `tutorial` or `week`") and *never ran*. **This reads unfinished.**
- **Later revision inside this set** - the derivation's title-scoped extraction of 2aa4 (`apparatus/titles2aa4/`, 31 files) is a de-facto second stratum on a different professor's deck, and it did work. Nobody in the corpus connects the two.

### 3. Non-PDF corpus and image-only material

- **INTENT** `[main-session agent]` - *`step-minus-1/TASK.md` §P2 sub-question 1.* Raised by the fixture survey and **not in the spec**: `2px3` holds 11 `.docx`, 2 `.pptx`, 1 `.xlsx` against only 9 `.pdf`. "Both the design and the spec discuss the corpus as if it were PDFs throughout."
- **CONCLUSION** `[main-session agent]` - *`step-minus-1/FINDINGS.md` §P2 sub-question 1.* "**C4's corpus path has a scope gap** that belongs in Week 2's plan rather than in Week 2's surprises." `pdftotext` covers none of the Office formats.
- **CONCLUSION** `[main-session agent]` - *`step-minus-1/FINDINGS.md` §P2 "Image-only PDFs".* Four `2da4` files return **zero extractable text across 27 pages**. "Neither the design doc nor the build spec contemplates material with no text layer." The requirement created is **detection, not OCR**: "a silent empty index entry is not deferrable, because it makes the corpus lie about its own coverage."
- **Revision inside this set** - *`step-minus-1/FINDINGS.md` §P6, collateral findings.* 2c03's tutorial notes are handwritten scans at ~23 extractable characters per page, "making image-only material a whole class in a core course **rather than the edge case P2 reported it as**."
- **Independently reproduced by two derivation agents.** `[A1]` *`agents/2c03-concepts-weeks-1-6.md` §nodes*: `TUT5Notes.pdf` / `TUT6 Notes.pdf` have no text layer; a pipeline routing by extension "will file them as `materialized_doc`, run `pdftotext`, get four page-footers, and produce a **confidently empty chunk set**". `[B2]` *`agents/2aa4-tutorials-assignments-artifacts.md` J1*: same, plus three more shapes.

### 4. External material vs Billy's own work

- **INTENT** `[main-session agent]` - *`step-minus-1/TASK.md` §P2 sub-question 2.* Design §4 rests on "all dangerous inputs are external", "which presumes the two are distinguishable" while they sit in one directory.
- **CONCLUSION** `[main-session agent]` - *`step-minus-1/FINDINGS.md` §P2 sub-question 2.* They separate "cleanly, **by accident**": Billy's artifacts carry his MacID. "Not universal - `Reflection 1 Draft.docx` carries no marker - so it is a good default, **not a rule**." Scoped: "The inbox model makes this moot for live use; it matters for replaying historical material."

### 5. The announcement stream - existence and export

- **INTENT** `[main-session agent]` - *`step-minus-1/TASK.md` §P3.* The deliverable was deliberately **not** an export: "that needs Billy and his portal session. What this probe produces is the **specification of the minimum usable export**, so that the manual effort is spent once and correctly."
- **CONCLUSION (established by sweep)** `[main-session agent]` - same section, repeated in FINDINGS. A filename search for `announc*` / `notice*` / `avenue*` across four courses returns one unrelated hit. "**No announcement content exists locally in any form.**"
- **CONCLUSION (hypothesis killed, recorded so it is not re-proposed)** `[main-session agent]` - same. Git history is **not** a chronology proxy. "Filenames and directory names (`week-01`, `Lecture 8`, `Report 1`) carry the ordering instead, and they carry it as **sequence without dates**."
- **CONCLUSION (the minimum export spec)** `[main-session agent]` - *`step-minus-1/FINDINGS.md` §P3.* Required: publication timestamp, body text, title/subject, course. Droppable: author, attachments, read-state. First-pass scope: **one course, `2px3`**, because it is `woven` and the hardest case.
- **INTENT (the hole, stated at launch rather than papered over)** `[main-session agent]` - same. If the stream is unrecoverable, the fallback validates the corpus path, manifest and schema, but what stays unvalidated is "**announcement routing - the whole insert-vs-rewrite fact path, the design's central mechanism.** That is a large hole and must be stated at launch."

### 6. Announcement segmentation (P4)

- **CONCLUSION** `[main-session agent]` - *`step-minus-1/FINDINGS.md` §P4.* **DEGRADE.** The stream holds 39 announcements. Billy's regex verbatim: 19 (49%). Corrected minutes + months + `\s*$`: 26 (67%). Plus dateless heads: 39 (100%).
- **CONCLUSION (two stacked defects)** - (1) the minutes defect, predicted, cost 7 of 26 dated announcements because "announcements get posted on the hour"; (2) **dateless heads, unpredicted, 13 of 39 (33%)** - a line that is non-empty but strips to empty occupies the date slot.
- **INTENT (the method that earned its keep)** `[main-session agent]` - *`step-minus-1/p4-segmentation/TASK.md` §Protocol step 2.* The deliberately loose independent scan was "what detects failure modes nobody predicted, rather than only the ones already listed". FINDINGS: "**This is the check earning its keep.**"
- **CONCLUSION (a requirement relaxed)** `[main-session agent]` - *`step-minus-1/FINDINGS.md` §P4.* P3 made the publication timestamp a hard requirement; a third of the export has none. "**But what design §4 needs is *ordering*, not absolute time.**" The requirement relaxes from "every announcement carries a timestamp" to "**the export preserves order**". Framed as "a sharpening of the requirement rather than a concession". See §C7.
- **Still unverified, stated as such** - whether 2c03 and 2da4 carry the same dateless-head artifact. **Reads unfinished.**
- **INTENT (the reporting constraint, and why)** `[main-session agent]` - *`step-minus-1/p4-segmentation/TASK.md` §"Reporting constraint".* P4 was forbidden to characterize what the announcements were *about*, because P5's rubric was being pre-registered concurrently and "must be written without knowledge of the content it will be applied to - otherwise the rubric is fitted to the data and the induction proves nothing."

### 7. The operations model - insert / rewrite / file (P5)

- **INTENT** `[main-session agent]` - *`step-minus-1/p5-induction/TASK.md` §"The question".* The framing question: "**What would this announcement require the system to do?** Answer in the announcement's own terms first, without reference to the schema. Only then force the answer into the reduction. Reversing that order fits the data to the schema, which is the failure this whole step exists to avoid."
- **INTENT** `[main-session agent]` - same, §Reduction targets. `rewrite` requires confirmation, "and the confirmation must present the **resolved target**, not a yes/no". `insert` and `file` are automatic.
- **CONCLUSION** `[main-session agent]` - *`step-minus-1/FINDINGS.md` §P5.* **The operations model is FALSIFIED.** 53 of 137 operations reduce (39%); 76 do not (55%). Ambiguity was resolved against the proposition, so this is a conservative lower bound.
- **CONCLUSION** - same. Supporting numbers: "**The deadline move happened once in a semester**, in the hardest course"; 21 of 22 executed rewrites were additive free-text appends; "**~30 confirmations/semester is not a real number**"; **D1 settled: read-time expiry beats write-time supersession ~7:1**; **D2: §4 anticipated one of three failure modes** - the others are *value unavailable* and *applicability unknown*. Residue concentrates: 42 of 76 in three classes (enrolment identity 17, pointer to unheld material 15, week-number to date 10).
- **CONCLUSION** - same. `woven` confirmed for 2px3 "with a refinement: the weekly spine is a quarter of the stream and is nearly pure insert-plus-pointer. **Every rewrite lives in the ad-hoc remainder.**"

### 8. Announcements - channel or knowledge (P6)

- **INTENT** `[main-session agent]` - *`step-minus-1/p6-channel-or-knowledge/TASK.md`.* Explicitly a **change of question** after P5's falsification: "narrower and cheaper to answer". The proposition: announcements are a delivery channel for facts, not a body of knowledge; if it holds, they are extracted and retained only as provenance - "never chunked, never embedded, never entering the retrieval corpus."
- **INTENT (anti-cheat with a stated direction)** - same, §Anti-cheat. "**Ambiguity resolves toward `knowledge`.** That is the direction that makes more work and denies the convenient conclusion. Excluding announcements removes an entire pipeline from the build, so the bias runs against the answer that saves effort."
- **INTENT (the alternative it refused to foreclose)** - same, §"Why this is not a foregone conclusion". "**If that is what these two courses show, the conclusion is not 'exclude announcements' but 'it depends on the course profile'** - which is a different and more expensive design."
- **CONCLUSION** `[main-session agent]` - *`step-minus-1/FINDINGS.md` §P6.* **FALSIFIED in both** courses. 2c03: 7/55 knowledge (13%), 5/55 net of redundancy (9%). 2da4: 7/38 (18%), 6/38 net (16%).
- **CONCLUSION** - same. "Both courses' knowledge converged on one thing: **it is almost always a correction against material the system already holds**, which is why extraction cannot hold it. **An amendment to a document is not a fact.**"
- **CONCLUSION** - same. "**The redundancy defence is dead, verified on disk in both courses.**" Named instances: `Tutorial_RiscFreeIDE.pdf` is still the pre-correction version locally; `lab01.pdf` names the superseded Quartus version; the locally held Week 7 deck is the blank-whiteboard variant in which the corrected complexity table does not exist at all.
- **CONCLUSION** - same. "**The bulk is redundant, the seam is not** - 40-51% overall, but 1 of 7 and 2 of 7 among knowledge instances."

### 9. Node kinds - the three-layer model

- **INTENT** `[main-session agent]` - *`derivation/BRIEF.md`.* obligation / concept / artifact, with within-layer hierarchy edges (`part-of`, `supersedes`, `builds-on`) and many-to-many cross-layer edges (`covers`, `requires`, `spec`).
- **CONCLUSION (H1)** `[main-session agent]` - *`derivation/FINDINGS.md` §1 H1.* "**Not falsified, on a thinner base than claimed.**" No node kind or edge kind appeared that one course needed and the other did not; 2aa4 needs strictly *fewer* than 2c03.
- **CONCLUSION (the base thinned)** `[B2]` J3, adopted by FINDINGS §1 - MODEL §3's density table "was wrong about 2aa4, and it is the row the hypothesis was calibrated on". §3 called 2aa4's obligation layer dense, ~16 nodes; B2 grepped all nine tutorial documents for deadline/submit/marks/graded/due/weight and got **zero hits**. The real layer is **7 nodes, sparse**. "**2aa4 is topic-dense / obligation-sparse - the same shape as 2c03.**" The wrong row was written from folder appearances - "**precisely the 'folders are not taxonomy' error the derivation was built to avoid, committed inside the model itself.**"
- **CONCLUSION (consequence)** - same. "The 'two axes with overlap' exemplar is gone. **H1 now rests on two courses of the same shape, plus 2px3, which this run excluded.**" Named as one of two gaps the run leaves.
- **CONCLUSION** `[B1]` - *`agents/2aa4-lecture-concepts.md` J5.* `announcement → node` in 2aa4 is "**structurally impossible**, not merely sparse". Under H1's own rule that is density zero and does not falsify, "but zero is qualitatively different from sparse: a per-course renderer must not assume the edge exists, or queries written against it return empty rather than degrading."
- **CONCLUSION** `[B2]` - *`agents/2aa4-tutorials-assignments-artifacts.md` J4.* "**A tutorial is an artifact, not an obligation, and not both.**" It has no deadline; no query in §6 reads it as one. "'Where should I be Wednesday at 2pm' is a calendar question the timetable answers."

### 10. The concept layer - tree vs DAG

- **CONCLUSION** `[B1]`, adopted `[main-session agent]` - *`agents/2aa4-lecture-concepts.md` §"It does not partition the concepts"*, adopted at *`derivation/FINDINGS.md` §2.* MODEL §2's "the tree survives inside a layer" is **false for the concept layer**. Instances: **Singleton** is `part-of` Creational patterns *and* `part-of` STUPID as the "S" anti-pattern - "two parents, opposite valence, the course deliberately teaches it twice"; **Liskov substitution** appears three times; **Observer** is behavioural, *is the mechanism of* MVC, and reappears in Façade; SOLID/GRASP/STUPID re-enter whole as sections of the Change lecture.
- **CONCLUSION** - same. "**The concept layer is a DAG. The artifact layer is the tree.**" The artifact layer partitions cleanly: 21 lectures into 5 groups, no document in two, none orphaned. "§2's rendering argument must be re-derived from the artifact layer."
- **CONCLUSION** `[main-session agent]` - *`derivation/FINDINGS.md` §2.* Treated as the general case, not a 2aa4 quirk: 2c03 has a visible candidate in `[A1]`'s report - "PQ-sort with a sorted list **is** an Insertion Sort" puts insertion sort under both sorting and priority queues. Caveat stated: "**B1 tested for multiple parents; A2 did not.**"
- **CONCLUSION** `[Billy]` - *`derivation/FINDINGS.md` §2.* See Origin intent item 8: two places is the truth of the data; the model may not cut edges to force a tree; rendering is deferred.

### 11. The concept layer - state, definition, and origin

- **CONCLUSION** `[Billy]` - *`derivation/FINDINGS.md` §5.* See Origin intent item 9. **The modelling layer is stateless.** The concept definition is de-stated. System-inferred mastery is forbidden. Cost stated plainly: surviving set-difference queries are structural, not personal.
- **INTENT (the question left open by that ruling)** `[B2]` - *`agents/2aa4-tutorials-assignments-artifacts.md` §"Open question for Billy".* Task-1's handwritten solution is "the densest single record of *what he actually understood* in the whole slice, and the model as frozen has no place to put it". B2 asks whether §10.7's exclusion of handwritten notes covers it, "and if it covers this, then the one signal that distinguishes 'Billy understands Chain of Responsibility' from 'Chain of Responsibility exists in this course' is being discarded by rule."
- **CONCLUSION** `[main-session agent]` - *`derivation/FINDINGS.md` §5.* B2's open question is answered: Billy's handwritten Task solutions are **artifacts**, not an understanding signal.
- **CONCLUSION (H3)** `[main-session agent]` - *`derivation/FINDINGS.md` §1 H3.* "**PASS on both courses, and both results are uninformative.**" Both agents who could judge it said so unprompted. `[A2]`: "*the partition is not induced, it is transcribed, and that is a weaker result than a pass.*" `[B1]`: `[Module N]` on 27 of 30 title slides plus a written two-level taxonomy on one closing slide. Verdict: "**Both courses state their own outline. Neither exercised induction. The question H3 was written to answer - can a multimodal pass find the partition when the course does not state it - remains UNTESTED.**" Named as the single largest gap this run leaves.
- **CONCLUSION** `[A1]` - *`agents/2c03-concepts-weeks-1-6.md` §H3.* A sharper reason 2c03 is the floor: "the affordance is **the instructor's uniform deck template**, not the discipline. A course whose decks lack a plan page loses the free coarse layer entirely."
- **CONCLUSION (a fourth origin)** `[A2]`, adopted - *`derivation/FINDINGS.md` §5.* "**[NEW] Billy authors them by hand, unprompted, mid-semester.**" The TUT7 ink edge and the mid-semester folder renames are the same behaviour in two modalities.
- **CONCLUSION (bulk authoring)** `[A2]`, adopted - same. "One clause in a tutorial handout creates 9 `requires` edges; one slide in a review deck creates 26. §10.2 assumed cross-layer edges are drawn item by item; **they are not.** Corollary: an edge is only as current as its sentence, and that sentence's document is dated 2025."

### 12. The hub question (H2) and progressive disclosure

- **INTENT** `[Billy]` - *`derivation/TASK.md` §H2.* The reframe from total size to expansion cost (Origin intent item 6). Measured quantities: degree distribution, hub detection, ring 0 size; N and E per layer are "context, not a gate".
- **CONCLUSION** `[main-session agent]` - *`derivation/FINDINGS.md` §1 H2.* "**The gate is invalid as posed.**" Three agents working blind to each other each showed the number is a function of a modelling choice not yet made: `[A1]` **edge conflation** (Big O is degree 3 as *subject-of*, ~15 as *requires-you-to-understand*); `[B2]` **concept granularity** ("Design patterns" degree ~16, cut one level down max ~4); `[B1]` **extraction scope** (`Interfaces` 16/21 full-text vs 2 title-scoped). "**H2 as written measured our own choices, not the material.**"
- **CONCLUSION** - same. Restated as a **W2 constraint, not a gate**: the extractor must be title-scoped (**mention ≠ coverage**), the concept layer cut at "one thing that can be separately asked about or separately taught", and `covers` split from the prerequisite relation.
- **CONCLUSION** - same. Measured distributions under those repairs: 2c03 W1-6 median 3 / p90 5; 2c03 W7-13 median 5 / p90 7; 2aa4 title-scoped **median 2 / p90 4 / max 10** (called the cleanest H2 measurement in the derivation, *`per-course/2aa4/counts.md`*).
- **CONCLUSION (one hub survives)** `[A2]`, adopted - same. `Week 13 Review Slides` covers **26 of 26** concepts; the textbook covers all and more. "Neither splitting the edge nor re-cutting the concepts helps, because a review deck's *subject* genuinely is everything." A2's reading adopted: their honest relation is "**indexes the whole course**", not 26 peer `covers` edges. **This hub is on the artifact side - a class MODEL did not model.**
- **Disagreement among agents, unreconciled** - see §C3.

### 13. Edges - what survived, what was cut, what was added (H4)

Bar: ≥3 real instances **and** a nameable query. *`derivation/FINDINGS.md` §1 H4* `[main-session agent]`, from the five agent reports.

**CONCLUSION - survived:**

| edge | evidence | note recorded |
|---|---|---|
| `artifact → concept` **covers** | ~150 (A2) / 118 (B1) | must split subject-of from prerequisite |
| `concept → concept` **part-of** | ~35 (A2) / ~30 (B1) | survives **as a DAG** |
| `obligation → concept` **requires** | 9 authored + ~12 induced (A3); Guide table authors 7 (B2) | **arrives in bulk from single sentences**, not pair by pair |
| `obligation → artifact` **spec** | ~45 (A3), 8 (B2) | needs a `role ∈ {given, owed}` discriminator |
| `sticky_note → node` | 7 (A3), 2 latent (A1), ≥4 in ink (A2), 5 (B2) | **targets straddle all three layers**, not only sections |
| `obligation → obligation` **builds-on** | 3 explicit (A3); stated *as a rule* in 2aa4's Guide (B2) | lives on the obligation side; A1/A2 found none in lecture material |

**CONCLUSION - cut:**

- `artifact → artifact` **supersedes** - "**CUT - 5 agents, 2 courses, zero instances.**" And "not merely unsupported; keeping it is actively harmful". Every real revision replaced the file at the same path under the same name, so there is no v1 on disk and D1's read-time expiry has no input. Three shapes would be mistyped and thereby **hide a live document** (`Tree Map UML` vs `BST Tree Map UML`; handout vs Sample Solutions; `.docx` vs `.pdf`). "`[B1]`'s **dating trap** is decisive": 2aa4's notes exports carry real lecture dates while every plain-slide export was produced in one batch on 2026-03-04, so "newest wins" **systematically discards the richer file**. Replace with a `revised_at` timestamp. **Corollary, from two courses: "the announcement stream is the only surviving record of supersession, because the filesystem destroys it."**
- `announcement → node` **mentions** - "**CUT - merged into `sticky_note.origin`**". Every high-value instance in A3's 55 announcements *is* a correction; the ~20 known-only items point at nothing. "**An announcement is therefore the origin field of a sticky note**, plus a flat provenance log."

**CONCLUSION - new edges the material demands:**

- `concept → concept` **requires** (prerequisite) - ≥7 in the course's own words `[A1]`. "**Adopt - MODEL §6's flagship query does not work without it.** §8 shipped only `obligation → concept`, so the 'transitive closure' terminated after one hop."
- `artifact → obligation` **prepares-for** - 8 (A1) + 5 (A2). "**Adopt - `obligation → spec → artifact` is the wrong direction and the wrong meaning.** A tutorial is not an assignment's spec."
- **edge payload `locator`** - A1: 25+ citations at section grain; A2: three independent forms (into a **method**, into a **page**, into a **question**). "**Adopt - nodes are typed and edges are bare pairs; the highest-frequency relation in the corpus cannot be stored without it.**"

**CONCLUSION - watch list, deliberately not adopted at one sighting each:** `contains` (A2, 9) · `projects` / is-a-view-of (A2, 6) · `sequence` (B1, 3) · `rendition-of` (B2, 1) · `produced` as a separate edge. *The instance counts on the first two exceed the stated ≥3 bar; see §C5.*

### 14. Ring 0 - the obligation layer

- **CONCLUSION** `[main-session agent]` - *`derivation/FINDINGS.md` §3.* "**Ring 0 is the layer the model got most wrong.** It was the layer MODEL.md was most confident about. Three agents broke it independently." What `due · status · target_date · workload` cannot hold:
  - **Tutorial participation, 10 of 12, worth 5%** (0.5% each, capped, with a snow-day credit changing the denominator) - "no `due`; status is a **count over twelve recurring events**". `[A1, A3]`
  - **12 late days, max 3 per assignment** - "a **course-level consumable resource that modulates every other obligation's effective deadline**. 'Can I be late on A5, and what does it cost me later?' has nowhere to live." `[A1]`
  - **Conditional grade weighting** - "10/10/30 **or** 0/0/50, whichever works out better for you" - "a rule, not a scalar. This is exactly the allocation planner's input." `[A1, A2, A3]`
  - **`status` is three orthogonal axes** - Completion / Score / **Evaluation Status**. A2 and A9 read "Feedback: Unread"; A2 was submitted in January at 100%. "`status: done` erases a live, months-old, actionable item." `[A3]`
  - **Obligations decompose into independently assessed parts** - A6: "if your cuckoo hashing doesn't work you can still get full marks for this report" (actual score 8/10). "`status` and `score` attach at the **part**, not the obligation." `[A3]`
  - **`weight` is absent from the schema entirely** `[A2, A3, B2]`
- **CONCLUSION** - same. "**`workload` is absent from every single obligation, in both courses, in every source.** No handout, portal cell, or announcement estimates effort. This is the second independent falsification of that field - Billy's own hand-maintained Notion table, kept for a year, also has no workload column and *does* have a `target_date` the schema lacks."
- **CONCLUSION (J8, categorical)** `[A3]` - same, and *`agents/2c03-obligations-and-edges.md` J8.* **Every one of the nine 2c03 handouts says, verbatim, "See Avenue for the due date."** "Ingesting all nine assignment PDFs with a full multimodal pass yields an obligation layer with **zero deadlines**. The portal screenshot is not an enrichment path for ring 0; it is **the primary one**, and the handouts are primary only for `requires` and `spec`. This upgrades design §10.7's screenshot ruling from a convenience to a dependency."
- **CONCLUSION (ring 0 is small)** `[A3]` - *`agents/2c03-obligations-and-edges.md` §nodes.* 15 rows for the whole course, three of them optional. A1 extrapolated ~15 independently. "The obligation layer is comfortably resident at this size."
- **INTENT (an unresolved tension raised, not settled)** `[A3]` J1 - the final exam skeleton states "25% Unit 1 · 35% Unit 2 · 40% Unit 3", which is simultaneously a `concept part-of concept` partition **and a weight field on concept nodes**. MODEL §7.1 hardens "allocation reads ring 0 only". A3: "the real allocation question for the largest obligation in the course is *'what do I study?'*, and its answer lives entirely in the concept layer … Either admit a uniform, typed, ring-0-shaped projection of the concept layer into allocation, or accept that study allocation is out of the system's scope." **`derivation/FINDINGS.md` does not record J1 anywhere. It reads dropped.**

### 15. Artifact backing and the "exists on disk" definition

- **CONCLUSION** `[B2]` J1, adopted `[main-session agent]` §4.1 - "**`backing` cannot be inferred from file type, and 'chunkable' is the wrong axis.**" Falsified four ways in one slice: scanned handwriting in a PDF wrapper; a text PDF whose exercises T1-T5 **are images** (backing is not uniform *within one file*); a `.png` containing a rendered prose block, more chunkable than several PDFs; one diagram held as both `.drawio` and `.png`.
- **CONCLUSION** - same. "**The real axis is whether meaning survives linearization** - a property of the materialization pass, not of the file. In `visitor.png` the labels linearize but **the edges are the content**." Adopted: `backing ∈ {materialized_doc, code_project}` plus a per-region **`text_extractable`** set by ingest, default false, true only when a pass actually recovered text. Its reading mechanism is the trust contract - distinguishing a **quotation** from a **generated description**.
- **CONCLUSION** `[B2]` J2 - "**`artifact` = 'a thing that exists on disk' is falsified.**" At least eight artifacts 2aa4 depends on are not on disk and never will be. B2 proposed `source_ref` admit URLs plus a `present` flag.
- **CONCLUSION** `[A3]` J7 - proposed a fourth backing, **`referenced_only`**, with ~13 instances in 2c03. "The extreme case: **Midterm 2 is a graded obligation with a released grade and literally zero artifacts on disk**." Named a corrected set-difference query: "obligations whose posted solutions I never downloaded", which "would have flagged all seven missing test-script zips and both midterm solution sets".
- **CONCLUSION** `[Billy]` - *`derivation/FINDINGS.md` §5.* **Both proposals overruled.** No URL, no `present` flag; "absence is not a field, it is the absence of store content" (a JOIN). See §C1 - A3's `referenced_only` need is not addressed by the JOIN framing.
- **CONCLUSION** `[B1]`, adopted §4.2 - "**One lecture, several files.**" 9 of 21 2aa4 lecture nodes back onto two files; the `~1` variant is a near-perfect subset (Jaccard 0.50-0.69) because the base is the **notes export** carrying speaker notes. In 2 of 11 pairs each side holds content the other lacks (**union required**). One pair is a **name collision, not a version** (Jaccard 0.21). Adopted as a **node property - a file list with a `variant` tag - not an edge**, because the query reads a list rather than a traversal. "**Filename similarity must never imply a relation.**"

### 16. Identity, naming and resolution

- **CONCLUSION** `[B2]` J5, adopted §4.3 - "**Resolution is semantic, everywhere, from three directions.**" Cross-references in 2aa4 are by informal alias and never by filename ("the Preliminary Tutorial document", "the refresher slides on Avenue"). Tutorial identity must be **topic-derived, never number-derived**: number in filename 5/9, `Structural.pptx` carries no number anywhere, header metadata 3/9 and **wrong in one**, while **topic appears on the title line 9 of 9**. *"The file knows what it is about; it does not reliably know when it happens."*
- **CONCLUSION** `[B1]` J3 - 2aa4 confirms the invariant "the graph has no time axis; time lives only in the obligation layer" *more strongly than the model claims*, "and simultaneously shows the invariant has a cost the model has not priced". B1 proposes: "**accept that the navigational handle is course-specific - week for 2c03, module for 2aa4 - and let the coarse grouping be the primary handle everywhere.**" **Not recorded in `derivation/FINDINGS.md`. Reads dropped.**
- **CONCLUSION** `[B1]` §nodes - proposes a **`lecture_date`** node field, "for 2aa4 the **only** ordering signal that exists", sourced from the notes-export `CreationDate` specifically. **Not in FINDINGS §6's adopted list. Reads dropped.**

### 17. Ingest ordering and cross-document decoding

- **CONCLUSION** `[A3, B2]`, adopted §4.4 - "**The governing artifact must be ingested before the ones it governs.**" `[A3]`: the course outline is the only artifact carrying grade weights, and without it 9 of 12 graded items have none - "the allocation planner runs blind". `[B2]` J8: assignment bodies carry a superscript marker attached to exactly the words a concept edge would want; it looked like ~20 authored edges and **reads nothing** - the Guide decodes it on page 5 as an intra-document pointer. "**Decoding required a different document.**"
- **CONCLUSION** `[B2]` J7, adopted §4.5 - "**Deadlines hide in prose inside governing documents.**" *"It is your duty to form teams by the end of Week 1"* appears in the Guide and nowhere else. "Governing documents cannot be treated as reference-only."
- **CONCLUSION** `[A3]` J6 - the `builds-on` edge is authored at both ends at different times, "and one end dangles". A8's handout says "You will need this code for assignment 9" while A9 does not yet exist as a node. "Ingest must be able to **write an edge whose target does not exist yet**, and must not create a duplicate when the other end arrives." **Not in FINDINGS §6. Reads dropped.**

### 18. Stale material and the redundancy defence

- **CONCLUSION** `[A2, A3]`, adopted §4.6 - "**Stale material circulates as current.**" 2c03's Week 7 Sample Solutions answer a **different question set** than the Week 7 handout - "the file answers a prior year's handout". The Week 8 tutorial and all eight UML PDFs are dated **2025**. Three uncorrected errors survive inside *current* 2c03 handouts, fixed by no announcement. "**'The corrected version is on the course site' fails for the third time.**"
- **CONCLUSION** `[main-session agent]` - *`step-minus-1/FINDINGS.md` §P6.* An announcement in 2c03 reproduces a stale copy-paste three weeks later, "which indexed announcement text would return as current".

### 19. Sticky notes

- **CONCLUSION** `[A3]` - *`agents/2c03-obligations-and-edges.md` §sticky_note.* Seven instances, "and their targets straddle all three layers". **Four of the seven attach to a concept or an obligation, not to a section**, against design §10.7's ruling that the note attaches to the section. "Refinement, not a contradiction … the highest-value ones (the Dijkstra note) attach to a concept precisely because they reconcile **two artifacts that disagree**."
- **CONCLUSION (a third origin nobody detects)** `[A1]` - *`agents/2c03-concepts-weeks-1-6.md` §"The sticky-note case I found is latent".* The two real contradictions in A1's slice (a deck and its handout disagreeing about which assignment a tutorial covers) **arrived with the original material**. "Nothing was delivered; the conflict is inert until someone reads both documents in the same sitting … This is a **third origin for a sticky note** beyond 'a correction arrives' and 'Billy states one' - *the corpus disagrees with itself* - and it is the one that most directly serves design §10.7 ruling 4 … It is also the one nothing in MODEL detects. I am not proposing a mechanism; I am recording that the class exists and is populated." **FINDINGS records the count ("2 latent (A1)") but not the class. Reads dropped.**
- **CONCLUSION** `[B2]` - two of its five sticky notes are "corrections the *author shipped inside the artifact*" (the JUnit 4/5 caveat; the conform-not-correspond footnote). "The sticky note is not only an inbound-correction mechanism."

### 20. Method and apparatus - the discipline itself

This is a concrete thing these sessions touch, deliberately, and it is arguably the most durable output.

- **INTENT** `[main-session agent]` - *`step-minus-1/TASK.md` §Anti-cheat rules*, and `fall26/README.md` §"Rules of the road": sampling rules written **before** any file content is opened; **ambiguous judgments resolve AGAINST the proposition**; verdict thresholds stated before the run and not adjusted afterwards; raw artifacts stay because "a conclusion whose evidence was deleted is not auditable".
- **INTENT** `[main-session agent]` - *`derivation/TASK.md` §preamble.* Why pre-registration matters more in the derivation than in step -1: "Step -1 was judged by data, this one is judged by Billy and the agent alone. §3's sealed ground truth is a *manufactured* adjudicator for H3, and arithmetic adjudicates H2. **H1 and H4 stay judgment calls** - that is stated up front rather than discovered afterwards."
- **INTENT** `[main-session agent]` - *`derivation/TASK.md` §2 rule 5, `BRIEF.md` rule 2.* "**A field or an edge is real only if you can name the query that reads it.** If you cannot name one, do not propose it. Over-modelling is this exercise's known failure mode: a complete-looking model is satisfying and mostly wrong."
- **INTENT** `[main-session agent]` - *`BRIEF.md` rule 1, `derivation/TASK.md` §2 rule 2.* "**No design vocabulary in the raw pass.** … Having the word 'concept node' available is enough to start hallucinating them."
- **CONCLUSION (the seal failed)** `[main-session agent]` - *`derivation/FINDINGS.md` §0*, corroborated *`apparatus/README.md` §"The seal leaked".* "**The seal leaked. The mechanism was mine and it was the wrong mechanism.**" Built from symlinks; `ls -la` prints symlink targets, "so the first command a shell-using agent naturally runs defeats it". Two agents hit it; both self-reported. `[A2]`'s contamination judged null. `[B2]` "saw the 2aa4 ground truth verbatim"; its induced concept **partition** is contaminated, its structural findings stand.
- **CONCLUSION** - same. `[B1]` established the leak could not have mattered for 2aa4: the grouping has three carriers and only one was sealed - folder name (sealed), **PDF `Title` metadata**, and **the rendered title slide** (`[Module N]` on 27 of 30). "**Carrier 3 is content** … so this grouping was never withholdable. **No re-run was ordered.**"
- **CONCLUSION** - same, and `apparatus/README.md`. "**Correct mechanism for any future blind run: copies, never symlinks, and strip document metadata.**"
- **INTENT** `[main-session agent]` - *`fall26/README.md`*, and `p4-segmentation/TASK.md` §"Reporting constraint". The subagent contract: "subagents swallow the process and emit only conclusions"; a `TASK.md` is written to be handed to a subagent verbatim.
- **INTENT (a preservation rule)** `[main-session agent]` - *`apparatus/README.md` §"What is deliberately NOT here".* "**Preserve what cannot be reconstructed, record the recipe for what can.**" B1's 732 KB full-text extraction is omitted because a recorded `pdftotext -layout` command regenerates it from sources not at risk; `SCORING-KEY.json` is preserved because "without this, which document an agent saw under which neutral name is unrecoverable".

---

## Vocabulary as coined here

Definitions are given **as stated in these sessions on 2026-08-22 to -24**, not as rulings.

| term | definition as stated | where | note |
|---|---|---|---|
| **obligation** | "a thing with a deadline (assignment, lab, midterm, presentation)" | `derivation/BRIEF.md` | |
| **concept** | "a thing the student understands or does not" → **rewritten within this set** to "a unit of subject matter the course teaches, independently addressable" | `BRIEF.md`; `derivation/FINDINGS.md` §5 `[Billy]` | **Meaning shifts.** The first presumes state; the ruling forbids it. |
| **artifact** | "a thing that exists on disk and is opened independently" | `BRIEF.md` | **Meaning shifts.** `[B2]` J2 falsifies "exists on disk" (≥8 named-not-held); `[Billy]` then rules absence is not a field. |
| **ring 0** | the always-resident tier; "the one genuinely always-resident thing"; MODEL §4 assigns it "how much is left" | `derivation/TASK.md` §H2; `agents/2c03-obligations-and-edges.md` J1 | measured at 15 rows for 2c03 |
| **progressive disclosure** | only ring 0 is resident; the rest is expanded on demand | `derivation/TASK.md` §H2 `[Billy]` | the reason total size stopped being the gate |
| **expansion cost** | the cost of expanding one node - the replacement gate for total N+E | `derivation/TASK.md` §H2 `[Billy]` | |
| **hub** | "a concept covered by dozens of artifacts, whose expansion is half a course"; "the only thing that can kill progressive disclosure" | `derivation/TASK.md` §H2 | **Meaning shifts.** `[A2]` J2 shows it is symmetric - `Week 13 Review Slides` is an *artifact* hub - and the model only modelled one side. |
| **mention vs coverage** | full-text matching finds *mention*; title-scoped matching finds *coverage* | `agents/2aa4-lecture-concepts.md` §caps | the distinction that dissolved a degree-16 node into degree 2 |
| **subject-of / requires-you-to-understand** | the two readings `covers` was silently carrying | `agents/2c03-concepts-weeks-1-6.md` §H2 | A1 proposed naming the second `applies`; not adopted under that name |
| **prepares-for** | `artifact → obligation`; a tutorial that preps an assignment | `agents/2c03-concepts-weeks-7-13.md` §edges | A1 called the same relation **material-for** - two names, one edge |
| **locator** | an edge payload naming a fragment: a section, a page, a method, a question | `derivation/FINDINGS.md` §1 | "nodes are typed and edges are bare pairs" |
| **variant** | a tag on a file in a lecture node's file list: `notes` \| `slides` | `derivation/FINDINGS.md` §4.2 | |
| **backing** | `{materialized_doc, code_project}` after `unchunkable_media` was dropped; `referenced_only` proposed and not adopted | `derivation/FINDINGS.md` §4.1; `agents/2c03-obligations-and-edges.md` J7 | **Meaning shifts** from a file-type property to an ingest-probed one |
| **text_extractable** | a per-region property set by ingest, "default false, true only when a pass actually recovered text" | `derivation/FINDINGS.md` §4.1 | |
| **meaning survives linearization** | the real axis replacing "chunkable vs not"; a property of the materialization pass, not the file | `agents/2aa4-tutorials-assignments-artifacts.md` J1 | |
| **sticky note** | a correction attached to a node; `sticky_note.origin` absorbs the announcement | `derivation/FINDINGS.md` §1 | **Meaning widens** within this set: targets straddle all three layers `[A3]`; a third origin is "the corpus disagrees with itself" `[A1]`; author-shipped in-artifact corrections count `[B2]` |
| **latent sticky note** | a conflict that arrived with the original material and is "inert until someone reads both documents in the same sitting" | `agents/2c03-concepts-weeks-1-6.md` | |
| **`woven` / `flat`** | course profiles; `woven` is "the weekly-announcement-pointing-outward shape" and "the hardest case routing must survive" | `step-minus-1/p5-induction/TASK.md` §Input | `woven` refined by P5: "the weekly spine is a quarter of the stream … **every rewrite lives in the ad-hoc remainder**" |
| **insert / rewrite / file** | the operation set: creates a fact / modifies a held fact (irreversible, confirmed) / large-or-static, only needs to be findable | `step-minus-1/p5-induction/TASK.md` | falsified as a complete set the same day |
| **ephemeral** | "leaves no durable fact at all" - explicitly *a candidate outcome, not a ruled one* | same | flagged as Billy's to rule |
| **does not reduce** | "none of the above fits - **this is the real output**" | same | 76 of 137 |
| **channel / channel+provenance / knowledge / noise** | the P6 classification; `knowledge` = "carries durable content that someone would retrieve *by content*, and that does not reduce to a small fact. This is the class that falsifies the proposition." | `step-minus-1/p6-channel-or-knowledge/TASK.md` | |
| **D1** | write-time supersession vs read-time expiry | `step-minus-1/p5-induction/TASK.md` §Measurements | "settled: read-time expiry beats write-time supersession ~7:1" - then the edge that would have read it was cut |
| **D2** | what happens when classification or target resolution fails | same | "the largest open design hole and currently has no rule at all" |
| **dateless head** | an announcement head where "a line that is non-empty but strips to empty occupies the date slot" | `step-minus-1/FINDINGS.md` §P4 | 13 of 39 |
| **silent-wrong** | a confident plausible incorrect label; pre-registered as "worse than no label at all" | `step-minus-1/TASK.md` §P2 | |
| **DEGRADE** | a third verdict between PASS and FAIL: the mechanism works but needs per-course tuning | `step-minus-1/p4-segmentation/TASK.md` §Verdict rule | |
| **the seal** | "Read material ONLY from the sealed directory you are given" - flattened, neutralized filenames, so induction is not transcription | `derivation/BRIEF.md` §THE SEAL | leaked; see §20 |
| **BLOCKED** | a verdict a subagent returns instead of guessing: "A blocked agent that asks a sharp question is worth more than a finished one that assumed" | `derivation/BRIEF.md` rule 5 | never fired; A3 came close and recorded it as a judgment instead |

---

## Internal contradictions

Surfaced, not resolved.

**C1 - Two agents independently proposed the field the human then dropped.** `[B2]` J2 argued `source_ref` must admit URLs and the node needs a `present` flag, on the grounds that §6's set-difference "answers wrongly in the most consequential direction: it reports *have* for things that are merely *named*". `[A3]` J7 independently proposed `backing: referenced_only`, with the extreme case that "Midterm 2 is a graded obligation with a released grade and literally zero artifacts on disk". `[Billy]` ruled both out (*`derivation/FINDINGS.md` §5*): "an artifact does **not** need a URL or a `present` flag … absence is not a field, it is the absence of store content." **The JOIN framing answers B2's set-difference concern. It does not obviously answer A3's - a node with no store content is indistinguishable from a node that was never created.** FINDINGS does not address the difference.

**C2 - FINDINGS misreports A3 on `produced`.** *`derivation/FINDINGS.md` §1 watch list*: "`produced` as a separate edge (A3, B2 - **both concluded a `role` attribute suffices**)". A3 J2 concluded the opposite: "I'd **split off** `obligation --produced--> artifact` … because it has its own named query that `spec` cannot serve: **'show me what I handed in for A8'** … Roles 1/2/4 can stay one edge with a `role` discriminator; **role 3 is a different relation.**" B2's `role ∈ {given, owed}` recommendation is about inputs vs outputs, which is a different cut.

**C3 - Three agents returned three different H2 verdicts, and the synthesis picks a fourth.** `[A1]`: "**FAIL, but not for the reason H2 anticipated**". `[A2]` J1: "**H2 fails on my slice, and it fails twice** … A tiered expansion strategy is owed before W1." `[B1]` J4: "**H2 passes on this slice**", contingent on title-scoping. *`derivation/FINDINGS.md`*: "**the gate is invalid as posed**". The synthesis is defensible, but A2's explicit demand - a tiered expansion strategy owed before W1 - is dissolved rather than answered.

**C4 - The granularity rule adopted contradicts A2's explicit warning.** *`derivation/FINDINGS.md` §1* adopts "the concept layer must be cut at 'one thing that can be separately asked about or separately taught'", following `[B2]` J6. But `[A2]` J1 argued the opposite for its own hub: "**Do not rescue the first hub by splitting it into per-topic analysis concepts.** That is re-describing, which §10.1 forbids, and it would also be wrong: **the whole value of the concept is that Big-O of Quicksort and Big-O of Dijkstra are the *same* skill.**" The adopted rule would license exactly the split A2 forbids. Not reconciled.

**C5 - The watch list holds edges that clear the stated bar.** The H4 bar is "≥3 real instances **and** a nameable query". `contains` has 9 instances and a named query `[A2]`; `projects`/is-a-view-of has 6 and a named query (de-duplication at expansion, "so that opening a concept does not return 4 diagrams of the same classes") `[A2]`; `sequence` has 3 `[B1]`. FINDINGS §1 files all three as "**one sighting each**, deliberately not adopted". *The instance counts in FINDINGS' own table contradict the "one sighting" characterization.*

**C6 - Three above-bar edges from A1 disappear without a ruling.** `[A1]` reported `answers` (6 instances, named query: "which tutorials have I never worked through"), `cites` (25+), and `example-code` (15+), each with a query. `cites` survives only in dissolved form, as the `locator` payload. **`answers` and `example-code` appear nowhere in `derivation/FINDINGS.md` - not adopted, not cut, not watch-listed.** `example-code` is the evidence for A1's point that a code-project reference resolves *into* a project (`tree.AbstractTree.heightBad()`), not at it - which A2 J5 independently raised as "the code library the diagram projects, a durable object spanning weeks, that the model can only see as six unrelated `code_project` artifacts". That thread ends here.

**C7 - The timestamp requirement was stated as hard and relaxed within the same document.** *`step-minus-1/FINDINGS.md` §P3* makes the publication timestamp **required** ("without it DoD 1 cannot be checked"). *§P4* then finds a third of the export has none and relaxes it to "the export preserves order", arguing "**what design §4 needs is *ordering*, not absolute time**". FINDINGS labels this "a sharpening of the requirement rather than a concession". **The self-labelling is worth noting rather than accepting: the P3 table was never rewritten**, so the document contains both statements.

**C8 - P2's image-only class was under-reported by its own probe, corrected two probes later.** *§P2* files image-only PDFs as a class with two Billy-authored files excludable. *§P6* corrects: 2c03's tutorial notes are handwritten scans, "making image-only material **a whole class in a core course rather than the edge case P2 reported it as**". Then `[A1]` and `[B2]` reproduce it independently in the derivation, in two more courses.

**C9 - Billy warned his folders are not taxonomy; the derivation TASK argued back and used them as ground truth anyway.** *`derivation/TASK.md` §2 rule 3* records the warning verbatim `[Billy]`. *§3* then makes his folder renames and his hand-written study guide the **sealed ground truth**, with the argument: "**correct, and irrelevant, because the target is not the course's taxonomy.** `resources/week-01..03` carry no topic suffix and `week-04-stack-queue-list` onward do: that is a timestamped record of *when naming a concept became necessary*." **This is an agent overriding a human warning by reframing what is being measured.** It may be right; it is recorded here because the override is not marked as one, and because the same document's rule 3 forbids exactly this use.

**C10 - The derivation set contains agent findings that the synthesis does not carry.** Beyond C6: `[B1]`'s `lecture_date` field and its course-specific-navigational-handle proposal (§16); `[A3]`'s J1 concept-weight tension and J6 dangling-edge requirement (§14, §17); `[A1]`'s third sticky-note origin (§19). Each has a named query or a named mechanism and appears in no adopted, cut, or watch list. **This may be deliberate compression or it may be loss; the corpus does not say which.**

**C11 - Two probe verdicts were reached and then the question was replaced.** P5 falsified the operations model (39% reduction); P6 then "**a change of question from P5** … This asks something narrower and cheaper to answer" (*`p6-channel-or-knowledge/TASK.md`*), and falsified *that* too. Neither the operations model nor the channel proposition survives, and the corpus does not state what replaced them. **This reads unfinished - the last thing `step-minus-1/FINDINGS.md` says is that Step 0 "invalidated the design cheaply", pointing at a design doc §10 outside my scope for what came next.**

---

## Coverage

**Read in full (2,974 lines of markdown, 100% of the in-scope markdown corpus):**

- `2026-08-22-step-minus-1/TASK.md`, `FINDINGS.md`, `p4-segmentation/TASK.md`, `p5-induction/TASK.md`, `p6-channel-or-knowledge/TASK.md` - 647 lines.
- `2026-08-22-derivation/BRIEF.md`, `TASK.md`, `FINDINGS.md`, `apparatus/README.md`, `agents/2c03-concepts-weeks-1-6.md`, `agents/2c03-concepts-weeks-7-13.md`, `agents/2c03-obligations-and-edges.md`, `agents/2aa4-lecture-concepts.md`, `agents/2aa4-tutorials-assignments-artifacts.md`, `per-course/2c03/inventory.md`, `per-course/2c03/counts.md`, `per-course/2aa4/inventory.md`, `per-course/2aa4/counts.md` - 2,327 lines.

**Read for orientation only:** `fall26/README.md`, `fall26/MOVED.md`.

**Listed but not read (in scope by directory, but not markdown; ~14,000 lines of data and code):** `step-minus-1/p1-pgvector/{probe.py,result.txt}` · `p2-structural-extraction/{extract.py,inventory.txt,candidates.json}` · `p4-segmentation/{segment.py,segment_multi.py,segment_v4.py,result.txt,multi_result.txt,v4_result.txt,segments*.json}` · `p5-induction/classification.json` · `p6-channel-or-knowledge/classification_{2c03,2da4}.json` · `derivation/apparatus/{seal.py,SCORING-KEY.json,titles2aa4/*}` · `derivation/per-course/{2c03,2aa4}/graph.json`. **Every number I cite from these comes from the markdown that reports them, not from the raw file.** The one place this matters: `p3-announcement-recon/` is an **empty directory** - P3 produced no artifacts, consistent with its stated deliverable being a specification rather than an export.

**Deliberately not read, per the task boundary:** `2026-08-23-slice-1/`, `2026-08-24-slice-1-write/`, `2026-08-23-cost-probe/`, `2026-08-22-modeling/`, anything else in `openclaw/`, and all of `~/Documents/Projects/fall26/`.

**What I could not account for:**

1. **`MODEL.md` and `PLAN.md` are the spine of the derivation and I could not read them.** Every H1-H4 verdict, every "§8 does not have this", and every "§2 asserts" is scored against a document out of scope. I have recorded the derivation's *characterizations* of MODEL.md, which are agent-reported and unverifiable from here.
2. **Same for `design §N` and `build spec §N`,** cited on nearly every page of `step-minus-1/`. The design's goal function, §4's insert-vs-rewrite mechanism, §10.7's rulings, and D1/D2's original statements all live there.
3. **`2026-08-22-modeling/PLAN.md`** is named in `fall26/README.md` as a design cycle's entry file and cited by the derivation's over-modelling rule; out of scope.
4. **The P5 and P6 per-announcement classifications** (`classification*.json`, ~3,000 lines) hold the individual `ephemeral` instances and `knowledge` quotes that both TASKs said were "the finding, not the tally". The markdown reports the tallies. **The instances themselves are unread.**
5. **`SCORING-KEY.json`** is the only record of which sealed name maps to which true document. Unread, so I cannot audit any agent's contamination claim independently.
6. **P2's pre-registered second stratum never ran**, and no file in scope records a decision to abandon it.
7. **P4's per-course check on 2c03 and 2da4 is listed as "still unverified"** and no in-scope file settles it, though `segments_2c03.json` and `segments_2da4.json` exist on disk, which suggests it ran and the verdict lives elsewhere.
8. **`per-course/*/graph.json` exists but `FINDINGS.md` never cites it**, and `counts.md` states that a deduplicated course-level count "was never produced". What is in those two JSON files, and whether it is the deliverable TASK.md §4 asked for, I cannot say.
9. **The rendered token count `derivation/TASK.md` §4 asked for was never computed** - stated outright in `per-course/2c03/counts.md`.
10. **Ratio of human to agent authorship, stated plainly:** of 2,974 lines, roughly 1,051 (35%) are verbatim subagent reports, ~740 (25%) are main-session compilations of those reports written two days later, and ~1,183 (40%) are main-session coordination prose. **Eleven passages carry explicit human attribution.** No transcript of the "grilling conversations" that produced the origin ideas is in scope, so the human's own framing survives here only as these eleven fragments and as agents' secondhand citation of a design doc I could not open.
