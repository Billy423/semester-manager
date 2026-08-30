# The open escalations, grouped for one reading

Derived from `04-thing-inventory.md` Part III. Regrouped by subject so that answering one informs the next, rather than by the merge's downstream-weight order.

**Already settled since Part III was written:**

- **E7, the goal function** — ruled 2026-08-29. Both forms are one criterion at two levels; the third job is **pull, not push**; the anti-inflation test keeps Form 1's shape (*does this reduce reload cost?*) with typed traversal counted as reducing it. This is the frame the rest are judged against, so it is stated here and not re-opened.
- **Concept granularity (C21)** — Billy notes 2026-08-29 that granularity was ruled and the write rules cover it. Flagged below where it bears, but treated as probably stale rather than open.

Every quote below is from the corpus. Nothing here is adjudicated.

---

## Group 1 — Scope: how wide is this system?

### E6. Is the boundary one semester, or the academic domain?

**Side A — 2026-08-21, `domain-design.md §0.6`.** The strongest statement in the corpus of why this is not a deadline tracker:

> "Winter-only mandatory courses ruled out a winter-27 co-op, and thereby set the entire recruiting target to summer 27. That decision was made inside ai-eng's academic track, and **Fairy never held the fact — because no home existed for a constraint spanning academics and career.** So the academic domain must hold **course offering-terms and prerequisite structure**, since that graph gates other domains' decisions. **This is the single most concrete design input carried in the originating dispatch, and it is why 'just track my deadlines' is the wrong target.**"

**Side B — graveyarded, `schema.md §7`.** `course.offering_term` and `course.prereq`: "null for both courses in the fixture, and **`offering_term`'s justification is another domain's need, in a domain that does not exist**." Under a standing do-not-re-add rule.

**What turns on it.** B's reason is **a container fact, not a domain fact** — "a domain that does not exist" describes what else was running in openclaw. The container has changed. Nothing in either corpus says what now holds offering-term and prereq, or whether §0.6 survives. `domain-design.md §0.1`'s telos is still on the record: "**every aspect of Billy's life managed under one contract.**"

**The question.** If the boundary is one semester, §0.6 is dead and should be recorded dead. If it is the academic domain, the requirement needs a home and the graveyard entry needs a new ruling to reverse it.

---

## Group 2 — The allocation layer: what carries "how much", and where the plan lives

These two are one subject. The plan is what allocation produces; size is what allocation needs. Neither exists right now.

### E2. `workload` was retired on a mechanism a later ruling removed, and nothing carries size

**The chain, all Billy, six days, three record sets.**

> **08-22, measured** (`derivation/FINDINGS.md §3`): "**`workload` is absent from every single obligation, in both courses, in every source.** … Billy's own hand-maintained Notion table, kept for a year, also has no workload column and *does* have a `target_date` the schema lacks."

> **08-23, Billy `[R]`** (`domain-design.md §6.1`): "hours_estimate 很难量化，我一般都是按照某个 assignment 的进度和 high-level 体量来判断的。" Ruled in three parts: not a field to be filled; "**Size is observed ordinally — from `parts` and item notes first**"; "its missing-rate is retired as a guard signal. **Replacement guard: faithfulness.**"

> **08-27, Billy, ruled** (`schema.md §3`): `grade_share` is "Reference only — never an input to a computed ranking, **because workload is judged from progress plus size rather than from the percentage.** **This is a standing EXEMPTION** from the rule every other field passes."

> **08-28, Billy, ruled** (`write-rules.md §3.4`): "**`parts` carries concepts, and it does not carry size.**"

> **08-28** (`ring-0.md §4`): `parts` excluded from the projection — "it carries concepts rather than size **so it does not answer *how much* either**."

**What this leaves.** `workload` is graveyarded with a no-re-add rule. Its stated replacement mechanism is gone. `grade_share`'s exemption names that removed mechanism as its reason. And **ring 0 — whose declared job is routing, "which node is worth one `look_at`" — carries no size or effort signal of any kind.**

**Why it reaches past one field.** `domain-design.md §10.5` names the risk the whole inbound reframe takes: "§6's own stated failure mode is 'everything lands in free text… the KB **degrades into a note pile**.' The reframe walks into that deliberately. **The only thing separating a designed KB from a note pile is that the small allocation layer stays populated.**" That layer has since lost `workload`, `status`, `manifest`, `offering_term`, `prereq`, `count`, per-part scores and `notes`.

