# Classification - Cluster D: the observation contract (ring 0, residency, the coordinator)

**Proposals only. Nothing here is created.** 15 inventory things (M66-M80) plus one thing my cluster carries that has no M-number (**M75b, the plan**). Classified against cluster B's term list, which owns the vocabulary spine.

**The correction this cluster runs under, restated so every entry below can cite it.** Lifetime is two questions:

- **the code process** is per-invocation - `design.md §5` conclusion 1, measured at 52 KB / 0.27 ms, "per-invocation and resident are indistinguishable";
- **the agent conversation** is long-running, days to weeks, and it survives into the successor as an interactive Claude Code session.

So `ring-0.md §7`'s *"ring 0 is resident for the coordinator and for nobody else"* means **held in the conversation's context**, not held in a process's memory. **A, B and C never conflicted. E1 as posed is void**, and with it the inventory's conclusion that `findings/read-cycle.md §4`'s null result becomes admissible: the successor's conversation is long-running, so `ring-0.md §2`'s refusal of that null stands. Every `⟂container` mark in this cluster that rests on "a per-invocation agent has no context between calls" is **void** and is named as such where it appears.

**What survives of E1** is a different question - *what must be in the agent's context before it decides anything?* - already tracked as **issue #7**, blocked on **issue #8** (the first real decision of fall 2026). **Nothing below answers it.** Six things route around it; each says how.

**Three things I found at source that the inventory does not have.** All three are 2026-08-29 and postdate it:

1. **Billy, 08-29: "ring 0 governs *residency*, not *readability*."** (`evidence/2026-08-29-course-level/NOTES.md` §2 round 4, landed as `63612df`.) `parts` returns with any read of the obligation record; excluded-from-the-projection is not unreadable. This is a ruled clarification of M66 and it closes an agent error that ran two rounds.
2. **Billy, 08-29: `look_at(course)` is a call the coordinator makes** (same file, round 3). "The coordinator must be able to see what a course is, or plan generation is blind." `domain-design.md §9.3`'s *"no corpus retrieval, no file reads, no fact writes"* is a purity restriction **on materials**, not an enumeration of the coordinator's reads. This corrects how M75 has been read.
3. **The ~55-obligation figure is not derived from disposability.** `design.md §8` states it independently as the corpus's own sizing number - *"the only sizing number that matters is that ring 0 for five courses is roughly 55 obligations"* - and §6 lists "whether residency still holds at five courses (~55 obligations, versus the 14 rows every read-side measurement was taken over)" as a revisit condition. `ring-0.md §1` credits it to `domain-design.md §9.5`, but §9.5 supplies only the *shape* of the bound ("one projection read"), never the number. **This resolves cluster A's worry on M11** - see the cross-cluster note under M67.

---

## M66. What ring 0 IS

**Destination: `CONTEXT`.**

The decision half of this thing is already cluster B's **M32** (*exactly two persisted things; ring 0 is not a third*). What is left here is a name three records state in near-identical words, plus a job description. That is glossary work, and the split is the same one B made between M13 (the names) and M32 (the ruling).

**Proposed term.**

| term | definition | _Avoid_ |
|---|---|---|
| **ring 0** | The obligation layer under a residency policy: the fixed-shape, uniform-depth set of obligation fields the coordinator holds in its conversation context so it can tell where to look next. It governs **residency, not readability**, and is not a third persisted thing. | *the projection* (bare - three different projections are in play; see the collision note) · *the obligation layer* used as a synonym (that is the persisted layer, ring 0 is a policy over it) · *the resident projection* as a name · ring 0 meaning **what is observable** (ruled against, Billy 08-23) · ring 0 meaning **what is readable** (ruled against, Billy 08-29) |

**Compatible with B's M32, and I confirm M32 is right.** `schema.md §3`, `design.md §3.0` and `ring-0.md §1` all say "not a separate store: residency is an access policy over `obligation` nodes", in three records with no drift. B's definition needs one addition it could not have: **`ring 0` is a policy over *obligation nodes' fields*, not over whole nodes** - `ring-0.md §4` admits seven of an obligation's fields and excludes `parts` and `grade_share` from the same node. "Access policy over `obligation` nodes" reads as node-grained and is field-grained.

**On the domain-side objection** (`domain-design.md §9`, Billy 08-23: §9.1 never says "ring 0", and the subtraction gloss is a later paraphrase): it holds as a fact about §9.1 and is answered anyway, because the spec tier states the equation as its own claim rather than as a reading of §9.1. Do not repair it by editing history; the ADR-free term above simply does not depend on the paraphrase.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 8 - "week N as a node joined by edges is not right modelling", and query-by-time-period "would relate to the skeleton's nodes the way ring 0 does". That analogy makes ring 0 a *kind of thing* (a typed access policy over a layer) rather than a one-off, which is a reason to define it as a policy and not as a field list.

**Merge candidates.** B's **M32** - same subject, different trade-off (M32 rules the store count; this names the thing). Do not merge; M32 should cite this term rather than restate it. Cluster A's **M6** is a *different* trade-off again (what quantity the size gate budgets).

**Depends on the open context question.** **No** for the definition; **yes** for the contents. Issue #7 can change which fields are in ring 0 without touching what ring 0 *is*, which is exactly why the definition is safe to write now.

**Cross-cluster.** B **M13**, B **M32** (both aimed here, both answered above). B's `obligation` layer definition already says "the same nodes ring 0 is a projection of" and is compatible.

**Zoomed.** Yes - `ring-0.md` in full, `domain-design.md §9`/§9.1, `model.md §7`, `schema.md §9`. Changed one thing: the field-grain correction to B's M32 wording.

---

## M67. Ring 0's field set - the two bands' contents

**Destination: `ADR`.**

