# Origin survey - the 2026-08-21 session log and the 2026-08-22 modeling PLAN

**What this is.** A first-hand read of the two oldest readable documents in the fall26 design effort, an audit of three secondhand purpose-claims recorded in `research/03-openclaw-origin-survey.md`, and a plain statement of what `PLAN.md` asserts. It feeds a wayfinder map. It is **not** a summary of conclusions and nothing here is a ruling.

**What I read, in full, and nothing else:**

- `/Users/billywu/Documents/Projects/openclaw/log/2026-08-21-fall26-domain-design.md` - 141 lines, 1,471 words, 9,977 bytes.
- `/Users/billywu/Documents/Projects/openclaw/fall26/2026-08-22-modeling/PLAN.md` - 120 lines, 1,191 words, 7,175 bytes.
- `/Users/billywu/Documents/Projects/semester-manager/research/03-openclaw-origin-survey.md`, for the citations under audit only.

**Boundary observed.** No other file under `/Users/billywu/Documents/Projects/openclaw/` or `/Users/billywu/Documents/Projects/fall26/` was read, listed, grepped or opened. Where a claim below required a file outside that boundary, I have marked it unreadable rather than fetched it.

---

## Finding zero, which reframes the whole ticket: this is not the design doc

The ticket calls `log/2026-08-21-fall26-domain-design.md` "the design doc". It is not. It is the **session log** for the design session, and it says so twice.

- Its own header: "**Session type:** design (no code)… **Artifacts:** `devlog/ideas/2026-08-21-fall26-domain-design.md` (design of record) · `docs/superpowers/specs/2026-08-21-fall26-build-spec.md` (plan of record). **Read the design doc for the design.** This log carries the day's arc - what was proposed, corrected and reversed - which is the part the design doc deliberately does not narrate." (log, header)
- Its `## Cross-links`: "Design of record: `devlog/ideas/2026-08-21-fall26-domain-design.md`".

The design of record has the **identical basename** and differs only by directory (`devlog/ideas/` vs `log/`). That collision is the most likely cause of the ticket's premise. The design of record is outside my boundary and I did not read it.

**Consequence for jobs one and two.** Every `§N` citation in `03-openclaw-origin-survey.md` (design §2, §4, §5, §6, §9, §10, §10.7) points at the design of record, not at this log. The log contains **no `§`-numbered sections of its own**; a search for `§` in it returns exactly one hit, `§1`, and that is a cross-link to a *third* document (`devlog/ideas/2026-06-23-domain-definition-contract.md` §1). So no citation of the form "design §N" can be ruled faithful or distorted against this file directly. What this log does contain is the **same session's narration of the same decisions**, which lets me test the citations for *substance* even though I cannot test them for *text*. That is what the audit below does, and each ruling says which of the two it is.

**Voice, up front.** The log is written entirely in an agent's voice, narrating Billy in the third person. It contains **two verbatim quotations of Billy in 1,471 words**: `"you cannot write the relationships today"` (§Key decisions) and `"大概率"` (§Open threads). Eleven further items carry explicit `(Billy)` / "Billy rejected" / "Billy refuted" attribution, but in the agent's paraphrase, not his words. `PLAN.md` contains **zero** Billy attributions and zero Billy quotations. Details in §Coverage.

---

## First-hand intent

Voice is marked on every item: **[Billy verbatim]** = his words in quotation marks in the source; **[Billy attributed]** = the source names him as the author of the position but paraphrases it; **[agent]** = the drafting agent's own position or prior framing; **[unattributable]** = the source gives no marker and I will not guess.

### What Billy says the system is for

**1. INTENT - the goal function. [unattributable]**
*log §The reversals, in order, item 4.* Verbatim: "**The goal function was wrong.** Not reminders — Billy is rarely behind. It is that five concurrent courses produce a fear of not holding the whole picture, which drives repeated polling. Reading a notice is cheap; *interpreting* it forces a full context reload. Collapsing five reloads into one is the product."

**This is the single highest-value passage in the file and its voice cannot be determined.** Item 4 is the only entry in an eleven-item list of corrections that carries **no** attribution marker, while items 2, 3, 6, 7, 8 and 11 are each tagged `(Billy)` and items 5, 9, 10 name him in the prose ("Billy rejected it", "Billy refuted both", "Billy had already ruled out"). The list's preamble does say the session was "almost entirely **Billy correcting the agent's framing**" (log §The arc), which makes Billy the likely author; the deliberate, consistent tagging of every other item makes the omission conspicuous rather than accidental. I am recording it as unattributable and flagging the omission, because guessing here would defeat the ticket.

**2. INTENT - what success means. [unattributable, same passage]** Success is stated as a *collapse of interpretation cost*, not as coverage, not as timeliness, not as never missing anything: "Collapsing five reloads into one is the product." The explicit non-goal in the same sentence is reminders, on the stated ground that "Billy is rarely behind."