**No record places the 08-23 ruling and the 08-28 ruling side by side.** They live in different record sets and were surveyed separately.

**The question, in three cheap parts.** (a) Does anything read size today? (b) If not, is `grade_share`'s exemption reason still true as written? (c) Is "faithfulness" a guard against the same failure the missing-rate guarded, or a different one?

### E5. "The current plan" has no representation anywhere

**Side A — 2026-08-21, `domain-design.md §9.1`.** "The projection carries every course's **obligations, time-points and the current plan**, with no free text." And `§9.3`: the coordinator does "**plan generation — its only substantive work, because it *is* coordination.**"

**Side B — 2026-08-28, `ring-0.md §7`.** "`time_point` and 'the current plan', both named by `domain-design.md §9.1` as part of the projection. `time_point` is not in slice 1; **the plan has no representation anywhere**, and this record does not invent one."

**What turns on it.** `time_point` is a clean deferral with a stated reason. **The plan is different**: it is the coordinator's only output, one of three things the projection was ruled to carry, and no kind, field or link represents it. `model.md §7`'s retraction of the hold-the-whole-skeleton draft rests on the entity list `obligations · time-points · plan` surviving — so a third of what survived does not exist.

**It also breaks a test.** Ring 0's membership test is "does it change **the plan's shape**". `findings/read-cycle.md §4` ran that test and returned nothing. It was measuring against an object with no representation.

**The question.** Is a plan a stored thing or a generated one? If stored, it is a kind and nothing has designed it. If generated per read, `§9.1`'s "the projection carries the plan" needs restating, because a generated plan is not something a projection carries.

---

## Group 3 — Facts the system does not have: asking, and self-contradiction

Both are about origins for facts nothing currently produces. Both are loosened by E7's ruling, since surfacing is now **pull**, not push — but neither is settled by it.

### E12. When does the system ask about progress?

**Side A — Billy, ruled 2026-08-23, `[R]`, `domain-design.md §9.6`, verbatim.**

> "假如需要判断的时候再问...**让系统从 waiting for input 变为 asking for input**...前者要求你 proactively provide input，但我自己都忘记了怎么可能 provide。"

The class it creates: "facts with no generating event — origin Billy himself, capture point **at the READ — the system ASKS**. The third class is self-authored but not durable: **progress**, difficulty, how much load a week already carries. A deadline is generated when the professor posts it; **a progress state is generated by nothing**, so **forgetting to supply it is structural rather than a lapse.**"

Its own governor, same block: "**only ask what changes a decision.** Left ungoverned this degenerates into an interrogation — one blind run alone produced about nine askable items. **The gate that decides what belongs in the observation space and the gate that decides what is worth asking are the same gate.**"

**Side B — Billy, 2026-08-27, `[R]`, `architecture.md §3`, first person.** "**The system must not chase the agent.** *'The system is designed to help me, not to raise questions, conflicts or concerns that no one will ever care about in daily usage.'*"

**Side B′ — Billy, 2026-08-28, `schema.md §4.5`.** Applying B to remove an occasion to ask about exactly A's example: "a nullable state would make the system **announce it does not know and give an agent a reason to ask *have you started this yet***, which `architecture.md §3` rules a defect in the rule." Therefore `progress.state` is **not nullable** and absence reads as `not_started`.

**What turns on it.** A's canonical example is **progress**. B′'s canonical application is **progress**. A says the system must ask because forgetting is structural; B′ removes the mechanism that would prompt the ask. A's own governor is the intended reconciliation and **neither record invokes it against the other**. Downstream: `schema.md §4.5`'s "only the owner authors it" is enforced "**nowhere, deliberately**", so nothing today either asks or prevents asking.

**Recency favours B′ by five days, but they are about different objects** — a capture-point policy and a field's nullability.

**The question.** Three positions are consistent with the record: (i) never unprompted, `not_started` is the answer and A's third class is served some other way; (ii) at the read, governed by A's own gate, which needs something other than a nullable field to trigger it; (iii) A is about *difficulty and load* while B′ is about *state*, in which case A's third class survives minus its headline example.

