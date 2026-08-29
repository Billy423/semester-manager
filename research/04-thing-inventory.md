# Thing inventory and conflict register - four surveys merged

**What this is.** One entry per concrete thing an ADR could be about, merged across all four surveys of the fall26 design corpus, plus a register of every conflict with a verdict, an escalation shortlist prepared for Billy, and a coverage statement. Nothing here is a ruling. Where a conflict needs Billy it is prepared, not answered.

**Inputs, cited throughout by shorthand.**

| tag | survey | slice it read |
|---|---|---|
| **S1** | `research/01-domain-records-survey.md` | `fall26/records/domain/` - `model.md` (709 lines), `domain-design.md` (799) |
| **S2** | `research/02-spec-records-survey.md` | `fall26/records/spec/` - `design.md`, `schema.md`, `write-rules.md`, `architecture.md`, `ring-0.md` (941 lines) |
| **S3** | `research/03-openclaw-origin-survey.md` | `openclaw:fall26/2026-08-22-step-minus-1/` and `2026-08-22-derivation/` (2,974 lines) |
| **S5** | `research/05-origin-design-doc-survey.md` | `openclaw:log/2026-08-21-fall26-domain-design.md` and `openclaw:fall26/2026-08-22-modeling/PLAN.md` |

Corpus files are cited directly - `domain-design.md §10.7`, `schema.md §4.5` - so a later reader can zoom without re-reading a survey. `domain/` = `fall26/records/domain/`; `spec/` = `fall26/records/spec/`.

## Merge rules in force

1. Newer date wins by default. Escalate where recency does not settle it or where the newer ruling looks wrong.
2. Older artifacts carry a heavier comparison burden; an early conclusion never stands merely because it was stated first and confidently.
3. A self-declared `dead` or `not ruled` is honoured. A self-declared `[R] ruled` is not, without comparison.
4. **Attribution density is not intent fidelity.** Ruled by Billy 2026-08-29: the openclaw material is his own words; those agents simply did not cite him the way the fall26 agents did. S3 and S5 both applied that discount and it does not stand. openclaw claims are weighed on content and date like anything else.
5. No corpus document is a reason to do something. It is evidence that a question was once asked and once answered.

## The four corrections applied to the inputs

**Correction 1 - S5's citation audit is VOID, and I verified why.** S5 audited three downstream purpose-citations against `openclaw:log/2026-08-21-fall26-domain-design.md` and concluded the design of record did not exist in scope. It did: it was imported to `domain/domain-design.md` on 2026-08-25 (S1 records the import line verbatim: "from `openclaw:devlog/ideas/2026-08-21-fall26-domain-design.md` on 2026-08-25"), and S1 read it in full. I zoomed `domain-design.md §10.7` to settle it. Ruling 4 reads verbatim:

> **This is not an enterprise RAG that answers every question precisely.** It is a personal knowledge base whose job is: remove the **anxiety** of not finding information · manage cross-course information in the background · **locate details Billy himself does not know about.**

So all three audited citations hold. "Anxiety" is in the design of record, at ruling **4**, in Billy's own numbered ruling list dated 2026-08-22. "Surface details Billy does not know to ask about" is ruling 4's third job. `§10.7 ruling 4` is used **consistently** by S3's agents. What is wrong is `PLAN.md`'s five-bullet restatement, whose ordering puts "not an enterprise RAG" fourth as a bare clause and drops the three jobs - which is the entire basis of S5's audit-summary rows 3C and 3D and of its contradictions X3 and X4. **S5's `## Citation audit` section, its audit summary table, and X1/X3/X4 are discarded.** What survives from S5 is carried into the inventory below: Billy's ingestion ruling, his verbatim "you cannot write the relationships today", the finding that `PLAN.md`'s enumerations are secondhand, and the 08-21 goal-function passage.

