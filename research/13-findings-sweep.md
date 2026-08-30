# 13 - the `records/findings/` sweep

**What I read, whole.** `/Users/billywu/Documents/Projects/fall26/records/findings/read-cycle.md` (401 lines) and `/Users/billywu/Documents/Projects/fall26/records/findings/ingestion-probe.md` (43 lines). Both read end to end before any conclusion, per the standing defect that this file has twice been mis-cited by a reader who saw only part of it.

**Boundary observed.** To check whether a finding is carried or cited elsewhere I read `records/domain/`, `records/spec/`, `records/plan/` and `records/archive/`. Nothing else: no `evidence/`, no `openclaw:` path, no other repository, no `app/` source. Every `openclaw:` link these two files make is therefore reported as the file states it and marked unauditable from this checkout - which both files say of themselves in their own headers. I also read `research/12-archive-sweep.md` in this repo to recover the four claims it handed over.

Branch: `design/course-level`; `records/` is identical to `main`.

**Standing of a `findings/` record, as the repo defines it.** Changed only by a new measurement; a reader may not argue with it; superseded by measuring again. So nothing below adjudicates whether the null result stands. Where a finding and a later ruling point different ways, both are reported and each is named for what it is.

---

## The read-cycle null result, at source

### The headline, before the detail

**The sentence that has been quoted all through this effort is real, is in §4 where it is cited, and carries its own scope in the same sentence.** And the ground on which `spec/ring-0.md` §2 "refuses" it is **not an outside objection at all - it is the finding's own stated limit, printed three separate times in the file.** `read-cycle.md` does not claim what the citing records have been treating it as claiming, and it never did.

The one thing the citing records get materially wrong is smaller and different, and it is in the other direction: **`spec/ring-0.md` §2 says `domain-design.md` §9.2's test "has been run and returned nothing", where `read-cycle.md` states twice that §9.2's premise is untested.**

### 1. What the test was, precisely, and who judged it

There is no single named "membership test" in `read-cycle.md`. What exists is a manipulation series and one reproduced outcome.

**What ran** (`read-cycle.md`, preamble, lines 15-18):

> **What ran:** 60 `claude -p` runs in `~/Documents/Projects/fall26-sim/`, a sibling of the build repo, with product vocabulary only (the run sees no *ring 0*, *skeleton* or *slice*). Every run got the same sentence — `help me plan for the rest of this semester` — over the same 22 real obligations from 2c03 and 2aa4. Twelve distinct `tools.py` surfaces across the 60. **Not one line of slice 1 was built.**

**The manipulation and the outcome** (§2, "The central negative result", lines 79-81):

> **Across roughly forty runs and four manipulations of what the planner could SEE — placement (E0), size legibility (E1a), the skeleton (E5), a complete ring 0 (E7) — the plan never stopped being a date-ordered sort. The planner reports; it does not allocate.**

**What counted as "changing the plan's shape" is stated concretely and is not a judgement call** (§2, lines 91-92):

> Every run produced the same ordering of the eight dated obligations: `a5 → 2aa4-a2 → a6 → {a7, 2aa4-a3} → a8 → bonus-survey → a9`. No hours distributed, no week balanced, no capacity, no tradeoff between courses.

So the judge is a **string comparison over the ordering of eight dated obligations**, plus the absence of four named allocation behaviours. Not a grader, not a reading of prose. This matters, because §0 line 42-44 sets the file's own admissibility rule:

> **The rule the cycle ended on, and it is the reason this file is short: weight counts; treat any reading of one run's prose as a hypothesis.** … **Every finding that survived replication is a count.**

**The claim was challenged once and survived on a better fixture** (§2, lines 94-99). Billy objected that the fixture was mostly holes - 7 of 22 items with no `due`, 13 of 22 with no `status` - where reporting holes *is* correct behaviour. A launch-shaped fixture was built with every value a launched ring 0 would hold present and only `hours_estimate` left null. "The plan was still `ORDER BY due − 7`. It went from *asserted on a bad fixture* to *tested on a launch-shaped one*."

**A precise limit the citing records do not carry** (§2, lines 108-112): the *ordering of the eight dated obligations* replicates; **the saved queue does not**. Runs differ on membership - a review session appears inside the sequence in two runs, in a separate bucket in one, not at all in three. "**'Identical in all six runs' is true of the sort and false of the artifact.**"

### 2. The instrument, and whether the file states its own limits

**It does, unprompted, in four places.** The claim that a separate record "refuses this null result on the ground that every run was a memoryless `claude -p` cold start" describes text that is already inside the finding.

§2's scope block, printed inside the same blockquote as the result (lines 83-89):

> **Its scope, carried here rather than left to the Caveats below (§1-§3), because this sentence is the one most often quoted alone.** Every one of those runs was a **memoryless `claude -p` cold start**, while the design's coordinator is long-running and holds ring 0 across turns; all ~40 used **one fixed prompt**, *help me plan for the rest of this semester*; and the two courses are **the same shape**. So this is a result about **one-shot planning from a fixed request**, and it is silent about what an observation space is worth to a coordinator deciding where to look next. **A device that cannot exercise routing returns "nothing changed" whether or not routing matters.**

Caveats §1 (lines 307-315), titled *Every run was a cold start; the product's coordinator is not*:

> Each run is a single `claude -p` invocation with no memory, no accumulated preferences and no prior turns. `domain/domain-design.md` §1 ruling 11 says the coordinator is **long-running** … **Nothing in this folder tested that topology.** Results about tool surfaces and data hold; results about what a coordinator would *accumulate* or *carry between turns* were never in scope.

§9, *What this cycle did NOT establish*, final bullet (line 298): "**Anything about a long-running coordinator.** Every run was a cold start (`CAVEATS.md` §1)."

And Caveats §7 (lines 372-377) puts a general warranty limit on every number in the folder: the scoring harness has been wrong twice, "**Both bugs produced confident numbers.** Any metric in this folder that has not been re-derived structurally should be treated as unverified."

**So `spec/ring-0.md` §2's refusal is a restatement of the finding, not a rebuttal of it.** Compare - `ring-0.md` line 28:

> **That null result does not license removing the fields, and it does not confirm the routing test either.** The instrument could not have detected the effect: every run was a memoryless `claude -p` cold start, and the design's coordinator is long-running … A device that cannot exercise routing returns "nothing changed" whether or not routing matters.

The last sentence is `read-cycle.md` §2's own words, line 88-89, reproduced without attribution.

**The parent's correction about lifetime lands cleanly on this, and does not disturb it.** `read-cycle.md`'s instrument is a *code process* cold start - `claude -p`, no prior turns. The design's coordinator is long-running as a *conversation*. The two are different questions, and the finding's own scope sentence names exactly the right one: the runs held nothing "across turns". Under the parent's framing this stays a **live question**, not a settled dismissal, and `read-cycle.md` frames it that way itself: §9 lists it under *what this cycle did NOT establish*, not under *what is refuted*.

### 3. The finding's stated scope - the sentence, quoted

The summary sentence everyone quotes is §4's closing paragraph (lines 177-180). **Its scope clause is in the same sentence and is not separable from it:**

> **Which is the same result as everything else this cycle produced.** `parts`, `worth_percent`, the skeleton, a complete ring 0, and now progress: **each is read, each is rendered, none changes the plan's shape** - under §2's scope, which this sentence inherits whole and which anyone quoting it must carry: memoryless cold starts, one fixed prompt, two courses of the same shape.

Three separate warnings tell a reader to take the Caveats first (line 13, line 5, and the §2 scope block), and the file records that this failed anyway (§0, lines 52-56):

> **Measured 2026-08-28, and it is why this paragraph exists.** A sitting applied *weight counts* correctly - it took a count rather than a reading of prose - and still used §4's summary sentence as evidence against a criterion those runs could not have tested. **This file warns three separate times to read the Caveats first, and that sitting skipped them anyway**, which is the same result the repository already has about warnings placed above content rather than on the claim.

That paragraph is dated the day `spec/ring-0.md` was created (`ring-0.md` changelog, line 104), and describes `ring-0.md` §2's use of the sentence exactly. **The loop is closed inside the corpus:** the defect was caught, the scope was moved up into the sentence, and `ring-0.md` §2 now carries the correction in its own next paragraph.

### 4. Do the citing records stay inside the scope?

Three records cite `findings/read-cycle.md` by name. All three are in `spec/ring-0.md`.

| citation | verdict |
|---|---|
| `ring-0.md` §2 (line 26) - the null result | **Over-reads in one respect, and self-corrects in another.** It says §9.2's test "has been run and returned nothing." `read-cycle.md` says §9.2's **premise is untested** - twice (§3 table row 2: "The premise is **untested**, neither supported nor refuted"; §9 bullet 2: "Whether `domain/domain-design.md` §9.2's premise holds … Untested"). The measurement was test-*shaped*; the file declines to say it ran §9.2's test. **But `ring-0.md` line 28 immediately restates the full scope**, so the record does not act on the over-read. |
| `ring-0.md` §5 (line 73) - array order | **Inside scope, and it is the strongest use of the file in the corpus.** §4's E10r result (lines 165-168) is exactly this: "**A swapped-cause control** moved the notes and changed nothing else: **A7 still comes first, 3 of 3** … Ordering is array order." `ring-0.md` uses it to convict the projection and state the fix. Section number omitted (it is §4); resolvable. |
| `ring-0.md` §6 (line 77) - conditional weighting, 24/17 and 29-of-77 | **Inside scope, and unusually careful.** The figures match §5 exactly (lines 187-191). `ring-0.md` line 79 then states the number's own standing unprompted, including that it "has **not** been re-derived structurally, which `CAVEATS.md` §7 asks for before any metric in that folder is trusted." That is the finding's own warranty limit, carried by the citing record. |

**Nothing in `domain/`, `plan/` or `archive/` cites `findings/read-cycle.md` by path.** `archive/` cites the openclaw originals; `domain/domain-design.md` §2 and §9.3 and `domain/model.md` §10 carry promoted conclusions from the same cycle without naming the findings record.

### 5. Caveats the citing records drop

`ring-0.md` carries Caveats §1, §2, §3 and §7. **Two are dropped by every citing record:**

- **Caveats §4, the fixture is historical and partly synthesized** (lines 334-342). Three of the four synthesized values trace to one accident - 2aa4's Avenue page was deleted after the fact - and the file records a retraction in place: the 2c03-rich / 2aa4-empty asymmetry "was defended earlier in the session as *'what a course looks like eighteen days before launch.'* It is not. It is an artifact of that deleted page, and it was sold as a feature before being caught." Note this is the **launch-shaped** fixture, the one that carried the null result past Billy's challenge.
- **Caveats §8, runs narrate tool calls they did not make** (lines 379-388), and the `tools.py` apparatus leak: "**`tools.py` is readable in every run directory**, so a run can learn what a verb would return without calling it - an apparatus leak present since the first run, and one a deployed assistant would not have."

