# Classification pass - Cluster A, purpose and trust

**What this is.** A routing proposal for the twelve things in cluster A of `research/04-thing-inventory.md` (lines 57-193). Four destinations: `CONTEXT` (a glossary term), `ADR` (a decision), `DEFER` (a decision deliberately not made, carrying its wake-up condition), `DROP` (not carried, with a reason). **Nothing here is created.** No `CONTEXT.md`, no ADR file, no issue. Two sibling agents are routing clusters B-F in parallel and a reconciliation pass follows; every cross-cluster contact I can see is flagged, generously.

**Rulings applied.** Billy's nine rulings of 2026-08-29 are newer than the whole corpus and are applied per thing. Where a thing carries an ordering ("slice 1", "slice 2", "build only the slice whose dependencies are derived"), the ordering is dropped and the ruling kept, per fall26's own `CLAUDE.md`: there is no plan of record.

---

## M1. The goal function

**Destination: `ADR`**

**Proposed title.** The system's job is three jobs, and precise question-answering is not one of them.

**Test 1 - hard to reverse.** Yes. Both domain files say §2 "is now the judge of everything else"; reversing it re-opens every scope call the corpus ever made and every one it has not made yet.

**Test 2 - surprising without context.** Yes. A knowledge base built over course materials that deliberately declines to answer every question precisely, and that deliberately surfaces things the user did not ask for, reads as a defect to anyone who has not seen the diagnosis.

**Test 3 - a real trade-off.** Yes. The original goal function was reminders and deadline-tracking; Billy killed it on the observation that he is rarely behind, and the alternative that replaced it (collapse five interpretation reloads into one) was itself specified a day later into three jobs.

**Proposed body.** The product is not a reminder system and not an enterprise RAG that answers every question precisely: five concurrent courses produce a fear of not holding the whole picture, and it is *interpreting* a notice, not reading it, that forces a full context reload. The system's three jobs are to remove the anxiety of not finding information, to manage cross-course information in the background, and to locate details Billy does not know to ask about. For unfamiliar material the reload is first construction rather than recall, so helping model an assignment's requirements is in scope.

**Shape.** None. The three jobs are the shape.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 1 bounds it: v1's goal function operates over coursework inside academics, and the cross-domain reach of `domain-design.md §0.6` is deferred to v2 rather than dead. Ruling 6 sharpens job 3: what the RAG store holds is semantic, decontextualized facts about course materials, which is the test for whether an artifact is embedded at all. Ruling 2 adds that the work need not be a functional one-pass, so "collapsing the reload" does not mean the agent completes the reload silently.

**Open rider I could not close.** E7 asks which of the two forms a downstream ADR cites when it has to *reject* something. `model.md §1`'s anti-inflation test ("modelling that does not reduce reload cost is out of scope") is derived from the cost framing, while job 3 puts work that *increases* what Billy reads in scope by definition. None of the nine rulings settles this. I propose the ADR state the three jobs and **not** carry the anti-inflation test as a clause, so nothing cites a test that points two ways. If reconciliation wants the anti-inflation test, it needs a separate ruling from Billy, not an inherited sentence.

**Cross-cluster.** (a) Whoever holds `domain-design.md §0.6` and E6 owns ruling 1's v2 deferral; that deferral and this ADR must not both restate the scope boundary. (b) Anything in cluster E about what is ingested or embedded must defer to ruling 6, not to job 3's wording. (c) A `CONTEXT` term for **reload** (the full context reconstruction a person performs when interpreting one course notice) is worth having and belongs to whichever cluster ends up writing the glossary's core; I am not claiming it here because M1's destination is the ADR.

**Zoomed.** No. Correction 1 already zoomed `§10.7` ruling 4 verbatim and I checked E7's framing against it; nothing was ambiguous about what the thing IS.

---

## M2. The trust clause, and faithfulness as its operational form

**Destination: `CONTEXT`**

**Proposed term.** `faithfulness`

**Definition.** The system's promise about its own claims: every claim traces to a fact the system holds, no relevant held fact is omitted, and nothing is invented. It is a promise of complete recall over what the system was told, never of coverage of the world.

**`_Avoid_`.** "the trust clause" (names the promise's origin, not the promise), "verification" (the system does not verify the user; disagreeing with the user is conflict detection), "accuracy", "correctness", "precision and recall" (the corpus's own precision-versus-recall framing is voided in place by the record that used it).