**Correction 2 - `model.md` is not frozen.** Its title says "frozen 2026-08-22"; its body carries `[R]` rulings dated 08-23, 08-24 and 08-28 and its changelog records edits on 08-25 and three on 08-28 (S1's D29). **Neither domain file is the standing one by position.** In several places `model.md` is the *later* record; in several others `domain-design.md` is. S3 and S5 both frame `MODEL.md`/`PLAN.md` as a fixed spine scored against - that framing predates the correction and is not carried forward. Every entry below dates per thing.

**Correction 3 - the changelogs do not cover the period.** They cover the 08-25 import housekeeping and the 08-28 corrections only. Everything decided 08-21 through 08-24 has its reasoning in in-place banners in the bodies. "Check the changelog" fails for half the period. Two rulings exist *only* in a changelog and in no body: the ±1-2 week window resolving to `today-7d .. today+14d` (`domain-design.md` changelog 08-28), and why `domain-design.md §6`'s table was flagged rather than rewritten. Both are re-homed below.

**Correction 4 - container drift is a second, orthogonal supersession axis.** Many rulings are properties of a human-operated CLI with a long-running resident coordinator process. The successor is a set of components an agent (Claude Code) uses. The records contain no test for this, because the container was not in question when they were written. Every thing it touches is marked **`⟂container`**. A `⟂container` mark says nothing about the thing's date-standing; it is a second axis and can invalidate a ruling that is perfectly current.

## What the clustering is by

**One entry per concrete thing - the unit an ADR would be about - merged by what it is, not by what it is called.** Every name a thing goes by is recorded in its `names` line. The clusters are cut by **what kind of question the thing answers**, not by source file, repo, or date:

- **A. Purpose and trust** - what the system is for and what it promises. 12 things.
- **B. Shape** - layers, node kinds, edges, the graph, the store. 27 things.
- **C. Fields and identity** - the per-field rulings and the graveyard. 26 things.
- **D. The observation contract** - ring 0, residency, what the coordinator may see. 15 things.
- **E. Inbound** - ingestion, announcements, operations, write rules, capture. 16 things.
- **F. The container** - tiers, language, packaging, surface, sessions, external systems. 18 things.

**114 things.** Cluster F is where things whose *whole content* is a container fact live; `⟂container` marks appear in every other cluster too, on things that have domain content and a container-bound mechanism.

Entry shape: **names** · what each source says with file/section/date/attribution · **standing** under the merge rules · **`⟂container`** if drift touches it. `→ Cn` cross-references the conflict register.

---

# Part I - The thing inventory

# Cluster A - Purpose and trust

## M1. The goal function

**Names:** "the goal function" (`domain-design.md §2`), "§2" throughout both domain files, "the standard" (`model.md §1`), "reload-collapse" (S5), "anxiety removal" (S3's agents), "the three jobs" (`domain-design.md §10.7` ruling 4). One thing, five names, two dated forms.

- **`openclaw:log/2026-08-21` §The reversals item 4, 2026-08-21, unattributed in a list where six of eleven items carry a `(Billy)` tag** (S5 items 1-2, 39, X7). Verbatim: "**The goal function was wrong.** Not reminders - Billy is rarely behind. It is that five concurrent courses produce a fear of not holding the whole picture, which drives repeated polling. Reading a notice is cheap; *interpreting* it forces a full context reload. **Collapsing five reloads into one is the product.**" Under rule 4 this is weighed on content and date: the session is described by its own log as "almost entirely Billy correcting the agent's framing", and the missing `(Billy)` tag is not a discount.
- **`domain-design.md §2`, 2026-08-21, "Corrected mid-session"** (S1 thing 1). The imported form of the same passage: two fears separated - *"did something new appear?"* (cheap, not the system's job) and *"do I hold the whole picture?"* (expensive, is the system's job). "The cost is not reading a notice; it is *interpreting* it… collapsing five of them into one is the product." No `[R]` on the section.
- **`domain-design.md §10.7` ruling 4, Billy, 2026-08-22, `[R]`** (S1 thing 4; verified by zoom). "**This is not an enterprise RAG that answers every question precisely.** It is a personal knowledge base whose job is: remove the anxiety of not finding information · manage cross-course information in the background · **locate details Billy himself does not know about.**"
- **`domain-design.md §10.4`, Billy, 2026-08-22** (S1 thing 1). "**§2 was never in question and is now the judge of everything else.** §2 was right; §3 and §4 were the wrong implementation of it."
- **`model.md §1`, Billy, 2026-08-22, `[R]`** (S1 thing 1). A **completion**, not a change: "dropped into an assignment's requirements he still has to model the requirements / tasks / topics himself, and helping with that is why the system exists." For unfamiliar material the reload is **first construction**, not recall - §2 described only the recall case. Consequence: "**the product is collapsing the reload, so modelling that does not reduce reload cost is out of scope.**"
- **`PLAN.md` §Settled, 2026-08-22, agent** (S5 A8). "design **§2 the goal function** - It has now judged §3, §4 and several agent drafts. It is the standard."
- **`derivation/agents/2c03-obligations-and-edges.md` J1/J5/J7, 2026-08-22, agent A3** (S3). Cites §2 and §10.7 ruling 4 as the anxiety this is built to remove and as the product. **Verified faithful** by the zoom above; S5's finding of distortion is void.

**Standing.** The 08-22 three-jobs form (`domain-design.md §10.7` ruling 4, Billy, `[R]`) is the current statement of the product; §2's 08-21 diagnosis is the reason it is the standard and both files say §2 survived everything; `model.md §1`'s completion (08-22) is additive. **Both dated forms belong in the register** - the shift from *interpretation-cost collapse* to *three jobs* is itself evidence about what the product is. → **C1** (seed 1).

**`⟂container`, qualified.** §2 itself is a fact about Billy and survives any container. The *unit* - a human's five reloads, a human's polling urge - is a human's reading act. In the plugin container the reload is an agent's context load, which is cheap in a way Billy's is not, so the anti-inflation test ("modelling that does not reduce reload cost is out of scope") has a different denominator. Flagged, not judged.

## M2. The trust clause, and faithfulness as its operational form

**Names:** "the trust clause", "completeness of recall over what Billy told it", "faithfulness".

- **`domain-design.md §2`, 2026-08-21, unattributed** (S1 thing 2). "the trust requirement moved from *coverage of the world* (unsolvable, and not the system's job now) to *completeness of recall over what Billy told it* (mechanically solvable)."
- **`openclaw:log/2026-08-21` §reversals item 3, Billy** (S5 item 12). The same move, and its cause: Billy's ingestion ruling "moved the trust requirement from *coverage of the world* (unsolvable) to *completeness of recall* (mechanical)". This is the first-hand record of *why* the clause has that shape.
- **`domain-design.md §2` `OPERATIONALISED` block, Billy, ruled 2026-08-23, written in 2026-08-24, `[R]`, verbatim** (S1 thing 2): "系统不会拒绝你问问题，改怎么使用是用户的 burden 而不是系统的。系统只需要保证回答对该回答的。" → "**Faithfulness is the system's burden; scope and usefulness are the user's.**" Operationally: every claim traceable to a held fact, no relevant held fact omitted, nothing invented.
- **Same block, the limit that travels with it.** "The 08-23 measurement graded 60 runs and found **zero omissions** - but at a scale where omission was **not possible rather than avoided**… **The precision-versus-recall framing that cycle used is void: the recall half of faithfulness was never loaded.**" A real test needs five courses, the skeleton in the denominator, and the corpus.
- **`model.md §8.1`, Billy, 2026-08-23, `[R]`** (S1 thing 2). "**not trusting the user is CONFLICT DETECTION, not verification.**" Response shape: "you told me this, the record says that - which holds?"
- **`schema.md §1`, 2026-08-28** (S2 T5). The `null` convention is justified by faithfulness: rendered as a default, a null `grade_share_conditional` "becomes an assertion that the stored share is a stated fact when no source said so - **measured as the largest single class of unfaithful claim**."
- **`ring-0.md §6`, 2026-08-28** (S2 T29). The number behind it: conditional weighting printed as a fixed number is 24 claims across 17 runs; with a bound restated as a point value, **29 of 77 unsupported-or-contradicted claims - 38% of every measured faithfulness failure**. Qualified in place: "**It has not been re-derived structurally**, which `CAVEATS.md` §7 asks for before any metric in that folder is trusted."

**Standing.** Current on every axis. The clause is Billy-ruled twice (08-21 shape, 08-23 operational form) and is the only replacement guard the corpus names for a retired one (→ M52, M54). **The recall half remains untested** and the corpus says so. → **C2**.

**`⟂container`, qualified.** The clause is domain. The measurement apparatus - 60 graded runs, the faithfulness grader, `claude -p` cold starts - is container-bound.

## M3. Scope is not a defect, and the active window

**Names:** "scope is not a defect", "the ±1-2 week observation", "the active window", "band A".

- **`domain-design.md §2` `OPERATIONALISED` block, Billy, 2026-08-23** (S1 thing 3). "**Scope is not a defect.** A request for a whole semester that gets a whole semester is answering what was asked. Billy's own observation that the useful window is ±1-2 weeks is a *requirement he may state*, not a failure to fix."
- **`domain-design.md` changelog, 2026-08-28, Billy, ruled** (S1 thing 3). "the ±1-2 week observation this section held as *a requirement Billy may state, not a failure to fix* **was stated and ruled on this date, as `today-7d .. today+14d`**." The body of §2 was never updated. This is one of the two rulings that live only in a changelog (Correction 3).
- **`ring-0.md §3` and changelog, 2026-08-28, Billy (the window) / agent (`done_by`), ruled** (S2 T28; verified by zoom). Band A "active" fires on any one of: `due` in `today-7d .. today+14d` · `done_by` in the same window · `state == in_progress`. Changelog: "**The window's own standing is new:** `domain-design.md §9.1` had recorded the ±1-2 week observation as *a requirement Billy may state, not a failure to fix*, and **it was never ruled until now.**" A second 08-28 ruling promotes `state == in_progress` to a trigger in its own right: "working ahead of the dated window is being active, so the partition is not a time window with exceptions but three independent triggers on one question."

**Standing.** **Settled and re-homed.** The changelog-only ruling S1 flags has a body: `ring-0.md §3`. The domain-side note is a pointer, not the authority. This is a clean cross-survey close - S1 held the ruling with no home, S2 held the home. → **C3**.

## M4. The system declares nothing outward; the assertion surface; `manifest`

**Names:** "the assertion surface", "the audit / completeness-assertion surface", "the trust mechanism that can lie", `course.manifest`.

- **`openclaw:log/2026-08-21` §reversals item 5, Billy attributed** (S5 items 3-4). The agent had derived "5 of 5 obligations held, last synced 10 min ago". "**Billy rejected it: the system declares nothing outward.**" The agent's own self-incriminating notes are recorded: the assertion "should be one boring line nobody reads", and its manifest "could go stale and lie confidently. **A trust mechanism that can lie is net-negative.**"
- **`domain-design.md §1` ruling 10, Billy, 2026-08-21** (S1 thing 5). Same ruling as an imported numbered item. "Trust accrues from being useful, not from self-reporting."
- **`domain-design.md §7`, `RULED OUT 2026-08-21`** (S1 thing 5). "Integrity checks (closure, no coexisting contradictions) survive as silent internal work. **The `manifest` field survives on a different justification** - see §6."
- **`domain-design.md §6` table, 2026-08-21** (S1 thing 29). `manifest` "earns typing because it makes answers complete ('A4 exists, not yet scheduled'), NOT because anything is reported outward."
- **`schema.md §7` graveyard, 2026-08-28** (S2 T49). `course.manifest` is **not carried**: "**exactly redundant with the rows** - 2c03 lists 15 and has 15, 2aa4 lists 7 and has 7. An obligation declared but unscheduled is a row with a null `due`."

**Standing.** The ruling stands: the system declares nothing outward. `manifest`'s *second* justification - completeness of an answer - was then killed by measurement in the spec tier, and `schema.md §7` does not cite the domain justification it is retiring. So the field is gone on both grounds, by two independent routes, neither of which mentions the other. → **C4**.

**`⟂container`.** "Declares nothing outward" is a statement about an app's user-facing surface. In a plugin the components *are* an agent's tool surface, where "does this component report on its own completeness?" is a different question with possibly a different answer.

## M5. Not an enterprise RAG; tune for recall; the third job

**Names:** "not enterprise RAG", "tune for recall not precision", "the third goal", "surface details Billy does not know to ask about", "set difference".

- **`domain-design.md §10.7` ruling 4, Billy, 2026-08-22** - the source clause. See M1.
- **`domain-design.md §10.8`, marker `## 10.8 Agent drafts, not ruled`** (S1 thing 4). "**Tune for recall, not precision.** Ruling 4's third goal … is the only one not served by 'retrieve when asked', and it wants breadth with the filtering left to him."
- **`model.md §6`, 2026-08-22, unattributed** (S1 thing 4). Upgrades the third goal from a tuning posture to a query: **set difference** "turns `domain-design.md §10.7` ruling 4's vaguest goal into a **deterministic query**."
- **`design.md §3.4` / `architecture.md §7`, 2026-08-27** (S2 T24). `nodes_without(node_kind, link_kind, direction) -> [Node]` is the set-difference operation, named, signed, and assigned: **application tier, slice 2**. `design.md §3.4`: "the query scans one layer… and it means **no link of that kind in that direction** - never 'a node lacking a kind'."

**Standing.** **Settled toward the query.** S1 records §10.8 and `model.md §6` as a mild unreconciled disagreement about whether the third goal is a retrieval tuning or a deterministic query. It is settled: the spec tier built the query, gave it a signature and a slice, and the tuning posture is self-declared "agent drafts, not ruled" and is honoured as such under merge rule 3. Neither survey could see this - S1 held the disagreement, S2 held the operation. → **C5**.

## M6. Progressive disclosure, and expansion cost as the gate

**Names:** "progressive disclosure", "expansion cost", "the H2 gate".

- **`openclaw:fall26/2026-08-22-derivation/TASK.md` §H2, Billy, 2026-08-22** (S3 origin intent item 6). "**Reframed by Billy, 2026-08-22**, before any extraction ran." An earlier H2 gated on total N + E against a fixed token budget; Billy ruled that wrong: "disclosure is progressive by design philosophy, only ring 0 is resident, and **nothing requires a CLI fetch to render the whole graph. The gate moves from *total size* to *expansion cost*.**"
- **`model.md §7`, Billy, 2026-08-22, `[R]`** (S1 thing 51). The imported form: "**progressive disclosure is the design philosophy, and ring 0 is everything the coordinator actually needs.** > The coordinator holds ring 0 resident and *queries* the skeleton on demand. It does not hold the skeleton."
- **`architecture.md §5`, Billy, 2026-08-27, ruled** (S2 T41). The surface form: "**one composable grammar with progressive disclosure** - each level renders what is around it, and going one level deeper is one more call."

**Standing.** Current, Billy-ruled, and the one origin-cycle reframe that propagated intact through three records over six days. Under rule 4 the openclaw statement is the *earliest and fullest* form and is not discounted.

**`⟂container`.** "Nothing requires a CLI fetch" and "each level renders" are surface facts.

## M7. No proactivity, no cron; Billy's urge to check is the scheduler

- **`domain-design.md §2`, 2026-08-21** (S1 thing 84). "**Consequence for scheduling:** no proactivity, no cron, no 24/7 - the existing on-demand ruling holds. **Billy's own urge to check is the scheduler**; the design gives that urge a better target instead of fighting it."

**Standing.** Uncontested anywhere in four surveys. **`⟂container`** - a statement about how a running service behaves, and about a human being the trigger.

## M8. "Sync" is the wrong model

- **`openclaw:log/2026-08-21` §reversals item 2, Billy, explicit `(Billy)` tag** (S5 item 11). "**'Sync' was the wrong model** (Billy). Not a system kept aligned with a remote - a KB that accumulates. Killed full re-reads, diffing, mirror state."
- **`domain-design.md §1` ruling 4, Billy, 2026-08-21** (S1 thing 80). Imported form: "It is a knowledge base: things enter, stale/wrong things leave, everything is classifiable and queryable."

**Standing.** Current, uncontested. The openclaw form carries what the import dropped: the three mechanisms it killed.

## M9. The two observed failure modes

- **`domain-design.md §1` ruling 12, Billy, 2026-08-21, from the live Fairy system** (S1 thing 86). "(a) the thread graph records at too fine a grain… (b) a coordinator that pulls in-depth information about one course cannot possibly hold every course's every topic, so its **weighting judgment gets polluted** by whichever slice it happens to have."
- **`openclaw:log/2026-08-21` §reversals item 7, Billy attributed** (S5 item 9). "**Asymmetric depth biases allocation** (Billy's failure mode, from live Fairy). … **visible work masquerades as important work.**" S5 records the source: "drawn from watching a live system, not from introspection."
- **`domain-design.md §9.1`** answers (a) with "pointers and summaries, never content" plus non-sedimentation; **`§9.2`** restates (b) as a mechanism; **`model.md §7`** aims mechanism 1 at (b) and is later replaced by the symmetry rule (→ M69).

**Standing.** Current, and (b) is the direct ancestor of the symmetry rule. This is the corpus's only requirement grounded in observed behaviour of a *running* system rather than in course material.

## M10. The schema must not be over-determined; "you cannot write the relationships today"

- **`openclaw:log/2026-08-21` §Key decisions, Billy verbatim** (S5 item 8). "**you cannot write the relationships today**" - one of only two verbatim Billy fragments in the 08-21 log. The rigidity rule is built as the answer to it.
- **`domain-design.md §1` ruling 7, Billy, 2026-08-21** (S1 thing 81). "**The schema must not be over-determined.** The cases cannot be enumerated today and the relationships cannot be written out today."
- **`domain-design.md §6`** answers it with the `/promote` gate: "**a tiny mechanical core plus everything else free**, not vagueness everywhere."
- **`model.md §8` watch list, 2026-08-22** (S1 thing 25). Same posture applied to edges: five candidates "one sighting each, **deliberately not adopted** (PLAN.md's over-modelling failure mode)."
- **`model.md §10.9`, Billy, 2026-08-23** (S1 thing 35). Same posture applied to conditional weighting: "**Billy rejected the general form** … as over-built for what is so far one concrete weight calculation."
- **`PLAN.md` §This cycle's own failure mode, 2026-08-22, agent** (S5 A7). "**Over-modelling.** Completing the model is satisfying and mostly wrong."
- **`design.md §4`, `schema.md §7`** (S2 T47, T49). The posture as a standing mechanism: "build only the slice whose dependencies are derived", and a fifteen-entry graveyard with "do not re-add without a new ruling."

**Standing.** The posture is current and is the corpus's most-applied meta-rule. **Its literal 08-21 conclusion is not**: eleven typed edges were written the next day (→ M25, C24). The tension between a Billy verbatim and a next-day edge table is real and is registered.

## M11. Disposability as the acceptance criterion

- **`domain-design.md §9.5`, 2026-08-21, named an agent draft by §9's header** (S1 thing 58). "> **If losing the coordinator session loses information, the design is wrong.** … it can be thrown away and rebuilt at the cost of one projection read." Corollary: "**do not try to make it survive a semester.** Its long-running scale is days-to-weeks."
- **`openclaw:log/2026-08-21` §reversals item, agent** (S5 C6). "**Coordinator purity is enforced at the tool surface**, not by instruction… with **disposability** as the acceptance criterion: losing the session must lose nothing."
- **`PLAN.md` §Settled, 2026-08-22** (S5 A8). Listed as settled and closed to re-litigation: "§9 - coordinator purity enforced by tool surface; **disposability as the acceptance test**; uniform-depth projection across all courses."
- **`ring-0.md §1`, 2026-08-28** (S2 T26). Inherited as a *size bound*: "losing the coordinator costs **one projection read** to rebuild. That is ring 0's size bound: roughly 55 obligations at five courses."

**Standing.** Current, and it has been converted from an acceptance criterion into a quantitative constraint on ring 0's size. **Standing note under merge rule 3:** `domain-design.md §9`'s header names §9.5 an agent draft and no later ruling promotes it, yet `PLAN.md` §Settled (08-22) lists it as settled and `ring-0.md` (08-28) inherits it as binding. → **C6**.

**`⟂container`.** The acceptance criterion is about a session object the successor container may not own at all.

## M12. Findings are surfaced for Billy; agents draft and never self-lock

- **`openclaw:fall26/2026-08-22-step-minus-1/p5-induction/TASK.md` §Explicit non-goals** (S3 origin intent item 11). "the repo's standing discipline that **agents draft and never self-lock**."
- **`derivation/BRIEF.md` rules 5-6** (S3). "**BLOCKED beats guessing** … A blocked agent that asks a sharp question is worth more than a finished one that assumed"; "**You may judge the model** … A finding that overturns the model is the most valuable thing you can return."
- **`p5-induction/TASK.md` §Reduction targets, Billy** (S3 item 5). Whether `ephemeral` is a fourth route is "**Billy's to rule**", so every instance is listed individually "so the ruling is made on **real instances rather than on this one hypothetical**."
- **`model.md`, `domain-design.md` throughout** (S1). The `[R]` marker system is this discipline's artifact; `model.md §4`'s `STANDING MARKED 2026-08-24` banner exists because "an unmarked agent passage was taken for, or overrode, a ruling" - three times in one day.
- **`schema.md` changelog 2026-08-25** (S2 T19). The same discipline applied in reverse: the sticky-note length bound was **demoted from `[R]` to owed** because "**No ledger anywhere supports the ruled standing** … demoting to the level the evidence supports is the conservative move."

**Standing.** Current, and it is why merge rule 3 works at all: this corpus marks its own standing, imperfectly but systematically. **It is also the corpus's most-violated rule** - S1 names three same-day violations, S2 names three self-corrections found by outside readers.

---

# Cluster B - Shape: layers, node kinds, edges, the store

## M13. Two layers, three compartments - facts / corpus, skeleton / store / ring 0

**Names:** "Facts layer" / "Corpus layer" (`domain-design.md §3`); "what a planner reads" / "what an agent reads" (`§10.5`); "ring 0 / skeleton / store" (`model.md §4`); "exactly TWO persisted things" (`design.md §3.0`).

- **`openclaw:log/2026-08-21` §reversals item 1, agent** (S5 C1). The origin: facts layer ("tiny, CRUD, authoritative for *what is true now*") vs corpus layer ("large, append+supersede, authoritative for *what the source said*"), on the moved-deadline example - "after a deadline moves, the spec PDF still says Wednesday and is *not wrong* … the fact says Friday and is *also not wrong*."
- **`domain-design.md §3`, 2026-08-21, unattributed** (S1 thing 6). Split by content type. "**Load-bearing consequence: full context in ordinary conversation needs no retrieval.**"
- **`domain-design.md §3` banner:** `⚠️ PARTLY SUPERSEDED 2026-08-22 - see §10.5. The number of layers holds; the split axis does not. The load-bearing sentence … is false as written.`
- **`domain-design.md §10.5`, 2026-08-22** (S1 thing 6). "**§3 - the split axis was wrong, not the number of layers.** … The working split is by *who reads it*… **the old two-layer split had no home for most of a course's real information.**" Survives: "**the allocation layer needs no retrieval.**"
- **`model.md §4`, agent-authored, 2026-08-22** (S1 things 6-7). Three compartments: "**the skeleton owns 'is there any, where, worth opening'; the store owns 'what is in it'; ring 0 owns 'when and how much'.**" Its own header admits terminology drift and does not map onto §3's two.
- **`design.md §3.0` / `§3.4` / `§3.5`, 2026-08-27** (S2 T34, T6). Settles it: "**Exactly TWO persisted things**" - the skeleton (nodes + links) and the store (chunks + embeddings, slice 3); **ring 0 is "not separately"** - "the obligation layer *is* ring 0. Ring 0 is the obligation-kind nodes' payload, and residency is an access policy over them." Corroborated identically in `schema.md §3` and `ring-0.md §1`.

**Standing.** **Settled by the spec, and it closes S1's most explicit unreconciled cross-file gap.** S1 records that `model.md §4` presents three compartments and never says whether ring 0 + skeleton together are "the facts layer". `design.md §3.0` answers exactly that: two persisted things, ring 0 an access policy over one of them, not a third thing. S1 could not see it; S2 recorded it as "the most stable statement in the corpus" without knowing what it resolved. → **C7**.

## M14. What a Node summary is for

- **`model.md §4` table, agent, undated** (S1 thing 7). The skeleton "answers … what is there, where does it sit, **is it worth opening**".
- **`model.md §4` banner, `STANDING MARKED 2026-08-24`.** "**This section is agent-authored and carries no `[R]`.**" On 08-23 its phrase was quoted in session as a settled ruling; "**it never was**", and Billy confirmed: *"我不记得我定论过 skeleton Node summary 的职责是什么这个问题"*.
- **`model.md §4.1`, heading `— NOT RULED`, Billy 2026-08-23, `[R]`** (S1 thing 7). "**the store's summary and the Node summary are different objects.**" *"Is it worth opening"* is wrong for the coordinator - §7's table denies it the store in both modes. *"Concise"* does not cover it either: the `2aa4-guide` summary was **55 words** and still noise "because it enumerated seven unrelated facts". The agent's amendment - *a summary is good iff it answers the question that made the agent look* - is "**the agent's, not Billy's, and has not been ruled on**."
- **`architecture.md §5`, Billy, 2026-08-28, ruled** (S2 T41c). "**Every level shows a one line per item, and that line is fields rather than a summary.** A *summary* is a written object, and it is written only where a node's identity is content the skeleton does not hold - **the artifact, and nothing else in the current kind set.** An obligation's line is therefore composed from what it already stores."
- **`design.md §4`, agent, 2026-08-27, measured** (S2 T41c). "**`label`-versus-`summary` is deferred, and it is no longer true that nothing is blocked by it.** A navigational surface renders a one-line summary at every level, so **the decision is presentation's first one.**"

**Standing.** **Substantially closed by the 08-28 architecture ruling**, which S1 could not see. What a Node summary is *for* is now: written only for artifacts; every other kind's line is composed from fields. The unruled agent amendment in `model.md §4.1` is superseded by a Billy ruling five days later. **What remains open** is the `label`-versus-`summary` decision itself, explicitly owned by the presentation tier which does not exist. → **C8**, **C9**.

## M15. The three node kinds, and the four slice-1 kinds

**Names:** obligation / concept / artifact (`derivation/BRIEF.md`, `model.md §2`); `kind` (`schema.md §1`, `design.md §3.1`); `layer` (`design.md §3.1`).

- **`derivation/BRIEF.md`, 2026-08-22, agent** (S3 §9, vocabulary table). obligation = "a thing with a deadline"; concept = "**a thing the student understands or does not**"; artifact = "**a thing that exists on disk** and is opened independently".
- **Both later definitions falsified within the same session** (S3 vocabulary table): concept rewritten by Billy's stateless ruling to "**a unit of subject matter the course teaches, independently addressable**"; "exists on disk" falsified by `[B2]` J2 (≥8 artifacts 2aa4 depends on are not on disk and never will be).
- **`model.md §2` table, 2026-08-22** (S1 thing 15). The corrected set: obligation carries time, "this layer *is* ring 0"; concept, no time; artifact, no time.
- **`design.md §3.1`, 2026-08-27** (S2 T3, T4). A different and orthogonal cut: "Slice 1 introduces `course` · `obligation` · `sticky_note` · `progress`; slice 2 adds `concept` · `artifact`." And: "**`layer` is a *different axis* and is not introduced in slice 1**: only the three skeleton kinds have one, `course` and `sticky_note` do not. **Introducing it early is precisely how the two axes get conflated.**"
- **`schema.md §1`, `design.md §3.1`** (S2 T3). "**Every node record carries a discriminator field named `kind`**"; "`kind` is **data on the node, never control flow**"; "remove this and the node has no shape."

**Standing.** **Both cuts are current and they are different axes** - the spec says so explicitly and names conflating them as the failure mode. The domain corpus has three *layers*; the spec has six *kinds* across two slices, of which four exist. `course`, `sticky_note` and `progress` are kinds with no layer. **This is a merge finding neither survey states**: S1 inventories the three node kinds without knowing `course` became a node, S2 inventories the four kinds without knowing the three layers are the domain's own axis. → **C10**.

**Residual gap the spec names against itself:** `design.md §3.1` lists four slice-1 kinds, then says "only the three skeleton kinds" have a layer and names two that do not - `progress` is unaccounted for in that sentence, and no record resolves it (S2 T4).

## M16. A course IS a node

- **`design.md §3.2`, 2026-08-27** (S2 T21). "**A course IS a node**, so `get(Ref('course','2c03'))` resolves and an `about` link to a course is an ordinary link with no special case. **This is forcing in slice 1, not slice 2:** course-level notes - the late-day budget, the snow-day credit, the conditional-weighting rule - must land and read back for F5 to pass."
- **`schema.md §1`** carries a weaker hedge: the kind tag "is what permits a ref to a `course` **whether or not courses ever join the node set**" - which `design.md` states flatly the other way.
- Nothing in the domain corpus says a course is a node; `domain-design.md §6`'s table has `course` as one of five **fact types**.

**Standing.** Spec-current (08-27), and load-bearing: it is what gives the late-day budget a home (→ M53). The `schema.md` hedge is internal drift, not a conflict with a ruling. → **C11**.

## M17. Layered graph, not a tree

- **`derivation/FINDINGS.md §2`, Billy, 2026-08-22, `[R]`** (S3 origin item 8). "a concept appearing in two places is **the truth of the data, not a rendering bug**. The model may not cut edges to force a tree. How rendering handles it is a CLI/UX decision, deferred."
- **`model.md §2`, Billy, 2026-08-22, `[R]`** (S1 thing 13). Identical ruling, imported. Argument: "A lecture PDF and a tutorial PDF exist independently and are used independently … yet both describe one concept (Stack). … **a file is not the object being modelled.**"
- **`derivation/BRIEF.md`** (S3): the motivating dissatisfaction, and the rejected alternative is the folder tree - vindicated three times independently by the material (`project 01` shared by A1 and A2; the midterm's material in a Week-5 deck *and* a Week-4 handout; T5/X5/N5 as three files, one question set).

**Standing.** Current, Billy-ruled, evidenced three ways. Uncontested in all four surveys.

## M18. Which layer is a tree - the concept DAG, the artifact tree

- **`model.md §2` original agent draft** (S1 thing 14). "*the tree survives inside a layer, which is what keeps rendering well-defined.*"
- **`derivation/FINDINGS.md §2`, `[B1]` adopted, 2026-08-22** (S3 §10). **False for the concept layer**, with named instances: **Singleton** is `part-of` Creational patterns *and* `part-of` STUPID - "two parents, opposite valence, the course deliberately teaches it twice"; **Liskov substitution** appears three times; **Observer** is behavioural and *is the mechanism of* MVC. "**The concept layer is a DAG. The artifact layer is the tree**" - 21 lectures into 5 groups, no document in two, none orphaned. Caveat stated in place: "**B1 tested for multiple parents; A2 did not.**"
- **`model.md §2`, `REVISED 2026-08-22 by the derivation`** (S1 thing 14). Same, imported, with 2c03's visible candidate added.
- **`design.md §3.3`, 2026-08-27** (S2 T23). `part-of` | `concept → concept` (**a DAG**) | slice 2 | ~35 (2c03) · ~30 (2aa4).

**Standing.** Current, evidenced, carried into the spec's LinkKind signature as a typed property of the edge. Uncontested. **Note the residual S1 flags:** `model.md`'s Status paragraph names this among three things the derivation *falsified*, and the falsified draft is still in the file above its own revision.

## M19. The modelling layer is stateless; system-inferred mastery is forbidden

- **`derivation/FINDINGS.md §5`, Billy, 2026-08-22, `[R]`** (S3 §11). "**the modelling layer is stateless.** It does not record what he has learned, understands, or does not; it presents the concepts and leaves judgment to him." Adopted consequences: the concept definition is de-stated; **system-inferred mastery is forbidden**; surviving set-difference queries are **structural** ("this concept has no artifact covering it") and never **personal** ("you never opened X").
- **`model.md §2`, Billy, 2026-08-22, `[R]`** (S1 thing 16). Same, imported, with the scoping parenthetical: "(Billy-stated progress survives untouched as a ring-0 row per `domain-design.md §1.6` - the constraint scopes to the modelling layer, not to facts Billy authors about himself.)"
- **`model.md §8.1`, derived not separately ruled** (S1 thing 16). "*'I've done part 1 of A6'*" → "**surface it for confirmation, never resolve it**" follows from the stateless ruling: "the agent has no evidence either way and may not manufacture some."
- **`schema.md §4.5`, 2026-08-28** (S2 T15). The ruling given an enforcement point - and a *ruled non-enforcement*: "**only the owner authors it** - system-inferred mastery is forbidden, so an agent may surface a progress claim for confirmation but never resolve one." Enforcement point: "**nowhere, deliberately** … It is a rule about the caller, and `architecture.md §1` forbids a method from defending itself against one."
- **`derivation/agents/2aa4-tutorials-and-artifacts.md` §Open question for Billy, `[B2]`, 2026-08-22** (S3 §11). The cost, raised and answered: Task-1's handwritten solution is "the densest single record of *what he actually understood* in the whole slice, and the model as frozen has no place to put it". Answered in `FINDINGS.md §5`: Billy's handwritten solutions are **artifacts**, not an understanding signal.

**Standing.** Current, Billy-ruled 08-22, mechanised 08-28. **A three-survey close**: S3 has the ruling and the cost B2 raised, S1 has the derived staleness rule, S2 has the enforcement decision. Nothing contradicts it.

**Broken cross-reference:** `model.md §2`'s parenthetical still calls Billy-stated progress "a ring-0 row per `domain-design.md §1.6`"; `domain-design.md §6.2` (08-24) and `schema.md §4.5` (08-28) rule it is **not** a typed obligation field but an annotation of its own kind. → **C12**.

## M20. Artifact existence - no `present` flag, no `external_ref`, and the residual

- **`derivation/agents/*` `[B2]` J2 and `[A3]` J7, 2026-08-22** (S3 §15, C1). Two agents, blind to each other, independently proposed the field: B2 argued `source_ref` must admit URLs and the node needs a `present` flag, because §6's set-difference "answers wrongly in the most consequential direction: it reports *have* for things that are merely *named*". A3 proposed `backing: referenced_only`, ~13 instances in 2c03, extreme case "**Midterm 2 is a graded obligation with a released grade and literally zero artifacts on disk.**"
- **`derivation/FINDINGS.md §5`, Billy, 2026-08-22, `[R]`** (S3 §15). **Both overruled.** "an artifact does **not** need a URL or a `present` flag - the resources exist on the portal, and knowing what a name refers to is sufficient; **he does not want everything stored locally**." Absence is not a field; it is the absence of store content, read as a JOIN.
- **`model.md §2` / `§9`, Billy, 2026-08-22, `[R]`** (S1 thing 17). Same, imported, with the counts: "2aa4 depends on ≥8 artifacts that are not on disk and never will be."
- **S3 C1, the residual the corpus does not address.** "**The JOIN framing answers B2's set-difference concern. It does not obviously answer A3's** - a node with no store content is indistinguishable from a node that was never created." `FINDINGS.md` does not address the difference.
- **Spec side: silent.** `artifact` is slice 2 (`design.md §4` must-not-build list). Nothing in `records/spec/` touches it.

**Standing.** The ruling is current and Billy's. **A3's residual is live and unaddressed in all four surveys' material** - and it now has no home, because the kind it concerns is slice 2 and the spec has not reached it. → **C13**.

## M21. H1 - course type as per-layer density

- **`derivation/TASK.md §1` H1, 2026-08-22** (S3 §9). "is course type per-layer *density* rather than *structure*? Falsified if either course needs a node kind or edge kind the other does not."
- **`derivation/FINDINGS.md §1` H1, 2026-08-22** (S3 §9). "**Not falsified, on a thinner base than claimed.**" And the base thinned in the same document: `[B2]` J3 grepped all nine 2aa4 tutorial documents for deadline/submit/marks/graded/due/weight and got **zero hits**. The real obligation layer is **7 nodes, sparse**, not ~16 dense. "**2aa4 is topic-dense / obligation-sparse - the same shape as 2c03.**" The wrong row "was written from folder appearances - **precisely the 'folders are not taxonomy' error the derivation was built to avoid, committed inside the model itself.**" Consequence: "**H1 now rests on two courses of the same shape, plus 2px3, which this run excluded.**"
- **`model.md §3`, Billy, 2026-08-22, `[R]` + `CORRECTED 2026-08-22` banner** (S1 thing 18). Same, imported; the 2aa4 row is struck through in the table. Plus a qualitative addition: "`announcement → node` is *structurally impossible* in 2aa4 rather than merely sparse, so a renderer must not assume the edge exists."
- **`model.md` header conditions** (S1). "§3's H1 (course type = per-layer density) is untested on an obligation-dense course; **gated on slice 2 running the extractor on 2px3.**"
- **`architecture.md §4`, Billy, 2026-08-28, ruled** (S2 T38). "**extracting the other three courses is not worth doing before the presentation tier exists.** Every contested field - `parts`, a note's `category`, `origin`, whether a note is worth keeping at all - needs a write rule, and a write rule is derived from what a value must be for a node to render well. **Reading three more courses without those rules produces three more courses of noise and does not produce the rules.**"

**Standing.** H1 is **not falsified and untested**, resting on two courses of one shape. **Its stated falsifier is now blocked behind a tier that does not exist.** The 08-22 gate ("slice 2 runs the extractor on 2px3") and the 08-28 ruling ("do not extract more courses before the presentation tier exists") are both current, both Billy-attributed, and neither cites the other. No single survey could see this: S1 holds the gate, S3 holds why the gate matters, S2 holds the blocking ruling. → **C14** - escalation.

## M22. The edge set

**Names:** "the edge set" (`model.md §8`), "H4" (`derivation/TASK.md`), "`LinkKind`" (`design.md §3.3`).

- **`derivation/FINDINGS.md §1` H4, 2026-08-22** (S3 §13). Bar: **≥3 real instances and a nameable query**. Survived with counts: `covers` ~150/118 · `part-of` ~35/~30 (as a DAG) · `obligation → concept requires` 9 authored + ~12 induced · `spec` ~45/8 (needs `role ∈ {given, owed}`) · `sticky_note → node` 7/2/≥4/5, "**targets straddle all three layers**" · `builds-on` 3 explicit. **Added:** `concept → concept requires` ("MODEL §6's flagship query does not work without it - §8 shipped only `obligation → concept`, so the transitive closure terminated after one hop") · `prepares-for` 8+5 ("`obligation → spec → artifact` is the wrong direction and the wrong meaning") · the edge payload **`locator`**. **Cut:** `supersedes`, `announcement → node mentions`.
- **`model.md §8`, scored 2026-08-22** (S1 thing 19). Eleven rows, same set, with the adoption rule: "Only changes supported by **≥2 agents or ≥2 courses**, or by a Billy ruling, were adopted." "Every entry passes the rigidity rule."
- **`design.md §3.3`, 2026-08-27** (S2 T23). Nine `LinkKind` rows with **signatures and slice assignments**: `about` (`annotation → any`) is the **only** slice-1 row; the other eight are slice 2. "**Slice 1 implements exactly one row of this table.** The rest is here to show that adding them is a table entry plus a signature - **trigger C defused** - not a schema change."
- **`model.md §8.2`, Billy, 2026-08-24** (S1 thing 19). `note-on` "generalises to `about`" - which is the name the spec's one slice-1 row carries.

**Standing.** **One thing across three records, converging.** The derivation scored it, the domain typed it, the spec signed it and sliced it. The domain's eleven rows and the spec's nine are the same set: the two cuts are absent and `sticky_note → node (note-on)` became `about (annotation → any)`. This is the cleanest three-way agreement in the corpus. → **C15** for the watch-list residue.

## M23. `supersedes` - cut

- **`derivation/FINDINGS.md §1`, 2026-08-22** (S3 §13). "**CUT - 5 agents, 2 courses, zero instances**", and "not merely unsupported; **keeping it is actively harmful**." Every real revision replaced the file at the same path under the same name, so there is no v1 and D1's read-time expiry has no input. Three shapes would be mistyped and **hide a live document**. "`[B1]`'s **dating trap** is decisive": 2aa4's notes exports carry real lecture dates while every plain-slide export was batch-produced 2026-03-04, so "newest wins" **systematically discards the richer file**. Replaced by `revised_at`. **Corollary from two courses: "the announcement stream is the only surviving record of supersession, because the filesystem destroys it."**
- **`model.md §8`, `**CUT**`, 2026-08-22** (S1 thing 20). Same, imported, plus: "**Filename similarity must never imply a relation** - one same-named pair turned out to be two different lectures (Jaccard 0.21)."
- **`domain-design.md §3`, 2026-08-21** (S1 thing 20). The corpus layer's write mode was "**append + supersede only**" - the very operation this cuts. §3's banner covers the split axis, not this column.
- **`design.md §3.3`, 2026-08-27** (S2 T23). No `supersedes` row exists in the LinkKind table.

**Standing.** Cut, on the strongest evidence base in the corpus, and absent from the spec. `domain-design.md §3`'s write column is superseded and unmarked. → **C16**.

## M24. `announcement → node (mentions)` - cut into `sticky_note.origin`

- **`step-minus-1/FINDINGS.md §P6`, 2026-08-22** (S3 §8). The proposition - announcements are a **delivery channel** for facts, not a body of knowledge - was pre-registered with the anti-cheat bias set *against* the convenient answer, and **FALSIFIED in both courses**: 2c03 7/55 knowledge (5/55 net of redundancy); 2da4 7/38 (6/38 net). What survives: "it is almost always **a correction against material the system already holds** … **An amendment to a document is not a fact.**" And: "**The redundancy defence is dead, verified on disk in both courses.**"
- **`derivation/FINDINGS.md §1`, 2026-08-22** (S3 §13). "**CUT - merged into `sticky_note.origin`**". "**An announcement is therefore the origin field of a sticky note**, plus a flat provenance log."
- **`domain-design.md §10.6`, 2026-08-22** (S1 thing 21). The imported finding, with the redundancy evidence named on disk.
- **`model.md §8` / `§9`** (S1 thing 21, D18). Cite §10.6 **twice in the direction of the proposition** ("announcements are a delivery channel, and the portal tree is a delivery layout") rather than of the finding.
- **`schema.md §4`, 2026-08-28** (S2 T17). `origin` is "**The annotation provenance field, shared with `progress`** … an announcement, someone saying so (`stated`), or the system having asked (`asked`)."

**Standing.** The **cut** is current. The **proposition is falsified** and `model.md`'s two paraphrases of §10.6 are wrong about what §10.6 found. S3's first-hand read settles it: S1 flagged the mis-citation and could not check it; S3 read the source probe. → **C17**, settled by evidence.

## M25. "No relationship graph" - overturned

- **`openclaw:log/2026-08-21` §Key decisions, unattributed** (S5 C5). "**No relationship graph:** relationships are inferred at read time, affordable because the layer fits."
- **`domain-design.md §6`, 2026-08-21** (S1 thing 26). "The only reason to declare them at write time is data too large to hold at once - and it fits."
- **`PLAN.md` §Settled, 2026-08-22, agent** (S5 A8). The narrowing, one day later: "**§6's rigidity rule** - a field is typed iff a mechanism reads it. **The *rule*, not the old type list.**" S5's own gloss: "The rule lived; the five-type list it was attached to was cut the next day."
- **`model.md §9`, 2026-08-22** (S1 thing 26). "**Design §6's 'No relationship graph.' Overturned by its own rule, not violated.** … the authorizing clause is the rigidity rule, and `obligation → concept` now has a mechanism that reads it."
- **`domain-design.md §6` banner** enumerates what changed in §6 and closes: "**Everything else in §6 … is unchanged and still governs.**" It does not list "No relationship graph" as changed.
- **`design.md §2` trigger C, 2026-08-27** (S2 T20). "**Relations are records, not fields on the related thing**" - held explicitly "**unaffected**" by the tier re-scoping.

**Standing.** **Overturned, and the overturn is corroborated by a document neither domain file cites.** `PLAN.md` (08-22) already recorded the narrowing to "the rule, not the type list" before `model.md §9` claimed the overturn - so the overturn is not `model.md`'s unilateral act. `domain-design.md §6`'s banner is stale on this one clause. → **C18**.

## M26. The rigidity rule, and its two standing exemptions

- **`openclaw:log/2026-08-21` §Key decisions, unattributed, answering a Billy verbatim** (S5 C5). "**Rigidity rule:** a field is typed *iff* a mechanism reads it. Deferring schema decisions is therefore free."
- **`domain-design.md §6`, 2026-08-21** (S1 thing 28). "Rigidity follows mechanism, not importance." Mechanisms: "M1 auto-retirement · M2 plan allocation · M3 rewrite targeting · M4 scope loading · M5 provenance". Banner: `⚠️ SCOPE CUT 2026-08-22 - see §10.5. The rigidity rule itself is vindicated and unchanged.`
- **`derivation/TASK.md §2` rule 5 / `BRIEF.md` rule 2, 2026-08-22** (S3 §20). The operational form the agents were held to: "**A field or an edge is real only if you can name the query that reads it.** If you cannot name one, do not propose it."
- **`domain-design.md §9.2` `RESTATED` block** (S1 thing 28). An agent lifts the rule one level: "*an observation earns its place if and only if a judgment demonstrably changes when it is present.*" Marked "**agent formulation … not separately ruled**".
- **`schema.md §3` and `§2`, 2026-08-27, Billy, ruled** (S2 T10, T13b). **Two ruled exemptions.** `grade_share`: "**This is a standing EXEMPTION** from the rule every other field passes - no mechanism reads it, and **the exemption is the point** rather than an oversight." `added_at`: "**No mechanism reads it** - it is carried deliberately, against a future reader, and is a declared exemption from the rule above rather than an oversight."
- **`schema.md` changelog 2026-08-27** restores the M1-M5 mechanism vocabulary *from* the domain records, noting it "**had never reached this record**" (S2).

**Standing.** The rule is current and is the corpus's most-cited instrument. **It now has two Billy-ruled exemptions that no domain record knows about.** S1 could not see them; S2 recorded them without knowing they are exceptions to a rule the domain corpus states as absolute. → **C19**.

## M27. `covers` / `applies` - why the split, and mention ≠ coverage

- **`derivation/FINDINGS.md §1` H2, 2026-08-22** (S3 §12). `[A1]` **edge conflation**: `Big O` is degree ~3 as *subject-of*, ~15 as *requires-you-to-understand*. `[B1]` **extraction scope**: `Interfaces` is 16/21 on full text, **2** title-scoped. The coined distinction: "full-text matching finds *mention*; title-scoped matching finds *coverage*". A1 proposed naming the second `applies`; the name was not adopted there.
- **`model.md §8` / `§10` item 1, 2026-08-22** (S1 things 23, 72). "It read two ways at once, and the reading determined whether a hub existed… **Only `covers` is rendered.**" `applies` is "never rendered; feeds closure."
- **`design.md §3.3`, 2026-08-27** (S2 T23). `applies` | `artifact → concept` | slice 2 | "**split out of `covers`; the split is what dissolved the phantom hub**."

**Standing.** Current, three records, converging, with the name A1 proposed adopted downstream. Uncontested.

## M28. The hub - H2, its dissolution, and the one that survives

- **`derivation/FINDINGS.md §1` H2, 2026-08-22** (S3 §12). "**The gate is invalid as posed.**" Three agents blind to each other each showed the number is a function of an unmade modelling choice. "**H2 as written measured our own choices, not the material.**" Restated as a **W2 constraint, not a gate**: title-scoped extraction, concepts cut at "one thing that can be separately asked about or separately taught", `covers` split from the prerequisite relation. Degrees under those repairs: 2aa4 title-scoped **median 2 / p90 4 / max 10 of 21**.
- **`model.md §10` item 1, `RESOLVED 2026-08-22, and the gate turned out to be invalid`** (S1 thing 72). Same, imported. "**One hub survives every repair and it is on the artifact side, which this document did not model:** a review deck covers 26 of 26 concepts and the textbook covers all of them. Their honest relation is **'indexes the whole course'**, not N peer `covers` edges. *Owed: how that is typed and rendered.*"
- **S3 C3 and C4, unreconciled inside the derivation.** Three agents returned three different H2 verdicts (`[A1]` "FAIL but not for the reason H2 anticipated"; `[A2]` "**fails twice** … a tiered expansion strategy is owed before W1"; `[B1]` "passes on this slice"); the synthesis picked a fourth. **A2's explicit demand - a tiered expansion strategy owed before W1 - is dissolved rather than answered.** And the adopted granularity rule directly contradicts A2's warning: "**Do not rescue the first hub by splitting it into per-topic analysis concepts** … the whole value of the concept is that Big-O of Quicksort and Big-O of Dijkstra are the *same* skill."
- **Spec side: silent.** `covers` and the artifact kind are slice 2.

**Standing.** The gate is dead; the constraints are current. **Two live residues, both invisible to S1**: the surviving artifact-side hub is owed and unclaimed by any record; and the granularity rule the corpus adopted is the exact split one of its own agents forbade. → **C20**, **C21**.

## M29. `spec` roles `{given, owed}`, and whether `produced` splits off

- **`derivation/agents/2c03-obligations-and-edges.md` J2, `[A3]`, 2026-08-22** (S3 C2). A3 concluded: "I'd **split off** `obligation --produced--> artifact` … because it has its own named query that `spec` cannot serve: **'show me what I handed in for A8'** … Roles 1/2/4 can stay one edge with a `role` discriminator; **role 3 is a different relation.**"
- **`derivation/FINDINGS.md §1` watch list, 2026-08-22** (S3 C2). **Misreports A3**: "`produced` as a separate edge (A3, B2 - **both concluded a `role` attribute suffices**)."
- **`model.md §7.2`, `**Left open, deliberately.**`** (S1 thing 24). Gets it right: "§8 compressed the derivation's four `spec` roles into two … **The derivation's J2 named a query that two roles do not obviously serve** - *'show me what I handed in for A8'* - and argued for splitting `produced`. **Not ruled.**"
- **`design.md §3.3`, 2026-08-27** (S2 T23). `spec` | `obligation → artifact`, `role ∈ {given, owed}` | slice 2.

**Standing.** **Open, correctly.** A cross-survey finding worth recording as a positive: the derivation's own synthesis misreported its agent, and `model.md §7.2` restored the agent's actual position without noticing it was correcting anything. S3 found the misreport; S1 found the restoration; neither could see the other. The question itself is deferred to slice 2. → **C22**.

## M30. `locator` - from edge payload to link identity

- **`derivation/FINDINGS.md §1`, 2026-08-22** (S3 §13). Adopted as an edge payload naming a fragment - a section, a page, a method, a question. "**nodes are typed and edges are bare pairs; the highest-frequency relation in the corpus cannot be stored without it.**" A1: 25+ citations at section grain; A2: three independent forms.
- **`model.md §8`, 2026-08-22** (S1 thing 19). "All edges may carry a `locator` payload."
- **`design.md §3.3` / `schema.md §5`, 2026-08-27** (S2 T22). **Promoted into the identity**: "`identity := (from, to, kind, role, locator)` - a natural key; no surrogate id." Justified by measurement: "**leaving it out silently destroys edges.** Computed over the source graphs: without it **7 real edges collapse**" - `s1 → textbook` cited four times from one deck with four different locators, `s6 → week-6-code` three times, and so on. "The residual is correct rather than a gap: two citations from the same source into the same target at the *same* locator are one edge." Measured: **28 instances in 2c03 (22 `cites` + 6 `example-code`)**.

**Standing.** Current and **strengthened** by the spec from payload to identity component, on a measurement neither domain record carries. → **C23** for what the 28 instances mean for S3's dropped edges.

## M31. `Ref`, one id space, and refs that dangle

- **`derivation/agents/2c03-obligations-and-edges.md` J6, `[A3]`, 2026-08-22** (S3 §17, C10). "the `builds-on` edge is authored at both ends at different times, **and one end dangles**. A8's handout says 'You will need this code for assignment 9' while A9 does not yet exist as a node. **Ingest must be able to write an edge whose target does not exist yet, and must not create a duplicate when the other end arrives.**" **Not in `FINDINGS.md §6`. S3 records it as dropped.**
- **`design.md §3.2`, 2026-08-27** (S2 T21). Independently arrived at: "`Ref := (kind, id)`" with property 3 - "**A ref may name something that is not there**, so a ref is not a foreign key and deleting a record does not have to cascade." Property 2: "**The kind tag makes a ref resolvable without a lookup**, which is what lets a link be *validated at write time* against its signature."
- **`design.md §3.2`, Billy, 2026-08-28, ruled** (S2 T21, T1). Property 3's *mechanism* is closed: "**What this is no longer for:** it used to carry forward reference - A8's handout names A9 before A9 exists - by letting a writer *construct* A9's id from its name. **That route is closed** … and the observation it rested on is handled without it: **list before linking, surface an untracked target to the user rather than auto-adding it, or resolve a batch ingest in two passes.**"
- **Cost, stated:** "a ref is not a foreign key, so nothing enforces that its target exists. Recovered by a validation pass over the link set - cheap at ~2,200 links, **and it is a real operation the design owes**, not a hand-wave."

**Standing.** **A3's dropped requirement survives, by a different route, using A3's own example.** The 08-28 ruling quotes the A8/A9 case verbatim and gives it three non-constructing answers. The duplicate-on-arrival half of J6 is answered by "list before linking". The validation pass is **owed**. A clean cross-survey close that neither survey could make: S3 recorded a dropped requirement, S2 recorded a ruling that resolves it without knowing it was answering anything. → **C24**.

## M32. Two persisted things; the coupling surface is one field

- **`model.md §6`, 2026-08-22, unattributed** (S1 thing 11). "**The coupling surface between skeleton and store is exactly one field: `chunk.node_id`.** Everything else is independent, which is what lets each degrade without the other."
- **`design.md §3.0` / `§3.5` / `§5` conclusion 3, 2026-08-27** (S2 T33, T34). Identical claim, plus: "`Chunk := id · node_id · ordinal · text · locator? · embedding`"; "**Separate engines are permitted and probably preferable**, because degradability wants them independent and the coupling is one field"; "**Nothing here is called `Store`.** That name is already taken: *the store* means materialized artifact content."

**Standing.** Current, triangulated across two records in near-identical words. Uncontested. **`⟂container`** - `chunk.node_id` names a table column in a store the app owned.

## M33. The store's access modes, and where the purity cut falls

- **`model.md §5` body, 2026-08-22, agent** (S1 thing 8). Two modes - by-handle and by-query. "**§9.0's purity cut falls exactly between them.**"
- **`model.md §5`, `REVISED 2026-08-23, Billy`** (S1 thing 8, D3). "That last sentence is **wrong as written and it misleads** … **§7's table denies it both.** The access levels are **three**, not two, and the coordinator's line sits above both store modes. … **The coordinator sees what a node IS; it never sees what a node SAYS.** §9.0's cut belongs between the skeleton read and by-handle. (It misled a session on 2026-08-23.)"
- **`domain-design.md §9.0`, 2026-08-21, agent draft** (S1 thing 8). "**Purity cannot be maintained by prompt. Only by tool surface.** … An agent holding a tool will use it."
- **`design.md §3.5` / `§2` trigger D, 2026-08-27** (S2 T33). Re-mechanised: "**The coordinator holds neither.** It sits above both store modes… Structurally: the coordinator holds the skeleton interface and does not hold the store interface, and **the skeleton's return type has no field a chunk could arrive in. Trigger D defused by type, not by restraint.**"

**Standing.** **Settled twice, in the same direction, by two different mechanisms.** Billy's 08-23 revision fixed the location; `design.md §3.5` (08-27) converted "remove the tool" into "the return type has no slot". The second is strictly stronger and is the argument the TypeScript ruling then rests on (→ M104). → **C25**.

**`⟂container`.** §9.0's mechanism assumes control of which tools the coordinator holds. In the plugin container the components *are* the tool surface, which may relocate rather than dissolve the rule - but the type-level version survives relocation, which is a reason to prefer it.

## M34. Materialization is not retrieval indexing

- **`model.md §5`, 2026-08-22, agent** (S1 thing 9). "Chunking, summarizing and tagging are paid once so that every later read is cheap; that cost exists whether or not anything is embedded. An earlier agent draft ('embed ~300 summaries instead of ~20,000 chunks') conflated the two and was **retracted** - it would have forced a runtime `pdftotext` on every detail read."
- **`design.md §5` conclusion 2, 2026-08-27** (S2 T33). The same separation at the storage layer: "**The store does want real storage**… 62 MB of vectors should not be re-parsed per invocation… But brute-force cosine over 10⁴ vectors is milliseconds, so what it needs is **storage, not an ANN index** - that is a slice-3 decision with a measurable trigger." Sizing is flagged **estimated, not measured**.

**Standing.** Current, uncontested, and the spec adds the measurable trigger the domain record lacked.

## M35. Where the vector index attaches

- **`domain-design.md §1` ruling 9, Billy, 2026-08-21** (S1 thing 10). "**RAG is accepted for corpus** - one-time embedding at material drop, **per-course buckets** for independence, metadata filtering. Math-equation chunking is a known industry problem and is deferred."
- **`step-minus-1/FINDINGS.md §P1`, 2026-08-22** (S3 §1). **PASS** - pgvector 0.8.0 on PostgreSQL 17.6, HNSW index built. The probe's *stated* motive is the anti-hype discipline, not the answer: the spec rated it `low` severity, "which is a rating of *likelihood*, not of blast radius", and grep returned zero references to pgvector anywhere in the repo.
- **`model.md §5`, "agent position, not ruled"** (S1 thing 10, D24). "Embeddings attach to the **concept layer** as the entry point; chunks stay in the artifact layer for reading. `query → nearest concept → walk covers → read artifact by-handle`."
- **`design.md §3.5` / `§7` item 4, 2026-08-27** (S2 T33). "**Not decided, and load-bearing for slice 3:** one position attaches embeddings to the **concept layer** as the entry point… That implies **two** embedding sets, not one." Owner: "the build, slice 3."

**Standing.** **Not a conflict - an open item with a named owner.** S1 registers per-course buckets (Billy 08-21) against the concept-layer entry point (`model.md` agent, unruled) as an unacknowledged cross-file disagreement. `design.md §7` item 4 names it open, assigns it to slice 3, and states the cost the domain record did not (two embedding sets). The two positions are also not exclusive: buckets are a partitioning of the index, an entry point is a routing decision. → **C26**.

**`⟂container`.** pgvector, HNSW and the managed Supabase instance are properties of a database the standalone app owned. The plugin container has no stated database.

## M36. The graph has no time axis; `week` is not a field; the navigational handle

- **`domain-design.md §10.5`, 2026-08-22** (S1 thing 27). "'A field is typed iff a mechanism reads it' is exactly what says `week` must **not** be a field: `week` is a retrieval term, and 2px3 organises by week while other courses organise by topic or assignment number. **Hardcoding either is the failure.**"
- **`derivation/per-course/2aa4/inventory.md`, `[B1]`, 2026-08-22** (S3 §16). Material: 2aa4 has **zero "Week N" markers in 687 KB of lecture text** and no announcement stream, "so it has no time signal at all except PDF creation dates."
- **`model.md §9`, 2026-08-22** (S1 thing 27). "**`time-anchor` as a node field.** Retracted… **Invariant instead: the graph has no time axis; time lives only in the obligation layer.**" And the cost it says it had not priced: "*'what is week 7 about'* is unanswerable for such a course from lecture material… **The navigational handle is course-specific - week for 2c03, module for 2aa4 - and it is a label on the coarse grouping that the schema never names.**"
- **`derivation/agents/2aa4-lecture-concepts.md` J3, `[B1]`** (S3 §16). The proposal that would have closed it: "**accept that the navigational handle is course-specific - week for 2c03, module for 2aa4 - and let the coarse grouping be the primary handle everywhere.**" **Not recorded in `derivation/FINDINGS.md`. S3 reads it as dropped.** `[B1]` also proposed a **`lecture_date`** node field, "for 2aa4 the **only** ordering signal that exists" - also dropped.
- **`PLAN.md` §What it is responsible for, question 2, 2026-08-22, agent** (S5 A3). Uses the same sentence as the paradigm case: "Ask '**what is week 7 about**' - some of the answer is on hand, the rest is fetched. **Where that line sits is the hardest and most important decision in this cycle.**"
- **`domain-design.md §10.4`, Billy, 2026-08-22** (S1 D19). Uses it as the paradigm of what the system is for: "when Billy asks '**what is week 7 about**', it holds the surrounding context."
- **Spec side: silent.** No record in `records/spec/` names a coarse grouping, a module, a week, or a navigational handle. `time_point` is graveyarded to slice 2 (→ M60).

**Standing.** **Live, and three surveys hold three pieces.** The invariant is current. The example sentence built on top of it is used by Billy (08-22) and by `PLAN.md` (08-22) as *the* paradigm, and by `model.md §9` (08-22, same day) as **unanswerable** for a timeless course. B1's proposed resolution was dropped from the derivation's synthesis on 08-22 and resurfaces in `model.md §9` only as an unpriced cost. Nothing in the spec tier gives the handle a home. → **C27** - escalation.

## M37. `backing`, and `text_extractable`

- **`derivation/FINDINGS.md §4.1`, `[B2]` J1 adopted, 2026-08-22** (S3 §15). "**`backing` cannot be inferred from file type, and 'chunkable' is the wrong axis.**" Falsified four ways in one slice: scanned handwriting in a PDF wrapper; a text PDF whose exercises **are images** (backing is not uniform *within one file*); a `.png` containing a rendered prose block, more chunkable than several PDFs; one diagram held as both `.drawio` and `.png`. "**The real axis is whether meaning survives linearization** - a property of the materialization pass, not of the file. In `visitor.png` the labels linearize but **the edges are the content**." Adopted: `backing ∈ {materialized_doc, code_project}` plus a per-region **`text_extractable`**, default false, true only when a pass actually recovered text. Its reader is the trust contract - **distinguishing a quotation from a generated description**.
- **`model.md §8` / `§9`, 2026-08-22** (S1 thing 39). Same, imported, with the four falsifications and the OneNote-export case: an extension rule would route to `pdftotext` and yield "**a confidently empty chunk set nothing downstream complains about**".
- **Spec side: silent.** `artifact` is slice 2; `design.md §4`'s must-not-build list excludes it.

**Standing.** Current, evidenced four ways, and **deferred by slice**. No conflict. → **C28** for its tension with the source-class RAG rule.

## M38. Detection of empty extraction, not OCR

- **`step-minus-1/FINDINGS.md §P2`, 2026-08-22** (S3 §3). Four 2da4 files return **zero extractable text across 27 pages**. "Neither the design doc nor the build spec contemplates material with no text layer." The requirement created is **detection, not OCR**: "**a silent empty index entry is not deferrable, because it makes the corpus lie about its own coverage.**"
- **`step-minus-1/FINDINGS.md §P6` collateral** (S3 §3, C8). Corrected upward two probes later: 2c03's tutorial notes are handwritten scans at ~23 extractable chars/page, "making image-only material **a whole class in a core course rather than the edge case P2 reported it as**." Independently reproduced by two derivation agents in two further courses.
- **`step-minus-1/FINDINGS.md §P2`, the silent-wrong instance** (S3 §2). `2aa4/assignments/assignment-01/Assignment 1.pdf` returns `"Course code: SFWRENG 2AA4"` for **all six pages** - "Non-empty, confident, plausible, wrong." Pre-registered as the failure mode that matters: "**A silent wrong label is worse than no label.**"
- **`model.md §9`** (S1 thing 39) carries the same requirement inside `text_extractable`'s default-false rule.
- **`domain-design.md §10.7` ruling 3, Billy, 2026-08-22** (S1 thing 65). Handwritten tutorial notes are **excluded from RAG** - "effectively treated as absent."

**Standing.** Current. The requirement (detect, do not silently produce empty) is carried by `text_extractable`'s default-false. **Note the collision** between "handwritten notes are excluded by rule" (Billy 08-22) and "handwritten scans are a whole class in a core course" (measured the same week) - the exclusion is a ruling, the class size is a measurement, and no record puts them side by side. → **C28**.

## M39. One lecture, several files; `variant`; filename similarity implies nothing

- **`derivation/FINDINGS.md §4.2`, `[B1]` adopted, 2026-08-22** (S3 §15). "**One lecture, several files.**" 9 of 21 2aa4 lecture nodes back onto two files; the `~1` variant is a near-perfect subset (Jaccard 0.50-0.69) because the base is the **notes export** carrying speaker notes. In **2 of 11 pairs each side holds content the other lacks (union required)**. One pair is a **name collision, not a version** (Jaccard 0.21). Adopted as a **node property - a file list with a `variant` tag - not an edge**, "because the query reads a list rather than a traversal." "**Filename similarity must never imply a relation.**"
- **`model.md §8` / `§9`** (S1 things 39, 20). `artifact: … files[]{ variant, text_extractable } · revised_at`, and the Jaccard-0.21 case is cited as part of `supersedes`'s cut.
- **Spec side: silent** (slice 2).

**Standing.** Current, deferred by slice. Uncontested.

---

# Cluster C - Fields and identity

## M40. `id` - the identity scheme

- **`derivation/agents/2aa4-tutorials-and-artifacts.md` J5, `[B2]`, 2026-08-22** (S3 §16). "**Resolution is semantic, everywhere, from three directions.**" Cross-references in 2aa4 are by informal alias and never by filename. Tutorial identity must be **topic-derived, never number-derived**: number in filename 5/9, `Structural.pptx` carries no number anywhere, header metadata 3/9 and **wrong in one**, while **topic appears on the title line 9 of 9**. "*The file knows what it is about; it does not reliably know when it happens.*"
- **`schema.md §1.1`, Billy, 2026-08-28, ruled** (S2 T1). The retired scheme is `<course_id>-slug(name)`. The ruling: "An `id` is **opaque, monotone, and assigned by the system**. It says nothing about the record it names, and nothing derives one from the material." · "one id space, shared by every kind that can be an edge endpoint" · "**It is never reused, a delete included.**" · "**An id is obtained by reading it back; nothing constructs one.** … **Every read that returns records therefore returns their ids**, or the rule cannot be followed."
- **Changelog reasoning, `schema.md` 2026-08-28** (S2 T1). Two reasons. The material: "one course names the same series `ChildMath A1` and `ChildsMath A4`, another spells one row `Week 2 Lab deliverables` and the next `Week 3 Lab diliverables`." And the load-bearing one: it "**contradicted `architecture.md §3`, which had already ruled that the agent never constructs an identifier - a divergence between two ruled records that nobody had propagated.**" The failure class named: "**Constructing an id is a bet on reproducing another writer's spelling - a cognition problem wearing a mechanism's clothes.**"
- **`architecture.md §3` consequence 4, Billy, 2026-08-27, `[R]`** (S2 T36). "**The agent works by listing, then acting on what it saw.** It does not address records by raw identifier and does not construct one. … **identifiers need not be human-facing**, and **matching two records is an interaction at the presentation tier, not an algorithm in the application tier.**"
- **Idempotency held harmless** (S2 T1): "it always rested on the caller supplying an id it had read, never on derivability."

**Standing.** Current, Billy-ruled twice, and **B2's 08-22 finding is its ancestor**: "resolution is semantic" and "matching is a presentation-tier interaction" are the same claim six days apart. Under merge rule 4 the openclaw finding is the earliest statement of it. No survey connects them. → **C29**.

## M41. `course.id` - the exception to opacity

- **`schema.md §2` and §1.1, Billy, 2026-08-28, ruled** (S2 T2). "`course.id` stays the supplied course code, and the id space is deliberately not uniformly opaque." · "**Supplied rather than assigned**: the source issues a canonical unique code, so there is nothing for the system to invent." · "**An id is assigned only where the material supplies no identifier of its own** - which today is every kind but `course`." Scope limit stated: "It settles nothing about `concept` or `artifact`, whose own material has not been read for this question."
- **`write-rules.md §2`, 2026-08-28, agent, measured** (S2 T2). Demoted out of the write-rules table into a pointer, because "**Sitting in a `records/spec/` table was giving an agent recommendation `ruled` standing by placement.**"

**Standing.** Current, scoped, and self-limited. Uncontested.

## M42. `kind` as a discriminator, and `layer` as a separate axis

See **M15** for the kind set. The discriminator itself:

- **`schema.md §1` / `design.md §3.1`, Billy, 2026-08-27, ruled** (S2 T3). "Without it a reader must infer the kind from **which fields are present**, and dispatching on a record's shape is precisely the control flow `design.md §3.1`'s trigger B forbids." · "**It is not metadata.** … what it actually does is **select which declared field set the node's payload has**."
- **`schema.md` 2026-08-28** amends the *argument* without amending the rule: "`kind`'s argument now rests on shape-sniffing being dispatch rather than on a degenerate record" - because the degenerate case (a null-state progress record) was itself removed by the `progress.state` reversal (→ M51).

**Standing.** Current, and a clean instance of the corpus repairing an argument when its example was withdrawn.

## M43. The conventions block - `null`, one free-text field, field-grain CRUD, timestamps

- **`domain-design.md §6`, 2026-08-21** (S1 thing 30). "**Rule: exactly one free-text field per type.** More and Billy has to decide where things go (the overhead returns); zero and it is over-structured." Banner-confirmed as still governing.
- **`schema.md §1`, 2026-08-28** (S2 T5). Four conventions ranging over every kind. `null` "means *no record*, never a default, and **must render as absence**" - with the `progress.state` carve-out. Free text: "**at most one field per kind. `course` has zero** - a cap, not a quota." Mutability: "**every field is individually CRUD-able.** Landing performs partial update, never whole-record replacement." Timestamps: ISO 8601, `added_at` on `course` and `obligation`; annotations carry `created_at` and `updated_at` "**because a note is modifiable and a record's birth is not its last claim**."
- **`schema.md` changelog 2026-08-28, agent, measured** (S2 T5). "§1's `added_at` on every node is corrected to `course` and `obligation`. Neither annotation kind's field table carried it, so **the blanket sentence was false as stated** and would have misled a slice-2 kind author."
- **`architecture.md §7`, 2026-08-27** (S2 T5, T24). "**What the application tier is made of is CRUD at field grain.** … `schema.md §1` has always implied it. **That clause had never been translated into a method set**, and its absence is why an operation list belonging to the graph was mistaken for the tier's contents."

**Standing.** Current. **The one-free-text-field rule is a cross-survey close**: S1 records it as a domain rule that `model.md §7.2` (summary + tags + sections) and `§8.2` (`progress`: state + detail + origin) never test themselves against. `schema.md §1` restates it as "at most one field per kind" and `progress` complies - `detail` is its one free-text field; `state` is an enum, `origin` an enum, `updated_at` a timestamp. **The `summary + tags + sections` case remains untested** because it is artifact-side and slice 2. → **C30**.

**`⟂container`.** "Must render as absence" is a rendering rule sitting inside a record whose own conditions line says "A rule about what an agent should DO is presentation tier and does not belong here." S2 flags it; the surface it names is the CLI.

## M44. `obligation.course` - a field, not an edge

- **`schema.md §3` / `design.md §3.3` / changelog 2026-08-27, Billy, ruled** (S2 T7). "**A field, not an edge**, and a property of `obligation` rather than of every node - a concept is not per-course." Reason: "Course membership is single-valued, mandatory and monomorphic, and nobody walks it… **The rule that relations are records exists to stop a polymorphic target becoming a field, and this target is not polymorphic.**"
- **Mutability is unruled** (S2 T7). `write-rules.md §3`: "*That* it is set at create and not updatable is an application-tier question, **still open at `../plan/application-tier.md §7.1` as a recommendation with no ruling. The code implements the recommendation; this record does not decide it.**"

**Standing.** The field/edge question is ruled. **Its mutability is not, and the code has already implemented an unruled recommendation.** → **C31**.

## M45. `due`, and what a date-only value means

**Names:** `due`, "date-only resolution", "the end of that day", `23:59`.

- **`model.md §8.3`, `PROMOTED 2026-08-24 (ruled 2026-08-23)` from `E10R-RESULTS.md §1`** (S1 thing 38). "`2aa4-a3`'s due was stored date-only, `"2026-03-20"`, and parsed to **`T00:00`, the start of the day**, against `2c03-a7`'s `T23:59`. *'Due March 20'* means its **end**. Consequence, measured: 2aa4's three dated obligations, and every `done_by` derived from them, were **a day early in all 60 runs**." The general lesson: "**It was found only because it invalidated an experiment's tie.** Nothing tested it, nothing errored, and its production signature would have been silent. **A date without a time needs an explicit convention at the schema level, not at the parser's discretion.**"
- **`schema.md §3` and changelog 2026-08-27, "Billy 2026-08-24 via `archive/changelog-2026-08-24-slice-1.md:241`", ruled** (S2 T8). "`due`'s date-only resolution is **`23:59`, the ruled value, restored over the prose *'the end of that day'* which lost the number.**" Type: `Date | DateTime`, nullable. "A `Date` resolves to `23:59` at read time; **which surface applies that resolution is presentation tier**, and the stored value is always returned raw. A `DateTime` is a stated time and is never overwritten by that default." · "**The moment this obligation is anchored to.** For something handed in that is the deadline; for a sitting it is when it starts - a narrower definition is false for the 3 of 22 rows that are exam sittings." · "The midterm pattern - a date first, a time later - is a CRUD of `Date` into `DateTime`."

**Standing.** **Settled by explicit ruling on the spec side, and the domain record is the weaker form.** `model.md §8.3` carries the prose ("the end of that day"); `schema.md §3` restored the number. This is one of the few places the corpus caught a *loss of precision in transcription* and reversed it. → **C32**.

## M46. `done_by` / `target_date` / `finished_by` - one field, three names

**This is a merge finding no survey makes.** Three names appear across three sources for what reads as one field, and no record connects them.

- **`derivation/TASK.md` §Courses / `FINDINGS.md §3`, 2026-08-22** (S3 §14, "how Billy actually works"). Billy's hand-maintained Notion table of 2px3's obligations, "kept for a year", has **no workload column** and **does have a `target_date`**. Recorded as evidence, twice, and used as the second independent falsification of `workload`.
- **`model.md §8` vocabulary, 2026-08-22** (S1 thing 40). `obligation: due · status{...} · weight · **target_date?** · workload? · parts[] · count{}`. No definition is given anywhere in the domain corpus for what `target_date` is.
- **`schema.md §3` / changelog 2026-08-27, Billy, ruled** (S2 T9). `finished_by` **renamed** `done_by`: "The ruled name was always `done_by` and the rename is a measured mechanism, not a label: **rendered as a start date the field was misread in every prior run**, and renaming it fixed the misread `finish 17 : start 1` **across six runs**. `finished_by` never had a ruling behind it." Definition: "**The date chosen to have this finished by.** Null means no record; a planner wanting a work-back date computes `due − 7 days` as a **derived** value under its own name… **A stored value therefore always means it was chosen.**" The 7 days: "a draft finished a week early makes urgency arrive while slack remains, which is **the one place the system's anxiety-removal goal reaches the schema**."
- **`ring-0.md §3` / §4 / §5, 2026-08-28** (S2 T9, T28). A band-A trigger and a band-A-only projection field; "**triggering and ordering are different jobs** and one field can do the first without doing the second"; "`due` is the primary key, **not `min(due, done_by)`**."
- **`step-minus-1/FINDINGS.md §P2` sub-question 2** (S3 §4). Corroborating behaviour: Billy's own reports "are dated **7-13 days ahead of each due date**."

**Standing.** `done_by` is current and fully specified. **`target_date` is the same field under the name Billy's own Notion table uses, and nothing in the corpus says so.** The domain record's `model.md §8` still lists `target_date?` in the same vocabulary block that lists the graveyarded `workload?` and `status{}` - i.e. it is unreviewed rather than reaffirmed. And the 7-day derivation is empirically anchored by a measurement in a third survey (7-13 days ahead) that the spec record does not cite. → **C33**.

## M47. `grade_share` / `weight` / `worth_percent` - one field, three names, and a standing exemption

- **`derivation/FINDINGS.md §3`, `[A2, A3, B2]`, 2026-08-22** (S3 §14). "**`weight` is absent from the schema entirely**" - three agents, independently.
- **`model.md §8` vocabulary, 2026-08-22** (S1 thing 35). `obligation: … weight …`.
- **`model.md §10.9` and `§7.1`** use **`worth_percent`** and **`grade_share`** for what reads as the same field, with no reconciliation (S1 D27).
- **`schema.md §3`, Billy, 2026-08-27, ruled** (S2 T10). `grade_share`: "**Approximate** share of the final course grade, in percent. **Reference only** - never an input to a computed ranking, **because workload is judged from progress plus size rather than from the percentage.** **This is a standing EXEMPTION** from the rule every other field passes." Reader column: "**none, by exemption**."
- **`design.md §7` item 1** (S2 T10). "The `weight` / `grade_share` field's **own name is not settled. Owner: the user.**" All four spec records use `grade_share` throughout.
- **`ring-0.md §6`, 2026-08-28** (S2 T29). **Excluded from ring 0 on measurement**: 38% of every measured faithfulness failure runs through it. Plus a measurement-free ground: "across 2c03's real rows the column sums to **95** while the 5% it is missing (tutorial attendance) **has no row at all**, and two rows carrying 1% are bonuses added outside the 100. **A rendered column of shares therefore reads as a partition that it is not.**"

**Standing.** **Settled name in practice, open name by ruling.** S1 registers three names as an unnoticed drift; `design.md §7` item 1 records it as a known open item with an owner. So it is not drift - it is a deliberate deferral. → **C34**. **Note the load-bearing clause in the exemption's own reason** - "workload is judged from progress plus size" - which is the mechanism `write-rules.md §3.4` later removed. → **C35**, escalation.

## M48. `grade_share_conditional`, and the conditional-weighting defect

- **`derivation/FINDINGS.md §3`, `[A1, A2, A3]`, 2026-08-22** (S3 §14). "**Conditional grade weighting** - '10/10/30 **or** 0/0/50, whichever works out better for you' - **a rule, not a scalar. This is exactly the allocation planner's input.**"
- **`model.md §10` item 9, 2026-08-22** (S1 thing 35). "`weight` is now a field; **the conditional form is not yet expressible.**"
- **`model.md §10.9`, `RESOLVED for conditional weighting - Billy 2026-08-23`, `[R]`** (S1 thing 35). "Billy ruled **the minimal fix**: `worth_percent` keeps its value and gains a `conditional` marker **plus a pointer to the rule**, so no reader can take the stored number for a stated fact. **Billy rejected the general form** - a `weighting_scheme` naming the alternatives with a derived weight - as over-built." Why it escalated: "**the top-ranked faithfulness defect** - 24 claims across 17 runs… With rank 6 (a floor restated as a point value) it is 29 of 77, **38% of every measured faithfulness failure**. … **the agent acts on a note that NEGATES a field and cannot act on a note that makes a field CONDITIONAL.**" An overstatement is corrected in place: "The often-repeated *'four delivery paths'* phrasing is an **overstatement corrected by adversarial review** - two mechanisms, two of them n = 1."
- **`schema.md §3` and changelog 2026-08-27, Billy, ruled** (S2 T11). "bool, **nullable**… **Null means unknown**, never *not conditional*." · "Covers both `10/10/30 or 0/0/50` and *'worth at least 30%'* - **a bound is the same defect as a conditional**." · "**The rule may optionally be left on a one-line sticky note; requiring one is not a rule, because a schema rule that manufactures a conflict nobody would care about is a defect in the rule.**"
- **`design.md §7` item 1** (S2 T11). "The conditional-weighting fix ships as `grade_share_conditional`."

**Standing.** **Ruled twice, four days apart, and the second narrows the first.** Billy's 08-23 ruling makes the fix "a `conditional` marker **plus a pointer to the rule**"; Billy's 08-27 ruling makes the pointer **optional**, on the "must not chase the agent" ground. The later ruling wins by recency; the narrowing is worth naming because the pointer was half of what made the marker actionable, and the 38% defect is what the marker exists to fix. → **C36**.

**The late-day budget - and it is now resolved.** S1 (thing 35) records "12 late days, at most 3 per assignment" as explicitly **NOT resolved** and staying open. S3 (§14) records it as "a **course-level consumable resource that modulates every other obligation's effective deadline**. 'Can I be late on A5, and what does it cost me later?' **has nowhere to live.**" `design.md §3.2` (08-27) gives it a home: "course-level notes - **the late-day budget**, the snow-day credit, the conditional-weighting rule - must land and read back for F5 to pass." A course is a node; a note hangs on it by an `about` link. **Closed by a survey neither of the other two could see.** → **C37**.

## M49. `parts`

**The most-revised field in the corpus** (S2's own words), and the one carrying the corpus's sharpest live hole.

- **`derivation/FINDINGS.md §3`, `[A3]`, 2026-08-22** (S3 §14). "**Obligations decompose into independently assessed parts** - A6: 'if your cuckoo hashing doesn't work you can still get full marks for this report' (actual score 8/10). **`status` and `score` attach at the part, not the obligation.**"
- **`model.md §8` vocabulary, 2026-08-22** (S1 thing 40). `parts[] (independently assessed, carrying their own status and score)`.
- **`domain-design.md §6.1`, Billy, 2026-08-23, `[R]`** (S1 thing 32). Reader 1: "**Size is observed ordinally - from `parts` and item notes first**, then by asking for a relative comparison."
- **`model.md §7.1`, Billy, 2026-08-28, `[R]`** (S1 thing 40). Reader 2: what the coordinator needs arrives from "the copied fields (`name`, `due`, `grade_share`), **`parts` for which concepts it contains**, and the artifact's summary one hop away."
- **`schema.md §3` + changelog ×2, Billy, 2026-08-27, ruled** (S2 T12). "**It carries the CONCEPTS the obligation's source carries**, as raw strings, **never as pointers to concept nodes**." First changelog entry: "the field now has **two readers** and which one drives the wording is owed." Second, same day: "**`parts` carries concepts only; the ordinal size-judgment reader is not designed. It is deferred until a size-judgment need actually arises… This closes the two-readers question instead of leaving it owed.**"
- **`write-rules.md §3.4`, Billy, 2026-08-28, ruled** (S2 T12). "**`parts` carries concepts, and it does not carry size.**" A part is "**a concept worth capturing because it might occur elsewhere in the system**". "**Write the canonical, singular name of the concept, not the phrase the source used.**" `Stacks and Queues` → `Stack` · `Queue`. "Effect on one real course: **50 candidate strings became 28.**"
- **`ring-0.md §4`, 2026-08-28** (S2 T12). **Excluded from ring 0**: "it answers *what is this about*, not *where do I look next*, and under `write-rules.md §3.4` it carries concepts rather than size so **it does not answer *how much* either**."
- **`schema.md §7` graveyard** (S2 T49). "**per-part weights and per-part scores** - modelling sub-items costs more complexity than it returns. **Measured and knowingly given up** - 2aa4 A1 splits `5% / 2.5% / 2.5% / 5%` and A2 `3.5% / 3.5% / 5.5%`, and 6 of 9 2c03 assignments are two independently assessed parts. **`parts[]` therefore carries no status and no score of its own.**"
- **`schema.md §9` item 1, current body** (S2 D7). Still lists "**`parts` birth rules + prompt** - before anything writes the field" as **blocking a writer**, and does not cite `write-rules.md §3.4`, which was created the next day to be exactly that rule's home.

**Standing.** `parts` carries concepts, as canonical singular names; the size reader is **deferred, not retired**; per-part status and score are **graveyarded with the cost recorded**; A3's 08-22 finding is the measured evidence the graveyard entry cites without attributing. **The live hole**: `domain-design.md §6.1` retired `workload` *on the ground that size is observed ordinally from `parts`*, and `write-rules.md §3.4` then removed size from `parts` and deferred the reader. → **C35**, **C38**, escalation.

## M50. `optional`

- **`schema.md §3`, Billy, 2026-08-27, ruled** (S2 T13). "bool, **nullable**. True when nothing is lost by not doing it. **Null means unknown**, never *not optional* - a non-nullable bool forces the system to assert what no source stated. **Without it a plan ranks a +1% survey among required work purely by date.**"
- **`write-rules.md §3.5`, Billy, 2026-08-28, ruled** (S2 T13). "**`optional` defaults to false unless a source states otherwise.** The field stays nullable and null still means *unknown* - `schema.md §3` is unchanged. **This is a rule about the writer, not about the field.**"
- **`write-rules.md §1.2`, OWED** (S2 T13). Generalised: "**Absent is not unknown when a person would not hesitate - OWED.** §3.5 is the first instance of a pattern that probably generalises… Whether that is one rule or one rule per field is not settled."
- **`schema.md` changelog 2026-08-27, agent, agent-drafted** (S2 T13). The `optional` tally was dropped because it "**counted a fixture that was rejected as a golden set**."
- **`derivation/agents/2c03-obligations-and-edges.md` §nodes, `[A3]`, 2026-08-22** (S3 §14). Material: 2c03 has "15 rows for the whole course, **three of them optional**."

**Standing.** Current, cleanly layered - a schema fact (nullable, null means unknown) plus a write rule (default false) plus an owed generalisation. **Note the residual nullability ground**: the 08-27 ruling that made `optional` and `grade_share_conditional` nullable cited "**the same defect as rendering a null `progress.state` as `not_started`**" - and that analogy was reversed the next day (→ M51). The two fields were **not revisited**. → **C39**.

## M51. `progress` - its carrier, its kind, and its default

**Names:** `progress` (both corpora), "a fifth typed row" (rejected), "a sticky-note kind" (rejected), "an annotation with its own kind" (current).

- **`domain-design.md §1` ruling 6, Billy, 2026-08-21** (S1 thing 34). "**Progress is independent of obligations** (option B). Not all time is spent on assignments/exams; a topic inside a chapter can carry progress with no deliverable attached."
- **`domain-design.md §6` table, 2026-08-21** (S1 thing 34). A typed fact type: `id · course · target · open/closed · updated_at`, free text "where I am", `target` polymorphic.
- **Demotion to a sticky-note kind, 2026-08-23** - referenced in both domain files, **written out in neither**. Its two grounds are quoted: "*The ordinal invited invention*" and "*no mechanism reads it*".
- **`model.md §8.2` / `domain-design.md §6.2`, Billy, 2026-08-24, `[R]`** (S1 thing 34). "an **annotation with its own kind**, targeted by an `about` link, carrying `state` (an enum), `detail` (prose), `origin` and `updated_at`… `annotation` is a **tag, not a type hierarchy**." Both files state the demotion's grounds are "**answered, not overridden**".
- **`model.md §8.2`, Billy, 2026-08-28, `[R]`** (S1 thing 34, D14). The fix is restated: "the fault is fixed by a **DEFINED default**, not by rendering absence. **`state` is not nullable** and an obligation with no progress record reads as **`not_started`**."
- **`domain-design.md §6.2`, never updated** (S1 D14). Still carries "The first is a **defaulting** fault, **fixed by rendering null as absence**". `domain-design.md`'s changelog has no 08-28 entry for progress.
- **`schema.md §4.5`, Billy, 2026-08-28, ruled** (S2 T14, T15). The full ruling, with its own blast radius stated: "enum `not_started | in_progress | done`, **not nullable**… **There is no unknown state.**" Ground: "**a nullable state would make the system announce it does not know and give an agent a reason to ask, which `architecture.md §3` rules a defect in the rule.**" And: "**The prohibition this reverses came from a measured incident in which a run invented that default; a defined default is not an invention.** **Four body sites that used this case as their canonical example are rewritten.**" Plus: "Nothing needs to be written at creation - absence carries the default. The stored vocabulary is fixed; the rendering is per kind of target - *Submitted* for an assignment, *Written* for an exam."
- **`schema.md §4.5` three rules, with real enforcement points, 2026-08-28, agent, measured** (S2 T15). "one current value per target" → **the service**; "`detail` requires `state`" → **construction**; "only the owner authors it" → **nowhere, deliberately**. Changelog: "**The record had asserted all three were validated at construction.**"
- **`ring-0.md §4`, 2026-08-28** (S2 T14). "**It is never null and never absent from the projection**: an obligation with no progress record projects as `not_started`."

**Standing.** **Settled by explicit ruling: `schema.md §4.5` is the authority.** `domain-design.md §6.2`'s "rendering null as absence" is superseded and stale on one side of the domain corpus only - exactly as S1 flagged, and S2 holds the ruling that closes it. → **C40**.

## M52. `status` - the three-axis field, and why it is dead without being wrong

- **`derivation/agents/2c03-obligations-and-edges.md`, `[A3]`, 2026-08-22** (S3 §14). "**`status` is three orthogonal axes** - Completion / Score / **Evaluation Status**. A2 and A9 read 'Feedback: Unread'; A2 was submitted in January at 100%. **`status: done` erases a live, months-old, actionable item.**"
- **`model.md §8` vocabulary, 2026-08-22** (S1 thing 33). `obligation: due · status{completion, score, evaluation} · …`. Never revised.
- **`model.md §8.1`, Billy, 2026-08-23, `[R]`** (S1 thing 33). "the three-axis `status` finding: there a scalar `done` **erased** a live item."
- **`domain-design.md §9.1` + changelog 2026-08-25, agent, measured** (S1 thing 33). "`status` was dropped 2026-08-25." The only record of the drop, with no ruler beyond "agent - measured".
- **`schema.md §7` graveyard** (S2 T49). "`status.completion` · `files` · `score` · `evaluation` - **none of these is the system's burden. This does not contradict the finding that a three-axis status prevented two live items being erased; it moots it, since nothing is asserted.**" And a separate entry: "`status.evaluation` - reaffirmed against the challenge that *'what do I still owe attention to'* is a deterministic query returning A2 and A9. **That challenge's hidden premise is that unread feedback is worth attention, and the only authority on that says it is not.**"

**Standing.** **`obligation.status` is dead, and the finding behind it is mooted rather than contradicted** - the spec says so in exactly those words, and reaffirms the specific A2/A9 case against a specific challenge. `model.md §8`'s vocabulary and `model.md §4`'s ring-0 list are both stale on it, and `model.md` was edited on 08-28 without touching either. **Three surveys hold three pieces**: S3 the evidence, S1 the drop with no ruler, S2 the ruling with its reason. → **C41**.

**Do not confuse it with `progress.state`.** They are different fields on different kinds. `obligation.status` is graveyarded; `progress.state` is a non-nullable enum on an annotation and is in ring 0 in both bands. No survey states the distinction; both corpora use "status"/"state" loosely enough to invite the confusion.

## M53. `workload` / `hours_estimate` / `workload-estimate`

**Names:** `workload-estimate` (`domain-design.md §6` table), `workload` (`§9.1`, `§10.5`, `model.md §8`), `hours_estimate` (`§6.1`). Three names, one field.

- **`derivation/FINDINGS.md §3`, 2026-08-22** (S3 §14). "**`workload` is absent from every single obligation, in both courses, in every source.** No handout, portal cell, or announcement estimates effort. **This is the second independent falsification of that field** - Billy's own hand-maintained Notion table, kept for a year, also has no workload column and *does* have a `target_date` the schema lacks."
- **`domain-design.md §6` table, 2026-08-21** (S1 thing 32). Typed on `obligation`, read by M1 M2 M3 M5. And: "**The signal is the missing-rate of `workload` and `due`**, not a subjective feeling" (now struck through in place).
- **`domain-design.md §7`, open, 2026-08-21** (S1 thing 32). "**Where `workload` estimates come from.** Tilt: Billy states a rough number, revisable."
- **`PLAN.md` §Settled, 2026-08-22, agent, no attribution** (S5 A8, C10). Lists as ruled 08-22: "**`workload` is stated by Billy, nullable, never defaulted**" - one of the three build-spec §7 decisions Billy had **deferred** on 08-21 (S5 X5).
- **`domain-design.md §6.1`, Billy, 2026-08-23, `[R]`** (S1 thing 32). Billy verbatim: "hours_estimate 很难量化，我一般都是按照某个 assignment 的进度和 high-level 体量来判断的。" Three parts: (1) **not a field to be filled, its null is not a gap**; (2) "**Size is observed ordinally** - from `parts` and item notes first, then by asking for a relative comparison"; (3) "**Its missing-rate is retired as a guard signal. Replacement guard: faithfulness (§2).**" Adversarial correction attached the same day: "**asking is only a remedy for a quantity the user can answer, and Billy answers ordinal comparisons, not hour counts.**"
- **`model.md §8` vocabulary, NOT REVISED** (S1 D12). Still reads `workload?`.
- **`schema.md §7` graveyard** (S2 T49). "**the world does not supply it, it is not a unit anyone thinks in, and its null is not a gap. Size, where it matters, is observed rather than stored.**" Confirmed by `schema.md §9` item 4: "the fields an older grain named - `status` and `workload` - **do not exist**."

**Standing.** **Dead, on three independent grounds, at three dates: measured absent (08-22), Billy-ruled retired (08-23), graveyarded with a standing no-re-add rule (08-27/28).** `model.md §8`'s `workload?` is stale. **But its replacement mechanism is gone** - see M49 and **C35**. And note the sequencing oddity S5 found: `PLAN.md` records `workload` as *ruled* on 08-22 under a "do not re-litigate" heading, one day after Billy deferred it and one day before Billy retired it. Under merge rule 4 `PLAN.md`'s claim is weighed on content and date - and on content it is superseded within 24 hours. → **C42**.

## M54. `count{done, of}` and recurring obligations

- **`derivation/FINDINGS.md §3`, `[A1, A3]`, 2026-08-22** (S3 §14). "**Tutorial participation, 10 of 12, worth 5%** (0.5% each, capped, with a snow-day credit changing the denominator) - no `due`; status is a **count over twelve recurring events**."
- **`model.md §8` vocabulary, 2026-08-22** (S1 thing 40). `count{done,of}` (for countable obligations: tutorial participation, 10 of 12).
- **`schema.md §7` graveyard, two entries** (S2 T49). `count{done, of}`: "one instance in 22 … and it counts attendance-as-score, which the row above covers." **recurring / countable obligations**: "keeping them out explicitly is preferred to the complexity of representing them. **Known cost, recorded rather than argued away:** the `n=1` behind not carrying `count` was measured on **the two courses least likely to contain recurring items**, and 2px3 was excluded throughout."
- **`architecture.md §4`, Billy, 2026-08-28, ruled** (S2 T38). This row is load-bearing downstream: the old 22-obligation count "included **a row the graveyard forbids** (recurring tutorial attendance), so **22 is not reachable by re-running the old route**."

**Standing.** **Graveyarded with the cost recorded and the evidence base self-disqualified in the same entry.** The n=1 was measured on the two courses least likely to have recurring items, and the one course most likely (2px3, the `woven` profile that S3 §Origin names "the hardest case routing must survive") was excluded throughout - and by M21/C14 cannot now be read. → **C43**.

## M55. `label` - is it a name, a summary, or neither

- **`model.md §8` vocabulary, 2026-08-22, agent-drafted** (S1 thing 36). `label(free text, written once at ingest)` - on **every** node, unqualified.
- **`model.md §7.2`, Billy, 2026-08-23, `[R]`** (S1 thing 36, D2). "at ingest an LLM writes a document's summary, tags and sections, and **`label` is that output** - §8's *'label (free text, written once at ingest)'* means **written**, not **named**."
- **`model.md §7.2`, `UNRESOLVED, and it must not be smoothed over`** (S1 D2). "§7's own table above enumerates *labels, summaries, sticky notes* as distinct things, and §4's store column lists a separate `summary`. … **reconciling it with §7's enumeration was never done.**"
- **`model.md §7.1`, Billy, 2026-08-28, `[R]`** (S1 thing 36). "**an obligation carries no ingest-written summary.** … The 2026-08-23 adversarial objection - that §8's node line gives `label` to every node without qualification - **does not survive, because that node line is agent-drafted and never had standing to block a ruling.**"
- **`schema.md §3` / `ring-0.md §4`, 2026-08-28** (S2 T29). The field is `name`: "**the label a person recognises the row by. It is not the handle and nothing is derived from it.**"
- **`write-rules.md §3.1`, Billy, 2026-08-28, ruled** (S2 T44). "**There is no system-owned naming convention, and one is not owed. Write the label the source uses.** This was owed only because the `id` used to be minted from the name… **The id is now opaque and assigned, so nothing downstream depends on how a name is spelled.**"
- **`architecture.md §5`, Billy, 2026-08-28, ruled** (S2 T41c). "a summary is written only where a node's identity is content the skeleton does not hold - **the artifact, and nothing else in the current kind set.**"

**Standing.** **Substantially closed by three 08-28 rulings the domain corpus does not carry.** The current answer: the field is `name`, it is what the source prints, nothing is derived from it, and a *summary* is a separate written object that exists only for artifacts. `model.md §8`'s "label on every node" is disqualified by `model.md §7.1` itself and superseded by the spec. **What remains open** is the `label`-versus-`summary` *presentation* decision, explicitly named as "presentation's first one" and owned by a tier that does not exist. → **C8**, **C9**, **C44**.

## M56. What ingest produces, and who reads each part

- **`model.md §7.2`, Billy, 2026-08-23, `[R]`** (S1 thing 37). summary = "concise **at birth**, not trimmed later", read by the coordinator; tags = "implies an enum set - **deliberately not settled now**", read by filtering; sections + pages = "**not the coordinator's responsibility**". And: "A sticky note renders **together with** the summary. Whether that pairing costs too much is a token-optimisation question for later."
- **`domain-design.md §10.2`, Billy, 2026-08-22** (S1 thing 37). "**§5 ruled out a *manual* taxonomy, not an LLM pass at ingest.** Since a multimodal pass must run anyway - scans, `.docx`, `.pptx` - section labels are its byproduct… **Most of P2's negative findings were artifacts of testing a method nobody had proposed.**"
- **`step-minus-1/FINDINGS.md §P2`, 2026-08-22** (S3 §2). The honest verdict the domain record is reacting to: "the honest verdict is **not** 'prose extraction fails' but '**the cheap method fails on prose**'. 'First non-empty line' discards font size and position, which is where a heading lives in prose." Slide-shaped 39/40 (~97%); prose-shaped 12/26 (~46%). Self-limited: "**97% is real, but it is 97% of a single template**" - all three slide-shaped slots landed on one professor's deck.
- **`step-minus-1/FINDINGS.md §P2` sub-question 1** (S3 §3). "2px3 holds 11 `.docx`, 2 `.pptx`, 1 `.xlsx` against only 9 `.pdf`. **Both the design and the spec discuss the corpus as if it were PDFs throughout.** `pdftotext` covers none of the Office formats."
- **`openclaw:log/2026-08-21` §reversals item 10, agent** (S5 C8). The origin design: grouped retrieval by the document's own structure "so the heading *becomes* the semantic group label with **zero annotation** - which **Billy had already ruled out doing by hand**." Groups nest `course > week > file > section`.
- **Spec side: silent** (artifact and the whole ingest path are slice 2/3).

**Standing.** Current and deferred. **Note the residual S3 alone holds**: P2's pre-registered second stratum **never ran**, and no in-scope file records a decision to abandon it - so the 46% prose figure rests on one sampling accident, and the derivation's own title-scoped 2aa4 extraction was a de-facto second stratum that *did* work, which nobody connected. → **C45**.

## M57. `sticky_note` - shape, `category`, `origin`, `body`, timestamps

- **`domain-design.md §10.7` ruling 2, Billy, 2026-08-22** (S1 thing 41). "**Corrections are sticky notes, not precise updates.** … Co-location is enough because **Billy is in the loop reading it**. This kills the corpus-override layer the agent was drafting."
- **`model.md §8.1`, Billy, 2026-08-23, `[R]`, verbatim** (S1 thing 41). "sticky_note 既然能被 attach，那肯定能被 detach 或者 modify，并且要是便宜的…" → "**the maintenance point is the READ.** Attach, detach and modify are all cheap and symmetric because a note is **an entity that points at a node**, not a property of one."
- **`derivation/agents/2c03-obligations-and-edges.md`, `[A3]`, 2026-08-22** (S3 §19). Seven instances, "**their targets straddle all three layers**". **Four of the seven attach to a concept or an obligation, not to a section**, against design §10.7's ruling that the note attaches to the section. "Refinement, not a contradiction … the highest-value ones (the Dijkstra note) attach to a concept precisely because they **reconcile two artifacts that disagree**."
- **`schema.md §4`, 2026-08-27/28** (S2 T18, T19). `category` (renamed from `kind`): "string, **open set**… **Deliberately not an enumeration**, because the cases cannot be enumerated. **The values in use are not yet a usable vocabulary:** across the 11 notes that exist, **one value holds 8 of them** and the boundaries between the others do not reproduce." `origin`: "**Provenance does not confer immutability:** an annotation may be edited, and an edit carries `origin` forward by default." Target: "**not a field.** It is an `about` link." Timestamps: both, and "the pair plus the maintenance-at-read rule is **what makes a time-bound statement safe to store at all**: an undated sentence from the start of term goes on influencing judgment forever. … **In slice 1 that comparison has no input**, because the revision date belongs to a kind that does not exist yet."
- **`write-rules.md §4`, 2026-08-28** (S2 T18, T17). `category`: **OWED** - "**two independent passes produced two non-overlapping vocabularies.** No rule; the field stores what it is given." `origin`: **OWED** - "the schema's prose says *how the claim was obtained*; **both passes reached for *what document class it came from*.**"

**Standing.** Current and converging - the mechanism is Billy-ruled twice (08-22 co-location, 08-23 maintenance-at-read), the shape is spec-ruled, and two write rules are owed with their evidence stated. **A3's 08-22 refinement is now the rule**: the note targets a node polymorphically via `about`, not a section. **Note the two records give different evidence for the same owed item** and neither cites the other: `schema.md` cites a distribution over 11 notes, `write-rules.md` cites two non-overlapping vocabularies from two passes. → **C46**.

## M58. What a sticky note is worth writing - the render test

- **`write-rules.md §4.0`, Billy, 2026-08-28, ruled** (S2 T45). "> **'Is it worth being written down so that every time I look at this node, the note comes with it?'** That is the whole rule. **A note is not a place to put things that are true; it is a thing that appears every single time its target is read.**" Measured on one course: **20 candidate notes became 12.** What failed: course-wide administrative policy, a restatement of what an assignment consists of, and **every erratum about a handout revision**, "which mattered on the day and never again."
- **`write-rules.md §4.2`, Billy, 2026-08-28, ruled** (S2 T46). `body` is "a concise self-contained summary, never a quotation. **Because a note renders inside the node it hangs on.**" Measured example: a 40-word announcement becomes "*+1 bonus for filling in every question. Open until the end of the day Friday, March 27.*"
- **`schema.md §4`** lists `erratum` among `category`'s example values (S2 D13) - the class §4.0's measured pass most consistently discards.

**Standing.** Current, Billy-ruled, evidence-derived. → **C47** for the `erratum` collision.

**`⟂container`.** The test is written in the first person about a human reading: "**every time I look at this node**". In the plugin container the reader is an agent, for which "comes with it every time" has a different cost.

## M59. A length bound on notes, and on the second unbounded route

- **`model.md §10` item 5, 2026-08-22, owed** (S1 thing 45). "**A length bound on sticky notes.** ~~The only route~~ by which unbounded free text can enter a resident skeleton."
- **`model.md §10.5`, `WIDENED 2026-08-24`** (S1 thing 45). "*'the only route'* is false. **`label` is a second unbounded route** … it now gates `domain-design.md §9.2`'s symmetry rule: **eight one-line summaries can be pulled for a comparison set; eight paragraphs cannot.**"
- **`model.md §10.5`, `MEASURED 2026-08-28`** (S1 thing 45). "*Real samples are short* is false. The 11 notes of the 2c03 corpus run **87 to 278 characters**, against the **~90** that `spec/write-rules.md §4.2`'s worked compression produces, and rendering the course level puts **871 characters** of course-scoped notes ahead of its first obligation row. **The bound is owed out of the presentation cycle rather than settled in advance.**"
- **`schema.md` changelog 2026-08-25, agent, agent-drafted** (S2 T19). "the sticky-note length bound **demoted from `[R]` to owed**. **No ledger anywhere supports the ruled standing**, and every other record has it as *owed*."
- **`schema.md §9` item 3 / conditions line** (S2 T19). "**It covers two routes, not one**… **The number is load-bearing: it gates whether the symmetry rule is affordable.**" Conditions: "has **no settled standing and no measured number**."
- **`write-rules.md §4.2`, 2026-08-28** (S2 T19). Its shape without a number: "**the bound follows from what a rendered node can carry, not from a number chosen in advance.**"

**Standing.** **Owed, on both sides, with the same shape and the same gate.** This is a two-corpus convergence: the domain record measured it (87-278 chars, 871 at the course level) and the spec record demoted it from ruled to owed and stated its shape. Neither cites the other. → **C48**.

## M60. `time_point`, and "the current plan"

- **`domain-design.md §6` table, 2026-08-21** (S1 thing 29). `time-point` is one of the five fact types. "Obligations and time-points are separate because **only obligations consume the weekly hours**."
- **`domain-design.md §9.1`, 2026-08-21, later confirmed a ruling** (S1 thing 51). "The projection carries **every course's obligations, time-points and the current plan**, with no free text."
- **`model.md §7`, 2026-08-22** (S1 thing 51). The retraction rests on this entity list: "§9.1's projection was always `obligations · time-points · plan`, i.e. ring 0."
- **`schema.md §7` graveyard** (S2 T48). "**Not in slice 1.** The type is real - an exam sitting, a review session and a conference are three fixture instances - and is separate from `obligation` because only obligations consume the weekly hours. Its reader is the **calendar projection**, which is itself out of slice 1; **the type is out because the projection is, not because nothing reads it.**" The only graveyard entry whose reason is deferral.
- **`ring-0.md §7`, 2026-08-28** (S2 T30b). "**`time_point` and 'the current plan'**, both named by `domain-design.md §9.1` as part of the projection. `time_point` is not in slice 1; **the plan has no representation anywhere**, and this record does not invent one."

**Standing.** **Two of the three entities `domain-design.md §9.1` names as the projection are not in ring 0.** `time_point` is deferred with a stated reason. **"The current plan" has no representation anywhere in the corpus** - and the plan is the coordinator's *only substantive work* under `domain-design.md §9.3` ("plan generation - its only substantive work, because it *is* coordination"). S1 records the entity list as the thing that survived the grain's death; S2 records that two thirds of it is missing. → **C49**, escalation.

## M61. `has-more`

- **`ring-0.md §4`, 2026-08-28** (S2 T29; verified by zoom). "**`has-more` is new and nothing writes it yet.** Its motivation is measured on the real corpus: **6 of 14 obligations carry an annotation and 8 carry none**, so a `look_at` costs the same call and returns nothing new on more than half the rows. Whether it is a boolean, a count, or a set of present link kinds is **not decided here**." The table's why-column: "**the only one here that no record has yet declared.**"
- Corrected in place, `ring-0.md` changelog 2026-08-28: the counts "were **6 of 14 carrying an annotation, 8 without** - not 5 and 9… **Both found by the next sitting reading the corpus rather than this record.**"

**Standing.** **A field declared in a projection that exists in no schema record**, said so by the record that declares it. Newest material, uncontradicted, incomplete. Genuinely open. → **C50**.

## M62. The graveyard itself

- **`schema.md §7`, header verbatim** (S2 T49). "**Deliberately absent - do not re-add without a new ruling.** These fields are not carried. **A later session reading an older document must not restore them.**" Fifteen entries. Record conditions line repeats the standing rule.
- **S2's own audit of it.** "Every count in this table is stated over the 22-row fixture or the two-course corpus, both of which `architecture.md §4` (2026-08-28) says are superseded, and one of which `schema.md`'s own 2026-08-27 changelog calls '**a fixture that was rejected as a golden set**'. **The graveyard's ruling stands under the no-re-add rule; its arithmetic rests on material two other rulings have set aside.**"
- Also: "for thirteen of fifteen, **no changelog line**" - so for most rows the removing ruling is only the row's own stated reason.

**Standing.** **The mechanism is current and is the corpus's only standing anti-regression device.** Its evidence base is self-disqualified. This is the single most important thing for a downstream reader to hold: the graveyard's *rulings* are binding under merge rule 3; its *numbers* are not. → **C51**.

## M63. `obligation.notes`, and the non-overlap rule

- **`schema.md §7` graveyard** (S2 T49). "under the **non-overlap rule**: a **negative** definition (*'everything no mechanism reads'*) cannot be non-overlapping, and across the 22 fixture rows it carried **six unlike purposes**. **All free text lives on annotations**, which carry `created_at`/`updated_at` and a maintenance-at-read rule."

**Standing.** Current. It is the mechanism that makes M43's one-free-text-field rule tractable: there is no catch-all field, so free text has one home per kind and one home overall (annotations).

## M64. Fields removed with no stated reason, and one with a homeless requirement

- **`schema.md §7`** (S2 T49). `stated_in` / `source_ref`: "**Not carried**" - no reason given. **release dates** (2 of 9, printed on the acceptance screenshot itself): "noise." **`course` free-text field**: "nothing identifiable would go in it." **`term_start`**: "one week-relative obligation in 22." **`due_precision`**: "the distinction lives in `due`'s own type." **coarse dates** (*"April 2026"*, the Final Exam): "a date that is not fixed is null. **The term's largest obligation therefore stores a null `due`.**"
- **`course.offering_term` · `course.prereq`** (S2 T49): "null for both courses in the fixture, and **`offering_term`'s justification is another domain's need, in a domain that does not exist**."
- **`domain-design.md §0.6`, 2026-08-21** (S1 thing 83). Against which: "Winter-only mandatory courses ruled out a winter-27 co-op, and thereby set the entire recruiting target to summer 27… **Fairy never held the fact - because no home existed for a constraint spanning academics and career.** So the academic domain must hold **course offering-terms and prerequisite structure**, since that graph gates other domains' decisions. **This is the single most concrete design input carried in the originating dispatch, and it is why 'just track my deadlines' is the wrong target.**"

**Standing.** **The fields are graveyarded; the requirement is homeless.** §0.6 is the strongest statement in the domain corpus of why the system is not a deadline tracker, and its three carrier fields are gone - two by a spec ruling whose reason ("a domain that does not exist") is a container fact, one (`manifest`) by measurement. **Nothing in either corpus says what now holds offering-term and prereq, or whether §0.6's requirement survives.** → **C52**, escalation.

## M65. Where the reasoning lives - the changelog gap

- **S1's coverage finding, confirmed.** `model.md` has 6 changelog entries, `domain-design.md` 5, all dated 08-25 or 08-28. "the changelogs cover only the 2026-08-25 import housekeeping and the 2026-08-28 corrections, so **the reasoning for everything decided 08-21 through 08-24 lives in in-place banners rather than in the changelog.**"
- **S2's contrast.** The spec records carry **54 changelog entries** across five files (21 in `schema.md` alone), and S2 found all four live contradictions "**from the changelogs, not from suspicion**."
- **Two rulings exist only in a changelog and in no body** (S1): the ±1-2 week window's resolution (→ M3, now re-homed to `ring-0.md §3`) and why `domain-design.md §6`'s table was flagged rather than rewritten - "**Flagged rather than rewritten, because rewriting the table is a schema decision and not a migration.**"
- **The corpus names its own hazard three times** (S2). "Recorded because a plan that predates the split still reads as authority" (`architecture.md §4`); "**a divergence between two ruled records that nobody had propagated**" (`schema.md` 08-28); "**The error: the archive's §14.4 was read as the current state of the question without opening the changelog of the record that owns the field**" (`write-rules.md` 08-28).

**Standing.** This is a property of the corpus, not of the domain, and it governs how everything above should be read. **"Check the changelog for the reasoning" works for `records/spec/` and fails for `records/domain/` before 08-25.** → **C53**.

---

# Cluster D - The observation contract: ring 0, residency, the coordinator

## M66. What ring 0 IS

- **`model.md §4`, 2026-08-22, agent** (S1 thing 6). "ring 0 / obligation layer … owns time and commitment."
- **`domain-design.md §9`, Billy, 2026-08-23** (S1 thing 51). A reviewer's point Billy recorded and did not overturn: "§9.1 enumerates the projection positively and removes one thing (free text) with a reason. **It never says 'ring 0', and the gloss *'ring 0 was arrived at by subtraction'* is a later paraphrase, not this section's words.**"
- **`model.md §7`, Billy, 2026-08-22, `[R]`** (S1 thing 51). "**The coordinator holds ring 0 resident and *queries* the skeleton on demand. It does not hold the skeleton.**" Its retraction of an agent draft rests on the equation "§9.1's projection was always `obligations · time-points · plan`, i.e. ring 0."
- **`schema.md §3` / `design.md §3.0` / `ring-0.md §1`, 2026-08-27 to -28** (S2 T6). Three records, one claim, no drift - S2 calls it "the most stable statement in the corpus": "**Ring 0 is the obligation layer**, held resident by the coordinator. **It is not a separate store: residency is an access policy over `obligation` nodes.**" And `ring-0.md §1`: "Its job is **routing, not deciding**. From ring 0 alone the coordinator must be able to tell **where to look next**."

**Standing.** **The definition is settled** and the domain-side objection is answered: the spec does not paraphrase §9.1, it states the equation as its own claim in three records. **The contents are not settled** - two of §9.1's three entities are missing (→ M60, C49). So S1's D15 splits: closed on the definition, open on the membership. → **C54**.

## M67. Ring 0's field set - seed entry 2, closed

**Names:** "the projection grain", "ring 0's field set", "the dead grain", "band A / band B fields".

S1 (thing 52) records **four non-identical lists** and says the authoritative one now lives at `spec/ring-0.md`, outside its boundary. S2 read `ring-0.md`. **The two surveys hold the two halves of one answer, and it closes.**

The four superseded lists, for the record:

| list | where | date | standing |
|---|---|---|---|
| `label / due / status / workload` | `domain-design.md §9.1` | 2026-08-21 | **dead**, declared so 2026-08-25; "no replacement grain is ruled" |
| `due · workload · status · course` | `domain-design.md §10.5` | 2026-08-22 | `workload` struck by §10.5's own `THE GUARD CHANGED` banner |
| `due · status · course · plan` | `model.md §4` | 2026-08-22 | agent-authored, never revised; `status` graveyarded, `plan` has no representation |
| `due · status{} · weight · target_date? · workload? · parts[] · count{}` | `model.md §8` | 2026-08-22 | vocabulary block, never revised; three of seven are graveyarded |

**The authoritative list** (`ring-0.md §4`, 2026-08-28, Billy direction / agent table, `mixed, marked per section`; verified by zoom):

| field | band A "active" | band B "known" |
|---|---|---|
| `course` | ✅ | ✅ |
| `name` | ✅ | ✅ |
| `due` | ✅ | ✅ |
| `state` | ✅ | ✅ |
| `optional` | ✅ | ❌ |
| `done_by` | ✅ | ❌ |
| `has-more` | ✅ | ❌ |
| `parts` | ❌ | ❌ |
| `grade_share` · `grade_share_conditional` | ❌ | ❌ |

Per-field reasons are in M45, M46, M47, M49, M50, M51, M61. **`ring-0.md`'s own conditions line:** "This record fills a vacuum: `domain-design.md §9.1` states that its own field grain is dead and that **no replacement is ruled**. **It supersedes nothing; it answers what §9.1 left open.**"

**Standing.** **Closed by recency and by an explicit self-positioning statement.** The four older lists are superseded; three of them contain fields the graveyard forbids. **One residual, which S2 found and S1 could not:** `schema.md §9` item 4 still lists "**A projection grain, owed to slice 4**" as owed, and does not cite `ring-0.md`, which was created the next day and is exactly that grain. → **C55**.

## M68. The membership test

- **`domain-design.md §9.2` `RESTATED` block, agent** (S1 thing 28). "*an observation earns its place if and only if a judgment demonstrably changes when it is present.*" Marked "**agent formulation, obtained by lifting the rigidity rule one level, not separately ruled**". Testable "by running the same task with and without the observation".
- **`ring-0.md §2`, 2026-08-28, agent-drafted** (S2 T27). "> **A field belongs in ring 0 if and only if, without it, the coordinator cannot decide where to look next.**" It explicitly declines the domain test: "it is deliberately **not** the test `domain-design.md §9.2` offers. **That one has been run and returned nothing:** `findings/read-cycle.md §4` reports `parts`, `grade_share`, the skeleton, a complete ring 0 and `progress` as **each read, each rendered, none changing the plan's shape**."
- **The null result refused in both directions** (S2 T27). "**That null result does not license removing the fields, and it does not confirm the routing test either.** The instrument could not have detected the effect: every run was a memoryless `claude -p` cold start, and **the design's coordinator is long-running**… all ~40 runs used one fixed prompt… and the two courses are the same shape. **A device that cannot exercise routing returns 'nothing changed' whether or not routing matters.**"

**Standing.** **Both tests are agent formulations and neither is ruled** - which is a merge finding neither survey could make. S2 reads `ring-0.md §2` as declining a domain-record test, and could not know that test is itself self-declared "not separately ruled". S1 records the domain test's unruled standing and could not know it had been declined and replaced. So there is **no ruled membership test for ring 0**, only two agent proposals, one of which produced the current field set. Under merge rule 3 both are honoured as unruled. → **C56**, escalation candidate.

**`⟂container`, sharply.** The refusal of the null result rests entirely on the container: `claude -p` cold starts cannot exercise a long-running coordinator. **In the plugin container, a memoryless cold start is not a broken instrument - it is the container.** If the coordinator is not long-running, the null result is not disqualified and the field set loses the argument that protects it.

## M69. The symmetry rule (formerly "allocation reads ring 0 only")

- **`domain-design.md §9.2`, 2026-08-21, later confirmed a ruling** (S1 thing 53). "**All five courses' views must be isomorphic and fixed-depth. Uniformly shallow beats one deep and four thin.**" With the dispatch escape: "the coordinator **dispatches an estimate** and receives back a value *in the same shape as the other four*."
- **`model.md §7` mechanism 1, 2026-08-22, agent, now struck through in place** (S1 thing 53). "~~**Allocation reads ring 0 only.**~~"
- **`model.md §7` / `domain-design.md §9.2`, Billy, ruled 2026-08-23, written in 2026-08-24** (S1 thing 53). Replaced by the **symmetry rule**: "*observe anything you can afford for every course at once; never observe anything you can only afford for one.*" **What forced it:** "the slice-1 blind run gave the planner an observation space of deadlines and weights alone and it produced a date-ordered queue, **which says more about the observation space than about ring 0**. **The invariant was never shallowness - it is uniformity** … **Ring 0 returns to being the layer that is RESIDENT, not the definition of what is observable.**" Plus: "**Symmetry is scoped to the set the judgment ranges over**, not unconditionally to all five courses."
- **The derivation of why ring 0 was wrong** (`domain-design.md §9.2`): "Ring 0 was arrived at by subtraction … **and that subtraction presumed we already knew what coordination needs.**"
- **Standing recorded in both files because it was contested** (S1 D6b): "this began as an agent proposal that overrode a ruled entry, was flagged by adversarial review as unruled, and was **then ruled by Billy on 2026-08-23**. `openclaw:fall26/2026-08-23-slice-1/doubt/RECONCILE.md §5` still lists it as open and **is stale on that point**."
- **What is NOT established** (`domain-design.md §9.2`): "§9.2's premise that a thin line drives an estimate request remains **untested**… **Neither supported nor refuted.**"
- **`ring-0.md §5`, 2026-08-28** (S2 T30). The rule made operative and used to convict the implementation: "the grouping key is a parameter… **because `domain-design.md §9.2` scopes the symmetry rule to *the set the judgment ranges over*.**" And: "**The tiebreak is the handle, never file order.** Array order is insertion order is write history, and §9.2 rules out asymmetry that comes from interaction history. **The order measured in `findings/read-cycle.md` was array order, so the projection has been violating that rule rather than lacking a rule.**"

**Standing.** **Current, Billy-ruled 08-23, and now operative in the newest record.** `RECONCILE.md §5`'s staleness is a fact both domain files record and neither can fix; S2 confirms the rule is live in `ring-0.md`, which settles it as stale rather than open. **A finding S1 could not have:** the projection has been *violating* the rule in its ordering, and that was discovered on 08-28 by a record built on the rule. → **C57**.

## M70. Grouping and order in the projection

- **`ring-0.md §5`, Billy, 2026-08-28, ruled** (S2 T30). "**Grouped by `course` by default, and the grouping key is a parameter.**" · "**Within a group, order by `due` ascending, nulls last; among nulls by `done_by`; ties broken by the handle.**" · "**`due` is the primary key, not `min(due, done_by)`**" · "**Nulls last gives an undated obligation a defined position**, which a bare date order does not have and which is the recorded objection to date ordering."
- The second read the grouping parameter serves - *what is due across every course this week* - is "the one `evidence/2026-08-27-tier-recut/derivations/L3-surface.md` records as **missing entirely**."

**Standing.** Newest material, uncontradicted, and the only place in the corpus that specifies an order. No domain record touches it.

## M71. The two bands and the active window

See **M3** for the window's provenance. The partition itself:

- **`ring-0.md §3`, Billy, 2026-08-28, ruled** (S2 T28; verified by zoom). Band A "active" fires on any one of three triggers; band B "known" is everything else, **including obligations with no date**.
- "**Two bands do not violate uniform depth.** The partition is computed from material facts plus one rule applied identically to every course, so it carries no interaction history."
- "**An undated obligation is in band B, and that is not a hazard.** It is present, it is routable, and its detail is one call away. **The system holds no notion of an obligation's importance - `grade_share` has no reader by standing exemption - so a rule that promoted 'important' undated rows would be asserting a judgment the system is ruled not to make.**"

**Standing.** Current, and internally consistent with the symmetry rule and with `grade_share`'s exemption. Uncontested. **Note it depends on M47's exemption** - if `grade_share` ever gets a reader, the band rule's stated ground disappears.

## M72. Expansions are discarded, never sedimented

- **`domain-design.md §9.1`, 2026-08-21** (S1 thing 54). "Retrieval on demand is only half the fix - **the other half is *not sedimenting* what was retrieved.** … Depth is added only inside ephemeral subagents, and does not come back."
- **`model.md §7` mechanism 2, 2026-08-22** (S1 thing 54). "Optional when the skeleton was resident; **mandatory now.** Without it a long-running coordinator converges on held-everything *plus* path-dependent bias - both costs, no benefit." And: "The store boundary remains the chokepoint for **content**; **discard discipline is the new one for structure.**"
- **Explicitly untouched by the symmetry replacement** - both `model.md §7`'s `REPLACED` banner and `domain-design.md §9.2`'s `RESTATED` block say so.
- **`domain-design.md §9.1`, Billy, 2026-08-24, `[R]`** (S1 thing 51). "**the symmetry rule does not conflict with this.** §9.1 governs the **view**… The symmetry rule governs what a **judgement** may observe inside its own scope, and those observations are **transient**… **The view does not deepen precisely because what is fetched is dropped.**"
- **`ring-0.md §1`, 2026-08-28** (S2 T26). Inherited verbatim: "**What is fetched is dropped, never sedimented.**"

**Standing.** Current, Billy-ruled 08-24, inherited by the newest record. Uncontested in all four surveys.

**`⟂container`.** "Sedimenting" presumes a context that persists between reads. A per-invocation agent sediments nothing by construction, which makes the mechanism either free or meaningless depending on the container.

## M73. Progressive disclosure and what the coordinator holds resident

Covered at **M6** (the philosophy) and **M66** (what ring 0 is). The residency claim itself:

- **`domain-design.md §9.1`, 2026-08-21** (S1 thing 51). "**The coordinator's view is fixed-shape and uniform-depth. It refreshes as facts change and never deepens.**" · "the coordinator's persistent memory holds **pointers and summaries, never content**."
- **`model.md §7`, retraction, 2026-08-22** (S1 thing 51). "An agent draft had the coordinator holding the whole skeleton resident. **Retracted.** … Billy's earlier correction was that a node's summary *can be called*; that was elaborated into *is permanently held*, which the design never said."
- **`ring-0.md §1` / §7, 2026-08-28** (S2 T26, T30b). "**ring 0 is resident for the coordinator and for nobody else.**"

**Standing.** Current by date, everywhere. **`⟂container`, and this is the hinge.** → **M74**, **C58**, escalation 1.

## M74. Is the coordinator long-running? - and is its lifetime allowed to decide anything?

**The largest cross-survey collision in the corpus, and the one container drift lands on hardest.**

- **`openclaw:log/2026-08-21` §reversals item 6, Billy, explicit `(Billy)` tag** (S5 item 14). "**The coordinator is long-running, not booted per session** (Billy). The agent's two-stage assembly-at-boot model died; the *projection* survived, restated as a standing constraint - fixed shape, uniform depth, never deepens."
- **`domain-design.md §1` ruling 11, Billy, 2026-08-21** (S1 thing 46). "Billy faces one persistent, high-level, conversational master session; depth only exists in freshly opened, targeted subagents."
- **Restated four more times in `domain-design.md`** (S1 thing 46): §5 ("The 'master session' is a **long-running coordinator**, not a per-session boot (corrected 08-21)"); §9.1 ("An earlier draft had a two-stage assembly at session start. **That was wrong**"); §9.5 ("**do not try to make it survive a semester.** Its long-running scale is **days-to-weeks**"); §9.3 ("This is the only reason it can run long - **purity is not fastidiousness, it *is* the longevity mechanism**").
- **`PLAN.md` §Settled, 2026-08-22** (S5 A8). §9 is listed settled and closed to re-litigation.
- **`design.md §5` conclusion 1, 2026-08-27** (S2 T31, D14). The opposite instruction, and it is stated as a guard: "**The coordinator's lifetime is not a deciding fact here, and must not be reintroduced as one:** the one-persistent-session decision is about the **conversation's** lifetime… and says nothing about a process holding the graph in memory. **The skeleton and its verbs are invoked on demand; every call may be a new process.**" Its cost model depends on this: "the load is cheap enough that **per-invocation and resident are indistinguishable**" - 2c03's 138-node graph is 52 KB and parses in **0.27 ms**.
- **`design.md §5`, the asymmetry it draws from that** (S2 T33). "**And the asymmetry between 1 and 2 is a hard boundary, not an optimisation.** … Under a resident-process assumption that difference reads as tuning; **under the real one it is the reason the two sides get different mechanisms.**"
- **`ring-0.md §1` / §2 / §7, 2026-08-28** (S2 T26, T27). Leans the whole way the other direction: ring 0 is "held **resident** by the coordinator"; "losing the coordinator costs **one projection read** to rebuild"; and the refusal of `read-cycle.md`'s null result rests on "every run was a memoryless `claude -p` cold start, and **the design's coordinator is long-running**."

**Standing.** **Not a contradiction on the records' own terms** - `design.md §5` distinguishes the *conversation's* lifetime from a *process* holding the graph, and is careful to say so. **But the two records use "the coordinator" for different objects one day apart, and the newest record (`ring-0.md`, 08-28) leans on residency in exactly the way `design.md §5` (08-27) forbids reintroducing.** Neither cites the other. Recency does not settle it: `ring-0.md` is newer, `design.md`'s clause is a guard written specifically against being overridden, and both are within one day.

**And container drift lands on the premise both share.** Billy's 08-21 ruling describes a human sitting in front of one persistent conversational session. In a Claude Code plugin the coordinator *is* an agent session whose lifetime the plugin does not own, and `claude -p` cold starts - the thing `ring-0.md §2` disqualifies as a broken instrument - are closer to the successor container than to the one the ruling described. If residency does not survive the container, the following go with it or must be re-derived: ring 0 as "the layer that is resident" (M66, M67), the membership test's protection from the null result (M68), the discard rule's purpose (M72), disposability as an acceptance criterion (M11), and ring 0's size bound (M11). → **C58**, escalation 1.

## M75. Who may touch what - the data-flow rule

- **`domain-design.md §9.3`, 2026-08-21, named an agent draft by §9's header** (S1 thing 50). A responsibility table: coordinator does conversation/judgement/advice, dispatching, **plan generation ("its only substantive work, because it *is* coordination")**; ingestion subagent returns "**one-line receipt**"; deep-read subagent returns "**the conclusion, never the material**"; task subagent returns "one-line status". "**Derived tool surface for the coordinator: read the fact projection · write plans · dispatch. No corpus retrieval, no file reads, no fact writes.**" And: "**subagents swallow the process and emit only conclusions.**"
- **`openclaw:fall26/README.md`, 2026-08-22** (S3 §20). The same contract, stated as the repo's subagent discipline: "**subagents swallow the process and emit only conclusions**"; a `TASK.md` is written to be handed to a subagent verbatim.
- **`PLAN.md` §What it is responsible for, question 3, 2026-08-22, agent** (S5 A3). "The coordinator reads the summary and writes plans, nothing else. Ingestion writes. Deep-read searches… **the coordinator stays pure because it does not *have* the other tools.**"
- **`model.md §7`, 2026-08-22** (S1 thing 50). Generalised off topology: "The invariant is a **data-flow rule, not an agent topology**… > **Store output enters the coordinator only as a conclusion; the context that produced it is then discarded. Who produced it is irrelevant.**"
- **`model.md §7`, Billy, 2026-08-22, `[R]`** (S1 thing 50). "the coordinator may not call the store (context pollution), but **rendering a node's own concise summary is a skeleton read and is obviously allowed** - otherwise it cannot read or analyse anything."
- **`architecture.md §1` / §7, Billy, 2026-08-27, `[R]`** (S2 T35). Re-cut entirely by the tier split: "**The application tier has no surface.** Its methods sit there as callable service methods, and **when they are called we expect them to be called correctly.** A method does not defend itself against a caller that should not have called it."

**Standing.** **The data-flow rule is current and is the durable form; the topology is superseded twice.** `model.md §7` (08-22) generalised it off agent topology; `architecture.md` (08-27) re-cut it onto tiers, where "who may touch what" becomes a question about which tier calls which and the answer to "who enforces it" is explicitly *nobody, by design*. S1's D17 ("the coordinator's tool surface is three items or four") is dissolved by the tier split rather than resolved. → **C59**.

**`⟂container`.** The whole responsibility table names agent roles the successor container may not have.

## M76. `look_at(node_id, question)` - the coordinator's material verb

- **`model.md §7.1`, `PROMOTED 2026-08-24 (ruled 2026-08-23)`, Billy, `[R]`, verbatim** (S1 thing 55). "给 A2 obligation 和它的 child 加一个 edge 不就行了？agent 看到了 A2 obligation node，因此它想知道具体的 spec 是去顺着那个 node 走一遍，不需要做整个 corpus 的 find_material。" The finding: "**The edge already exists** - §8's `obligation → artifact (spec, role ∈ {given, owed})`. **Nothing is missing from the model; what was wrong was the operation**, and it was wrong in the slice-1 apparatus rather than in the design." Walk = "deterministic, O(degree), no store, no embeddings", coordinator ✅; search = ANN, "affordable once, not eight times", coordinator ❌.
- **Signature** (`model.md §7.1`): `look_at(node_id, question) -> { summary, sticky_notes[], edges: [{ role, direction, target_id, target_summary }] }`. **Hard constraint:** "**It returns no sections, no pages, no paragraph, no chunk.** … **the boundary is the tool surface, never self-restraint.**"
- **`model.md §8.2`, Billy, 2026-08-24** (S1 D26). Return shape revised without editing §7.1: "`look_at` returns `{summary, annotations[], edges[]}`."
- **`schema.md §4.6` + changelog, 2026-08-28, agent, measured** (S2 D4). The triple is **withdrawn from the schema record entirely**: "**It does not state the return shape, and the `{ summary, annotations[], edges[] }` it used to quote was not one.** That triple was written for an application-tier verb; **`look_at` is presentation**, and a **complete** contract has to say where a node's own typed fields arrive, which the triple never did - read as complete, **it makes `obligation.parts` look homeless**." The withdrawal has a demonstrated cost: "a reader concluded from it that `obligation.parts` had nowhere to be returned."
- **`architecture.md §7`, Billy direction / agent table, 2026-08-27, ruled** (S2 T24). `look_at(node, question)` is re-homed: **presentation tier**, "a composed view".
- **`design.md §4`** (S2 T47). `look_at` is on the must-not-build list for slice 1.

**Standing.** **The verb survives; both stated return shapes are withdrawn; the tier moved.** S1's D26 (`sticky_notes[]` vs `annotations[]`) is moot - the schema record retracted the triple as never having been a contract, `architecture.md` moved the verb to presentation, and no presentation tier exists. S1 could not see any of that. → **C60**.

**`⟂container`.** A named tool with an enforced parameter is a property of a tool registry. It is also the single most plausible survivor of the container change, since a plugin's tools are exactly this shape.

## M77. The `question` parameter, and its retirement condition

- **`model.md §7.1`, Billy, 2026-08-23, `[R]`, verbatim** (S1 thing 56). "预期猜测这个问题，不如 dev 模式让它调用的时候问出这个问题。" → "The question is **not to be predicted but stated at call time**, and the parameter is **required** so it is enforced at the tool surface rather than requested in a prompt."
- **Two honesty caveats recorded at the source** (S1 thing 56). "it **perturbs what it measures** … **but it must never later be reported as a finding**", and "it **doubles as a test of read-time filtering**."
- **`model.md §4.1`, Billy, 2026-08-23, `[R]`** (S1 thing 56). Retirement condition: "within the development cycle, once summaries answer the questions at some threshold, the parameter retires." The threshold itself is "**an agent proposal, both conditions required and the number explicitly flagged as arbitrary**": ≥80% of calls answered across one three-run arm, plus no new question kind. "The agent's position is that **(2) matters more than (1)**."
- **Spec side: silent.** `look_at` is presentation and not in the first build.

**Standing.** Billy-ruled, with the threshold self-flagged as arbitrary and unruled. **`⟂container`, heavily** - "dev 模式", "within the development cycle", "three-run arm" are all the old app's experiment apparatus, and the parameter's whole justification is enforcing a behaviour on an agent through a tool signature, which is the one mechanism that *gains* force in the plugin container.

## M78. A shape for returned conclusions

- **`model.md §10` item 4, 2026-08-22, owed** (S1 thing 59). "**A shape for returned conclusions.** 'Emit only conclusions' is a promise, not a mechanism, until the return value has a required form (`domain-design.md §9.2`'s estimate - *'a value in the same shape as the other four'* - is the template)."
- **`domain-design.md §9.6` `COMPLETED` block, Billy, 2026-08-23** (S1 thing 59). Extended to the user: asking Billy "is §9.2's dispatch with the **user** as target instead of a subagent, and **the return contract is unchanged** - a value *in the same shape as the other four*."
- **`design.md §3.6` / `architecture.md §7`, 2026-08-27** (S2 T41d, T24). One concrete instance exists: `land(candidates) -> Diff`, with outcomes "created · updated · unchanged · **CONFLICT**". "**`Diff` is the confirmation surface:** the dev-time confirmation toggle reads a `Diff`, and so does F2's conflict question - **one return type serves both**." Re-homed: `land()` is "a batch composition over entity CRUD; **`Diff`'s conflict question is a presentation adjudication**", and "**is therefore not in the first build.**"

**Standing.** **Still owed in general; one instance exists and is deferred.** `Diff` is the only typed return contract in the corpus and it is the template M78 asked for, in the one place it is needed most. Neither survey connects them. → **C61**.

## M79. The trust contract owed for generated content

- **`model.md §1`, 2026-08-22** (S1 thing 60). "§2's trust clause does not cover content the system *generates*. A proposed concept partition was never told to it. **A separate trust contract is owed for generated content - §7.**"
- **`model.md §7`, agent position, "Not yet ruled"** (S1 thing 60). "**the system proposes a partition, Billy disposes, and a wrong proposal must be cheap** - it degrades grouping, never destroys anything. Same asymmetry that made ingest judgment non-load-bearing."
- **`model.md §9`** gives it a concrete reader: `text_extractable`'s "reading mechanism is §7's trust contract: distinguishing a **quotation** from a **generated description**."
- **`model.md §10` item 6** narrows its scope by evidence: "Where a course does state it, the concept layer is extraction, not inference - **which correspondingly narrows what §7's generated-content trust contract has to cover.**"
- **`derivation/FINDINGS.md §1` H3, 2026-08-22** (S3 §11). The evidence behind that narrowing, first-hand: "**PASS on both courses, and both results are uninformative.**" `[A2]`: "*the partition is not induced, it is transcribed, and that is a weaker result than a pass.*"
- **Spec side: silent.** `concept` is slice 2.

**Standing.** **Owed, narrowed, unruled, and its scope depends on an untested hypothesis (H3, → M87).** → **C62**.

## M80. Multiagent - one justified use, two rejected

- **`domain-design.md §8`, 2026-08-21, marked "Raised by Billy; analysis below is draft, not ruled"** (S1 thing 57). "❌ per-course *expert* agents - what actually differs between courses is a working-instruction bundle, which lives in the preferences layer and loads with the scope. **Not an agent.** ❌ orchestration / master-slave - coupling is through the store. ✅ **context-isolated deep reads** … **This is justified by context economy, not expertise.**"
- **`domain-design.md §5`, 2026-08-21** (S1 thing 47). "There is no master/slave and no orchestrator - no control relationship, **only a scope parameter. Coupling is through the store, never through a call.**"
- **`model.md §7`, 2026-08-22** (S1 thing 57). Generalised away entirely: "The invariant is a **data-flow rule, not an agent topology**."

**Standing.** The analysis is self-declared draft and is honoured as unruled under merge rule 3. Its conclusion (context economy, not expertise) was superseded by generalisation, not by contradiction. **`⟂container`** throughout - and this is the thing whose container question is most nearly *the same question* as the plugin decision: a Claude Code plugin is exactly a bundle of working instructions plus tools, which is what §8 said a per-course expert agent should be instead of an agent. → **C63**.

---

# Cluster E - Inbound: ingestion, announcements, operations, capture

## M81. Ingestion is out of scope; Billy is the fetcher

- **`openclaw:log/2026-08-21` §reversals item 3, Billy, explicit `(Billy)` tag** (S5 item 12). "**Ingestion is out of scope** (Billy). **He is the fetcher; the system's boundary starts at the endpoint.**" It "retired an entire branch the agent had built over two rounds (source registries, coverage guarantees, scraping)."
- **`domain-design.md §1` ruling 5, Billy, 2026-08-21** (S1 thing 61). Same, imported: "It does not need to know how a source arrived."
- **`domain-design.md §4`, qualified the same day** (S1 thing 61). "the system does not need to know how a source arrived, but it does need the source's **publication** time, not the ingestion time. Dumping three notices on Sunday in the wrong order would otherwise let an older fact silently overwrite a newer one."
- **`domain-design.md §10.7` ruling 5, Billy, 2026-08-22** (S1 thing 61; verified by zoom). "Live intake is Billy **pasting a screenshot**, so there is no segmentation problem at all - and **the ingestion endpoint is multimodal from day one**, which both documents currently write as text processing."
- **`model.md §7`, `§8`, `§10`** (S1 thing 61). Ingest is a first-class writer across every layer.
- **`design.md §1` F1, 2026-08-27** (S2 container list). "A pasted portal screenshot, **read by the session itself**… **No API call.**"

**Standing.** Current and Billy-ruled twice. **The word "ingestion" is used in two senses across the whole corpus - *fetching* (out of scope) and *processing at the endpoint* (extensively designed) - and no passage anywhere reconciles them.** S1 flags it; S5 supplies the first-hand statement that establishes which sense Billy ruled on. → **C64**.

**`⟂container`.** "Billy opens Avenue and downloads PDFs; the boundary starts at the endpoint" describes where the app sits relative to a human, and "read by the session itself" describes a session that no longer exists in the same form.

## M82. The operations model (file it / apply it) - dead, and its counter-argument

- **`openclaw:log/2026-08-21` §Key decisions, unattributed** (S5 C3). "Routing at the endpoint between **insert** and **rewrite**; rewrites come only from announcements and from new versions of obligation-bearing documents; only rewrites are confirmed (~30/semester), and **the confirmation presents the *resolved target*, not a yes/no.**"
- **`domain-design.md §4`, 2026-08-21** (S1 thing 62). Same, imported. "Nearly all the pain comes from (2) being handled as (1)." Plus "**retirement … happens at the moment of write.**"
- **`step-minus-1/p5-induction/TASK.md`, 2026-08-22** (S3 §7). The method the falsification used, which is itself a durable thing: "**What would this announcement require the system to do?** Answer in the announcement's own terms first, without reference to the schema. Only then force the answer into the reduction. **Reversing that order fits the data to the schema, which is the failure this whole step exists to avoid.**"
- **`step-minus-1/FINDINGS.md §P5`, 2026-08-22** (S3 §7). "**The operations model is FALSIFIED.** 53 of 137 operations reduce (39%); 76 do not (55%). **Ambiguity was resolved against the proposition, so this is a conservative lower bound.**" Supporting: "**The deadline move happened once in a semester**, in the hardest course"; **21 of 22 executed rewrites were additive free-text appends**; "**~30 confirmations/semester is not a real number**"; **D1 settled: read-time expiry beats write-time supersession ~7:1**; **D2: §4 anticipated one of three failure modes** - the others are *value unavailable* and *applicability unknown*. Residue concentrates: 42 of 76 in three classes.
- **`domain-design.md §4` banner + §10.3 + §10.5, 2026-08-22** (S1 thing 62). Imported: `⚠️ SUPERSEDED`, "**is dead (P5)**", "**superseded almost entirely.**" The confirmation numbers: "~115 across five courses; applied to destructive overwrites only it is 1-2 per course."
- **`PLAN.md` §Open, and owned here, item 4, 2026-08-22, agent** (S5 A9). The counter-argument, quoted because it is the sharpest open objection in either origin file: storing-and-tagging leaves "due Wednesday" and "moved to Friday" coexisting for the LLM to reconcile at read time, which "***relocates Billy's uncertainty into the system while making it look handled***". "The agent's position is that this holds for an unbounded pile and fails for a scoped, time-ordered set. **Answer it or accept the risk explicitly; do not pass over it.**"
- **`domain-design.md §10.8`, 2026-08-22, agent drafts not ruled** (S1 thing 62). Same objection, same status: "**that is an assertion, not a design**, and it is the reason the allocation layer cannot shrink to zero." Named "**the entry point for the next design round**".
- **Spec side: silent.** Nothing in `records/spec/` addresses read-time reconciliation.

**Standing.** **The model is dead on measurement. Its counter-argument has been open, flagged, and named as the entry point for the next round since 2026-08-21, and is unanswered in every record dated through 2026-08-28.** Two independent documents flag it with an explicit instruction not to pass over it. → **C65**, escalation.

## M83. Inbound is to be known, not to trigger an action

- **`domain-design.md §10.4`, Billy, 2026-08-22** (S1 thing 63). "> **Inbound does not arrive to trigger an action. It arrives to be known.** … **This is what dissolves the 55%.** Room changes, section-scoped notices, pointers to Avenue paths, an accumulating strike count - **none of them needed the system to *do* anything. They needed to be *known*.** The operations model forced them into a binary that had no correct branch, and recorded their refusal as failure."
- **`domain-design.md §10.7` ruling 1, Billy, 2026-08-22** (verified by zoom). Restated as a numbered ruling.
- **`domain-design.md §10.5`, the consequence flagged against itself** (S1 thing 63). "§6's own stated failure mode is 'everything lands in free text, so M1/M2 stop working and the KB degrades into a note pile.' **The reframe walks into that deliberately.** The only thing separating a designed KB from a note pile is that the small allocation layer stays populated."

**Standing.** Current, Billy-ruled, and it is the ruling that replaced the dead operations model. **Its own record names the risk it takes**, and the mitigation ("the small allocation layer stays populated") is exactly the layer whose field set has been shrinking (M52, M53) and whose size guard was retired (M53). → **C66**.

## M84. Confirmation policy

- **`domain-design.md §4`, 2026-08-21** (S1 thing 64). "**stratified by operation, not by item:** filing is fully automatic (wrong tag is harmless); rewriting asks, because it is irreversible… Roughly **~30 confirmations per semester**." And: "**The hard part of a rewrite is not the confirmation, it is resolving the target.**"
- **`domain-design.md §10.3`, 2026-08-22** (S1 thing 64). "**§4's ~30 confirmations/semester is not a real number.** Applied to all rewrites it is ~115 across five courses; applied to destructive overwrites only it is 1-2 per course." The earlier figure stands uncorrected in place in the same file.
- **`model.md §8.1`, Billy, 2026-08-23, `[R]`** (S1 thing 44). A separate regime for notes: "**note CRUD asks a short confirmation during development**, and the behaviour is observed, *'像一个 toggle 一样'*." The exit condition is an "**Agent addition, not ruled**", with N = 5 "explicitly flagged as arbitrary. **There is no evidence behind the number.**"
- **`design.md §3.6`, 2026-08-27** (S2 T41d). Mechanised as `Diff`: "**the dev-time confirmation toggle reads a `Diff`**, and so does F2's conflict question."
- **`architecture.md §3` consequence 3, Billy, 2026-08-27, `[R]`** (S2 T36). The governing principle: "**The system must not chase the agent.** *'The system is designed to help me, not to raise questions, conflicts or concerns that no one will ever care about in daily usage.'* **A schema rule that manufactures a conflict a person would not care about is a defect in the rule.**"

**Standing.** The stratification survives; the ~30 figure is superseded in place; the note regime is Billy-ruled with an arbitrary unruled exit; the mechanism is `Diff` and it is deferred. **`architecture.md §3`'s consequence 3 is the successor principle and is the ground two later `schema.md` rulings cite** - so this thing's centre of gravity has moved from a count to a principle. → **C67**.

**`⟂container`.** "During development" is a mode of the old app's own build cycle; "daily usage" is a human's.

## M85. Conflict detection: "you told me this, the record says that"

- **`model.md §8.1`, Billy, 2026-08-23, `[R]`** (S1 thing 2). "**not trusting the user is CONFLICT DETECTION, not verification.**"
- **`domain-design.md §4`, 2026-08-21** (S1 D23). The apparent counter: "**All dangerous inputs are external.** Billy-authored input (notes, code, spoken status) is never a dangerous rewrite - **he is the authority on his own state.**"
- **`step-minus-1/FINDINGS.md §P2` sub-question 2, 2026-08-22** (S3 §4). The probe that tested §4's presupposition: external material and Billy's own separate "cleanly, **by accident**" - his artifacts carry his MacID. "**Not universal** … so it is a good default, **not a rule**." Scoped: "The inbox model makes this moot for live use; it matters for replaying historical material."
- **`design.md §1` F2, 2026-08-27** (S2 T41d). Elevated to an acceptance requirement: "Landing is idempotent and **detects conflicts instead of overwriting**: *'you told me this, the record says that, which holds'*." Its mechanism is `Diff`'s **CONFLICT** outcome, and `architecture.md §7` rules the adjudication **presentation tier**.
- **`schema.md §4.5`, 2026-08-28** (S2 T15). "an agent may **surface** a progress claim for confirmation but **never resolve one**."

**Standing.** **Settled, and S1's D23 dissolves.** The two are not in conflict: §4 says Billy's input is never a *dangerous rewrite* (an authority claim about the source); §8.1 says a claim that disagrees with a held record is *surfaced* (a mechanism about the write). `design.md` F2 makes surfacing an acceptance requirement and `architecture.md §7` puts the adjudication where a human can answer it. Three records, one posture. → **C68**.

## M86. Always keep, judge only linkage

- **`domain-design.md §10.8`, agent drafts not ruled** (S1 thing 66). "The ingest judgment should not be load-bearing, because its failure is asymmetric: **wrongly discarding a correction leaves the corpus quietly wrong, while wrongly attaching one costs a little noise.** So retain every announcement's text against its course and any document it names, and let the agent decide only what to *link* and what to *index*. **A misjudgment then costs retrieval reach, not data.**"
- **`step-minus-1/p6-channel-or-knowledge/TASK.md` §Anti-cheat, 2026-08-22** (S3 §8). The same asymmetry, pre-registered as a bias direction: "**Ambiguity resolves toward `knowledge`.** That is the direction that makes more work and denies the convenient conclusion. Excluding announcements removes an entire pipeline from the build, **so the bias runs against the answer that saves effort.**"
- **`architecture.md §3` consequence 2, Billy, 2026-08-27, `[R]`** (S2 T36). Pulling the other way: "**The agent never auto-adds anything unless it is clear the user wants it.** What gets a row is what the user wants tracked, and **the user triggers it.**"
- **`write-rules.md §4.0`, Billy, 2026-08-28, ruled** (S2 T45). Also pulling the other way, with a measurement: 20 candidate notes became **12**.

**Standing.** **Unruled on the domain side and contradicted in posture by two later Billy rulings.** "Retain everything, judge only linkage" is self-declared an agent draft. `architecture.md §3.2` (08-27) and `write-rules.md §4.0` (08-28) both rule toward *not* retaining by default. The two are reconcilable in principle - retain the *text* against the course, but do not make a *row* or a *note* - but no record performs that reconciliation and the retention half now has no ruled home. → **C69**.

## M87. H3 - can a multimodal pass find a partition the course does not state

- **`derivation/TASK.md §1` H3, 2026-08-22** (S3 §11). "from only what the real system would hold at ingest, can a usable concept partition be induced?"
- **`derivation/FINDINGS.md §1` H3, 2026-08-22** (S3 §11). "**PASS on both courses, and both results are uninformative.**" Both agents said so unprompted. `[A2]`: "*the partition is not induced, it is transcribed, and that is a weaker result than a pass.*" `[B1]`: `[Module N]` on 27 of 30 title slides plus a written two-level taxonomy on one closing slide. Verdict: "**Both courses state their own outline. Neither exercised induction.** … **remains UNTESTED.** Named as the single largest gap this run leaves." `[A1]` adds the sharper reason: "the affordance is **the instructor's uniform deck template**, not the discipline. **A course whose decks lack a plan page loses the free coarse layer entirely.**"
- **`model.md §10` item 6, 2026-08-22** (S1 thing 71). Same, imported: "**H3 was never exercised - the largest gap this cycle leaves.**"
- **`PLAN.md` §Open, but not here, 2026-08-22, agent** (S5 A10). The related probe: "**P7**, whether one multimodal pass produces usable structure from the real material… **The last unrun piece of Step 0.**" And a reversal recorded in place: an earlier draft claimed P7 constrained the entity model; "**That was wrong: whether a correction attaches to a whole document or to one section is a granularity parameter on a relation, not a structural difference.**" Fallback if it fails: "retrieval falls back to whole-document plus course/week metadata, which costs precision and changes nothing here."
- **`architecture.md §4`, Billy, 2026-08-28, ruled** (S2 T38). Blocks the test the same way it blocks H1: do not extract more courses before the presentation tier exists.

**Standing.** **Untested, named the largest gap by its own cycle, with a stated fallback, and now behind the same 08-28 sequencing ruling that blocks H1.** Three surveys, three pieces: S3 has the verdict and why it is uninformative, S5 has P7's status and the fallback, S2 has the block. → **C70**.

## M88. Ingest ordering; cross-document decoding; deadlines hiding in prose

- **`derivation/FINDINGS.md §4.4`, `[A3, B2]` adopted, 2026-08-22** (S3 §17). "**The governing artifact must be ingested before the ones it governs.**" `[A3]`: the course outline is the only artifact carrying grade weights; **without it 9 of 12 graded items have none** and "the allocation planner runs blind". `[B2]` J8: assignment bodies carry a superscript marker attached to exactly the words a concept edge would want; it looked like ~20 authored edges and **reads nothing** - "**Decoding required a different document.**"
- **`derivation/FINDINGS.md §4.5`, `[B2]` J7** (S3 §17). "**Deadlines hide in prose inside governing documents.**" *"It is your duty to form teams by the end of Week 1"* appears in the Guide and nowhere else. "**Governing documents cannot be treated as reference-only.**"
- **`model.md §10` item 8, 2026-08-22** (S1 thing 70). Imported: "**Cross-document decoding is a real requirement, not an optimization.**"
- **`derivation/FINDINGS.md §3` J8, `[A3]`** (S3 §14). The other half: "**Every one of the nine 2c03 handouts says, verbatim, 'See Avenue for the due date.'** Ingesting all nine assignment PDFs with a full multimodal pass yields an obligation layer with **zero deadlines**. The portal screenshot is not an enrichment path for ring 0; it is **the primary one**." `model.md §10` item 7 (S1 thing 69) imports it: "Design §10.7's screenshot ruling is **upgraded from convenience to dependency**."
- **Spec side: silent** (ingest is not in slice 1).

**Standing.** Current, evidenced by two agents in two courses, and **deferred entirely** - no spec record touches ingest ordering. **`⟂container`** for the screenshot half: a human-in-the-app paste act.

## M89. Stale material circulates as current; the redundancy defence is dead

- **`derivation/FINDINGS.md §4.6`, `[A2, A3]` adopted, 2026-08-22** (S3 §18). "**Stale material circulates as current.**" 2c03's Week 7 Sample Solutions answer a **different question set** than the Week 7 handout - "the file answers a prior year's handout". The Week 8 tutorial and all eight UML PDFs are dated **2025**. Three uncorrected errors survive inside *current* 2c03 handouts, fixed by no announcement. "**'The corrected version is on the course site' fails for the third time.**"
- **`step-minus-1/FINDINGS.md §P6`, 2026-08-22** (S3 §8, §18). "**The redundancy defence is dead, verified on disk in both courses**": `Tutorial_RiscFreeIDE.pdf` is still the pre-correction version locally; `lab01.pdf` names the superseded Quartus version; the locally held Week 7 deck is **the blank-whiteboard variant in which the corrected complexity table does not exist at all**. And: an announcement in 2c03 reproduces a stale copy-paste three weeks later, "**which indexed announcement text would return as current**."
- **`domain-design.md §10.6`** (S1 thing 21). Imported: "**The bulk is redundant; the seam is not.** Full-or-partial redundancy runs 40-51% overall, but only 1 of 7 and 2 of 7 among the knowledge instances."
- **`schema.md §4`, 2026-08-27/28** (S2 T19). The mechanism it lands in: sticky-note timestamps "**plus the maintenance-at-read rule is what makes a time-bound statement safe to store at all**". **"In slice 1 that comparison has no input**, because the revision date belongs to a kind that does not exist yet."

**Standing.** **The finding is current and load-bearing; its mechanism has no input in slice 1.** The whole staleness apparatus depends on `artifact.revised_at`, which belongs to a slice-2 kind. S3 has the evidence; S2 has the mechanism and the gap; neither states that the corpus's best-evidenced hazard is unmitigated in the only slice being built. → **C71**.

## M90. The correction seam - and whether it is detectable at intake

- **`step-minus-1/FINDINGS.md §P6`, 2026-08-22** (S3 §8). "Both courses' knowledge converged on one thing: **it is almost always a correction against material the system already holds**, which is why extraction cannot hold it. **An amendment to a document is not a fact.**"
- **`domain-design.md §10.9`, still open** (S1 thing 87). "Whether the correction seam is **detectable at intake**. The twelve instances share a signature - they name a document - **but twelve is too few to build on**."
- **`derivation/agents/2c03-concepts-weeks-1-6.md`, `[A1]`, 2026-08-22** (S3 §19). **A third origin nobody detects.** The two real contradictions in A1's slice arrived **with the original material**: "Nothing was delivered; the conflict is inert until someone reads both documents in the same sitting … This is a **third origin for a sticky note** beyond 'a correction arrives' and 'Billy states one' - *the corpus disagrees with itself* - and it is the one that most directly serves design §10.7 ruling 4 … **It is also the one nothing in MODEL detects.** I am not proposing a mechanism; I am recording that the class exists and is populated." **`FINDINGS.md` records the count ("2 latent") but not the class. S3 reads it as dropped.**
- **`derivation/agents/2aa4-tutorials-and-artifacts.md`, `[B2]`** (S3 §19). A fourth: two of its five sticky notes are "**corrections the *author shipped inside the artifact***" (the JUnit 4/5 caveat; the conform-not-correspond footnote). "**The sticky note is not only an inbound-correction mechanism.**"
- **`write-rules.md §4.0`, Billy, 2026-08-28** (S2 T45). Cuts against the intake framing from the other end: "**every erratum about a handout revision**" fails the render test.

**Standing.** **Open, and two of the four origins have no home.** The intake-detection question is explicitly open (08-22) and untouched since. A1's *latent* class - the corpus disagreeing with itself - is the origin that most directly serves ruling 4's third job (locating what Billy does not know to ask about), was recorded by its own author as undetected by any mechanism, was dropped from the derivation's synthesis, and appears in no fall26 record. → **C72**, escalation.

## M91. RAG source classes, and what is excluded

- **`domain-design.md §1` ruling 9, Billy, 2026-08-21** (S1 thing 65). "**RAG is accepted for corpus** - one-time embedding at material drop, per-course buckets, metadata filtering. Math-equation chunking is a known industry problem and is deferred."
- **`domain-design.md §10.7` ruling 3, Billy, 2026-08-22** (verified by zoom). "**RAG stores `slides / pdf / textbook`-class sources.** Handwritten tutorial notes are excluded - not embedded, effectively treated as absent. (Agent note on the criterion: they fail on **density and redundancy, not on volatility**. **The source-class rule is the operative one.**)"
- **`domain-design.md §10.9`, open** (S1 thing 65). "The corpus pipeline's own design (the pass granularity, what gets embedded, whether page images are kept)."
- **`model.md §9`** (S1 thing 39, and S1's own flag). The tension: file-type-based routing was "falsified four ways in one slice" and "the real axis is whether meaning survives linearization - **a property of the materialization pass, not of the file**". **A source-*class* rule is a file-level rule of exactly the kind that retraction is about. Neither passage cites the other.**
- **`step-minus-1/FINDINGS.md §P6`** (S3 §3). And the measurement that makes the exclusion expensive: handwritten scans are "**a whole class in a core course rather than the edge case P2 reported it as**".
- **`design.md §5` / `§7` item 4, 2026-08-27** (S2 T33). The whole store is slice 3 and its pipeline is "**Not decided, on purpose.**"

**Standing.** **A Billy ruling (08-22) sitting on an axis the same week's evidence retracted, over a class the same week's evidence found larger than reported, all deferred to a slice that does not exist.** Recency does not settle it: the ruling and the retraction are the same day, in the same corpus, and neither cites the other. → **C28**, escalation candidate.

## M92. The portal's folder tree is not the skeleton's shape

- **`derivation/TASK.md §2` anti-cheat rule 3, Billy, 2026-08-22** (S3 origin item 7). "**Folder structure is not taxonomy.** Billy's folders are admissible **only** as evidence of the organization *he reaches for under pressure*, and must be tagged as such - **never cited as the course's structure.** (Billy, 2026-08-22.)"
- **`derivation/TASK.md §3`, agent, arguing back** (S3 C9). The same document then makes Billy's folder renames and his hand-written study guide the **sealed ground truth**: "**correct, and irrelevant, because the target is not the course's taxonomy.** `resources/week-01..03` carry no topic suffix and `week-04-stack-queue-list` onward do: that is a timestamped record of *when naming a concept became necessary*." S3: "**This is an agent overriding a human warning by reframing what is being measured** … the override is not marked as one, and the same document's rule 3 forbids exactly this use."
- **`model.md §9`, Billy, 2026-08-22, `[R]`** (S1 thing 67). "the portal shows how files are *distributed*, which is not how knowledge should be *organized*; **finding the better organization is why the system exists.**" And: "an intake screenshot carries **provenance**, not **position**. Parent resolution is semantic, not a path match."
- **`model.md §3` `CORRECTED` banner** (S1 thing 18). The same error committed inside the model: "The original row was written from folder appearances (`tutorials/` holds 11 files), **which is exactly the *folders-are-not-taxonomy* error this cycle exists to avoid.**"

**Standing.** **The ruling is current, Billy's, and was violated by the same session that recorded it - twice, in two different ways.** Once as a deliberate reframe (S3 C9, unmarked as an override), once as a straight error inside `MODEL §3` (caught and corrected). S1 has the corrected error; S3 has the unmarked override. → **C73**.

## M93. The skeleton is not authored by Billy at course setup

- **`model.md §9`** (S1 thing 68). "**Skeleton authored by Billy once at course setup** (an agent draft justified by `domain-design.md §9.6`'s slow+self-authored test). **Retracted** - at setup Billy does not yet know the concept structure; **he knows it at the end. It failed on the same survivorship bias.**"
- **`derivation/FINDINGS.md §5`, `[A2]` adopted, 2026-08-22** (S3 §11). The evidence that both refutes and complicates it: "**[NEW] Billy authors them by hand, unprompted, mid-semester.**" The TUT7 ink edge ("This question tests: ① MAD compression ② linear probing insertion ③ probe counting", in a form with **no text layer**) and the mid-semester folder renames are the same behaviour in two modalities.
- **`derivation/FINDINGS.md §5`, `[A2]`** (S3 §11). And the scale correction: "One clause in a tutorial handout creates **9** `requires` edges; one slide in a review deck creates **26**. §10.2 assumed cross-layer edges are drawn item by item; **they are not.** Corollary: **an edge is only as current as its sentence, and that sentence's document is dated 2025.**"

**Standing.** The retraction is current. **But S3 holds a fourth origin for concept edges - Billy authoring them by hand, mid-semester, unprompted, sometimes in ink on a page with no text layer - that the retraction does not address and no record designs for.** "Not at setup" is not the same as "not by Billy". → **C74**.

## M94. Concept split / merge / rename

- **`model.md §10` item 3, 2026-08-22, owed** (S1 thing 73). "The concept layer is built incrementally and must be refinable. **This is *not* the falsified operations model returning:** that was **inbound rewriting a fact** (external, destructive, irreversible); this is **understanding refining a model** (Billy's own, lossless, reversible). **Different object, different author, different failure cost.**"

**Standing.** Owed. Uncontested. The distinction it draws is the corpus's cleanest statement of why one falsification does not generalise, and it is the operation M93's fourth origin would need.

## M95. The capture point - `/wrap`, and the third class

- **`openclaw:log/2026-08-21` §The capture-point finding, agent** (S5 item 23, C7). "**It was never a problem with the ritual. It was a problem with the material.**" `/wrap` "fits **slow + self-authored** material… fall26's *facts* are externally-originated and time-critical, satisfying neither, so they need at-the-moment capture." Self-limited in place: the yield/value inversion that motivated the doubt is "**Not fixed by this finding, and still live**".
- **`domain-design.md §1` ruling 2, Billy, 2026-08-21** (S1 thing 74). "**The capture-point doubt is the same problem**, not an adjacent one - do not settle the ritual and the domain separately."
- **`domain-design.md §9.6`, `COMPLETED - Billy 2026-08-23`, `[R]`, verbatim** (S1 thing 74). "假如需要判断的时候再问...让系统从 waiting for input 变为 asking for input...前者要求你 proactively provide input，但我自己都忘记了怎么可能 provide。" A **third class**: facts with no generating event - origin Billy himself, capture point "**at the READ - the system ASKS**". "The third class is **self-authored but not durable**: progress, difficulty, how much load a week already carries. A deadline is generated when the professor posts it; **a progress state is generated by nothing**, so there is no moment at which it could be volunteered and **forgetting to supply it is structural rather than a lapse**."
- **The governor, same block.** "**only ask what changes a decision.** Left ungoverned this degenerates into an interrogation - one blind run alone produced about nine askable items… **The gate that decides what belongs in the observation space and the gate that decides what is worth asking are the same gate.**"
- **`architecture.md §3` consequence 3, Billy, 2026-08-27, `[R]`** (S2 T36). Pulls hard the other way: "**The system must not chase the agent.**" And `schema.md §4.5` (08-28) uses it explicitly to *remove* an occasion to ask: "a nullable state makes the system announce it does not know, which **gives an agent a reason to ask *have you started this yet*** - the system chasing the agent."

**Standing.** **Both are Billy's, four days apart, and they point opposite ways on the same act.** 08-23: the system moves from waiting for input to *asking for input*, because a progress state is generated by nothing and forgetting is structural. 08-28: a nullable `progress.state` is removed **precisely so the agent has no reason to ask about progress**. The governor ("only ask what changes a decision") is the intended reconciliation, and neither record invokes it against the other. This is the sharpest recency-does-not-settle-it case in the corpus. → **C75**, escalation.

## M96. An asked answer persists

- **`domain-design.md §9.6`, Billy, 2026-08-23, `[R]`** (S1 thing 75). "**an asked answer PERSISTS.** It is stored with its timestamp and `source: asked` **stated prominently, so that an agent cannot read a historical answer as a current fact.** The harm was never storage; it was **silent** influence (*'结果后续的决策一直被他影响'*). Same shape as the three-axis `status` finding: `done` was harmful because it was read as terminal, not because it was recorded."
- **`schema.md §4` / §4.5, 2026-08-28** (S2 T17). Landed as a field: `origin` values are "an announcement, someone saying so (`stated`), or the system having **asked** (`asked`)", shared across both annotation kinds. "**An asked answer persists stated prominently, so that an agent cannot read a historical answer as a current fact**" - the domain sentence, imported verbatim into the schema record.
- **`write-rules.md §4`, 2026-08-28** (S2 T17). `origin`: **OWED** - "the schema's prose says *how the claim was obtained*; **both passes reached for *what document class it came from*.**" A named divergence between definition and practice.

**Standing.** **Settled and implemented - a clean cross-corpus carry-through**, and S1's open question ("whether `source: asked` is that `origin`") is answered: it is. The write rule is owed with its failure mode already measured. → **C76**.

---

# Cluster F - The container: tiers, surface, language, sessions, external systems

Everything in this cluster is `⟂container` by construction - these are the things whose *whole content* is a fact about the container. They are listed because several of them carry rulings that other clusters depend on, and because the successor container is the one thing this corpus was never asked about.

## M97. The three-tier split

- **`architecture.md` conditions + §1 + §3, Billy, 2026-08-27, `[R]`** (S2 T35). "**none. This record governs every other record in `records/spec/`**, and it re-scopes `design.md`, whose bounded question was written before the split existed." **presentation** = the CLI, the bundled skill, rendering including every one-line summary, and **every rule about what an agent should do**. **application** = the field set, kinds and links, construction-time validation, CRUD services at field grain per kind, id minting. **persistence** = the serialized files and the adjacency index, fetch-by-key and one-hop traversal.
- **Per-record assignment** (`architecture.md §2`): `schema.md` → application; `design.md` → application and persistence, "its passages on docstrings and the MCP adapter are presentation"; **`../domain/` → "none - it is the material both tiers are derived from, and it predates the split"**; the CLI, tool descriptions, the skill → presentation, "**none of these exists yet.**"
- **The sequencing rule it carries** (`architecture.md §1`): "**A tier is designed against the tier below it, and that tier must already exist.** Designing the presentation surface before the application tier is built **is how this project spent three cycles specifying descriptions for methods that do not exist.**"

**Standing.** Newest structural ruling in the corpus, Billy `[R]`, never amended (§4, §5 and §6 were amended; §1 and §3 were not). **It explicitly places the entire domain corpus outside the scheme** as pre-split material - which is the corpus's own statement that S1's material is not superseded by S2's, it is upstream of it. Load-bearing for how everything above should be read. → **C77**.

## M98. The four §3 consequences

All four `[R]` Billy, 2026-08-27, none amended (S2 T36). They are the grounds cited by the *later* rulings in `schema.md`, which is the shape of load-bearing material rather than superseded material.

1. **"A write rule never refers to the source."** "The field set says what a legal value is; **how to produce one lives in the tool description or the bundled skill.**" → **contradicted by the rules written under it** - see **C78**.
2. **"The agent never auto-adds anything unless it is clear the user wants it."** "What gets a row is what the user wants tracked, **and the user triggers it.** This is a presentation-tier behavioural rule; the application tier holds no rule about what deserves to exist."
3. **"The system must not chase the agent."** Billy in the first person: "*'The system is designed to help me, not to raise questions, conflicts or concerns that no one will ever care about in daily usage. The schema-level rules shouldn't be a burden that keeps chasing the agent.'*" **Cited as grounds by `schema.md §4.5` (M51) and §3 (M48).**
4. **"The agent works by listing, then acting on what it saw."** "**identifiers need not be human-facing**, and **matching two records is an interaction at the presentation tier, not an algorithm in the application tier.**" **Cited as grounds by `schema.md §1.1` (M40).**

**Standing.** Current and heavily load-bearing. **`⟂container` on all four, and consequence 3 most of all** - it is quoted from Billy about *daily usage* by a person, and it is the ground two schema rulings rest on, so its container-sensitivity propagates into the field set. → **C79**.

## M99. The migration list - what the tier split moved

- **`architecture.md §4`, opening line, 2026-08-27** (S2 T37). "**Recorded because a plan that predates the split still reads as authority.**" Moved to presentation: `land()`'s docstring and the read operations' descriptions ("The 2026-08-26 ruling that write rules precede the build **still holds and its target changed**: they precede the *presentation* tier"); the **MCP adapter** ("at most an adapter over the CLI's grammar, **and may never be built**"); the **verb-routing evaluation**; the **screenshot-extraction evaluation**.

**Standing.** Current. **This is the single most container-loaded ruling in the corpus for the successor question**: it demotes an agent protocol adapter below a human CLI and may never build it. In a Claude Code plugin the adapter is the product. → **C80**, escalation.

## M100. The surface is a CLI, and the grammar beats N verbs

- **`architecture.md §5`, Billy, 2026-08-27, ruled** (S2 T41). "The presentation tier is a **CLI**. An adapter for an agent protocol is at most a thin shell over the same grammar, and may never be built."
- **"What is rejected is a shape, not a protocol:** N single-purpose verbs, each deciding when it is called from its own description. This project has measured how fragile that is - **rewording one docstring moved a verb's call count from 1 to 9 with data availability held constant**" (`design.md §3.6`).
- **What replaces it:** "**one composable grammar with progressive disclosure** - each level renders what is around it, and going one level deeper is one more call. Listing returns ring 0's summary; drilling into a course is a further call; drilling into a single node is the walk."
- **"The distinction is independent of transport, which is why transport is a late and cheap decision.** **A server exposing exactly ONE tool whose argument is a command string has the same property**; a CLI with forty subcommands, each needing `--help` to know when it applies, has the old defect. **The grammar is the early and expensive decision.**"

**Standing.** Current, Billy-ruled. **And it contains its own bridge across the container change**, in the transport-independence clause: the ruling that matters is about the *shape* (one grammar, not N described verbs), and it explicitly says a single-tool MCP server has the same property. The 1-to-9 docstring measurement is the load-bearing evidence for two separate rulings and it is a measurement of *an LLM routing over tool descriptions* - i.e. it is evidence about the successor container, obtained in the old one. → **C81**.

## M101. Addressing at the surface

- **`architecture.md §5`, Billy, 2026-08-28, ruled** (S2 T41b). "**Addressing is the presentation tier's, not the schema's.** … the surface may render a record however it likes and **resolve at call time, the way a materialized view does.** The `id` is opaque precisely so that nothing at the surface has to mean anything to the layers below. **One constraint binds it:** nothing constructs an id, so **every read that returns records must return their handles** - a handle absent from the render makes the level below unreachable."
- **The rule for the double duty:** "**The render is simultaneously the message and the input to the next call**… **human-readable by default, a machine branch for machine consumption, and any locator the next call needs must appear in the human render too - never only in the machine branch.**"

**Standing.** Current, newest, and the second half is the corpus's sharpest single container assumption: it presupposes a human reading the primary render and a machine reading a branch. **In the successor container the primary reader is the agent, which inverts which branch is the default.** → **C82**.

## M102. The acceptance criterion - 22 obligations across two courses, then one course

- **`design.md §1` F5, imported 2026-08-25, body rewritten 2026-08-27, unattributed** (S2 T38). "Ring 0 holds all **22** real obligations with **no free-text escape hatch**."
- **`architecture.md §4`, Billy, 2026-08-28, ruled** (S2 T38). Amended: "the field set holds **one course's real obligations**, landed and read back through the operations rather than hand-written. **'Landed' means written through the write operations**, not through `land()` specifically." And: "**The 22 came from a transcription that has since been superseded**: a fresh extraction from source found **14** for 2c03, and the old count included **a row the graveyard forbids** (recurring tutorial attendance), so **22 is not reachable by re-running the old route.**"
- **`schema.md` still counts in 22s throughout §3, §6, §7** (S2 D2), and its own 08-27 changelog had already called that fixture "**rejected as a golden set**" the day before `architecture.md` amended the criterion. **Neither correction propagated.**

**Standing.** **Amended by ruling; the superseded number is still what a reader hits first in two records.** Every count in the graveyard (M62) is stated over it. → **C83**.

## M103. The skeleton does not need a database

- **`design.md §5` conclusion 1, 2026-08-27** (S2 T31). "**The skeleton does not need a database.** It needs a durable serialization plus an adjacency index rebuilt at load. All three operations are scans over that index, and **the load is cheap enough that per-invocation and resident are indistinguishable.**" Facts: ~640-1,600 nodes · ~2,200-3,700 links at five courses, from a base of 256/224 enumerated over two courses, "**Enumeration is 15-25% of observed links… The conclusions survive a 2-3× error, which is why the range is quoted.**" Measured cold-load: 2c03's 138-node/137-link graph is 52 KB and parses in **0.27 ms**.
- **A prior heuristic explicitly refused** (S2 T31). A general "*few writers means no database*" heuristic "does not decide this either: its stated justification is that a database's concurrency machinery buys nothing, which is a **concurrency** argument… **so a conclusion may coincide while the heuristic still does not apply.**"
- **A market fact, held at arm's length:** "The obvious embedded-graph-database answer is gone: **Kùzu is archived and its team acqui-hired** … **which is a reason to be glad conclusion 1 holds, not the reason it holds.**"
- **"What would overturn this:** the corpus growing an order of magnitude · multi-device sync becoming real (a MacBook plus the deferred Mac Mini) · the skeleton growing far past ~640 nodes." · "**Not decided, on purpose:** the actual serialization format and the store's engine."
- **`domain-design.md §10.1` P1** (S1 thing 10) and **`step-minus-1/FINDINGS.md §P1`** (S3 §1) record the opposite infrastructure: pgvector 0.8.0 on PostgreSQL 17.6, HNSW built, PASS.

**Standing.** **Current for the skeleton and it survives the container change better than almost anything else in the corpus** - its argument is explicitly per-invocation, its measurement is 0.27 ms, and its overturning conditions are named. The Postgres/pgvector result belongs to the store (slice 3) and to a database the plugin container does not have. → **C84**.

## M104. The language - TypeScript

- **`architecture.md §6`, Billy, 2026-08-27, ruled** (S2 T39). "**TypeScript**, and the tiers are directories under one source root." The argument: "**The language is settled by what this design already claims about itself.** `design.md §3.5` says trigger D is *'defused by type, not by restraint'*, and `schema.md §8` says construction is the only enforcement point there is. **Both are claims about a compiler that can refuse.** Python cannot refuse: any module may import any other, so the purity cut degrades into discipline; and **adding a kind in slice 2 raises no error at the sites that must change**, so trigger B's promise is hoped for rather than checked."
- Costs stated: runtime type erasure "**is a wash and is not a reason to prefer either**"; "**The embedding ecosystem is Python's**… the store may be Python without crossing a tier boundary. `fall26/ingest.py` stays Python as an offline pass and **is in no tier**"; "Rust fits the data shapes best… Neither is chosen, **on iteration speed for a solo build.**"
- Changelog: "**the agent had recommended Python and reversed**, because the two mechanisms this design claims for itself both presuppose a compiler that can refuse."
- **`design.md §1`'s constraint line still reads "directly-callable Python, no MCP, no Postgres, no `PA_SOURCE`"** and was not edited (S2 D3). `design.md §3.7` is compatible ("not committed to Python"); §1's line is not, and is what a reader hits first.

**Standing.** Ruled TypeScript 08-27, on an argument that derives from two earlier design claims rather than from taste. **The Python constraint line is stale in the record a reader opens first.** → **C85**.

## M105. Packaging - packages, then directories

**The corpus's fastest reversal: ruled and reversed within 24 hours** (S2 T40).

- **2026-08-27, Billy, ruled.** "the tiers are **separate packages in one workspace**… **a package boundary is enforcement, a lint rule is a convention.**"
- **2026-08-28, Billy, ruled.** "**§6 reversed:** the tiers are **directories under one source root**, not separate packages. The original ruling's ground was that a manifest cannot be waived; **under npm that is false, because workspace dependencies hoist and a manifest cannot refuse an import it does not declare.** The enforcement is `app/tests/boundary.test.ts`, which resolves every relative import and **has been shown to fail.**" Its limits are stated in place: "it sees relative specifiers only, and it scans `src/`, not `tests/`. Both are fine while there is one package and no path aliases, and **both stop being fine the moment either changes.**"

**Standing.** Current (08-28). A model instance of the corpus's best behaviour: reversed on a checkable fact, with the replacement's limits stated rather than discovered.

## M106. Serialization - JSONL, `schema_version`, and where validation happens

- **`schema.md §8`, 2026-08-27/28** (S2 T32). "Each file carries a **`schema_version`**: JSONL enforces nothing and construction is the only gate, so without a version a stale file fails as a validation error with no explanation. `nodes.jsonl` + `links.jsonl`; vectors, if they ever arrive, go to a **side binary store keyed by node id**, never into the JSONL." Two-phase cold start: parse and construct by kind; parse and build the adjacency index.
- **"Construction is the only place a record's own shape is checked."** And two things it is not: "A rule that ranges over more than one record cannot run there - **a constructor sees one line** - so the id space, one-current-value-per-target and link identity belong to the **services**." And: "**construction is not currently part of the load** … **A malformed line therefore loads without complaint and is rewritten intact by the next flush.** Closing that needs a load-time pass owned by the application tier… **parked at `../plan/backlog.md`.**"
- **Changelog 2026-08-28, agent, measured** (S2 T32). "§8 no longer claims that validation happens at load… **Measured, not inferred: a store carrying `due: 'April 2026'` and a slice-2 `concept` node loaded without error and was rewritten intact.**"
- **Residual** (S2 T32): the code block in §8 still carries the inline comment `-- validation happens HERE` directly above prose saying construction is not part of the load.

**Standing.** Current, corrected by measurement, with the remaining hole parked with an owner. The one thing worth carrying forward regardless of container: **a malformed record survives a round trip silently**, and nothing closes it in slice 1.

## M107. Session topology; no fold; course ≠ domain; the store is the channel

- **`domain-design.md §5`, 2026-08-21** (S1 things 47-49). Three scopes: semester (all courses, shallow, "**a real working session** - cross-course planning is reasoning, not a view"); course (persistent, "**state is what persists, not a session**"); task (deep, "this is where sessions live; scope loaded at entry"). "**'Just-enough depth' has a precise definition: enough to triage, not enough to work.**" · "**No fold.** Fairy needs one because domains emit prose-grained events at volume; fall26's facts layer is small and structured, so the coordination layer reads all of it every time." · "**Structurally isomorphic to Fairy↔domains - steal the shape, not the mechanism.**" · "The domain contract (registry entry, episodes, /wrap, /standup, ack protocol) is repo-level ceremony; six courses times that is exactly the cloned-build-repo-furniture mistake ruled out. **fall26 is ONE domain.**" · `§9.4`: "**the store is the channel.**"
- **`PLAN.md` §Settled, 2026-08-22** (S5 A8). "§5 - **no fold; course ≠ domain; coupling through the store, never a call**" - listed settled and closed to re-litigation.

**Standing.** Current by date and by `PLAN.md`'s settled list. **`⟂container` end to end** - every term (registry, episodes, /wrap, /standup, ack, fold, domain) is the old container's vocabulary, and the sibling system it steals from is Fairy, which the successor repo explicitly does not inherit from. **One residue S1 flags:** "reads all of it every time" is the same premise `domain-design.md §3`'s banner calls false as written, and §5 ties itself to §3 explicitly; the banner does not propagate to §5. → **C86**.

## M108. Calendar goes to Notion; is Notion authority or projection

- **`domain-design.md §1` ruling 8, Billy, 2026-08-21** (S1 thing 77). "**Calendar goes to Notion.** That removes the only human-facing rendering requirement from this repo."
- **`domain-design.md §7`, open, 2026-08-21** (S1 thing 77). "**Notion: authority or projection?** Tilt: projection… **One authority (facts layer), many views.**" Under `## 7. Open - not yet ruled`.
- **`openclaw:log/2026-08-21` §Open threads** (S5 item 21). "**Three rulings before W1:** Notion projection vs authority · own tables vs reusing PA's `todos` · where `workload` estimates come from. **Billy deferred all three** to when the build reaches them."
- **`PLAN.md` §Settled, 2026-08-22, agent, no attribution** (S5 C10, X5). One day later, under a heading forbidding re-litigation: "**The three build-spec §7 decisions, ruled 08-22** - Notion is a projection; fall26 gets its own Postgres schema and its own MCP; `workload` is stated by Billy, nullable, never defaulted." S5: "**the deferral condition Billy set was not the condition under which they were ruled**" - the build had not reached them.
- **The contradiction §1.8 walked into** (S1 D21). "removes the **only** human-facing rendering requirement" is contradicted by later rendering work in the same corpus: `model.md §2` defers "which spine a view renders" as a CLI/UX decision; `§7.2` rules a sticky note renders with the summary; `§10.5` measures what rendering the course level costs in characters; and `architecture.md §5` (08-27) makes rendering the presentation tier's whole content.

**Standing.** **Rendering is back in scope and §1.8's premise is false.** The Notion authority/projection question was deferred by Billy (08-21) and recorded as ruled by an unattributed agent document (08-22) - which under merge rule 4 is weighed on content and date, and on content it decides a question Billy had just deferred, under a do-not-re-litigate heading. Two of the three decisions in that same bullet are since superseded (`workload` retired 08-23; "its own Postgres schema and its own MCP" superseded by `design.md §5` and `architecture.md §4/§5`). → **C87**, **C88**.

## M109. Relationship to the existing PA db

- **`domain-design.md §7`, 2026-08-21, open** (S1 thing 78). "Tilt: keep separate. **An obligation is not a todo** (todos are flat, cross-domain, carry no workload/course/source and no externally-driven status transitions); overloading them would pollute PA's cross-domain work-trace. fall26 gets its own tables in the same database, and an obligation entering 'this week' *projects* a PA todo - **fall26 authoritative, PA a view.**"
- **`PLAN.md` §Settled, 2026-08-22** records it as ruled (see M108). **`design.md §1`** lists "no `PA_SOURCE`" among its constraints (S2 T39 container list).

**Standing.** Open on 08-21, recorded ruled 08-22 by an unattributed agent document, and the constraint line in the newest design record says `PA_SOURCE` is out. **`⟂container`** - PA is a system in the old container.

## M110. Repo rituals - `/wrap`, `/promote`, manual markdown, `memory/calibration.md`

- **`domain-design.md §1` ruling 3, Billy, 2026-08-21** (S1 thing 79). "**Manual markdown maintenance is out.** The information granularity is too fine and too time-sensitive for the `devlog/`-style discipline."
- **`domain-design.md §6`, 2026-08-21** (S1 thing 31). "**Schema evolution uses the existing `/promote` gate** (recurrence + boundary + coverage), with the object changed from basis dimensions to schema fields… **Only typed fields make migrations, so deferring a decision is free.**"
- **`model.md §10.9`, 2026-08-23** invokes it as the escape valve for the rejected general form of conditional weighting: "`/promote` promotes it if it recurs."
- **`domain-design.md §9.6`, `/wrap`** - see M95.
- **`domain-design.md §8`, `memory/calibration.md`** (S1 thing 76). "a preference store with a write discipline (propose-then-confirm); **at fall26's volume that discipline is too heavy.**"

**Standing.** **`⟂container` completely, and this cluster is where the successor container has the strongest claim to change the answer.** `/promote` is the escape valve two rulings lean on, and it is a slash command in a repo that no longer exists. A plugin has skills and commands; whether one of them is `/promote` is a live design question, not an inheritance. → **C89**.

## M111. Preferences are a fact type, not a layer

- **`domain-design.md §8`, 2026-08-21, "Raised by Billy; analysis below is draft, not ruled"** (S1 thing 76). "**Preferences are not a new layer - they are a fact type.** … Structurally it is **identical to `progress`**: small, self-authored, unenumerable, mostly free text… because it is nearly all free text it carries no rewrite danger and needs no confirmation." On mem0: "the capability worth taking is *passive extraction from conversation*… The part to reject is the *separate store* - a second source of truth about Billy sitting beside the facts layer reproduces the 'deadline Wednesday / moved to Friday' pathology one level up. **Take the mechanism, not the product.**"
- **`domain-design.md §6` table** already types a `preference` row; **`§9.3`** already assigns it a close-of-session extractor; **`§7`** still lists it as open pointing at §8 (S1's mild internal inconsistency).
- **Spec side: silent.** `preference` is not a kind in slice 1 or slice 2 (`design.md §3.1`), and appears nowhere in `records/spec/`.

**Standing.** **Self-declared draft, honoured as unruled, and now doubly unmoored.** The analogy it rests on - "structurally identical to `progress`" - broke when `progress` moved out of the fact-type table into an annotation kind (M51), and no record asks whether preferences follow. And the kind does not exist in either spec slice. → **C90**.

## M112. Method and apparatus - pre-registration, anti-cheat, the seal

**S3 calls this "arguably the most durable output" of the origin sessions, and on the evidence it is right.**

- **`step-minus-1/TASK.md` §Anti-cheat rules and `fall26/README.md`, 2026-08-22** (S3 §20). Sampling rules written **before** any file content is opened; **ambiguous judgments resolve AGAINST the proposition**; verdict thresholds stated before the run and not adjusted afterwards; raw artifacts stay because "**a conclusion whose evidence was deleted is not auditable**."
- **`derivation/TASK.md` §preamble** (S3 §20). Why pre-registration matters more here: "Step -1 was judged by data, this one is **judged by Billy and the agent alone**… **H1 and H4 stay judgment calls** - that is stated up front rather than discovered afterwards."
- **`PLAN.md` §This cycle's own failure mode, 2026-08-22** (S5 A7). The same admission from the other side: "**this cycle has no external adjudicator**… so **everything it produces is an assertion until W1/W2 test it.**"
- **`BRIEF.md` rule 1** (S3 §20). "**No design vocabulary in the raw pass.** … Having the word 'concept node' available is enough to start hallucinating them."
- **The seal, and its failure** (S3 §20). "**The seal leaked. The mechanism was mine and it was the wrong mechanism.**" Built from symlinks; `ls -la` prints symlink targets, "so **the first command a shell-using agent naturally runs defeats it**." Two agents hit it; both self-reported. `[B2]` "saw the 2aa4 ground truth verbatim"; its induced concept **partition** is contaminated, its structural findings stand. `[B1]` established the leak could not have mattered for 2aa4: the grouping has three carriers and only one was sealed - **"Carrier 3 is content… so this grouping was never withholdable. No re-run was ordered."** The correction: "**copies, never symlinks, and strip document metadata.**"
- **A preservation rule** (S3 §20). "**Preserve what cannot be reconstructed, record the recipe for what can.**"
- **`write-rules.md`'s 2026-08-28 method statement** (S2 T42) - the same discipline, six days later and in the other repo: "Writing them in the abstract **stalled for two months**… **These came from Billy editing one course's extracted records by hand: the rule is what he did, and the before-and-after is the evidence.**"

**Standing.** Current, and it is the one thing in the corpus that is neither domain nor container - it is method. **It is also the corpus's only recorded procedural fix for a two-month stall.** → **C91**.

## M113. Sequencing - fall26 first, the template afterwards

- **`domain-design.md §1` ruling 1 and §0.1, Billy, 2026-08-21** (S1 thing 82). "**Sequencing inverted.** fall26 first; do not generalize from the three build-repo instances and clone outward." And: "this design IS the B-layer work - **the template is whatever survives generalization afterwards**, not something to be derived up front. The standing telos behind it: **every aspect of Billy's life managed under one contract.**"
- **`architecture.md §4`, Billy, 2026-08-28, ruled** (S2 T38). The same posture applied within fall26: do not extract more courses before the presentation tier exists.

**Standing.** Current, and applied twice at two scales. **`⟂container`** - B-layer, dispatch and build-repo instances are old-container structure - but **the posture itself is the one the successor repo's own framing already adopts**, and the telos behind it is the reason `course.offering_term` mattered (M64).

## M114. Scale is out of scope

- **`design.md` header, 2026-08-27** (S2 T47). "**Scale is out of scope, stated once:** one user, one machine, one session at a time, so load estimation, horizontal scaling, failover and redundancy are **discarded whole.** The only sizing number that matters is that ring 0 for five courses is roughly **55 obligations**, and the only availability concern is a scratchpad holding the sole copy of an apparatus."

**Standing.** Current. **`⟂container`** - "one session at a time" is precisely the assumption the successor container puts in question, and it is stated as a discard rather than as a ruling with a falsifier.

---

# Part II - The conflict register

Every conflict, both sides with dates and provenance, and one verdict of three:

- **settled by recency** - the later side wins and nothing about the later side looks wrong.
- **settled by an explicit ruling** - a named ruling decides it, cited.
- **needs Billy** - recency does not settle it, or the newer ruling looks wrong, or both sides are Billy's.

**`✚` marks a cross-survey conflict** - one where two or more surveys each held a piece and no single survey could have seen the whole. These are the highest-value entries and there are **43** of them.

---

### C1 ✚ - The goal function, stated twice one day apart (seed entry 1)

| side | text | where | date | who |
|---|---|---|---|---|
| A | "five concurrent courses produce a fear of not holding the whole picture, which drives repeated polling… **Collapsing five reloads into one is the product.**" | `openclaw:log/2026-08-21` §reversals item 4; imported as `domain-design.md §2` | 2026-08-21 | unattributed in a list where six of eleven items carry `(Billy)`; the session is described as "almost entirely Billy correcting the agent's framing" |
| B | "**This is not an enterprise RAG that answers every question precisely.** It is a personal knowledge base whose job is: remove the anxiety of not finding information · manage cross-course information in the background · **locate details Billy himself does not know about.**" | `domain-design.md §10.7` ruling 4 | 2026-08-22 | **Billy, `[R]`** (verified by zoom) |

**Verdict: settled by recency, and both belong on the record.** B is one day newer, Billy-ruled, and `domain-design.md §10.4` (Billy, same day) says "§2 was never in question and is now the judge of everything else" - so B is stated as a *specification* of A, not a replacement. `model.md §1` adds a third increment the same day (first construction, not only recall). **The shift is itself evidence** and is prepared for Billy at **E7**: A names one product (interpretation-cost collapse); B names three jobs, of which only the second obviously is that product. Under merge rule 4, A is not discounted for lacking a `(Billy)` tag.

*What S5 got wrong here is void: it read A as the only goal statement and B as a downstream coinage. B is in the design of record, in Billy's own numbered list, one day after A.*

### C2 - Faithfulness measured at a scale where the thing measured could not occur

| side | text | where | date |
|---|---|---|---|
| A | 60 runs graded, **zero omissions** | 08-23 measurement, cited in `domain-design.md §2` | 2026-08-23 |
| B | "at a scale where omission was **not possible rather than avoided** … **The precision-versus-recall framing that cycle used is void: the recall half of faithfulness was never loaded.**" | same block, same file | recorded with A |

**Verdict: settled by an explicit ruling** - the record voids its own framing in place and states the conditions for a real test (five courses, the skeleton in the denominator, the corpus). No action; the limitation travels with the claim.

### C3 ✚ - The ±1-2 week window: a ruling with no body

| side | text | where | date | who |
|---|---|---|---|---|
| A | body still reads as if the window is unstated: "a *requirement he may state*, not a failure to fix" | `domain-design.md §2` | 2026-08-23 | Billy |
| B | "**was stated and ruled on this date, as `today-7d .. today+14d`**" - changelog only, no body | `domain-design.md` changelog | 2026-08-28 | Billy, ruled |
| C | the body: band A fires on `due` **or** `done_by` in `today-7d .. today+14d` **or** `state == in_progress` | `ring-0.md §3` | 2026-08-28 | Billy (window) / agent (`done_by`), ruled |

**Verdict: settled by an explicit ruling** - `ring-0.md §3` is the home. S1 found a ruling with no body; S2 found the body without knowing it closed a changelog-only orphan. → M3.

### C4 ✚ - `manifest` killed twice, on two grounds, neither citing the other

| side | text | where | date |
|---|---|---|---|
| A | the assertion surface is ruled out, **but `manifest` survives on a different justification**: it makes answers complete | `openclaw:log/2026-08-21` item 5; `domain-design.md §7`, §6 | 2026-08-21 |
| B | `course.manifest` graveyarded: "**exactly redundant with the rows** - 2c03 lists 15 and has 15" | `schema.md §7` | 2026-08-27/28 |

**Verdict: settled by recency.** B removes the field on a measurement that has nothing to do with A's justification, and does not cite it. No conflict of substance - the field is gone on both grounds - but a reader following A will look for a field that does not exist.

### C5 ✚ - Is the third goal a retrieval tuning or a deterministic query?

| side | text | where | date | who |
|---|---|---|---|---|
| A | "**Tune for recall, not precision.**" | `domain-design.md §10.8` | 2026-08-22 | self-declared **"Agent drafts, not ruled"** |
| B | set difference turns ruling 4's vaguest goal "**into a deterministic query**" | `model.md §6` | 2026-08-22 | unattributed |
| C | `nodes_without(node_kind, link_kind, direction)` - signature, tier, slice 2 | `design.md §3.4`, `architecture.md §7` | 2026-08-27 | Billy direction / agent table, ruled |

**Verdict: settled by recency and by merge rule 3.** A is self-declared unruled and is honoured as such; B was built. S1 recorded A-vs-B as an unreconciled mild disagreement; S2 held C without knowing what it settled. The two are not exclusive in principle (a recall-tuned retrieval and a set-difference query answer different halves), but only one has an implementation.

### C6 - Is disposability a ruling or an agent draft?

| side | text | where | date |
|---|---|---|---|
| A | `domain-design.md §9`'s header names §9.5 an **agent draft** | `domain-design.md §9` | 2026-08-21 |
| B | listed under "**Settled - do not re-litigate**" | `PLAN.md` §Settled | 2026-08-22 |
| C | inherited as a binding size bound on ring 0 | `ring-0.md §1` | 2026-08-28 |

**Verdict: needs Billy** (low weight). Under merge rule 3 a self-declared draft stays a draft; no record promotes §9.5. Yet two later records treat it as binding, and one derives a number from it (55 obligations). Nobody ruled it. Folded into **E1** because its content is the residency question.

### C7 ✚ - Two layers or three compartments?

| side | text | where | date |
|---|---|---|---|
| A | two layers; number holds, split axis wrong | `domain-design.md §3` + §10.5 | 2026-08-21/22 |
| B | three compartments - ring 0 / skeleton / store - with no mapping onto A | `model.md §4` | 2026-08-22, agent |
| C | "**Exactly TWO persisted things**"; **ring 0 "not separately"** - "residency is an access policy over `obligation` nodes" | `design.md §3.0`, `schema.md §3`, `ring-0.md §1` | 2026-08-27/28 |

**Verdict: settled by an explicit ruling.** C answers exactly the question `model.md §4`'s header raised and did not answer. S1 recorded the gap; S2 recorded the answer as "the most stable statement in the corpus" without knowing it was one.

### C8 ✚ - What a Node summary is for

| side | text | where | date | who |
|---|---|---|---|---|
| A | the skeleton answers "**is it worth opening**" | `model.md §4` | undated | agent, later marked "**carries no `[R]`**"; Billy: *"我不记得我定论过…"* |
| B | that framing "is wrong for the coordinator"; **NOT RULED**; the agent's replacement amendment "has not been ruled on" | `model.md §4.1` | 2026-08-23 | Billy + agent |
| C | "**a summary is written only where a node's identity is content the skeleton does not hold - the artifact, and nothing else in the current kind set.** An obligation's line is composed from what it already stores." | `architecture.md §5` | 2026-08-28 | **Billy, ruled** |

**Verdict: settled by an explicit ruling.** C is five days newer than B, Billy-ruled, and answers the question B left open by removing the object for every kind but one. S1 could not see C.

### C9 - `label`-versus-`summary` is deferred to a tier that does not exist

| side | text | where | date |
|---|---|---|---|
| A | "nothing in slice 1 is blocked by `label`-versus-`summary`" | `design.md §4`, prior text | pre-08-27 |
| B | "**it is no longer true that nothing is blocked by it.** A navigational surface renders a one-line summary at every level, so **the decision is presentation's first one.**" | `design.md §4` | 2026-08-27, agent, measured |

**Verdict: settled by recency** (A is withdrawn in place). The residue is not a conflict but a dependency: presentation's first decision, and presentation does not exist. → **E4**.

### C10 ✚ - Three layers or four kinds?

| side | text | where | date |
|---|---|---|---|
| A | three node kinds = three layers: obligation / concept / artifact | `derivation/BRIEF.md`, `model.md §2` | 2026-08-22 |
| B | six kinds across two slices - `course` · `obligation` · `sticky_note` · `progress`, then `concept` · `artifact` - and "**`layer` is a *different axis*** … **Introducing it early is precisely how the two axes get conflated.**" | `design.md §3.1` | 2026-08-27 |

**Verdict: settled by an explicit ruling** - B names the conflation as the failure mode and separates the axes deliberately. Not a contradiction: A's three layers are B's three skeleton kinds; `course` and the two annotation kinds are kinds without a layer. **Neither survey states this**; both inventoried one axis as though it were the only one.

### C11 - Is a course a node?

`design.md §3.2` (08-27): "**A course IS a node** … forcing in slice 1." `schema.md §1`: the kind tag permits a ref to a course "**whether or not courses ever join the node set**". **Verdict: settled by recency and by dependency** - `design.md`'s F5 requirement (course-level notes must land and read back) requires it; `schema.md`'s hedge is stale phrasing, not a competing position.

### C12 - `model.md §2`'s broken cross-reference on progress

`model.md §2` cites `domain-design.md §1.6` as making Billy-stated progress "a ring-0 row"; `domain-design.md §6.2` (08-24) and `schema.md §4.5` (08-28) rule it is an annotation of its own kind, and `ring-0.md §4` puts only `state` in the projection. **Verdict: settled by recency.** The parenthetical is stale; the ruling it protects (progress is Billy's own and survives the stateless constraint) is intact.

### C13 ✚ - A node with no store content vs a node that was never created

| side | text | where | date | who |
|---|---|---|---|---|
| A | `[A3]` J7: `backing: referenced_only`, ~13 instances; "**Midterm 2 is a graded obligation with a released grade and literally zero artifacts on disk**" | `derivation/agents/2c03-obligations-and-edges.md` | 2026-08-22 | agent |
| B | "an artifact does **not** need a URL or a `present` flag… **absence is not a field, it is the absence of store content**" (a JOIN) | `derivation/FINDINGS.md §5`; `model.md §2`, §9 | 2026-08-22 | **Billy, `[R]`** |

**Verdict: needs Billy** (deferred by slice). S3's own C1 states the residue precisely: the JOIN answers B2's set-difference concern but not A3's, because "a node with no store content is indistinguishable from a node that was never created". Billy ruled on the *field*; the *distinguishability* question was never put to him. Both the artifact kind and the store are slice 2/3, so nothing is blocked today. Folded into **E9**.

### C14 ✚ - H1's falsifier is blocked behind a tier that does not exist

| side | text | where | date | who |
|---|---|---|---|---|
| A | "H1 … is untested on an obligation-dense course; **gated on slice 2 running the extractor on 2px3**" | `model.md` header conditions | 2026-08-22 | Billy `[R]` on H1; gate unattributed |
| A′ | "**H1 now rests on two courses of the same shape, plus 2px3, which this run excluded.**" | `derivation/FINDINGS.md §1` | 2026-08-22 | agent |
| B | "**extracting the other three courses is not worth doing before the presentation tier exists.** … Reading three more courses without those rules **produces three more courses of noise and does not produce the rules.**" | `architecture.md §4` | 2026-08-28 | **Billy, ruled** |

**Verdict: settled by recency, and the consequence needs Billy.** B is newer, Billy-ruled, and its reasoning is sound on its own terms. **But it makes A's gate unreachable**, and A's gate is the only stated falsifier for the hypothesis the entire node-kind and edge model rests on. Neither ruling cites the other; nobody chose to leave H1 untestable. → **E3**. Three surveys, three pieces: S1 the gate, S3 why it matters, S2 the block.

### C15 ✚ - Three above-bar edges left the corpus without a ruling

The H4 bar was "**≥3 real instances and a nameable query**" (`derivation/TASK.md`). S3 C5/C6 found:

| edge | instances | query named | disposition |
|---|---|---|---|
| `contains` | 9 `[A2]` | yes | filed "**one sighting each**, deliberately not adopted" |
| `projects` / is-a-view-of | 6 `[A2]` | yes (de-duplication at expansion) | same |
| `sequence` | 3 `[B1]` | yes | same |
| `answers` | 6 `[A1]` | "which tutorials have I never worked through" | **appears nowhere** - not adopted, not cut, not watch-listed |
| `cites` | 25+ `[A1]` | yes | survives dissolved, **as the `locator` payload** |
| `example-code` | 15+ `[A1]` | yes | **appears nowhere in FINDINGS** |

**Verdict: partly settled by an explicit ruling, partly needs Billy.** `cites` and `example-code` are settled: `design.md §3.3` (08-27) measures **28 `locator` instances in 2c03 = 22 `cites` + 6 `example-code`**, so both survive as edge payloads rather than edge kinds. S3 recorded them as dropped; S2 recorded the 28 without knowing what it closed. **`answers` is genuinely lost** - above bar, with a named query, in no adopted/cut/watch list, and absent from `model.md §8` and `design.md §3.3`. And the three watch-listed edges are mischaracterised: FINDINGS' own table gives them 9, 6 and 3 instances under a heading saying "one sighting each". Folded into **E9**.

### C16 - Is the corpus append-and-supersede?

A: `domain-design.md §3` table, corpus write mode "**append + supersede only**" (08-21). B: `supersedes` **CUT** - zero instances across five agents and two courses, "actively harmful" (`derivation/FINDINGS.md`, `model.md §8`, 08-22); read-time expiry beats write-time supersession ~7:1 (`domain-design.md §10.3`); no `supersedes` row in `design.md §3.3` (08-27). **Verdict: settled by recency and evidence.** §3's banner covers the split axis, not this column, so the stale text stands unmarked.

### C17 ✚ - Announcements: channel or knowledge?

| side | text | where | date |
|---|---|---|---|
| A | `model.md §8`, §9 cite §10.6 as having **ruled** "announcements are a delivery channel" | `model.md` | 2026-08-22 |
| B | the channel proposition "**FALSIFIED in both**" - 5/55 and 6/38 net of redundancy, with the bias pre-registered *against* the convenient answer. What survives is narrower: "**almost always a correction against material the system already holds**" | `step-minus-1/FINDINGS.md §P6`; `domain-design.md §10.6` | 2026-08-22 |

**Verdict: settled by an explicit ruling** - B is the primary probe with its bias direction stated in advance, and `domain-design.md §10.6` carries its finding intact. `model.md`'s two paraphrases are wrong about what §10.6 found. S1 flagged the mis-citation and could not check it; S3 read the source. **The cut itself is unaffected** - `announcement → node` is merged into `sticky_note.origin` on independent grounds.

### C18 ✚ - "No relationship graph" overturned, on one side only

A: `domain-design.md §6` banner enumerates what changed and closes "**Everything else in §6 … is unchanged and still governs**", not listing this clause (08-25). B: `model.md §9`, "**Overturned by its own rule, not violated**" (08-22). C: `PLAN.md` §Settled already narrowed it on 08-22 - "**the *rule*, not the old type list**". D: `design.md §2` trigger C, "**Relations are records**", held explicitly unaffected by the tier re-scoping (08-27). **Verdict: settled by an explicit ruling.** S5's `PLAN.md` reading corroborates B independently, which S1 could not see; D makes it structural. §6's banner is stale on this clause.

### C19 ✚ - The rigidity rule now has two ruled exemptions

A: "**A field earns `typed` if and only if some mechanism reads it**", stated absolutely and banner-confirmed as "vindicated and unchanged" (`domain-design.md §6`, 08-21/22). B: `grade_share` - "**This is a standing EXEMPTION** … the exemption is the point rather than an oversight", reader "none, by exemption"; `added_at` - "**No mechanism reads it** … a declared exemption from the rule above" (`schema.md §2`, §3, Billy, 08-27). **Verdict: settled by recency.** Two Billy-ruled exceptions to a rule the domain corpus states without exception. Not a contradiction - an exemption presupposes the rule - but no domain record knows they exist, and the rule is invoked in the domain corpus as though absolute.

### C20 - The hub that survives every repair

`model.md §10` item 1: "**One hub survives every repair and it is on the artifact side, which this document did not model:** a review deck covers 26 of 26 concepts… Their honest relation is '**indexes the whole course**', not N peer `covers` edges. *Owed: how that is typed and rendered.*" Nothing in `records/spec/` addresses it; the artifact kind is slice 2. **Verdict: needs Billy** (deferred). Owed, unclaimed, and the only modelling question the corpus names as surviving its own repair.

### C21 ✚ - The adopted granularity rule is the split one of its own agents forbade

| side | text | where | who |
|---|---|---|---|
| A | adopt: the concept layer is cut at "**one thing that can be separately asked about or separately taught**" | `derivation/FINDINGS.md §1`, following `[B2]` J6 | agent synthesis |
| B | "**Do not rescue the first hub by splitting it into per-topic analysis concepts.** That is re-describing, which §10.1 forbids, and it would also be wrong: **the whole value of the concept is that Big-O of Quicksort and Big-O of Dijkstra are the *same* skill.**" | `derivation/agents/…` `[A2]` J1 | agent |

**Verdict: needs Billy.** S3 found it and could not resolve it; S1 imported only the adopted side (`model.md §10` item 1 carries A as a W2 extraction constraint, with no trace of B). Under merge rule 2 the adopted side does not win by having been written into the synthesis. Low urgency - the concept layer is slice 2 - but it is a rule about how the concept layer is cut, and it will be applied before anyone re-reads A2. Folded into **E9**.

### C22 ✚ - The derivation misreported its own agent on `produced`

A: `derivation/FINDINGS.md §1` watch list - "`produced` as a separate edge (A3, B2 - **both concluded a `role` attribute suffices**)". B: A3 J2 concluded the opposite and named the query `spec` cannot serve - "*show me what I handed in for A8*". C: `model.md §7.2` states A3's actual position correctly and marks it **Not ruled**. **Verdict: settled by an explicit ruling** (the question stays open, correctly). Recorded as a positive: the downstream record repaired an upstream misreport without noticing. S3 found the misreport; S1 found the repair.

### C23 - The `locator` payload absorbed two "lost" edges

See **C15**. `design.md §3.3`'s 28 measured instances (22 `cites` + 6 `example-code`) is the evidence. **Verdict: settled by an explicit ruling.**

### C24 ✚ - The dangling-edge requirement: dropped, then answered by another route

A: `[A3]` J6 - "**Ingest must be able to write an edge whose target does not exist yet, and must not create a duplicate when the other end arrives**" (08-22). S3: not in FINDINGS §6, **reads dropped**. B: `design.md §3.2` property 3 - "**A ref may name something that is not there**, so a ref is not a foreign key" (08-27). C: Billy, 08-28 - property 3's *construct-the-id* mechanism is closed, and the A8/A9 case is answered instead by "**list before linking, surface an untracked target to the user rather than auto-adding it, or resolve a batch ingest in two passes.**" **Verdict: settled by an explicit ruling.** The requirement survives its own drop, using its own example, three answers deep. The residue is that **the validation pass over the link set is "a real operation the design owes"** and is unbuilt.

### C25 - Where the purity cut falls

A: `model.md §5` body - "exactly between" by-handle and by-query (08-22, agent). B: `model.md §5` `REVISED` - "**wrong as written and it misleads** … three levels, not two … the cut belongs between the skeleton read and by-handle" (08-23, Billy). C: `design.md §3.5` - "**the skeleton's return type has no field a chunk could arrive in. Trigger D defused by type, not by restraint**" (08-27). **Verdict: settled by an explicit ruling.** B fixes the location; C converts it from a tool-registry fact to a type-system fact, which is the form that survives a container change.

### C26 ✚ - Where the vector index attaches

A: `domain-design.md §1.9`, Billy 08-21 - "**per-course buckets** for independence, metadata filtering". B: `model.md §5`, agent, explicitly "not ruled" - "embeddings attach to the **concept layer** as the entry point". C: `design.md §3.5`/§7 item 4, 08-27 - "**Not decided, and load-bearing for slice 3** … That implies **two** embedding sets, not one." Owner: the build, slice 3. **Verdict: settled by an explicit ruling that it is open, with an owner and a stated cost.** S1 registered A-vs-B as an unacknowledged cross-file disagreement; C names it open. The two are also not exclusive - a bucket is a partition, an entry point is a route.

### C27 ✚ - "What is week 7 about"

| side | text | where | date | who |
|---|---|---|---|---|
| A | the paradigm case of what the system is for: "when Billy asks '**what is week 7 about**', it holds the surrounding context" | `domain-design.md §10.4` | 2026-08-22 | **Billy** |
| A′ | "Ask '**what is week 7 about**' … **Where that line sits is the hardest and most important decision in this cycle**" | `PLAN.md` §What it is responsible for | 2026-08-22 | agent |
| A″ | listed as a skeleton-answerable scenario | `model.md §6` scenario 2 | 2026-08-22 | unattributed |
| B | **unanswerable** for 2aa4 from lecture material - zero occurrences of "Week N" in 687 KB - and "**the navigational handle is course-specific … a label on the coarse grouping that the schema never names**" | `model.md §9` | 2026-08-22 | unattributed, evidence-driven |
| C | the resolution: "**let the coarse grouping be the primary handle everywhere**"; and a `lecture_date` field, "for 2aa4 the **only** ordering signal that exists" | `derivation/agents/2aa4-lecture-concepts.md` J3, `[B1]` | 2026-08-22 | agent - **dropped from FINDINGS, S3 reads it as lost** |
| D | silence - no spec record names a coarse grouping, a module, a week, or a navigational handle | `records/spec/` | 2026-08-27/28 | — |

**Verdict: needs Billy.** All of A, B and C are the same day; recency cannot separate them. B's evidence is uncontested; A is Billy's own paradigm sentence; C is the only proposed resolution and it was dropped by an agent synthesis without a reason. Three surveys, three pieces. → **E8**.

### C28 ✚ - Is RAG inclusion decided by source class or by whether meaning survives linearization?

| side | text | where | date | who |
|---|---|---|---|---|
| A | "**RAG stores `slides / pdf / textbook`-class sources.** Handwritten tutorial notes are excluded - not embedded, effectively treated as absent. **The source-class rule is the operative one.**" | `domain-design.md §10.7` ruling 3 | 2026-08-22 | **Billy, `[R]`** (verified by zoom) |
| B | file-type routing "**falsified four ways in one slice**"; "the real axis is **whether meaning survives linearization** - a property of the materialization pass, **not of the file**" | `derivation/FINDINGS.md §4.1`, `model.md §9` | 2026-08-22 | agent, evidence-driven |
| C | handwritten scans are "**a whole class in a core course rather than the edge case P2 reported it as**", reproduced independently in two more courses | `step-minus-1/FINDINGS.md §P6`; `[A1]`, `[B2]` | 2026-08-22 | agent, measured |

**Verdict: needs Billy.** A source-*class* rule is a file-level rule of exactly the kind B retracts, and C says the excluded class is larger than the ruling assumed. All three are 2026-08-22. Recency cannot settle it; neither passage cites the other; the spec defers the whole pipeline to slice 3 "**Not decided, on purpose.**" S1 flagged the tension without the measurements; S3 has both measurements and not the ruling's standing. → **E10**.

### C29 ✚ - "Resolution is semantic" and the opaque id are the same claim, six days apart

A: `[B2]` J5, 08-22 - "**Resolution is semantic, everywhere, from three directions**"; identity must be topic-derived, never number-derived; header metadata is wrong in one of nine. B: `architecture.md §3` consequence 4, Billy 08-27 - "**matching two records is an interaction at the presentation tier, not an algorithm in the application tier**"; `schema.md §1.1`, Billy 08-28 - "**Constructing an id is a bet on reproducing another writer's spelling - a cognition problem wearing a mechanism's clothes**", with the `ChildMath A1` / `ChildsMath A4` evidence. **Verdict: settled by recency, and the earlier finding is the later ruling's unattributed ancestor.** Recorded because merge rule 4 makes A a full-weight statement of the same insight, and because the 08-28 changelog names the real cost: "**a divergence between two ruled records that nobody had propagated.**"

### C30 ✚ - One free-text field per type

A: `domain-design.md §6`, banner-confirmed "unchanged and still governs" (08-21). B: `model.md §7.2` (ingest writes summary + tags + sections) and §8.2 (`progress` carries state + detail + origin) - neither tested against A (S1's D22). C: `schema.md §1`, 08-28 - "**at most one field per kind. `course` has zero - a cap, not a quota**", and `obligation.notes` graveyarded "under the **non-overlap rule** … **All free text lives on annotations.**" **Verdict: settled by an explicit ruling for the kinds that exist.** `progress` complies (`detail` is its one free-text field). The `summary + tags + sections` case is artifact-side and slice 2, so B's untested half is deferred rather than resolved.

### C31 - `obligation.course` mutability: the code implements an unruled recommendation

`write-rules.md §3`: "*That* it is set at create and not updatable is an application-tier question, **still open at `../plan/application-tier.md §7.1` as a recommendation with no ruling. The code implements the recommendation; this record does not decide it.**" **Verdict: needs Billy** (low weight, and it is the general pattern of `STATUS.md`'s B28/B29 rather than a one-off).

### C32 ✚ - Date-only `due`: prose vs the number

A: `model.md §8.3`, promoted 08-24 from an experiment - "*'Due March 20'* means its **end**", measured cost: 2aa4's three dated obligations were **a day early in all 60 runs**. B: `schema.md §3` + changelog 08-27, "Billy 08-24 via `archive/changelog-2026-08-24-slice-1.md:241`" - "`due`'s date-only resolution is **`23:59`, the ruled value, restored over the prose *'the end of that day'* which lost the number.**" **Verdict: settled by an explicit ruling.** The domain record carries the weaker transcription of a ruling the spec restored - the one case in the corpus of a caught precision loss.

### C33 ✚ - `target_date` / `finished_by` / `done_by` - one field, three names, and nothing says so

| name | where | date | status |
|---|---|---|---|
| `target_date` | Billy's own hand-maintained Notion table, "kept for a year" (`derivation/TASK.md` §Courses, `FINDINGS.md §3`); and `model.md §8` vocabulary, undefined anywhere | 2026-08-22 | live in a domain vocabulary block, defined nowhere |
| `finished_by` | retired; "**never had a ruling behind it**" | pre-08-27 | retired |
| `done_by` | `schema.md §3`, Billy, ruled; "the date chosen to have this finished by"; `due − 7 days` is a *derived* value under its own name; **band-A trigger** | 2026-08-27/28 | current, fully specified |

**Verdict: settled by recency; the identification needs stating.** `done_by` is current. **No record anywhere says `target_date` and `done_by` are the same field**, and `target_date` is the name in the one artifact Billy actually maintains by hand. Corroborating measurement in a third survey the spec does not cite: Billy's own reports are "dated **7-13 days ahead of each due date**" (`step-minus-1/FINDINGS.md §P2`), which is the empirical anchor for the ruled 7 days. A three-survey merge that no survey made.

### C34 - `weight` / `worth_percent` / `grade_share`

S1's D27 records three names with "no passage says they are the same field or distinguishes them". `design.md §7` item 1: "**the field's own name is not settled. Owner: the user.**" All four spec records use `grade_share`. **Verdict: settled by an explicit ruling that it is open, with an owner.** Not drift - a deliberate deferral S1 could not see.

### C35 ✚✚ - `workload` was retired on a mechanism that was later removed

**The single most consequential cross-survey conflict in this merge.** Three surveys, three pieces, no two overlapping.

| step | claim | where | date | who |
|---|---|---|---|---|
| 1 | `workload` is **absent from every single obligation, in both courses, in every source**. Second independent falsification: Billy's own year-old Notion table has no workload column | `derivation/FINDINGS.md §3` (**S3**) | 2026-08-22 | agent, measured |
| 2 | `hours_estimate` is **NOT a field to be filled**, its null is not a gap. **"Size is observed ordinally - from `parts` and item notes first"**, then by asking for a relative comparison. **"Its missing-rate is retired as a guard signal. Replacement guard: faithfulness."** | `domain-design.md §6.1` (**S1**) | 2026-08-23 | **Billy, `[R]`** |
| 3 | `grade_share` is **reference only, a standing exemption**, "**because workload is judged from progress plus size rather than from the percentage**" | `schema.md §3` (**S2**) | 2026-08-27 | **Billy, ruled** |
| 4 | "`parts` carries concepts only; **the ordinal size-judgment reader is not designed. It is deferred** until a size-judgment need actually arises." | `schema.md` changelog (**S2**) | 2026-08-27 | **Billy, ruled** |
| 5 | "**`parts` carries concepts, and it does not carry size.**" | `write-rules.md §3.4` (**S2**) | 2026-08-28 | **Billy, ruled** |
| 6 | `parts` excluded from ring 0: "under `write-rules.md §3.4` it carries concepts rather than size **so it does not answer *how much* either**" | `ring-0.md §4` (**S2**) | 2026-08-28 | Billy direction / agent table |

**The state this leaves.** `workload` is retired. Its stated replacement - ordinal size from `parts` - was removed from `parts` and deferred with no owner and no trigger beyond "when a need arises". `grade_share`'s standing exemption from the rigidity rule is justified by a sentence naming that same removed mechanism. And ring 0, whose declared job is **routing**, carries **no size or effort signal of any kind** - not `workload`, not `parts`, not `grade_share`.

**Verdict: needs Billy.** Every step is Billy's and every step is defensible alone; recency settles each pair and settles nothing about the whole. The corpus contains no record that puts steps 2 and 5 side by side, because they live in different repositories' record sets and were surveyed separately. → **E2**.

### C36 - The conditional-weighting pointer was made optional

A: `model.md §10.9`, Billy 08-23 - "`worth_percent` keeps its value and gains a `conditional` marker **plus a pointer to the rule**, so no reader can take the stored number for a stated fact." B: `schema.md §3`, Billy 08-27 - "**The rule may optionally be left on a one-line sticky note; requiring one is not a rule**, because a schema rule that manufactures a conflict nobody would care about is a defect in the rule." **Verdict: settled by recency**, and worth naming: the pointer was half of what made the marker actionable against a defect measured at 38% of all faithfulness failures. Under B, a reader learns the number is conditional and may have no way to learn *how*.

### C37 ✚ - The late-day budget has a home

A: "the late-day budget is **NOT resolved** and stays open" (`model.md §10.9`, S1). A′: "a **course-level consumable resource that modulates every other obligation's effective deadline**. 'Can I be late on A5, and what does it cost me later?' **has nowhere to live**" (`[A1]`, S3). B: "course-level notes - **the late-day budget**, the snow-day credit, the conditional-weighting rule - must land and read back for F5 to pass" (`design.md §3.2`, 08-27, S2). **Verdict: settled by an explicit ruling.** A course is a node; a note hangs on it by an `about` link; it is a slice-1 forcing requirement. Two surveys called it homeless; the third holds the home. **The residue**: a note is free text, so "what does it cost me later" is not computable - the budget is *stored*, not *modelled*. That is the same trade as C36.

### C38 - Is `parts` owed or ruled?

A: `schema.md §9` item 1, "**Blocking a writer**" - "`parts` birth rules + prompt - **before anything writes the field**" (current body). B: `write-rules.md §3.4`, Billy 08-28 - answers what counts as one (the recurrence test, 50 candidates → 28) and what the wording is for (canonical singular concept name). **Verdict: settled by recency.** `write-rules.md` was created the next day to be exactly this rule's home; `schema.md`'s owed list was last rewritten 08-27 and does not cite it. **One sub-item is unanswered in both**: what context the writing agent must hold.

### C39 - The nullability analogy flipped and its consumers were not revisited

A: `optional` and `grade_share_conditional` made nullable, Billy 08-27, on the ground that a non-nullable bool "**is the same defect as rendering a null `progress.state` as `not_started`**". B: 08-28, Billy - `progress.state` is **not nullable** and `not_started` is a **defined default**, not an invention. **Verdict: settled by recency for `progress.state`; the two consumers stand unrevisited.** S2 states it: "The 2026-08-27 nullability ruling … cited this case as its analogy and was **not** revisited when the analogy flipped." The rulings are not in conflict - nullability for a *bool about a source's silence* is a different question from nullability for a *state with a natural zero* - but the stated reason for A no longer holds.

### C40 ✚ - How the `progress` defaulting fault is fixed

A: "The first is a **defaulting** fault, **fixed by rendering null as absence**" (`domain-design.md §6.2`, still current text; `model.md` changelog 08-25 says the same). B: "**the fault is fixed by a DEFINED default, not by rendering absence.** `state` is not nullable; no record reads as `not_started`" (`model.md §8.2` + changelog, Billy 08-28). C: the full ruling with its blast radius, ground and four rewritten sites (`schema.md §4.5`, Billy 08-28). **Verdict: settled by an explicit ruling** - `schema.md §4.5` is the authority and `ring-0.md §4` implements it. `domain-design.md §6.2` is stale; its changelog has no 08-28 entry. S1 found the one-sided landing; S2 found the ruling.

### C41 ✚ - `obligation.status`

A: `model.md §8` types `status{completion, score, evaluation}` and `model.md §4` puts `status` in ring 0 - never revised, and `model.md` was edited 08-28 without touching either. B: "`status` was dropped 2026-08-25" (`domain-design.md §9.1` + changelog, **agent - measured**, no ruler). C: graveyarded with a stated reason, and the finding behind it explicitly **mooted rather than contradicted** (`schema.md §7`); `status.evaluation` separately reaffirmed against a named challenge. **Verdict: settled by an explicit ruling.** C gives B the ruler B lacked. Three surveys, three pieces: S3 the A2/A9 evidence, S1 the unattributed drop, S2 the ruling. **Do not confuse `obligation.status` (dead) with `progress.state` (live, non-nullable, in both ring-0 bands).** No survey states the distinction.

### C42 - `workload`'s standing was recorded as ruled between a deferral and a retirement

A: Billy **deferred** where workload estimates come from, 08-21 (`openclaw:log` §Open threads). B: `PLAN.md` §Settled, 08-22, agent, no attribution - "**`workload` is stated by Billy, nullable, never defaulted**", under a do-not-re-litigate heading. C: Billy **retires** it, 08-23 (`domain-design.md §6.1`). D: graveyarded, 08-27/28. **Verdict: settled by recency.** B is superseded within 24 hours. Recorded because it is the clearest instance of the pattern S5 named (X5): an agent document recording as *ruled* three things Billy had *deferred*, one day later, under a heading forbidding re-litigation. Under merge rule 4 B is not discounted for being unattributed - it is discounted for being wrong on content one day later.

### C43 - The `count` graveyard entry disqualifies its own evidence

`schema.md §7`: "**Known cost, recorded rather than argued away:** the `n=1` behind not carrying `count` was measured on **the two courses least likely to contain recurring items**, and 2px3 was excluded throughout." And 2px3 cannot now be read (C14). **Verdict: settled by an explicit ruling, with the cost recorded.** No action, but it is the second thing (after H1) that the 08-28 sequencing ruling makes permanently untestable.

### C44 - `label` on every node

A: `model.md §8` gives `label(free text, written once at ingest)` to every node, unqualified. B: `model.md §7.1`, Billy 08-28 - that node line "**is agent-drafted and never had standing to block a ruling**"; an obligation carries no ingest-written summary. C: `schema.md §3` / `ring-0.md §4` - the field is `name`, "**not the handle and nothing is derived from it**"; `write-rules.md §3.1` - "**write the label the source uses**", no convention owed. **Verdict: settled by an explicit ruling.** A is disqualified by its own file and superseded by three spec rulings.

### C45 - P2's second stratum never ran

`step-minus-1/FINDINGS.md §P2` pre-registered a second sampling stratum; it "**never ran**, and no file in scope records a decision to abandon it" (S3). The 46% prose figure therefore rests on one sampling accident, and the derivation's own title-scoped 2aa4 extraction was a de-facto second stratum on a different professor's deck that **did** work - "**Nobody in the corpus connects the two.**" **Verdict: settled by recency**, in the sense that `domain-design.md §10.2` (Billy, 08-22) already said "**Most of P2's negative findings were artifacts of testing a method nobody had proposed.**" S1 has that ruling; S3 has the unrun stratum. The ruling reaches the same place from a different direction.

### C46 - Two records give different evidence for the same owed item

`schema.md §4` grounds `sticky_note.category`'s owed write rule on a distribution (one value holds 8 of 11 notes); `write-rules.md §4` grounds it on two independent passes producing two non-overlapping vocabularies. Neither cites the other. **Verdict: settled by recency** - both are 08-28 and both point the same way; the item is owed either way. Recorded because a reader closing it will want both.

### C47 - `erratum` is a legal `category` and the class the write rule most discards

`schema.md §4` lists `erratum` among `category`'s example values; `write-rules.md §4.0`'s measured pass rejects "**every erratum about a handout revision**, which mattered on the day and never again." **Verdict: settled by an explicit ruling** - not formally contradictory (the schema names a legal value, the write rule says when to write one), but the illustrative example should not be the discarded class.

### C48 ✚ - The length bound

A: measured on the domain side - notes run **87-278 characters**, a course level opens with **871**, against `write-rules.md §4.2`'s worked ~90; "**owed out of the presentation cycle rather than settled in advance**" (`model.md §10.5`, 08-28). B: demoted from `[R]` to owed because "**No ledger anywhere supports the ruled standing**" (`schema.md` changelog 08-25); "**The number is load-bearing: it gates whether the symmetry rule is affordable**" (`schema.md §9` item 3); "**the bound follows from what a rendered node can carry, not from a number chosen in advance**" (`write-rules.md §4.2`, 08-28). **Verdict: settled by an explicit ruling that it is owed, with an agreed shape.** Two corpora converged on the same answer independently and neither cites the other. Both say it covers **two** routes.

### C49 ✚ - Two of the projection's three entities do not exist

A: "The projection carries every course's **obligations, time-points and the current plan**" (`domain-design.md §9.1`, 08-21, later confirmed a ruling), and `model.md §7`'s retraction rests on that entity list surviving the grain's death. B: "**`time_point` and 'the current plan'**, both named by `domain-design.md §9.1` … `time_point` is not in slice 1; **the plan has no representation anywhere**, and this record does not invent one" (`ring-0.md §7`, 08-28). **Verdict: needs Billy.** `time_point` is a clean deferral with a stated reason. **The plan is not** - it is the coordinator's *only substantive work* under `domain-design.md §9.3`, and nothing in either corpus represents it. S1 recorded the entity list as what survived; S2 recorded that two thirds of it is missing. → **E5**.

### C50 - `has-more` is declared in a projection and in no schema

`ring-0.md §4` says so about itself: "the only one here that no record has yet declared", and "Whether it is a boolean, a count, or a set of present link kinds is **not decided here**." **Verdict: needs Billy** (low weight, newest material, honestly flagged).

### C51 - The graveyard's rulings stand; its arithmetic does not

`schema.md §7` carries a standing no-re-add rule over fifteen entries. Every count in it is stated over the 22-row fixture, which `architecture.md §4` (08-28) says is superseded and `schema.md`'s own 08-27 changelog calls "**a fixture that was rejected as a golden set**". Thirteen of fifteen entries carry no changelog line. **Verdict: settled by an explicit ruling** for the removals; **the evidence base is disqualified** and a later reader must not re-derive from the numbers. This is the most important caveat in the whole merge.

### C52 ✚ - §0.6's cross-domain requirement is homeless

A: "the academic domain must hold **course offering-terms and prerequisite structure**, since that graph gates other domains' decisions. **This is the single most concrete design input carried in the originating dispatch, and it is why 'just track my deadlines' is the wrong target**" (`domain-design.md §0.6`, 08-21). B: `course.offering_term` and `course.prereq` graveyarded - "null for both courses in the fixture, and **`offering_term`'s justification is another domain's need, in a domain that does not exist**" (`schema.md §7`); `course.manifest` graveyarded separately. **Verdict: needs Billy.** B's reason is a **container fact** ("a domain that does not exist"), not a domain fact, and the container has changed. Nothing anywhere says what now holds the requirement or whether it survives. S1 flagged it as homeless within the domain corpus; S2 supplied the reason it was removed without knowing what it was carrying. → **E6**.

### C53 - "Check the changelog for the reasoning" fails for half the period

`records/spec/` carries 54 changelog entries across five files and S2 found every live contradiction from them. `records/domain/` carries 11, all 08-25 or 08-28; everything decided 08-21 through 08-24 has its reasoning in in-place banners. **Verdict: settled by an explicit ruling** - S1 states it as a positive finding and the two changelog-only orphans are identified and re-homed (C3 and the §6-flagging reason). A property of the corpus, and it governs how to read everything above.

### C54 ✚ - Is the projection the same thing as ring 0?

A: `domain-design.md §9` (Billy, 08-23) records a reviewer's still-valid point - "§9.1 **never says 'ring 0'**, and the gloss *'ring 0 was arrived at by subtraction'* is a later paraphrase". `model.md §7`'s retraction rests on the paraphrase. B: three spec records state the equation as their own claim in near-identical words (`schema.md §3`, `design.md §3.0`, `ring-0.md §1`, 08-27/28). **Verdict: settled by an explicit ruling on the definition; the membership stays open (C49).** S1 could not see that the paraphrase became a ruling in three records.

### C55 - The projection grain: owed to slice 4, or already written

A: `schema.md §9` item 4 - "**A projection grain, owed to slice 4.** No current grain names the ring 0 fields `done_by`, `grade_share` and `optional`" (current body, last rewritten 08-27). B: `ring-0.md §4` is a grain and names all three with bands and reasons (08-28). **Verdict: settled by recency.** Note B *excludes* `grade_share` while A asks for a grain that *names* it; naming and including are not the same and no record says which A meant. `ring-0.md`'s "**It supersedes nothing**" is positioned against the *domain* record's dead grain, not against A.

### C56 ✚ - There is no ruled membership test for ring 0

A: "*an observation earns its place iff a judgment demonstrably changes when it is present*" - `domain-design.md §9.2`, self-declared "**agent formulation … not separately ruled**". B: "**A field belongs in ring 0 iff, without it, the coordinator cannot decide where to look next**" - `ring-0.md §2`, changelog-attributed "**agent-drafted**", and it explicitly declines A on a null result it then refuses in both directions. **Verdict: needs Billy** (medium weight). Under merge rule 3 both are unruled; the current field set was produced by an unruled agent test that declined another unruled agent test. Neither survey could see that both are unruled. Its container dependency is severe - see **E1**.

### C57 - The projection has been violating the symmetry rule

`ring-0.md §5` (08-28): "**The tiebreak is the handle, never file order.** Array order is insertion order is write history, and §9.2 rules out asymmetry that comes from interaction history. **The order measured in `findings/read-cycle.md` was array order, so the projection has been violating that rule rather than lacking a rule.**" **Verdict: settled by an explicit ruling** - the newest record convicts the implementation and states the fix. Recorded because it is evidence the symmetry rule is live and operative, which settles S1's D6b (`RECONCILE.md §5` is stale, not open).

### C58 ✚✚ - Is the coordinator long-running, and may its lifetime decide anything?

| side | text | where | date | who |
|---|---|---|---|---|
| A | "**The coordinator is long-running, not booted per session**" | `openclaw:log/2026-08-21` item 6 | 2026-08-21 | **Billy, explicit `(Billy)` tag** |
| A′ | restated five times: one persistent conversational master session; "corrected 08-21"; "an earlier draft had a two-stage assembly at session start - **that was wrong**"; "its long-running scale is **days-to-weeks**"; "**purity … *is* the longevity mechanism**" | `domain-design.md §1.11, §5, §9.1, §9.5, §9.3` | 2026-08-21 | Billy (§1.11); §9.3/§9.5 named agent drafts |
| A″ | listed under "Settled - do not re-litigate" | `PLAN.md` §Settled | 2026-08-22 | agent |
| B | "**The coordinator's lifetime is not a deciding fact here, and must not be reintroduced as one** … **every call may be a new process.**" Cost model: 52 KB, 0.27 ms, "**per-invocation and resident are indistinguishable**" | `design.md §5` conclusion 1 | 2026-08-27 | unattributed |
| C | "held **resident** by the coordinator"; "losing the coordinator costs one projection read"; "**ring 0 is resident for the coordinator and for nobody else**"; and the null result is refused because "every run was a memoryless `claude -p` cold start, and **the design's coordinator is long-running**" | `ring-0.md §1, §2, §7` | 2026-08-28 | Billy direction / agent |

**Verdict: needs Billy.** B and C are one day apart and both current. B is careful - it distinguishes the *conversation's* lifetime from a *process* holding the graph, and says so - so this is not a flat contradiction on the records' own terms. But C leans on residency in exactly the way B forbids reintroducing, in the newest record, without citing B. And **container drift lands on the premise both share**: A describes a human in front of one persistent conversational session; in a Claude Code plugin the coordinator is an agent session whose lifetime the plugin does not own, and `claude -p` cold starts - the instrument C disqualifies - are closer to the successor container than to A's. **If residency does not survive, M66, M67, M68, M72, M11 and ring 0's size bound all need re-deriving.** → **E1**.

### C59 - The coordinator's tool surface: three items or four

A: `domain-design.md §9.3` (agent draft, 08-21) - "read the fact projection · write plans · dispatch. **No corpus retrieval, no file reads, no fact writes.**" B: `model.md §7`/§7.1 (Billy `[R]`, 08-22/23) adds a fourth, the skeleton query, named `look_at`. C: `architecture.md` (Billy, 08-27) re-cuts the whole question onto tiers, where `look_at` is **presentation**, the application tier **has no surface**, and "a method does not defend itself against a caller that should not have called it." **Verdict: settled by an explicit ruling** - dissolved rather than resolved. S1's D17 asks a question the tier split stopped asking.

### C60 ✚ - What `look_at` returns

A: `{ summary, sticky_notes[], edges[] }` (`model.md §7.1`). B: `{summary, annotations[], edges[]}` (`model.md §8.2`, Billy 08-24; §7.1 not updated) - S1's D26. C: `schema.md §4.6` + changelog, 08-28 - "**It does not state the return shape, and the `{ summary, annotations[], edges[] }` it used to quote was not one** … read as complete, **it makes `obligation.parts` look homeless**", with a demonstrated cost ("a reader concluded from it that `obligation.parts` had nowhere to be returned"). D: `architecture.md §7` re-homes the verb to **presentation**, which does not exist. **Verdict: settled by an explicit ruling.** S1's D26 is moot - both shapes are withdrawn, by a record that says the triple was never a contract.

### C61 - A shape for returned conclusions, and the one instance of it

A: owed - "'Emit only conclusions' is a promise, not a mechanism, until the return value has a required form" (`model.md §10` item 4, 08-22). B: `land(candidates) -> Diff` with four outcomes, and "**one return type serves both**" the dev toggle and the conflict question (`design.md §3.6`, 08-27); re-homed and "**not in the first build**" (`architecture.md §7`). **Verdict: settled by recency for the one case; owed in general.** `Diff` is exactly the template A asked for, in the place it matters most, and neither survey connects them.

### C62 - The generated-content trust contract

`model.md §1`/§7: owed, agent position, "**Not yet ruled**", scope narrowed by H3's transcription result. Spec side silent (`concept` is slice 2). **Verdict: needs Billy** (deferred). Its scope depends on H3, which is untested and now blocked (C14, C70).

### C63 - Multiagent: a draft superseded by generalisation

`domain-design.md §8` is self-declared "draft, not ruled"; `model.md §7` (08-22) generalises off topology entirely. **Verdict: settled by recency and merge rule 3.** Recorded because §8's own conclusion - what differs between courses is "**a working-instruction bundle** … **Not an agent**" - describes a plugin, which is what the successor container is.

### C64 - "Ingestion" means two things and nothing reconciles them

Sense 1, out of scope, Billy 08-21: fetching. Sense 2, extensively designed across `model.md §7`, §8, §10: processing at the endpoint. **Verdict: settled by an explicit ruling** - S5's first-hand read of the 08-21 log establishes which sense Billy ruled on ("**He is the fetcher; the system's boundary starts at the endpoint**"), and it retired "source registries, coverage guarantees, scraping". No design work is invalidated; the word is overloaded.

### C65 ✚ - §4's counter-argument to read-time reconciliation, unanswered since 08-21

| side | text | where | date |
|---|---|---|---|
| A | storing-and-tagging leaves "due Wednesday" and "moved to Friday" coexisting for the LLM to reconcile at read time, which "***relocates Billy's uncertainty into the system while making it look handled***" | `domain-design.md §4`, quoted at `PLAN.md` §Open item 4 | 2026-08-21 |
| B | "The agent's position is that this holds for an unbounded pile and fails for a scoped, time-ordered set. **Answer it or accept the risk explicitly; do not pass over it.**" | `PLAN.md` §Open, owned here | 2026-08-22, agent |
| B′ | "**that is an assertion, not a design**, and it is the reason the allocation layer cannot shrink to zero"; named "**the entry point for the next design round**" | `domain-design.md §10.8` | 2026-08-22 |
| C | silence | all of `records/spec/`, through 2026-08-28 | — |

**Verdict: needs Billy.** The operations model is dead on measurement; its objection is not, and two independent documents flag it with an instruction not to pass over it. Six days of spec work never touched it. It is also the objection the "inbound is to be known" reframe (M83) walks into deliberately. S1 and S5 each hold one flag; neither could see that the other exists or that the spec never answered. → **E4**.

### C66 - The reframe's own stated risk, and the layer that mitigates it

`domain-design.md §10.5`: "§6's own stated failure mode is 'everything lands in free text… **the KB degrades into a note pile**.' **The reframe walks into that deliberately.** The only thing separating a designed KB from a note pile is that **the small allocation layer stays populated.**" That layer has since lost `workload`, `status`, `manifest`, `offering_term`, `prereq`, `count`, per-part scores and `notes`. **Verdict: needs Billy** - folded into **E2**, since the mitigation and C35's hole are the same layer.

### C67 - The ~30 confirmations figure

A: "~30 confirmations per semester" (`domain-design.md §4`, 08-21), still in place. B: "**not a real number** … ~115 across five courses; applied to destructive overwrites only it is 1-2 per course" (`§10.3`, 08-22). **Verdict: settled by recency.** The stratification survives; the figure does not; the successor principle is `architecture.md §3` consequence 3.

### C68 ✚ - Is Billy-authored input ever a dangerous write?

A: "**All dangerous inputs are external.** Billy-authored input … **is never a dangerous rewrite** - he is the authority on his own state" (`domain-design.md §4`, 08-21) - S1's D23. B: a spoken "A6 is done" against a portal record is **surfaced as a conflict** (`model.md §8.1`, Billy 08-23). C: F2 makes it an acceptance requirement and `Diff`'s CONFLICT outcome the mechanism; `architecture.md §7` makes the adjudication **presentation tier** (`design.md §1`, §3.6, 08-27). **Verdict: settled by an explicit ruling; the apparent conflict dissolves.** A is an authority claim about the *source*; B is a mechanism about the *write*. Three records, one posture. S1 could not see C.

### C69 ✚ - "Always keep, judge only linkage" vs "the agent never auto-adds"

A: retain every announcement's text; the agent decides only what to link and index; "**a misjudgment then costs retrieval reach, not data**" (`domain-design.md §10.8`, **self-declared agent draft**). B: "**The agent never auto-adds anything unless it is clear the user wants it.** … the user triggers it" (`architecture.md §3` consequence 2, Billy `[R]`, 08-27). C: the render test cuts 20 candidate notes to 12 (`write-rules.md §4.0`, Billy 08-28). **Verdict: settled by recency and merge rule 3** - A is unruled, B and C are Billy-ruled and later. **The residue**: the two are reconcilable (retain the *text* against the course; do not make a *row* or a *note*), but no record performs the reconciliation, and A's retention half now has no ruled home while its asymmetry argument (discarding a correction is silent, over-attaching is noisy) is untouched by B or C.

### C70 ✚ - H3 is untested and now blocked

A: "**PASS on both courses, and both results are uninformative** … **Both courses state their own outline. Neither exercised induction** … remains **UNTESTED**. Named as the single largest gap this run leaves" (`derivation/FINDINGS.md`, 08-22; imported as `model.md §10` item 6). B: P7, "**the last unrun piece of Step 0**", with a stated fallback - "retrieval falls back to whole-document plus course/week metadata, which costs precision and changes nothing here" (`PLAN.md`, 08-22). C: the 08-28 sequencing ruling blocks further extraction (C14). **Verdict: settled by recency, consequence needs Billy** - same shape as C14, same escalation (**E3**). Three surveys, three pieces.

### C71 ✚ - The corpus's best-evidenced hazard has no mechanism in slice 1

A: "**Stale material circulates as current**" - a prior year's solutions, 2025-dated tutorials, three uncorrected errors in current handouts, "'the corrected version is on the course site' **fails for the third time**"; and "**the redundancy defence is dead, verified on disk in both courses**" (S3 §18, §8). B: the mitigation is sticky-note timestamps plus maintenance-at-read - and "**In slice 1 that comparison has no input**, because the revision date belongs to a kind that does not exist yet" (`schema.md §4`, 08-28). **Verdict: settled by an explicit ruling** (the gap is stated by the record that owns the mechanism), **but the pairing is new**: S3 has the hazard, S2 has the mechanism and its gap, and no record states that the hazard the corpus proved hardest is the one slice 1 cannot address.

### C72 ✚ - The latent sticky note - an origin nothing detects

A: "This is a **third origin for a sticky note** … *the corpus disagrees with itself* - and it is the one that **most directly serves design §10.7 ruling 4** … **It is also the one nothing in MODEL detects.** I am not proposing a mechanism; I am recording that the class exists and is populated" (`[A1]`, 08-22). **`FINDINGS.md` records the count and not the class. S3 reads it as dropped.** A′: `[B2]` adds a fourth - corrections the author shipped inside the artifact. B: `domain-design.md §10.9` leaves "whether the correction seam is **detectable at intake**" open - "twelve is too few to build on". C: no fall26 record names the latent class. **Verdict: needs Billy** (medium weight, high leverage). The origin that most directly serves ruling 4's third job is recorded nowhere downstream. → **E11**.

*Note: `[A1]`'s citation of "§10.7 ruling 4" here is correct on the zoomed text - ruling 4's third job is locating what Billy does not know to ask about. S5's X4 reads this as inconsistent reference; that reading is void.*

### C73 ✚ - Billy's folder warning, overridden by the document that recorded it

A: "**Folder structure is not taxonomy.** Billy's folders are admissible **only** as evidence of the organization *he reaches for under pressure* … **never cited as the course's structure.** (Billy, 2026-08-22.)" B: the same `TASK.md` §3 then makes his folder renames and study guide the **sealed ground truth**, arguing "**correct, and irrelevant, because the target is not the course's taxonomy**". S3: "**an agent overriding a human warning by reframing what is being measured** … **the override is not marked as one.**" C: the same error committed straight, inside `MODEL §3`, and caught: the 2aa4 row "was written from folder appearances … **exactly the *folders-are-not-taxonomy* error this cycle exists to avoid**." **Verdict: needs Billy** (low weight, method rather than domain). B may well be right; it is an unmarked override of a Billy rule by the document carrying the rule, and the H3 result that rests on the sealed ground truth (C70) is downstream of it.

### C74 ✚ - Billy authors concept edges by hand, mid-semester, and nothing designs for it

A: "Skeleton authored by Billy once at course setup" - **retracted**: "at setup Billy does not yet know the concept structure; **he knows it at the end**" (`model.md §9`). B: "**[NEW] Billy authors them by hand, unprompted, mid-semester**" - the TUT7 ink edge (in a form with **no text layer**) and the mid-semester folder renames, "the same behaviour in two modalities" (`derivation/FINDINGS.md §5`, `[A2]`). C: "One clause in a tutorial handout creates **9** `requires` edges; one slide in a review deck creates **26** … **they are not** drawn item by item. **An edge is only as current as its sentence, and that sentence's document is dated 2025.**" **Verdict: needs Billy** (deferred - concept is slice 2). "Not at setup" is not "not by Billy", and B is a fourth origin for concept edges with a measured modality (ink, no text layer) that no record designs for. Folded into **E9**.

### C75 ✚ - Asking: "the system ASKS" vs "the system must not chase the agent"

| side | text | where | date | who |
|---|---|---|---|---|
| A | "假如需要判断的时候再问...**让系统从 waiting for input 变为 asking for input**...但我自己都忘记了怎么可能 provide。" A third class of facts, captured **at the READ - the system ASKS**; "a progress state is generated by nothing, so **forgetting to supply it is structural rather than a lapse**" | `domain-design.md §9.6` | ruled 2026-08-23 | **Billy, `[R]`, verbatim** |
| A′ | the governor, same block: "**only ask what changes a decision** … Left ungoverned this degenerates into an interrogation - one blind run produced about nine askable items" | same | 2026-08-23 | Billy |
| B | "**The system must not chase the agent.** … A schema rule that manufactures a conflict a person would not care about is a defect in the rule." | `architecture.md §3` consequence 3 | 2026-08-27 | **Billy, `[R]`, first person** |
| B′ | applied to remove an occasion to ask: a nullable `progress.state` "makes the system announce it does not know, which **gives an agent a reason to ask *have you started this yet*** - the system chasing the agent" | `schema.md §4.5` | 2026-08-28 | **Billy, ruled** |

**Verdict: needs Billy.** Both sides are Billy's, four days apart, and they point opposite ways on the same act - asking about progress. A says forgetting is structural so the system must ask; B′ removes the nullable state *specifically so it has no reason to ask about progress*. A′'s governor is the intended reconciliation and neither record invokes it against the other. Recency favours B′, but B′ is a schema mechanism and A is a capture-point ruling, so they are not obviously the same object. **The sharpest recency-does-not-settle-it case in the corpus.** → **E12**.

### C76 - `source: asked` is `origin`

`domain-design.md §9.6` (Billy 08-23) says an asked answer persists with `source: asked` stated prominently; S1 could not tell whether that is `model.md §8.2`'s `origin`. `schema.md §4`/§4.5 (08-28) answers: `origin` values are announcement / `stated` / `asked`, shared across both annotation kinds, and imports the domain sentence verbatim. **Verdict: settled by an explicit ruling.** The write rule for `origin` is **OWED** with the failure already measured: "both passes reached for *what document class it came from*."

### C77 - The domain corpus is outside the tier scheme

`architecture.md §2`: `../domain/` gets tier "**none - it is the material both tiers are derived from, and it predates the split.**" **Verdict: settled by an explicit ruling.** This is the corpus's own statement that S2's records do not supersede S1's wholesale - they are derived from them. It is why per-thing dating is the only correct merge and why the "spec is superseded, domain is live" hypothesis in the brief is the wrong shape (S2's own conclusion: volatility is concentrated at field level, not at abstraction level).

### C78 - "A write rule never refers to the source" is contradicted by three of the five rules written under it

A: `architecture.md §3` consequence 1, Billy `[R]`, 08-27, still standing; echoed in `write-rules.md`'s conditions block. B: `write-rules.md` changelog 08-28 - "**the condition line's absolute phrasing is corrected.** *'A rule here never refers to the source'* **was contradicted by three of the five rules**; the real distinction is **the direction a rule is derived from**." Instances: "store what the material prints" (§3.1), "`optional` defaults to false **unless a source states otherwise**" (§3.5), "when a source does not state a value and the agent infers one, **it asks the user**" (§1.1). **Verdict: settled by an explicit ruling; the correction never landed in either body.** Both `architecture.md §3` and `write-rules.md`'s conditions still carry the withdrawn phrasing, and it is what a reader hits first in both.

### C79 - Consequence 3's container-sensitivity propagates into the field set

"The system must not chase the agent" is quoted from Billy in the first person about "**daily usage**" by a person. It is the ground cited by `schema.md §4.5` (progress.state non-nullable) and `schema.md §3` (the optional note on conditional weighting). **Verdict: needs Billy** - folded into **E1**. Not a conflict between records; a conflict between a ruling's premise and the successor container, which reaches two field-level rulings through it.

### C80 - The MCP adapter is demoted and may never be built

`architecture.md §4`, §5, Billy 08-27: the MCP adapter is presentation, "at most an adapter over the CLI's grammar, **and may never be built**"; the verb-routing and screenshot-extraction evaluations are re-homed to presentation and cannot run against an application tier with no descriptions. **Verdict: needs Billy.** Current by date and Billy-ruled. **In the successor container the adapter is the product.** → **E1**.

### C81 - The 1-to-9 docstring measurement is evidence about the successor container

"**rewording one docstring moved a verb's call count from 1 to 9 with data availability held constant**" (`design.md §3.6`, quoted at `architecture.md §5`) is the load-bearing evidence for two rulings, and it is a measurement of an LLM routing over tool descriptions. **Verdict: settled by an explicit ruling** - and recorded as the one place the old container's evidence transfers *directly* to the new one. `architecture.md §5`'s transport-independence clause ("**A server exposing exactly ONE tool whose argument is a command string has the same property**") is the bridge.

### C82 - "Human-readable by default, a machine branch for machine consumption"

`architecture.md §5`, Billy 08-28. **Verdict: needs Billy** - folded into **E1**. Current and correct for a CLI; in the successor container the primary reader is the agent, which inverts which branch is the default. The binding constraint under it survives either way: **every read that returns records must return their handles.**

### C83 - 22 obligations versus 14

A: `design.md §1` F5 and every count in `schema.md §3`, §6, §7 (current bodies). B: `architecture.md §4`, Billy 08-28 - "a fresh extraction found **14** for 2c03, and the old count included a row the graveyard forbids, so **22 is not reachable by re-running the old route.**" C: `ring-0.md §4`, 08-28 - "**6 of 14** obligations carry an annotation". **Verdict: settled by an explicit ruling.** The superseded number is still what a reader hits first in two records, and it underwrites every graveyard count (C51).

### C84 - Postgres/pgvector versus no database

A: pgvector 0.8.0 PASS, HNSW built (`step-minus-1/FINDINGS.md §P1`, `domain-design.md §10.1`, 08-22); "fall26 gets its own Postgres schema and its own MCP" (`PLAN.md` §Settled, 08-22). B: "**The skeleton does not need a database**", measured at 0.27 ms (`design.md §5`, 08-27); "no MCP, no Postgres" (`design.md §1` constraints). **Verdict: settled by recency**, and they are about different halves - A is the store (slice 3), B is the skeleton (slice 1). B says so; A's `PLAN.md` bullet does not.

### C85 - "Directly-callable Python" versus TypeScript

A: `design.md §1` constraints, still current text. B: `architecture.md §6`, Billy 08-27, ruled - TypeScript, on the ground that "**Python cannot refuse**" and two of this design's own mechanisms presuppose a compiler that can. **Verdict: settled by an explicit ruling.** `design.md §3.7` is already compatible ("not committed to Python"); §1's constraint line is stale and is what a reader hits first. `architecture.md §2` lists `design.md`'s presentation passages as re-scoped; the language constraint is not among them.

### C86 - "The coordination layer reads all of it every time"

`domain-design.md §5`'s no-fold argument rests on it, and ties itself to §3 explicitly; §3's banner calls the same premise "**false as written**" for ordinary conversation and does not propagate to §5. **Verdict: settled by recency** - the premise is superseded where §3 says it is (ordinary conversation), and survives where §5 uses it (the *facts* layer is small and structured, which §10.5 also affirms: "the allocation layer needs no retrieval"). Narrow, not fatal.

### C87 - Three rulings deferred by Billy, recorded as ruled the next day

A: "Billy **deferred all three** to when the build reaches them" - Notion authority/projection, own tables vs PA's todos, where `workload` comes from (`openclaw:log/2026-08-21` §Open threads). B: "**The three build-spec §7 decisions, ruled 08-22**" under a do-not-re-litigate heading, no attribution (`PLAN.md` §Settled). **Verdict: settled by recency for two of three; the third is superseded (C42).** Recorded because the *deferral condition Billy set* - when the build reaches them - was not the condition under which they were recorded as ruled, and the build was two cycles away. Under merge rule 4 B is weighed on content: `workload` was reversed in a day, "its own Postgres schema and its own MCP" was reversed in five, and only "Notion is a projection" still stands unchallenged.

### C88 - Is rendering in scope?

A: Notion "removes the **only** human-facing rendering requirement from this repo" (`domain-design.md §1.8`, Billy 08-21). B: `model.md §2` defers which spine a view renders as a CLI/UX decision; `§7.2` rules a note renders with the summary; `§10.5` measures rendering the course level in characters; `architecture.md §5` (08-27) makes rendering the presentation tier's entire content and "**every one-line summary**" its property. **Verdict: settled by recency.** A's premise is false; the ruling that the calendar goes to Notion is untouched.

### C89 - `/promote` and `/wrap` are repo rituals two rulings depend on

`/promote` is the escape valve `domain-design.md §6` and `model.md §10.9` both lean on; `/wrap` is the capture-point ritual §9.6 re-cut. Both are slash commands in a repo that no longer exists. **Verdict: needs Billy** - folded into **E1**. A plugin has skills and commands; whether one is `/promote` is a design question, not an inheritance.

### C90 - Preferences: a draft whose analogy broke

`domain-design.md §8` (self-declared draft) rests on "preferences are **structurally identical to `progress`**"; `progress` then moved out of the fact-type table into an annotation kind (M51), and `preference` is not a kind in either spec slice. **Verdict: needs Billy** (low weight, deferred). Under merge rule 3 the draft stays a draft; but §6's table already types a `preference` row and §9.3 already assigns it an extractor, so the corpus half-adopted an unruled draft.

### C91 - The method survives, and it is the only recorded fix for a stall

Pre-registration, ambiguity-against-the-proposition, thresholds fixed in advance, raw artifacts kept, no design vocabulary in the raw pass, "agents draft and never self-lock", "**a conclusion whose evidence was deleted is not auditable**" (S3 §20); the seal's failure and its correction ("**copies, never symlinks, and strip document metadata**"); and `write-rules.md`'s 08-28 statement that abstract rule-writing "**stalled for two months**" and was broken by deriving rules from Billy's own hand edits. **Verdict: settled by an explicit ruling** - no conflict. Registered because it is the one thing in the corpus that is neither domain nor container, and because the plugin container inherits it for free.

---

# Part III - The escalation shortlist

The conflicts needing Billy - **25** carrying that verdict outright, plus **3** carrying a *consequence needs Billy* rider (C14, C15, C70) - grouped into **12 escalations** and ordered by how much downstream work hangs on each. Each one is prepared so the evidence and the rules are in front of Billy: both versions quoted, dated, sourced, with what turns on the answer. **None is adjudicated here.** Where I have a view about which way the *evidence* leans, it is labelled as such and is not an answer.

---

## E1. Does the coordinator's residency survive the container change?

**Covers:** C58, C6, C56, C79, C80, C82, C89. **Blocks:** the whole observation contract (M66-M74), the surface rulings (M100-M101), and two field-level rulings that inherit a container premise.

**Side A - Billy, 2026-08-21, and restated five times.**
> "**The coordinator is long-running, not booted per session** (Billy). The agent's two-stage assembly-at-boot model died; the *projection* survived, restated as a standing constraint." - `openclaw:log/2026-08-21-fall26-domain-design.md` §reversals item 6, explicit `(Billy)` tag.

> "Billy faces one persistent, high-level, conversational master session; depth only exists in freshly opened, targeted subagents." - `domain-design.md §1` ruling 11.

> "**do not try to make it survive a semester.** Its long-running scale is **days-to-weeks**." - `domain-design.md §9.5`.

**Side B - the spec tier, 2026-08-27, stated as a guard.**
> "**The coordinator's lifetime is not a deciding fact here, and must not be reintroduced as one:** the one-persistent-session decision is about the **conversation's** lifetime… and says nothing about a process holding the graph in memory. **The skeleton and its verbs are invoked on demand; every call may be a new process.**" - `design.md §5` conclusion 1. Measured: 52 KB, 0.27 ms; "per-invocation and resident are indistinguishable."

**Side C - the newest record, 2026-08-28, leaning the other way.**
> "**ring 0 is resident for the coordinator and for nobody else**" - `ring-0.md §7`. And the refusal of a null result that would otherwise have removed five ring-0 fields: "every run was a memoryless `claude -p` cold start, and **the design's coordinator is long-running** … **A device that cannot exercise routing returns 'nothing changed' whether or not routing matters.**" - `ring-0.md §2`.

**What turns on it.**

1. **Ring 0's existence as a distinct concept.** "Residency is an access policy over `obligation` nodes" (`schema.md §3`, `design.md §3.0`, `ring-0.md §1`). If nothing is resident, ring 0 is a *default query shape*, not a policy - which may still be worth having under a different name.
2. **The field set's protection.** `findings/read-cycle.md §4` ran the domain corpus's own membership test and returned **nothing** - `parts`, `grade_share`, the skeleton, a complete ring 0 and `progress` were "each read, each rendered, **none changing the plan's shape**". `ring-0.md §2` refuses that null result *solely* because the instrument was a cold start and the design's coordinator is not. **If the successor's coordinator is a cold start, the null result is no longer disqualified**, and the current seven-field set loses the argument that protects it.
3. **Disposability, the discard rule, and the size bound.** "If losing the coordinator session loses information, the design is wrong" (`domain-design.md §9.5`); "expansions are discarded, never sedimented" (`model.md §7`); "losing the coordinator costs one projection read - **that is ring 0's size bound: roughly 55 obligations**" (`ring-0.md §1`). All three are free or meaningless if nothing persists between calls.
4. **The surface.** "The presentation tier is a **CLI**"; the MCP adapter is "at most an adapter over the CLI's grammar, **and may never be built**" (`architecture.md §4`, §5, Billy 08-27). In a Claude Code plugin the adapter is the product. The bridge the corpus itself supplies: "**The distinction is independent of transport** … **A server exposing exactly ONE tool whose argument is a command string has the same property**" (`architecture.md §5`) - so the *grammar* ruling may survive intact while the *CLI* ruling does not.
5. **Two field-level rulings inherit the premise.** `architecture.md §3` consequence 3 - "The system must not chase the agent", quoted from Billy about **daily usage** by a person - is the stated ground for `progress.state` being non-nullable (`schema.md §4.5`) and for the conditional-weighting note being optional (`schema.md §3`).

**Rules that apply.** Recency does not settle B vs C (one day apart, both current, neither cites the other). Container drift is orthogonal to both. Merge rule 3 makes `domain-design.md §9.5` a draft that two later records treat as binding without promoting it (C6).

**The question, narrowly.** Not "is the design wrong" - it is: **in the successor container, is there anything that persists between reads, and if not, which of the five items above are re-derived and which are dropped?** `design.md §5` already answers the *persistence* half in the container-neutral direction and shows its work.

---

## E2. `workload` was retired on a mechanism a later ruling removed - and nothing carries size

**Covers:** C35, C66. **Blocks:** the obligation field set, ring 0's routing job, `grade_share`'s standing exemption, and the mitigation the "inbound is to be known" reframe relies on.

**The chain, all Billy, six days, three record sets.**

> **08-22, measured** (`derivation/FINDINGS.md §3`): "**`workload` is absent from every single obligation, in both courses, in every source.** … This is the second independent falsification of that field - **Billy's own hand-maintained Notion table, kept for a year, also has no workload column** and *does* have a `target_date` the schema lacks."

> **08-23, Billy `[R]`** (`domain-design.md §6.1`), verbatim: "hours_estimate 很难量化，我一般都是按照某个 assignment 的进度和 high-level 体量来判断的。" Ruled in three parts: not a field to be filled; "**Size is observed ordinally - from `parts` and item notes first**, then by asking for a relative comparison"; "**Its missing-rate is retired as a guard signal. Replacement guard: faithfulness.**"

> **08-27, Billy, ruled** (`schema.md §3`): `grade_share` is "**Reference only** - never an input to a computed ranking, **because workload is judged from progress plus size rather than from the percentage.** **This is a standing EXEMPTION** from the rule every other field passes."

> **08-27, Billy, ruled** (`schema.md` changelog): "`parts` carries concepts only; **the ordinal size-judgment reader is not designed. It is deferred until a size-judgment need actually arises.**"

> **08-28, Billy, ruled** (`write-rules.md §3.4`): "**`parts` carries concepts, and it does not carry size.**"

> **08-28** (`ring-0.md §4`): `parts` excluded from the projection - "under `write-rules.md §3.4` it carries concepts rather than size **so it does not answer *how much* either**."

**What this leaves.** `workload` is graveyarded with a standing no-re-add rule. Its stated replacement mechanism is gone. `grade_share` is exempted from the rigidity rule on a reason that names that removed mechanism. And **ring 0 - whose declared job is routing, "which node is worth one `look_at`" - carries no size or effort signal of any kind.**

**Why it matters beyond one field.** `domain-design.md §10.5` names the risk the whole inbound reframe takes: "§6's own stated failure mode is 'everything lands in free text… the KB **degrades into a note pile**.' **The reframe walks into that deliberately. The only thing separating a designed KB from a note pile is that the small allocation layer stays populated.**" That layer has since lost `workload`, `status`, `manifest`, `offering_term`, `prereq`, `count`, per-part scores and `notes`.

**Rules that apply.** Recency settles every adjacent pair and settles nothing about the whole. Every step is Billy's. **No record in the corpus places the 08-23 ruling and the 08-28 ruling side by side, because they live in different record sets and were surveyed separately.**

**The question, narrowly.** **Is the ordinal size reader still owed, and if so where does it live?** Three sub-questions, each cheap: (a) does anything read size today; (b) if not, is `grade_share`'s exemption reason still true as written; (c) is "faithfulness" (the replacement guard, §6.1 part 3) actually a guard against the same failure the missing-rate guarded, or a different one?

---

## E3. H1 and H3 are untestable behind a tier that does not exist

**Covers:** C14, C70, and C43's second-order effect. **Blocks:** whether the node-kind and edge model generalises beyond two courses of one shape.

**Side A - the gates, 2026-08-22.**
> "§3's H1 (course type = per-layer density) is untested on an obligation-dense course; **gated on slice 2 running the extractor on 2px3.**" - `model.md` header conditions.

> "**H1 now rests on two courses of the same shape, plus 2px3, which this run excluded.**" - `derivation/FINDINGS.md §1`. And on H3: "**Both courses state their own outline. Neither exercised induction** … remains **UNTESTED**. Named as the single largest gap this run leaves."

**Side B - Billy, 2026-08-28, ruled.**
> "**extracting the other three courses is not worth doing before the presentation tier exists.** Every contested field - `parts`, a note's `category`, `origin`, whether a note is worth keeping at all - needs a write rule, and a write rule is derived from what a value must be for a node to render well. **Reading three more courses without those rules produces three more courses of noise and does not produce the rules.**" - `architecture.md §4`.

**What turns on it.**

- H1's own falsifier is "a course that needs a node kind or edge kind the others do not." 2px3 is the `woven` profile, named in the origin cycle as "**the hardest case routing must survive**" and excluded from every run so far. It is also the course whose absence weakens the `count` graveyard entry ("the `n=1` was measured on **the two courses least likely to contain recurring items**, and 2px3 was excluded throughout").
- H3's fallback is stated and cheap: "retrieval falls back to whole-document plus course/week metadata, which costs precision and changes nothing here" (`PLAN.md`). So H3 being untested is a *precision* risk, not a structural one.
- B's reasoning is sound and self-contained. **Neither ruling cites the other. Nobody chose to leave H1 untestable.**

**Rules that apply.** B wins by recency and attribution. Rule 2 says A's gate does not survive merely by having been stated first - but A is not a conclusion, it is a *stated condition on a live hypothesis*, and B silently removes it.

**The question, narrowly.** **Is H1 still gated, and on what?** Three options visible in the corpus, none chosen: (i) accept H1 on two courses and record the exposure; (ii) keep the gate and accept that the model is provisional until presentation exists; (iii) read 2px3 for **structure only** (does it need a kind or edge the others lack) without extracting records - which is a different and much cheaper act than what B rules out, and B does not address it.

---

## E4. §4's counter-argument to read-time reconciliation, open since 2026-08-21

**Covers:** C65, C9's dependency, and it is the stated entry point for the next design round.

**The objection, verbatim, quoted in two independent documents.**
> Storing-and-tagging leaves "due Wednesday" and "moved to Friday" coexisting for the LLM to reconcile at read time, which "***relocates Billy's uncertainty into the system while making it look handled***." - `domain-design.md §4`, quoted at `PLAN.md` §Open item 4.

**Both flags, both saying do not pass over it.**
> "The agent's position is that this holds for an unbounded pile and fails for a scoped, time-ordered set. **Answer it or accept the risk explicitly; do not pass over it.**" - `PLAN.md` §Open, and owned here, 2026-08-22.

> "**that is an assertion, not a design**, and it is the reason the allocation layer cannot shrink to zero." Named "**the entry point for the next design round**." - `domain-design.md §10.8`, 2026-08-22.

**The state.** The operations model it defends is dead on measurement (39% reduction; `step-minus-1/FINDINGS.md §P5`, bias resolved against the proposition). The objection survives its own model's death. **Six days of spec work (08-23 to 08-28) never touched it** - nothing in `records/spec/` addresses read-time reconciliation. And `domain-design.md §10.4`'s replacement ruling ("inbound arrives to be known") walks into the exact failure mode §4 named, with §10.5 saying so in place.

**Rules that apply.** Rule 5, sharply: the documents establish that this question was asked twice and answered zero times. Recency does not apply - there is no second side, only silence.

**The question, narrowly.** **Answer it or accept the risk explicitly.** The corpus's own instruction, unchanged. The agent's position is on the record and is labelled an assertion; the two options the documents leave are (i) design the read-time reconciliation, or (ii) record that the risk is accepted and why.

---

## E5. "The current plan" has no representation anywhere

**Covers:** C49. **Blocks:** the coordinator's only substantive output.

**Side A - 2026-08-21, later confirmed a ruling.**
> "The projection carries every course's **obligations, time-points and the current plan**, with no free text." - `domain-design.md §9.1`. And `§9.3`: the coordinator does "**plan generation** - its only substantive work, **because it *is* coordination**."

**Side B - 2026-08-28.**
> "**`time_point` and 'the current plan'**, both named by `domain-design.md §9.1` as part of the projection. `time_point` is not in slice 1 (`schema.md §7`); **the plan has no representation anywhere**, and this record does not invent one." - `ring-0.md §7`.

**What turns on it.** `time_point` is a clean deferral with a stated reason (its reader is the calendar projection, which is out of slice 1). **The plan is different**: it is the coordinator's only output, it is one of three things the projection was ruled to carry, and no kind, field or link in either spec slice represents it. `model.md §7`'s retraction of the hold-the-whole-skeleton draft rests on the entity list `obligations · time-points · plan` surviving the field grain's death - so a third of the thing that survived does not exist.

**Rules that apply.** B is newer and states its own non-invention honestly. It does not overrule A; it reports A unimplemented.

**The question, narrowly.** **Is a plan a stored thing or a generated one?** If stored, it is a kind and nothing has designed it. If generated per read, `domain-design.md §9.1`'s projection ruling needs restating, because a generated plan is not something a projection "carries".

---

## E6. §0.6's cross-domain requirement is homeless, and it was removed on a container reason

**Covers:** C52. **Blocks:** whether the system's target is wider than one semester.

**Side A - 2026-08-21, the strongest statement in the corpus of why this is not a deadline tracker.**
> "Winter-only mandatory courses ruled out a winter-27 co-op, and thereby set the entire recruiting target to summer 27. That decision was made inside ai-eng's academic track, and **Fairy never held the fact - because no home existed for a constraint spanning academics and career.** So the academic domain must hold **course offering-terms and prerequisite structure**, since that graph gates other domains' decisions. **This is the single most concrete design input carried in the originating dispatch, and it is why 'just track my deadlines' is the wrong target.**" - `domain-design.md §0.6`.

**Side B - graveyarded.**
> `course.offering_term` · `course.prereq`: "null for both courses in the fixture, and **`offering_term`'s justification is another domain's need, in a domain that does not exist**." - `schema.md §7`, under a standing "do not re-add without a new ruling" rule.

> `course.manifest`: "**exactly redundant with the rows.**" - same.

**What turns on it.** B's reason for `offering_term` is **a container fact, not a domain fact** - "a domain that does not exist" is a statement about what else was running in openclaw. The container has changed, and the new repo's brief describes a fresh start with no inherited domains at all, which does not obviously make the requirement more or less alive. Nothing in either corpus says what now holds offering-term and prereq, or whether §0.6 survives. `domain-design.md §0.1`'s telos is still on the record: "**every aspect of Billy's life managed under one contract.**"

**Rules that apply.** B wins by recency on the *fields*. Rule 5 says §0.6 is evidence a question was asked, not a reason to re-add anything. Rule 2 says §0.6 does not stand merely by being early and emphatic - but B never engages §0.6's argument, only its fields' fixture nullity.

**The question, narrowly.** **Is the system's boundary one semester, or the academic domain?** If the former, §0.6 is dead and should be recorded dead. If the latter, the requirement needs a home and the graveyard entry needs a new ruling to reverse it.

---

## E7. The goal function, in two forms one day apart (seed entry 1)

**Covers:** C1. **Blocks:** nothing structurally - and it is the frame everything else is judged against, which is why it is here.

**Form 1 - 2026-08-21.**
> "**The goal function was wrong.** Not reminders - Billy is rarely behind. It is that **five concurrent courses produce a fear of not holding the whole picture, which drives repeated polling.** Reading a notice is cheap; *interpreting* it forces a full context reload. **Collapsing five reloads into one is the product.**" - `openclaw:log/2026-08-21-fall26-domain-design.md` §reversals item 4; imported as `domain-design.md §2`.

**Form 2 - Billy, 2026-08-22, `[R]`.**
> "**This is not an enterprise RAG that answers every question precisely.** It is a personal knowledge base whose job is: **remove the anxiety of not finding information · manage cross-course information in the background · locate details Billy himself does not know about.**" - `domain-design.md §10.7` ruling 4.

**Form 2′ - Billy, same day, a completion of Form 1.**
> "dropped into an assignment's requirements he still has to model the requirements / tasks / topics himself, and helping with that is why the system exists." The reload is **first construction**, not recall. Consequence: "**the product is collapsing the reload, so modelling that does not reduce reload cost is out of scope.**" - `model.md §1`.

**What the shift is.** Form 1 names **one** product and it is a cost reduction: five interpretation passes become one. Form 2 names **three jobs**, of which only the second ("manage cross-course information in the background") is obviously that product; the first is an emotional outcome, and the third ("locate details Billy himself does not know about") is a *capability the system did not previously claim* and is the one `domain-design.md §10.8` says is "the only one not served by 'retrieve when asked'". Form 2 is also the only place either form says what the system is **not**.

**Rules that apply.** Recency gives Form 2, and `domain-design.md §10.4` (Billy, same day) says §2 "was never in question and is now **the judge of everything else**" - so Form 2 is stated as a specification of Form 1, not a replacement. Rule 4: Form 1 is not discounted for lacking a `(Billy)` marker.

**Why it is on the list anyway.** `model.md §1`'s consequence - "**modelling that does not reduce reload cost is out of scope**" - is the corpus's only anti-inflation test, and it is derived from Form 1's cost framing. Under Form 2's third job, work that *increases* what Billy reads (surfacing what he did not ask about) is in scope by definition. The two tests point opposite ways on the same proposal.

**The question, narrowly.** **Which form is the anti-inflation test taken from?** Not which form is right - both are Billy's - but which one a downstream ADR cites when it has to reject something.

---

## E8. The navigational handle - "what is week 7 about"

**Covers:** C27. **Blocks:** whether the coarse grouping is a modelled thing.

**Side A - the paradigm case, Billy, 2026-08-22.**
> "when Billy asks '**what is week 7 about**', it holds the surrounding context." - `domain-design.md §10.4`. Restated the same day as the cycle's hardest question: "Ask '**what is week 7 about**' - some of the answer is on hand, the rest is fetched. **Where that line sits is the hardest and most important decision in this cycle.**" - `PLAN.md`. And listed as skeleton-answerable at `model.md §6` scenario 2.

**Side B - the same day, measured.**
> "687 KB of 2aa4 lecture text contains **zero** occurrences of 'Week N', and the course has no announcement stream - its lecture layer is genuinely timeless." So "*'what is week 7 about'* is unanswerable for such a course from lecture material, while *'what is topic X about'* answers well. **The navigational handle is course-specific - week for 2c03, module for 2aa4 - and it is a label on the coarse grouping that the schema never names.**" - `model.md §9`.

**Side C - the proposed resolution, dropped.**
> "**accept that the navigational handle is course-specific - week for 2c03, module for 2aa4 - and let the coarse grouping be the primary handle everywhere.**" - `derivation/agents/2aa4-lecture-concepts.md` J3, `[B1]`. Plus a `lecture_date` field, "for 2aa4 the **only** ordering signal that exists". **Neither is in `derivation/FINDINGS.md`'s adopted, cut or watch lists.** No reason is recorded.

**Side D - silence.** No record in `records/spec/` names a coarse grouping, a module, a week, or a navigational handle. `time_point` is deferred (E5). The invariant that forbids a `week` field is intact and correct: "`week` is a retrieval term, and 2px3 organises by week while other courses organise by topic or assignment number. **Hardcoding either is the failure**" (`domain-design.md §10.5`).

**Rules that apply.** A, B and C are the same day. Recency cannot separate them. B's evidence is uncontested and B is the one that names the cost as unpriced.

**The question, narrowly.** **Is the coarse grouping a first-class thing?** The invariant (no time axis, no `week` field) is not in question. What is in question is whether the *per-course label on the coarse grouping* - week / module / unit - is a modelled property, a rendering convention, or nothing. Today it is nothing, and the sentence used to describe the product cannot be answered for one of the two courses read.

---

## E9. Four slice-2 residues that will be acted on before anyone re-reads their evidence

**Covers:** C13, C15, C21, C74. Grouped because each is cheap alone, all four are deferred by slice, and each is a case where a *dropped or overruled agent finding* will be silently re-decided by whoever builds slice 2.

**(a) A node with no store content vs a node that was never created.** Billy ruled 08-22 that an artifact needs no URL and no `present` flag - "absence is not a field, it is the absence of store content", read as a JOIN. That answers `[B2]`'s set-difference concern. It does not answer `[A3]`'s: "**Midterm 2 is a graded obligation with a released grade and literally zero artifacts on disk**", ~13 `referenced_only` instances in 2c03, and a corrected query - "obligations whose posted solutions I never downloaded" - that "would have flagged all seven missing test-script zips and both midterm solution sets". *The distinguishability question was never put to Billy; only the field was.*

**(b) The `answers` edge.** 6 instances, named query "which tutorials have I never worked through", cleared the stated H4 bar (≥3 instances **and** a nameable query), and **appears in no adopted, cut or watch list**, and in neither `model.md §8` nor `design.md §3.3`. Two of its siblings (`cites` 25+, `example-code` 15+) survive as the `locator` payload - `design.md §3.3` measures exactly **22 `cites` + 6 `example-code` = 28** - so their disappearance is explained. `answers` is not.

**(c) The granularity rule contradicts the agent it was drawn against.** Adopted: cut concepts at "one thing that can be separately asked about or separately taught". `[A2]` J1 argued the opposite for its own hub: "**Do not rescue the first hub by splitting it into per-topic analysis concepts** … **the whole value of the concept is that Big-O of Quicksort and Big-O of Dijkstra are the *same* skill.**" Not reconciled anywhere; only the adopted side reached `model.md`.

**(d) Billy authors concept edges by hand, mid-semester.** "Skeleton authored by Billy once at course setup" was retracted - at setup he does not know the structure. But `[A2]` found the positive fact: "**Billy authors them by hand, unprompted, mid-semester**" - the TUT7 ink annotation ("This question tests: ① MAD compression ② linear probing insertion ③ probe counting", **on a page with no text layer**) and the mid-semester folder renames, "the same behaviour in two modalities". *"Not at setup" is not "not by Billy", and nothing designs for the mid-semester case.* Related and unaddressed: "One clause in a tutorial handout creates **9** `requires` edges; one slide in a review deck creates **26** … **an edge is only as current as its sentence, and that sentence's document is dated 2025.**"

**The question, narrowly.** These four do not need answering now. They need **recording as open before slice 2 starts**, because each is a case where the corpus's synthesis lost or overrode a finding that its own bar admitted.

---

## E10. Is RAG inclusion decided by source class, or by whether meaning survives linearization?

**Covers:** C28. **Blocks:** the corpus pipeline (slice 3), which is "Not decided, on purpose."

**Side A - Billy, 2026-08-22, `[R]`.**
> "**RAG stores `slides / pdf / textbook`-class sources.** Handwritten tutorial notes are excluded - not embedded, **effectively treated as absent**. (Agent note on the criterion: they fail on **density and redundancy, not on volatility** - posted notes do not change. **The source-class rule is the operative one.**)" - `domain-design.md §10.7` ruling 3.

**Side B - the same day, measured.**
> File-type routing was "**falsified four ways in one slice**" - a PDF wrapping scanned handwriting; a text PDF whose exercises **are images**, so backing is not uniform *within one file*; a `.png` carrying a rendered prose block, more chunkable than several PDFs; one diagram held as both `.drawio` and `.png`. "**The real axis is whether meaning survives linearization** - a property of the materialization pass, **not of the file**." - `derivation/FINDINGS.md §4.1`, imported at `model.md §9`.

**Side C - the same week, on the size of the excluded class.**
> 2c03's tutorial notes are handwritten scans at ~23 extractable characters per page, "making image-only material **a whole class in a core course rather than the edge case P2 reported it as**", reproduced independently by two agents in two more courses. And the requirement that creates: "**a silent empty index entry is not deferrable, because it makes the corpus lie about its own coverage.**"

**What turns on it.** A source-*class* rule is a file-level rule of exactly the kind B retracts. A excludes a class C says is core, in a corpus where `[A2]` found Billy's densest hand-authored concept edges living precisely in handwritten form. And A's own agent note concedes the criterion is density-and-redundancy, not the source class - which is a *content* judgment wearing a *class* label.

**Rules that apply.** A, B and C are all 2026-08-22. Recency cannot settle it. A is Billy's ruling; B and C are measurements. Rule 3 does not help - A is a genuine `[R]`. Neither passage cites the other, and the spec defers the whole pipeline.

**The question, narrowly.** **Does ruling 3 survive the linearization axis, and does "excluded from RAG" mean "not embedded" or "not held"?** A says "effectively treated as absent"; B's `text_extractable` (default false, true only when a pass recovered text) already provides a per-region mechanism that would let handwritten material be *held and marked* rather than *absent*. The two may be compatible under a narrower reading of A.

---

## E11. The latent sticky note - the origin that serves ruling 4's third job and that nothing detects

**Covers:** C72.

**The finding, `[A1]`, 2026-08-22, recorded by its author as unclaimed.**
> The two real contradictions in A1's slice - a deck and its handout disagreeing about which assignment a tutorial covers - **arrived with the original material**. "Nothing was delivered; the conflict is inert until someone reads both documents in the same sitting … This is a **third origin for a sticky note** beyond 'a correction arrives' and 'Billy states one' - ***the corpus disagrees with itself*** - and **it is the one that most directly serves design §10.7 ruling 4** … **It is also the one nothing in MODEL detects.** I am not proposing a mechanism; I am recording that the class exists and is populated."

**A fourth origin, `[B2]`, same cycle.** Two of its five sticky notes are "corrections **the author shipped inside the artifact**" (the JUnit 4/5 caveat; the conform-not-correspond footnote). "**The sticky note is not only an inbound-correction mechanism.**"

**What happened to them.** `derivation/FINDINGS.md` records A1's **count** ("2 latent") and not the **class**. No fall26 record names either origin. `domain-design.md §10.9` leaves the adjacent question open - "whether the correction seam is **detectable at intake**. The twelve instances share a signature - they name a document - **but twelve is too few to build on**" - which is about *inbound* corrections, a different origin.

**Why it is worth Billy's eye.** `domain-design.md §10.7` ruling 4's third job is "**locate details Billy himself does not know about**" (verified verbatim). A1 identified the one sticky-note origin that directly produces such details - the corpus contradicting itself, inert until someone reads both documents - and said in the same sentence that nothing detects it. `model.md §6` scenario 5 ("what should I know that I have not asked") is answered by set difference plus sticky notes, which presumes the notes exist.

**Rules that apply.** Rule 4: A1's finding is openclaw material and is weighed on content. Rule 5: it is evidence a class exists, not a reason to build a detector.

**The question, narrowly.** **Are latent contradictions in scope, and if so, does anything create the notes?** A1 explicitly declined to propose a mechanism. The corpus has three note origins with mechanisms and one without.

---

## E12. Asking: "the system ASKS" and "the system must not chase the agent" are both Billy's

**Covers:** C75. **Blocks:** the capture point for the third class of facts.

**Side A - Billy, ruled 2026-08-23, `[R]`, verbatim.**
> "假如需要判断的时候再问...**让系统从 waiting for input 变为 asking for input**...前者要求你 proactively provide input，但我自己都忘记了怎么可能 provide。" - `domain-design.md §9.6`.
>
> The class it creates: "facts with no generating event - origin Billy himself, time-criticality only when needed, capture point **at the READ - the system ASKS**. The third class is self-authored but not durable: **progress**, difficulty, how much load a week already carries. A deadline is generated when the professor posts it; **a progress state is generated by nothing**, so there is no moment at which it could be volunteered and **forgetting to supply it is structural rather than a lapse.**"
>
> Its own governor, same block: "**only ask what changes a decision.** Left ungoverned this degenerates into an interrogation - one blind run alone produced about nine askable items, which is not an improvement on one stale value. **The gate that decides what belongs in the observation space and the gate that decides what is worth asking are the same gate.**"

**Side B - Billy, 2026-08-27, `[R]`, first person.**
> "**The system must not chase the agent.** *'The system is designed to help me, not to raise questions, conflicts or concerns that no one will ever care about in daily usage. The schema-level rules shouldn't be a burden that keeps chasing the agent.'*" - `architecture.md §3` consequence 3.

**Side B′ - Billy, 2026-08-28, ruled, applying B to remove an occasion to ask about exactly A's example.**
> "a nullable state would make the system **announce it does not know and give an agent a reason to ask *have you started this yet***, which `architecture.md §3` rules a defect in the rule." Therefore `progress.state` is **not nullable** and absence reads as `not_started`. - `schema.md §4.5`.

**What turns on it.** A's canonical example of the third class is **progress**. B′'s canonical application is **progress**. A says the system must ask because forgetting is structural; B′ removes the mechanism that would prompt the ask, on the ground that asking is chasing. A'`s governor ("only ask what changes a decision") is the intended reconciliation and **neither record invokes it against the other**. Downstream: `schema.md §4.5`'s three progress rules include "**only the owner authors it**", enforced "**nowhere, deliberately**" - so nothing today either asks or prevents asking.

**Rules that apply.** Both sides are Billy's. Recency favours B′ by five days. But rule 1's escalation clause applies twice: recency does not settle it (they are about different objects - a capture-point policy and a field's nullability), and the newer ruling removes the mechanism the older ruling's whole point depended on.

**The question, narrowly.** **When does the system ask about progress?** Three positions are consistent with the record and the corpus does not choose: (i) never unprompted - `not_started` is the answer and A's third class is served some other way; (ii) at the read, governed by A′'s gate - which requires something other than a nullable field to trigger it; (iii) A is about *difficulty and load* and B′ is about *state*, in which case A's third class survives minus its own headline example.

---

# Part IV - Coverage

## What I merged

**All four surveys, in full: 2,870 lines.** S1 (1,194), S2 (1,006), S3 (402), S5 (268). Every thing entry, every disagreement table, every coverage note and every container list in all four was read and is accounted for below.

**Input counts and how they merged.**

| survey | things it inventoried | conflicts it recorded | where they went |
|---|---|---|---|
| S1 | 88 things | 32 (D1-D32) + 11 marked-by-the-documents | all 88 mapped; D1-D32 all carry a register entry |
| S2 | ~59 things (T1-T50 with sub-letters) | 15 (D1-D15) | all mapped; D1-D15 all carry a register entry |
| S3 | 20 concrete things + 11 origin-intent items + a vocabulary table | 11 (C1-C11) | all mapped; C1-C11 all carry a register entry |
| S5 | ~24 intent items + 11 conclusions + 11 `PLAN.md` assertions | 8 (X1-X8) | X2, X5, X6, X7, X8 carried; **X1, X3, X4 discarded with the void audit** |

**Output: 114 merged things in six clusters; 91 conflicts.** Verdicts split **39 settled by an explicit ruling · 27 settled by recency · 25 needs Billy**; three of the settled ones carry a *consequence needs Billy* rider (C14, C15, C70), so the escalation shortlist draws on **28**. **43 conflicts are marked `✚` cross-survey** - a conflict at least two surveys each held a piece of and no single survey could have seen. Twelve escalations prepared.

**Merge ratio.** 88 + 59 + 20 + ~24 ≈ 191 source entries → 114 merged things. The compression is almost entirely one thing appearing under different names in different record sets. The largest merges:

- **`workload-estimate` / `workload` / `hours_estimate`** - three names, three surveys, one field (M53).
- **`target_date` / `finished_by` / `done_by`** - three names across three sources, and **no record anywhere says they are one field** (M46, C33).
- **`weight` / `worth_percent` / `grade_share`** - three names, and `design.md §7` records the name as an open item with an owner (M47, C34).
- **`sticky_note.kind` / `category`; `note-on` / `about`; `label` / `name` / `summary`; `MODEL.md` / `model.md`; the design of record / `domain-design.md`; three layers / six kinds; the projection / ring 0; `Skeleton operations` / `the slice-1 verbs`.**

**Provenance zooms - two, both to settle load-bearing questions the surveys raised and could not close.**

1. `fall26/records/domain/domain-design.md §10.7`, read whole. Purpose: settle Correction 1. Result: ruling 4 contains "**anxiety**" and "**locate details Billy himself does not know about**" verbatim, in Billy's own numbered list dated 2026-08-22. S5's citation audit is void on the text, not just on the boundary; and `PLAN.md`'s five-bullet restatement is confirmed as the thing that does not match.
2. `fall26/records/spec/ring-0.md` §1, §3, §4 and changelog. Purpose: close seed entry 2. Result: the field set, the bands, `today-7d .. today+14d`, `has-more`, and `ring-0.md`'s "It supersedes nothing" positioning, all confirmed as S2 reports them.

Nothing else was opened. `fall26/evidence/` was reachable and not used - no claim in this merge needed it.

## The two seed entries

**Seed 1 - the goal function, stated twice one day apart.** Both forms are in the inventory (M1) and the register (C1) and are prepared for Billy at **E7**. Verdict: settled by recency toward `domain-design.md §10.7` ruling 4 (Billy, 08-22), with §10.4 (Billy, same day) establishing that Form 2 specifies Form 1 rather than replacing it. **The shift is kept as evidence**: Form 1 names one product and it is a cost reduction; Form 2 names three jobs, one of which is a capability that *adds* to what Billy reads. `model.md §1`'s anti-inflation test is derived from Form 1's framing, which is why the escalation asks which form a downstream rejection cites.

**Seed 2 - ring 0's field set. Closed.** S1 found four non-identical lists and said the authority was outside its boundary; S2 read the authority. `ring-0.md §4` (2026-08-28, Billy direction / agent table) carries a seven-field two-band table with a per-field reason, and `ring-0.md`'s own conditions line states its relationship to the dead grain: "**It supersedes nothing; it answers what §9.1 left open.**" The four superseded lists are tabulated at **M67**; three of them contain fields the graveyard forbids. **One residue**, which is the merge's own finding: `schema.md §9` item 4 still lists "a projection grain, owed to slice 4" and does not cite `ring-0.md`, created the next day to be exactly that (C55).

## What I could not reconcile, and why

**1. Four numeric pairs, none closable from inside any survey's material.**

| pair | sides | why it stays open |
|---|---|---|
| **18 vs 11 `about` facts**; "zero at course level" vs "4 hang on the course" | `design.md §3.3` (imported 08-25 from openclaw evidence) vs `ring-0.md §7` (08-28, measured on `evidence/2026-08-28-corpus`) | probably two different corpora; **both are stated as the count of `about` facts in the material** and no record reconciles them. Load-bearing on both sides: `design.md §3.2` uses the course case to argue a course must be a node in slice 1; `ring-0.md §7` uses the 4/7 split to say the course level is owed 4 notes |
| **N≈300 vs V=640** | `design.md §3.4` opening vs the same section's cost table and §5 | same record, same section, unreconciled. Neither survey could resolve it and neither can I without the evidence folder |
| **22 vs 14 obligations** | `design.md` F5 and `schema.md §3/§6/§7` vs `architecture.md §4` (Billy 08-28) | **settled as a ruling** (C83) but not propagated: every graveyard count still stands on 22 |
| **~45 vs ~53 `spec` edge instances** | `design.md §3.3` (~45, 2c03) vs `model.md §7.1` ("roughly **53 instances across both courses**; the ~45 figure quoted through the 08-23 session is 2c03 alone") | reconcilable and reconciled by `model.md §7.1`; recorded because the spec record still carries the un-annotated 45 |

**2. `[A1]`'s `answers` edge.** Above the H4 bar with a named query, in no adopted, cut or watch list, and absent from both `model.md §8` and `design.md §3.3`. Its two siblings' disappearance *is* explained by the `locator` payload (C15, C23). This one is not, and no document in any survey's slice says what happened to it. Left dangling at **E9(b)**.

**3. Whether `target_date` and `done_by` are one field.** I assert in M46 and C33 that they read as one thing - "the date chosen to have this finished by", corroborated by Billy's own Notion column and by his reports being dated 7-13 days ahead. **No record in any of the four slices says so**, and `model.md §8`'s `target_date?` carries no definition anywhere. This is the one place in the merge where I have identified two names as one thing on inference rather than on a record saying so. It is flagged as such.

**4. The 08-23 demotion of `progress` to a sticky-note kind.** Referenced and overturned in both domain files; **written out in neither**. Its two grounds are quoted ("the ordinal invited invention", "no mechanism reads it") and both are answered, but the ruling itself is in no survey's slice.

**5. `spec §10.9 item 3` and the "2026-09-01 ruling".** `domain-design.md §6.1` says it reverses a 2026-09-01 ruling. **That date is in the future relative to every other date in the corpus.** S1 recorded it verbatim and could not resolve it; neither can I without `records/plan/` or `records/archive/`.

**6. `has-more`'s definition.** Declared in `ring-0.md §4`'s projection, in no schema record, and `ring-0.md` says so about itself. Newest material, honestly incomplete (M61, C50).

**7. `RECONCILE.md §5`.** Both domain files record that a third document still lists the symmetry-rule question as open and is stale on that point. Neither can fix it from inside; nor can I - it is in the out-of-bounds `2026-08-23-slice-1/` tree. S2's evidence that the rule is live and operative in `ring-0.md §5` settles the *question*; the stale document remains stale (C57).

## Where the four surveys disagree about the corpus itself

These are disagreements about **what the corpus is**, not about the domain. They matter more than the domain conflicts because they determine how everything else is weighed.

**A. Whether `model.md` is frozen - and it is not.** S1 establishes the correction: the title says "frozen 2026-08-22", the body carries `[R]` rulings dated 08-23, -24 and -28, and the changelog records edits on 08-25 and three on 08-28. **S3 and S5 both frame `MODEL.md` and `PLAN.md` as a fixed spine that later work is scored against** - S3 says "every H1-H4 verdict… is scored against a document out of scope", S5 says "for the corpus that scores its verdicts against MODEL/PLAN, this is the PLAN half". That framing predates the correction and does not survive it. **Applied throughout: neither domain file is standing by position; only per-thing dates decide.**

**B. Whether the design of record exists.** S5's **Finding zero** concluded the ticket's premise was wrong and that the design of record was outside every boundary. It was inside S1's: `domain-design.md`'s own import line reads "from `openclaw:devlog/ideas/2026-08-21-fall26-domain-design.md` on 2026-08-25", which is exactly the file S5 named as unreachable. **S5's X1 says its own §20-coverage gap is "still open after this survey"; it was closed by S1 before S5 wrote.** Same for S3's coverage item 1 (`MODEL.md` unreadable): `model.md` is its successor and S1 read it whole. **Two surveys' largest declared gaps were already covered by a third.**

**C. Attribution density as a credibility discount.** S3 counts "roughly eleven passages in the whole corpus that are explicitly the human's own words" in 2,974 lines and builds an INTENT/CONCLUSION tagging scheme on it. S5 counts "**2 verbatim Billy fragments**, roughly 0.5% of the file" and "**zero** Billy attributions" in `PLAN.md`, and treats the 08-21 goal function as "unattributable" for want of a `(Billy)` tag inside an otherwise-tagged list. **Ruled by Billy 2026-08-29: the openclaw material is his own words; those agents simply did not cite him the way the fall26 agents did.** Applied as merge rule 4 throughout. It changes the standing of at least: the 08-21 goal function (M1, E7), the layer split (M13), the operations-model routing (M82), the retirement predicate (M25), and every `PLAN.md` assertion, which is now weighed on content and date - and on content, three of its "settled" items were reversed within five days (C42, C87).

**D. Whether the spec tier is superseded, and in which direction the two corpora relate.** S2 tested the hypothesis and split it: "**the field-level layer moved constantly, the tier-level and abstraction-level layers did not move at all.** The hypothesis's own qualifier - *especially anything schema-level* - is the part the evidence supports, and it supports it strongly. The unqualified form is not." S1 did not test it. **S2 also reports that the spec records "defer to the domain records repeatedly and never overrule them."** The merge shows that is too generous: the spec **does** overrule domain records - `schema.md §4.5` reverses `domain-design.md §6.2`'s stated fix (C40); `schema.md §3` restores a number `model.md §8.3`'s prose lost (C32); `architecture.md §5` answers what `model.md §4.1` left NOT RULED (C8); `schema.md §3` grants two exemptions to a rule `domain-design.md §6` states absolutely (C19). S2 could not see it because it did not read the domain records. **The corpus's own statement of the relation is `architecture.md §2`**: `../domain/` gets tier "none - it is the material both tiers are derived from, and it predates the split" (C77) - derivation, not supersession, which is why per-thing dating is the only correct merge.

**E. Granularity of "a thing".** S1 flags this against itself: "several entries could reasonably be split or merged - `label` and 'what a Node summary is for' are arguably one question about node identity; `workload`, `status` and `weight` are arguably one question about the obligation's field set… **Anyone landing these in a single source of truth should re-cut that boundary deliberately.**" S2 cuts finer (per field, per convention); S3 cuts coarser (per probe, per hypothesis). **I re-cut it**: merged S1's things 7 and 36 into M14 + M55 by *what the answer is about* rather than by which section ruled; kept `workload`, `status` and `weight` separate (M53, M52, M47) because each has a distinct disposition and a distinct downstream consumer, and cross-referenced them through C35. That is a judgment and it is reversible.

**F. What the changelogs cover.** S2 found every live contradiction "**from the changelogs, not from suspicion**" across 54 entries in five files. S1 reports "Changelog: silent" as a positive finding on most things, across 11 entries in two files. **These are not different reading styles - they are different corpora.** "Check the changelog for the reasoning" works for `records/spec/` and fails for `records/domain/` before 08-25 (M65, C53).

**G. What is unfinished, reported only by S3.** `p3-announcement-recon/` is an **empty directory**. P2's pre-registered second stratum **never ran** and no file records a decision to abandon it. P4's per-course check on 2c03 and 2da4 is listed "still unverified" though the segment JSONs exist on disk. `per-course/*/graph.json` exists and `FINDINGS.md` never cites it. The rendered token count `derivation/TASK.md §4` asked for was never computed. **None of this is visible from fall26**, because the origin cycle's incompleteness did not travel with its conclusions.

## What I left dangling

**Files no survey read, and I did not open.** Every claim resting on one of these is reported as the citing record states it:

- **`fall26/records/plan/`** - `backlog.md` B19/B20/B27; `application-tier.md §7.1` (the unruled `obligation.course` immutability recommendation **the code already implements**); `write-rules.md` (the two-month-frozen mandate).
- **`fall26/records/archive/`** - `build-plan-2026-08-27.md` (the "plan of record", cited in `model.md`'s header with "**§9 first**"); `changelog-2026-08-24-slice-1.md` (`:241`, the `23:59` ruling's origin; §14.4, the recommendation that misled a reader).
- **`fall26/findings/read-cycle.md`** §4, §5 - the null result on the judgment-change test and the 24/17 and 29-of-77 faithfulness counts. **Load-bearing on E1**: the null result is what `ring-0.md §2` refuses, and the refusal is the container argument.
- **`fall26/evidence/`** - 30 files, 2,201 lines, reachable and unused. Includes `2026-08-27-tier-recut/derivations/L3-surface.md` and `2026-08-28-corpus/2c03/records.json`, the source of all four write rules.
- **The out-of-bounds openclaw trees** - `2026-08-23-slice-1/` (`FINDINGS.md`, `INCONSISTENCIES.md`, `NOTE-MECHANISM.md`, `E10R-RESULTS.md`, `OBSERVATION-SPACE.md`, `FAITHFULNESS.md`, `doubt/RECONCILE.md`, `CAVEATS.md`), `2026-08-24-slice-1-write/`, `2026-08-23-cost-probe/`. Six `[R]` rulings in `model.md` are promotions out of this tree.
- **`openclaw:fall26/2026-08-22-modeling/MODEL.md`** - superseded by `model.md`, which S1 read, so this is covered by succession rather than by reading.
- **Code** - `app/tests/boundary.test.ts`, `fall26/ingest.py`, the 12 `.ts` files and 62 tests. None read; none needed. `STATUS.md`'s B28/B29 (spec ran ahead of code twice, never reconciled) is the general form of C31.
- **S3's unread data** - `classification*.json` (~3,000 lines holding the individual `ephemeral` and `knowledge` instances that both TASKs said were "the finding, not the tally"), `SCORING-KEY.json` (the only record of which sealed name maps to which document, so no contamination claim is independently auditable), `graph.json`.

**Judgments I made that a later reader should be able to reverse.**

1. **The cluster cut.** Six clusters by *what kind of question the thing answers*. A cut by *slice* (what exists, what is slice 2, what is slice 3) would be equally defensible and would make the build sequence legible instead of the question structure. I chose the question structure because the next artifact is ADRs, not a build plan.
2. **`target_date` = `done_by`** (M46, C33) - inference, not record. Flagged in place.
3. **Splitting `workload` / `status` / `weight` into three things** rather than one obligation-field-set thing, against S1's own caveat. They share a downstream consumer (ring 0) and a common cause (the 08-24 grain deletion), so a single entry is arguable.
4. **Treating container drift as a mark rather than a cluster.** Cluster F holds things whose *whole content* is a container fact; `⟂container` marks appear on 31 things across the other five clusters. The alternative - one container register - would make E1 easier to act on and would scatter the domain content.
5. **Voiding S5's X1, X3 and X4 along with its citation audit.** X1 (file identity) is void on fact - the design of record was in scope. X3 and X4 derive entirely from the audit's readings of ruling 4 and of `PLAN.md`'s enumeration, both of which the zoom disproves. **X3's underlying substantive question** - does "locate details Billy himself does not know about" require the system to volunteer, against "the system declares nothing outward"? - I judged answered inside the corpus, by `domain-design.md §10.8` (it is a retrieval tuning, i.e. it happens *in an answer*) and `model.md §6` (it is a set-difference query, i.e. it is asked). Recorded at M5/C5. **If Billy thinks that is too quick, it belongs on the escalation list and it is not there.**

**One thing I did not do.** I did not re-derive any number. Every count in this file - 60 runs, 38% of faithfulness failures, 39% reduction, 5 of 55, 53 spec instances, 7 collapsed edges, 87-278 characters, 22 vs 14, 6 of 14, 0.27 ms - is reported as the record states it. Several of them rest on a fixture two rulings have set aside (C51) and one is qualified by its own record as "**not re-derived structurally**" (M2). A reader building on any single number should open the record that owns it first.