And one more, dropped by every reader including `ring-0.md` - **§0's fourth paragraph** (lines 46-50), which is the file's own statement of what *weight counts* does not catch:

> *Weight counts* filters for whether a number is **real**. It does not filter for whether the number answers the question being asked of it. **A perfectly reproduced count can be a count of something else.** §2's central result is exactly that case.

### 6. Where Billy's 2026-08-30 rulings land on it

- **Ruling 2 (size, and the work need not be a functional one-pass) largely moots the null result rather than overturning it.** §2 measured *the planner does not allocate*. Ruling 2 says the agent "sees the skeleton and ring 0, notices, and **asks when needed** rather than executing blindly", and that `hours_estimate` is not quantifiable. The criterion the ~40 runs failed - hours distributed, weeks balanced, capacity, cross-course tradeoff - is no longer a v1 criterion. The measurement is untouched; its consumer is gone.
- **Ruling 3 (`time_point` out, the plan is real but not settleable now) removes the object the test measured against.** §2's outcome variable is *the plan's shape*. `ring-0.md` §7 states "**the plan has no representation anywhere**". The finding measured a change in an object the system does not represent.
- **Ruling 4 (`progress.state` defaults to `not_started`) was already reconciled inside the file**, by its own 2026-08-28 changelog entry and the boxed note at §4 lines 171-175. The observation ("the ordinal invited invention") stands; the rule it was judged against does not. The file says so explicitly and adds "Do not cite this line as authority for a rule that is gone."

---

## The ingestion probe, at source

**What was measured** (header, lines 3-4): four providers and forty arms available 2026-08-23, over the five-course corpus (~3400 page-images). **Conclusions only** were imported from `openclaw:fall26/2026-08-23-cost-probe/FINDINGS.md` on 2026-08-25; "The forty arms, their per-page scores and the scoring key stayed there, so nothing here is auditable from this checkout."

**Its stated scope, quoted** (line 3):

> **conditions:** measured on the four providers and forty arms available 2026-08-23. Prices and model names age; the failure modes are the durable half.

That sentence is the whole scope statement, and it is a good one: it partitions its own content into a perishable half (prices, model names) and a durable half (failure modes, tokenisation, container).

**Why the record exists at all** (line 5) - and it is the same class of problem this sweep is for:

> **note:** written because several of these facts existed nowhere in this repository except an always-loaded instruction file, which is the wrong home for a measurement.

**What was concluded.** Six things, one of them a ruling:

1. **The ruling** (line 9): "Build on `claude-sonnet-5` with **native passthrough**. Cost, quality and latency optimisation is deferred and revisited only when cost becomes a reason to. **[R] Billy, 2026-08-23.**"
2. **Cost is not a constraint** (line 13): one structure pass over ~3400 page-images costs **$2 to $20** of input, every arm under $25 all-in, so the corpus layer is designed for quality rather than thrift. The provider spread survives holding price constant - at a fixed $2.00/MTok the per-page spread is still **3.51x** - "so it is a **tokenisation** fact rather than a pricing one."
3. **Structured output is not needed** (line 19): "**39 of 40 arms returned parseable JSON and none invented a section.**" The decisive case: a handwritten scan yielding **73 characters** to `pdftotext` still produced 5 to 7 correct sections in every arm.
4. **The concept layer is transcribed, not induced** (line 21) - "Every provider reproduces a deck's stated section structure verbatim" - which is why H3 remains untested.
5. **What it gets wrong** (line 25): "**A model will import a correct definition that appears nowhere in the source.** One arm produced a textbook-accurate definition that is absent from the page image it was given. It is correct and it is not a quotation, and nothing downstream can tell the difference. **Never present a generated description as something the source said.**" And (line 27) "**Zero-hallucination is a vendor property, not a tier property**" - the tier-matched `gemini-3.1-pro-preview` scored worst of four at 2.67x flash's price; `claude-sonnet-5` "was the only arm that stated nothing false."
6. **The container** (line 31): "**PNG is the wrong container, and the batching trigger is REQUEST BYTES** - not context, not page count." A 29-page deck is 25.0 MB base64 at 150 DPI, 78% of the 32 MB request ceiling, 413 seconds at 200 DPI. Self-rendered PNG breaks above ~37 pages and the corpus holds seven decks between 36 and 64. Remedies in order: JPEG, then native, then batching.

**Which records cite it: none.** Grep of `domain/`, `spec/`, `plan/` and `archive/` returns **zero** references to `findings/ingestion-probe.md` by path, and zero occurrences of `sonnet`, `passthrough`, `JPEG`, `DPI`, `32 MB` or `batching` anywhere in the three live tiers. **So the scope question does not arise - nothing cites it, inside its scope or outside.** The only other statements of these facts in the whole corpus are `archive/openclaw-registry-2026-08-25.md` entries 42, 43, 44, 45 and 47, which are frozen.

**Consequence, and it is the finding of this section: `findings/ingestion-probe.md` is the sole live home of every fact it carries, including a `[R]` Billy ruling.** If it does not migrate, all of it is lost.

---

## Live material found