**Why not an ADR.** The move from coverage-of-the-world to completeness-of-recall is a real decision, but its whole content is the definition of the word, and the *behavioural* half of the burden split (an over-broad question gets an over-broad answer, and that is not a defect) is carried by M3's ADR. Putting it in both places would duplicate one ruling across two artifacts.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 7 replaces the corpus's weak "not trusting the user is CONFLICT DETECTION, not verification" with a much stronger rule, and that rule is a decision in its own right that cluster A does not own (see cross-cluster). Ruling 9 bears on the untested half: the corpus records that the recall half of faithfulness was never loaded, and ruling 9 says an end-to-end run is unrunnable today and structure-only reading is rejected, so the real test is not merely unrun, it is currently unrunnable.

**Not carried with the term, and why.** The 08-23 measurement (60 runs, zero omissions, at a scale where omission was not possible) and the 38%-of-measured-failures figure behind the `null` convention are **exposition**: they are the argument, and the rulings they support live elsewhere (the `null` convention is a schema ruling, cluster C). The one residue worth keeping is the deferral in the next line.

**Cross-cluster, and this is the biggest one I have.** (a) **Ruling 7 needs an ADR that cluster A cannot write.** "Two conflicting statements must never coexist in the system"; shallow conflicts (two announcements colliding on a due date or a room) the agent may resolve itself but must report afterwards, never transparently; deeper conflicts (assignment spec or requirements, concepts, exam location or time) the agent must ask about before resolving. That is hard to reverse, surprising, and a real trade-off, and it belongs with write rules or the store invariants, cluster B or E. Whoever holds it should also absorb ruling 5: the risk is not sources disagreeing but the agent asking repeatedly or persisting noise, so the *detection* mechanism waits until it bites. (b) The untested-recall residue should become a **deferral issue owned by whichever cluster holds the hypothesis gate and evaluation** (ruling 9, E3), not a second deferral here. (c) `schema.md §1`'s `null` convention and `ring-0.md §6`'s conditional-weighting number are cluster C and D respectively and both cite faithfulness; they should cite this glossary term rather than re-deriving it.

**Zoomed.** Yes, incidentally: I read `domain-design.md` around §2 to confirm the recall-half caveat is stated in the body and travels with the claim. It does. Nothing changed.

---

## M3. Scope is not a defect, and the active window

**Destination: `ADR`**

**Proposed title.** Breadth is not a defect, and "active" is three independent triggers rather than a time window with exceptions.

**Test 1 - hard to reverse.** Partly, and this is the weakest of the three. The constants are cheap to change; the *shape* is not, because ring 0's contents and the whole "what counts as a failure" posture are downstream of it.

**Test 2 - surprising without context.** Yes. Two surprises: a system that answers a whole-semester question with a whole semester rather than helpfully narrowing, and an activity test where being in progress counts as much as being dated.

**Test 3 - a real trade-off.** Yes. The narrow window was available as a default narrowing from 08-23 and was deliberately *not* applied as one until Billy stated it as a requirement on 08-28; and `state == in_progress` was promoted from an exception inside the window to a trigger of its own, on the reasoning that working ahead of the dated window is being active.

**Proposed body.** A request for a whole semester that gets a whole semester is answering what was asked, so breadth is never treated as a failure to fix; the useful window is a requirement Billy stated, not a defect the system corrects on his behalf. Active is any one of three independent triggers on one question, so the partition is not a time window carrying exceptions.

**Shape, riding inside.** `active := due ∈ [today-7d, today+14d] OR done_by ∈ [today-7d, today+14d] OR state == in_progress`

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine directly. Ruling 3 is adjacent but distinct: it removes the calendar projection and `time_point` from the near term without touching this window, which is a residency band and not a calendar.

**Cross-cluster, and this is a hard collision.** The window is `ring-0.md §3`'s band A. **Cluster D almost certainly proposes the same ADR.** My recommendation to reconciliation: **cluster D owns the shape** (band A, the triple, the mechanism), and cluster A's contribution is the one clause D cannot see, that breadth is not a defect and the window is a stated requirement rather than a fix. Merge into one ADR, D's, with that clause in the body. Do not ship two. Also note C3 closes cleanly here: S1 found a changelog-only ruling with no body, S2 found the body, and there is nothing left to escalate.