### E11. The latent sticky note — an origin nothing detects

**The finding, `[A1]`, 2026-08-22, recorded by its author as unclaimed.**

> The two real contradictions in A1's slice — a deck and its handout disagreeing about which assignment a tutorial covers — **arrived with the original material**. "Nothing was delivered; the conflict is inert until someone reads both documents in the same sitting … This is a **third origin for a sticky note** beyond 'a correction arrives' and 'Billy states one' — ***the corpus disagrees with itself*** — and **it is the one that most directly serves ruling 4's third job** … **It is also the one nothing in MODEL detects.** I am not proposing a mechanism; I am recording that the class exists and is populated."

**A fourth origin, `[B2]`.** Two of its five sticky notes are "corrections **the author shipped inside the artifact**". "The sticky note is not only an inbound-correction mechanism."

**What happened to them.** `derivation/FINDINGS.md` records A1's **count** ("2 latent") and not the **class**. No fall26 record names either origin.

**Why it is worth your eye now.** E7's ruling makes the third job — "locate details Billy himself does not know about" — a **pull** operation, and `nodes_without` implements one form of it. A latent contradiction is a different form: it is not a missing edge, it is two documents that disagree, and no set-difference query finds it.

**The question.** Are latent contradictions in scope, and if so does anything create the notes? The corpus has three note origins with mechanisms and one without.

---

## Group 4 — The store: what gets kept, and what happens when two things disagree

### E10. What goes into the searchable store, and what it means to leave something out

**The setup, in plain terms.** Course material comes in as files. Some of it gets turned into searchable text so the system can find things in it later. Some of it does not.

**Your rule, 2026-08-22, `domain-design.md §10.7` ruling 3.** Decide by the *kind of file*:

> "**RAG stores `slides / pdf / textbook`-class sources.** Handwritten tutorial notes are excluded, not embedded, **effectively treated as absent**."

The agent note attached to it already wobbles: they fail "on **density and redundancy, not on volatility**", but "**the source-class rule is the operative one**."

**The problem, measured the same day, `derivation/FINDINGS.md §4.1`.** File type does not predict what you get. Four counterexamples in one slice:

- a PDF that is just scanned handwriting
- a text PDF whose exercises are **pictures**, so one file is readable in parts and not in others
- a `.png` holding a clean block of prose, more usable than several PDFs
- one diagram stored twice, as `.drawio` and as `.png`

The conclusion: "**The real axis is whether meaning survives linearization**" — plain version: *does this thing still make sense once it has been flattened into a string of text?* You find that out by trying, not by looking at the extension. It is a property of the extraction pass, not of the file.

**How big the excluded pile is.** 2c03's tutorial notes are handwritten scans yielding about **23 usable characters per page**. Two more agents found the same in two more courses. So image-only material is "**a whole class in a core course rather than the edge case**". And separately: your **densest hand-written concept links live in exactly that handwritten material** (the ink annotation on TUT7, group 6 item d).

One more line from that finding, which is a requirement rather than an observation: "**a silent empty index entry is not deferrable, because it makes the corpus lie about its own coverage.**" Plain version: if a file goes in and yields nothing, the system must say so. A blank entry that looks like a real one is worse than no entry.

**Why recency does not help.** All three are 2026-08-22. Yours is a real `[R]`.

**The question, two halves.**

1. Does the file-type rule survive, given that file type was falsified as a predictor the same day?
2. Does "excluded" mean **not searchable** or **not kept at all**? You wrote "effectively treated as absent". But `text_extractable` already exists as a per-region flag, which would let handwritten material be **kept and marked as unsearchable** instead of dropped. Under that reading the two positions may not conflict at all.

---

### E4. When two notices disagree, who resolves it and when

**The setup, in plain terms.** An announcement says an assignment is due Wednesday. A later announcement says it moved to Friday. Two ways to handle that:

- **Fix it on the way in.** When the second notice arrives, update the record. Now there is one answer: Friday.
- **Keep both and sort it out later.** Store both, tag them, and let the model work out which is current at the moment someone asks.

The corpus took the second.