**3. INTENT - the system declares nothing outward. [Billy attributed]**
*log §The reversals, item 5.* The agent had derived an auditable trust surface, "5 of 5 obligations held, last synced 10 min ago". "Billy rejected it: the system declares nothing outward." The log then supplies the agent's own self-incriminating evidence: the agent's draft "noted the assertion 'should be one boring line nobody reads', and separately that its manifest could go stale and lie confidently. A trust mechanism that can lie is net-negative."

**4. CONCLUSION - what the `manifest` field is for, after the rejection. [agent]** "The `manifest` field survived on a *different* justification: it makes answers complete ('A4 exists, not yet scheduled'), not because anything is reported." (log §reversals, item 5.) Completeness *of an answer given*, explicitly not a report volunteered.

### What a semester actually looks like to him

**5. INTENT - five concurrent courses, and the shape of the load. [unattributable]** *log §reversals, item 4.* "five concurrent courses produce a fear of not holding the whole picture, which drives repeated polling." The unit of pain is the **context reload**, and the asymmetry named is that reading is cheap and interpreting is not.

**6. INTENT - the two real course shapes, evidenced by screenshots. [Billy attributed]**
*log §reversals, item 9.* "Billy refuted both with two screenshots — a flat course (6 decks, 11 references, 8 assignments) and an engineering course whose weekly announcements point outward in four directions at a density no person can organise." This is the closest the corpus gets to Billy describing his semester in concrete terms, and it arrives as **evidence he produced**, not as prose he wrote.

**7. INTENT - he will not annotate by hand. [Billy attributed]** *log §reversals, item 10.* The structural-chunking design is justified because the heading "*becomes* the semantic group label with zero annotation — which Billy had already ruled out doing by hand."

**8. INTENT - he cannot specify the relationships in advance. [Billy verbatim]**
*log §Key decisions.* "…which is what answers Billy's **'you cannot write the relationships today'**." One of two verbatim Billy quotes in the file. It is a statement about the limits of his own foresight, and the rigidity rule is built as the answer to it.

**9. INTENT - his own failure mode, named by him. [Billy attributed]**
*log §reversals, item 7.* "**Asymmetric depth biases allocation** (Billy's failure mode, from live Fairy). A coordinator holding detail on one course and one line on another over-weights the first, because visible work masquerades as important work." Note the source of the observation: it is drawn from watching a live system, not from introspection.

**10. INTENT - the deadline-moves example, as the thing one store cannot hold. [unattributable]** *log §reversals, item 1.* "after a deadline moves, the spec PDF still says Wednesday and is *not wrong* — it is evidence; the fact says Friday and is *also not wrong*." Item 1 carries no `(Billy)` tag; by the same tagging logic as item 4, its voice is undetermined.

### What he rejected, and the reason he gave

Every rejection below is tagged with the marker the log itself uses.

**11. INTENT - "sync" as the model. [Billy attributed, explicit `(Billy)` tag]** *log §reversals, item 2.* "**'Sync' was the wrong model** (Billy). Not a system kept aligned with a remote — a KB that accumulates. Killed full re-reads, diffing, mirror state."

**12. INTENT - ingestion, out of scope. [Billy attributed, explicit `(Billy)` tag]** *log §reversals, item 3.* "**Ingestion is out of scope** (Billy). He is the fetcher; the system's boundary starts at the endpoint." Reason given, in the agent's framing of the consequence: it "moved the trust requirement from *coverage of the world* (unsolvable) to *completeness of recall* (mechanical)." It "retired an entire branch the agent had built over two rounds (source registries, coverage guarantees, scraping)."

**13. INTENT - the completeness-assertion layer. [Billy attributed]** Item 3 above. Reason: "the system declares nothing outward", reinforced by "a trust mechanism that can lie is net-negative."

**14. INTENT - boot-time assembly of the coordinator. [Billy attributed, explicit `(Billy)` tag]** *log §reversals, item 6.* "**The coordinator is long-running, not booted per session** (Billy). The agent's two-stage assembly-at-boot model died; the *projection* survived, restated as a standing constraint — fixed shape, uniform depth, never deepens."

**15. INTENT - "test routing quality" as Step 0's verb. [Billy attributed, explicit `(Billy)` tag]** *log §reversals, item 8.* "**Step 0 as 'test routing quality' was refuted** (Billy): with no contract, there is no target to route to. The material stays the input but the verb changes from *test* to **induct** — derive the operation set from ~50 real announcements."

**16. INTENT - the agent's invented numeric health thresholds. [Billy attributed, same item]** "the agent had invented numeric thresholds ('6 good, 30 bad'); replaced with a structural one (every operation must reduce to insert/rewrite/file over the five fact types)."