**Zoomed.** No. The inventory quotes `ring-0.md §3` and its changelog verbatim on both halves and S2 recorded them as verified by zoom.

---

## M4. The system declares nothing outward

**Destination: `ADR`**

**Proposed title.** The system makes no assertions about its own completeness.

**Test 1 - hard to reverse.** Yes. Once a completeness or freshness assertion exists, readers rely on it, and withdrawing it later is a visible regression rather than a quiet cleanup.

**Test 2 - surprising without context.** Strongly yes. "5 of 5 obligations held, last synced 10 minutes ago" is the obvious thing to build, an agent did build it, and its absence is exactly what a future reader will ask about.

**Test 3 - a real trade-off.** Yes. The alternative was derived and rejected with a stated reason: the assertion would be one boring line nobody reads, and it can go stale and lie confidently, and a trust mechanism that can lie is net-negative. Trust accrues from being useful, not from self-reporting.

**Proposed body.** The system never asserts its own completeness or freshness; integrity work (closure, no coexisting contradictions) runs silently and is not reported as a status. Trust accrues from being useful, and a self-report that can go stale is worse than none because it lies confidently. This is not a rule against speaking: the agent still reports actions it took and still asks before it resolves anything deep.

**Shape.** None.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 7 narrows it, and the narrowing must be in the body or the ADR will be read as forbidding the reporting ruling 7 requires. Resolving a shallow conflict silently is forbidden and must be reported afterwards; a deep conflict must be asked about first. Neither is a completeness assertion, so both are compatible, but only if the ADR says what it prohibits precisely.

**`⟂container`, resolved rather than flagged.** The inventory flags that "declares nothing outward" is a statement about an app's user-facing surface, and that in a plugin the components *are* the agent's tool surface. I read the flag as resolving in favour of keeping the ruling, and more sharply: a tool that returns "5 of 5 held" to a coordinating agent is the rejected thing with a machine reader instead of a human one, and the staleness argument is unchanged. I am recording this as my reading, not as a ruling.

**Cross-cluster.** (a) `course.manifest`'s graveyarding on redundancy grounds (`schema.md §7`) is a **field ruling and belongs to cluster C**; C4's finding is that the field dies twice by two routes that do not cite each other, so C's graveyard entry and this ADR should cross-reference rather than each carry half. (b) "No coexisting contradictions" as a store invariant is ruling 7's territory and belongs with the conflict ADR I flagged under M2, not here; this ADR only says such work is silent. (c) Whoever owns the tool or CLI surface (cluster F) must not reintroduce a health or status verb.

**Zoomed.** No. The two rulings are quoted verbatim from `domain-design.md §1` ruling 10 and §7, and the openclaw origin gives the rejected artifact and the agent's own self-incriminating note.

---

## M5. The third job is a query, not a retrieval posture

**Destination: `ADR`**

**Proposed title.** Surfacing what Billy did not ask about is a deterministic set-difference query, not a recall-tuned retrieval.

**Test 1 - hard to reverse.** Yes. The two answers pull the whole design in different directions: a recall-tuned retrieval wants everything embedded and filtered at read time, a set-difference query wants the structure typed enough to subtract over.

**Test 2 - surprising without context.** Yes. "Locate details Billy does not know to ask about" reads as a retrieval-quality problem, and a reader will not expect to find it answered by an operation that walks one layer and returns nodes with no link of a given kind in a given direction.

**Test 3 - a real trade-off.** Yes. "Tune for recall, not precision" was the standing proposal and is self-declared "agent drafts, not ruled"; the query was specified, named and signed instead. The two are not mutually exclusive in principle, but only one was built.

**Proposed body.** The third job is served by subtraction over the graph, not by loosening retrieval: the query scans one layer and returns nodes that have no link of the named kind in the named direction. It means exactly that, and never "a node lacking a kind".

**Shape, riding inside.** `nodes_without(node_kind, link_kind, direction) -> [Node]`

**Sequencing stripped.** Yes. `design.md §3.4` and `architecture.md §7` assign this to "application tier, **slice 2**". I drop the slice. The tier assignment is an architecture claim, not sequencing, but it is not cluster A's to carry either, so I leave it to whoever owns the tier split.