**The objection, 2026-08-21, quoted verbatim in two independent documents.** Keeping both leaves "due Wednesday" and "moved to Friday" coexisting for the model to reconcile at read time, which

> "***relocates Billy's uncertainty into the system while making it look handled***."

Plain version: **you still do not know which one is right. But now it looks like the system does.** That is worse than knowing you do not know, because you stop checking.

**Both places that quote it say do not skip it.**

> "The agent's position is that this holds for an unbounded pile and fails for a scoped, time-ordered set. **Answer it or accept the risk explicitly; do not pass over it.**"

> "**that is an assertion, not a design**, and it is the reason the allocation layer cannot shrink to zero." Named "**the entry point for the next design round**."

**Where it stands now.** The model this objection was defending is dead: measured, 39% reduction, and the bias was deliberately set against the convenient answer. **But the objection outlived the thing it was arguing for.** Six days of spec work (08-23 to 08-28) never touched it. Nothing in `records/spec/` addresses read-time reconciliation at all. And the ruling that replaced the old model, "inbound arrives to be known", walks straight into the failure the objection named, with `§10.5` saying so in place.

**There is no other side here.** Not two rulings disagreeing. One question, asked twice, answered zero times, and it went quiet rather than getting settled.

**The question.** The corpus's own instruction, unchanged: **answer it, or write down that you accept the risk and why.** Both are legitimate. Silence is the one option that is not.

---

## Group 5 — Is the structural model right, and can it still be checked?

### E8. "What is week 7 about" does not work for every course

**The setup, in plain terms.** You use "what is week 7 about" as the sentence that describes what this product does. It holds the surrounding context and hands you the picture without a reload.

**It works for one course and not the other, and this was measured.** `model.md §9`:

> 687 KB of 2aa4 lecture text contains **zero** occurrences of "Week N", and the course has no announcement stream. Its lecture layer is "**genuinely timeless**."

So for 2aa4, "what is week 7 about" is **unanswerable from the lecture material**. "What is topic X about" answers fine. 2c03 organises by week; 2aa4 organises by module. **The sentence you use to describe the product fails on one of the two courses you actually read.**

**Someone proposed the fix and it vanished.** An agent proposed: let each course carry its own name for its chunks — week for 2c03, module for 2aa4 — and make the chunk itself the primary handle everywhere. Plus a `lecture_date` field, which for 2aa4 is "the **only** ordering signal that exists." **Neither shows up in any adopted, cut or watch list. No reason was recorded.** It was not rejected. It was dropped.

**The spec never mentions it.** No record in `records/spec/` names a chunk, a module, a week or a navigational handle.

**What is not in question.** The rule forbidding a `week` field is intact and correct: "`week` is a retrieval term, and 2px3 organises by week while other courses organise by topic. **Hardcoding either is the failure.**" That is not what this asks.

**The question.** A course groups its material into chunks, and each course calls its chunks something different. Is *that label* a real modelled property, a display convention, or nothing? **Today it is nothing.**

---

### E3. The main hypothesis has one test, and a later ruling made it impossible to run

**The setup, in plain terms.** H1 is the bet the whole node-and-edge model rests on: **different kinds of course need different amounts of structure in different layers.** The way to break it: find a course that needs a node kind or an edge kind the others do not.

**The test course was named and then never run.** 2px3. Described in the origin cycle as the **`woven` profile, "the hardest case routing must survive."** Excluded from every run so far. `model.md`'s own header says H1 is "**gated on slice 2 running the extractor on 2px3**", and the derivation says "H1 now rests on **two courses of the same shape**."

