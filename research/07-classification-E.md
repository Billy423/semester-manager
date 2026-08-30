# Classification pass - Cluster E: inbound (ingestion, announcements, operations, capture), M81-M96

**Proposals only.** Nothing here is created. Sibling passes are running on other clusters and a reconciliation follows. Terms are classified against cluster B's list; where I think B is wrong I say so under the thing.

**What I zoomed.** `domain-design.md` §4, §9.6, §10.3-10.9 in full · `model.md` §7.2, §9, §10 in full · `write-rules.md` in full including its changelog · `schema.md` §4, §4.5, §4.6 · `architecture.md` §3, §4 · `design.md` §1, §3.6, §5, §7 · `step-minus-1/FINDINGS.md` P2 and P6 · `p5-induction/TASK.md`, `p6-channel-or-knowledge/TASK.md` · `derivation/FINDINGS.md` H3, §4, §5 · `derivation/TASK.md` §2-§3 · `derivation/agents/2c03-concepts-weeks-1-6.md`, `2aa4-tutorials-assignments-artifacts.md` · `openclaw:log/2026-08-21` reversals and capture-point sections · `2026-08-22-modeling/PLAN.md` §Open. Five entries changed as a result and are marked **zoomed: changed**.

**The two rulings that overturn this cluster.** Ruling 6 kills the source-class rule and the linearization axis as inclusion criteria; §`What ruling 6 overturns` lists every record in this cluster that stated either and what survives of each. Ruling 7 answers a question open in this cluster since 2026-08-21; §`Where ruling 7 anchors` proposes its home.

---

## M81. Ingestion is out of scope; Billy is the fetcher

**Destination: `ADR`**

**Proposed title.** The system does not fetch; the boundary starts at the endpoint, and the endpoint is multimodal.

**Tests.**

- *Hard to reverse* - **yes.** Reversing it re-opens the branch that was actually built and then retired over two rounds (source registries, coverage guarantees, scraping), and it moves the trust requirement back from *completeness of recall* (mechanical, measurable) to *coverage of the world* (unsolvable). Every trust claim the system makes rests on which side of that line it sits.
- *Surprising without context* - **yes.** A course knowledge base that cannot reach the course portal reads as an unfinished feature rather than a decision, and "the endpoint is multimodal from day one" is surprising in a system with no fetcher: the reason is that the delivery act is a paste, and a paste is often an image.
- *Real trade-off* - **yes.** Coverage guarantees were the alternative and were built before being retired. The cost taken is real: the system can never assert that it holds everything, only that it holds everything it was given.

**Body.** The system does not fetch anything. The user delivers material and the boundary starts at the endpoint, which moves the trust requirement from coverage of the world to completeness of recall over what it was given. Because delivery is a paste, the endpoint is multimodal from the first version rather than text-first, and it records the source's **publication** time and not its arrival time - three notices dropped in on a Sunday in the wrong order would otherwise let an older fact silently overwrite a newer one.

**Sequencing stripped.** `design.md §1`'s framing of F1 as "slice 1's write side" is dropped; the requirement is that a pasted screenshot produces facts that land, not that it is first.

**Touched by Billy's rulings.** Ruling 9 - who does onboarding and how information arrives is now an explicit open question, and it sits directly on top of this ADR: this ADR fixes *where* the boundary is, and leaves entirely open *who carries material across it* in the successor container. That open question is M95's and M84's, not this ADR's, and this ADR should not be read as answering it.

**Merge candidates.** M88, on one clause only: "the pasted portal screenshot is the primary deadline path, not an enrichment of it" is a consequence of M88's measurement and a property of this ADR's endpoint. Recommend M81 states the boundary, M88 states the dependency, one cross-reference, no merge.