**Touched by Billy's rulings.** Ruling 6, indirectly and importantly. The determinant for RAG inclusion is the nature of the store, semantic decontextualized facts about course materials. That makes the "tune for recall" posture even less attractive as an answer to job 3, since inclusion is now decided by a content test rather than by a recall appetite. It does not create a conflict: this query runs over the graph, not the RAG store.

**Cross-cluster.** (a) Ruling 6 answers E10 and belongs to whichever cluster owns RAG inclusion, probably E; that ADR and this one must be readable side by side without either claiming job 3 whole. (b) The tier and surface assignment is cluster F. (c) If cluster B proposes an ADR on link direction or on what a link kind means, this signature depends on it and should cite rather than restate. (d) M1's ADR states job 3; this one states how it is served. Reconciliation should keep them as two ADRs, not merge, because the mechanism is what is surprising.

**Zoomed.** No. The signature and the "never a node lacking a kind" gloss are quoted verbatim in the inventory from `design.md §3.4`.

---

## M6. Progressive disclosure, and expansion cost as the gate

**Destination: `ADR`**

**Proposed title.** The size gate is expansion cost, not total graph size.

**Test 1 - hard to reverse.** Yes. Every layering decision downstream (what is held, what is fetched, what one more level costs) is derived from this gate; changing it re-derives them.

**Test 2 - surprising without context.** Yes. A reader looking for the token-budget check against total nodes plus edges will not find one, and the earlier design had exactly that check.

**Test 3 - a real trade-off.** Yes. The earlier gate was total N + E against a fixed token budget; Billy replaced it on the reasoning that nothing ever requires rendering the whole graph, so total size is not the quantity under pressure.

**Proposed body.** Nothing ever renders the whole graph, so total size is the wrong quantity to budget: what must stay bounded is the cost of going one level deeper. Each level renders what is around it, and one level deeper is one more call.

**Shape.** None.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine directly. Ruling 8 is adjacent: query-by-time-period is explicitly not the skeleton's responsibility, which is a scope statement about the layer this gate governs, and the two should be consistent when both land.

**`⟂container`, and how I phrased around it.** The corpus states the gate with two container-bound premises: "only ring 0 is resident" and "nothing requires a CLI fetch". I propose the ADR carry **neither**. The gate survives both a resident coordinator and a per-invocation process, because the reason (nothing renders the whole graph) does not depend on what persists. Residency itself is E1 and unresolved by the nine rulings; leaving it out of this ADR is what lets this ADR stand while E1 is open.

**Cross-cluster, and I expect duplication here.** (a) Ring 0 residency (cluster D, E1) is the premise I stripped; if D's proposal restates residency as part of progressive disclosure, this ADR and D's must be reconciled so the gate does not inherit an open question. (b) The skeleton-versus-ring-0 split (cluster B, M13 and the two-layers thing) is the structure this gate produces; B may well propose "progressive disclosure" as its own ADR. **My recommendation: cluster A owns the gate (why expansion cost), cluster B or D owns the structure (what is resident, what is queried).** (c) "Progressive disclosure" is a general concept and must not enter `CONTEXT.md` as a term; only its project-specific gate is carryable, and that is a decision, not a definition.

**Zoomed.** No.

---

## M7. Proactivity and asking

**Destination: `DEFER`**

**What is deferred.** When the agent may speak or ask unprompted, and how often. The corpus holds two of Billy's own positions in tension: "no proactivity, no cron, no 24/7, Billy's own urge to check is the scheduler" (`domain-design.md §2`, 08-21) against "让系统从 waiting for input 变为 asking for input", the system asks at the read for facts with no generating event (`domain-design.md §9.6`, Billy, 08-23). That is E12.

**Precondition that wakes it.** Ruling 2 states it and it is testable: the system is roughly built (skeleton and ring 0 exist behind an exposed surface, so interaction rounds can actually be run), and a set of interaction rounds has been run and ask-frequency measured. The wake condition is met when there is a run log to count asks in. The ruling also states what the count means: if the agent must ask constantly, either something needs persisting or the design has a seam, and either finding is a design change rather than a tuning.

**Touched by Billy's rulings.** Rulings 2 and 4, decisively. Ruling 4 says proactivity is written too rigidly at present and will bite, and to design it when it is needed. Ruling 2 says the work need not be a functional one-pass: the agent sees the skeleton and ring 0, **notices**, and asks the user when needed rather than executing blindly, and puts ask-frequency in acceptance and evaluation rather than in the design. Ruling 4 also gives the one concrete piece that is already settled: `progress.state` defaults to `not_started` precisely so the agent does not keep asking how far along Billy is.