### L1. The ruling on the ingestion model - `[R]` Billy, 2026-08-23

`findings/ingestion-probe.md`, "The ruling", line 9: "Build on `claude-sonnet-5` with **native passthrough**. Cost, quality and latency optimisation is deferred and revisited only when cost becomes a reason to."

A `[R]`-marked Billy ruling sitting in a findings record - the wrong tier by the repo's own definition, since a ruling is not a measurement. Its only other statement is `archive/openclaw-registry-2026-08-25.md` entry 42 (frozen). Nothing in `domain/`, `spec/` or `plan/` states it.

**Destination: deferral issue**, carrying the precondition **the corpus / offline ingestion pass is being built** (Billy's ruling 1 keeps v1 inside coursework; the corpus layer is slice 3 and not in v1). The issue should carry the ruling, the $2-$20 cost bound and the 3.51x tokenisation fact as its evidence, since the cost gate is what licences designing that layer for quality rather than thrift.

### L2. Never present a generated description as something the source said

`findings/ingestion-probe.md`, "What it gets wrong", line 25, quoted in full above. The header (line 5) records that this fact "existed nowhere in this repository except an always-loaded instruction file" and that the record was created to rescue it.

**It is still homeless outside this file.** Grep of the three live tiers finds no statement of it. `spec/schema.md` §4 comes near it from a different direction - `sticky_note.origin` records "how this annotation came to exist" - but that is provenance typing, not a prohibition on attributing generated text to a source.

This is **not** corpus-only. Billy's ruling 6 makes the RAG determinant "semantic, decontextualized facts about course materials, whatever the artifact's form", and v1's screenshot intake produces exactly the class of artifact the finding is about: a model reading an image and writing text that a reader will take as what the source said.

**Destination: ADR, slug `generated-text-is-never-attributed-to-the-source`.** All three tests hold - hard to reverse (it constrains every write surface and every rendering surface at once); surprising without context (the failure mode is a *correct* definition, so correctness checking cannot catch it); the result of a real trade-off (generated enrichment is useful, and the price of keeping it is that it can never be presented as quotation). The 39-of-40 and the one-arm counterexample are its evidence.

### L3. Live intake and the corpus are two paths that must never be crossed

`findings/ingestion-probe.md`, line 35: "Live intake is a pasted screenshot **read by the session itself** - the harness reads the image, so there is no API call and no token cost. The corpus is page-images that cannot enter a session context at any price, and it goes through this pass offline. **Routing either one through the other is a category error, not an optimisation.**"

The live tiers carry **halves** of this and never the rule. `spec/architecture.md` §? (line 91) says "`fall26/ingest.py` stays Python as an offline pass and **is in no tier**". `archive/slice-1-plan-2026-08-27.md` §3 line 42 says "Live intake is read by the session itself. The harness reads the pasted image. No API call, no `structure_pass`." Neither states that crossing them is a category error, and the archive is frozen. `archive/openclaw-registry-2026-08-25.md` entry 47 states it, and is frozen.

**Destination: ADR, slug `live-intake-and-corpus-ingestion-are-separate-paths`.** Hard to reverse (it is a tier boundary); surprising without context (the two look like the same multimodal problem at different scales); a real trade-off (one shared path would be simpler and would cost either tokens or a session). The v1-relevant half is the live-intake half, which is in scope under Billy's ruling 1.

### L4. `[R]` Billy, 2026-08-23 - repair over bannering, and the `*-BROKEN` exclusion

`findings/read-cycle.md` §0 item 1, lines 29-35: a crashing tool in nine runs; **[R]** Billy ruled repair over bannering (*"与其打 banner，不如 fix 后再对那些受影响的重新跑一遍…只为保证这些结果都是可被引用的"*). The nine configurations were re-run; the defective originals are preserved as `*-BROKEN` and **excluded from citation**.

A ruling, in a findings record, about how a defective measurement is handled. Its object is an openclaw evidence folder that is not migrating.

**Destination: not carried.** The specific artifacts are outside the new repo. The general form of it - a wrong number left in place gets cited, so delete and re-run rather than banner - is stated a second time in the same section (item 3, lines 38-40: the omission matcher's column was "**deleted** … rather than bannered - a wrong number left in place gets cited") and belongs to methodology rather than to this project.

### L5. The instrument perturbation that must never be reported as a finding

`findings/read-cycle.md` §6, lines 248-250: "`look_at(node_id, question)` requires the agent to say why it is calling, which makes the call more deliberate. Constant across arms, so it does not confound a comparison — **but it must never later be reported as a finding.**"

This is live and load-bearing: the `question` parameter is a real design element in the corpus (`archive/openclaw-registry-2026-08-25.md` entry 55 area carries Billy's ruling that "the question is not to be predicted but stated at call time"), and this sentence is a standing prohibition on citing an artifact of the apparatus as evidence for it. Stated nowhere else in `domain/`, `spec/` or `plan/`.

**Destination: not carried as its own item, but it must travel with any ADR on the read verbs' `question` parameter** as a note on the evidence. It is a caveat on a measurement, and the ADR whose reason it qualifies is the one that adopts a `question` parameter. Under Billy's ruling 9 the verb surface is deferred, so this waits with it.

### L6. Nothing else in either file is a ruling

Everything else in `read-cycle.md` is a count or a retraction. The other `[R]` marks in the file - Caveats §2's *"how to use it is the user's burden, not the system's"* and Caveats §5's *blind scoring does not work on this fixture* - are **already homed live** in `domain/domain-design.md` §2 (lines 146-165), which carries both and marks the first as promoted. No action.

---

## Open questions never re-homed

### Q1. The owed experiment, and the two remaining suspects

`findings/read-cycle.md` §2, lines 101-106:

> **What is isolated, and the two are separable:** the cause lies in **sizing** or in **the absence of an allocation procedure**, and nowhere else in the observation space.
>
> **The next experiment must vary what the agent must DO, not what it can SEE.** E8 attempted exactly that — a `save_plan` that requires a weekly shape — and **E9 retracted both of its claims** (§3). The attempt is owed again, on uncontaminated runs.

`spec/architecture.md` §4 voided acceptance (c), which was its carrier. **Destination: deferral issue**, precondition **an evaluation harness exists that can vary the required output shape**. Note in the issue that Billy's ruling 2 answers the *sizing* suspect directly - size is judged from progress and load, `hours_estimate` is not quantifiable - so only the *absence of an allocation procedure* survives as a live suspect, and ruling 2's "asks when needed rather than executing blindly" may retire that one too.

### Q2. Three of the five things the schema could not hold

`findings/read-cycle.md` §7, lines 256-262. Two of the five were ruled 2026-08-23 (items 2 and 3, conditional weighting and the bound). Of the remaining three:

- **Item 1, the late-day budget** - "**12 late days, up to 3 per assignment** … **still open.** A course-level consumable resource modulating every deadline. Inert in 0 of 6 runs — **nothing in the plan ever computes lateness**, so a policy about being late has no consumer. Typing it alone changes nothing." **Already homed live**: `domain/model.md` §10 item 9 says "the late-day budget is NOT resolved and stays open", and `spec/design.md` F4 and §3 make it a course-level note. **No action** - though the finding's sharper form (typing it changes nothing without a consumer) is stated only here.
- **Item 4, team formation** - "**'form teams by the end of Week 1'** … **still open.** No term calendar exists in any held material, so `due` is `null` and the obligation's only timing information is discarded." **Homeless.** No live record states that no term calendar exists. Billy's ruling 1 graveyards `offering_term` for v1 and ruling 3 removes `time_point`, so the two candidate carriers are both out. **Destination: deferral issue**, precondition **a term calendar becomes representable** (i.e. `offering_term` or the time layer is un-graveyarded). Billy's ruling 8 - content and time layers must be separate - is the frame this lands in.
- **Item 5, the snow-day credit** - "`count{done,of}` holds the target but not a credit that changes the denominator." **Mooted, not open.** `spec/schema.md` §7 graveyards `count{done,of}` and recurring obligations entirely, and `plan/backlog.md` B1 carries the residue. **Destination: not carried**, with the reason that its subject was graveyarded.

### Q3. The self-report gap in the faithfulness rubric

`findings/read-cycle.md` §5, lines 224-231, carries the measurement - **9 scored findings across 6 of 60 runs**, all about `ask_about_course`, plus **21 further findings across 13 runs** asserting a tool's behaviour without invoking it; 48 of 60 runs called a tool they never name; "**`calls.jsonl` is the only trustworthy record of behaviour**" - and adds "**The grader makes unsupported claims of its own**, in several rank-3 verdicts."

What it does **not** carry is the owed repair. `calls.jsonl` appears **zero times** in `domain/`, `spec/` and `plan/`. **Destination: deferral issue**, precondition **an evaluation harness with a tool-call log exists**, carrying the rule that a run's narration of its own tool use is void as evidence.

### Q4. What §9 says was never established, and is still not

`findings/read-cycle.md` §9, lines 291-298: five items. Three of them are still open and not carried anywhere live - whether the walk would be used for judgment rather than gap-filling; whether `domain-design.md` §9.2's premise holds; whether any configuration is better than any other. §9.2's premise is separately flagged as untested at §3 line 121. **`domain/domain-design.md` §9.2 does not record that its premise is untested** - see the citation defect C3 below.

---

## Reasons a live record depends on that only exist here

### R1. `spec/ring-0.md` §6's entire justification for excluding `grade_share`

`ring-0.md` is titled, at §6, "**Why `grade_share` is excluded, on measurement rather than argument**". Its argument is two sentences of numbers, and **every number in them is from `findings/read-cycle.md` §5** (lines 187-191): 24 claims across 17 runs; 29 of 77; 38% of every measured faithfulness failure; the only defect kind appearing in every configuration group. `ring-0.md` restates them but does not restate what produced them - "All 60 runs graded by an independent grader given the run's own tool output and its answer, nothing else. **77 unsupported · 32 contradicted · 449 well-handled**, over 870 run-item pairs."

**If `read-cycle.md` does not migrate, `ring-0.md` §6's title becomes false** - the exclusion stops resting on measurement. `ring-0.md` §6 line 81 does supply an independent argument from the corpus (2c03's column sums to 95, the missing 5% has no row, two 1% bonuses sit outside the 100), which would survive alone; but the record's stated basis would not.

`domain/model.md` §10 item 9 (line 683) carries the same figures a second time, promoted 2026-08-24. So the numbers survive in a live record - but `model.md` is frozen 2026-08-22 and its §10 is an *owed* list, which is a weaker carrier than a findings record.

### R2. The negation/conditional asymmetry, in its sharp form

`findings/read-cycle.md` §5, lines 195-203, the two-row table and its conclusion:

> **The agent acts on a note that NEGATES a field and cannot act on a note that makes a field CONDITIONAL.**

`domain/model.md` §10 item 9 (line 686) carries this sentence. But two things sit only here: **the sharpest instance** (lines 205-209) - "one run **formulated the question itself**, asked the course how the midterms are weighted, received the summary carrying the rule, and its output never mentions it. Not a delivery failure and not an attention failure" - and **the correction to the phrasing**: "The commonly-quoted *'falsified across four delivery paths'* is an **overstatement corrected by review** — two mechanisms, two of them n = 1. The measurement is what carries the ruling, not the phrasing."

That correction is the reason `model.md` §10 item 9 states the ruling on a count rather than on the delivery-path claim. The reason is here; the conclusion is there.

### R3. `spec/ring-0.md` §5's conviction of the implementation

`ring-0.md` §5 line 73: "The order measured in `findings/read-cycle.md` was array order, so the projection has been violating that rule rather than lacking a rule." The evidence is §4's swapped-cause control (lines 165-168) - A7 first 3 of 3 with the notes moved. **Only here.** Without it, `ring-0.md` §5 is a rule with no defendant.

### R4. The zero-omission correction, and the reason it is only a regression guard

`findings/read-cycle.md` §5's boxed `[CORRECTED, Billy 2026-08-23]` block (lines 211-222). `domain/domain-design.md` §2 (lines 163-165) and §9.3 (line 359) both carry the conclusion - "at slice-1 scale the recall half was never loaded", "the precision-versus-recall framing that cycle used is void". **Two things they do not carry**, and they are the reason:

> a **second instrument in the same directory disagrees on 20 of 60 runs** (hand-checked on three; the structural matcher is right and the LLM grader wrong), and the zero is **not robust to a defensible tightening** — removing one permissive matching rule yields 47 omissions across 17 runs. "Zero" is the output of the most permissive of several reasonable matchers.

`domain-design.md` reports the zero as real-but-trivial. The finding says the zero is also **matcher-dependent**. That is a stronger statement and it exists only here.

---

## Broken or ambiguous citations

**Outbound, from the two findings files:**

| # | where | defect |
|---|---|---|
| C1 | `ingestion-probe.md` line 35 | "The ruled form of this is `plan/slice-1.md` §3." **`records/plan/slice-1.md` does not exist** (`plan/` holds `application-tier.md`, `backlog.md`, `write-rules.md`). The successor is `archive/slice-1-plan-2026-08-27.md`, whose **§3 is the right section** ("What is settled and must not be re-litigated", line 42 carries the rule). Path dead, section number correct. `plan/write-rules.md` line 38 already uses the corrected relative link, so the corpus knows the move and `findings/` was not updated with it. |
| C2 | `read-cycle.md` line 401 (changelog, 2026-08-25) | Same dead path: "the settled list (now in `plan/slice-1.md`)". |
| C3 | `read-cycle.md` §5 line 193, and §7 table row 2 line 259 | "Billy's minimal fix is at [`domain/model.md`](../domain/model.md) §10.9". **`model.md` has no §10.9** - it has `## 10` with a numbered list, and the conditional-weighting ruling is **item 9**. It resolves by content, and the numbering is inherited from the openclaw-era `MODEL.md §10.9` (`archive/openclaw-registry-2026-08-25.md` entry 66 uses the same form). **Ambiguous, resolvable, and it fires twice.** |
| C4 | `read-cycle.md` Caveats §3 line 330 | "FINDINGS §3's correction to `domain/model.md` §3". **This is the silent-resolution defect.** After the 2026-08-25 merge of `FINDINGS.md` and `CAVEATS.md` into one file, "FINDINGS §3" has no referent - **this file's §3 is "What did NOT survive"**, a real section about something else entirely, and a reader lands there. The intended target is the pre-merge `FINDINGS.md` §3. `model.md` §3 ("The unification hypothesis") is the right target for the second half; the density table is at line 111 inside it. |
| C5 | `read-cycle.md` §4 lines 171-175 | Cites `spec/schema.md` §4.5 - **correct and current** (`schema.md` line 95). This is the one citation in the corpus that was actively repaired when its target moved; the 2026-08-28 changelog entry records why. Noted as the counter-example. |
| C6 | `read-cycle.md` Caveats §1 line 312 | Cites `domain/domain-design.md` §1 ruling 11 - **correct** (`domain-design.md` line 116, "The coordinator is long-running, not booted per session"). |
| C7 | `read-cycle.md` §3 line 121, §9 line 294, Caveats §3 line 330 | Cite `domain/domain-design.md` §9.2 - **correct** (line 474). |
| C8 | both files, all `openclaw:` links | `read-cycle.md` links `experiments/`, `FIXTURE-PROVENANCE.md`, `BLIND-PACKET.md`, `INCONSISTENCIES.md`; `ingestion-probe.md` names `fall26/2026-08-23-cost-probe/FINDINGS.md`. **Unauditable from this checkout by design**, and both headers say so. Not defects, but every one of them dies on migration. |

**Inbound, from the other tiers:**

| # | where | defect |
|---|---|---|
| C9 | `spec/ring-0.md` §2 line 26 | **A field name that does not appear in the source, inside a bolded quotation.** `ring-0.md` renders §4's list as "`parts`, **`grade_share`**, the skeleton, a complete ring 0 and `progress`". `read-cycle.md` §4 line 177 says **`worth_percent`**. **`grade_share` appears zero times in `records/findings/`.** The substitution is semantically defensible - `archive/slice-1-plan-2026-08-27.md` line 53 records `weight` → `grade_share` as a rename and `model.md` line 675 uses `worth_percent` for the same field - but a reader who greps `read-cycle.md` for the quoted term finds nothing, and the bold formatting asserts verbatim quotation. Propagated verbatim into `research/02`, `research/04` and `research/07-classification-D`. |
| C10 | `spec/ring-0.md` §2 line 26 | The quoted clause is a **paraphrase presented as a quotation**: "each read, each rendered, none changing the plan's shape" against the source's "each is read, each is rendered, none changes the plan's shape". It also **truncates before the scope clause**, which is in the same sentence. `ring-0.md` restores the scope in its next paragraph, so no scope is lost in that record - but the truncated form is what travelled. |
| C11 | `spec/ring-0.md` §2 line 26 | **Over-read.** "That one has been run and returned nothing" - `read-cycle.md` §3 line 121 and §9 line 294 both state `domain-design.md` §9.2's premise is **untested**. |
| C12 | `spec/ring-0.md` §2 line 28 | Cites `openclaw:fall26/2026-08-23-slice-1/CAVEATS.md` §1 when **the identical text is in-repo** at `findings/read-cycle.md`, Caveats §1. A live spec record pointing at an unauditable external file over the in-repo home. |
| C13 | `spec/ring-0.md` §2 line 28 | **The worst instance of the silent-resolution class in this pass.** After the `CAVEATS.md` §1 citation, the same sentence continues "all ~40 runs used one fixed prompt … **(§2)**; and the two courses are the same shape **(§3)**." Those are `CAVEATS.md` §2 and §3. **A reader inside `ring-0.md` resolves them to `ring-0.md` §2 and §3** - both of which exist ("What earns a place", "Two bands") and are about something else. Fails invisibly. |
| C14 | `spec/ring-0.md` §6 line 79 | Same as C12: cites `CAVEATS.md` §7 where `findings/read-cycle.md`, Caveats §7 holds it. |
| C15 | `spec/ring-0.md` §5 line 73 | "The order measured in `findings/read-cycle.md`" - **no section**. It is §4. Under-specified; the file is 401 lines. |

**Nothing anywhere cites `findings/ingestion-probe.md`.** That is not a defect in a citation - it is the absence of one, and it is the reason the file's contents have no second home.

---

## Contradictions with standing records

### X1. Where 2c03's grade weights live - a measurement against a frozen record

**The finding**, `read-cycle.md` §7 lines 268-271, from the 2026-08-23 load of the 22 real obligations:

> **A provenance finding that outranks the schema ones.** 2c03's A1–A9 weights, its late-day policy, its participation rule and its conditional weighting all exist in exactly one place: **page 8 of the Week 1 lecture deck** — not the outline, not the portal, not any handout. **An ingest order that prioritises outlines and handouts would miss every grade weight in this course.**

**The standing record**, `domain/model.md` §10 item 8 (lines 667-670):

> **Ingest ordering: the governing artifact before the ones it governs.** The course outline is the only carrier of grade weights (without it, 9 of 12 graded items have none and the planner runs blind) …

**These are flatly opposed on the same course.** The finding is a **measurement** dated 2026-08-23; `model.md` is **frozen 2026-08-22** and its claim comes from the earlier derivation cycle. Under the tier rule the measurement is the later instrument and `model.md` cannot argue with it - but `model.md` is the live record and states the opposite, and **nothing has reconciled them.** The finding is the winner on standing; the contradiction is unresolved in the corpus. Not adjudicated here.

### X2. The portal screenshot's primacy - stated categorically live, corrected here, correction never applied

**The finding**, `read-cycle.md` §7 lines 273-277, which flags its own status:

> **A live correction to a registry entry**, made by the load and **not yet applied**: the registry carries *"the portal screenshot is ring 0's PRIMARY source"*, generalised from 2c03. **2aa4's handouts carry their own due dates.** The ruling holds for `status`, `score` and evaluation state everywhere and for `due` in 2c03; *"the deadline is never in the obligation's own material"* is **course-specific, not categorical**.

**The standing record**, `domain/model.md` §10 item 7 (lines 663-666): "The portal screenshot is not an enrichment path for ring 0 — it is the primary one, and the handouts are primary only for `requires` and `spec`. Design §10.7's screenshot ruling is upgraded from convenience to dependency." Still categorical. `archive/build-plan-2026-08-27.md` line 334 repeats the categorical form.

**"Not yet applied" is still true**, three days and one tier-recut later. The finding is the winner; the live record is unamended. The archive sweep's X5 is confirmed - and note that under the correction the unrestricted residue is empty, because `status`, `score` and evaluation state are all graveyarded by `spec/schema.md` §7.

### X3. `progress.state`'s default - already reconciled, recorded for completeness

`read-cycle.md` §4 line 170 observes "**The ordinal invited invention** — one run asserted `'not started'` over five items with no progress record at all, with no rule in force that said it could." The boxed note beneath it (lines 171-175) records that the rule it was judged against was overturned 2026-08-28 by `spec/schema.md` §4.5, that "the observation is unaffected", and that the line must not be cited as authority for the gone rule. Billy's 2026-08-30 ruling 4 confirms the schema side. **A finding and a later ruling pointing different ways, correctly handled in place.** No action; recorded because it is the corpus's one worked example of the pattern.

### X4. The null result against Billy's ruling 2 - not a contradiction, an obsolescence

Covered in the first section. §2 and §4 measured *the plan does not become an allocation*; ruling 2 removes that as a requirement. The measurement stands and its criterion is gone. Neither is the loser.

---

## The four claims handed over from the archive sweep

`research/12-archive-sweep.md` line 164 named O1, O2, X5 and the registry 42-45/67 row as bounded by not having read `records/findings/`. Resolved:

| claim | homed here? |
|---|---|
| **O1** - the owed experiment ("vary what the agent must DO, not what it can SEE") and the two suspects (sizing, the absence of an allocation procedure) | **YES, fully.** `read-cycle.md` §2 lines 101-106 carries both, in the same words: "the cause lies in **sizing** or in **the absence of an allocation procedure**, and nowhere else in the observation space" and "**The next experiment must vary what the agent must DO, not what it can SEE.** … The attempt is owed again, on uncontaminated runs." It also carries the E8/E9 history the registry compresses. **Not orphaned.** See Q1. |
| **O2** - the second apparatus repair: the faithfulness rubric does not check claims about the agent's own actions, which `calls.jsonl` can check exactly | **HALF.** The *measurement* and the *rule* are here in full - §5 lines 224-231 and Caveats §8 lines 379-388, "**`calls.jsonl` is the only trustworthy record of behaviour** … Any claim resting on a run *saying* it did something is void." The *owed repair* - extend the rubric - is **not** stated here as owed. It exists only in `archive/slice-1-plan-2026-08-27.md` §8, which is frozen and whose carrier `spec/architecture.md` §4 voided. **Half-orphaned: the evidence has a live home, the task does not.** See Q3. |
| **X5** - the portal screenshot's primacy corrected from categorical to course-specific | **YES, verbatim, and the finding flags itself as unapplied.** `read-cycle.md` §7 lines 273-277. **Not orphaned** - and the contradiction with `domain/model.md` §10 item 7 that the archive sweep suspected is real and open. See X2. |
| **registry 42-45 and 67** - cost probe, vendor property, long reference works and `pack()`, PNG container, the read-side gate | **THREE OF FIVE, and the two misses matter.** **Entry 42** (`claude-sonnet-5` + native passthrough, optimisation deferred) → `ingestion-probe.md` "The ruling". **Entry 43** (vendor property, 2.67x, 3.51x tokenisation) → "What it gets wrong". **Entry 45** (PNG container, request bytes, 25.0 MB / 78% / 413s / 37 pages / seven decks) → "The container". **Entry 44** (long reference works out of scope - the 738-page textbook, the 118-page manual - which is what makes `pack()` the identity function and retires section-truncation) is **NOT in either file**, and appears nowhere in `domain/`, `spec/` or `plan/`. **Entry 67** (the read-side gate) is carried in substance by `read-cycle.md` §2 but **not as a gate** - the "gated-on" framing that makes it a live conditional is registry-only. |

**So: entry 44 is homeless and must be said to be.** Its only statement in the corpus is `archive/openclaw-registry-2026-08-25.md` entry 44 (frozen), whose own ref points at the cost-probe `FINDINGS.md` in openclaw. It carries a `[R]` Billy ruling (08-23) and a revisit-condition ("the artifact layer needs an 'indexes the whole course' node type", pointing at `model.md` §10 item 1's owed item, which **is** live at `domain/model.md` line 630). **Destination: deferral issue**, precondition **the artifact layer needs an "indexes the whole course" node type** - the same precondition `model.md` §10 item 1 already carries, so the two should be one issue.

---

## Coverage

**Read whole:** `records/findings/read-cycle.md` (401 lines, all nine sections plus eight Caveats plus the changelog) and `records/findings/ingestion-probe.md` (43 lines). No section of either was skipped or skimmed; the scope sentences, the boxed corrections and the changelogs were read as content rather than as furniture, which is the specific failure the file itself records at §0 lines 52-56.

**Read for citation-checking:** all of `records/domain/` (2 files, 1,508 lines), `records/spec/` (5 files, 941 lines), `records/plan/` (3 files, 364 lines) and `records/archive/` (4 files, 1,168 lines) - by targeted grep plus full reads of `spec/ring-0.md` (104 lines, the only record that cites `findings/` by path) and the cited passages of `domain/model.md` §10, `domain/domain-design.md` §1/§2/§9.1/§9.2, `spec/schema.md` §4/§4.5/§7 and `archive/openclaw-registry-2026-08-25.md` entries 40-71.

**Read in this repo:** `research/12-archive-sweep.md`, to recover the four handed-over claims.

**Not read, and it bounds nothing in this report:** `records/evidence/`, every `openclaw:` path, every other repository, `app/` source. Both findings files declare their own raw runs unauditable from this checkout, so no claim below the level of "the record says X" was available to verify from any boundary I could have been given. Where a figure's provenance matters I quoted the record's own statement of its standing rather than asserting the figure.

**What I did not do.** I did not adjudicate whether the null result stands - the first section reports what was measured, on what instrument, at what scope, and where the citations diverge, and stops there. I did not create anything but this file.

**Empty sections, stated plainly.** None. Every section found material; the thinnest is *Contradictions*, at four items of which one is already reconciled and one is an obsolescence rather than a conflict.