**Proposed title.** *Ring 0 carries seven routing fields; `parts` and `grade_share` are excluded, and `grade_share`'s exclusion is measured rather than argued.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** Every render, every band rule and the whole "what is at a glance" surface is downstream. Four earlier grains exist and three of them name fields the graveyard now forbids - re-cutting the grain has cost the project a full cycle each time. |
| Surprising without context | **Yes**, twice. A planning system that omits **grade weight** from the view its planner sees reads as an oversight; and the set includes **`has-more`**, a field nothing writes and no other record declares. |
| A real trade-off | **Yes.** `grade_share` was in two of the four earlier grains and its removal is against the intuitive design; it is excluded on a count (29 of 77 unsupported-or-contradicted claims, 38% of every measured faithfulness failure) plus a corpus argument that needs no measurement (2c03's column sums to 95, the missing 5% has no row, two 1% rows are bonuses outside the 100 - so a rendered column reads as a partition it is not). |

**Body.** Ring 0 carries `course`, `name`, `due`, `state`, `optional`, `done_by` and `has-more`; band B drops the last three. `parts` and `grade_share`/`grade_share_conditional` are out of the projection in both bands - `parts` because it answers *what is this about* rather than *where do I look next*, `grade_share` because a rendered column of shares reads as a partition of the grade that it is not, which is the single largest measured faithfulness defect in the corpus. **Excluded from the projection is not unreadable**: ring 0 governs residency, and `parts` comes back with any read of the obligation record.

**Shape riding inside.**

| field | band A "active" | band B "known" |
|---|---|---|
| `course` · `name` · `due` · `state` | ✅ | ✅ |
| `optional` · `done_by` · `has-more` | ✅ | ❌ |
| `parts` · `grade_share` · `grade_share_conditional` | ❌ | ❌ |

**Carve-out that must ride with it: `has-more` is declared and undecided.** `ring-0.md §4` admits it and says so - "the only one here that no record has yet declared", "nothing writes it yet", and whether it is a boolean, a count or a set of present link kinds is open. Its motivation is measured (6 of 14 obligations carry an annotation, 8 carry none, so a `look_at` returns nothing new on more than half the rows). The 08-29 cycle carried it as mandate item C and did **not** produce a verdict. If reconciliation prefers one-destination-per-thing strictly, split `has-more`'s shape out as its own deferral; I keep it here because the field's *presence* in the set is what this ADR rules and its *shape* is a build detail.

**Sequencing stripped.** Two. (a) `schema.md §9` item 4 still lists "a projection grain, **owed to slice 4**" and does not cite `ring-0.md`, written the next day and exactly that grain - C55, a bookkeeping residual, not carried. (b) `ring-0.md`'s "It supersedes nothing; it answers what §9.1 left open" is positioning, not content.

**Touched by Billy's rulings.** Heavily. **Ruling 2** is the sharpest: `hours_estimate` is not quantifiable, size is judged from progress and load, and *the work need not be a functional one-pass - the agent sees the skeleton and ring 0, notices, and asks when needed.* **Ring 0's declared job is routing, and this field set carries no size or effort signal of any kind.** Ruling 2 makes that survivable (the agent asks) and simultaneously makes it the thing to watch (ask-frequency is the eval item). **Ruling 1** keeps `offering_term`/`prereq` graveyarded, which is why no scope field appears. **Ruling 3** is why no `time_point` and no plan field appears.

**Merge candidates.** **None to merge.** Cluster C's `grade_share` exemption (M47) is the *same subject and a different trade-off* - C's is exemption from the rigidity rule on "no reader"; this one is exclusion from a projection on a measured defect. They must both exist and each should cite the other. Flag, do not merge.

**Depends on the open context question.** **Yes, directly.** #7 asks what must be in the window; this is the current answer, produced by an unruled test (M68). Route-around: the ADR records **the set and its per-field reasons**, and explicitly does **not** record the test that generated it. If #7 revises membership, the per-field reasons survive as the evidence a revision argues against.

**Cross-cluster.** **Cluster A's M11.** A routed disposability `DROP` and warned that D would then carry the ~55-obligation size bound with its stated derivation removed. **It does not: the number is stated independently at `design.md §8` and §6 as the corpus's own sizing figure, and §9.5 only supplies the bound's shape.** So A's DROP does not orphan the number - but see M73, where I do dispute A's DROP on other grounds. Cluster C owns `grade_share`, `done_by`, `optional`, `state`, `parts` at field grain; this ADR must cite C's field definitions, not restate them.

**Zoomed.** Yes - `ring-0.md §4`, §6; `schema.md §9`; `design.md §5`, §6, §8; `evidence/2026-08-29-course-level/NOTES.md`. Changed the call on the size bound's provenance.

---

## M68. The membership test

**Destination: `DEFER`** - and **do not create a new issue**. This is already tracked as **issue #7**, *what must be in the agent's context before it decides anything?*, blocked on **issue #8**. Reconciliation should attach this thing's material to #7 rather than open a second ticket.

**The wake-up precondition.** Issue #8 lands - the by-hand observation, waiting on the first real decision of the fall 2026 semester. As of 2026-08-29 there are none.

**What must be carried into #7 when it wakes.**

1. **The test may already be written.** `domain-design.md §9.2`: *"an observation earns its place if and only if a judgment demonstrably changes when it is present"* - marked **agent formulation, obtained by lifting the rigidity rule one level, not separately ruled**. When #8 lands, #7 may be a ruling on this one sentence rather than an invention.
2. **The competing test is also unruled.** `ring-0.md §2`: *"a field belongs in ring 0 if and only if, without it, the coordinator cannot decide where to look next"* - agent-drafted per the changelog, and it declines the §9.2 test. **Both are agent formulations and neither is ruled.** That is the merge finding neither survey could make and it is the reason this defers rather than lands.
3. **The null result stays refused, and now on two independent grounds.** `findings/read-cycle.md §4` reported `parts`, `grade_share`, the skeleton, a complete ring 0 and `progress` as each read, each rendered, none changing the plan's shape. **Ground one, and it survives the correction:** the runs were memoryless `claude -p` cold starts and the design's *conversation* is long-running, which the successor container also is - so the instrument mismatch is real, not an artifact of the old container. **Ground two, which the inventory does not carry and which needs no lifetime argument at all:** `evidence/2026-08-23-read-cycle/PROVENANCE.md` records that the fixture is written to a dead schema (`status`, `workload`, `count`, `manifest`, `offering_term`, `prereq` - all graveyarded) and that **three of its six launch-shaped values are synthesized rather than observed**, after 2aa4's Avenue page was deleted. Add the single fixed prompt and the two same-shape courses and the null is uninformative on its face.
4. **`ring-0.md §2`'s routing test is unmeasured**, and the 08-29 cycle's own hand-off note says so (`NOTES.md` §5: "agent-drafted and unmeasured, and §2 says so").
5. **E7's ruling shrinks the answer.** If typed traversal reaches context deterministically, what must be resident is only enough to know **where to start**, not everything needed to decide - which is what makes ring 0's declared routing job coherent.
6. **Ruling 2 names what #7's answer will be tested against**: ask-frequency. If the agent must ask constantly, either something needs persisting or the design has a seam.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 2 (above). Ruling 9's hypothesis gate is the general form of why this cannot land now.

**Merge candidates.** **None, and one explicit anti-merge.** Cluster B's M26 is right: **the rigidity rule is a different test** - it asks whether a field exists at all, this asks whether an existing field must be in the window. §9.2 obtained this "by lifting the rigidity rule one level", which is a genealogy, not an identity. **Must not merge.**

**Depends on the open context question.** **It is the open context question.**

**Cross-cluster.** B **M26** (anti-merge, honoured). B **M32** (whatever #7 answers, ring 0 stays not-separately-persisted). A **M11** - A observes that E1 blocked the observation contract; under the correction it does not, and only this narrower question does.

**Zoomed.** Yes - `ring-0.md §2`, `domain-design.md §9.2`, `evidence/2026-08-23-read-cycle/PROVENANCE.md`, `evidence/2026-08-29-course-level/NOTES.md` §5, `06-escalations-for-billy.md` issue #7. The fixture provenance is new and changes the strength of the deferral.

---

## M69. The symmetry rule

**Destination: `ADR`.**

**Proposed title.** *The observation invariant is symmetry, not shallowness, and it is scoped to the set the judgment ranges over.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** It decides what a judgment may look at, which every read path and every render is built against; and it has already been reversed once, at the cost of a cycle. |
| Surprising without context | **Yes.** The corpus's earlier and more intuitive rule - *allocation reads ring 0 only* - is still written down in several places, struck through in one. A reader will meet the dead rule before the live one. |
| A real trade-off | **Yes.** "Uniformly shallow" was ruled, implemented and measured. It lost to evidence: the blind run gave the planner deadlines and weights alone and it produced a date-ordered queue, "which says more about the observation space than about ring 0". The invariant was never shallowness; it is uniformity, and the hazard is **path-dependent** depth, not depth. |

**Body.** Observe anything you can afford for every course at once; never observe anything you can only afford for one - the second case is `dispatch`'s entrance, and its result must come back in the same shape as the other four. Asymmetry that comes from the material is legitimate; asymmetry that comes from interaction history is not. **Symmetry is scoped to the set the judgment ranges over**, not unconditionally to all five courses.

**Shape riding inside.**

```
observe(X) is permitted for a judgment over set S
  iff  X is affordable for every member of S
  else dispatch(X, member) -> a value in the same shape as every other member's
```

**Two limits that must ride with it, both on the record.** (a) §9.2's premise that a thin line drives an estimate request is **untested** - "neither supported nor refuted"; one instance of the predicted shape appeared in 1 run of 3. (b) **Affordability is load-bearing and its bound is unwritten** - `model.md §10.5`, widened 08-24 to cover `label` as well as sticky notes: eight one-line summaries can be pulled for a comparison set, eight paragraphs cannot. **And that bound's own evidence was voided on 2026-08-29**: Billy ruled the corpus is evidence about what the material contains, not about what a record should look like, so the character counts cannot issue the bound - it comes down from affordability instead.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** **Ruling 2** - the dispatch escape is how a size judgment gets made without a size field; "the agent notices and asks when needed" is the human-facing form of the same escape. **Ruling 8** - the time projection would relate to the skeleton the way ring 0 does, so whatever set a time query ranges over is a *different* S and the scoping clause is what makes that legal.

**Merge candidates.** **M70** shares this rule's *consequence* (the grouping key is a parameter because symmetry is scoped) but not its trade-off. Flag, do not merge - M70 would then have to carry M69's whole reversal history to make sense.

**Depends on the open context question.** **No.** Symmetry constrains what a judgment may observe; #7 asks what must be resident before judging. The 08-23 ruling explicitly separates them: *"ring 0 returns to being the layer that is RESIDENT, not the definition of what is observable."* That sentence is what lets this ADR stand while #7 is open, and it belongs in the body.

**Cross-cluster.** Cluster C - the affordability bound is owed and its inputs are the length rules on `sticky_note.body` and `label`. Cluster E - `write-rules.md §4.0`'s render test is what will issue it. Note the corpus-is-not-evidence-about-records ruling (08-29) is an orphan; see `## Orphan rulings`.

**Zoomed.** Yes - `domain-design.md §9.2` in full including the RESTATED block, `model.md §7` mechanism 1 with its REPLACED banner, `ring-0.md §5`, `model.md §10.5`, `evidence/2026-08-29-course-level/NOTES.md` §6.

---

## M70. Grouping and order in the projection

**Destination: `ADR`.**

**Proposed title.** *The projection's order is derived from the material, never from write history.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes** - as stated. The reversible part is which key sorts; the irreversible part is the prohibition on array order, which forbids the free default and constrains every read path that assembles the projection. The record convicts the existing implementation on exactly this. |
| Surprising without context | **Yes.** Array order is the default everywhere and costs nothing, and it was in use; the claim that it is *forbidden* - because insertion order is write history and §9.2 rules out asymmetry from interaction history - is not something a reader derives. Also surprising: `due` and not `min(due, done_by)`. |
| A real trade-off | **Yes.** Three live alternatives, each with a stated loser's case: `min(due, done_by)` (rejected - an obligation due earlier carries the earlier hard deadline even where another is *planned* to finish sooner); nulls first or absent (rejected - nulls last is what gives an undated obligation a defined position, which is the recorded objection to date ordering); a constant grouping key (rejected - symmetry is scoped to the set the judgment ranges over, so *what is due across every course this week* needs a different grouping). |

**Body.** The projection groups by `course` by default and the grouping key is a parameter, because the symmetry rule is scoped to the set the judgment ranges over. Within a group, order by `due` ascending, nulls last; among nulls by `done_by`; ties broken by the handle - **never by file order, because array order is insertion order is write history**. `due` is the primary key, not `min(due, done_by)`: triggering and ordering are different jobs and one field can do the first without the second.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** **Ruling 8** - the cross-course *what is due this week* read is a time-shaped question, and this ADR is where it is legal to ask it (a grouping parameter) rather than where it is answered (not ring 0's responsibility). If B's naming proposal lands, "the time projection" is the thing that would use this parameter, and the two must not grow two mechanisms.

**Merge candidates.** **M69** - shares the scoping clause, different trade-off (see M69). **M71** - shares the record and the subject (both are `ring-0.md`'s partition/ordering) but the trade-offs are unrelated: M71 decides what *counts as active*, this decides what *order things come back in*. Flag both, merge neither.

**Depends on the open context question.** **No.** Ordering is a property of whatever set ends up resident.

**Cross-cluster.** Cluster C owns `due`, `done_by` and the handle/`id`. Cluster F's M101 (addressing at the surface, "every read that returns records must return their handles") is the precondition for a handle tiebreak being usable - this ADR should cite it.

**Zoomed.** Yes - `ring-0.md §5` and its changelog entry (Billy, ruled).

---

## M71. The two bands and the active window

**Destination: `ADR`. Per cluster A's own recommendation, D owns the shape and A's M3 merges into it.**

**Proposed title.** *Active is three independent triggers on one question, not a time window with exceptions.*

| test | verdict |
|---|---|
| Hard to reverse | **Partly, and A named this correctly as the weakest of the three.** The constants are cheap; the *shape* is not - ring 0's band assignments and the whole at-a-glance surface are downstream of it, and `done_by`-as-a-trigger is the one place the anxiety-removal goal reaches the schema. |
| Surprising without context | **Yes.** Two surprises: `state == in_progress` fires with no reference to any date, and a whole-semester question gets the whole semester rather than a helpful narrowing. |
| A real trade-off | **Yes.** The ±1-2 week window was available as a default narrowing from 08-23 and was deliberately **not** applied until Billy stated it as a requirement on 08-28; and `in_progress` was promoted from an exception *inside* the window to a trigger in its own right. |

**Body.** An obligation is in band A if any one of three things holds - `due` in `today-7d .. today+14d`, `done_by` in the same window, or `state == in_progress`; everything else, including obligations with no date, is band B. Breadth is never treated as a defect: a request for a whole semester that gets a whole semester is answering what was asked, and the useful window is a requirement Billy stated rather than a fix the system applies on his behalf. **Two bands do not violate uniform depth**, because the partition is computed from material facts plus one rule applied identically to every course and so carries no interaction history.

**Shape riding inside.**

```
active := due ∈ [today-7d, today+14d]
       OR done_by ∈ [today-7d, today+14d]
       OR state == in_progress
```

**One dependency to state in the body.** An undated obligation lands in band B and that is not a hazard - **and the stated ground is that the system holds no notion of an obligation's importance**, `grade_share` having no reader by standing exemption. If `grade_share` ever gets a reader, this ground disappears and the band rule needs re-arguing.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** **Ruling 3** is adjacent and must not be confused with it: removing the calendar projection and `time_point` does not touch this window, which is a residency band and not a calendar. **Ruling 8** - same distinction, stated from the other side.

**Merge candidates.** **Cluster A's M3 - merge, and D owns the merged ADR.** A proposes exactly this and contributes the clause D could not see (breadth is not a defect; the window is a stated requirement, not a defect the system corrects). That clause is in the body above. **Ship one ADR, not two.** Also: C3 closes cleanly here - S1 found a changelog-only ruling with no body, S2 found the body, nothing is left to escalate.

**Depends on the open context question.** **No.** #7 asks *which fields*; this decides *which rows*. A band assignment is stable under any change to the field set.

**Cross-cluster.** A **M3** (merged, D owns). C **M47** (`grade_share`'s exemption is this rule's stated ground - the dependency must be recorded in both places or a later reader will silently break it). C owns `state`, `due`, `done_by`.

**Zoomed.** Yes - `ring-0.md §3` and its two 08-28 changelog entries (Billy, ruled).

---

## M72. Expansions are discarded, never sedimented

**Destination: `ADR`.** The inventory's `⟂container` note on this thing - *"a per-invocation agent sediments nothing by construction, which makes the mechanism either free or meaningless"* - is **void under the correction**. Sedimentation happens in the **conversation's** context, and the successor's conversation is long-running. This is the clearest case in the cluster of the container change killing a justification while the ruling survives intact.

**Proposed title.** *What is fetched is dropped; depth never comes back into the conversation.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** It is what makes the fixed-shape view possible at all: "the view does not deepen precisely because what is fetched is dropped." Reversing it re-opens uniform depth, the symmetry rule's affordability premise, and the longevity claim together. |
| Surprising without context | **Yes.** Keeping what you already paid to retrieve is the obvious behaviour, and the corpus records that it was **optional** under the earlier design and became **mandatory** only when disclosure went progressive. |
| A real trade-off | **Yes, with the losing case stated:** holding expansions saves refetches. It loses because without discarding, a long-running conversation converges on held-everything **plus** path-dependent bias - "both costs, no benefit". The refetch is the price paid for uniformity. |

**Body.** Depth is added only inside ephemeral contexts and does not come back: what is fetched is rendered, used and dropped, never accumulated into the conversation. The store boundary is the chokepoint for **content**; discard discipline is the chokepoint for **structure**. The rule does not conflict with the symmetry rule - §9.1 governs the view, symmetry governs what a judgment may observe inside its own scope, and those observations are transient.

**The container note that belongs *in* the ADR**, because it is where the container axis is load-bearing: in a Claude Code session the discard is not automatic - compaction is lossy and unpredictable, not a discipline - so the rule becomes a **statement about what the conversation must not be asked to keep**, and the thing that enforces it is the tool's return shape (cluster B's M33), not the agent's restraint.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine directly. Ruling 2's "asks when needed" is adjacent: asking is the mechanism that replaces a sedimented answer.

**Merge candidates.** **M73** - same record, same paragraph in `model.md §7`, and genuinely close. Different trade-off: M73 decides *what is held*, this decides *what happens to what is fetched*. Flag as the strongest merge candidate in the cluster; if reconciliation merges them, the merged ADR must carry both losing cases (hold-the-skeleton, and keep-what-you-fetched) because they are different alternatives.

**Depends on the open context question.** **No**, and deliberately so: the rule constrains what may **accumulate**, not what must be **present**. #7 can answer anything without touching it.

**Cross-cluster.** B **M33** (the return-type enforcement is what makes this checkable rather than hoped-for). A **M6** (the size gate is the reason expansion cost is the quantity that matters, which is why dropping expansions is not wasteful).

**Zoomed.** Yes - `domain-design.md §9.1` including the 08-24 `[R]` block, `model.md §7` mechanism 2, `ring-0.md §1`.

---

## M73. Progressive disclosure, and what the coordinator holds resident

**Destination: `ADR`.**

**Proposed title.** *The coordinator holds ring 0 in its context and queries the skeleton on demand; it never holds the skeleton, and nothing else is resident.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** Every other mechanism in this cluster is built on it - the discard rule, the symmetry rule's affordability, the size bound, the whole depth-on-demand read path. |
| Surprising without context | **Yes**, and the corpus proves it: an agent draft had the coordinator holding the whole skeleton resident, it was **retracted** by Billy on 08-22, and the retraction records the exact reasoning slip - "a node's summary *can be called*" was elaborated into "*is permanently held*", which the design never said. A second agent made a related error over two rounds on 08-29. A reader will make it a third time without this written down. |
| A real trade-off | **Yes.** Hold-the-skeleton was live and had a real case (no fetch latency, no refetch). It lost because what has been expanded then depends on what was asked, which is path-dependent depth - the exact failure mode uniformity exists to prevent. |

**Body.** The coordinator holds ring 0 in its conversation context and **queries** the skeleton on demand; it does not hold the skeleton. Its persistent memory holds pointers and summaries, never content, and the view refreshes as facts change but never deepens. **Ring 0 is resident for the coordinator and for nobody else** - a person at the surface holds nothing, which is why the same call is redundant to one reader and the only view of a course to the other. Depth is *just enough to triage, never enough to work*.

**The lifetime clause the ADR must carry verbatim.** **Resident means held in the conversation's context.** The code process is per-invocation and its lifetime is not a deciding fact here (`design.md §5`); the agent conversation is long-running, days to weeks. **Never write "the coordinator's lifetime" without saying which one** - collapsing the two produced a false conflict that stood as the corpus's largest open escalation for a day.

**How this routes around #7.** The ADR carries the **negative and the audience halves** - never the skeleton, nobody else resident - and does **not** carry a membership claim. That is the same move cluster A made on M6 (stripping the residency premise so the gate can stand), applied in the mirror direction: A keeps the gate without residency, D keeps residency without the membership.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** **Ruling 2** - "the agent sees the skeleton and ring 0, notices, and asks when needed" is a ruling *about* what the coordinator holds, and it is the first statement in the corpus that treats **asking** as a legitimate substitute for residency. That belongs in the body. **Ruling 9** - onboarding is undefined (coordinator? dedicated subagent? mechanical script? LLM API?), so the ADR must not assume the coordinator is the only agent in the system.

**Merge candidates.** **M72** (see there - strongest in the cluster). **Cluster A's M6** - same subject, genuinely different trade-off (A: which quantity is budgeted; D: what is held versus queried). **Do not merge**, and A's split recommendation is right: A owns the gate, D owns the structure. **Cluster B's M33** - B says merge in D's favour for the contract; the contract is M75, not this. This one is residency.

**And I dispute cluster A's `DROP` on M11.** A drops disposability as an unruled draft whose content is a general engineering principle. Two objections. (a) **The content is not general once it is stated in the successor's terms**: "nothing of value may live only in the conversation" is a specific, checkable constraint in a container where compaction is routine and unpredictable, and it is the *acceptance criterion* for everything in this ADR. (b) Cluster F's finding is that the container change kills a carrier, not a ruling. My recommendation to reconciliation: **fold M11's residue into this ADR as its acceptance clause** - *any change that makes losing the conversation painful is moving backwards* - rather than dropping it. The ~55 figure does not depend on it either way (see M67).

**Depends on the open context question.** **Yes, and this is the tightest coupling in the cluster.** #7 decides what must be in the window; this decides what may not be. Routed around as described - if reconciliation is uncomfortable, the fallback is `DEFER` onto #7, and that is my least certain call.

**Cross-cluster.** B **M33** (enforcement). A **M6** (the gate), A **M11** (dispute above). F **M107** hands me the one durable clause from its dropped session table - *"just-enough depth: enough to triage, not enough to work"* - and it is in the body above. F **M103** carries the process half of the lifetime correction and this ADR should cite it rather than restate the measurement.

**Zoomed.** Yes - `domain-design.md §9.1`, `model.md §7` including the retraction, `ring-0.md §1` and §7, `design.md §5`, `evidence/2026-08-29-course-level/NOTES.md` §2-§3.

---

## M74. Is the coordinator long-running - and is its lifetime allowed to decide anything?

**Destination: `CONTEXT`.**

**Under the correction there is no conflict left to rule.** Both statements are true about different objects, one day apart: the **code process** is per-invocation (`design.md §5`, measured), the **agent conversation** is long-running (Billy 08-21, restated five times). E1 as posed is void; C58's "needs Billy" verdict is answered, not escalated. What remains is a **word that names two things**, which is glossary work - the same shape as cluster B's M34 (materialization versus ingestion) and B's two `summary` objects.

**Proposed term.**

| term | definition | _Avoid_ |
|---|---|---|
| **coordinator** | The single long-running agent conversation Billy talks to - it holds ring 0, dispatches, walks the graph and writes the plan. It is a **conversation**, not a process: its scale is days to weeks, and every call it makes may run in a new process. | *master session* · *the agent* (bare - the successor has more than one) · *orchestrator* (there is no control relationship) · **"the coordinator's lifetime"** without saying which lifetime - the conversation's, or the process's |

**Why not an ADR.** The decision-shaped half already has a home: `design.md §5` conclusion 1 is cluster **F's M103**, and F carries it with the correction's sentence quoted at source. Writing a second ADR here would restate F's, and the guard clause - *"must not be reintroduced as one"* - is a guard about how to argue, not a decision about what to build. It belongs in the term's `_Avoid_` line, where a reader meets it before making the mistake.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 9 - onboarding's owner is undecided among four candidates, which is a live question about how many long-running conversations there are. The definition above says "the coordinator is one conversation" and must not be read as "there is only one agent".

**Merge candidates.** **F's M103** - not a merge; a citation in each direction. If reconciliation wants the lifetime distinction stated once as a decision rather than twice as a term, M103 is the home and this becomes a pure `_Avoid_` line.

**Depends on the open context question.** **No.** #7 is about window *contents*; this is about what the word names. The relationship runs the other way: getting this term wrong is what made #7 look like a lifetime question in the first place.

**Cross-cluster.** F **M103** (the process half, ADR home). F **M107** (session topology, which uses "session" in a third sense and should be checked against this term). A **M11** (E1's void status changes A's framing - A wrote that E1 "remains open"; it does not, and only #7's narrower form does). **All of clusters A, B and F should be told E1 is void**, because at least A and F reference it as live.

**Zoomed.** Yes - `design.md §5` in full, `domain-design.md §1.11`/§5/§9.1/§9.3/§9.5, `ring-0.md §1`/§2/§7. Confirmed the two records are about different objects and that `design.md §5` says so in its own words.

---

## M75. Who may touch what - the data-flow rule

**Destination: `ADR`.**

**Proposed title.** *Store output enters the coordinator only as a conclusion; the context that produced it is discarded, and who produced it is irrelevant.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** It is the chokepoint the whole purity argument runs through and the stated longevity mechanism - "purity is not fastidiousness, it *is* the longevity mechanism." It also decides the language (cluster F/B: a compiler that can refuse). |
| Surprising without context | **Yes.** The corpus's visible form is an agent-topology table with named subagent roles, and the durable rule is deliberately topology-free. A reader will copy the table and inherit roles the successor container may not have. |
| A real trade-off | **Yes, three formulations, each with its case.** Agent topology (08-21) - concrete, but names roles that do not survive a container change. Data-flow rule (08-22) - survives, but names no enforcer. Tier boundary (08-27) - enforceable by an import test, and it answers "who enforces it" with **nobody, by design**: "the application tier has no surface… a method does not defend itself against a caller that should not have called it." |

**Body.** The invariant is a data-flow rule, not an agent topology: store output enters the coordinator only as a conclusion, the context that produced it is then discarded, and who produced it is irrelevant - a spawned subagent, a session Billy opens himself and a task session are all implementations. The coordinator may not call the store in either mode; **rendering a node's own summary is a skeleton read and is allowed**, otherwise it cannot read or analyse anything.

**The 2026-08-29 correction that must be in the body.** `domain-design.md §9.3`'s *"no corpus retrieval, no file reads, no fact writes"* is a purity restriction **on materials**, and reading it as a complete enumeration of the coordinator's reads is an error Billy has now rejected twice: **`look_at(course)` is a call the coordinator makes, and the coordinator must be able to see what a course is or plan generation is blind.** The general guard from the same sitting is worth one line: *before treating any list as exhaustive, state what question it was written to answer.*

**Sequencing stripped.** The three-column responsibility table's slice and tier assignments; `look_at`'s "not in slice 1".

**Touched by Billy's rulings.** **Ruling 7** - two conflicting statements must never coexist; shallow conflicts the agent may resolve itself but must report afterwards, deeper ones it must ask about first. That is a *data-flow* rule about what comes back from a resolution, and it is the first content this ADR has ever had on the outbound direction. **Ruling 9** - no exposed CLI surface, and "the coordinator" as a product-facing role is undecided.

**Merge candidates.** **Cluster B's M33** - B proposes merging in D's favour for the contract and keeping M33 for the enforcement mechanism. **I accept that split**, with one refinement: M33's sentence *"the coordinator sees what a node IS; it never sees what a node SAYS"* is the cleanest statement of this contract in the corpus and should move into **this** ADR's body, while M33 keeps the two store modes and the return-type argument. **F's M107** depends on this and should cite rather than restate.

**Depends on the open context question.** **No.** It constrains what may *enter* the context, not what must already be in it.

**Cross-cluster.** B **M33** (split above, accepted). F **M107** (the store is the channel - depends on this). F **M97**/M98 (the tier split is the third formulation and its "nobody enforces it, by design" clause is F's to state; this ADR must not contradict it).

**Zoomed.** Yes - `domain-design.md §9.0`/§9.3, `model.md §7`, `architecture.md §1`/§3/§7, `evidence/2026-08-29-course-level/NOTES.md` §2-§3. The 08-29 correction is new and changed how I wrote the body.

---

## M75b. The plan - the coordinator's only substantive output

**Destination: `DEFER`. No M-number in the inventory** - it appears only inside M66's standing, M67's table and C49/E5. Billy's ruling 3 assigns it to this cluster, so I carry it as a thing.

**The gap, stated once.** `domain-design.md §9.1` ruled the projection carries **obligations · time-points · the current plan**; `domain-design.md §9.3` names plan generation the coordinator's **only substantive work, "because it *is* coordination"**; and `model.md §7`'s retraction of the hold-the-whole-skeleton draft rests on that three-entity list surviving. `ring-0.md §7`, 08-28: *"the plan has no representation anywhere, and this record does not invent one."* **Two of the three entities are missing and one of them is the system's only output.** `time_point` is a clean deferral with a stated reason (ruling 3: its reader, the calendar projection, is out). The plan is not.

**The wake-up precondition.** Billy, ruling 3: **the plan is a real requirement but not settleable now** - it needs its own grilling session and **cannot be designed before schema, API and CLI shape settle**. So: schema, API and CLI shape settle → the plan gets its own design sitting. The 08-29 cycle independently placed it the same way and refused to touch it - *"the `plan` boundary inside `domain-design.md` §9 is N+2 and Billy's; deciding it here would let a presentation convenience settle a domain question."*

**What the deferral must carry.** (a) The plan is an **output**, and the corpus has exactly one template for what an output must look like - M78's *"a value in the same shape as the other four"*. (b) It is the one thing whose absence makes ring 0's third entity a fiction; whatever else changes, the entity list must be corrected or filled. (c) Ruling 2 bears on it: if size is judged from progress and load rather than stored, the plan is where that judgment gets written down, or nowhere.

**Sequencing stripped.** "N+2" as a position in a cycle order is dropped; what survives is the **dependency** (after schema, API and CLI shape), which is a real precondition and not an ordering.

**Touched by Billy's rulings.** **Ruling 3** in full. Ruling 2 (above).

**Merge candidates.** **M78** (a shape for returned conclusions) - closely related and **not the same trade-off**: M78 asks what shape *any* returned conclusion must have, this asks what the plan *is*. If the plan is designed first, M78's general answer may fall out of it; if M78 is answered first, the plan inherits a constraint. Flag the ordering, merge neither.

**Depends on the open context question.** **Partly.** If the plan must be in the window in order to be revised, #7 constrains its size and shape. If it is written out and re-read, it does not. That question is downstream of the plan existing at all.

**Cross-cluster.** Cluster C owns `time_point`'s deferral (M60) and should record that the plan's deferral is a **different kind** - C's is "the reader is out", this is "the requirement is real and undesigned". **Flag to reconciliation as an inventory completeness gap**, not just a routing decision.

**Zoomed.** Yes - `domain-design.md §9.1`/§9.3, `ring-0.md §7`, `model.md §7`, `evidence/2026-08-29-course-level/NOTES.md` §1. Confirmed no `plan` field, kind or link exists in `schema.md`.

---

## M76. The walk - `look_at(node_id, question)`

**Destination: `ADR`.**

**Proposed title.** *The coordinator reaches material by walking a node's edges, never by searching the corpus.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** It is what makes the purity cut affordable rather than merely stated: reversing it puts an ANN search on the coordinator's path and the store boundary stops being a boundary. |
| Surprising without context | **Yes.** The obvious way to answer *what does A2 actually ask for* is a corpus search, and the slice-1 apparatus did exactly that. The finding is that **nothing was missing from the model** - the `obligation → artifact (spec, role ∈ {given, owed})` edge already existed, running to roughly 53 instances across two courses; **the operation was wrong**, not the model. |
| A real trade-off | **Yes, with both costs priced.** Walk: deterministic, O(degree), no store, no embeddings, "cheap enough for a whole comparison set". Search: ANN over the store, "affordable once, not eight times". The walk's cost is that it returns nothing where no edge exists - 3 of 22 obligations have no artifact at all, "and that is not a defect: those obligations really are only a name." |

**Body.** When the coordinator needs to know what a node is about, it follows that node's edges and reads its neighbours' definitions; it does not search the corpus. The verb returns no sections, no pages, no paragraph and no chunk even where the underlying data holds them - **the boundary is the tool surface, never self-restraint.** Where no edge exists the walk returns nothing, which is a true answer about the material.

**Two carve-outs the ADR must name rather than settle.** (a) **The return shape is withdrawn, not decided.** Both stated triples are retracted; `schema.md §4.6`'s withdrawal is explicit that the triple "was written for an application-tier verb" and, read as complete, "makes `obligation.parts` look homeless" - with a demonstrated cost, a reader who concluded exactly that. **Where a node's own typed fields arrive is open** and was mandate item E of the 08-29 cycle, which produced no `course-level.md`. (b) **The name is not product-facing.** Ruling 9 leaves verb names undecided; `look_at` is the internal name for the operation, and the operation is what this ADR rules.

**Sequencing stripped.** `design.md §4`'s "no `look_at`" on the slice-1 must-not-build list; `architecture.md §7`'s presentation-tier re-homing is carried as a **tier** fact (it is a composed view, not a primitive), not as a schedule.

**Touched by Billy's rulings.** **Ruling 9** - product-facing verb names undecided, no exposed CLI surface, structure-only reading rejected. **Ruling 8** - a time-shaped query is not this verb's job.

**Merge candidates.** **M77** (the `question` parameter) - same verb, and the parameter is *part of this signature*. Different trade-off: this decides walk-versus-search, M77 decides predict-versus-state-at-call-time. Flag as a plausible merge if reconciliation wants one verb ADR; I keep them apart because M77 defers and this lands.

**Depends on the open context question.** **No**, and it is the thing that makes #7's answer smaller: if typed traversal reaches context deterministically, what must be resident is only enough to know where to start.

**Cross-cluster.** B **M14** (`look_at` returns a summary; `label` versus `summary` stays deferred - and B's finding that only the `artifact` carries a written summary is what makes the walk's one-hop answer work: the obligation has no summary of its own and reaches the `role=given` artifact's). B **M22** (the `spec` link kind is the edge this walks). F **M100** (the grammar: "drilling into a single node is the walk"). Cluster C - `parts` is returned by an ordinary read, not by ring 0, per the 08-29 ruling.

**Zoomed.** Yes - `model.md §7.1` in full, `schema.md §4.6` and its 08-28 changelog entry, `architecture.md §7`, `design.md §4`, `evidence/2026-08-29-course-level/NOTES.md` §1 item E.

---

## M77. The `question` parameter, and its retirement condition

**Destination: `DEFER`.**

**The wake-up precondition.** **A verb surface exists** - that is, the presentation tier is designed and any read verb is actually exposed. Ruling 9 states the gate directly: no exposed CLI surface, product-facing verb names undecided, prompt and docstring work not landed. The parameter is a constraint on a signature that does not exist yet.

**What the deferral must carry.**

- **The ruling, which is durable and must not be lost.** Billy, 08-23: *"预期猜测这个问题，不如 dev 模式让它调用的时候问出这个问题。"* The question is **not to be predicted but stated at call time**, and the parameter is **required so it is enforced at the tool surface rather than requested in a prompt.** That last clause is the same principle as `domain-design.md §9.0` ("purity cannot be maintained by prompt, only by tool surface") and cluster B's M33 (enforced by type, not by restraint) - and the inventory is right that it is the one mechanism that **gains** force in the plugin container, where a tool signature is exactly what the harness enforces.
- **Two honesty caveats recorded at the source, which travel with it.** It **perturbs what it measures** - requiring an agent to say why it is calling makes the call more deliberate; constant across arms, so it does not confound a comparison, "but it must never later be reported as a finding". And it **doubles as a test of read-time filtering**.
- **The retirement condition is Billy's; the threshold is not.** Billy ruled that once summaries answer the questions at some threshold, the parameter retires. The threshold - ≥80% of `look_at` calls having their stated question answered across one full three-run arm, **plus** no new question kind - is an **agent proposal with the number explicitly flagged as arbitrary**, and the agent's own position is that condition (2) matters more than (1). **The number does not survive; condition (2) is a real stopping rule and should be re-proposed when a surface exists.**

**Sequencing stripped, and this is the heaviest strip in the cluster.** "dev 模式", "within the development cycle", "one full three-run arm" are the old app's experiment apparatus, not spec. What is stripped is the *measurement schedule*; what is kept is the *rule* (state the question at the surface) and the *retirement shape* (retire it when it stops surfacing new question kinds).

**Touched by Billy's rulings.** **Ruling 9** in full (this is the gate). **Ruling 2** - "the agent asks when needed" is the same instinct one level up: the system's design preference is for the agent to state what it wants rather than for the system to predict it.

**Merge candidates.** **M76** (see there). **B's M33** - *same trade-off*, at different grain: both are "enforce at a mechanism the agent cannot talk its way past, not in a prompt". If reconciliation wants one enforcement-locus ADR, M33 is its home and this deferral cites it. That is a genuine merge candidate and I flag it as such.

**Depends on the open context question.** **No.**

**Cross-cluster.** B **M33** (merge candidate above). B **M14** (the amendment "*a summary is good iff it answers the question that made the agent look*" is the agent's, unruled, and is the retirement condition's actual subject - B should know its `summary` term has an unruled quality criterion attached). F **M100** (the docstring measurement - rewording one docstring moved a verb's call count from 1 to 9 - is the evidence that prompt-level instruction is unreliable, which is this ruling's ground).

**Zoomed.** Yes - `model.md §7.1` and §4.1 in full. §4.1's two-party split (Billy proposed, the agent amended, only the agent's amendment is unruled) is sharper at source than in the inventory.

---

## M78. A shape for returned conclusions

**Destination: `DEFER`.**

**The wake-up precondition.** **A caller exists.** `architecture.md §7` states it exactly: `land()`'s "signature is determined by the caller above it - what a candidate fact is, what a `Diff` carries, how the conflict question is phrased - and **that caller does not exist**. It is therefore not in the first build." So: the presentation tier gets a confirmation surface, or the plan gets designed (M75b) - either one supplies a caller.

**What the deferral must carry, and one of these is new.**

- **The owed item, unchanged since 08-22.** "*Emit only conclusions* is a promise, not a mechanism, until the return value has a required form." The template is `domain-design.md §9.2`'s dispatch estimate - **a value in the same shape as the other four**.
- **It was extended to the user, ruled.** `domain-design.md §9.6`, Billy 08-23: asking Billy is §9.2's dispatch with the **user** as target instead of a subagent, and **the return contract is unchanged**. So the shape must work for a human answer as well as a subagent's.
- **One instance exists and neither survey connected it to the owed item.** `land(candidates) -> Diff`, outcomes *created · updated · unchanged · **CONFLICT***. "`Diff` is the confirmation surface: the dev-time confirmation toggle reads a `Diff`, and so does the conflict question - one return type serves both." **`Diff` is the only typed return contract in the corpus and it is exactly the template M78 asked for, in the place it matters most.**
- **Ruling 7 gives `Diff`'s CONFLICT outcome content it did not have.** Two conflicting statements must never coexist; shallow conflicts the agent may resolve itself **but must report afterwards**, deeper ones it **must ask about first**. That is a two-outcome split inside CONFLICT - *resolved-and-reported* versus *asked-first* - and it means `Diff` is not a one-shape return but a shape with a branch. **This is the single most actionable thing in my cluster's deferrals** and the write-rules cluster is holding the other half of it.

**Sequencing stripped.** "Not in the first build", "slice 1"; the dependency (the caller must exist) is kept because it is a real precondition, not an ordering.

**Touched by Billy's rulings.** **Ruling 7** in full (above). **Ruling 5** - the risk is repeated asking about small conflicts or persisting them as noise, "wait until it bites", which is a reason this defers rather than lands. **Ruling 4** - `progress.state` defaults to `not_started` precisely so the agent does not keep asking; same instinct, and the reason a CONFLICT branch must not be chatty.

**Merge candidates.** **Cluster E's write-rule things** (B flags M23 → E's M85/M90 as ruling 7's home) - **same trade-off**, seen from the write side. My recommendation: **one ruling, two consequences** - E owns the write rule (when to resolve, when to ask), D owns the return type that carries the answer back. Reconciliation should place them adjacent and cross-cite, and must not let ruling 7 land in two records with two vocabularies. **M75b** - see there.

**Depends on the open context question.** **No.**

**Cross-cluster.** E (ruling 7's write rule - the merge candidate above). B **M32**/M33 (`Diff` is application-tier and its conflict question is a presentation adjudication - the tier facts are F's/B's). **F** - the dev-time confirmation toggle is a container-shaped mechanism and F should say whether it survives.

**Zoomed.** Yes - `model.md §10` item 4, `domain-design.md §9.2`/§9.6, `design.md §3.6`, `architecture.md §7`.

---

## M79. The trust contract owed for generated content

**Destination: `DEFER`.**

**The wake-up precondition, and it is a conjunction.** (a) **`concept` exists** - the contract's motivating case is a proposed concept partition, and nothing generates one yet. (b) **H3 is exercised** - whether a multimodal pass can find a partition when the course does **not** state one. Both of this corpus's courses state their own outline (2c03: every deck's page-2 plan recurring verbatim; 2aa4: `[Module N]` on 27 of 30 title slides plus a written taxonomy), so both results are uninformative - the agents' own words: *"the partition is not induced, it is transcribed, and that is a weaker result than a pass."* **Where a course states its outline the concept layer is extraction, not inference, which correspondingly narrows what this contract has to cover** - so the scope of the deferral cannot be fixed until a course that does not state one is available.

**What the deferral must carry.**

- **The gap, from `model.md §1`:** §2's trust clause covers *completeness of recall over what Billy told it*, and **does not cover content the system generates**. A proposed concept partition was never told to it.
- **The agent's position, "Not yet ruled":** the system proposes a partition, Billy disposes, and a wrong proposal must be cheap - it degrades grouping, never destroys anything. Same asymmetry that made ingest judgment non-load-bearing.
- **It already has a concrete reader.** `text_extractable`'s reading mechanism **is** this contract: distinguishing a **quotation** from a **generated description**. That is not a future dependency - it is a live field whose semantics are undefined until this lands. Cluster B's M38 flag is correct and this is the strongest reason not to drop the item.

**Sequencing stripped.** "`concept` is slice 2" and "the spec side is silent" - both ordering. What survives is the real dependency (the kind must exist).

**Touched by Billy's rulings.** **Ruling 6** - the determinant for RAG inclusion is the **nature of the store**: semantic, decontextualized facts about course materials, whatever the artifact's form. That is an *inclusion* rule and this is a *trust* rule, and the two touch at exactly one point: a materialized summary is generated content that lands in a store defined as holding facts **about** materials. **Ruling 7** - two conflicting statements must never coexist, which applies to a generated description that contradicts a quotation from the same artifact.

**Merge candidates.** **None to merge.** Cluster B's M34 flags a live word collision (**materialization** versus **ingestion**), and B's term list separates `summary` from `materialized summary`. This contract governs the **materialized summary** and never the node `summary` - that boundary should be written into the deferral so the collision does not reappear inside it. Cluster E's RAG-inclusion thing is a different trade-off (what goes in) from this (what a reader may believe about what is in).

**Depends on the open context question.** **No.** #7 asks what must be in the window; this asks what a reader may trust about what arrives.

**Cross-cluster.** B **M34** (materialization/ingestion collision, and the two-summaries distinction). B **M38** (`text_extractable`'s reader is this contract - honoured above). B **M19** (system-inferred mastery is forbidden; "surface for confirmation, never resolve" is the same asymmetry as "propose, Billy disposes" and the two should be stated once). E (RAG inclusion under ruling 6). Cluster A - H3 is on the instrument-readiness precondition A flagged at M21.

**Zoomed.** Yes - `model.md §1`, §7, §9 (`text_extractable`'s retraction of `backing: unchunkable_media`), §10 item 6. Confirmed the `text_extractable` link is verbatim and is the contract's only named reader.

---

## M80. Multiagent - one justified use, two rejected

**Destination: `DROP`.**

**Which kind: agent draft never ruled, *and* superseded by generalisation.** `domain-design.md §8` says so in its own header - *"Raised by Billy; analysis below is draft, not ruled"* - and merge rule 3 honours it. It is also superseded, not by contradiction but by `model.md §7` (08-22) generalising the whole question off topology: *"the invariant is a data-flow rule, not an agent topology."* **Nothing is lost by dropping it**, because the one surviving positive (✅ context-isolated deep reads, justified by context economy) is fully contained in M75's rule - a spawned subagent, a session Billy opens himself and a task session are all implementations of the same data-flow constraint, and who produced the conclusion is irrelevant.

**Why this is not a container drop, and the note that must go somewhere.** §8's own conclusion is that what differs between courses is **a working-instruction bundle that loads with the scope - "Not an agent."** A Claude Code plugin is exactly a bundle of working instructions plus tools. So this thing's rejected option is a description of the successor container, which is genuinely interesting - **and cluster F already carries it**: M107's body states "what actually differs between courses is a working-instruction bundle that loads with the scope, not an agent." **F is the right home; nothing needs re-homing here.**

**Sequencing stripped.** None.

**Touched by Billy's rulings.** **Ruling 9** - onboarding's owner is open among four candidates including "dedicated subagent", so the *question* §8 asked is alive even though §8's answer is not. That is a reason to leave the question with ruling 9's deferral, not a reason to carry §8.

**Merge candidates.** F **M107** - already carries the durable clause. Not a merge; a confirmation.

**Depends on the open context question.** **No.**

**Cross-cluster.** F **M107** (confirmed home). B **M32** (the "coupling is through the store" clause is F's and B's, not this thing's).

**Zoomed.** Yes - `domain-design.md §8` and §5, `model.md §7`. The draft marker is at the section head, unambiguous.

---

# Terms cluster D owns

For cluster E and reconciliation. Definitions are what the thing **IS**; the decisions live in the ADRs named.

| term | definition | _Avoid_ |
|---|---|---|
| **ring 0** *(M66)* | The obligation layer under a residency policy: the fixed-shape, uniform-depth set of obligation fields the coordinator holds in its conversation context so it can tell where to look next. It governs **residency, not readability**, and is not a third persisted thing. | *the projection* (bare) · *the obligation layer* as a synonym · *the resident projection* · ring 0 meaning **what is observable** · ring 0 meaning **what is readable** |
| **coordinator** *(M74)* | The single long-running agent conversation Billy talks to - it holds ring 0, dispatches, walks the graph and writes the plan. A **conversation**, not a process: its scale is days to weeks, and every call it makes may run in a new process. | *master session* · *the agent* (bare) · *orchestrator* · **"the coordinator's lifetime"** without saying which one |
| **band A** / **band B** *(from ADR, M71)* | The two halves of ring 0's partition. **Band A "active"** is any obligation whose `due` or `done_by` falls in `today-7d .. today+14d` or whose `state` is `in_progress`; **band B "known"** is everything else, including obligations with no date. | *the active window* used for band A (the window is one of three triggers, not the partition) · *urgent* / *backlog* |
| **the walk** *(from ADR, M76)* | The operation that follows a node's edges and reads its neighbours' definitions - deterministic, O(degree), no store, no embeddings. Its internal name is `look_at(node_id, question)`; the product-facing name is undecided. | *search* · *find_material* · *retrieval* · treating the walk and a by-query store read as one operation |
| **dispatch** *(M69, M78)* | Sending a question out of the coordinator's context - to a subagent, a task session, or **Billy himself** - and receiving back a value in the same shape as every peer's. The context that produced the value stays outside. | *delegate* · *spawn* · *ask* (asking Billy is one case of dispatch, not a different mechanism) |
| **`has-more`** *(M67, provisional)* | A routing field on a ring 0 row saying whether a walk on that node returns anything beyond what ring 0 already holds. Declared in `ring-0.md §4`, written by nothing, shape undecided. | treating it as decided · reading it as a count without saying so |

**Vocabulary collisions I am escalating.**

1. **"the projection", three referents.** Ring 0's resident projection (mine) · the **calendar projection** (out per ruling 3) · B's proposed **time projection** (ruling 8's naming fix). Nobody should write "the projection" unqualified. My proposal: **ring 0** never needs the word, and B's "the time projection" keeps it.
2. **"resident", two readings** - held in a conversation's context (correct) versus held in a process's memory (wrong, and the source of the void E1). The term `coordinator` above carries the guard; if reconciliation prefers, add **resident** as its own term meaning *in the conversation's context, and nowhere else*.
3. **The product-facing name problem, per ruling 9.** The verb names "ring 0" and "skeleton" **obviously cannot** be what a user sees. That is a real constraint on this whole term list: these are the *engineering* names, and `CONTEXT.md` is an engineering glossary. Reconciliation should say so once, at the top, rather than in six entries.

---

# Orphan rulings

Rulings I met with no M-number in any cluster. All would be lost.

1. **"Ring 0 governs residency, not readability."** Billy, 2026-08-29, `evidence/2026-08-29-course-level/NOTES.md` §2 round 4, landed as commit `63612df`. `parts` returns with any read of the obligation record; excluded from the projection is not unreadable. **Carried into M66 and M67 above**, but it postdates the inventory and no M-number holds it.
2. **"`look_at(course)` is a call, and the coordinator must be able to see what a course is or plan generation is blind."** Billy, 2026-08-29, same file, round 3. Rejects the reading that `domain-design.md §9.3`'s tool surface enumerates the coordinator's reads. **Carried into M75.**
3. **"Before treating any list as exhaustive, state what question it was written to answer."** Same file, §3. A methodology guard, stated after two agent errors that were the same reasoning move. Probably not `CONTEXT.md` material, but it should not vanish - it belongs wherever this repo keeps its agent instructions.
4. **"The corpus is evidence about what the material contains. It is not evidence about what a record should look like."** Billy, 2026-08-29, same file §6. It **voids** `model.md §10.5`'s 08-28 changelog entry (standing `agent - measured`), which used note lengths from `records.json` to falsify *"real samples are short"*; the notes were a subagent's own compressions written with no write rule to follow, partly overwritten by Billy's hand edits, and nothing in the file says which body is which. **This kills every length-based argument taken from `records.json`** and it bears on M69's affordability bound, on cluster C's length rules and on cluster E's write rules. Highest-value orphan in this list.
5. **`ring-0.md §7`: "What this record does NOT establish, and must not be read as establishing: that the course level is worth a call."** *Ring 0's complement* is a negative definition, not a justification. Unruled, and named as the presentation cycle's question. No M-number.
6. **The plan** - carried above as **M75b**; flagged here too because it is an inventory completeness gap, not only a routing decision. It has a conflict number (C49) and no M-number, and Billy's ruling 3 makes it a real requirement.
7. **The ~55-obligation figure's real home.** `design.md §8`: *"the only sizing number that matters is that ring 0 for five courses is roughly 55 obligations"*, and §6 lists "whether residency still holds at five courses (~55 obligations, versus the 14 rows every read-side measurement was taken over)" as a revisit condition. Not a ruling, but it is the fact cluster A's M11 assumed was derived from a draft it dropped. Recorded so the correction is not re-lost.

---

# Summary

**Counts.** `CONTEXT` **2** (M66, M74) · `ADR` **8** (M67, M69, M70, M71, M72, M73, M75, M76) · `DEFER` **5** (M68, M75b, M77, M78, M79) · `DROP` **1** (M80). **16 things** - 15 inventory M-numbers plus M75b.

**Terms owned: 6**, plus 3 escalated vocabulary collisions.

**Blocked on the open context question (issue #7).** Three things, at three different strengths:

| thing | how it depends | how it is routed around |
|---|---|---|
| **M68** the membership test | **it *is* #7** | deferred onto the existing ticket; do not open a second |
| **M67** ring 0's field set | #7 can revise membership | the ADR records the **set and its per-field reasons**, never the test that generated them |
| **M73** what is held resident | #7 decides what must be in the window | the ADR carries only the **negative and audience halves** - never the skeleton, nobody else resident |

Three more touch it and are not blocked: **M75b** (partly - only if the plan must be revised in-window), **M76** (it makes #7's answer *smaller*, per E7), **M66** (the definition is safe; only the contents move).

**Sequencing stripped, gathered.** M67 (`schema.md §9`'s "owed to slice 4"; `ring-0.md`'s "supersedes nothing"), M75 (the responsibility table's slice/tier columns; "`look_at` not in slice 1"), M75b ("N+2" - the *dependency* on schema/API/CLI is kept, the position is dropped), M76 (`design.md §4`'s must-not-build list; presentation re-homing kept as a tier fact), M77 (**heaviest** - "dev 模式", "within the development cycle", "one full three-run arm"; the rule and the retirement *shape* are kept, the measurement schedule is dropped), M78 ("not in the first build"; the caller-must-exist dependency is kept), M79 ("`concept` is slice 2"; the kind-must-exist dependency is kept).

**Three least certain calls.**

1. **M73 as `ADR` rather than `DEFER`.** It is the thing most tightly coupled to #7, and I split it the way cluster A split M6 - keep what does not depend on the open question, drop the premise that does. If a reconciler reads "what is resident" as inseparable from "what must be resident", this should defer onto #7 instead. I think the negative half (never the skeleton) and the audience half (nobody else) are genuinely independent of membership, and the retraction on record is worth protecting from being re-made a fourth time.
2. **M67 as `ADR` while its generating test is unruled.** The field set was produced by an unruled agent test that declined another unruled agent test. I route the set to `ADR` and the test to `DEFER`, which records a decision whose justification is deferred - uncomfortable, and defensible only because the per-field reasons are independently strong (`grade_share` on a measured count, `parts` on a residency-versus-readability ruling) and because ruling 2 says the agent asks rather than executing blindly. A reconciler who wants the whole thing deferred has a case.
3. **M74 as `CONTEXT` rather than folding into F's M103.** The lifetime distinction is arguably one decision stated once (F's), not a term. I kept it as a term because the failure mode is a *word*, and a glossary entry is what a reader hits before making the mistake - but this is the entry most likely to be absorbed in reconciliation.

**Orphan rulings: 7.** The two that matter most: **"ring 0 governs residency, not readability"** (Billy, 08-29, carried into M66/M67) and **"the corpus is evidence about what the material contains, not about what a record should look like"** (Billy, 08-29, which voids a truth record's changelog entry and every length-based argument drawn from `records.json`).

**Every cross-cluster flag, in one list.**

| direction | with | what |
|---|---|---|
| **in** | B M13, B M32 → M66 | honoured; `ring 0` defined compatibly. **One correction to M32:** ring 0 is a policy over obligation nodes' **fields**, not over whole nodes - `ring-0.md §4` admits seven fields of the same node and excludes two |
| **in** | B M33 → M73, M75 | split accepted: D owns the **contract** (M75), B owns the **enforcement** (return type). B's sentence *"the coordinator sees what a node IS; it never sees what a node SAYS"* should move into M75's body |
| **in** | B M26 → M68 | **anti-merge honoured.** The rigidity rule and the membership test are different tests; §9.2's "lifted one level" is genealogy, not identity |
| **in** | B M14 → M76, M79 | honoured; B's "only the artifact carries a written summary" is what makes the walk's one-hop answer work. **Back to B:** §4.1's summary-quality criterion is an unruled *agent amendment*, not Billy's, and it is attached to B's `summary` term |
| **in** | B M19 → M79 | "surface for confirmation, never resolve" and "propose, Billy disposes" are the same asymmetry; state once |
| **in** | B M34 → M79 | materialization/ingestion collision honoured; the trust contract governs the **materialized summary**, never the node `summary` |
| **in** | B M38 → M79 | honoured - `text_extractable`'s reader **is** the trust contract, and it is the strongest reason M79 is a `DEFER` and not a `DROP` |
| **in** | A M3 → M71 | **merged, D owns the ADR.** A's clause (breadth is not a defect; the window is a stated requirement) is in the body. Ship one, not two |
| **in** | A M6 → M73 | not merged. A owns the gate (which quantity is budgeted), D owns the structure (what is held versus queried). A's stripping of the residency premise is right and I mirrored it |
| **in** | A M11 → M67, M73 | **I disagree with A's `DROP`, on one of its two grounds.** The ~55 figure does **not** hang on §9.5 (it is stated independently at `design.md §8`/§6), so A's stated worry is void - but the *acceptance clause* ("any change that makes losing the conversation painful is moving backwards") is specific, not general, in a container where compaction is routine. **Recommend folding M11's residue into M73's ADR rather than dropping it** |
| **in** | F M107 → M73 | its dropped session table's one durable clause - *"just-enough depth: enough to triage, not enough to work"* - is in M73's body |
| **out** | → **A, B, F: E1 is void** | at least A and F reference E1 as the live blocking escalation. It is not; only the narrower #7 is, and #7 does not block the observation contract the way E1 was thought to |
| **out** | → **C** (M47) | `grade_share`'s ring-0 exclusion (M67, measured) and its rigidity-rule exemption (C's) are **different trade-offs** on one field. Both must exist and cross-cite. Also: M71's band rule names C's exemption as its **stated ground** - if `grade_share` gets a reader, M71 needs re-arguing |
| **out** | → **C** (M60) | the plan's deferral (M75b) is a **different kind** from `time_point`'s: C's is "the reader is out", mine is "the requirement is real and undesigned" |
| **out** | → **C, E** | orphan 4 (the 08-29 corpus-is-not-evidence-about-records ruling) voids `model.md §10.5`'s changelog entry and every length argument taken from `records.json`; it bears on C's length rules and E's write rules |
| **out** | → **E** (ruling 7) | **one ruling, two consequences.** E owns the write rule (resolve-and-report versus ask-first); D owns the return type that carries the answer back (`Diff`'s CONFLICT branch, M78). Do not let ruling 7 land twice in two vocabularies |
| **out** | → **F** (M100, M101, M103) | M70's handle tiebreak depends on F's "every read must return handles"; M76's walk is F's grammar's third level; M74 cites F's M103 for the process half of the lifetime correction rather than restating it |
| **out** | → **reconciliation** | the plan (M75b) and orphans 1-5 are **inventory completeness gaps**, not routing decisions |