**Sequencing stripped.** None.

**What I dropped rather than deferred.** The "no cron, no 24/7" half. It is an artifact of the old container: a standalone repo run as an app with a long-running resident process is the only thing that could have had a cron. A Claude Code plugin has no daemon to schedule, so the ruling is moot rather than live, and carrying it would make a container fact look like a domain constraint. What survives from that sentence is not the prohibition but the observation, that the user's own urge to check is the trigger, and that observation is already inside M1's ADR as the diagnosis.

**Cross-cluster.** (a) `progress.state`'s non-nullable default and its stated reason are a **field ruling in cluster C**; ruling 4 supplies the reason, and C's entry should carry it rather than this deferral. (b) `architecture.md §3` consequence 3, "the system must not chase the agent", is quoted in the corpus from Billy about daily usage by a person and is cited as ground for two field-level rulings; that is E1's item 5 and belongs to cluster D or C. (c) Whoever owns evaluation and acceptance criteria should receive ask-frequency as a metric, since ruling 2 puts it there explicitly. (d) This deferral and the untested-recall deferral I flagged under M2 both wake on "the system is roughly built and runnable"; reconciliation may want them as one issue with two acceptance items, or as two issues citing a shared precondition, but should notice they are the same gate.

**Zoomed.** Yes. I read `domain-design.md` lines 169-171 and 585-605 to confirm both sides are Billy's own and that the 08-23 "asking" ruling is a promoted `[R]` with a three-row table, not an agent draft. It is. That is what moved this from a possible ADR ("no proactivity") to a deferral: the corpus does not hold one position here, it holds two of Billy's, and ruling 4 declines to pick today.

---

## M8. "Sync" is the wrong model

**Destination: `ADR`**

**Proposed title.** The store accumulates; it is never synchronised against a source.

**Test 1 - hard to reverse.** Yes. Diffing and mirror state are load-bearing once built, and their absence is equally load-bearing: nothing in the design maintains a correspondence to re-establish.

**Test 2 - surprising without context.** Strongly yes. A reader will ask why the system does not re-read the course site and reconcile, which is what every integration they have seen does.

**Test 3 - a real trade-off.** Yes. Sync was the working model and Billy killed it, and three concrete mechanisms died with it: full re-reads, diffing, and mirror state.

**Proposed body.** This is not a system kept aligned with a remote, it is a knowledge base that accumulates: things enter, stale or wrong things leave, and everything is classifiable and queryable. There is no full re-read, no diff against a source, and no mirror state, because there is no correspondence to maintain.

**Shape.** None.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 7 constrains what "accumulates" is allowed to mean, and the two must be read together: accumulation is not permission for two conflicting statements to sit side by side, because ruling 7 forbids exactly that. Ruling 5 says the detection mechanism waits until it bites, which is what keeps the two compatible in practice today.

**Cross-cluster, and this one is load-bearing for another cluster's ADR.** (a) The corpus layer's write mode, "append + supersede only" (`domain-design.md §3`), is **cluster B's**, and C16 records that `supersedes` was cut on zero measured instances with read-time expiry beating write-time supersession about 7:1. Whoever writes that ADR is describing the same decision from the store side; this ADR is the purpose side. They should be reconciled and may want to be one. (b) Ingestion and write rules (cluster E) inherit "no full re-read" directly. (c) Ruling 7's conflict ADR, flagged under M2, is the constraint on accumulation and should cite this one.

**Zoomed.** No. The openclaw form and the imported form are both quoted and agree; the openclaw form additionally names the three killed mechanisms, which is what makes the ADR concrete.

---

## M9. The two observed failure modes

**Destination: `DROP`**

**Which kind.** **Exposition.** These are the observations that ground rulings, not rulings. (a) The thread graph records at too fine a grain, which grounds "pointers and summaries, never content" and non-sedimentation. (b) A coordinator that pulls in-depth information about one course cannot hold every course's every topic, so its weighting judgment gets polluted by whichever slice it happens to have, and visible work masquerades as important work. (b) is the direct ancestor of the symmetry rule and of uniform-depth projection.