(H3, the other one, is about whether the system can work out a course's structure when the course does not state it. Both courses stated theirs, so it was never exercised. Its fallback is stated and cheap, so H3 untested is a precision risk, not a structural one. H1 is the one that matters here.)

**Your 08-28 ruling, `architecture.md §4`, which is sound on its own terms.**

> "**extracting the other three courses is not worth doing before the presentation tier exists.** Every contested field needs a write rule, and a write rule is derived from what a value must be for a node to render well. **Reading three more courses without those rules produces three more courses of noise and does not produce the rules.**"

**What happened.** The gate said "H1 is untested until 2px3 is read." The later ruling said "do not read more courses yet." **Neither ruling mentions the other.** Nobody decided to leave the model's main hypothesis untestable. It fell out of two reasonable rulings passing in the dark.

**The question.** Is H1 still gated, and on what? Three options exist in the corpus, none chosen:

1. Accept H1 on two courses and write down the exposure.
2. Keep the gate, and accept the model is provisional until the presentation tier exists.
3. **Read 2px3 for structure only** — just "does it need a kind or an edge we do not have" — without extracting any records. This is a much cheaper act than the one you ruled out, and **your ruling does not address it.** It produces no records, so it cannot produce noise.

---

## Group 6 — Four things that need writing down, not deciding

### E9. Findings that were dropped, and will be silently re-decided by whoever builds slice 2

Each of these is a case where an agent found something real, and the summary that followed lost it or overrode it. **None of them needs an answer now.** They need to exist as open items before slice 2 starts, because otherwise whoever builds it will hit each one and quietly decide it alone.

**(a) "No file on disk" and "never existed" look the same.**

You ruled 08-22 that an artifact needs no URL and no `present` flag: absence is not a field, it is the absence of content in the store, found by a join. That answers the question that was asked.

It does not answer the one that was not: **Midterm 2 is a graded obligation, with a released grade, and literally zero files on disk.** Plus ~13 `referenced_only` cases in 2c03 (mentioned somewhere but never downloaded). An agent wrote the query that would separate these: *"obligations whose posted solutions I never downloaded."* It "would have flagged all seven missing test-script zips and both midterm solution sets."

**The field question was put to you. The can-you-tell-them-apart question never was.**

**(b) An edge type passed the bar and then disappeared.**

`answers` (a tutorial answers a question set): 6 real instances, and a nameable query, "which tutorials have I never worked through". The stated bar was ≥3 instances plus a nameable query. It cleared it. Then it appears in **no adopted list, no cut list, no watch list**.

Two sibling edges also vanished, but their disappearance is explained: they survive as part of the `locator` payload, and the counts add up exactly. `answers` has no such explanation. It was not rejected. It went missing.

**(c) Concept granularity.** *You noted 2026-08-29 that this was ruled and the write rules cover it. Verify at source before treating it as open; it is listed only so it does not vanish twice.*

**(d) You author concept links by hand, in the middle of the semester.**

The original draft said the structure is authored by you once at course setup. That was retracted, correctly: at setup you do not know the structure yet.

But an agent found the positive half, and only the retraction survived: **you author them by hand, unprompted, mid-semester.** Evidence, in two different forms: an ink annotation on TUT7 reading "This question tests: ① MAD compression ② linear probing insertion ③ probe counting" — **on a page with no text layer at all** — and the mid-semester folder renames. "The same behaviour in two modalities."

**"Not at setup" is not "not by Billy."** Nothing in the design accounts for you doing this mid-semester.

Related and unaddressed: "One clause in a tutorial handout creates **9** `requires` edges; one slide in a review deck creates **26** … **an edge is only as current as its sentence, and that sentence's document is dated 2025.**"

---

## Group 7 — Waiting on the world

### What must be in the agent's context before it decides anything? (issue #7)

**Blocked on [#8](https://github.com/Billy423/semester-manager/issues/8)**, the by-hand observation, which waits for the first real decision of the fall 2026 semester. As of 2026-08-29 there are none.

Two things found today should be carried in when it unblocks:

**The test may already be written.** `domain-design.md §9.2` contains this, marked as an **agent formulation that was never separately ruled**:

> "*an observation earns its place if and only if a judgment demonstrably changes when it is present.*"

Plain version: **a field belongs in the window only if taking it away changes what you decide.** That is the ablation experiment, stated as a rule, six days ago, by an agent, and never approved. When #8 lands, #7 may be a ruling on this one sentence rather than an invention.

**E7's ruling makes the answer smaller.** If typed traversal reaches context deterministically, then what has to be sitting in the window is only **enough to know where to start looking**, not everything needed to decide. That is a much smaller set, and it finally makes ring 0's declared job — routing, "which node is worth one `look_at`" — coherent with everything else.

**And it is exactly what E2 tests.** Routing means choosing what to look at next. Right now ring 0 carries no signal for how big or how heavy anything is. Either that absence changes a decision, or size was never needed in the window at all.