**17. INTENT - deferring embeddings, and gating them on failure-to-find. [Billy attributed]** *log §reversals, item 9.* "The agent had scheduled storage as a week-3 afterthought and gated embeddings on failure-to-find. Billy refuted both." The sharper correction, whose exact voice the log does not mark: "**the embedding threshold is not 'cannot find' but 'reduce the cost of finding'** — a located 50-page PDF is still a haystack, and full extraction every time is neither cheap nor reliable."

**18. INTENT - deferring the build to post-launch. [Billy attributed, explicit `(Billy)` tag]** *log §reversals, item 11.* "**Build it all before the semester** (Billy), embeddings included, against the agent's proposal to defer them to the first post-launch month. Reason: the semester brings more work, and the time for end-to-end validation exists now."

**19. INTENT - the Supabase credential rotation, ruled out of existence. [Billy attributed]** *log §Standup half.* "the third (Supabase rotation) verified still open and then **ruled out of existence** by Billy — the exposed credential stays in use knowingly." Recorded because it is an explicit ruling with an attribution marker, per the ticket. No reason is given in the log beyond "knowingly".

**20. INTENT - a false `done` is a corruption. [unattributable]** *log §Standup half.* Four past-due todos were set "**`dropped`, not `done`**: they were never executed, and a false `done` corrupts the work-trace the PA layer exists to keep honest." No attribution marker. This is the same integrity principle that drives item 3's rejection of a trust surface that can lie, but I am not asserting they share an author.

### Explicit rulings and deferrals, with their markers

**21. INTENT - three rulings deferred by name. [Billy attributed]** *log §Open threads.* "**Three rulings before W1:** Notion projection vs authority · own tables vs reusing PA's `todos` · where `workload` estimates come from. Billy deferred all three to when the build reaches them." *(These three are recorded as ruled on 08-22 in `PLAN.md` §Settled - see §Contradictions item 5.)*

**22. INTENT - coordinator location, a tilt and not a ruling. [Billy verbatim, partially]** *log §Open threads.* "**Coordinator location** — a CC session in a dedicated fall26 directory (Billy's tilt, '大概率', not hard-ruled)." The second and last verbatim Billy quote in the file. The log is careful to mark it as a leaning, not a decision.

**23. INTENT - the capture-point question the dispatch actually asked. [agent]** *log §The capture-point finding.* "**It was never a problem with the ritual. It was a problem with the material.**" `/wrap` "fits **slow + self-authored** material… fall26's *facts* are externally-originated and time-critical, satisfying neither, so they need at-the-moment capture." Bolded and framed as a finding; no Billy marker anywhere in the section.

**24. INTENT - Billy asked for a verification pass. [Billy attributed]** *log §Self-review of the spec.* "Billy asked for a verification pass. Six defects found and fixed in place." The act is his; the six findings are the agent's.

---

## Citation audit