**Why drop, with the qualification that matters.** The rulings land elsewhere and this is their argument. But (b) is the rare argument an ADR genuinely needs: "uniform depth across all courses" is not obviously right, and without the observation a future reader will read it as needless rigidity and relax it. So this is a drop **conditional on the argument riding elsewhere**, and I am flagging it rather than assuming it.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine.

**Cross-cluster, and this is the flag I most want read.** **Cluster D cannot see this thing.** Failure mode (b) must ride as the one-clause rationale inside D's uniform-depth or symmetry ADR (the inventory points at M69), in roughly this form: asymmetric depth biases allocation, so visible work masquerades as important work. Failure mode (a) is the rationale for non-sedimentation, also cluster D. Both are drawn from watching a live system (Fairy), not from introspection, which is worth one clause because it is the corpus's only requirement grounded in a running system's observed behaviour rather than in course material. If D's proposals carry those rationales, this drop is clean. If they do not, reconciliation should push the clauses in rather than resurrect this entry.

**Zoomed.** No.

---

## M10. The schema must not be over-determined

**Destination: `ADR`**

**Proposed title.** Under-model deliberately: the relationships cannot be written today.

**Test 1 - hard to reverse.** Asymmetrically yes, and the asymmetry is the point. Under-modelling is cheap to walk back one field at a time; over-modelling is not, because a written-down relationship acquires readers and a vocabulary before anyone checks whether it was real.

**Test 2 - surprising without context.** Yes. A schema with a small typed core, a fifteen-entry graveyard, and an explicit "do not re-add without a new ruling" looks like an unfinished schema rather than a decided one.

**Test 3 - a real trade-off.** Yes. Completing the model was available, was named as satisfying, and was rejected as mostly wrong. It was applied against five candidate edge kinds with one sighting each and against a general form of conditional weighting, both rejected as over-built for the evidence in hand.

**Proposed body.** The cases cannot be enumerated today and the relationships cannot be written out today, so the design is a tiny mechanical core plus everything else free, which is not vagueness everywhere. Completing the model is satisfying and mostly wrong; a thing enters the typed core when evidence and a reader for it exist, and a graveyarded thing does not come back without a new ruling.

**Shape.** None. The `/promote` gate and the rigidity rule are the mechanisms and are not cluster A's (see cross-cluster).

**Sequencing stripped.** Yes, one. `design.md §4`'s "build only the slice whose dependencies are derived" is an ordering rule wearing a posture's clothes. I keep the posture and drop the ordering; what to build next is the wayfinder session's output, not an inheritance.

**Touched by Billy's rulings.** Ruling 5 is this posture applied to conflict detection: wait until the mechanism bites rather than building for a risk that has not shown up. Ruling 9 is the same posture applied to the hypothesis gate: the instrument cannot reflect the ideal case yet, so the result would be untrustworthy and the gate is deferred rather than run in a degraded form. Ruling 3 is it applied to the plan: a real requirement that is not settleable before the schema, API and CLI shape settle. Three of the nine are this posture in action, which is the strongest argument for carrying it as a standing decision rather than as method.

**The tension I am not hiding.** The literal 08-21 conclusion, "you cannot write the relationships today", is one of only two verbatim Billy fragments in that log, and eleven typed edges were written the next day. The posture survives that; the literal claim does not. The ADR I propose states the posture and does not quote the literal claim as a rule.

**Cross-cluster, and high collision risk.** (a) The **rigidity rule** ("a field earns `typed` if and only if some mechanism reads it") is the mechanism this posture produces and is **cluster C's**, along with its two Billy-ruled exemptions, `grade_share` and `added_at` (C19). If C proposes an ADR for the rigidity rule, **merge**: one ADR with the posture as the reason and the rule plus its exemptions as the shape, rather than two that each hold half. (b) The graveyard itself and its "do not re-add" clause are cluster C. (c) The `/promote` gate is cluster B or C. (d) `model.md §8`'s watch list of five edges is cluster B, and C15 notes those edges are mischaracterised in their own source (9, 6 and 3 instances filed under "one sighting each"), which is a correction B needs and cannot see from here.

**Zoomed.** No. The five citations across four records agree and the disagreement (the literal claim versus the next-day edge table) is already registered at C24.

---

## M11. Disposability as the acceptance criterion

**Destination: `DROP`**