**Cross-cluster.** (a) **The `ingestion` word collision (B's M34, C64) resolves by deletion, not by coining** - see `## Terms proposed`. (b) The multimodal-endpoint clause is the premise of B's M37/M38 (`text_extractable`, detection of empty extraction). (c) `⟂container`: "read by the session itself, no API call" is old-container phrasing that survives repaired - in the successor the agent is the reader, which makes the multimodal clause easier, not harder.

**Zoomed.** Yes, `openclaw:log/2026-08-21` reversals item 3 and `domain-design.md §4`'s timestamps paragraph. Unchanged: both hold exactly as the inventory records them.

---

## M82. The operations model (file it / apply it) - dead, and its counter-argument

**Destination: `DROP`**

**Reason: a model falsified by measurement, plus exposition.** 53 of 137 operations reduce, 76 do not; the deadline move that the whole routing design was built around happened once in a semester; 21 of 22 executed rewrites were additive free-text appends. This is not a container casualty and it is not repairable - the insert-versus-rewrite axis had no correct branch for 55% of real announcements. Its replacement ruling is M83's and is already an ADR.

**The three live residues, and where each goes, because dropping the thing must not drop them.**

1. **The falsification itself** rides inside M83's ADR as its ground. Without it, "inbound arrives to be known" reads as a preference rather than as the thing that dissolved a measured 55% failure.
2. **The counter-argument** - that storing-and-tagging leaves "due Wednesday" and "moved to Friday" coexisting for a reader to reconcile, which *"relocates Billy's uncertainty into the system while making it look handled"* - **is now answered by ruling 7 and goes to M85's ADR.** It has been flagged open by two independent documents since 2026-08-21, named "the entry point for the next design round", and untouched by six days of spec work. It is closed, and the objection is upheld.
3. **The p5 method** - *"answer in the announcement's own terms first, without reference to the schema; reversing that order fits the data to the schema"* - is a research-method ruling, not a domain one. It belongs with C91 (cluster F's method thread), not here. Flagged, not carried.

**Also dropped.** The `~30 confirmations/semester` figure and its `~115` / `1-2 per course` corrections, all of which measure a rewrite regime that no longer exists. **Zoom correction to the inventory:** §4 carries an `⚠️ SUPERSEDED` banner at the top pointing at §10.3-10.4, so the ~30 figure is not "standing uncorrected in place" - it is inside a section marked dead. The inventory over-reads this as a live hazard.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 7 closes residue 2. Ruling 5 bears on the drop itself: the operations model was an apparatus for handling conflicts that were assumed frequent, and ruling 5 says the real risk is the opposite - an agent that finds small conflicts and asks about them repeatedly. Dropping the apparatus is consistent with waiting until the mechanism bites.

**Merge candidates.** M83 - not a merge candidate but a *relocation target*; the two are one decision seen from its two sides.

**Cross-cluster.** B's M23 (`supersedes` cut) is the schema-side face of this drop: the operations model is what `supersedes` existed for, and read-time expiry beat write-time supersession roughly 7:1. Recommend B's graveyard entry cite this drop as its ground.

**Zoomed.** Yes, `domain-design.md §4` and §10.3, `p5-induction/TASK.md`, `PLAN.md` §Open item 4. **Changed:** the inventory's "the earlier figure stands uncorrected in the same file" is wrong, per the banner above.

---

## M83. Inbound is to be known, not to trigger an action

**Destination: `ADR`**

**Proposed title.** Inbound arrives to be known, not to trigger an action.

**Tests.**

- *Hard to reverse* - **yes.** It decides that the endpoint produces knowledge rather than operations, which fixes the size and the job of the typed layer and therefore the whole write side. Reversing it means re-deriving what every kind of inbound is *for*.
- *Surprising without context* - **yes.** An intake that executes nothing for most of what arrives reads as an intake that dropped the input. The record's own defence is the surprising part: a room change, a section-scoped notice, a pointer to a portal path, an accumulating strike count did not need the system to *do* anything, and the model that forced them into a binary recorded their refusal as a failure of the material rather than of the model.
- *Real trade-off* - **yes, and the cost is stated by the record itself.** The reframe walks deliberately into the failure mode the earlier record named: everything lands in free text and the knowledge base degrades into a note pile. The only thing separating the two is that the small typed layer stays populated.

**Body.** Inbound does not arrive to trigger an action; it arrives to be known. The job is that when the user asks what a week was about, the system holds the surrounding context from announcements, slides and anywhere else - not that it executes one operation per input, which is the model that had no correct branch for 55% of real announcements. The cost is taken knowingly: this is one step from a note pile, and the only thing that keeps it a designed knowledge base is that the small typed layer stays populated.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** **Ruling 6** supplies what "known" means on the store side - semantic, decontextualized facts about course materials - and therefore says what does *not* enter the store merely because it arrived. **Ruling 7 bounds this ADR and must be cited inside it**: "to be known" is not "coexisting contradictions are acceptable". The reframe's stated risk (a note pile) and ruling 7's invariant (two conflicting statements never coexist) are the same worry from two directions, and ruling 7 is the first hard limit anyone has put on the reframe.

**Merge candidates.** M82 - one decision, two sides; M82's falsification is this ADR's ground. Not a merge with M85: M85 is what happens when two things collide, this is what happens when one thing arrives.

**Cross-cluster.** (a) B's M24 flags announcements-as-intake to me; taken. (b) **B's M24 also reports that `model.md §8` and `§9` mis-cite `§10.6` - confirmed at source, and the mis-citation matters more than B could see from its side.** `§10.6` is the *finding* that announcements are a channel **with one seam**, measured at 5/55 and 6/38 knowledge after redundancy, with the bias pre-registered *toward* knowledge so the number is a floor. `model.md §9` paraphrases it as the flat proposition "announcements are a delivery channel", which is the proposition that **failed in both courses**. Anything carrying that paraphrase forward carries a falsified claim. The correct one-line statement is: *announcements are mostly a channel, and the 9-16% that is not is almost always a correction against material already held.* (c) A's flag 10 (ruling 6 belongs to cluster E) - taken at M91.

**Zoomed.** Yes, `domain-design.md §10.4`, §10.5, §10.6, §10.7 ruling 1. **Changed:** the mis-citation in (c) above is verified at source, and §10.6's own numbers are what falsify the paraphrase.

---

## M84. Confirmation policy

**Destination: `DEFER`**

**What is deferred.** How often the system asks or confirms before writing, and in what form the ask is presented.

**Precondition that wakes it.** Ruling 2 states it: the system is roughly built (a surface exists, interaction rounds can be run) and ask-frequency has been measured over real rounds. Ruling 2 also says what the count means - if the agent must ask constantly, either something needs persisting or the design has a seam - so the wake condition is a run log to count asks in, not a design argument.

**What must travel with the deferral or it is lost.**

- **The shape of an ask is settled even though its frequency is not**: *"the hard part of a rewrite is not the confirmation, it is resolving the target"* - "the deadline moved to Friday" names none of a course's three assignments - so a confirmation presents the **resolved target** ("changing assignment 3's due from Wed to Fri"), never a yes/no. This clause is live, it is what ruling 7's "ask to clarify or confirm" and "report afterwards" both need in order to be executable, and **it should ride inside M85's ADR rather than sit in a deferral where it will not be read.**
- **The stratification axis has changed and the old one has no carrier.** `§4` stratified by *operation* - filing automatic, rewriting asks - and the operation axis died with the operations model (M82). Ruling 7 restratifies by **conflict depth**. Nothing should carry forward the filing/rewriting split.

**What is dropped inside this deferral.**

- **The dev-time confirmation toggle and its N = 5 exit.** `⟂container` - "during development" is a mode of the old app's own build cycle, and the exit condition is a self-declared agent addition with the number "explicitly flagged as arbitrary; there is no evidence behind the number". The mechanism it reads (`Diff`) survives and is B's/F's.
- **Every confirmation count** - ~30, ~115, 1-2 per course. See M82.

**Sequencing stripped.** `architecture.md §7` removes `land()` from the first build and re-homes the `Diff` conflict question to the presentation tier. The tier assignment is kept; "not in the first build" is dropped.

**Touched by Billy's rulings.** Ruling 2 supplies the precondition. Ruling 7 supplies the policy this deferral no longer has to invent. Ruling 4 says proactivity is written too rigidly now and will bite, which is why this stays deferred rather than being written today.

**Merge candidates.** **Strong: cluster A's M7 (proactivity and asking) and my M95 (the capture point).** All three defer a different face of the same question and all three wake on the same gate. Recommend reconciliation make them **one deferral issue with three acceptance items** - unprompted speech (A/M7), confirmation before a write (M84), asking at the read for a fact with no generating event (M95) - rather than three issues that will be closed independently and inconsistently.

**Cross-cluster.** `architecture.md §3` consequence 3 ("the system must not chase the agent") is cited here but is **cluster F's M98 / cluster C's field-level uses**; this deferral cites it and must not restate it. B's M19 flags "surface for confirmation, never resolve" at M84 - **redirect: that phrase's home in this cluster is M85, not M84.**

**Zoomed.** Yes, `domain-design.md §4` and §10.3, `model.md §8.1`, `design.md §3.6`, `architecture.md §3`.

---

## M85. Conflict detection: "you told me this, the record says that"

**Destination: `ADR`** - and **this is where I anchor ruling 7.**

**Proposed title.** Two conflicting statements never coexist, and how a conflict closes depends on what is in conflict.

**Tests.**

- *Hard to reverse* - **yes.** It is an invariant over what the store may ever hold. The landing operation is built against it (landing detects conflicts instead of overwriting, and its return type carries a `CONFLICT` outcome), and every read is written assuming it holds. Reversing it means every reader must reconcile, which is exactly the design this rejects.
- *Surprising without context* - **yes, twice.** First, the owner is the authority on his own state and the system still refuses to take his word against a held record. Second, an agent that *may* resolve a conflict itself is nevertheless forbidden to do so silently - reporting afterwards is mandatory, not courtesy.
- *Real trade-off* - **yes, and it is the corpus's longest-running one.** The rejected alternative is store-and-tag with read-time reconciliation, argued for on the ground that it fails only for an unbounded pile and holds for a scoped, time-ordered set. That argument was never answered in six days of spec work; ruling 7 rejects it, and the original objection - that read-time reconciliation relocates the user's uncertainty into the system while making it look handled - is what it is rejected on.

**Body.** Two conflicting statements never coexist in the system: landing detects a conflict instead of overwriting, and a conflict is closed at write time rather than left for a reader to reconcile. How it closes depends on what is in conflict - a shallow collision the agent may resolve itself, because the user delivered the material deliberately, but it must report the resolution afterwards and never resolve transparently; a deeper one it must put to the user before resolving. The owner's own claim is not exempt: it is surfaced against the held record - *"you told me this, the record says that, which holds"* - because being the authority on a fact is not the same as being right about what the system currently holds.

**Shape riding inside** (it encodes the policy more precisely than prose, and the examples are Billy's own):

| depth | what is in conflict | how it closes |
|---|---|---|
| **shallow** | a due date · a room | the agent resolves it, **then reports the resolution**. Never silently |
| **deep** | an assignment's spec or requirements · a concept · an exam's time or place | the agent **asks the user to clarify or confirm before resolving** |

**A requirement this places on the field set, which nothing currently states:** the system must carry the fields needed to tell the two apart at write time. Depth is not a property of the announcement, it is a property of what the announcement collides with, so the discriminator lives on the record, not in the prompt. That is a cross-cluster obligation on C.

**Three distinctions that must survive the merge, because a careless reading of ruling 7 corrupts each of them.**

1. **`write-rules.md §5` and `schema.md §4.5`'s *"only the owner authors it, so an agent may surface a progress claim and never resolve one"* is an authorship rule, not a conflict rule.** Ruling 7 does not license an agent to resolve a progress claim. Progress is never a shallow conflict; it is not a conflict class at all.
2. **`schema.md §4`'s maintenance-at-read rule already has ruling 7's two-tier shape in miniature and is missing its second half.** At source: *a target revised later than the note is evidenced staleness the agent may act on in passing, while anything else may be surfaced for confirmation and never resolved.* That is shallow-versus-deep by another name - but "act on in passing" carries **no report obligation**, and ruling 7 forbids exactly that. The §4 rule needs the report clause added; it is the one place in the corpus where an agent is currently authorised to resolve something transparently.
3. **Ruling 7 governs conflicts the system *meets*; it is not a mandate to hunt for them.** Ruling 5 is the governor on the other side - the real risk is an agent finding small conflicts and asking repeatedly, or persisting one as noise that colours every later read. The two reconcile cleanly and the reconciliation should be stated in the ADR, or ruling 7 will be read as an instruction to build a detector (see M90).

**Sequencing stripped.** F2's framing as a slice-1 acceptance requirement, and `architecture.md §7`'s "not in the first build" for `land()`. The tier assignment (adjudication is presentation) is kept.

**Touched by Billy's rulings.** Ruling 7 in full. Ruling 5 as its governor. Ruling 2, indirectly and importantly: ruling 7's deep tier routes load onto asking, and ruling 2 says nothing measures ask-frequency yet.

**Merge candidates.** **M96, on a real shared trade-off and I recommend against merging.** "An asked answer persists, stated prominently, so an agent cannot read a historical answer as a current fact" (Billy, 08-23) and "never resolve transparently, report afterwards" (Billy, 08-29) are the same rule about two different acts: the system may act or store, but never invisibly, because the harm was always silent influence and never the act. Six days apart, neither citing the other. Merging them would bury ruling 7's two-tier table inside a principle; recommend two ADRs that cite each other and name the shared principle in one line.

**Cross-cluster.** (a) **Cluster A's flag 1 is answered here** - ruling 7 has a home. (b) **B's M23 flag is taken**: the resolve-and-report / ask-first split is this cluster's write rule, and `supersedes` belongs in the graveyard (its justification was the operations model, M82). (c) The field-set requirement above is C's. (d) `Diff` and its `CONFLICT` outcome are the mechanism and are B's/F's; this ADR names the policy, not the return type. (e) The orphan `write-rules.md §1.1` (see `## Orphan rulings`) is this ADR's already-written field-level instance and should be adopted into it.

**Zoomed.** Yes, `model.md §8.1`, `domain-design.md §4`, `schema.md §4` and §4.5, `write-rules.md §5`, `design.md §1` F2 and §3.6, `step-minus-1/FINDINGS.md` P2 sub-question 2. **Changed:** distinction 2 above - the two-tier rule already exists in `schema.md §4` and no survey or inventory entry records it. That is what made M85 rather than M82 the right anchor.

---

## M86. Always keep, judge only linkage

**Destination: `DEFER`**

**What is deferred.** Whether raw inbound text is retained beyond what becomes a typed row, a note, or a store entry - and if it is, against what.

**Precondition that wakes it.** Ruling 5 gives it: wait until the mechanism bites. Concretely, either (a) a discarded correction is observed to have left the corpus quietly wrong - the asymmetry's failure mode actually occurring rather than being argued about, or (b) the class of source ruling 5 names enters the system: Billy's own products, a running assignment, sources for work in progress, leftovers from an engineering project. Ruling 5 says that class is **not in the system yet** and will probably enter in its own session, and it is the class where retaining the raw text is most likely to pay.

**What must travel.**

- **The asymmetry, which is the only part nothing has answered**: wrongly discarding a correction leaves the corpus quietly wrong, while wrongly attaching one costs a little noise. A misjudgment then costs retrieval reach, not data. Both later Billy rulings that cut against retention (**never auto-add**; **the render test**, 20 candidate notes to 12) are about *making a row or a note*, and neither touches whether the text is kept.
- **The reconciliation nobody has performed**, as the leading candidate rather than as a ruling: retain the *text* against the course, do not make a *row* or a *note*. Three records point at it and none states it.

**Touched by Billy's rulings.** **Ruling 6 supplies the store-side half of the answer and shrinks this deferral.** What enters the store is now decided by whether it improves the knowledge base as semantic, decontextualized facts about course materials - and raw announcement text mostly is not that. M89's collateral finding is the sharp case: an announcement in one course reproduces a stale copy-paste three weeks later, *"which indexed announcement text would return as current"*. So ruling 6 answers "should announcement text be embedded" with a fairly firm no, and leaves open only "should it be **kept** somewhere that is not the store" - which is what remains deferred. Ruling 5 supplies the precondition.

**Sequencing stripped.** None.

**Merge candidates.** None inside this cluster. The retention question is not the same trade-off as M90's detection question, though they will be discussed together.

**Cross-cluster.** (a) B's M19 flags "surface for confirmation, never resolve" here - **it is not in this thing**; redirect to M85. (b) C's graveyard and the `sticky_note` render test are where the anti-retention rulings live; this deferral cites them.

**Zoomed.** Yes, `domain-design.md §10.8`, `architecture.md §3` consequence 2, `write-rules.md §4.0`, `p6-channel-or-knowledge/TASK.md` anti-cheat. Unchanged, except that the P6 anti-cheat's pre-registered bias (*ambiguity resolves toward `knowledge`, the direction that makes more work*) makes the 9-16% knowledge figure a **floor**, which strengthens the retention side and is worth carrying into the deferral.

---

## M87. H3 - can a multimodal pass find a partition the course does not state

**Destination: `DEFER`**

**What is deferred.** Whether a multimodal pass can induce a usable concept partition from a course that does **not** state its own outline. Named by its own cycle as the single largest gap that run left.

**Precondition that wakes it - two parts, and both are needed.**

1. **A course whose material does not state its own outline is in the corpus.** Both measured courses state theirs, so the test cannot be run on what is held: 2c03's every deck page 2 recurs verbatim as a section divider; 2aa4 carries `[Module N]` on 27 of 30 title slides plus a written two-level taxonomy on a closing slide. The result was PASS and both agents volunteered that it was uninformative - *"the partition is not induced, it is transcribed, and that is a weaker result than a pass."*
2. **Extracting further courses is worth doing**, which `architecture.md §4` blocks until the presentation tier exists, because every contested field needs a write rule first and reading three more courses without those rules produces three more courses of noise.

**Touched by Billy's rulings.** **Ruling 9's instrument clause is the sharpest thing said about this and should be the deferral's headline**: when the instrument cannot reflect the ideal case, its result is untrustworthy. That is exactly what happened - the instrument was two courses that answer the question for free, so the PASS measures the courses, not the pass. Ruling 9 also supplies part 2 of the precondition.

**What must travel.**

- **The stated fallback**, which makes this a cost question and not a kill switch: if structure extraction fails, retrieval falls back to whole-document plus course/week metadata, which costs precision and changes nothing structural.
- **The sharper reason the free result is fragile**: the affordance is *the instructor's uniform deck template*, not the discipline. A course whose decks lack a plan page loses the free coarse layer entirely, and nothing predicts which courses those are.
- **A second, independent reason the result is uninformative, which no record states.** H3 was scored against a sealed ground truth built from Billy's own folder renames and his hand-written study guide - the artifacts M92's rule admits *only* as evidence of the organization he reaches for under pressure. Whether that invalidates the score depends on whether H3's target is the course's taxonomy or Billy's, and the task document argues the latter. It is coherent, but it means the PASS is a pass against *Billy's* partition and must never be reported as a pass against the course's.

**Sequencing stripped.** "The last unrun piece of Step 0", "not on this cycle's path", "it serves W2". All cycle ordering. The dependency claims (an instrument that can reflect the ideal case; a presentation tier before more extraction) are kept as preconditions, not as an order.

**Merge candidates.** None on trade-off. **Shared precondition** with B's M21 (H1), A's M11, F's M102 - part 2 of my precondition is their whole precondition. Recommend one shared wake-up condition cited by four deferrals rather than a merge, since the four hypotheses are unrelated.

**Cross-cluster.** M92 supplies the sealed-ground-truth caveat above; M93 is downstream of the same H3 result.

**Zoomed.** Yes, `derivation/FINDINGS.md` H3, `derivation/TASK.md` §1 and §3, `PLAN.md` §Open, `architecture.md §4`. **Changed:** the sealed-ground-truth caveat is mine, from reading `TASK.md §3` against its own rule 3; no survey connects M92 to M87.

---

## M88. Ingest ordering; cross-document decoding; deadlines hiding in prose

**Destination: `ADR`**

**Proposed title.** Intake is ordered and cross-document; no artifact is understood alone.

**Tests.**

- *Hard to reverse* - **yes.** Per-file independent intake is the obvious shape and is what every earlier record wrote; building it means every downstream field that only a governing document carries is silently absent, and the absence is invisible - a full multimodal pass over nine assignment PDFs in one course yields an obligation layer with **zero deadlines** and no error.
- *Surprising without context* - **yes, and this is the corpus's single most surprising measured fact for anyone designing intake.** Every handout in that course says, verbatim, *"See Avenue for the due date."* The handouts are primary for requirements and specs and are worthless for deadlines; the pasted portal screenshot is the **primary** deadline path, not an enrichment of it.
- *Real trade-off* - **yes.** Independent per-file intake is cheaper, parallel, and restartable. It was rejected on two courses' measurement by two agents: without the course outline, 9 of 12 graded items carry no grade weight and the allocation planner runs blind; a superscript marker peppered through one course's assignment bodies looks like about 20 authored concept edges and reads nothing, because it decodes only on page 5 of a different document.

**Body.** The governing artifact is ingested before the artifacts it governs, and no file is understood in isolation. The course outline is the only carrier of grade weights; assignment bodies carry markers that decode only against another document; deadlines hide in the prose of governing documents, so a governing document can never be treated as reference-only; and where every handout defers the date to the portal, the pasted portal screenshot is the primary deadline path rather than an enrichment of one. Cross-document decoding is a requirement, not an optimization.

**Sequencing stripped.** "Ingest is not in slice 1" - the whole spec silence on this thing is a slice fact and is dropped. The ordering *inside* the ADR (governing before governed) is a data dependency, not a plan, and stays.

**Touched by Billy's rulings.** Ruling 6, lightly: what a governing document contributes is often exactly the semantic decontextualized fact the store wants, which is one more reason it cannot be reference-only. Ruling 3 removes the calendar projection and with it any temptation to read "ordering" as a time-layer concern - the ordering here is a dependency between documents, not a position in time.

**Merge candidates.** M81 on the screenshot clause only (see M81). **Candidate for a larger merge that reconciliation can see and I cannot**: there is a scattered set of **extraction rules** - ordered and cross-document (here) · title-scoped, not full-text (B's M28, flagged to me) · write the canonical singular concept name, not the source's phrase (`write-rules.md §3.4`, M94) · never cite folder structure as the course's structure (M92) · no design vocabulary in the raw pass (`derivation/TASK.md` anti-cheat 2). Five rules about the same act, in four clusters. Recommend reconciliation consider one ADR or one write-rules section rather than five entries.

**Cross-cluster.** B's M28 flags "title-scoped, not full-text" as belonging here as a write rule - **taken**, and it is the fifth member of the set above. B keeps the edge semantics (`covers` versus mention); the extraction constraint belongs with intake.

**Zoomed.** Yes, `derivation/FINDINGS.md §4.4`, §4.5, §3 J8, and `model.md §10` items 7 and 8. Unchanged.

---

## M89. Stale material circulates as current; the redundancy defence is dead

**Destination: `ADR`**

**Proposed title.** The course site is not a source of truth; the system dates what it holds.

**Tests.**

- *Hard to reverse* - **yes.** It is the ground for holding and dating content at all rather than holding references and letting the reader fetch the current version. Every timestamp on every annotation, and the read-time maintenance pass that reads them, exist because of this finding.
- *Surprising without context* - **yes.** "The corrected version is on the course site" is what any reasonable designer assumes, and it failed on disk three times in two courses: a tutorial PDF still in its pre-correction form, a lab still naming a superseded toolchain version, and a slide deck held in the blank-whiteboard variant in which the corrected table does not exist at all. Worse, three uncorrected errors survive inside *current* handouts and were fixed by no announcement, and one course's solutions answer a prior year's question set.
- *Real trade-off* - **yes.** Holding references is far cheaper and keeps the system honest about not owning the material. It was rejected on measurement, twice, in two courses, by different agents.

**Body.** The course site cannot be relied on to hold the corrected version, so the system dates what it holds and compares dates at the read rather than deferring to the source. Locally held material is provably stale in both measured courses, current handouts carry errors that no announcement ever corrected, and material a year old circulates as current - so "the corrected version is on the portal" is not a mitigation and must not be written as one.

**The dependency the body must state, replacing a slice claim.** The comparison this rests on - a note's date against its target's revision date - has no input until a kind that carries a revision date exists. That is a known, stated gap in the record that owns the mechanism, and it means **the hazard this corpus evidenced most heavily is the one currently unmitigated**. Neither the record with the evidence nor the record with the mechanism says that; it is worth one sentence in the ADR.

**Sequencing stripped.** "In slice 1 that comparison has no input" becomes the dependency above. No ordering is carried.

**Touched by Billy's rulings.** **Ruling 7** - staleness is a conflict class, and evidenced staleness is its shallow tier: `schema.md §4` already lets the agent act on it in passing, which under ruling 7 now requires a report (see M85, distinction 2). **Ruling 6** - the stale copy-paste an announcement reproduces three weeks later is the concrete case for why raw announcement text fails the store's test: indexing it would return stale text as current.

**Merge candidates.** **M93, on a shared object**: "an edge is only as current as its sentence, and that sentence's document is dated 2025" is this hazard applied to concept edges. Same hazard, different carrier; recommend cross-reference, not merge, since M93 is deferred and this is not.

**Cross-cluster.** The revision-date field and the annotation timestamps are C's; the artifact kind that carries the revision date is B's/C's. This ADR states the requirement and must not restate the fields.

**Zoomed.** Yes, `derivation/FINDINGS.md §4.6`, `step-minus-1/FINDINGS.md` P6, `domain-design.md §10.6`, `schema.md §4`. Unchanged.

---

## M90. The correction seam - and whether it is detectable at intake

**Destination: `DEFER`**

**What is deferred.** Whether the correction seam is detectable at intake, and what - if anything - detects the two origins that no mechanism covers.

**The four origins, because two of them appear in no fall26 record and will be lost otherwise.**

1. A correction arrives (an announcement). Designed for.
2. The user states one. Designed for.
3. **The corpus disagrees with itself** - two documents already held contradict each other, nothing was delivered, and the conflict is inert until someone reads both in the same sitting. Its own author recorded it as *"a third origin for a sticky note ... it is the one that most directly serves ruling 4"* and *"the one nothing in MODEL detects"*, explicitly declining to propose a mechanism. The derivation's synthesis kept the count (2 latent) and dropped the class.
4. **The author shipped the correction inside the artifact** - a caveat that the tutorial targets an older library version, a footnote correcting the document's own terminology. Two of one course's five real notes are this. The sticky note is therefore not only an inbound-correction mechanism.

**Precondition that wakes it.** Ruling 5 states the governing posture - wait until the mechanism bites - and names the trigger better than any record does: the class of source where real conflict is likely is **Billy's own products** (a running assignment, sources for work in progress, leftovers from an engineering project), and that class is **not in the system yet**. Wake when it enters. The record's own second precondition also stands: the twelve known instances share a signature (they name a document) and twelve is too few to build on, so a larger instance count is the other trigger - which is behind the same extraction block as M87.

**Touched by Billy's rulings, and this is the entry ruling 7 changes most.** Origin 3 is two conflicting statements sitting in **source material**, which ruling 7 does not reach - the ruling governs what the *system* holds. But the moment both sides are extracted, they become two conflicting statements in the system, and ruling 7 forbids that. So **ruling 7 converts origin 3 from an undetected nice-to-have into a write-time obligation on any intake that reads both documents**, and detecting it at write time is precisely what nothing does. That is the sharpest content this deferral carries and it should be written into the issue. Ruling 5 is the counterweight and prevents the obvious over-reaction: ruling 7 constrains what happens when a conflict is met, it does not authorise building a corpus-wide contradiction hunter, and a hunter is exactly the mechanism ruling 5 predicts will ask repeatedly and persist noise.

**Sequencing stripped.** None. ("Under 10.8's first draft it stops being critical" is a dependency on M86's unruled draft, not an ordering; it is noted, not carried.)

**Merge candidates.** None on trade-off. Origin 4 (author-shipped corrections) is arguably a different thing from origins 1-3 and could be split out in reconciliation; it needs no detection at all, only that extraction is allowed to write a note from inside a document rather than only from an inbound message.

**Cross-cluster.** (a) B's M24 flags announcements-as-intake here and at M83; the `origin` field is C's. (b) The write-rules cut from the other end - *every erratum about a handout revision* fails the render test - is C's/`write-rules.md §4.0`'s and bounds this: detecting a seam is not the same as writing a note for it. (c) Ruling 4's third job (locate what the user does not know to ask about) is A's M5; origin 3 is the origin that most directly serves it, and A should know that its best-served mechanism is undetected.

**Zoomed.** Yes, both derivation agent files, `domain-design.md §10.9`, `step-minus-1/FINDINGS.md` P6, `write-rules.md §4.0`. Unchanged; the agent's self-limiting note (*"I am not proposing a mechanism; I am recording that the class exists and is populated"*) is verbatim and is the reason this is a deferral rather than an ADR.

---

## M91. RAG source classes, and what is excluded

**Destination: `ADR`, repaired by ruling 6.** The record's own content is overturned; what replaces it is a decision, not a deferral.

**Proposed title.** What goes into the store is decided by the store's nature, not by the file's.

**Tests.**

- *Hard to reverse* - **yes.** It decides the store's contents, and materialization is a pass paid once per artifact. It also silently decides what a whole class of retrieval can never reach - an excluded artifact is not merely unindexed, it is *effectively absent*, which is the phrasing the overturned ruling used and the reason the stakes are high.
- *Surprising without context* - **yes, and pointedly so.** It overrides the file-shaped intuition twice over: a handwritten note qualifies if it improves the knowledge base, and no source class is admitted merely for being slides, a PDF or a textbook. Two prior positions - one Billy's own - said the opposite.
- *Real trade-off* - **yes, with two named and rejected alternatives**, both of which were on the record: the **source-class rule** (slides / pdf / textbook in, handwritten tutorial notes out) and the **linearization axis** (embed it if meaning survives linearization). Both make the decision a property of the artifact. Ruling 6 makes it a property of the store, which is the axis neither considered.

**Body.** What is embedded is decided by the nature of the store: it holds semantic, decontextualized facts about course materials, so an artifact of any form belongs in it if embedding it improves the knowledge base's overall quality. A handwritten note qualifies on that test. No source class is admitted or excluded as a class, and no property of the file - its type, or whether its meaning survives linearization - decides the question.

**Why this had to be re-decided, worth one line in the ADR.** The excluded class was measured larger than the exclusion assumed - handwritten scans are a whole class in a core course at about 23 extractable characters per page, not the edge case the earlier probe reported - and the axis the exclusion rested on was retracted the same day, in the same corpus, by evidence that falsified file-type routing four ways in one slice. Neither passage cited the other; recency could not settle it.

**What survives from the overturned records as a requirement, not a criterion.** Intake must notice that a file yielded no text and record it as un-indexed rather than filing it as an empty document that silently answers nothing. **OCR is a separate, deferrable decision; a silent empty index entry is not deferrable, because it makes the corpus lie about its own coverage.** This requirement already has a home in cluster B (M38, detection of empty extraction, routed to ADR) - **this entry cites it and must not restate it.**

**What ruling 6 does not settle, and should become or join a deferral.** The corpus pipeline's own design remains explicitly open in the record: pass granularity, whether page images are kept, and math-equation chunking (deferred at the outset as a known industry problem). Ruling 6 supplies the inclusion criterion and nothing else. Recommend this ride with cluster B's store deferral (M35) rather than becoming a sixteenth issue.

**Sequencing stripped.** "The whole store is slice 3" and "not decided, on purpose" as a slice statement. The deferral above is kept on its merits, not on its slice.

**Touched by Billy's rulings.** Ruling 6, in full - see `## What ruling 6 overturns`.

**Merge candidates.** None. This is the store's inclusion rule; B's M32-M35 are the store's structure and access. They must cite each other and stay distinct.

**Cross-cluster - and this one needs care.** B's M37 flag says my record of the source-class rule is now wrong and *"both must not survive"*. Agreed on the source-class rule. **Sharpening on the other half: what dies is linearization as an *inclusion criterion*. `text_extractable` survives as a materialization *outcome* - a per-region flag, default false, set true only when a pass actually recovered text, read by the trust contract to tell a quotation from a generated description.** That is a record of what happened, not a rule about what may enter, and ruling 6 does not touch it. B's M37 should carry that distinction explicitly or the field will be over-killed along with the axis.

**Zoomed.** Yes, `domain-design.md §10.7` ruling 3 and §1 ruling 9 and §10.9, `model.md §9`, `derivation/FINDINGS.md §4.1` and §5, `step-minus-1/FINDINGS.md` P2 and P6, `design.md §5`. **Changed:** a **third** record rests on the overturned rule and neither the inventory nor cluster B lists it - see `## What ruling 6 overturns`, item 3.

---

## M92. The portal's folder tree is not the skeleton's shape

**Destination: `ADR`**

**Proposed title.** Delivery layout is not organization; resolution is semantic.

**Tests.**

- *Hard to reverse* - **yes.** It fixes that a pasted intake screenshot carries **provenance, not position**, so parent resolution is semantic rather than a path match. Everything that places a node rests on it, and the cheap alternative is always available and always tempting.
- *Surprising without context* - **yes**, and the evidence of how surprising is that the same session that recorded the rule violated it twice: once as a deliberate reframe that was not marked as an override, and once as a straight error inside the model, caught and corrected in place with the note that it was *"exactly the folders-are-not-taxonomy error this cycle exists to avoid."*
- *Real trade-off* - **yes.** The folder tree is free, already structured, and right there. It is rejected because it shows how files are *distributed*, which is not how knowledge should be *organized* - and finding the better organization is the reason the system exists.

**Body.** The portal's folder tree shows how files are distributed, not how knowledge is organized, and finding the better organization is why the system exists. A pasted intake screenshot therefore carries provenance and not position: a node's parent is resolved semantically and never by a path match, and filename similarity implies nothing - in every measured case the discriminator was content. The user's own folders are admissible as evidence of the organization he reaches for under pressure, and never as the course's structure.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 8, in agreement and worth a cross-reference: the same instinct that reads a folder tree as taxonomy reads "Week N" as a node. Both are delivery scaffolding mistaken for structure. The content layer and the time layer stay separate, and neither is the portal's.

**Merge candidates.** None on trade-off inside this cluster.

**Cross-cluster.** (a) **B's M17 flag - I disagree, with the record.** B reads M92 as the same ruling as "layered graph, not a tree", aimed at intake. `model.md §9` states its own sibling and it is a different one: *"This is design §10.6's finding one level up - announcements are a delivery channel, and the portal tree is a delivery layout."* M92's ground is *distribution is not organization*; M17's ground is *a course's knowledge does not nest*. Recommend M92 pair with M83 (the channel finding), not with M17. (b) **B's M39 flag - agreed, and here is the one-place proposal**: "filename similarity implies nothing" was measured in B's M39 (one lecture, several files) and should be **stated once there**, with M92's ADR citing it as the same principle aimed at intake. (c) M87 depends on this rule and partly conflicts with it - see M87's third bullet.

**Zoomed.** Yes, `model.md §9` and §3's CORRECTED banner, `derivation/TASK.md` §2 rule 3 and §3. **Changed:** the inventory reports the §3 override as an agent overriding a human warning. At source the override carries a coherent defence - the seal's target is Billy's organization, not the course's, which is what H3 was asking about - and the inventory does not quote it. The override is still unmarked and the H3 result still rests on it, but it is a method risk to record at M87, not evidence that the rule was broken.

---

## M93. The skeleton is not authored by Billy at course setup

**Destination: `DEFER`**

**What is deferred.** Where concept nodes and cross-layer edges come from, and who draws them. The record's own owed item says it: *order and weight unsettled.*

**Precondition that wakes it.** The `concept` kind exists (it does not in the current field set), and the same instrument gate as M87 - a course that does not state its own outline - since the dominant origin today is transcription from a stated outline and that origin makes the question moot wherever it applies.

**What must travel, three things, and the second and third are why this is not a one-line deferral.**

1. **Not at setup.** At setup the user does not yet know the concept structure; he knows it at the end. The earlier draft failed on survivorship bias - it was justified by the slow-plus-self-authored test, which is satisfied, and still wrong.
2. **"Not at setup" is not "not by Billy".** He authors concept edges by hand, unprompted, mid-semester. The measured instance is ink over a tutorial exercise - *"This question tests: MAD compression, linear probing insertion, probe counting"* - an artifact-to-concept edge at fragment grain, on a page with no text layer, in a form the system can never read. The mid-semester folder renames are the same behaviour in a second modality. **Nothing in any record designs for this origin**, and it is the origin most likely to be right.
3. **Edges are authored in bulk from single sentences.** One clause in a tutorial handout creates 9 prerequisite edges; one slide in a review deck creates 26. The model assumed cross-layer edges are drawn item by item; they are not. The corollary is a hazard: an edge is only as current as its sentence, and that sentence's document may be a year old.

**Sequencing stripped.** "Concept is slice 2" becomes the dependency in the precondition. No ordering carried.

**Touched by Billy's rulings.** Ruling 1 bounds it - v1 is coursework inside academics, and concepts are not graveyarded, only later. Ruling 9's instrument clause supplies half the precondition.

**Merge candidates.** **M94** - strong, and I recommend reconciliation consider one deferral. M93 asks where a concept edge comes from; M94 asks how one is changed afterwards. Origin 2 above (hand-authored, mid-semester) is exactly the operation M94 defers, and M94's own record says the concept layer is built incrementally and must be refinable. They are two halves of one question and were separated only because they sit in different items of the same owed list. **Also M89**, on the staleness corollary in point 3 - cross-reference, not merge.

**Cross-cluster.** The `concept` kind and its edges are B's (M22, M27, M28); this deferral is about who writes them, not what they are.

**Zoomed.** Yes, `model.md §9` and §10 item 2, `derivation/FINDINGS.md §5`. Unchanged.

---

## M94. Concept split / merge / rename

**Destination: `DEFER`**

**What is deferred.** The refinement operations on the concept layer - split, merge, rename - and what they do to identity and to existing links.

**Why deferral and not ADR.** It is self-declared under *"Owed, and deliberately not settled here"*, and merge rule 3 honours a self-declared not-ruled. What is in the record is an argument for why the operations are legitimate, not a mechanism.

**Precondition that wakes it.** The `concept` kind exists and the first refinement is actually needed - which per M93 is mid-semester, by Billy, on material he has just re-understood. Cluster B's M28 gives a second, sharper trigger for the granularity half: when a single artifact's extraction would produce coverage edges to more than about half a course's concepts, the question is live.

**What must travel.**

- **The distinction, which is the corpus's cleanest statement of why one falsification does not generalise, and which will otherwise be lost.** Refining concepts is *not* the falsified operations model returning. That model was **external inbound destructively rewriting a held fact** - irreversible, and the author was not the reader. This is **the owner refining his own model of the material** - lossless, reversible, and authored by the person the system serves. Different object, different author, different failure cost. Without this sentence, the M82 drop will be read as forbidding refinement.
- **The deferral is narrower than it looks, because admission and granularity are already ruled.** Two written rules do that job and **neither record says it is doing it**:
  - *Admission* - `write-rules.md §3.4`, Billy, 2026-08-28: a concept is worth capturing **because it might occur elsewhere in the system**, on another obligation or in another course. Measured: 50 candidate strings became 28; the paper's structure (`Multiple Choice`, `Problem Solving`) is noise, and one-off local names (`Monte-Carlo`, `A5Tree`) are not worth capturing. Plus: write the **canonical singular** name, not the source phrase - `Stacks and Queues` becomes `Stack` and `Queue`.
  - *Granularity* - the derivation's restatement: one concept is one thing that can be **separately asked about or separately taught**. This is what dissolved the hub ("design patterns" at 16 versus its members at 4).

**Sequencing stripped.** "Slice 2" as the concept layer's home. The dependency (the kind must exist) is kept.

**Touched by Billy's rulings.** None of the nine touches it directly. Ruling 1 keeps concepts alive for later.

**Merge candidates.** **M93** - see M93; recommend one deferral covering origin and refinement.

**Cross-cluster - and B's flag needs sharpening.** B's M28 says `write-rules.md §3.4`'s recurrence test **is** the concept-granularity ruling, which neither record says. **Half agreed, and the half matters.** The recurrence test decides **whether** a string is a concept worth a node; the separability test decides **at what grain** one is cut. They are two different jobs and both are needed - `Multiple Choice` recurs constantly and is still noise, which the recurrence test catches and the separability test does not. Recommend they be recorded as two halves of one rule, not as one rule stated twice. Consequently, **cluster B's `concept` term definition is correct as a definition of the kind and incomplete as a rule for the write side**: "a unit of subject matter the course teaches, independently addressable" is the separability half, and not every independently addressable unit gets a node - only one that might occur elsewhere does. B's term can stand; the admission clause belongs in this ADR or in C's `parts` entry, and one of them must carry it.

**Zoomed.** Yes, `model.md §10` items 1 and 3, `write-rules.md §3.4` and its 08-28 changelog entries, `derivation/FINDINGS.md §5`. **Changed:** the inventory records M94 as "owed, uncontested" and single-source. It is neither - two later written rules answer half of it, and the inventory's own C21 is about the same rule.

---

## M95. The capture point - `/wrap`, and the third class

**Destination: `DEFER`** - and ruling 4 says so explicitly: the capture-point question is deferred, not answered, and this cluster owns it.

**What is deferred.** Whether the system asks at the read for facts with no generating event - progress, difficulty, how much load a week already carries.

**Precondition that wakes it.** Ruling 2's gate: the system is roughly built and ask-frequency has been measured over real interaction rounds, with the stated interpretation - if the agent must ask constantly, either something needs persisting or the design has a seam, and either finding is a design change rather than a tuning. A second, concrete trigger comes from the governor itself: *only ask what changes a decision* is unrunnable until there is a decision being made, so the first case where the agent cannot complete a real allocation because a third-class fact is missing is the wake event.

**What must travel.**

- **The third class is real and its argument is not a preference.** Facts split three ways, not two: external and time-critical (capture at the moment) · self-authored and durable (capture at close of session) · **self-authored and not durable** (capture at the read, because the system asks). A deadline is generated when the professor posts it; **a progress state is generated by nothing**, so there is no moment at which it could be volunteered, and forgetting to supply it is **structural rather than a lapse**. Billy's own words: the system moves from *waiting for input* to *asking for input*, because proactive supply requires remembering, and remembering is the thing that failed.
- **The governor, which is the intended reconciliation and which neither side of the conflict ever invoked**: only ask what changes a decision. Left ungoverned this degenerates into an interrogation - one blind run alone produced about nine askable items, which is not an improvement on one stale value. And the sharp form: **the gate that decides what belongs in the observation space and the gate that decides what is worth asking are the same gate.**
- **The counter-pressure, which is settled and must not be re-opened by this deferral.** `progress.state` is non-nullable and defaults to `not_started` precisely so the system does not announce it does not know and thereby give an agent a reason to ask *have you started this yet*. Ruling 4 confirms it. So the deferral is about the *rest* of the third class - difficulty, load, how far along - not about progress state.
- **`/wrap` itself is dropped as an old-container artifact.** It is a repo ritual in a container that no longer exists. What survives is not the ritual but its diagnosis, which is the finding: *"It was never a problem with the ritual. It was a problem with the material."* The two-property test (slow, self-authored) is the durable content and it is what produced the third class.

**Touched by Billy's rulings.** Ruling 4 defers this by name and says why: proactivity is written too rigidly at present and will bite; design it when it is needed. Ruling 2 supplies the measurement gate. Ruling 9 raises the adjacent unknown it will collide with - onboarding is undefined, including who does it and how information arrives, and asking-at-the-read is one candidate answer to "how information arrives".

**Sequencing stripped.** None.

**Merge candidates.** **Strong, and this is my main structural recommendation to reconciliation**: A's M7 (proactivity and asking), M84 (confirmation before a write) and M95 (asking at the read) are three faces of one question with one wake condition. One deferral issue with three acceptance items.

**Cross-cluster.** (a) A's M7 - direct duplicate of the gate; A already flagged it. (b) `progress.state`'s default is C's field ruling and this deferral must cite, not restate it. (c) Ruling 9's onboarding question has no owner anywhere; it lands next to this one and reconciliation should decide whether it joins this issue or gets its own.

**Zoomed.** Yes, `domain-design.md §9.6` in full including the promoted `[R]` block and its three-row table, `openclaw:log/2026-08-21` capture-point section, `architecture.md §3`, `schema.md §4.5`. Unchanged - both sides are Billy's own, four days apart, and the governor is in the same block as the ruling it governs.

---

## M96. An asked answer persists

**Destination: `ADR`**

**Proposed title.** An asked answer is kept, and its provenance is loud.

**Tests.**

- *Hard to reverse* - **yes.** It is a field shared across both annotation kinds plus a rendering obligation on every read. Removing it makes every asked answer indistinguishable from a volunteered one, which is the exact failure it was written to prevent.
- *Surprising without context* - **yes.** The intuitive fix for "a stale answer keeps influencing decisions" is to stop storing it, or to expire it. This does the opposite: it stores it and makes the storage loud. The reasoning is the surprising part - the harm was never storage, it was **silent** influence, *"so that an agent cannot read a historical answer as a current fact"*.
- *Real trade-off* - **yes, two alternatives, both rejected on the record.** Not persisting the answer means asking again forever, and the ask is the expensive act. Expiring it repeats a measured mistake: `done` was harmful because it was read as terminal and erased a live item, not because it was recorded.

**Body.** An answer the system asked for is stored, with its timestamp and its provenance, and the provenance is stated prominently at every read. The harm of a stale answer was never that it was recorded - it was that it went on influencing decisions invisibly - so the fix is to make the record loud rather than to drop or expire it. This is the same shape as the finding that a terminal-looking status was harmful for being read as terminal, not for existing.

**The owed rider, with its failure mode already measured.** The write rule for the provenance field is owed, and the divergence is known: the schema's prose says the field records **how the claim was obtained**, and *both* independent extraction passes reached instead for **what document class it came from**. That is a definition-versus-practice divergence that will recur every time the field is written until the rule exists. It should ride inside the ADR as a named gap, not be silently inherited.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 4, indirectly and importantly: the whole point of not re-asking is that asking is expensive, which is the same premise ruling 4 uses to remove an occasion to ask. Ruling 7 shares this ADR's principle - see below.

**Merge candidates.** **M85, on a genuinely shared trade-off, and I recommend cross-reference over merge.** "Stated prominently, so an agent cannot read a historical answer as a current fact" (Billy, 2026-08-23) and "never resolve transparently; report afterwards" (Billy, 2026-08-29) are one principle applied to two acts: **the system may act, and may store, but never invisibly.** Six days apart, in different records, neither citing the other. Reconciliation should name the shared principle in one line in both ADRs; merging them would bury ruling 7's two-tier table.

**Cross-cluster.** The `origin` field itself, and its sharing across both annotation kinds, is C's. This ADR owns the ruling and the rendering obligation; C owns the field.

**Zoomed.** Yes, `domain-design.md §9.6`'s second `[R]` block, `schema.md §4` and §4.5, `write-rules.md §4`. Unchanged; the domain sentence is imported into the schema verbatim, which is the cleanest cross-corpus carry-through in this cluster.

---

# Terms proposed

No thing in this cluster routes to `CONTEXT.md` as its destination, which is itself a finding: cluster E answers *what the system does when something arrives*, and that is decision-shaped. Cluster B owns the noun spine and I classify against it. Four terms spin off from ADRs here, in B's `(from ADR)` convention, plus one amendment to a term B already owns.

| term | definition | _Avoid_ |
|---|---|---|
| **extraction** *(from ADR, M88)* | The pass that reads delivered material and produces candidate facts. It changes with the material. | *ingestion* · *parsing* · using it for what happens to the candidates afterwards |
| **landing** *(from ADR, M85)* | The write of candidate facts into the skeleton. It is idempotent, it detects conflicts instead of overwriting, and it changes with the schema. | *ingestion* · *import* · `land()` used as the name of the concern rather than of one operation |
| **conflict** *(from ADR, M85)* | Two statements the system holds that cannot both be true of the same thing. It is shallow or deep by what is in conflict, and that is what decides whether the agent may close it itself. | *contradiction* used interchangeably · using it for a mismatch between the system and the world, which is **staleness** · using it for a progress claim, which is an authorship question |
| **write rule** *(from cluster F's M98, consequence 1)* | An instruction to whoever produces a value for a field whose legal values cannot be enumerated. It is derived from what has to be true for the node to **render well**, never from what a source document happens to say. | the withdrawn absolute *"a write rule never refers to the source"* · *validation* (a write rule is enforced nowhere) · *schema rule* |

**The `ingestion` / `materialization` collision resolves by deletion, not by coining a term.** Cluster B raised it (M34) and the inventory raised it (C64: the word is used for *fetching*, which Billy ruled out of scope, and for *processing at the endpoint*, which is extensively designed, and nothing anywhere reconciles them). The resolution is that **`ingestion` should not be a term of this project at all.** One of its senses names something ruled out of scope (M81), and the other names three concerns that a record already separates on the ground that they change for unlike reasons: **extraction** (with the material) · **landing** (with the schema) · reading (with agent-engineering practice). **materialization** - B's term, the one-time pass turning an artifact's raw content into stored readable form - is a fourth and is correctly named. So: add `ingestion` to `_Avoid_` on **materialization**, **extraction** and **landing**, and let the word die. B's `materialization` definition is correct as written and needs no change beyond that.

**Received from cluster F.** F flagged that M98's consequence 1 (write rules) belongs here and must carry the 2026-08-28 correction. Taken, as the **write rule** term above. The correction: the condition line's absolute phrasing was withdrawn because **three of the five written rules do refer to a source** - *store what the material prints* (§3.1), *`optional` defaults to false unless a source states otherwise* (§3.5), and *when a source does not state a value and the agent infers one, it asks the user* (§1.1). The real distinction is **the direction a rule is derived from**. The withdrawn phrasing still stands in both bodies at source and is what a reader hits first in each, so it must be written into the term or it will be inherited twice.

---

# What ruling 6 overturns

Every record in this cluster that stated the source-class rule or the linearization axis as a **standing criterion for what enters the store**, and what survives of each as a requirement.

**1. `domain-design.md §10.7` ruling 3 (Billy, 2026-08-22) - the source-class rule. Overturned whole.** *"RAG stores slides / pdf / textbook-class sources. Handwritten tutorial notes are excluded - not embedded, effectively treated as absent ... The source-class rule is the operative one."* Nothing of the criterion survives: under ruling 6 a handwritten note qualifies if it improves the knowledge base's quality, and no class is admitted for being a class. **What survives is not from this passage but from the evidence around it** - that the excluded class was measured larger than the exclusion assumed (handwritten scans at about 23 extractable characters per page are a whole class in a core course), which is now a fact about how much material the store must handle, not an argument about who is right. Carried in M91's ADR as the reason the question had to be re-decided.

**2. `model.md §9` and `derivation/FINDINGS.md §4.1` (agent, 2026-08-22) - the linearization axis. Overturned as a criterion; its field survives.** *"The real axis is whether meaning survives linearization - a property of the materialization pass, not of the file."* As a rule for what gets embedded, it dies with the source-class rule: ruling 6 makes the decision a property of the store, and both prior positions made it a property of the artifact. **What survives is twofold and both halves are requirements, not criteria.** (a) `text_extractable`, per region, default false, set true only when a pass actually recovered text - a record of what a pass achieved, read by the trust contract to distinguish a quotation from a generated description. It is not an inclusion rule and must not be deleted along with the axis; this is the sharpening cluster B's M37 needs. (b) The falsification itself remains valid evidence that file type predicts nothing - PDFs with no text layer at all, a text PDF whose exercises are images so backing is not uniform *within one file*, a `.png` more chunkable than several PDFs, one diagram held as both a machine-readable and a raster form.

**3. `derivation/FINDINGS.md §5` (2026-08-22) - a third record resting on the overturned rule, listed in no survey and in no cluster.** Deciding what to do with Billy's own handwritten task solutions, it says: *"Whether they enter the store is decided by design §10.7's source-class rule alone."* That dependency is now void and the question it delegated is re-opened - under ruling 6 the answer is whatever improves the knowledge base, and a handwritten solution is exactly the case ruling 6 names as qualifying. Flagged so the reconciler does not carry `§5`'s adopted consequences forward with a dead delegation inside them.

**4. `step-minus-1/FINDINGS.md` P2 - the requirement that survives all of it.** Not an inclusion criterion and never was, which is why it is the one thing that comes through unchanged: *"ingestion must notice that a file yielded no text and record it as un-indexed, rather than filing it as an empty document that silently answers nothing. OCR is a separate, deferrable decision; a silent empty index entry is not deferrable, because it makes the corpus lie about its own coverage."* It has a home in **cluster B's M38** and this cluster cites it.

**What ruling 6 does not settle.** The pipeline itself - pass granularity, whether page images are kept, math-equation chunking. Explicitly open in the record before ruling 6 and still open after it.

---

# Where ruling 7 anchors

**Proposal: M85, as a repaired ADR titled "Two conflicting statements never coexist, and how a conflict closes depends on what is in conflict."** The two-tier resolve policy rides inside it as a table. Reasons, in order:

1. **M85 is the only thing in any cluster that already holds the invariant's mechanism.** Landing detects conflicts instead of overwriting; the return type carries a `CONFLICT` outcome; the adjudication is assigned to the presentation tier; and the corpus's one existing conflict rule - "you told me this, the record says that, which holds" - is Billy's own, from 2026-08-23. Ruling 7 generalises what M85 already does for one case.
2. **M85 already holds a two-tier rule in miniature and needs ruling 7 to complete it.** `schema.md §4`'s maintenance-at-read pass says evidenced staleness is *"staleness the agent may act on in passing"* while anything else is *"surfaced for confirmation and never resolved"*. That is shallow-versus-deep by another name, written 2026-08-28, and it has **no report obligation** - it is the one place in the corpus where an agent is currently authorised to resolve something transparently, which ruling 7 forbids. Anchoring ruling 7 here fixes an existing rule rather than adding a parallel one.
3. **M82 is the alternative and is the wrong home.** M82 holds the *objection* that ruling 7 upholds, and the objection is six days older than any spec record and belongs to a model that is dead on measurement. Putting a live invariant inside a falsified model's entry buries it. M82 drops and its objection relocates here as this ADR's rejected alternative - which is exactly what it is, and it is the strongest rejected-alternative statement in the corpus: *"it relocates Billy's uncertainty into the system while making it look handled."*
4. **Cluster A's flag 1 asked for exactly this** and named B or E, whichever holds write rules and store invariants. E holds both, per cluster F's hand-off of consequence 1.

**What must be written into it beyond the ruling.** The resolved-target shape from M84 (a confirmation presents *"changing assignment 3's due from Wed to Fri"*, never a yes/no), because ruling 7's "ask to clarify or confirm" and "report afterwards" are otherwise not executable. The three distinctions listed at M85 - progress is an authorship rule and not a shallow conflict; `schema.md §4` needs the report clause; ruling 5 is the governor and ruling 7 is not a mandate to hunt. And the field-set requirement: depth is a property of what the statement collides with, not of the statement, so the discriminator lives on the record and that is an obligation on cluster C.

**What ruling 7 closes, elsewhere.** C65 (open since 2026-08-21, flagged by two documents with an explicit instruction not to pass over it, untouched by six days of spec work) - closed, objection upheld. C68 - already dissolved, now with a policy attached. It also **converts M90's latent origin from an undetected class into a write-time obligation the moment both sides of a corpus self-contradiction are extracted**, which is the consequence I would most expect a reconciler to miss.

---

# Orphan rulings

**1. `write-rules.md §1.1` - "An inferred value is asked about, not annotated." Billy-ruled 2026-08-28, and it has no M-number in any cluster.** It is surveyed as S2's T43 and appears in the inventory **only** as one of three instances inside conflict C78, where it is cited to prove a different point (that the absolute "never refers to the source" phrasing was contradicted). No thing entry is about it. Its content:

> When a source does not state a value and the agent infers one, it **asks the user**. It does not write the inference into a note beside the field. Measured: the extraction stored a derived final-exam date and attached a note explaining the derivation. Wrong shape - *"when the announcement about an actual date and time comes, the agent should change the time for that obligation, not attach a note saying that a time is inferred."* **An update is an update.** A correction changes the field; it does not accumulate commentary beside it.

**Why it matters, twice over.** (a) *"A correction changes the field; it does not accumulate commentary beside it"* is **ruling 7's invariant already written at field level, eight days before ruling 7** - it forbids exactly the coexistence ruling 7 forbids, in the one place a write actually happens. It should be adopted into M85's ADR as its existing field-level instance. (b) *"it asks the user"* is a fourth item in the asking thread, alongside rulings 2, 5 and 7, and it is the only one that is already a written rule rather than a deferral. Recommend: adopt into M85's ADR; do not create a separate thing.

**2. A ruling inside a cited section that no entry records: `schema.md §4`'s two-tier maintenance rule.** *"a target revised later than the note is evidenced staleness the agent may act on in passing, while anything else may be surfaced for confirmation and never resolved."* M89 cites `schema.md §4` for the *neighbouring* sentence (timestamps plus maintenance-at-read is what makes a time-bound statement safe to store) and no survey or inventory entry records this one. It is the corpus's only existing shallow-versus-deep conflict policy and the only place an agent is currently allowed to resolve silently. Not a full orphan - its section is cited - but it is a ruling nobody has, and it changes where ruling 7 anchors. Carried at M85, distinction 2.

**3. Weak, flagged rather than claimed: `design.md §3.6`'s "extraction, landing and reading are three concerns, and they change for unlike reasons."** Cited by four inventory entries (M84, M85, and two in cluster F) and no entry is about it. It is the record that resolves the `ingestion` word collision, so it needs a carrier somewhere; the two terms above are my proposal for what survives of it. If reconciliation prefers, it is a small ADR in cluster B or F rather than an E thing.

---

# Summary

**Counts.**

| destination | count | things |
|---|---|---|
| `CONTEXT` | **0** | none as a destination; **4 terms spun off from ADRs**, plus one amendment to cluster B's `materialization` |
| `ADR` | **8** | M81, M83, M85, M88, M89, M91, M92, M96 |
| `DEFER` | **7** | M84, M86, M87, M90, M93, M94, M95 |
| `DROP` | **1** | M82 |

Total **16**. The zero in the first row is expected rather than a gap: this cluster answers *what happens when something arrives*, which is decision-shaped, and cluster B owns the noun spine.

**Sequencing stripped, gathered.** Slice and cycle framing dropped from M81 ("slice 1's write side"), M84 ("`land()` not in the first build" - the tier assignment kept), M85 (F2 as a slice-1 acceptance requirement), M87 ("the last unrun piece of Step 0", "it serves W2"), M88 ("ingest is not in slice 1" - the whole spec silence), M89 ("in slice 1 that comparison has no input" - rewritten as a dependency on a kind that carries a revision date), M91 ("the whole store is slice 3"), M93 and M94 ("concept is slice 2" - rewritten as a dependency on the kind existing). **Two orderings were kept deliberately because they are data dependencies and not plan**: M88's governing-artifact-before-governed, and M87's instrument-before-test.

**Least certain calls, in order.**

1. **M82 as `DROP`.** It is the only drop in the cluster and it drops the entry that carries ruling 7's objection, on the argument that the objection relocates cleanly to M85. If reconciliation reads the relocation as lossy, the right correction is not to keep M82 as an ADR - the model is dead on measurement and an ADR would be recording a corpse - but to fold M82's falsification numbers into M83's ADR body more fully than I have.
2. **M94 as `DEFER` rather than `ADR`.** Its self-declared standing is *owed*, which merge rule 3 honours, so deferral is defensible. But the operations-model distinction inside it is a live reasoning move that the M82 drop makes *more* necessary, not less, and it will sit unread in a deferral. A reconciler who prefers a small ADR ("concepts are refinable, and that is not the operations model returning") has a case, and it merges cleanly with M93.
3. **M85 as ruling 7's anchor rather than a new thing.** The ruling is broader than M85's original content and I am repairing an entry rather than creating a home. Anchoring it here is right if `schema.md §4`'s existing two-tier rule is real - I verified it at source and it is - but a reconciler who reads ruling 7 as a store invariant first and a conflict policy second may prefer it to sit with cluster B's store entries. I would argue against that: the invariant without the two-tier policy is unimplementable.
4. **M91 as `ADR` rather than `DEFER`.** Ruling 6 gives a criterion and nothing else - not the pipeline, not the granularity, not page images. I routed it to ADR because the criterion is the hard-to-reverse part and it now has three rejected alternatives on the record. If reconciliation reads it as too thin to build on, the fallback is an ADR with a companion deferral, not a deferral alone; the criterion must be written down or the source-class rule will come back.

**One finding that belongs to no thing and should not be lost.** **Rulings 2, 5 and 7 all route load onto asking, `write-rules.md §1.1` adds a fourth route, and nothing measures ask-frequency.** Ruling 2 says so itself and calls it an acceptance and evaluation item measurable only after the system is roughly built. Three deferrals in two clusters (A's M7, my M84, my M95) wake on that measurement and none of them owns it. Recommend one deferral issue with three acceptance items and a named owner for the metric.

**Every cross-cluster flag, in one list.**

| from | to | what |
|---|---|---|
| M81 | B (M34), all clusters | **`ingestion` should be retired as a term**, not disambiguated - one sense is out of scope, the other is three already-named concerns. Add to `_Avoid_` on `materialization`, `extraction`, `landing` |
| M81 | B (M37, M38) | the multimodal-endpoint clause is the premise of `text_extractable` and of empty-extraction detection |
| M82 | B (M23) | the `supersedes` cut's ground is this drop - read-time expiry beat write-time supersession about 7:1 |
| M82 | F (C91) | the p5 method (*answer in the material's own terms first*) is a research-method ruling and belongs with F's method thread |
| M83 | B (M24) | **confirmed and sharpened**: `model.md §8`/`§9` paraphrase `§10.6` as the flat proposition *announcements are a delivery channel*, which is the proposition that **failed in both courses**. The correct statement is *mostly a channel; the 9-16% that is not is almost always a correction against material already held*, and the bias was pre-registered against that answer so it is a floor |
| M84, M95 | **A (M7)** | **strong merge**: three deferrals, one wake condition. Recommend one issue with three acceptance items |
| M84 | F (M98), C | `architecture.md §3` consequence 3 is cited here and owned there; this cluster must not restate it |
| M84, M86 | B (M19) | **redirect**: "surface for confirmation, never resolve" is at **M85**, not M84 or M86 |
| M85 | **A (flag 1)** | **answered** - ruling 7 anchors at M85 |
| M85 | B (M23) | the resolve-and-report / ask-first split is this cluster's write rule; taken |
| M85 | **C** | new obligation: the field set must carry what distinguishes a shallow conflict from a deep one, because depth is a property of what a statement collides with, not of the statement |
| M85 | B (M37), F | `Diff` and its `CONFLICT` outcome are the mechanism; this ADR owns the policy only |
| M87 | B (M21), A (M11), F (M102) | **shared precondition, not a merge** - four deferrals wake on "the presentation tier exists so more extraction is worth doing" |
| M88 | B (M28) | "title-scoped, not full-text" as an extraction rule - **taken** |
| M88 | reconciliation | **five extraction rules in four clusters** (ordered/cross-document · title-scoped · canonical singular names · folders-are-not-taxonomy · no design vocabulary in the raw pass). Consider one home |
| M89 | C, B | the revision-date field and the artifact kind that carries it; this ADR states the requirement only |
| M90 | A (M5) | the origin that most directly serves ruling 4's third job is the one nothing detects; A should know |
| M91 | **B (M37)** | **sharpening**: linearization dies as an *inclusion criterion*; `text_extractable` survives as a materialization *outcome*. Do not delete the field with the axis |
| M91 | B (M35) | the pipeline's open half (pass granularity, page images, math chunking) should ride with B's store deferral rather than become a sixteenth issue |
| M91 | B (M38) | the silent-empty-index requirement has its home there; cited, not restated |
| M92 | **B (M17)** | **disagreement, with the record**: `model.md §9` names its own sibling and it is the announcements-as-channel finding, not the layered graph. Pair M92 with M83 |
| M92 | B (M39) | "filename similarity implies nothing" - state it once in M39, cite it from M92 |
| M94 | **B (M28), C** | **sharpening**: the recurrence test decides *whether*, the separability test decides *at what grain*. Two halves, not one rule stated twice |
| M94 | **B (term list)** | B's `concept` definition is correct as a definition and incomplete as a write-side rule - not every independently addressable unit gets a node, only a recurring one does. Either M94's entry or C's `parts` must carry the admission clause |
| M95 | C | `progress.state`'s non-nullable default is C's field ruling; cited, not restated |
| M95 | reconciliation | **ruling 9's onboarding question has no owner in any cluster** - who does it, and how information arrives. It lands beside M95 |
| M96 | C | the `origin` field and its sharing across both annotation kinds are C's; the ruling and the rendering obligation are here |
| M96 + M85 | reconciliation | one shared principle across two ADRs - **the system may act, and may store, but never invisibly**. Cross-reference, do not merge |
| **orphan 1** | M85 | `write-rules.md §1.1` - Billy-ruled 08-28, no M-number anywhere, and it is ruling 7's invariant already written at field level |
| **orphan 2** | M85 | `schema.md §4`'s two-tier maintenance rule - recorded by no entry, and the only place an agent may currently resolve silently |
| **orphan 3** | B or F | `design.md §3.6`'s three-concerns split - cited by four entries, owned by none |
| received | **F (M98 c1)** | write rules are this cluster's; taken as the `write rule` term, carrying the 08-28 withdrawal of the absolute phrasing |