`research/03-openclaw-origin-survey.md` §"The goal function, as this corpus reports it secondhand" (lines 38-44) records three purpose-claims it could not verify. All three cite `design §N`, which as established in §Finding zero lives in `devlog/ideas/2026-08-21-fall26-domain-design.md`, **outside my boundary**. So each ruling below has two parts: a **textual** ruling (can the quoted text be found in what I read) and a **substantive** ruling (does the same session's narration of the same decision support the claim).

### Citation 1 - "'what should I be studying' is exactly the anxiety this is built to remove"

*Cited by 03-survey line 42, from `agents/2c03-obligations-and-edges.md` J1, to "design §2's goal function".*

**Textual ruling: ABSENT.** Neither file I read contains a `§2`, the string "anxiety", or the string "what should I be studying". Verified by search across both files.

**Substantive ruling: DISTORTED, in a specific and traceable way.** The one place either file states a goal function is log §reversals item 4, quoted in full: "It is that five concurrent courses produce a fear of not holding the whole picture, which drives repeated polling. Reading a notice is cheap; *interpreting* it forces a full context reload. Collapsing five reloads into one is the product."

Two substitutions have happened between that text and the citation:

1. **"fear of not holding the whole picture" → "anxiety".** Defensible as a paraphrase in register, but it drops the object. The log's fear is about **holding a complete picture**; "anxiety" unqualified is about a state of mind. The narrower reading is the load-bearing one, because it is what makes *completeness of recall* (item 12) the trust requirement.
2. **"repeated polling / context reload" → "what should I be studying".** This is the substantive drift. The log names the driven behaviour as **polling** and the product as **collapsing five reloads into one**: an *interpretation-cost* problem. "What should I be studying" is a *prioritization* query, which is a different question with a different answer shape. The log's goal function does not ask the system to rank Billy's work; it asks the system to let him reload context once instead of five times.

The claim may still be faithful to design §2, which I cannot read and which may say more than the log narrates. What I can say is that **the log's version of the goal function does not contain it**, and that the substitution from reload-collapse to study-prioritization is the exact step at which a summary would start pointing at a different product.

### Citation 2 - "a KB whose stated purpose is anxiety removal"

*Cited by 03-survey line 43, from `agents/2aa4-tutorials-assignments-artifacts.md`, as the doc's stated purpose.*

**Textual ruling: ABSENT.** The string "anxiety" does not occur in either file. Neither does "anxiety removal" in any form.

**Substantive ruling: ABSENT as a stated purpose; at best a downstream coinage.** The only purpose statement in either file is "Collapsing five reloads into one is the product" (log §reversals item 4). "Anxiety removal" is a re-description of the *motivation* named one clause earlier ("a fear of not holding the whole picture"), promoted to being the *purpose*. Those are different roles: the log makes the fear the **diagnosis** and the reload-collapse the **product**. A downstream agent using "anxiety removal" as the stated purpose is treating a symptom description as a spec, and it is doing so in the phrase that then licenses "the single most obviously-wanted query" - a conclusion about what to build, resting on a purpose the source never states in those terms.

I want to be precise about the limit here: this is **not** evidence that the purpose is wrong, only that this file does not state it that way. If design §2 uses the word, the citation is faithful and this note is moot. That is checkable in one read of a file I was not permitted to open.

### Citation 3 - "the allocation planner - the thing design §10.7 ruling 4 names as the product", and "surface details Billy does not know to ask about"

*Cited by 03-survey line 44, from `agents/2c03-obligations-and-edges.md` J5 and J7.*

**Part A, "the allocation planner" as a real named thing: FAITHFUL, and dated.** `PLAN.md` §What this cycle is uses the term as settled vocabulary: "On 08-22 §6's scope was cut — the five types went from *the destination of all inbound* to *only what the allocation planner reads*". So by 2026-08-22 the allocation planner exists in the design vocabulary and is the named consumer of the five fact types.

**Part B, the 08-21 log does not know the term. [contradiction, surfaced not resolved]** The string "allocation planner" does not appear in the log at all. "Allocation" appears exactly once, in log §reversals item 7, and there it is a **failure mode being guarded against**, not a product: "Asymmetric depth biases allocation (Billy's failure mode…)". On 08-21 the product is named as reload-collapse; by 08-22 the product is being referred to as the allocation planner. I record both and adjudicate neither.

**Part C, "§10.7 ruling 4 names it as the product": UNVERIFIABLE HERE, and in tension with the only enumeration of §10.7 I can read.** `PLAN.md` §Settled - do not re-litigate enumerates them: "**The five rulings of 08-22** (design §10.7) — inbound is to be known, not to trigger an action · corrections are sticky notes, not applied overwrites · RAG stores `slides / pdf / textbook`-class sources only · this is not an enterprise RAG · live intake is a pasted screenshot, so the endpoint is multimodal."

Counting that list, **ruling 4 is "this is not an enterprise RAG"**, which names nothing as the product. Two caveats I will not paper over: `PLAN.md`'s bullet order is not stated to be §10.7's numbering, and a compressed restatement may reorder. But the discrepancy is real enough to record, and it is cheap to settle: read design §10.7 and count. Note also that `03-survey` itself uses "§10.7 ruling 4" for a *third* thing at its line 293, where the sticky-note class that "most directly serves design §10.7 ruling 4" is the corpus disagreeing with itself - which fits ruling 2 ("corrections are sticky notes") better than either candidate for ruling 4. **The reference "§10.7 ruling 4" is being used inconsistently across the secondhand corpus.**

**Part D, "surface details Billy does not know to ask about": ABSENT, and in direct tension with a ruling I can read.** The phrase and the concept appear nowhere in either file. The nearest adjacent text is the `manifest` justification at log §reversals item 5: "it makes answers complete ('A4 exists, not yet scheduled'), **not because anything is reported**." That is answer-completeness on a question asked, and the same item records Billy's rejection of the alternative: "**the system declares nothing outward**." A system that surfaces details Billy does not know to ask about is, on its face, a system that declares something outward. I am not ruling that the two are incompatible - the design of record may reconcile them and the distinction may be exactly "in the answer, not unprompted". I am recording that **the citation's phrasing points the opposite way from the one ruling in this file that most nearly governs it**, and that this is worth Billy's eye.

### Audit summary

| # | Claim | Textual | Substantive |
|---|---|---|---|
| 1 | "what should I be studying" = the anxiety | **absent** | **distorted** - source names polling/reload-collapse, not prioritization |
| 2 | stated purpose = anxiety removal | **absent** | **absent** - source states the product as reload-collapse; anxiety is the diagnosis, not the purpose |
| 3A | "allocation planner" is real vocabulary | **faithful** (PLAN.md §What this cycle is) | faithful, from 08-22 onward |
| 3B | it is *the product* | **absent from 08-21 log** | conflicts with log's named product |
| 3C | "§10.7 ruling 4 names" it | **unverifiable**; PLAN.md's 4th bullet is "not an enterprise RAG" | reference used inconsistently across the corpus |
| 3D | "surface details Billy does not know to ask about" | **absent** | in tension with "the system declares nothing outward" |

**One structural note on all three.** All three claims originate in the same two `derivation/agents/` files (`2c03-obligations-and-edges.md`, `2aa4-tutorials-...md`) and all three cite the design of record. None of them quotes Billy. The chain is: Billy → design of record (agent-drafted, one verbatim quote of him per ~700 words in the parallel log) → derivation agent → `03-survey` → here. **The word "anxiety" enters that chain at the derivation-agent link at the earliest**, since it is in neither 08-21 nor 08-22 document I can read.

---

## What §10 says

**Direct answer: the file I read has no §10, and no `§`-numbered sections at all.** A search for `§` in `log/2026-08-21-fall26-domain-design.md` returns one hit, `§1`, at line 140, and it is a pointer to a different document: "Originating dispatch's own ruling context: `devlog/ideas/2026-06-23-domain-definition-contract.md` (§1 premise now superseded — header added this session)."

**What §10 is, secondhand from `PLAN.md`, which I can read.** The §10 the other record points at belongs to the **design of record**, `devlog/ideas/2026-08-21-fall26-domain-design.md`. Three things in `PLAN.md` establish its role:

1. *`PLAN.md` §Inputs.* "Design of record + what 08-22 changed: `devlog/ideas/2026-08-21-fall26-domain-design.md`, **§10 first**." The bolded "§10 first" and the framing "+ what 08-22 changed" together identify **§10 as the section where the 08-22 empirical cycle's results were written back into the 08-21 design doc**. It is an amendment section appended to an older document, which is why a reader is told to start there.
2. *`PLAN.md` §Settled.* "**The five rulings of 08-22** (design §10.7)" - so §10 has at least seven subsections and §10.7 carries the five rulings, listed verbatim in §Citation audit part C above.
3. *`PLAN.md` §What this cycle is.* What 08-22 did to the design: "the shape met 132 real announcements and real PDFs | **half of it did not survive**", and specifically "On 08-21 this cycle did not need to exist: design §6 *was* the model, five fact types with their fields listed, and W1 was transcription. On 08-22 §6's scope was cut — the five types went from *the destination of all inbound* to *only what the allocation planner reads* — and three entities appeared that §6 never had."

**On the two falsified propositions the other record asks about.** `PLAN.md` does not use the words "falsified" or "proposition", and it does not enumerate two of anything replaced. What it does record as changed by 08-22, and therefore as candidate content of §10, is: **(a)** §6's scope cut, from destination-of-all-inbound to what-the-allocation-planner-reads; **(b)** three new entities §6 never had, named at §Open, and owned here item 2 - "a correction attached to a document section · an announcement retained but not indexed · an announcement naming a document"; **(c)** **D1** restated as "retirement is read-time expiry, **~7:1** over write-time supersession", which puts a measured ratio on what the 08-21 log stated qualitatively as "**Retirement is a read-time predicate**, not a sweep". I am listing these as candidates because they are what `PLAN.md` says 08-22 changed. **I am not asserting they are the two propositions in question**, and I did not read §10. That thread stays unfinished, and one read of the design of record closes it.

---

## What PLAN.md asserts

`PLAN.md` is the entry document for the **modeling cycle**, dated 2026-08-22, "design cycle, not a probe. **Size: one day.**" Voice: **entirely agent-authored**. It contains no Billy attribution and no Billy quotation anywhere in 1,191 words. The one quoted passage is a quotation of design §4, not of Billy. For the corpus that scores its verdicts against "MODEL/PLAN", this is the PLAN half; per the ticket I did not look for the MODEL half and did not read it.

**A1. Its place in the sequence.** *§What this cycle is.* Four cycles: design (08-21) "reasoned a shape out of Billy's needs | shape produced"; empirical (08-22) "the shape met 132 real announcements and real PDFs | **half of it did not survive**"; modeling (this one) "turn what survived into entities, relations and a verb surface"; build "W1 storage+verbs · W2 ingestion+corpus · W3 coordinator+replay". **This is the load-bearing assertion for the age rule**: the cycle immediately after the design doc records that half the design doc did not survive contact with data.

**A2. Why the cycle exists at all.** *§What this cycle is.* "On 08-21 this cycle did not need to exist: design §6 *was* the model… So the position between 'we know what the material demands' and 'we write the DDL' is now empty, and this cycle fills it."

**A3. Three questions, and only three.** *§What it is responsible for.* **(1) What things exist** - "A course. An assignment with a deadline. A document. A piece of a document. A correction stuck onto that piece. An announcement kept as a receipt. Those nouns, and what each one holds." **(2) What the system already knows without going to look** - "Ask 'what is week 7 about' — some of the answer is on hand, the rest is fetched. **Where that line sits is the hardest and most important decision in this cycle**, because it is the boundary between the two layers, and once it is drawn the answer to question 1 follows from it." **(3) Who can touch what** - "The coordinator reads the summary and writes plans, nothing else. Ingestion writes. Deep-read searches… the coordinator stays pure because it does not *have* the other tools."

**A4. The cost curve that justifies the cycle.** *§Why it is the load-bearing layer.* "Answer them once here and the three weeks become transcription instead of decide-while-building. Get them wrong and W1 builds the wrong tables, W2 pours material into the wrong shape, and W3 hands the coordinator the wrong tools — **with the cost of the fix roughly doubling each week**, and no time left to pay it by W3."

**A5. The acceptance test.** *§Acceptance.* "**The output must be transcribable, not merely coherent.** If a load-bearing place still reads 'and then the agent works it out', the cycle is not done."

**A6. Explicit non-scope.** *§Explicitly NOT this cycle.* The corpus pipeline's internals ("pass granularity, chunking parameters, embedding choice… decided in W2"); the coordinator's behaviour or prompting ("design §9 settled its shape"); "**Anything the rigidity rule defers.** No mechanism reads it, it does not get modelled."

**A7. Its own declared failure mode, and its own declared weakness.** *§This cycle's own failure mode.* "**Over-modelling.** Completing the model is satisfying and mostly wrong." And, importantly for anyone scoring verdicts against this document: "**this cycle has no external adjudicator.** The empirical cycle was judged by data; this one is judged by Billy and the agent alone, so **everything it produces is an assertion until W1/W2 test it**. That argues for the smallest model that could work, and for finishing fast."

**A8. What it declares settled and closed to re-litigation.** *§Settled - do not re-litigate.* Verbatim list: design **§2 the goal function** - "It has now judged §3, §4 and several agent drafts. It is the standard"; **§5** - "no fold; course ≠ domain; coupling through the store, never a call"; **§9** - "coordinator purity enforced by tool surface; disposability as the acceptance test; uniform-depth projection across all courses"; **§6's rigidity rule** - "a field is typed iff a mechanism reads it. The *rule*, not the old type list"; **the three build-spec §7 decisions, ruled 08-22** - "Notion is a projection; fall26 gets its own Postgres schema and its own MCP; `workload` is stated by Billy, nullable, never defaulted"; **the five rulings of 08-22 (design §10.7)**, quoted in full in the citation audit; **D1** - "retirement is read-time expiry, ~7:1 over write-time supersession".

**A9. What it holds open and owns.** *§Open, and owned here.* Four items: the surface (question 2), "**The keystone; everything else waits on it**"; the entity model across both layers including the three new 08-22 entities; the verb partition by consumer; and **design §4's unanswered counter-argument**, quoted here because it is the sharpest open objection in either file - that storing-and-tagging leaves "due Wednesday" and "moved to Friday" coexisting for the LLM to reconcile at read time, which *"relocates Billy's uncertainty into the system while making it look handled"*. "The agent's position is that this holds for an unbounded pile and fails for a scoped, time-ordered set. **Answer it or accept the risk explicitly; do not pass over it.**"

**A10. What it explicitly pushes out of its own path.** *§Open, but not here.* **P7**, "whether one multimodal pass produces usable structure from the real material… The last unrun piece of Step 0". `PLAN.md` records reversing an earlier claim about it: "An earlier draft claimed it constrained the entity model, on the grounds that corrections need a section to attach to. That was wrong: whether a correction attaches to a whole document or to one section is a granularity parameter on a relation, not a structural difference." Fallback if structure extraction fails: "retrieval falls back to whole-document plus course/week metadata, which costs precision and changes nothing here."

**A11. Its inputs.** *§Inputs.* The design of record "**§10 first**"; the build spec "**§9 first**"; and evidence at `fall26/2026-08-22-step-minus-1/FINDINGS.md`. All three are outside my boundary and unread.

---

## Conclusions reached here

Per the age rule: **these are what these two documents concluded on 2026-08-21 and 2026-08-22.** They are the least credible material in the corpus, because `PLAN.md` itself records that half of the 08-21 shape "did not survive" contact with 132 real announcements one day later, and because two further weeks of work I cannot see followed. Nothing below is a statement of what is true now.

**C1. [agent, log §reversals item 1]** The knowledge base splits into a **facts layer** ("tiny, CRUD, authoritative for *what is true now*") and a **corpus layer** ("large, append+supersede, authoritative for *what the source said*"). Rationale is the moved-deadline example at intent item 10: "One store forces a choice between falsifying history and holding stale facts."

**C2. [unattributable, log §Key decisions]** "Two layers + provenance link; **only the facts layer may be rewritten**, everything else append-only or read-only. Every pathology met this session is an instance of violating that one rule." *Status note: `PLAN.md` §Open item 2 records that 08-22 added three entities the 08-21 model never had, so the entity set this rule ranges over changed within a day.*

**C3. [unattributable, log §Key decisions]** "Routing at the endpoint between **insert** and **rewrite**; rewrites come only from announcements and from new versions of obligation-bearing documents; only rewrites are confirmed (~30/semester), and the confirmation presents the *resolved target*, not a yes/no." *Status: `PLAN.md` §Open item 4 records design §4's counter-argument to this mechanism as still unanswered on 08-22.*

**C4. [unattributable, log §Key decisions]** "**Retirement is a read-time predicate**, not a sweep — nothing runs, nothing cleans." *Status: survives to 08-22 as D1, quantified: "read-time expiry, ~7:1 over write-time supersession" (`PLAN.md` §Settled).*

**C5. [unattributable, log §Key decisions; answers a Billy-verbatim objection]** "**Rigidity rule:** a field is typed *iff* a mechanism reads it. Deferring schema decisions is therefore free… No relationship graph: relationships are inferred at read time, affordable because the layer fits." *Status: survives to 08-22 explicitly and narrowly - "**§6's rigidity rule** — … The *rule*, not the old type list" (`PLAN.md` §Settled). The rule lived; the five-type list it was attached to was cut the next day.*

**C6. [unattributable, log §Key decisions]** "**Coordinator purity is enforced at the tool surface**, not by instruction… with **disposability** as the acceptance criterion: losing the session must lose nothing." *Status: survives verbatim to 08-22 as settled §9 (`PLAN.md` §Settled).*

**C7. [agent, log §The capture-point finding]** "`/wrap` fits **slow + self-authored** material… fall26's *facts* are externally-originated and time-critical, satisfying neither, so they need at-the-moment capture. fall26's *preferences* satisfy both, and keep the ritual." Self-limited in the same section: the yield/value inversion that motivated the doubt is "Not fixed by this finding, and still live".

**C8. [agent, log §reversals item 10]** Grouped retrieval by the document's own structure, "so the heading *becomes* the semantic group label with zero annotation". Groups nest "`course > week > file > section`". Claimed to dissolve the math-equation chunking worry: "structural units keep an equation with its own slide." *Status: `PLAN.md` §Explicitly NOT this cycle pushes chunking parameters to W2, and §Open, but not here records that the multimodal pass which would validate structure extraction (P7) was **still unrun** on 08-22.*

**C9. [agent, log §Self-review of the spec]** Six defects found in the build spec and fixed in place; the two named worst are that "**Syllabus ingestion was missing entirely** — yet `manifest` has no other source, and the replay acceptance test checks against the manifest", and that the historical announcement export "was filed as a risk while Step 0 was still scheduled first — self-contradictory, since Step 0 consumes that export. Promoted to Step -1."

**C10. [agent, `PLAN.md` §Settled]** The three rulings Billy deferred on 08-21 (intent item 21) are recorded as **ruled on 08-22**: "Notion is a projection; fall26 gets its own Postgres schema and its own MCP; `workload` is stated by Billy, nullable, never defaulted." `PLAN.md` gives no attribution for who ruled them.

**C11. [agent, `PLAN.md` §Settled]** The five rulings of 08-22, quoted verbatim in the citation audit part C. Recorded here as conclusions of that date, with the numbering caveat noted there.

---

## Contradictions

Surfaced, not resolved. Adjudication is Billy's.

**X1. The file identity.** The ticket, and by inference the wayfinder map, treats `log/2026-08-21-fall26-domain-design.md` as the design doc. The file's own header and cross-links name `devlog/ideas/2026-08-21-fall26-domain-design.md` as the design of record and this file as the log of the day's arc. **Identical basename, different directory.** Every `design §N` citation in `03-openclaw-origin-survey.md` resolves to the unread file, which means `03-survey`'s §20 coverage gap (its line 394, "Same for `design §N` and `build spec §N`… The design's goal function, §4's insert-vs-rewrite mechanism, §10.7's rulings, and D1/D2's original statements all live there") is **still open after this survey**, not closed by it.

**X2. Two different things are called "the product", one day apart.** 08-21: "Collapsing five reloads into one is the product" (log §reversals item 4). 08-22 and after: the allocation planner is what the design's five fact types now serve (`PLAN.md` §What this cycle is), and the secondhand corpus calls it "the thing design §10.7 ruling 4 names as the product" (`03-survey` line 44). Whether the second replaced, refined or merely re-named the first is not determinable from these two files.

**X3. "The system declares nothing outward" vs "surface details Billy does not know to ask about."** Log §reversals item 5 records the first as Billy's rejection of a built-and-demolished layer. The second is a derivation agent's framing of what the system is for. They may be reconcilable (in-answer completeness vs unprompted reporting; the `manifest` survived on exactly that distinction) but nothing in either file I read performs that reconciliation, and the citation's phrasing does not preserve it.

**X4. "§10.7 ruling 4" denotes at least two different things in the secondhand corpus.** `03-survey` line 44 has it naming the allocation planner as the product; line 293 has it as the ruling served by a sticky note arising from the corpus disagreeing with itself, which matches ruling 2 in `PLAN.md`'s list ("corrections are sticky notes, not applied overwrites"); and `PLAN.md`'s own fourth bullet is "this is not an enterprise RAG". At most one of these is right.

**X5. Three rulings recorded as deferred, then as settled, with no visible ruling event.** Log §Open threads: "Billy deferred all three to when the build reaches them." `PLAN.md` §Settled, one day later: "**The three build-spec §7 decisions, ruled 08-22**", with all three decided, under a heading that forbids re-litigating them. The build had not reached them - `PLAN.md` §What this cycle is places W1 two cycles away. Not necessarily wrong, but the deferral condition Billy set was not the condition under which they were ruled.

**X6. Build-it-all-before-the-semester vs the actual 08-22 deferral pattern.** Log §reversals item 11 records Billy overriding the agent's proposal to defer embeddings, on the reason that "the semester brings more work, and the time for end-to-end validation exists now." `PLAN.md` §Explicitly NOT this cycle defers "pass granularity, chunking parameters, embedding choice" to W2, and §Open, but not here records that P7, the one probe that would validate structure extraction end-to-end, is "**The last unrun piece of Step 0**". These are compatible as *scheduling* (W2 is still pre-semester) but they sit against the stated reason, which was about validating end-to-end while time exists.

**X7. Item 4's missing attribution, inside a rigorously attributed list.** Six of eleven reversals carry an explicit `(Billy)` tag and three more name him in the prose. Items 1 and 4 carry nothing. Item 4 is the goal function - the most-cited passage in the entire downstream corpus. Either the omission is meaningful (the goal-function reframing was the agent's, ratified by Billy) or it is an oversight in an otherwise careful document. **I cannot tell, and the choice changes who authored the project's purpose.**