**Which kind.** **Agent draft never ruled.** `domain-design.md §9`'s header names §9.0 and §9.3-9.5 agent drafts, and §9.5 is disposability. This is stronger than "nobody got around to promoting it": on 2026-08-23 Billy went through this exact section after an adversarial review and promoted **§9.1 and §9.2 only**, recording why and saying it was marked "so it need not be asked again". A ruling pass that touched the neighbours and left §9.5 as a draft is a decision about §9.5.

**Why this matters and why it is still a drop.** Two later records treat it as binding anyway: `PLAN.md` lists it under "settled, do not re-litigate" and `ring-0.md §1` derives a number from it (losing the coordinator costs one projection read, therefore ring 0's size bound is roughly 55 obligations at five courses). That is C6, verdict "needs Billy", low weight. Merge rule 3 says a self-declared draft stays a draft, and I am applying it.

**Two things I want on the record against my own call.** First, the content is not container-dead. "If losing the session loses information, the design is wrong" translates cleanly into a plugin, where the agent's context is compacted, cleared and resumed, and it reads as: nothing of value may live only in the conversation. Second, that is a general engineering principle rather than a project-specific decision, and it fails the ADR "surprising" test on exactly that ground. So it is dropped as an unruled draft whose content is general, not as a container artifact. **This is my least confident call in the cluster.**

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine. E1, which C6 is folded into, is untouched by the 08-29 rulings and remains open.

**Cross-cluster, and cluster D must see this.** Ring 0's size bound cites disposability as its ground. If cluster D carries the size bound, **it carries a number whose stated derivation I am dropping**, and D should either re-ground it or carry it as a measured bound rather than a derived one. Separately, E1 (does the coordinator's residency survive the container change) is the largest open escalation in the corpus, it blocks the whole observation contract, and none of the nine rulings touches it: **cluster D should be proposing a deferral for E1**, and if it does, this thing's residue belongs inside that deferral rather than as its own entry.

**Zoomed.** Yes, and it changed the call. I read `domain-design.md` §9's header and the 08-23 `[R]` block directly. The header alone would have supported "unpromoted draft"; the 08-23 block, which promotes the two neighbours by name and explains why the omission mattered, is what makes the draft standing deliberate rather than accidental.

---

## M12. Agents draft and never self-lock

**Destination: `DROP`**

**Which kind.** **Artifact of the old container.** The `[R]` marker system, the drafts-versus-rulings header convention, `BLOCKED beats guessing`, and the demote-to-the-level-the-evidence-supports move are the working discipline of a records-based standalone repo with a document taxonomy. This repo's discipline is written elsewhere and differently: GitHub issues driven through `gh`, five canonical triage labels, a single `CONTEXT.md` and `docs/adr/`. `BRIEF.md` is explicit that inventing a document taxonomy is the failure mode that killed the last two attempts.

**What is not lost, and why it still does not become one of the four.** The practice itself is good and this repo keeps it, in `CLAUDE.md` and `docs/agents/`. That is a working-discipline location, not a domain artifact, so "not carried" here means "not carried into `CONTEXT.md`, an ADR, or a deferral", not "abandoned". I am stating that explicitly because a bare DROP would read as discarding the one discipline that makes the corpus readable at all.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 2 is the product-side analogue and should not be confused with this: the *runtime* agent notices and asks rather than executing blindly. That is a design requirement about the shipped system, and it is carried by M7's deferral. This thing is about the *design-time* agent and its records, which is a different agent doing a different job.

**Cross-cluster.** (a) If any cluster proposes carrying the `[R]` convention or a drafts-versus-rulings marker into this repo's artifacts, it collides with this drop and with `BRIEF.md`; flag it rather than accommodate it. (b) The observation that this is the corpus's most-violated rule (three same-day violations in one file, three self-corrections found by outside readers) is the reason merge rule 3 was needed at all, and it is worth one sentence in whatever document explains how the corpus was mined. That document is research output, not a destination on this list.

**Zoomed.** No.

---

## Summary

**Counts.**

| destination | count | things |
|---|---|---|
| `CONTEXT` | 1 | M2 |
| `ADR` | 7 | M1, M3, M4, M5, M6, M8, M10 |
| `DEFER` | 1 | M7 |
| `DROP` | 3 | M9, M11, M12 |

**Least certain, in order.**

1. **M11 (disposability), dropped as an unruled agent draft.** The zoom hardened the draft standing, but the content translates cleanly into the new container and two later records rely on it, one of them numerically. If reconciliation disagrees, the right correction is not to make it an ADR (it fails the surprising test as a general principle) but to fold it into cluster D's E1 deferral.
2. **M3 (the active window), routed to ADR knowing cluster D holds the same thing.** I expect a duplicate. My proposal is that D owns the shape and A contributes one clause; if reconciliation prefers, A can drop this entirely with the "breadth is not a defect" clause pushed into D's body.
3. **M2 (faithfulness), routed to CONTEXT rather than ADR.** The burden split is a real decision, and I put its behavioural half in M3's ADR and its definitional half in the glossary. If M3 merges into cluster D's ring-0 ADR, that behavioural half could get lost in the merge, and M2 may then need to become an ADR after all. Worth checking after D's proposal lands.
4. **M10 (under-modelling), routed to ADR at high collision risk with cluster C's rigidity rule.** I would rather see one merged ADR than my version standing alone.

**Every cross-cluster flag, gathered.**

1. **Ruling 7 has no owner in cluster A and needs an ADR.** Two conflicting statements must never coexist; shallow conflicts (due date, room) the agent resolves but must report afterwards, never transparently; deep conflicts (assignment spec or requirements, concepts, exam location or time) the agent must ask about before resolving. Cluster B or E, whichever holds write rules and store invariants. Ruling 5 (wait until the mechanism bites) belongs with it. Touches M2, M4 and M8 from here.
2. **M3 duplicates cluster D's band A.** Recommend one ADR, D's, with A's "breadth is not a defect" clause in the body.
3. **M6 may duplicate cluster B's or D's progressive-disclosure entry.** Recommend A owns the gate (expansion cost, not total size) and B or D owns the structure. I stripped the residency premise deliberately so the gate does not inherit E1.
4. **M9 is dropped on the condition that cluster D carries its rationale.** Failure mode (b), asymmetric depth pollutes weighting and visible work masquerades as important work, must ride inside D's uniform-depth or symmetry ADR. Failure mode (a) grounds non-sedimentation, also D.
5. **M11's drop removes the stated ground for ring 0's ~55-obligation size bound.** Cluster D must re-ground or re-label that number.
6. **E1 has no owner that I can see and none of the nine rulings touches it.** Cluster D should be proposing a deferral for whether anything persists between reads in the plugin container. Several cluster A things lean on it and I phrased around it in every case.
7. **M10 collides with cluster C's rigidity rule and its two Billy-ruled exemptions (`grade_share`, `added_at`).** Recommend merging into one ADR: A's posture as the reason, C's rule and exemptions as the shape. The graveyard and `/promote` are C's and B's.
8. **`course.manifest` (M4) is a field ruling and is cluster C's.** C4 records that it dies twice by two routes that do not cite each other; C's entry and A's ADR should cross-reference.
9. **`progress.state`'s non-nullable `not_started` default (M7) is cluster C's, and ruling 4 supplies its reason.**
10. **Ruling 6 (RAG inclusion is decided by the nature of the store: semantic decontextualized facts about course materials) answers E10 and belongs to cluster E.** It touches M1's job 3 and M5; none of the three should claim job 3 whole.
11. **Ruling 1's v2 deferral of `domain-design.md §0.6`'s cross-domain requirement** belongs wherever §0.6 lives (E6). It bounds M1's ADR and must not be restated in two places.
12. **Ask-frequency (M7) is an acceptance and evaluation item per ruling 2**, and belongs to whoever owns evaluation. It shares a wake-up gate with the untested-recall deferral flagged under M2; those two may be one issue.
13. **The untested recall half of faithfulness (M2)** should become a deferral owned by whoever holds the hypothesis gate and E3, under ruling 9.
14. **The `supersedes` cut and "append + supersede" corpus write mode (C16) is cluster B's** and is the store-side face of M8's ADR. Possibly one ADR.
15. **`nodes_without`'s tier assignment (M5) is cluster F's**; I dropped only the slice, not the tier.
16. **C15's mischaracterisation of the watch-listed edges** (9, 6 and 3 instances filed under "one sighting each") is a correction cluster B needs and cannot see from M10.
17. **A `CONTEXT` term for `reload`** is worth having and is not claimed here; whoever writes the glossary's core should take it.
18. **Nothing in this repo should reintroduce the `[R]` marker convention** (M12); it collides with `BRIEF.md`'s warning about inventing a document taxonomy.