**X8. A meta-contradiction the log itself records and resolved, worth keeping visible.** Log §Self-review lists among the fixed defects "a component table that pre-empted a ruling the same document listed as outstanding." The same failure mode - a downstream artifact treating an open question as settled - is what X5 and citations 1 and 2 look like from here. The corpus has caught this in itself before.

---

## Coverage

**Read in full:** the two approved files, and `research/03-openclaw-origin-survey.md` for the audited citations only.

**Not read, boundary observed:** everything else under `/Users/billywu/Documents/Projects/openclaw/` and `/Users/billywu/Documents/Projects/fall26/`. No directory listing, no grep, no glob was run against either tree beyond the two named files.

**Voice accounting, `log/2026-08-21-fall26-domain-design.md`** - 1,471 words, agent-authored throughout, third-person about Billy.

- **Verbatim Billy: 2 fragments.** "you cannot write the relationships today" (§Key decisions); "大概率" (§Open threads). Under 10 words combined, roughly **0.5% of the file**.
- **Explicitly attributed to Billy in paraphrase: 11 items.** `(Billy)` tag on reversals 2, 3, 6, 7, 8, 11; named in prose at reversals 5, 9, 10, at §Standup half ("ruled out of existence by Billy"), and at §Self-review ("Billy asked for a verification pass"). "Billy" appears 17 times total across the file.
- **Unattributable but decision-bearing: at least 4 passages**, including reversals 1 and 4, the whole of §Key decisions (six bullets, none carrying an attribution marker), and §The capture-point finding.
- **Explicitly the agent's own, quoted as being corrected: 6 fragments** - "5 of 5 obligations held, last synced 10 min ago", "should be one boring line nobody reads", "test routing quality", "6 good, 30 bad", "returns the right passage", "the ritual is wrong".

**Voice accounting, `PLAN.md`** - 1,191 words, **zero** Billy attributions, **zero** Billy quotations. Billy is named three times, always as an object of design ("reasoned a shape out of Billy's needs", "judged by Billy and the agent alone", "`workload` is stated by Billy"). Its one quoted passage quotes design §4, whose author is unknown to me.

**What this survey could not do, and what would close it.** Every `design §N` and `build spec §N` reference remains unverified, which is the same gap `03-survey` §20 recorded. The three citations audited above are ruled against the *session log's narration* of the same decisions, not against the cited text. **One read of `devlog/ideas/2026-08-21-fall26-domain-design.md` §2 and §10 would settle citations 1, 2 and 3C, and would close the unfinished §10 thread, in a single pass.** I did not do it, because it is outside the boundary set for this ticket.

**One term I could not source at all.** "Anxiety" appears in neither file. If design §2 does not use it either, then the project's most-repeated statement of purpose was coined downstream of every document that has a claim to stating it.
