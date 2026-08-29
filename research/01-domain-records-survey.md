# Survey — fall26 domain records, inventoried by the thing they rule on

**What I read.** Exactly two files, both in full, both primary:

- `/Users/billywu/Documents/Projects/fall26/records/domain/model.md` (709 lines) — cited below as `model.md §N`
- `/Users/billywu/Documents/Projects/fall26/records/domain/domain-design.md` (799 lines) — cited below as `domain-design.md §N`

**Boundary observed.** Nothing else was opened. Both files cite outward — `spec/schema.md`, `spec/ring-0.md`, `spec/write-rules.md`, `openclaw:fall26/2026-08-22-derivation/FINDINGS.md`, `openclaw:fall26/2026-08-23-slice-1/*` (`FINDINGS.md`, `INCONSISTENCIES.md`, `NOTE-MECHANISM.md`, `E10R-RESULTS.md`, `OBSERVATION-SPACE.md`, `FAITHFULNESS.md`, `doubt/RECONCILE.md`), `records/archive/build-plan-2026-08-27.md`, `memory/calibration.md` — and none of those were read. Where a ruling's field grain or evidence lives only in one of those, the entry below says so and stops there. Nothing in the semester-manager repo was read; nothing outside this file was written.

**What these records are.** Evidence that a question was once asked and once answered. They carry no authority here. Nothing below is adjudicated: where two passages disagree, both are recorded with their locations and dates and neither is preferred.

## Standing declarations the two documents make about themselves

These govern how every entry below should be weighted, so they come first.

| | `model.md` | `domain-design.md` |
|---|---|---|
| self-declared status | "MODEL — the fall26 domain model (**frozen 2026-08-22**)"; "**Status.** Agent draft, **scored 2026-08-22**. Billy-ruled items are marked **[R]**; everything else is the agent's position." | "**Date:** 2026-08-21 · **Status:** IDEA — design session in progress, **not a decision doc.**" |
| strength banner | "**stronger than this directory implies:** passages marked `[R]` are ruled and are not open to argument. §8's per-section promotion banners carry standing at section grain." | "**weaker than this directory implies:** this was an IDEA document written before the model met real material. Only passages marked `[R]` are ruled; §2's goal function is the part that has survived everything." |
| conditions | "§3's H1 (course type = per-layer density) is untested on an obligation-dense course; gated on slice 2 running the extractor on 2px3." | "§9.1's projection grain is dead and no replacement is ruled; §6's fact-type table lists six graveyarded fields and is superseded by `spec/schema.md`." |
| import | from `openclaw:fall26/2026-08-22-modeling/MODEL.md` on 2026-08-25; over the 200-line cap, exempt until next substantial edit | from `openclaw:devlog/ideas/2026-08-21-fall26-domain-design.md` on 2026-08-25; same cap exemption |

**A meta-disagreement that colours the whole corpus, and it is not marked anywhere in either file.** `model.md`'s title says **frozen 2026-08-22**, and its Status paragraph explains the freeze as methodological (frozen before the derivation ran so the derivation would be a test rather than a self-confirmation). But `model.md`'s own body carries `[R]` rulings dated **2026-08-23**, **2026-08-24** and **2026-08-28** (`model.md` §4.1, §5, §7.1, §8.1, §8.2, §8.3, §10.5, §10.9), and its `## Changelog` records edits on 2026-08-25 and **three on 2026-08-28**. The word "frozen" survives in the title unqualified. So the framing that `model.md` is the frozen file and `domain-design.md` the file that moved past it is only half true: **both files were edited on the same later dates, and `model.md` is in places the *later* of the two.** Where that matters, individual entries say so.

## Legend

- **Marker** quotes the document's own standing string verbatim.
- **Who** is Billy, an agent, or unattributed — as the document itself attributes it.
- **Container-sensitive** flags a ruling that reads as a property of the old container (a standalone repo running as an app a human uses) rather than of the domain. Flag only, no judgment. Every flagged item is also collected in `## Container-sensitive rulings` at the end.

---

# Part A — Purpose, trust, and what the system is for

## 1. The goal function

**Named:** "the goal function" (`domain-design.md` §2 heading), "§2" throughout both files, "the standard" (`model.md` §1).

**Revisions**

- **`domain-design.md` §2, 2026-08-21, unattributed in-body but the section says "Corrected mid-session".** The need is not reminding; it is the fear of not holding the whole picture. Two fears separated: *"did something new appear?"* (cheap, not the system's job) and *"do I hold the whole picture?"* (expensive, is the system's job). "The cost is not reading a notice; it is *interpreting* it… collapsing five of them into one is the product." No `[R]` marker on the section itself.
- **`domain-design.md` §10.4, 2026-08-22, Billy.** "**§2 was never in question and is now the judge of everything else.** An operations model that drops 55% of input cannot deliver §2's 'completeness of recall over what Billy told it'. §2 was right; §3 and §4 were the wrong implementation of it."
- **`model.md` §1, 2026-08-22.** "Design §2 stands unchanged as the standard. One clarification landed 2026-08-22, and it is a **completion** of §2's domain, not a change to it." **[R]** Billy, 2026-08-22: "dropped into an assignment's requirements he still has to model the requirements / tasks / topics himself, and helping with that is why the system exists." The thing reloaded *is* the model of the course; for unfamiliar material the reload is **first construction**, not recall — §2 described only the recall case.
- **`model.md` §1, consequence.** "§2 supplies the anti-inflation test for modelling work: **the product is collapsing the reload, so modelling that does not reduce reload cost is out of scope.**"

**Changelog:** silent. Neither file's `## Changelog` touches §2 or `model.md` §1.

**Disagreement:** none internal to the thing. Both files treat §2 as the one passage that survived everything (`domain-design.md` header banner says so explicitly).

## 2. The trust clause, and faithfulness as its operational form

**Named:** "the trust clause" (`model.md` §1, `model.md` §8.1, `domain-design.md` §2), "completeness of recall over what Billy told it", "faithfulness" (`domain-design.md` §2, §6.1).

**Revisions**

- **`domain-design.md` §2, 2026-08-21, unattributed.** "the trust requirement moved from *coverage of the world* (unsolvable, and not the system's job now) to *completeness of recall over what Billy told it* (mechanically solvable)."
- **`domain-design.md` §2, marker `OPERATIONALISED — Billy 2026-08-23, written in here 2026-08-24 — promoted from fall26/2026-08-23-slice-1/experiments/FAITHFULNESS.md, which is now evidence only`. [R] Billy, 2026-08-23, verbatim:** "系统不会拒绝你问问题，改怎么使用是用户的 burden 而不是系统的。系统只需要保证回答对该回答的。" → "**Faithfulness is the system's burden; scope and usefulness are the user's.**" Operationally: every claim traceable to a held fact, no relevant held fact omitted, nothing invented.
- **Same block, limit attached and marked as travelling with it.** "The 08-23 measurement graded 60 runs and found **zero omissions** — but at a scale where omission was **not possible rather than avoided** (14 rows returned whole in one ~3,200-token call, no skeleton counted, no store in existence). **The precision-versus-recall framing that cycle used is void: the recall half of faithfulness was never loaded.**" A real test needs five courses, the skeleton in the denominator, and the corpus — slices 2 and 3.
- **`model.md` §1, 2026-08-22.** Scope limit added: "§2's **trust clause** … does not cover content the system *generates*. A proposed concept partition was never told to it. A separate trust contract is owed for generated content — §7." (See thing 60.)
- **`model.md` §8.1, [R] Billy, 2026-08-23.** "**not trusting the user is CONFLICT DETECTION, not verification.** The system has neither the standing nor the ability to verify Billy; §2's trust clause is *completeness of recall over what Billy told it*, not coverage of the world." Response shape when Billy says "A6 is done" and the portal records no submission: "you told me this, the record says that — which holds?"

**Changelog:** silent in both files.

## 3. Scope is not a defect

**Revisions**

- **`domain-design.md` §2, `OPERATIONALISED` block, ruled Billy 2026-08-23.** "**Scope is not a defect.** A request for a whole semester that gets a whole semester is answering what was asked. Billy's own observation that the useful window is ±1–2 weeks is a *requirement he may state*, not a failure to fix."
- **`domain-design.md` `## Changelog`, 2026-08-28 — Billy — ruled.** "the +/-1-2 week observation this section held as *a requirement Billy may state, not a failure to fix* **was stated and ruled on this date, as `today-7d .. today+14d`**." The ruling's home is `spec/ring-0.md`, not this file.

**Changelog is the only place the window's resolution appears.** The body of `domain-design.md` §2 still reads as if the window is unstated. This is a case where the changelog is strictly ahead of the body.

## 4. What the system is NOT: not enterprise RAG, and its three jobs

**Revisions**

- **`domain-design.md` §10.7 ruling 4, Billy, 2026-08-22, marker `## 10.7 Billy's rulings, 2026-08-22`.** "**This is not an enterprise RAG that answers every question precisely.** It is a personal knowledge base whose job is: remove the anxiety of not finding information · manage cross-course information in the background · **locate details Billy himself does not know about.**"
- **`domain-design.md` §10.8, marker `## 10.8 Agent drafts, not ruled`.** "**Tune for recall, not precision.** Ruling 4's third goal … is the only one not served by 'retrieve when asked', and it wants breadth with the filtering left to him. This is the opposite tuning from enterprise RAG."
- **`model.md` §6, agent.** The third goal is upgraded from a tuning posture to a query: set difference "turns `domain/domain-design.md` §10.7 ruling 4's vaguest goal (*surface details Billy does not know to ask about*) from a retrieval heuristic into a **deterministic query**."

**Changelog:** silent.

**Disagreement (mild, cross-file):** `domain-design.md` §10.8 says the third goal wants recall-tuned *retrieval*; `model.md` §6 says it is served by a deterministic graph query instead. Neither passage acknowledges the other. `domain-design.md` §10.8 is unruled; `model.md` §6's two-query claim is also unattributed.

## 5. The system declares nothing outward

**Named:** "the assertion surface", "audit / completeness-assertion surface".

**Revisions**

- **`domain-design.md` §1 ruling 10, marker `## 1. Billy-ruled in this session`, 2026-08-21, Billy.** "**The system declares nothing outward.** An audit / completeness-assertion surface was drafted and rejected: it manages the calendar and helps when Billy jumps in; internally it does what it needs. Trust accrues from being useful, not from self-reporting."
- **`domain-design.md` §7, marker `~~How Billy verifies the system actually holds full context.~~ **RULED OUT 2026-08-21.**`** Same ruling restated, plus: "a self-audit that can itself go stale is net-negative. Integrity checks (closure, no coexisting contradictions) survive as silent internal work. The `manifest` field survives on a different justification — see §6."
- **`domain-design.md` §5.** "The 'assert what is held' step that appeared in an earlier draft was ruled out (§1.10)."

**Changelog:** silent.

**Container-sensitive.** "Declares nothing outward" is a statement about an app's user-facing surface. The successor's container is an agent's tool surface, where the same question ("does the component report on its own completeness?") may not have the same answer.

---

# Part B — Layering, and who reads what

## 6. Two layers: facts and corpus

**Named:** "Facts layer" / "Corpus layer" (`domain-design.md` §3); superseded naming "what a planner reads" / "what an agent reads" (`domain-design.md` §10.5); later naming "ring 0 / skeleton / store" (`model.md` §4).

**Revisions**

- **`domain-design.md` §3, 2026-08-21, unattributed.** A table splitting by content type: facts = deadlines/status/requirements/progress/plans, tiny, CRUD, per-row, RAG **harmful**; corpus = slides/spec text/reference, large, append+supersede, per chunk, RAG correct. "**Load-bearing consequence: full context in ordinary conversation needs no retrieval.**"
- **`domain-design.md` §3 banner, marker `⚠️ **PARTLY SUPERSEDED 2026-08-22 — see §10.5.** The number of layers holds; the split axis does not. The load-bearing sentence "full context in ordinary conversation needs no retrieval" is false as written.`**
- **`domain-design.md` §10.5, 2026-08-22, evidence-driven.** "**§3 — the split axis was wrong, not the number of layers.** … The working split is by *who reads it*: what a planner reads (resolved, typed, small) versus what an agent reads (text, retrieved). 'Which room does T04 meet in' is neither a deadline nor a slide — **the old two-layer split had no home for most of a course's real information.**" What survives: "**the allocation layer needs no retrieval.**"
- **`model.md` §4, agent-authored (see thing 7's standing marker), terminology mapping.** Three names, not two: ring 0 / skeleton / store. "One line: **the skeleton owns 'is there any, where, worth opening'; the store owns 'what is in it'; ring 0 owns 'when and how much'.**"

**Changelog:** `domain-design.md` changelog is silent on §3. `model.md` changelog is silent on §4.

**Disagreement (cross-file, unreconciled anywhere):** `domain-design.md` says two layers, number holds, axis wrong. `model.md` §4 presents **three** compartments and never states whether ring 0+skeleton together are "the facts layer" or whether the skeleton is a third thing. `model.md` §4's own header calls itself "Terminology drifted during the session; this is the mapping" — i.e. it asserts the mapping exists but does not map it onto `domain-design.md` §3's two.

## 7. What a Node summary is for — and §4's standing

**Named:** "Node summary", against "the store's summary" (`model.md` §4.1). The records insist these are two objects with confusingly similar names.

**Revisions**

- **`model.md` §4, agent-authored table.** The skeleton "answers … what is there, where does it sit, **is it worth opening**".
- **`model.md` §4 banner, marker `> **STANDING MARKED 2026-08-24 (the confusion it records is 2026-08-23).** **This section is agent-authored and carries no `[R]`.**`** "On 2026-08-23 its phrase *'is it worth opening'* was quoted in session as a settled ruling about what a Node summary is for; **it never was**, and Billy confirmed as much (*'我不记得我定论过 skeleton Node summary 的职责是什么这个问题'*). The marker is added here because that mistake is one of three the same day in which an unmarked agent passage was taken for, or overrode, a ruling."
- **`model.md` §4.1, heading marker `### 4.1 What a Node summary is for — NOT RULED`, plus `> **PROMOTED 2026-08-24 (ruled 2026-08-23)** … **Nothing in this subsection is settled.**`**
- **`model.md` §4.1, [R] Billy, 2026-08-23.** "**the store's summary and the Node summary are different objects.** §4's store column (*summary / tags / chunks / embeddings*) is retrieval infrastructure and the coordinator never sees it; the Node summary serves the coordinator's viewpoint." This "dissolves a 'two summaries per node' proposal made an hour earlier."
- **`model.md` §4.1, two framings discarded.** *"Is it worth opening"* is wrong for the coordinator because §7's table denies it the store in both modes, so "the coordinator never opens anything". *"Concise"* does not cover the failure either: the `2aa4-guide` summary was **55 words** and still noise, "because it enumerated seven unrelated facts".
- **`model.md` §4.1, the two-party split, explicitly "must not be collapsed".** Billy proposed: *a summary is good if it helps the agent know what the node is.* The agent judged that non-discriminating and amended it to: *a summary is good iff it answers the question that made the agent look.* "**This amendment is the agent's, not Billy's, and has not been ruled on.**"
- **`model.md` §4.1, a further unruled proposal.** "*the Node summary carries what its own layer uniquely knows and never restates what ring 0 already holds.*" Marked "**A proposed layer rule, also unruled**"; the agent's own position is that it is a proxy for the question rule rather than an independent principle.
- **`model.md` §7.2, [R] (unattributed date).** "**summary** | concise **at birth**, not trimmed later | the coordinator" — a length property only.

**Changelog:** silent in both files on §4 and §4.1.

**Disagreement (within `model.md`, explicitly flagged by the document):** §4's table says the skeleton answers "is it worth opening"; §4.1 says that framing "is wrong for the coordinator" and that §4 was never ruled. Both passages remain in the file.

## 8. The store's access modes, and where the purity cut falls

**Named:** "by-handle" / "by-query" (`model.md` §5); "the three access levels" (`model.md` §5 revision); "§9.0's purity cut" (`domain-design.md` §9.0).

**Revisions**

- **`model.md` §5 body, 2026-08-22, agent.** Two modes — by-handle (`node_id`, JOIN, deterministic) and by-query (text, ANN). "They share one store and are two different capabilities. **§9.0's purity cut falls exactly between them.**"
- **`model.md` §5, marker `> **REVISED 2026-08-23, Billy.**`** "That last sentence is wrong as written and it misleads: it places the purity cut **between** by-handle and by-query, which implies the coordinator may do by-handle. **§7's table denies it both.** The access levels are **three**, not two, and the coordinator's line sits above both store modes." New table: skeleton read ✅ may query, does not hold; store by-handle ❌ (ephemeral context ✅); store by-query ❌ (ephemeral context ✅). "**The coordinator sees what a node IS; it never sees what a node SAYS.** §9.0's cut belongs between the skeleton read and by-handle." Noted: "(It misled a session on 2026-08-23, which is why this is marked here rather than only in the slice-1 folder.)"
- **`domain-design.md` §9.0, 2026-08-21, marked in §9's header as an agent draft.** "**Purity cannot be maintained by prompt. Only by tool surface.** … An agent holding a tool will use it. Remove corpus retrieval from its tool surface and drift becomes structurally impossible rather than a discipline problem. This is the repo's own `enforcement-locus-chokepoint` dimension."

**Changelog:** silent in both files.

**Disagreement (within `model.md`, flagged in place):** the §5 body sentence and its 2026-08-23 revision disagree about where the cut falls. The revision states the body sentence "survives only as a statement about the store's two internal modes".

**Container-sensitive.** §9.0's mechanism is "remove the tool from the coordinator's tool surface" — a claim about who controls the agent's tool registry. In the successor container the components *are* the tool surface, which may relocate rather than dissolve the rule.

## 9. Materialization is not retrieval indexing

**Revisions**

- **`model.md` §5, 2026-08-22, agent.** "Chunking, summarizing and tagging are paid once so that every later read is cheap; that cost exists whether or not anything is embedded. An earlier agent draft ('embed ~300 summaries instead of ~20,000 chunks') conflated the two and was **retracted** — it would have forced a runtime `pdftotext` on every detail read."

**Changelog:** silent.

## 10. Where the vector index attaches

**Revisions**

- **`domain-design.md` §1 ruling 9, Billy, 2026-08-21.** "**RAG is accepted for corpus** — one-time embedding at material drop, **per-course buckets** for independence, metadata filtering. Math-equation chunking is a known industry problem and is deferred."
- **`model.md` §5, marker `**Where the graph puts the vector index (agent position, not ruled).**`** "Embeddings attach to the **concept layer** as the entry point; chunks stay in the artifact layer for reading. `query → nearest concept → walk covers → read artifact by-handle`. Side benefit: retrieval becomes explainable."
- **`domain-design.md` §10.1, P1, 2026-08-22.** "is pgvector available | PASS — 0.8.0, HNSW builds."

**Changelog:** silent.

**Disagreement (cross-file, unacknowledged):** `domain-design.md` §1.9 rules per-course buckets as the index's organizing axis; `model.md` §5 proposes the concept layer as the entry point. Neither is stated as replacing the other, and `model.md` §5 flags itself as "agent position, not ruled" while `domain-design.md` §1.9 is in the Billy-ruled list.

**Container-sensitive.** pgvector availability, HNSW, per-course buckets are properties of a database the standalone app owned.

## 11. The coupling surface between skeleton and store

**Revisions**

- **`model.md` §6, 2026-08-22, unattributed.** "**The coupling surface between skeleton and store is exactly one field: `chunk.node_id`.** Everything else is independent, which is what lets each degrade without the other: store down → the skeleton still navigates ('this material exists, open it yourself'); skeleton wrong → by-query still finds text but cannot say where it sits."

**Changelog:** silent. **Container-sensitive** (names a table column in a store the app owns).

## 12. The two graph queries that earn their keep

**Revisions**

- **`model.md` §6, 2026-08-22, unattributed.** "**Two graph queries that earn their keep at this scale** (and only these two — centrality, community detection and similar are premature at N≈300): **transitive closure of `requires`** … **set difference** — concepts no artifact covers = material Billy does not have; concepts no obligation points at = will not be examined."
- **`model.md` §8 edge table** makes transitive closure the sole reading mechanism justifying the `requires` edge's addition ("**transitive closure — §6's flagship query** | **ADDED**"), and the `applies` split-out is "never rendered; feeds closure".

**Changelog:** silent.

---

# Part C — The graph: shape, node kinds, edges

## 13. The structure is a layered graph, not a tree

**Revisions**

- **`model.md` §2, [R] Billy, 2026-08-22.** "obligation / concept / artifact are not a pick-one; an assignment and a topic coexist. The implementation is a graph (DAG or layered graph), not a tree. Different entities pointing at the same thing is how humans understand material."
- **`model.md` §2, argument.** "A lecture PDF and a tutorial PDF exist independently and are used independently … yet both describe one concept (Stack). Containment forces a choice between filing by concept and filing by material kind; the relation is many-to-many, so one spine cannot hold it. This is the specific failure Billy named on 2026-08-22: *a file is not the object being modelled.*"
- **`model.md` §2, [R] Billy, 2026-08-22.** "a concept appearing in two places is **the truth of the data, not a rendering bug** — the model may not cut edges to force a tree. Which spine a view renders is a CLI/UX decision, **deferred**."

**Changelog:** silent.

## 14. Which layer is a tree — the within-layer claim

**Revisions**

- **`model.md` §2, original agent draft (quoted inside its own revision).** "*the tree survives inside a layer, which is what keeps rendering well-defined.*"
- **`model.md` §2, marker `> **REVISED 2026-08-22 by the derivation.**`** "**False for the concept layer.** Concepts routinely have more than one legitimate parent, and the recurrence is pedagogy rather than duplication: **Singleton** is a Creational pattern *and* the 'S' of STUPID …; **Liskov substitution** sits under SOLID, under the pattern block's principles, and again under 'SOLID for change'; **Observer** is a behavioural pattern and *is the mechanism of* MVC. **The concept layer is a DAG. The artifact layer is the tree** — 2aa4's 21 lectures partition into 5 groups with no document in two and none orphaned. … Treat this as the general case: it was tested on 2aa4 and 2c03 has visible candidates."
- **`model.md` Status paragraph** names this among the three things the derivation falsified: "It was not confirmed: §2's within-layer tree claim, §3's 2aa4 row, and three entries in §8 were falsified against real material."

**Changelog:** silent (the revision is marked in place, per the document's stated method: "Revisions are marked in place with the evidence that forced them").

## 15. The three node kinds / layers

**Revisions**

- **`model.md` §2 table, 2026-08-22.** obligation = "a thing with a deadline", carries time, "this layer *is* ring 0"; concept = "a unit of subject matter the course teaches, independently addressable", no time; artifact = "a thing the course delivers and that is opened independently", no time.
- **`model.md` §8 vocabulary block, scored 2026-08-22.** `id · course · layer(obligation|concept|artifact) · label(free text, written once at ingest) · added_at`, plus per-layer fields (see things 30–38).
- **`model.md` §10 item 2, owed.** "**Where concept nodes come from**, and who draws cross-layer edges. Candidates: the outline's schedule · the per-artifact multimodal pass · Billy's rejection. **Order and weight unsettled.**"

**Changelog:** silent on the kind set itself.

## 16. The modelling layer is stateless — no system-inferred mastery

**Revisions**

- **`model.md` §2, [R] Billy, 2026-08-22.** "**the modelling layer is stateless.** An earlier draft defined a concept as *'a thing Billy understands or does not'*; that wording presumed state the system must not keep. The system presents concepts and leaves judgment to him. **System-inferred mastery is forbidden.** (Billy-stated progress survives untouched as a ring-0 row per `domain-design.md` §1.6 — the constraint scopes to the modelling layer, not to facts Billy authors about himself.)"
- **`model.md` §8 vocabulary.** "`concept: — (no state; see §2)`".
- **`model.md` §8.1, derived not separately ruled.** The staleness table's second row — "*'I've done part 1 of A6'*" → "**surface it for confirmation, never resolve it**" — "follows from §2's ruling that system-inferred mastery is forbidden and the modelling layer is stateless: the agent has no evidence either way and may not manufacture some."
- **`domain-design.md` §6, rigidity rule.** Independent arrival at the same place: "a topic matters, but no mechanism reads 'what a topic is', so it gets no taxonomy, no chapter hierarchy, **no mastery scale**."

**Changelog:** silent.

**Note on the cross-reference:** `model.md` §2 cites `domain-design.md` §1.6 as making Billy-stated progress "a ring-0 row". `domain-design.md` §6.2 (2026-08-24) rules progress is **not** a typed row but an annotation with its own kind (see thing 34). The parenthetical in `model.md` §2 was not updated.

## 17. Artifact existence: no `present` flag, no `external_ref`

**Revisions**

- **`model.md` §2, [R] Billy, 2026-08-22.** "an artifact does **not** have to exist on disk, need a URL, or carry a `present` flag. It exists on the portal, and knowing what its name refers to is enough — he does not want every resource stored locally. **Absence therefore has no field: it is simply the absence of store content** for that node. (2aa4 depends on ≥8 artifacts that are not on disk and never will be; it has zero code projects locally because its code lives in GitHub.)"
- **`model.md` §9, restated as a supersession.** "**`external_ref` backing and a `present` flag.** Both proposed by the derivation, both **rejected by Billy** (§2). Absence is not a field; it is the absence of store content, which §6's set-difference reads as a JOIN."

**Changelog:** silent.

## 18. The unification hypothesis H1 — course type as per-layer density

**Revisions**

- **`model.md` §3, [R] Billy, 2026-08-22.** "accepted as the starting point, revisable if the derivation induces something better." The claim: academic / pure-teamwork / concept+lab+assignment courses are "**one structure with different per-layer density**, not three structures". Falsifier stated: "a course that needs a node kind or edge kind the others do not. Density differences alone do not falsify it."
- **`model.md` §3, marker `> **CORRECTED 2026-08-22 — and this row was the hypothesis's calibration point.**`** The 2aa4 row is struck through in the table itself. "2aa4's obligation layer is **sparse, not dense**: no tutorial carries a deadline, a submission, or a mark (grepped across all nine, zero hits) … **2aa4 is topic-dense / obligation-sparse — the same shape as 2c03.** The original row was written from folder appearances (`tutorials/` holds 11 files), which is exactly the *folders-are-not-taxonomy* error this cycle exists to avoid, **committed inside the model**."
- **Same block, standing after correction.** "**H1 is not falsified** — no course needed a node or edge kind another lacked, and 2aa4 needs strictly fewer. **But the dual-axis exemplar is gone, so H1 now rests on two courses of the same shape**, plus 2px3, which the derivation excluded. Also qualitative, not fatal: `announcement → node` is *structurally impossible* in 2aa4 rather than merely sparse, so a renderer must not assume the edge exists."
- **`model.md` header conditions block.** "§3's H1 (course type = per-layer density) is untested on an obligation-dense course; gated on slice 2 running the extractor on 2px3."

**Changelog:** silent.

## 19. The edge set

**Revisions**

- **`model.md` §8, scored 2026-08-22 against 2c03 and 2aa4 by the derivation.** Adoption rule stated: "Only changes supported by **≥2 agents or ≥2 courses**, or by a Billy ruling, were adopted; single sightings went to the watch list. Every entry passes the rigidity rule — **a field or edge is typed iff a mechanism reads it**." Edges and per-row status verbatim: `concept → concept` part-of "**survives — as a DAG, §2**"; `concept → concept` **requires** "**ADDED**"; `obligation → obligation` builds-on "survives"; `artifact → concept` **covers** "**survives, narrowed**"; `artifact → concept` **applies** "**split out of `covers`**"; `obligation → concept` requires "survives"; `obligation → artifact` spec `role ∈ {given, owed}` "survives, discriminated"; `artifact → obligation` **prepares-for** "**ADDED**"; `sticky_note → node` note-on + `origin` "survives — **targets all three layers**"; `artifact → artifact` supersedes "**CUT**"; `announcement → node` mentions "**CUT — merged into `sticky_note.origin`**". "All edges may carry a `locator` payload."
- **`model.md` §8.2, Billy 2026-08-24.** note-on "generalises to `about`" and `look_at` returns `{summary, annotations[], edges[]}`. This changes the §8 edge table's `sticky_note → node (note-on)` row without editing it.

**Changelog:** `model.md` 2026-08-25 records only the import decision for §8's banners: "the promotion banners inside §8 were left in place because they carry standing, not history — agent — agent-drafted".

## 20. `supersedes` — cut

**Revisions**

- **`model.md` §8, marker `**CUT**`, with the reasoning under `**Why the two cuts.**`** "scored **zero instances across five agents and two courses**, and keeping it is actively harmful. Revisions replace the file at the same path under the same name, so there is no v1 to point from and D1 has no input; meanwhile three real shapes would be mistyped as supersession and would **hide a live document** — `Tree Map UML` vs `BST Tree Map UML`, handout vs sample solutions, `.docx` vs `.pdf` of one report. The decisive case is 2aa4's dating trap: notes exports carry real lecture dates while every plain slide export was batch-produced on 2026-03-04, so 'newest wins' systematically discards the **richer** file. Replaced by `revised_at`; *what* changed is carried by the sticky note. **Filename similarity must never imply a relation** — one same-named pair turned out to be two different lectures (Jaccard 0.21)."
- **`domain-design.md` §3, 2026-08-21 (pre-evidence).** The corpus layer's write mode was "**append + supersede only**" — the very operation §8 cuts.
- **`domain-design.md` §10.3, 2026-08-22.** "**Retirement is read-time expiry, roughly 7:1 over write-time supersession.** §4's 'it happens at the moment of write' describes only the smaller branch. **This settles D1.**"

**Changelog:** silent.

**Disagreement (cross-file, unmarked):** `domain-design.md` §3's corpus write model ("append + supersede only") is contradicted by `model.md` §8's cut of `supersedes` and by `domain-design.md` §10.3's own 7:1 finding. §3 carries a `PARTLY SUPERSEDED` banner, but that banner is about the *split axis*, not about the write column.

## 21. `announcement → node (mentions)` — cut, merged into `sticky_note.origin`

**Revisions**

- **`model.md` §8, marker `**CUT — merged into `sticky_note.origin`**`.** "*`mentions`* duplicated `sticky_note`. Every high-value announcement **is** a correction; the rest point at nothing. An announcement is the sticky note's `origin`, plus a flat provenance log — which is what design §10.6 ruled and this appendix had half-undone."
- **`domain-design.md` §10.6, P6, 2026-08-22.** Billy's proposition was "announcements are a **delivery channel for facts, not a body of knowledge** — consumed and discarded, never indexed". "**Tested on two courses with the bias set against the convenient answer. It failed in both** — 5 of 55 in a theory course, 6 of 38 in a hardware lab course, after discounting redundancy. Not profile-specific." What survives: "it is almost always **a correction against material the system already holds**." And: "**an amendment to a document is not a fact.** It belongs to the corpus as metadata, not to the facts layer."
- **`domain-design.md` §10.6, redundancy defence.** "**dead, verified on disk in both courses**" — the locally held `Tutorial_RiscFreeIDE.pdf` is the broken pre-correction version, `lab01.pdf` names the superseded Quartus version, the Week 7 deck is the blank-whiteboard variant. "The bulk is redundant; the seam is not. Full-or-partial redundancy runs 40-51% overall, but only 1 of 7 and 2 of 7 among the knowledge instances."

**Changelog:** silent.

**Disagreement (cross-file):** `model.md` §8 says the merge "is what design §10.6 ruled". `model.md` §9 restates §10.6 as "announcements are a delivery channel, and the portal tree is a delivery layout". But `domain-design.md` §10.6's headline finding is that the delivery-channel proposition **failed in both courses** and that the surviving claim is narrower (announcements carry a correction seam). `model.md` cites §10.6 twice in the direction of the proposition rather than the finding.

## 22. No generic `related_to`

**Revisions**

- **`model.md` §8, unattributed.** "Nothing reads 'related'. The real instance behind it (*the tutorial's Dijkstra differs from the lecture's — follow the lecture*) is a correction: a sticky note carrying an origin and a target."

**Changelog:** silent. Note the same instance appears in `domain-design.md` §10.6's knowledge list, where it is one of the announcements that falsified the channel proposition.

## 23. Why `covers` split

**Revisions**

- **`model.md` §8.** "It read two ways at once, and the reading determined whether a hub existed: `Big O` is degree ~3 as *subject-of* and ~15 as *requires-you-to-understand*. **Only `covers` is rendered.**"
- **`model.md` §10 item 1.** Edge conflation is named as one of the three modelling choices that manufactured the hub: "**H2 measured us, not the material.**"

**Changelog:** silent.

## 24. `spec` roles: `{given, owed}`, and whether `produced` splits off

**Revisions**

- **`model.md` §8.** `obligation → artifact (spec, role ∈ {given, owed})`, "survives, discriminated".
- **`model.md` §8 watch list.** "`produced` as a distinct edge (a `role` attribute suffices)" — one sighting, "deliberately not adopted".
- **`model.md` §7.2, marker `**Left open, deliberately.**`** "§8 compressed the derivation's four `spec` roles into two … The derivation's J2 named a query that two roles do not obviously serve — *'show me what I handed in for A8'* — and argued for splitting `produced` off. **Not ruled.**"

**Changelog:** silent.

## 25. The watch list

**Revisions**

- **`model.md` §8, marker `**Watch list — one sighting each, deliberately not adopted** (PLAN.md's over-modelling failure mode)`.** `artifact → artifact contains` (9) · `projects` / is-a-view-of (6) · `sequence` (3) · `rendition-of` (1) · `produced` as a distinct edge.

**Changelog:** silent.

## 26. "No relationship graph" — overturned

**Revisions**

- **`domain-design.md` §6, 2026-08-21, unattributed.** "**No relationship graph.** Relationships are inferred at read time by the LLM, not declared at write time. The only reason to declare them at write time is data too large to hold at once — and it fits."
- **`model.md` §9, marker `## 9. What this supersedes`.** "**Design §6's 'No relationship graph.' Overturned by its own rule, not violated.** §6's stated reason was *'the only reason to declare relationships at write time is data too large to hold at once — and it fits'*; the authorizing clause is the rigidity rule, and `obligation → concept` now has a mechanism that reads it. Same event class as §3 and §4: **the rule survives, the conclusion falls to new evidence.**"

**Changelog:** silent in both files.

**Disagreement (cross-file, one-sided):** `domain-design.md` §6's banner enumerates what changed in §6 ("the five types' standing", the `workload-estimate` entry, the missing-rate sentence, the `progress` row's carrier) and closes: "**Everything else in §6 — the rigidity rule, the one-free-text-field rule, `/promote` evolution — is unchanged and still governs.**" It does not list "No relationship graph" as changed. `model.md` §9 says that clause is overturned. The overturn is recorded only on the `model.md` side.

## 27. The graph has no time axis; `week` / `time-anchor` is not a field

**Revisions**

- **`domain-design.md` §10.5, 2026-08-22.** "'A field is typed iff a mechanism reads it' is exactly what says `week` must **not** be a field: `week` is a retrieval term, and 2px3 organises by week while other courses organise by topic or assignment number. Hardcoding either is the failure."
- **`model.md` §9.** "**`time-anchor` as a node field.** Retracted — a renamed `week`, which `domain-design.md` §10.5 already ruled out. **Invariant instead: the graph has no time axis; time lives only in the obligation layer.**"
- **`model.md` §9, evidence added 2026-08-22.** "687 KB of 2aa4 lecture text contains **zero** occurrences of 'Week N', and the course has no announcement stream — its lecture layer is genuinely timeless."
- **`model.md` §9, cost the document says it had not priced.** "*'what is week 7 about'* is unanswerable for such a course from lecture material, while *'what is topic X about'* answers well. **The navigational handle is course-specific — week for 2c03, module for 2aa4 — and it is a label on the coarse grouping that the schema never names.**"

**Changelog:** silent.

**Disagreement (cross-file, unresolved by either):** `domain-design.md` §10.4 states the system's job as "when Billy asks '**what is week 7 about**', it holds the surrounding context". `model.md` §6 scenario 2 lists "what is week 7 / topic X about" as a skeleton-answerable question. `model.md` §9 then says that exact question is **unanswerable** for a course with no week structure and that the schema names no handle for it. The 2026-08-22 material evidence and the 2026-08-22 reframe point opposite ways on the same example sentence.

---

# Part D — Fields and the schema

## 28. The rigidity rule

**Revisions**

- **`domain-design.md` §6, 2026-08-21, unattributed in-body.** "**A field earns `typed` if and only if some mechanism reads it. Everything else is free text.** Rigidity follows mechanism, not importance." Mechanisms enumerated: "M1 auto-retirement · M2 plan allocation · M3 rewrite targeting · M4 scope loading · M5 provenance".
- **`domain-design.md` §6 banner, marker `⚠️ **SCOPE CUT 2026-08-22 — see §10.5.** The rigidity rule itself is vindicated and unchanged.`**
- **`domain-design.md` §10.5.** "**§6 — the rule is vindicated, its scope is cut.**"
- **`model.md` §8.** "Every entry passes the rigidity rule — **a field or edge is typed iff a mechanism reads it**."
- **`domain-design.md` §9.2, `RESTATED` block.** An agent lifts the rule one level: "*an observation earns its place if and only if a judgment demonstrably changes when it is present.*" Marked "**agent formulation, obtained by lifting the rigidity rule one level, not separately ruled**". Testable "by running the same task with and without the observation".

**Changelog:** silent.

## 29. The fact-type table (the five types)

**Revisions**

- **`domain-design.md` §6 table, 2026-08-21.** course · obligation · time-point · progress · plan · preference, each with typed fields, one free-text field, and reading mechanisms. "Obligations and time-points are separate because **only obligations consume the weekly hours**." `target` is polymorphic — "an obligation id, or free topic text. The entire cost of ruling 6 (independent progress) is concentrated in this one field and spreads no further." `manifest` "earns typing because it makes answers complete ('A4 exists, not yet scheduled'), NOT because anything is reported outward — the assertion surface it was first drafted for was ruled out 08-21". `offering-term` is "the one field justified by *another domain's* need".
- **`domain-design.md` §10.5, 2026-08-22.** "What shrinks is the five types' standing: from *the destination of all inbound* to *only what the allocation planner reads* — `due`, `workload`, `status`, `course`. Everything else is knowledge."
- **`domain-design.md` §6, in-body supersession note (added 2026-08-25 per changelog).** "**This table is superseded by `spec/schema.md` as the field set.** It still lists `status`, `workload-estimate`, `source-ref`, `manifest`, `prereq` and `offering-term`, **every one of which is in the schema graveyard**. It is kept because the *rigidity rule* it illustrates is still live; read it for the rule, never for the fields."
- **`domain-design.md` header conditions.** "§6's fact-type table lists six graveyarded fields and is superseded by `spec/schema.md`."

**Changelog (`domain-design.md`), 2026-08-25 — agent — agent-drafted:** "§6's fact-type table marked as superseded by `records/schema.md`: it still lists `status`, `workload-estimate`, `source-ref`, `manifest`, `prereq` and `offering-term`, all of which are in the schema graveyard. **Flagged rather than rewritten, because rewriting the table is a schema decision and not a migration.**" — this is the changelog stating the reason the body was left wrong on purpose.

**Note:** the changelog says `records/schema.md`; the body says `spec/schema.md`. Same for `model.md`'s 2026-08-25 progress entry (`records/schema.md`) versus `model.md` §8.2's body (`spec/schema.md`).

## 30. One free-text field per type

**Revisions**

- **`domain-design.md` §6, 2026-08-21.** "**Rule: exactly one free-text field per type.** More and Billy has to decide where things go (the overhead returns); zero and it is over-structured."
- **`domain-design.md` §6 banner.** Explicitly listed as still governing.

**Changelog:** silent.

**Disagreement (cross-file, unacknowledged):** `model.md` §7.2 rules ingest writes **summary, tags and sections** onto a node, and §8.2 gives `progress` both `state` (enum) and `detail` (prose) alongside `origin`. Neither passage tests itself against the one-free-text-field rule that `domain-design.md` §6's banner says is unchanged.

## 31. Schema evolution via `/promote`

**Revisions**

- **`domain-design.md` §6, 2026-08-21.** "**Schema evolution uses the existing `/promote` gate** (recurrence + boundary + coverage), with the object changed from basis dimensions to schema fields … Only typed fields make migrations, so deferring a decision is free — which is what dissolves the over-determination worry: **a tiny mechanical core plus everything else free**, not vagueness everywhere."
- **`model.md` §10.9, 2026-08-23 ruling.** `/promote` is invoked as the escape valve for the rejected general form: "`domain-design.md` §6's `/promote` evolution mechanism promotes it if it recurs."

**Changelog:** silent. **Container-sensitive** — `/promote` is a repo slash-command ritual.

## 32. `workload` / `hours_estimate`

**Named:** `workload-estimate` (`domain-design.md` §6 table), `workload` (`domain-design.md` §9.1, §10.5; `model.md` §8), `hours_estimate` (`domain-design.md` §6.1). Three names, one thing.

**Revisions**

- **`domain-design.md` §6 table, 2026-08-21.** `obligation` typed fields include `workload-estimate`, read by M1 M2 M3 M5.
- **`domain-design.md` §6, 2026-08-21.** "**The signal is the missing-rate of `workload` and `due`**, not a subjective feeling." (Now struck through in place.)
- **`domain-design.md` §7, open, 2026-08-21.** "**Where `workload` estimates come from.** Tilt: Billy states a rough number, revisable. Inferring from spec or learning from progress history both require data that does not exist yet." Under heading `## 7. Open — not yet ruled`.
- **`domain-design.md` §10.5, 2026-08-22.** `workload` listed among what the allocation planner reads.
- **`domain-design.md` §6.1, heading marker `### 6.1 `workload` / `hours_estimate` is NOT a field to be filled — [R] Billy, 2026-08-23`, block marker `> **RULED 2026-08-23, written in here 2026-08-24; this subsection governs over the `workload-estimate` entry in §6's table and over §6's missing-rate sentence.**`** Billy verbatim: "hours_estimate 很难量化，我一般都是按照某个 assignment 的进度和 high-level 体量来判断的。" Three-part ruling: (1) not a field to be filled, its null is not a gap; (2) "**Size is observed ordinally** — from `parts` and item notes first, then by asking for a relative comparison"; (3) "**Its missing-rate is retired as a guard signal.** Replacement guard: **faithfulness** (§2)."
- **`domain-design.md` §6.1, reversal recorded at both ends.** "It reverses spec §10.9 item 3, which says the 2026-09-01 ruling *'is not overturned'* — **it is now overturned**, and the reversal is marked at both ends."
- **`domain-design.md` §6.1, adversarial correction, 2026-08-23.** "The claim that the third falsification differs *in kind* from the first two … **does not hold**: the Notion-table evidence is already user-side. What survives is narrower and still sufficient: **asking is only a remedy for a quantity the user can answer, and Billy answers ordinal comparisons, not hour counts.**"
- **`domain-design.md` §10.5, marker `> **THE GUARD CHANGED — Billy 2026-08-23, written in here 2026-08-24; see §6.1.**`** "That also strikes `workload` from this section's list of what the allocation planner reads."
- **`domain-design.md` §9.1.** "`workload` retired 2026-08-23" — one of the two reasons the projection grain is declared dead.
- **`model.md` §8 vocabulary block — NOT REVISED.** The obligation line still reads `due · status{...} · weight · target_date? · **workload?**`. No banner, no strikethrough, no cross-reference to §6.1.

**Changelog:** `domain-design.md` 2026-08-25 — agent — measured: "§9.1's projection grain marked DEAD in place: it read *label/due/status/workload*, but `status` was dropped 2026-08-25 and `workload` retired 2026-08-23. No replacement grain is ruled." `model.md`'s changelog never mentions `workload`.

**Disagreement (cross-file, live and unmarked):** `model.md` §8 keeps `workload?` as a typed obligation field; `domain-design.md` §6.1 (Billy-ruled 2026-08-23) retires it. This is the clearest case of `model.md`'s "frozen" vocabulary section not having been carried forward.

## 33. `status` — the three-axis field

**Revisions**

- **`domain-design.md` §6 table, 2026-08-21.** `obligation` typed: `status`, read by M1 M2 M3 M5.
- **`model.md` §8 vocabulary, 2026-08-22.** `obligation: due · status{completion, score, evaluation} · weight …` — three axes.
- **`model.md` §8.1, [R] Billy, 2026-08-23, referring back to it.** "the three-axis `status` finding: there a scalar `done` **erased** a live item."
- **`domain-design.md` §9.6, `COMPLETED` block, Billy 2026-08-23.** "Same shape as the three-axis `status` finding: `done` was harmful because it was read as terminal and erased a live item, not because it was recorded."
- **`domain-design.md` §9.1, 2026-08-25.** "`status` was dropped 2026-08-25".
- **`domain-design.md` §6, in-body supersession note.** `status` is listed among the six fields "in the schema graveyard".

**Changelog:** `domain-design.md` 2026-08-25 — agent — measured (the §9.1 entry above) is the only record that `status` was dropped, and it records the date without a ruler beyond "agent — measured".

**Disagreement (cross-file, live and unmarked):** `model.md` §8's vocabulary still types `status{completion, score, evaluation}` on obligation and `model.md` §4 lists `status` in ring 0's field set; `domain-design.md` records `status` as dropped 2026-08-25 and graveyarded. `model.md` was edited on 2026-08-28 (three changelog entries) without touching either passage.

## 34. `progress` — its carrier, and its default

**Named:** `progress` (both files); "an annotation with its own kind" (`model.md` §8.2, `domain-design.md` §6.2); "a fifth typed row" (rejected framing, `domain-design.md` §6.2); "a sticky-note kind" (rejected framing).

**Revisions, in order**

1. **`domain-design.md` §1 ruling 6, Billy, 2026-08-21, marker `## 1. Billy-ruled in this session`.** "**Progress is independent of obligations** (option B). Not all time is spent on assignments/exams; a topic inside a chapter can carry progress with no deliverable attached."
2. **`domain-design.md` §6 table, 2026-08-21.** `progress` is a typed fact type: `id · course · target · open/closed · updated_at`, free text "where I am", read by M1 M4. `target` polymorphic.
3. **Demotion to a sticky-note kind — 2026-08-23**, referenced in both files but written out in neither. Its two grounds are quoted: "*The ordinal invited invention*" and "*no mechanism reads it*".
4. **`model.md` §8.2 / `domain-design.md` §6.2, [R] Billy, 2026-08-24.** "`progress` is an **annotation with its own kind**, targeted by an `about` link, carrying `state` (an enum), `detail` (prose), `origin` and `updated_at`. The high-level state is typed; the detail stays prose." Field grain deferred to `spec/schema.md` §4.5. "It shares one shape with `sticky_note` - `annotation` is a **tag, not a type hierarchy** - so `look_at` returns `{summary, annotations[], edges[]}` and note-on generalises to `about`." Both files state the demotion's two grounds are "**answered, not overridden**".
5. **`model.md` §8.2, restated 2026-08-28, [R] Billy.** The *ordinal invited invention* fault "is a **defaulting** fault, and it is fixed by **defining** the default rather than by removing the field: **`state` is not nullable** and an obligation with no progress record reads as **`not_started`**."

**Changelog — this is where the reasoning lives, and the two files' changelogs disagree**

- `model.md` 2026-08-25 — Billy 2026-08-24 — ruled: "§8.2 rewritten: `progress` is its OWN kind, not a sticky-note kind. The 08-23 demotion is overturned; its two reasons are answered rather than overridden (**the *ordinal invited invention* fault was defaulting, fixed by null-renders-as-absence**; *no mechanism reads it* is now false)."
- `model.md` 2026-08-28 — Billy — ruled: "§8.2's fix for the *ordinal invited invention* fault is restated: **the fault is fixed by a DEFINED default, not by rendering absence.** `progress.state` is no longer nullable and an obligation with no progress record reads as `not_started`. What the run did wrong was invent a default where none was specified; specifying one removes the invention."
- `domain-design.md` 2026-08-25 — Billy 2026-08-24 — ruled: "§6.2 rewritten: `progress` is its OWN kind, matching `records/schema.md` §4.5. The sticky-note-carrier form is retracted."
- `domain-design.md` changelog has **no 2026-08-28 entry for progress**, and its §6.2 body still carries the superseded fix: "The first is a **defaulting** fault, **fixed by rendering null as absence**".

**Disagreement (cross-file, live):** `model.md` §8.2 (2026-08-28, Billy, ruled) says `state` is **not nullable** and the fix is a *defined default*; `domain-design.md` §6.2 says the fix is *rendering null as absence*. The 2026-08-28 restatement landed on one side of the corpus only.

**Disagreement (within `model.md`):** its own changelog carries both the 2026-08-25 "fixed by null-renders-as-absence" line and the 2026-08-28 "fixed by a DEFINED default, not by rendering absence" line, unreconciled — by design, since the changelog is append-only, but a reader taking the changelog as the reasoning record meets both.

**Note:** `model.md` §2's parenthetical still calls Billy-stated progress "a ring-0 row per `domain-design.md` §1.6"; §6.2 rules it is not a typed row.

## 35. `weight` / `worth_percent` / `grade_share`, and the `conditional` marker

**Named:** three names appear for one field — `weight` (`model.md` §8 vocabulary), `worth_percent` (`model.md` §10.9 ruling), `grade_share` (`model.md` §7.1's list of an obligation's copied fields). The records never say they are the same field; nothing distinguishes them either.

**Revisions**

- **`model.md` §8 vocabulary, 2026-08-22.** `obligation: … weight …`.
- **`model.md` §10 item 9, added by the derivation 2026-08-22.** "**Conditional rules do not fit scalar fields.** *'10/10/30 or 0/0/50, whichever works out better for you'* and *'12 late days, at most 3 per assignment'* are the allocation planner's actual inputs and are rules, not numbers. `weight` is now a field; the conditional form is not yet expressible."
- **`model.md` §10.9, marker `> **RESOLVED for conditional weighting — Billy 2026-08-23, written in here 2026-08-24; the late-day budget is NOT resolved and stays open.**`** "**[R]** Billy ruled **the minimal fix**: `worth_percent` keeps its value and gains a `conditional` marker plus a pointer to the rule, so no reader can take the stored number for a stated fact. **Billy rejected the general form** — a `weighting_scheme` naming the alternatives with a derived weight — as over-built for what is so far one concrete weight calculation. The supporting observation: nothing in 60 runs ever attempted to compare the two branches, so the ability to compare them is **unevidenced**."
- **`model.md` §10.9, why it escalated.** "Across 60 graded runs the conditional printed as a fixed number is the **top-ranked faithfulness defect** — 24 claims across 17 runs, and the only defect kind that appears in *every* group, i.e. the only one that is a property of the schema rather than of a configuration. With rank 6 (a floor restated as a point value) it is 29 of 77, **38% of every measured faithfulness failure**. The sharper statement of the mechanism, from E7: **the agent acts on a note that NEGATES a field and cannot act on a note that makes a field CONDITIONAL.**"
- **Same block, an overstatement corrected.** "the E0/E5/E7 result that free text is **read and not applied** — placement, bulk delivery, active fetch and self-initiated search were all excluded as the cause. The often-repeated *'four delivery paths'* phrasing is an **overstatement corrected by adversarial review** — two mechanisms, two of them n = 1. The measurement, not the phrasing, is what carries the ruling."
- **The late-day budget** ("12 late days, at most 3 per assignment") is explicitly **not resolved** and "stays open".
- **`model.md` §10.7, derivation, 2026-08-22.** Related: "The course outline is the only carrier of grade weights (without it, 9 of 12 graded items have none and the planner runs blind)."

**Changelog:** silent in both files.

**Disagreement (naming, within `model.md`):** `weight`, `worth_percent` and `grade_share` are used for what reads as one field, across §7.1, §8 and §10.9, with no reconciliation.

## 36. `label` — is it a name or a summary?

**Revisions**

- **`model.md` §8 vocabulary, 2026-08-22, agent-drafted.** `id · course · layer(...) · **label(free text, written once at ingest)** · added_at` — on **every** node, unqualified.
- **`model.md` §7.2, [R] Billy, 2026-08-23, marker `> **PROMOTED 2026-08-24 (ruled 2026-08-23)**`.** "at ingest an LLM writes a document's summary, tags and sections, and **`label` is that output** — §8's *'label (free text, written once at ingest)'* means **written**, not **named**."
- **`model.md` §7.2, marker `> **UNRESOLVED, and it must not be smoothed over.**`** "§7's own table above enumerates *labels, summaries, sticky notes* as distinct things, and §4's store column lists a separate `summary`. Reading `label` **as** the ingest-written summary is the 08-23 ruling; **reconciling it with §7's enumeration was never done.** See `openclaw:fall26/2026-08-23-slice-1/INCONSISTENCIES.md`."
- **`model.md` §7.1, [R] Billy, 2026-08-28.** "**an obligation carries no ingest-written summary.** … The 2026-08-23 adversarial objection — that §8's node line gives `label` to every node without qualification — **does not survive, because that node line is agent-drafted and never had standing to block a ruling.**"
- **`model.md` §7.1, agent-stated corollary.** "**A summary is written where a node's identity IS content the skeleton does not hold**, which is the artifact and nothing else in the current kind set. A concept carries no state and is not a handle to anything, so it does not get one either."
- **`model.md` §10.5, marker `> **WIDENED 2026-08-24, on the 2026-08-23 ruling** (§7.2)`.** "*'the only route'* is false. **`label` is a second unbounded route** — it is the ingest-written summary, and a summary plus tags plus sections is not the 'one line each' §4 promises."

**Changelog:** `model.md` 2026-08-28 — Billy — ruled: "§7.1's obligation-label question is settled: an obligation carries no ingest-written summary. The NOT SETTLED block is removed. The 08-23 adversarial objection rested on §8's node line giving `label` to every node, and that line is agent-drafted, so it never had standing to block a ruling. The walk argument stands as the reason: an obligation's content is its `role=given` artifact's summary, one hop away, and the obligations with no artifact really are only a name."

**Disagreement (within `model.md`, two layers of it):**
1. §7.2 rules `label` **is** the ingest summary; §7's own table and §4's store column treat labels and summaries as distinct. The document marks this `UNRESOLVED` and says reconciliation "was never done".
2. §8's node line gives `label` to every node; §7.1 (2026-08-28) says obligations get no ingest-written summary and, since label **is** the summary, disqualifies §8's line as agent-drafted. §8's line was left unedited.

## 37. What ingest produces, and who reads each part

**Revisions**

- **`model.md` §7.2, [R] Billy, 2026-08-23, table.** summary = "concise **at birth**, not trimmed later", read by the coordinator; tags = "implies an enum set — **deliberately not settled now**", read by filtering; sections + pages = "the index depth goes in through", "**not the coordinator's responsibility**".
- **`model.md` §7.2, [R] (no date given).** "A sticky note renders **together with** the summary. Whether that pairing costs too much is a token-optimisation question for later, not a design question now."
- **`domain-design.md` §10.2, Billy's correction, 2026-08-22.** "**§5 ruled out a *manual* taxonomy, not an LLM pass at ingest.** Since a multimodal pass must run anyway — scans, `.docx`, `.pptx` — section labels are its byproduct, and mechanical extraction is at most a cheap prior. Most of P2's negative findings were artifacts of testing a method nobody had proposed."
- **`domain-design.md` §10.2, method-independent survivals.** "the corpus is **not** PDFs (one course holds 11 `.docx`, 2 `.pptx`, 1 `.xlsx` against 9 `.pdf`); an image-only material class exists; and **Billy's own artifacts are separable from the professor's by a MacID in the filename**."

**Changelog:** silent.

## 38. A date-only `due` means the end of that day

**Revisions**

- **`model.md` §8.3, marker `> **PROMOTED 2026-08-24 (ruled 2026-08-23)** from openclaw:fall26/2026-08-23-slice-1/experiments/E10R-RESULTS.md §1. It is a schema convention, so it belongs in the vocabulary rather than in an experiment write-up.`** "`2aa4-a3`'s due was stored date-only, `\"2026-03-20\"`, and parsed to **`T00:00`, the start of the day**, against `2c03-a7`'s `T23:59`. *'Due March 20'* means its **end**. Consequence, measured: 2aa4's three dated obligations, and every `done_by` derived from them, were **a day early in all 60 runs** of the slice-1 cycle. Normalised to end-of-day."
- **Same section, the general lesson.** "**It was found only because it invalidated an experiment's tie.** Nothing tested it, nothing errored, and its production signature would have been silent. **A date without a time needs an explicit convention at the schema level, not at the parser's discretion.**"

**Changelog:** silent.

## 39. `backing` — from `unchunkable_media` to per-region `text_extractable`

**Revisions**

- **`model.md` §8 vocabulary.** `artifact: backing(materialized_doc | code_project)`, `files[]{ variant, text_extractable } · revised_at`.
- **`model.md` §9.** "**`backing: unchunkable_media`.** Retracted — a guess about file type, and the axis was wrong. Falsified four ways in one slice: PDFs with **no text layer at all** (scanned handwriting, and Billy's OneNote exports, which an extension rule would route to `pdftotext` and yield a **confidently empty chunk set nothing downstream complains about**); a text PDF whose exercises **are images**, so backing is not uniform *within one file*; a `.png` carrying a rendered prose block, more chunkable than several PDFs; and one diagram held as both `.drawio` and `.png`."
- **Same, the replacement axis.** "The real axis is **whether meaning survives linearization** — a property of the materialization pass, not of the file. In a pattern diagram the labels linearize but **the edges are the content**. Replaced by a per-region `text_extractable`, default false, set true only when a pass actually recovered text. **Its reading mechanism is §7's trust contract: distinguishing a quotation from a generated description.**"

**Changelog:** silent.

## 40. `parts`, `count`, `target_date`, `revised_at`

**Revisions**

- **`model.md` §8 vocabulary, 2026-08-22.** `obligation: … target_date? … parts[] (independently assessed, carrying their own status and score) · count{done,of} (for countable obligations: tutorial participation, 10 of 12)`; `artifact: … revised_at`.
- **`model.md` §7.1, [R] Billy, 2026-08-28.** `parts` is given a second reading mechanism: what the coordinator needs to know an obligation arrives from "the copied fields (`name`, `due`, `grade_share`), **`parts` for which concepts it contains**, and the artifact's summary one hop away."
- **`domain-design.md` §6.1, [R] Billy, 2026-08-23.** `parts` is given a third: "**Size is observed ordinally** — from `parts` and item notes first".
- **`model.md` §8, `supersedes` cut.** `revised_at` is the replacement for the cut edge; it is also the evidence test for "evidenced staleness" in §8.1.

**Changelog:** silent.

**Note:** `model.md` §7.1 names an obligation's copied fields as `name`, `due`, `grade_share`. §8's vocabulary has `label`, `due`, `weight`. Neither `name` nor `grade_share` appears in §8.

---

# Part E — Sticky notes and annotations

## 41. The sticky-note mechanism, and the maintenance point

**Revisions**

- **`domain-design.md` §10.7 ruling 2, Billy, 2026-08-22.** "**Corrections are sticky notes, not precise updates.** A correction does not need to be applied so that the corpus is accurate; it needs to be attached to the section it concerns, visibly. Co-location is enough because Billy is in the loop reading it. **This kills the corpus-override layer the agent was drafting.**"
- **`model.md` §8.1, marker `> **PROMOTED 2026-08-24 (ruled 2026-08-23)** from openclaw:fall26/2026-08-23-slice-1/experiments/NOTE-MECHANISM.md §1–§5, which is now evidence and process only.`** "§8's edge table above types `sticky_note → node`; **it never said how a note is kept true.**"
- **`model.md` §8.1, [R] Billy, 2026-08-23 — "the maintenance point is the READ":** "sticky_note 既然能被 attach，那肯定能被 detach 或者 modify，并且要是便宜的。假如 agent 当 lookup(course) 之后看到了某个 sticky_note 已经过时，他能'顺手'便宜的改写或者撤掉，不带任何 burden。" Consequence: "Attach, detach and modify are all cheap and symmetric because a note is an **entity that points at a node**, not a property of one."
- **`model.md` §8.1, marker `**agent reasoning, not a ruling**`.** "Maintenance-by-render maintains exactly the subset that matters and neglects exactly the subset whose neglect is free. … A periodic sweep would spend its cost precisely where nothing depends on the result."
- **`model.md` §6 scenario 6.** "a correction arrives | — | ✅ attach a sticky note | ❌ **untouched** (`domain-design.md` §10.7 ruling 2)."
- **`model.md` §8.2, Billy 2026-08-24.** The sticky note is generalised: `annotation` is "a **tag, not a type hierarchy**"; note-on generalises to `about`.

**Changelog:** silent on the mechanism itself.

## 42. Who may declare a note stale

**Revisions**

- **`model.md` §8.1, marker `**Who may declare a note stale — derived from §2, not separately ruled.**`** Two cases: **evidenced staleness** (a correction note says "the fixed version is on Avenue" and `revised_at` now post-dates it) → "rewrite or detach it in passing"; **staleness only Billy can know** ("I've done part 1 of A6") → "**surface it for confirmation, never resolve it**". Derived from §2's stateless-modelling ruling.

**Changelog:** silent.

## 43. Provenance does not confer immutability

**Revisions**

- **`model.md` §8.1, [R] Billy, 2026-08-23.** "从系统的角度来说，'公告来的事实'和'用户嘴里说出来的事实'都是事实，我不需要用一个截屏来证明我说的就是对的。"
- **Same, retraction.** "An earlier agent draft — *origin-bearing notes are append-only, self-authored notes are editable in place* — is **retracted**. Its premise was false: §8's merge of `announcement → node mentions` into `sticky_note.origin` keeps a **flat provenance log**, so the announcement text lives there and the note is the extracted meaning. Editing a note destroys nothing. Residual, an implementation detail rather than a rule: an edit carries `origin` forward by default and may drop it."

**Changelog:** silent.

**Cross-reference tension worth noting:** `domain-design.md` §4 rules "**All dangerous inputs are external.** Billy-authored input (notes, code, spoken status) is never a dangerous rewrite — he is the authority on his own state." `model.md` §8.1's conflict-detection ruling (thing 2) says a spoken "done" against a portal record must be surfaced as a conflict rather than accepted. The two are not obviously the same posture; neither cites the other.

## 44. Note CRUD confirmation, and the dev toggle

**Revisions**

- **`model.md` §8.1, [R] Billy, 2026-08-23.** "**note CRUD asks a short confirmation during development**, and the behaviour is observed, *'像一个 toggle 一样'*."
- **Same, marker `**Agent addition, not ruled:**`.** "an exit condition, because a dev toggle without one becomes permanent by inertia — it turns off after N consecutive confirmations that are approvals with no correction, and any correction resets the count to zero. **Agent proposal, explicitly flagged as arbitrary: N = 5. There is no evidence behind the number.**"

**Changelog:** silent. **Container-sensitive** — "during development" is a mode of the standalone app's own build cycle.

## 45. A length bound on sticky notes — and, widened, on `label`

**Revisions**

- **`model.md` §10 item 5, 2026-08-22, owed.** "**A length bound on sticky notes.** ~~The only route~~ by which unbounded free text can enter a resident skeleton. Bound them at write time or the skeleton quietly grows."
- **`model.md` §10.5, marker `> **WIDENED 2026-08-24, on the 2026-08-23 ruling** (§7.2)`.** "*'the only route'* is false. **`label` is a second unbounded route** … This owed item must cover both, and **it now gates `domain-design.md` §9.2's symmetry rule**: eight one-line summaries can be pulled for a comparison set; eight paragraphs cannot."
- **`model.md` §10.5, marker `> **MEASURED 2026-08-28, and it corrects this item's own premise.**`** "*Real samples are short* is false. The 11 notes of the 2c03 corpus run **87 to 278 characters**, against the **~90** that `spec/write-rules.md` §4.2's worked compression produces, and rendering the course level puts **871 characters** of course-scoped notes ahead of its first obligation row. The bound's input is what a rendered level can carry, so it is **owed out of the presentation cycle rather than settled in advance**."
- **`domain-design.md` §9.2, `RESTATED` block.** "**A cost that is owed, not paid.** Affordability is now load-bearing, and the length bound that decides it is still unwritten — `model.md` §10.5, widened the same day."
- **`model.md` §7.2.** "§4 says the skeleton is *'one line each'*. A summary is one line; a summary plus tags plus sections is not."

**Changelog:** `model.md` 2026-08-28 — agent — measured: "**§10.5's premise *real samples are short* is falsified by the corpus.** The 11 real notes run 87-278 characters against the ~90 that §4.2's own worked example produces, and a course level opens with 871 characters of course-scoped notes before its first obligation row. The owed bound is therefore larger than a tidy-up, and its input is what a rendered level can carry."

**Note on banner ordering:** §10.5 carries the 2026-08-28 `MEASURED` banner **above** the 2026-08-24 `WIDENED` banner, so the section reads newest-first while the surrounding document does not.

---

# Part F — The coordinator, sessions, and agent topology

## 46. The coordinator is long-running, not booted per session

**Revisions**

- **`domain-design.md` §1 ruling 11, Billy, 2026-08-21.** "**The coordinator is long-running, not booted per session.** Billy faces one persistent, high-level, conversational master session; depth only exists in freshly opened, targeted subagents."
- **`domain-design.md` §5.** "The 'master session' is a **long-running coordinator**, not a per-session boot (corrected 08-21 — see §9.1). Its loop is read the projection → triage → replan when asked."
- **`domain-design.md` §9.1.** "An earlier draft had a two-stage assembly at session start. That was wrong: the coordinator is long-running (1.11)."
- **`domain-design.md` §9.5.** "**do not try to make it survive a semester.** Its long-running scale is days-to-weeks."
- **`domain-design.md` §9.3.** "This is the only reason it can run long - purity is not fastidiousness, it *is* the longevity mechanism."

**Changelog:** silent. **Container-sensitive** — the whole notion of a persistent master session is a property of the app the human sits in front of.

## 47. Session topology: semester / course / task

**Revisions**

- **`domain-design.md` §5, 2026-08-21, unattributed.** "There is no master/slave and no orchestrator — no control relationship, only a scope parameter. **Coupling is through the store, never through a call.**" Three layers: semester = all courses, shallow, "**a real working session** — cross-course planning is reasoning, not a view"; course = one course, persistent, "**state is what persists, not a session**"; task = one assignment/topic, deep, "this is where sessions live; scope loaded at entry".
- **Same section.** "**'Just-enough depth' has a precise definition: enough to triage, not enough to work.** Depth beyond triage is waste, and §9.2 shows it is worse than waste — it biases allocation."
- **`domain-design.md` §9.4.** "There is no queue, no ack and no cursor here, because there is no second party that might be asleep - **the store is the channel.**"

**Changelog:** silent. **Container-sensitive** throughout.

## 48. No fold

**Revisions**

- **`domain-design.md` §5, 2026-08-21.** "**No fold.** Fairy needs one because domains emit prose-grained events at volume; fall26's facts layer is small and structured, so the coordination layer reads all of it every time. No cursor, no compression, no staleness."
- **Same section.** "**Structurally isomorphic to Fairy↔domains — steal the shape, not the mechanism.** … Fairy solves *delivery*; fall26 solves *allocation* … One human, one store, no delivery problem — so dispatch/ack/fold are all unnecessary here."

**Changelog:** silent. **Container-sensitive** — a claim about a sibling system's mechanism set.

**Note:** the "reads all of it every time" premise is the same one `domain-design.md` §3's `PARTLY SUPERSEDED` banner calls false as written for ordinary conversation; §5 explicitly ties itself to §3 ("This is the same reason the coordination layer needs no fold (§5)" — `domain-design.md` §3). The §3 banner does not propagate to §5.

## 49. Course ≠ domain

**Revisions**

- **`domain-design.md` §5, 2026-08-21.** "The domain contract (registry entry, episodes, /wrap, /standup, ack protocol) is repo-level ceremony; six courses times that is exactly the cloned-build-repo-furniture mistake ruled out. **fall26 is ONE domain; the coordination layer is internal to it.**"

**Changelog:** silent. **Container-sensitive** — the entire vocabulary (registry, episodes, /wrap, /standup, ack) is the old container's.

## 50. Who may touch what — the data-flow rule

**Revisions**

- **`domain-design.md` §9.3, 2026-08-21, named an agent draft by §9's header.** A responsibility table: coordinator does conversation/judgement/advice, dispatching, plan generation ("its only substantive work, because it *is* coordination"); ingestion subagent returns "**one-line receipt**"; deep-read subagent returns "**the conclusion, never the material**"; task subagent (Billy enters it himself) returns "one-line status at the end"; preference extraction at close-of-session. "**Derived tool surface for the coordinator: read the fact projection · write plans · dispatch. No corpus retrieval, no file reads, no fact writes.**" And: "**subagents swallow the process and emit only conclusions.**"
- **`model.md` §7, 2026-08-22.** Reframed: "The invariant is a **data-flow rule, not an agent topology**. Design §9.3's real contract is *'subagents swallow the process and emit only conclusions'*; a spawned subagent, a dedicated session Billy opens himself (already in §9.3's own table), and a task session are all implementations of it. > **Store output enters the coordinator only as a conclusion; the context that produced it is then discarded. Who produced it is irrelevant.**"
- **`model.md` §7 table.** coordinator: ring 0 ✅ resident · skeleton ✅ may query, does not hold · store by-handle ❌ · store by-query ❌ · write plans ✅ · dispatch ✅. ephemeral context: read · read · ✅ · ✅ · ❌ · ❌. ingest: ✅ write across all four, ❌ plans, ❌ dispatch.
- **`model.md` §7, [R] Billy, 2026-08-22.** "the coordinator may not call the store (context pollution), but **rendering a node's own concise summary is a skeleton read and is obviously allowed** — otherwise it cannot read or analyse anything."

**Changelog:** silent.

**Disagreement (cross-file):** `domain-design.md` §9.3's derived tool surface for the coordinator is three items — read the projection, write plans, dispatch. `model.md` §7 adds a fourth (query the skeleton) and §7.1 names it as a verb (`look_at`). `domain-design.md` §9.3 was never amended, and its §9 header still lists §9.3 as an agent draft while `model.md` §7's expansion of it carries a Billy `[R]`.

## 51. Progressive disclosure, and what the coordinator holds resident

**Revisions**

- **`domain-design.md` §9.1, 2026-08-21, later confirmed as a ruling.** "**The coordinator's view is fixed-shape and uniform-depth. It refreshes as facts change and never deepens.** … The projection carries every course's obligations, time-points and the current plan, with **no free text**." And: "the coordinator's persistent memory holds **pointers and summaries, never content**. Retrieval on demand is only half the fix - the other half is *not sedimenting* what was retrieved."
- **`domain-design.md` §9, [R] Billy, 2026-08-23.** "**§9.1 and §9.2 are rulings**, not agent drafts. The header above names 9.0 and 9.3-9.5 as drafts and was silent on these two, which left their status underivable from the document — a reviewer flagged it, and **a session had already cited them as textually settled without checking.**"
- **`domain-design.md` §9, the reviewer's separate and still-valid point.** "§9.1 enumerates the projection positively and removes one thing (free text) with a reason. **It never says 'ring 0', and the gloss *'ring 0 was arrived at by subtraction'* is a later paraphrase, not this section's words.**"
- **`model.md` §7, [R] Billy, 2026-08-22.** "**progressive disclosure is the design philosophy, and ring 0 is everything the coordinator actually needs.** Nothing requires a CLI fetch to render all N + E. > **The coordinator holds ring 0 resident and *queries* the skeleton on demand. It does not hold the skeleton.**"
- **`model.md` §7, retraction.** "An agent draft had the coordinator holding the whole skeleton resident. **Retracted** - `domain-design.md` §9.1's projection was always `obligations · time-points · plan`, i.e. ring 0. (§9.1's field grain is dead and no replacement is ruled; the entity list is what this retraction rests on.) Billy's earlier correction was that a node's summary *can be called*; that was elaborated into *is permanently held*, which the design never said."
- **`domain-design.md` §9.1, [R] Billy, 2026-08-24.** "**the symmetry rule does not conflict with this.** §9.1 governs the **view** … The symmetry rule governs what a **judgement** may observe inside its own scope, and those observations are **transient** … **The view does not deepen precisely because what is fetched is dropped.** So §9.1 is unmodified; only §9.2's 'allocation reads ring 0 only' was replaced."

**Changelog:** `model.md` 2026-08-25 — agent — measured: "§7's retraction paragraph no longer states the projection's field grain. The entity list (obligations, time-points, plan) survives; the *label/due/status/workload* grain does not." `domain-design.md` 2026-08-25 — agent — measured, and 2026-08-28 — Billy — ruled (the grain's replacement is `spec/ring-0.md`, "not here").

**Disagreement (cross-file):** `model.md` §7 leans on the equation "§9.1's projection … i.e. ring 0". `domain-design.md` §9 (Billy 2026-08-23) records the reviewer's still-valid point that §9.1 **never says "ring 0"** and that the equation is a later paraphrase. `model.md` §7's retraction rests on that paraphrase; the paraphrase's status is contested on the other file's side.

## 52. Ring 0's field set

**Revisions — four non-identical lists**

- **`domain-design.md` §9.1 (dead grain).** `label / due / status / workload` — declared dead 2026-08-25, "**No replacement grain is ruled**" (changelog) and replaced 2026-08-28 by `spec/ring-0.md`, not read here.
- **`domain-design.md` §10.5.** what the allocation planner reads: "`due`, `workload`, `status`, `course`" — `workload` struck by §10.5's own `THE GUARD CHANGED` banner.
- **`model.md` §4.** "ring 0 / obligation layer … owns time and commitment: `due · status · course · plan`".
- **`model.md` §8.** obligation typed fields: `due · status{...} · weight · target_date? · workload? · parts[] · count{}`.

**Changelog:** `domain-design.md` 2026-08-28 — Billy — ruled: "**§9.1's dead grain has a replacement, and it is not here.** `spec/ring-0.md` carries the membership test, the active/known bands and the field set; §9.1 keeps only the standing constraints that record inherits."

**Disagreement:** four lists, none identical, and the authoritative one is outside this corpus.

## 53. The symmetry rule (formerly "allocation reads ring 0 only")

**Revisions**

- **`domain-design.md` §9.2, 2026-08-21, later confirmed a ruling.** "**All five courses' views must be isomorphic and fixed-depth. Uniformly shallow beats one deep and four thin.**" With the dispatch escape: "the coordinator **dispatches an estimate** and receives back a value *in the same shape as the other four*."
- **`model.md` §7 mechanism 1, 2026-08-22, agent, now struck through in place.** "~~**Allocation reads ring 0 only.**~~ §1.12(b)'s harm is specifically that *weighting judgment* gets polluted, and weighting is allocation."
- **`model.md` §7, marker `> **REPLACED — Billy 2026-08-23, written in here 2026-08-24** — by the **symmetry rule**, written out at `domain-design.md` §9.2`.** "*observe anything you can afford for every course at once; never observe anything you can only afford for one.* **What forced it:** the slice-1 blind run gave the planner an observation space of deadlines and weights alone and it produced a date-ordered queue, which says more about the observation space than about ring 0. **The invariant was never shallowness — it is uniformity** … **Ring 0 returns to being the layer that is RESIDENT, not the definition of what is observable.**"
- **`domain-design.md` §9.2, marker `> **RESTATED — Billy 2026-08-23, written in here 2026-08-24 — the observation rule is SYMMETRY, not residency.**`** Adds: "**Symmetry is scoped to the set the judgment ranges over**, not unconditionally to all five courses." And the derivation of why ring 0 was wrong: "Ring 0 was arrived at by subtraction … and that subtraction presumed we already knew what coordination needs."
- **Standing, recorded in both files because it was contested.** `model.md` §7: "this began as an agent proposal that overrode a ruled entry, was flagged by adversarial review as unruled, and was **then ruled by Billy on 2026-08-23**. `openclaw:fall26/2026-08-23-slice-1/doubt/RECONCILE.md` §5 still lists it as open and is stale on that point." `domain-design.md` §9.2 carries the same paragraph.
- **`domain-design.md` §9.2, marker `**What is NOT established.**`** "§9.2's premise that a thin line drives an estimate request remains **untested**: the blind run's 2–2 course split was read as evidence against it and that reading was withdrawn (per-run counts 2,2,0 / 0,2,5 — no signal at that variance). One instance of the predicted shape appeared later, in 1 run of 3. **Neither supported nor refuted.**"

**Changelog:** silent in both files, despite both files marking the replacement in place.

**Disagreement:** the two files now agree post-ruling, but both record that a **third** document (`RECONCILE.md` §5) still lists the question as open. That is a disagreement the corpus itself names and could not close from inside.

## 54. Expansions are discarded, never sedimented

**Revisions**

- **`domain-design.md` §9.1, 2026-08-21.** "Retrieval on demand is only half the fix - the other half is *not sedimenting* what was retrieved." And: "Depth is added only inside ephemeral subagents, and does not come back."
- **`model.md` §7 mechanism 2, 2026-08-22.** "**Expansions are discarded, never sedimented** … Optional when the skeleton was resident; **mandatory now.** Without it a long-running coordinator converges on held-everything *plus* path-dependent bias — both costs, no benefit."
- **`model.md` §7 `REPLACED` banner and `domain-design.md` §9.2 `RESTATED` block, both.** "Mechanism 2 (expansions are discarded, never sedimented) and the store boundary are **unaffected** / **untouched**."
- **`model.md` §7.** "The store boundary remains the chokepoint for content; **discard discipline is the new one for structure.**"

**Changelog:** silent.

## 55. `look_at(node_id, question)` — the coordinator's material verb

**Revisions**

- **`model.md` §7.1, marker `> **PROMOTED 2026-08-24 (ruled 2026-08-23)** … Forced by §5's revised three-level table, which denies the coordinator **both** store modes and so leaves the permitted operation unnamed.`**
- **[R] Billy, 2026-08-23, verbatim:** "给 A2 obligation 和它的 child 加一个 edge 不就行了？agent 看到了 A2 obligation node，因此它想知道具体的 spec 是去顺着那个 node 走一遍，不需要做整个 corpus 的 find_material。"
- **`model.md` §7.1, the finding.** "**The edge already exists** — §8's `obligation → artifact (spec, role ∈ {given, owed})`. **Nothing is missing from the model; what was wrong was the operation**, and it was wrong in the slice-1 apparatus rather than in the design." Walk vs search table: walk = "deterministic, O(degree), no store, no embeddings", coordinator ✅; search = "ANN over the store … affordable once, not eight times", coordinator ❌.
- **Signature.** `look_at(node_id, question) -> { summary, sticky_notes[], edges: [{ role, direction, target_id, target_summary }] }`.
- **Hard constraint.** "**It returns no sections, no pages, no paragraph, no chunk.** Even where the store's underlying data holds content, the verb must not surface it — `domain-design.md` §9.0: **the boundary is the tool surface, never self-restraint.**"
- **Instance count corrected.** "The `obligation → artifact (spec)` edge runs to roughly **53 instances across both courses**; the ~45 figure quoted through the 08-23 session is 2c03 alone."
- **`model.md` §8.2, Billy 2026-08-24.** Return shape revised without editing §7.1: "`look_at` returns `{summary, annotations[], edges[]}`".

**Changelog:** silent on `look_at` itself.

**Disagreement (within `model.md`):** §7.1's signature returns `sticky_notes[]`; §8.2 says it returns `annotations[]`. §7.1 was not updated.

**Container-sensitive** — a named tool with an enforced parameter is a property of the app's tool registry.

## 56. The `question` parameter, and its retirement condition

**Revisions**

- **`model.md` §7.1, [R] Billy, 2026-08-23.** "预期猜测这个问题，不如 dev 模式让它调用的时候问出这个问题。" → "The question is **not to be predicted but stated at call time**, and the parameter is **required** so it is enforced at the tool surface rather than requested in a prompt."
- **Two honesty caveats recorded at the source.** "it **perturbs what it measures** (requiring an agent to say why it is calling makes the call more deliberate — constant across arms, so it does not confound a comparison, **but it must never later be reported as a finding**)", and "it **doubles as a test of read-time filtering**".
- **`model.md` §4.1, retirement condition. [R] Billy, 2026-08-23:** "within the development cycle, once summaries answer the questions at some threshold, the parameter retires." Then, marked "**The threshold is an agent proposal, both conditions required and the number explicitly flagged as arbitrary**": (1) ≥ **80%** of `look_at` calls have their stated question answered, across one full three-run arm; (2) the round produces no question kind absent from the previous round. "The agent's position is that **(2) matters more than (1)**."

**Changelog:** silent. **Container-sensitive** — "dev 模式", "within the development cycle", "three-run arm" are all properties of the app's own experiment apparatus.

## 57. Multiagent — one justified use, two rejected

**Revisions**

- **`domain-design.md` §8, 2026-08-21, marker `Raised by Billy; analysis below is draft, not ruled.`** "❌ per-course *expert* agents — what actually differs between courses is a working-instruction bundle, which lives in the preferences layer and loads with the scope. Not an agent. ❌ orchestration / master-slave — coupling is through the store (§5). ✅ **context-isolated deep reads** … **This is justified by context economy, not expertise.**"
- **`domain-design.md` §7.** Listed as "**Multiagent / expert mechanism** (raised 08-21) — see §8, resolved into the responsibility table §9.3" under `## 7. Open — not yet ruled`.
- **`model.md` §7.** Generalised away from topology entirely: "The invariant is a **data-flow rule, not an agent topology**."

**Changelog:** silent. **Container-sensitive.**

## 58. Disposability — the acceptance criterion

**Revisions**

- **`domain-design.md` §9.5, 2026-08-21, named an agent draft by §9's header.** "> **If losing the coordinator session loses information, the design is wrong.** … Under 9.3 it holds nothing unique … So it can be thrown away and rebuilt at the cost of one projection read." Corollary: "**do not try to make it survive a semester.** Its long-running scale is days-to-weeks. The known ailment of long sessions … is not solved - it is **made not to matter** … Any change that makes losing the coordinator painful is moving backwards."

**Changelog:** silent. **Container-sensitive** — the acceptance criterion is about a session object the successor container may not own.

## 59. A shape for returned conclusions — owed

**Revisions**

- **`model.md` §10 item 4, 2026-08-22, owed.** "**A shape for returned conclusions.** 'Emit only conclusions' is a promise, not a mechanism, until the return value has a required form (`domain-design.md` §9.2's estimate — *'a value in the same shape as the other four'* — is the template)."
- **`domain-design.md` §9.6, `COMPLETED` block, Billy 2026-08-23.** The same return contract is extended to the user: asking Billy "is §9.2's dispatch with the **user** as target instead of a subagent, and the return contract is unchanged — a value *in the same shape as the other four*."

**Changelog:** silent.

## 60. The trust contract owed for generated content

**Revisions**

- **`model.md` §1, 2026-08-22.** "A separate trust contract is owed for generated content — §7."
- **`model.md` §7, marker `**The trust contract owed for generated content (§1).** Agent position: … **Not yet ruled.**`** "**the system proposes a partition, Billy disposes, and a wrong proposal must be cheap** — it degrades grouping, never destroys anything. Same asymmetry that made ingest judgment non-load-bearing (`domain-design.md` §10.8)."
- **`model.md` §9.** Given a concrete reading mechanism: `text_extractable`'s "reading mechanism is §7's trust contract: distinguishing a **quotation** from a **generated description**."
- **`model.md` §10 item 6.** Scope narrowed by evidence: "Where a course does state it, the concept layer is extraction, not inference — **which correspondingly narrows what §7's generated-content trust contract has to cover.**"

**Changelog:** silent.

---

# Part G — Ingest and inbound

## 61. Ingestion is out of scope; Billy is the fetcher

**Revisions**

- **`domain-design.md` §1 ruling 5, Billy, 2026-08-21.** "**Ingestion is out of scope.** Billy is the fetcher — he opens Avenue, reads announcements, downloads PDFs. The system's boundary starts at the endpoint. It does not need to know how a source arrived."
- **`domain-design.md` §4.** Qualified the same day: "the system does not need to know how a source arrived, but it does need the source's **publication** time, not the ingestion time. Dumping three notices on Sunday in the wrong order would otherwise let an older fact silently overwrite a newer one."
- **`domain-design.md` §10.7 ruling 5, Billy, 2026-08-22.** "Live intake is Billy **pasting a screenshot**, so there is no segmentation problem at all — and **the ingestion endpoint is multimodal from day one**, which both documents currently write as text processing."
- **`model.md` §7, §8, §10.** Ingest is treated as a first-class writer across every layer (`ingest: ✅ write` on all four columns), with owed items about its ordering and dependencies (things 63–64). The word "ingestion" is used in two senses across the corpus — fetching (out of scope) and processing at the endpoint (extensively designed) — and no passage reconciles them.

**Changelog:** silent.

**Container-sensitive** — "Billy opens Avenue and downloads PDFs; the boundary starts at the endpoint" describes where the app sits relative to a human.

## 62. The operations model (file it / apply it) — dead

**Revisions**

- **`domain-design.md` §4, 2026-08-21, unattributed.** Two operations behind one endpoint: "**File it**" (tag + store, append-only, harmless) and "**Apply it**" (an UPDATE, not an INSERT). "Nearly all the pain comes from (2) being handled as (1)." Plus: "**So retirement is not periodic cleanup. It happens at the moment of write.**" And: "**Rewrites come from exactly two places:** announcements, and new versions of obligation-bearing documents. Everything else is pure insert."
- **`domain-design.md` §4 banner, marker `⚠️ **SUPERSEDED 2026-08-22 — see §10.3-10.4.** The operations model was falsified against real material (39% reduction). Its counter-argument to read-time reconciliation survives and is unanswered (§10.8).`**
- **`domain-design.md` §10.1, P5 verdict.** "does the operation set reduce to insert/rewrite/file over five fact types | **FALSIFIED — 39%**".
- **`domain-design.md` §10.3, heading marker `### 10.3 The operations model is dead (P5)`.** "39 announcements of the hardest course produced 137 operations. **53 reduce (39%). 76 do not (55%).**" Three findings: "**The deadline move — the event §4's whole routing design is built around — happened once in a semester.** 21 of 22 executed rewrites were additive free-text appends, not destructive overwrites"; "**§4's ~30 confirmations/semester is not a real number.** Applied to all rewrites it is ~115 across five courses; applied to destructive overwrites only it is 1-2 per course"; "**Retirement is read-time expiry, roughly 7:1 over write-time supersession.** §4's 'it happens at the moment of write' describes only the smaller branch. **This settles D1.**"
- **`domain-design.md` §10.3, target resolution.** "§4 also anticipated only one of three real target-resolution failures. The other two are *value unavailable* ('see Avenue for your specific due date' — there is no 'to' to confirm) and *applicability unknown* (an extension that applies only if Billy filed an accommodation)."
- **`domain-design.md` §10.5.** "**§4 — superseded almost entirely.** Its counter-argument survives and is unanswered; see 10.8."
- **`domain-design.md` §10.8, marker `## 10.8 Agent drafts, not ruled`.** "**§4's unanswered counter-argument, which is the entry point for the next design round.** §4 rejected read-time reconciliation … The agent's judgement is that this holds for an unbounded pile and fails for a scoped, time-ordered set — but **that is an assertion, not a design**, and it is the reason the allocation layer cannot shrink to zero."

**Changelog:** silent in `domain-design.md`'s changelog — the whole §4 supersession predates the changelog's first entry (2026-08-25).

**Disagreement (within `domain-design.md`, explicitly preserved):** §4 is simultaneously "dead", "superseded almost entirely", and the holder of a counter-argument that "survives and is unanswered". §10.5's stated method is why: "the sections above are left intact rather than edited, so the reasoning that produced them stays legible."

## 63. Inbound is to be known, not to trigger an action

**Revisions**

- **`domain-design.md` §10.4, Billy, 2026-08-22.** "> **Inbound does not arrive to trigger an action. It arrives to be known.** … **This is what dissolves the 55%.** Room changes, section-scoped notices, pointers to Avenue paths, an accumulating strike count — none of them needed the system to *do* anything. They needed to be *known*. The operations model forced them into a binary that had no correct branch, and recorded their refusal as failure."
- **`domain-design.md` §10.7 ruling 1, Billy, 2026-08-22.** Restated as a numbered ruling.
- **`domain-design.md` §10.5, consequence the section flags against itself.** "§6's own stated failure mode is 'everything lands in free text, so M1/M2 stop working and the KB degrades into a note pile.' **The reframe walks into that deliberately.** The only thing separating a designed KB from a note pile is that the small allocation layer stays populated."

**Changelog:** silent.

## 64. Confirmation policy

**Revisions**

- **`domain-design.md` §4, 2026-08-21.** "**stratified by operation, not by item:** filing is fully automatic (wrong tag is harmless); rewriting asks, because it is irreversible and overwrites something Billy will later rely on. Roughly **~30 confirmations per semester**." And: "**The hard part of a rewrite is not the confirmation, it is resolving the target.** … the confirmation must present the *target* … not a yes/no."
- **`domain-design.md` §10.3, 2026-08-22.** "**§4's ~30 confirmations/semester is not a real number.** Applied to all rewrites it is ~115 across five courses; applied to destructive overwrites only it is 1-2 per course."
- **`domain-design.md` §6 table, preference row.** "nearly all free text, so it carries no rewrite danger and needs no confirmation."
- **`model.md` §8.1, [R] Billy, 2026-08-23.** A separate confirmation regime for notes (thing 44).

**Changelog:** silent. **Disagreement:** the ~30 figure and the ~115 / 1-2 figures stand in the same file, the earlier one uncorrected in place.

## 65. RAG source classes

**Revisions**

- **`domain-design.md` §1 ruling 9, Billy, 2026-08-21.** "**RAG is accepted for corpus** — one-time embedding at material drop, per-course buckets for independence, metadata filtering. Math-equation chunking is a known industry problem and is deferred."
- **`domain-design.md` §10.7 ruling 3, Billy, 2026-08-22.** "**RAG stores `slides / pdf / textbook`-class sources.** Handwritten tutorial notes are excluded — not embedded, effectively treated as absent. (Agent note on the criterion: they fail on **density and redundancy, not on volatility** — posted notes do not change. **The source-class rule is the operative one.**)"
- **`domain-design.md` §10.9, open.** "The corpus pipeline's own design (the pass granularity, what gets embedded, whether page images are kept)."

**Changelog:** silent.

**Tension worth noting:** `model.md` §9's `backing` retraction falsifies file-type-based routing four ways and says "the real axis is whether meaning survives linearization — a property of the materialization pass, not of the file". A source-**class** rule (`slides / pdf / textbook`) is a file-level rule of the kind that retraction is about. Neither passage cites the other.

## 66. Always keep, judge only linkage

**Revisions**

- **`domain-design.md` §10.8, marker `## 10.8 Agent drafts, not ruled`.** "The ingest judgment should not be load-bearing, because its failure is asymmetric: wrongly discarding a correction leaves the corpus quietly wrong, while wrongly attaching one costs a little noise. So retain every announcement's text against its course and any document it names, and let the agent decide only what to *link* and what to *index*. A misjudgment then costs retrieval reach, not data."
- **`model.md` §7.** Cited as precedent for the generated-content trust contract: "Same asymmetry that made ingest judgment non-load-bearing (`domain-design.md` §10.8)."

**Changelog:** silent.

## 67. The portal's folder tree is not the skeleton's shape

**Revisions**

- **`model.md` §9, [R] Billy, 2026-08-22.** "the portal shows how files are *distributed*, which is not how knowledge should be *organized*; **finding the better organization is why the system exists.** This is `domain-design.md` §10.6's finding one level up — announcements are a delivery channel, and the portal tree is a delivery layout."
- **Same, consequences.** "an intake screenshot carries **provenance**, not **position**. Parent resolution is semantic, not a path match. An agent draft claiming the screenshot makes placement easy is **retracted**."
- **`model.md` §3, `CORRECTED` banner.** The same error committed inside the model: "The original row was written from folder appearances (`tutorials/` holds 11 files), which is exactly the *folders-are-not-taxonomy* error this cycle exists to avoid."

**Changelog:** silent.

## 68. The skeleton is not authored by Billy at course setup

**Revisions**

- **`model.md` §9.** "**Skeleton authored by Billy once at course setup** (an agent draft justified by `domain-design.md` §9.6's slow+self-authored test). **Retracted** — at setup Billy does not yet know the concept structure; he knows it at the end. **It failed on the same survivorship bias.**"

**Changelog:** silent.

## 69. The obligation-side ingest dependency

**Revisions**

- **`model.md` §10 item 7, added by the derivation 2026-08-22.** "Every 2c03 handout says *'See Avenue for the due date.'* Ingesting all nine assignment PDFs with a full multimodal pass yields **zero deadlines**. **The portal screenshot is not an enrichment path for ring 0 — it is the primary one**, and the handouts are primary only for `requires` and `spec`. Design §10.7's screenshot ruling is **upgraded from convenience to dependency**."

**Changelog:** silent. **Container-sensitive** — the screenshot-paste intake is a human-in-the-app act.

## 70. Ingest ordering: the governing artifact first

**Revisions**

- **`model.md` §10 item 8, added by the derivation 2026-08-22.** "The course outline is the only carrier of grade weights (without it, 9 of 12 graded items have none and the planner runs blind), and a marker peppered through 2aa4's assignment bodies is decodable **only by reading a different document**. **Cross-document decoding is a real requirement, not an optimization.**"

**Changelog:** silent.

## 71. H3 — whether a multimodal pass can find a partition the course does not state

**Revisions**

- **`model.md` §10 item 6, added by the derivation 2026-08-22.** "**H3 was never exercised — the largest gap this cycle leaves.** Both courses **state their own outline** (2c03: every deck's page-2 plan recurring verbatim as a section divider, plus Week 13's three-group partition; 2aa4: `[Module N]` on 27 of 30 title slides, plus a written two-level taxonomy on one closing slide). Both agents said so unprompted — *'the partition is not induced, it is transcribed, and that is a weaker result than a pass.'* **Whether a multimodal pass can find a partition when the course does not state one is untested.**"

**Changelog:** silent.

## 72. The hub that survives every repair — owed

**Revisions**

- **`model.md` §10 item 1, marker `**RESOLVED 2026-08-22, and the gate turned out to be invalid.**`** "Three agents, blind to each other, each showed the hub was produced by a modelling choice: edge conflation … concept granularity ('design patterns' 16 vs its members 4), and extraction scope (full-text `Interfaces` 16/21 vs title-scoped 2 — *mention* is not *coverage*). **H2 measured us, not the material.** It survives only as a **W2 extraction constraint**: title-scoped extraction, concepts cut at 'one thing that can be separately asked about or separately taught', and `covers` split from the prerequisite relation. Under all three, degrees are comfortable (2aa4: median 2, p90 4, max 10 of 21)."
- **Same item, what remains.** "**One hub survives every repair and it is on the artifact side, which this document did not model:** a review deck covers 26 of 26 concepts and the textbook covers all of them. Their honest relation is **'indexes the whole course'**, not N peer `covers` edges. *Owed: how that is typed and rendered.*"

**Changelog:** silent.

## 73. Concept split / merge / rename — owed

**Revisions**

- **`model.md` §10 item 3, 2026-08-22, owed.** "The concept layer is built incrementally and must be refinable. This is *not* the falsified operations model returning: that was **inbound rewriting a fact** (external, destructive, irreversible); this is **understanding refining a model** (Billy's own, lossless, reversible). Different object, different author, different failure cost."

**Changelog:** silent.

---

# Part H — Capture point, preferences, external systems, framing

## 74. The capture point — `/wrap`, and the third class

**Revisions**

- **`domain-design.md` §1 ruling 2, Billy, 2026-08-21.** "**The capture-point doubt is the same problem**, not an adjacent one — do not settle the ritual and the domain separately."
- **`domain-design.md` §9.6, 2026-08-21, named an agent draft by §9's header.** A two-row table: facts (external origin, high time-criticality, "**must be at the moment**") vs preferences (Billy himself, low, "close-of-session is fine"). "`/wrap` fits slow, self-authored material. Build repos contain nothing else, which is why it has always worked there. … **It was never a problem with the ritual. It was a problem with the material.**"
- **`domain-design.md` §9.6, marker `> **COMPLETED — Billy 2026-08-23, written in here 2026-08-24 — with a THIRD CLASS — the capture point is the READ.**`** "**[R]** Billy, 2026-08-23: '假如需要判断的时候再问...让系统从 waiting for input 变为 asking for input...前者要求你 proactively provide input，但我自己都忘记了怎么可能 provide。'" Third row: **facts with no generating event** — origin Billy himself, time-criticality "only when needed", capture point "**at the READ — the system ASKS**". "The third class is **self-authored but not durable**: progress, difficulty, how much load a week already carries. A deadline is generated when the professor posts it; **a progress state is generated by nothing**, so there is no moment at which it could be volunteered and forgetting to supply it is **structural rather than a lapse**."
- **Same block, the governor.** "**The governor is §9.2's observation gate, unchanged: only ask what changes a decision.** Left ungoverned this degenerates into an interrogation — one blind run alone produced about nine askable items, which is not an improvement on one stale value. **The gate that decides what belongs in the observation space and the gate that decides what is worth asking are the same gate.**"

**Changelog:** silent. **Container-sensitive** — `/wrap` is a repo ritual; "build repos contain nothing else" is a statement about the old container's siblings.

## 75. An asked answer persists

**Revisions**

- **`domain-design.md` §9.6, [R] Billy, 2026-08-23.** "**an asked answer PERSISTS.** It is stored with its timestamp and `source: asked` **stated prominently, so that an agent cannot read a historical answer as a current fact.** The harm was never storage; it was **silent** influence (*'结果后续的决策一直被他影响'*). Same shape as the three-axis `status` finding: `done` was harmful because it was read as terminal and erased a live item, not because it was recorded."

**Changelog:** silent.

**Cross-reference:** `model.md` §8.2 gives `progress` an `origin` field and an `updated_at`; whether `source: asked` is that `origin` is not stated in either file.

## 76. Preferences are a fact type, not a layer

**Revisions**

- **`domain-design.md` §7, 2026-08-21.** Listed under `## 7. Open — not yet ruled` as "**Preferences layer** (raised 08-21) — see §8".
- **`domain-design.md` §8, marker `Raised by Billy; analysis below is draft, not ruled.`** "**Preferences are not a new layer — they are a fact type.** … Structurally it is identical to `progress`: small, self-authored, unenumerable, mostly free text, relationships inferred at read. … because it is nearly all free text it carries no rewrite danger and needs no confirmation."
- **`domain-design.md` §6 table.** Already carries a `preference` row: "id · scope (global | course) · updated_at", read by M4, "added 08-21 (§8)".
- **`domain-design.md` §8, on mem0.** "the capability worth taking is *passive extraction from conversation* (without a verb call), because preferences are exactly what one never thinks to record. The part to reject is the *separate store* — a second source of truth about Billy sitting beside the facts layer reproduces the 'deadline Wednesday / moved to Friday' pathology one level up. **Take the mechanism, not the product.** Precedent already in this repo: `memory/calibration.md` is a preference store with a write discipline (propose-then-confirm); at fall26's volume that discipline is too heavy."
- **`domain-design.md` §9.3.** "preference extraction | close-of-session extractor".

**Changelog:** silent.

**Disagreement (mild, within `domain-design.md`):** §8 is marked "draft, not ruled", yet §6's table already types `preference` as a fact type and §9.3 already assigns it an extractor. The §7 open item points at §8 as if unresolved.

**Note:** `domain-design.md` §8 says preferences are "structurally identical to `progress`". §6.2 / `model.md` §8.2 later move `progress` out of the fact-type table into an annotation kind. Whether the analogy travels is not addressed.

## 77. Calendar goes to Notion; Notion's authority

**Revisions**

- **`domain-design.md` §1 ruling 8, Billy, 2026-08-21.** "**Calendar goes to Notion.** That removes the only human-facing rendering requirement from this repo."
- **`domain-design.md` §7, open.** "**Notion: authority or projection?** Tilt: projection. 'Manage my calendar' implies the system owns the dates; if Notion is also writable, the two-sources-of-truth pathology returns in a new place. **One authority (facts layer), many views.**" Under `## 7. Open — not yet ruled`.
- **`domain-design.md` §0.5.** What Billy named concretely: "**a calendar he can look at**, and **a note-taking mechanism** with knowledge-base character."

**Changelog:** silent.

**Disagreement (cross-file):** §1.8's claim that Notion "removes the only human-facing rendering requirement from this repo" is contradicted by later rendering work inside the corpus: `model.md` §2 defers "which spine a view renders" as "a CLI/UX decision", `model.md` §7.2 rules that "a sticky note renders **together with** the summary", and `model.md` §10.5 measures what "rendering the course level" costs in characters. Rendering is live in `model.md` and declared exported in `domain-design.md`.

**Container-sensitive** — both the Notion projection and "this repo" are container facts.

## 78. Relationship to the existing PA db

**Revisions**

- **`domain-design.md` §7, 2026-08-21, under `## 7. Open — not yet ruled`.** "Tilt: keep separate. An obligation is not a todo (todos are flat, cross-domain, carry no workload/course/source and no externally-driven status transitions); overloading them would pollute PA's cross-domain work-trace. fall26 gets its own tables in the same database, and an obligation entering 'this week' *projects* a PA todo — **fall26 authoritative, PA a view.**"

**Changelog:** silent. **Container-sensitive.**

## 79. Manual markdown maintenance is out

**Revisions**

- **`domain-design.md` §1 ruling 3, Billy, 2026-08-21.** "**Manual markdown maintenance is out.** The information granularity is too fine and too time-sensitive for the `devlog/`-style discipline."
- **`domain-design.md` §0.4.** "**The manual-markdown discipline this repo already runs** (`devlog/`, dated decision docs) is the wrong instrument at this granularity: the information is finer-grained and far more time-sensitive, so the maintenance overhead would exceed the value. Ruled out explicitly (§1.3)."

**Changelog:** silent. **Container-sensitive** — names a specific repo's discipline.

## 80. "Sync" is the wrong model

**Revisions**

- **`domain-design.md` §1 ruling 4, Billy, 2026-08-21.** "**'Sync' is the wrong model.** This is not a continuously-changing system kept aligned with a remote. It is a knowledge base: things enter, stale/wrong things leave, everything is classifiable and queryable."

**Changelog:** silent.

## 81. The schema must not be over-determined

**Revisions**

- **`domain-design.md` §1 ruling 7, Billy, 2026-08-21.** "**The schema must not be over-determined.** The cases cannot be enumerated today and the relationships cannot be written out today."
- **`domain-design.md` §6.** Answered by the `/promote` gate: "**a tiny mechanical core plus everything else free**, not vagueness everywhere."
- **`model.md` §8 watch list.** The same posture applied to edges: "one sighting each, **deliberately not adopted** (PLAN.md's over-modelling failure mode)."
- **`model.md` §10.9, Billy 2026-08-23.** The same posture applied to conditional weighting: "**Billy rejected the general form** … as over-built for what is so far one concrete weight calculation."

**Changelog:** silent.

**Note:** ruling 7 says "the relationships cannot be written out today", and §6's "No relationship graph" flows from the same posture. `model.md` §8 writes out eleven typed edges the following day. `model.md` §9 justifies this via the rigidity rule (thing 26) but not against ruling 7.

## 82. Sequencing: fall26 first, template afterwards

**Revisions**

- **`domain-design.md` §1 ruling 1, Billy, 2026-08-21.** "**Sequencing inverted.** fall26 first; do not generalize from the three build-repo instances and clone outward. (Carried in the dispatch.)"
- **`domain-design.md` §0.1.** "The B-layer domain-definition contract was un-parked with an inverted sequencing ruling: fall26 comes first and forces the template. So this design IS the B-layer work — **the template is whatever survives generalization afterwards**, not something to be derived up front. The standing telos behind it: every aspect of Billy's life managed under one contract."

**Changelog:** silent. **Container-sensitive** — B-layer, dispatch, build-repo instances are all old-container structure.

## 83. Offering-term and prerequisite structure — the cross-domain hook

**Revisions**

- **`domain-design.md` §0.6, 2026-08-21.** "Winter-only mandatory courses ruled out a winter-27 co-op, and thereby set the entire recruiting target to summer 27. That decision was made inside ai-eng's academic track, and **Fairy never held the fact — because no home existed for a constraint spanning academics and career.** So the academic domain must hold **course offering-terms and prerequisite structure**, since that graph gates other domains' decisions. **This is the single most concrete design input carried in the originating dispatch, and it is why 'just track my deadlines' is the wrong target.**"
- **`domain-design.md` §6 table.** `course` typed: "id · name · term · **offering-term · prereq · manifest**"; `offering-term` is "the one field justified by *another domain's* need".
- **`domain-design.md` §6 supersession note, 2026-08-25.** `offering-term`, `prereq` and `manifest` are all named as being "**in the schema graveyard**".

**Changelog:** `domain-design.md` 2026-08-25 — agent — agent-drafted (the §6 table entry).

**Disagreement:** §0.6 calls this "the single most concrete design input" and the reason the target is not "just track my deadlines". Its three carrier fields are recorded as graveyarded by 2026-08-25, with the graveyarding done by an agent as a flag ("**Flagged rather than rewritten, because rewriting the table is a schema decision**") rather than as a ruling. Nothing in either file says what now holds offering-term and prereq, or whether §0.6's requirement survives.

## 84. No proactivity, no cron

**Revisions**

- **`domain-design.md` §2, 2026-08-21.** "**Consequence for scheduling:** no proactivity, no cron, no 24/7 — the existing on-demand ruling holds. **Billy's own urge to check is the scheduler**; the design gives that urge a better target instead of fighting it."

**Changelog:** silent. **Container-sensitive** — a statement about how a running service behaves.

## 85. Courses vary enormously in shape

**Revisions**

- **`domain-design.md` §0.2, 2026-08-21, pre-evidence.** Three shapes described: a stats course needing no materials; a typical course posting a flat professor-categorised list; an engineering course posting weekly announcements pointing outward "at a density where understanding the week's task can itself require a dedicated session".
- **`model.md` §3, 2026-08-22.** The same observation, formalised as H1 and then partly corrected by the 2aa4 row (thing 18).

**Changelog:** silent.

## 86. The two observed failure modes

**Revisions**

- **`domain-design.md` §1 ruling 12, Billy, 2026-08-21, from the live Fairy system.** "(a) the thread graph records at too fine a grain — detail nobody needed got written down, when what is wanted is retrieval on demand; (b) a coordinator that pulls in-depth information about one course cannot possibly hold every course's every topic, so its **weighting judgment gets polluted** by whichever slice it happens to have."
- **`domain-design.md` §9.1.** (a) answered by "pointers and summaries, never content" plus non-sedimentation.
- **`domain-design.md` §9.2.** (b) restated as a mechanism: "if the coordinator holds detail on course A and one line on course B, it will systematically over-weight A, because **visible work masquerades as important work**."
- **`model.md` §7.** (b) is what mechanism 1 was aimed at — "§1.12(b)'s harm is specifically that *weighting judgment* gets polluted, and weighting is allocation" — and that aim was later replaced by the symmetry rule (thing 53).

**Changelog:** silent.

## 87. What retrieval actually is — still open

**Revisions**

- **`domain-design.md` §10.9, marker `### 10.9 Still open`.** "How retrieval actually works — Billy's cascade (check the surface, then search, then read the original and its surroundings). **'The surface' is undefined, and its definition is the boundary between the two layers.**" Also open there: "What triggers extraction: at paste time, or later off a stored item"; "Whether the correction seam is detectable at intake. The twelve instances share a signature — they name a document — but twelve is too few to build on"; "The corpus pipeline's own design."

**Changelog:** silent.

## 88. Expected behaviour — the six scenarios

**Revisions**

- **`model.md` §6, 2026-08-22, unattributed.** Six scenarios with per-layer ✅/❌: (1) what is due this week → ring 0 only; (2) what is week 7 / topic X about → skeleton walk + labels; (3) what does that worksheet require → skeleton locate + store by-handle; (4) where was the difference between X and Y covered → skeleton map-back + store by-query; (5) what should I know that I have not asked → skeleton browse + set difference + sticky notes; (6) a correction arrives → attach a sticky note, store ❌ **untouched**.

**Changelog:** silent.

**Note:** scenario 2's phrasing is the one `model.md` §9 later says is unanswerable for a timeless course (thing 27). Scenarios 3 and 4 assign store access without saying to whom — §5's revised three-level table denies both to the coordinator.

---

# Disagreements

Consolidated. Each entry gives both sides with location and date; none is adjudicated.

### Marked by the documents themselves

| # | The thing | Side A | Side B | Where it is flagged |
|---|---|---|---|---|
| D1 | **What a Node summary is for** | `model.md` §4 (agent, undated): the skeleton answers "**is it worth opening**" | `model.md` §4.1 (2026-08-23, Billy + agent): that framing "is wrong for the coordinator, because §7's table denies it the store in both modes and so the coordinator never opens anything"; §4 "carries no `[R]`" and Billy "never ruled" it | `model.md` §4 `STANDING MARKED 2026-08-24`; §4.1 heading `— NOT RULED` |
| D2 | **Is `label` the ingest summary?** | `model.md` §7.2 (2026-08-23, **[R]** Billy): "`label` is that output — means **written**, not **named**" | `model.md` §7 table and §4 store column: labels, summaries and sticky notes enumerated as **distinct** things | `model.md` §7.2 `> **UNRESOLVED, and it must not be smoothed over.** … reconciling it with §7's enumeration was never done` |
| D3 | **Where the purity cut falls** | `model.md` §5 body (2026-08-22, agent): "exactly between" by-handle and by-query | `model.md` §5 (2026-08-23, **Billy**): "wrong as written and it misleads … the cut belongs between the skeleton read and by-handle"; three levels, not two | `model.md` §5 `> **REVISED 2026-08-23, Billy.**` |
| D4 | **Which within-layer hierarchy is a tree** | `model.md` §2 earlier draft: "the tree survives inside a layer" | `model.md` §2 (2026-08-22, derivation): "**False for the concept layer** … The concept layer is a DAG. The artifact layer is the tree" | `model.md` §2 `> **REVISED 2026-08-22 by the derivation.**` |
| D5 | **2aa4's obligation density** | `model.md` §3 original row: 2aa4 obligation-dense, "two axes with overlap" | `model.md` §3 (2026-08-22): "**sparse, not dense** … the same shape as 2c03"; row struck through in the table | `model.md` §3 `> **CORRECTED 2026-08-22 — and this row was the hypothesis's calibration point.**` |
| D6 | **What allocation may observe** | `model.md` §7 mechanism 1 (agent, 2026-08-22): "**Allocation reads ring 0 only**" | `domain-design.md` §9.2 / `model.md` §7 (**Billy 2026-08-23**): the **symmetry rule**; "the invariant was never shallowness — it is uniformity"; "Ring 0 returns to being the layer that is RESIDENT, not the definition of what is observable" | `model.md` §7 `> **REPLACED — Billy 2026-08-23, written in here 2026-08-24**`; `domain-design.md` §9.2 `> **RESTATED …**` |
| D6b | **…and a third document still disagrees** | Both files: ruled by Billy 2026-08-23 | `openclaw:fall26/2026-08-23-slice-1/doubt/RECONCILE.md` §5 "still lists it as open and is stale on that point" — stated identically in both files, unfixable from inside this corpus | `model.md` §7 and `domain-design.md` §9.2, both under `**Standing, recorded because it was contested.**` |
| D7 | **The two-layer split axis** | `domain-design.md` §3 (2026-08-21): split by **content type**; "full context in ordinary conversation needs no retrieval" | `domain-design.md` §10.5 (2026-08-22): split by **who reads it**; the load-bearing sentence is "**false as written**" | `domain-design.md` §3 `⚠️ **PARTLY SUPERSEDED 2026-08-22**` |
| D8 | **The operations model** | `domain-design.md` §4 (2026-08-21): file-it / apply-it; retirement at write time; ~30 confirmations/semester | `domain-design.md` §10.3 (2026-08-22): "**FALSIFIED — 39%**"; retirement is read-time expiry ~7:1; "~30 … is not a real number" (~115, or 1-2 per course) | `domain-design.md` §4 `⚠️ **SUPERSEDED 2026-08-22**`; §10.3 heading "**is dead (P5)**" |
| D8b | **…except its counter-argument** | §4's rejection of read-time reconciliation | `domain-design.md` §10.8: it "**survives and is unanswered**"; the agent's rebuttal "is an assertion, not a design" | `domain-design.md` §4 banner and §10.8 |
| D9 | **`workload`'s standing** | `domain-design.md` §6 table (2026-08-21): typed, read by M1 M2 M3 M5; §7 open item on where estimates come from | `domain-design.md` §6.1 (**[R] Billy 2026-08-23**): "**NOT a field to be filled** … its missing-rate is retired as a guard signal" | `domain-design.md` §6 `⚠️ **TWO FIELDS BELOW NO LONGER GOVERN**`; §6.1 heading |
| D10 | **`progress`'s carrier** | `domain-design.md` §6 table: a typed fact type. Then (08-23): demoted to a sticky-note kind | `model.md` §8.2 / `domain-design.md` §6.2 (**[R] Billy 2026-08-24**): "an **annotation with its own kind**", `about` link; the demotion is "**overturned**" | banners in both files; both changelogs, 2026-08-25 |
| D11 | **The length bound's premise** | `model.md` §10.5 (2026-08-22): "the only route" by which unbounded free text enters; real samples assumed short | `model.md` §10.5 (2026-08-24 `WIDENED`, 2026-08-28 `MEASURED`): `label` is a second route; real notes run 87–278 chars and a course level opens with 871 | two stacked banners in `model.md` §10.5, newest-first |

### Not marked anywhere — cross-file or unnoticed

| # | The thing | Side A | Side B |
|---|---|---|---|
| D12 | **Does an obligation have `workload`?** | `model.md` §8 vocabulary (frozen-header section, never revised): `obligation: due · status{...} · weight · target_date? · **workload?**` | `domain-design.md` §6.1 (**[R] Billy 2026-08-23**): retired, "its null is not a gap to close". `model.md` was edited on 2026-08-28 without touching this line. |
| D13 | **Does an obligation have `status`?** | `model.md` §8: `status{completion, score, evaluation}`; `model.md` §4 puts `status` in ring 0 | `domain-design.md` §9.1 + changelog 2026-08-25: "`status` was dropped 2026-08-25"; `domain-design.md` §6 lists `status` among the six graveyarded fields |
| D14 | **How the `progress` defaulting fault is fixed** | `domain-design.md` §6.2: "fixed by **rendering null as absence**"; `model.md` changelog 2026-08-25 says the same | `model.md` §8.2 + changelog 2026-08-28 (**Billy — ruled**): "fixed by a **DEFINED default, not by rendering absence**; `state` is **not nullable**; no record reads as `not_started`". The 08-28 restatement landed on one side of the corpus only. |
| D15 | **Is the projection the same thing as ring 0?** | `model.md` §7's retraction rests on "§9.1's projection was always `obligations · time-points · plan`, **i.e. ring 0**" | `domain-design.md` §9 (Billy 2026-08-23, recording a reviewer's still-valid point): §9.1 "**never says 'ring 0'**, and the gloss *'ring 0 was arrived at by subtraction'* is a later paraphrase, not this section's words" |
| D16 | **Ring 0's field set** | Four lists, none identical: `domain-design.md` §9.1 (`label/due/status/workload`, dead), `domain-design.md` §10.5 (`due, workload, status, course`, minus workload), `model.md` §4 (`due · status · course · plan`), `model.md` §8 (seven fields) | Resolution lives at `spec/ring-0.md`, outside this corpus |
| D17 | **The coordinator's tool surface** | `domain-design.md` §9.3 (agent draft): "read the fact projection · write plans · dispatch. **No corpus retrieval, no file reads, no fact writes**" — three items | `model.md` §7 (**[R] Billy 2026-08-22**) + §7.1 (**[R] Billy 2026-08-23**): a fourth, skeleton query, named as the verb `look_at(node_id, question)`. §9.3 was never amended. |
| D18 | **Announcements: channel or knowledge?** | `model.md` §8 and §9 cite `domain-design.md` §10.6 as having **ruled** "announcements are a delivery channel" | `domain-design.md` §10.6: the channel proposition "**failed in both**" courses (5 of 55, 6 of 38 after discounting redundancy); what survives is the narrower correction-seam claim |
| D19 | **Is "what is week 7 about" answerable?** | `domain-design.md` §10.4 (Billy 2026-08-22) uses it as the paradigm case of what the system is for; `model.md` §6 scenario 2 marks it skeleton-answerable | `model.md` §9 (2026-08-22): **unanswerable** for 2aa4 from lecture material — zero occurrences of "Week N" in 687 KB — and "the navigational handle … is a label on the coarse grouping that **the schema never names**" |
| D20 | **Is the corpus append-and-supersede?** | `domain-design.md` §3 table: corpus write mode is "**append + supersede only**" | `model.md` §8: `supersedes` **CUT**, zero instances, "keeping it is actively harmful"; `domain-design.md` §10.3: read-time expiry beats write-time supersession 7:1. §3's banner covers the split axis, not this column. |
| D21 | **Is rendering in scope?** | `domain-design.md` §1.8 (Billy 2026-08-21): Notion "removes the **only** human-facing rendering requirement from this repo" | `model.md` §2 ("which spine a view renders is a CLI/UX decision, deferred"), §7.2 ("a sticky note renders **together with** the summary"), §10.5 (measures the cost of "rendering the course level") |
| D22 | **One free-text field per type** | `domain-design.md` §6, banner-confirmed as "unchanged and still governs" | `model.md` §7.2: ingest writes **summary + tags + sections**; §8.2: `progress` carries `state` + `detail` + `origin`. Neither tests itself against the rule. |
| D23 | **Is Billy-authored input ever a dangerous write?** | `domain-design.md` §4: "**All dangerous inputs are external.** Billy-authored input … is never a dangerous rewrite — he is the authority on his own state" | `model.md` §8.1 (**[R] Billy 2026-08-23**): a spoken "A6 is done" against a portal record must be surfaced as a conflict — "you told me this, the record says that — which holds?" |
| D24 | **Does the vector index key on courses or concepts?** | `domain-design.md` §1.9 (Billy 2026-08-21): "**per-course buckets** for independence, metadata filtering" | `model.md` §5 (agent, explicitly "not ruled"): "embeddings attach to the **concept layer** as the entry point" |
| D25 | **Is RAG inclusion decided by source class?** | `domain-design.md` §10.7 ruling 3 (Billy 2026-08-22): "RAG stores `slides / pdf / textbook`-class sources … **The source-class rule is the operative one.**" | `model.md` §9: file-type-based routing (`backing: unchunkable_media`) was "**falsified four ways in one slice**"; the real axis is "whether meaning survives linearization — a property of the materialization pass, **not of the file**" |
| D26 | **What `look_at` returns** | `model.md` §7.1: `{ summary, **sticky_notes[]**, edges[] }` | `model.md` §8.2 (Billy 2026-08-24): `{summary, **annotations[]**, edges[]}`. §7.1's signature was not updated. |
| D27 | **One field, three names** | `weight` (`model.md` §8), `worth_percent` (`model.md` §10.9's ruling), `grade_share` (`model.md` §7.1) — no passage says they are the same field or distinguishes them | Similarly `model.md` §7.1 names an obligation's copied field `name` where §8's vocabulary has `label` |
| D28 | **Are relationships written at write time?** | `domain-design.md` §1 ruling 7 (Billy): "the relationships cannot be written out today"; §6: "**No relationship graph**" — banner says everything else in §6 "is unchanged and still governs" | `model.md` §8 types eleven edges the next day; `model.md` §9 declares §6's clause "**Overturned by its own rule**". The overturn is recorded only on `model.md`'s side. |
| D29 | **Is `model.md` frozen?** | Title: "**frozen 2026-08-22**"; Status: frozen so the derivation "would be a test rather than a self-confirmation" | Its own body carries `[R]` rulings dated 2026-08-23, -24 and -28, and its changelog records edits on 2026-08-25 and three on 2026-08-28. The word "frozen" is never qualified. |
| D30 | **What does `domain-design.md` §8's "identical to `progress`" now mean?** | §8: preferences are "**structurally identical to `progress`**: … a fact type" | §6.2 / `model.md` §8.2 move `progress` out of the fact-type table entirely, into an annotation kind. Whether preferences follow is not addressed. |
| D31 | **Does §0.6's cross-domain requirement survive?** | `domain-design.md` §0.6: offering-term + prereq are "the single most concrete design input carried in the originating dispatch" | `domain-design.md` §6 note (2026-08-25, **agent, flagged not ruled**): `offering-term`, `prereq` and `manifest` are all "in the schema graveyard". No passage says what now holds the requirement. |
| D32 | **Which path is the schema at?** | Bodies of both files: `spec/schema.md`, `spec/ring-0.md`, `spec/write-rules.md` | Both changelogs (2026-08-25): `records/schema.md`. Cosmetic, but it means the two halves of each file point at different paths for the same authority. |

---

# Container-sensitive rulings

Flagged only — these read as properties of the old container (a standalone repo running as an app a human uses) rather than of the domain. The successor is a set of components an agent uses. No judgment is offered about whether any of them survives.

**The session and agent architecture**
- Coordinator is long-running, not booted per session — `domain-design.md` §1.11, §5, §9.1, §9.5 (thing 46).
- Session topology semester/course/task, "coupling is through the store, never through a call" — `domain-design.md` §5 (thing 47).
- Disposability as the acceptance criterion ("if losing the coordinator session loses information, the design is wrong"; scale is days-to-weeks) — `domain-design.md` §9.5 (thing 58).
- No fold, no dispatch/ack/cursor, "the store is the channel" — `domain-design.md` §5, §9.4 (thing 48).
- Multiagent: which agents exist and why — `domain-design.md` §8, §9.3 (thing 57).
- The responsibility table's specific agent roles (ingestion subagent, deep-read subagent, task subagent Billy enters himself, close-of-session extractor) — `domain-design.md` §9.3 (thing 50). Note `model.md` §7 already generalises this away from topology to a data-flow rule.

**The tool surface**
- "Purity cannot be maintained by prompt. Only by tool surface" — `domain-design.md` §9.0 (thing 8). Assumes control of which tools the coordinator holds.
- The `look_at(node_id, question)` verb, and the `question` parameter being **required** "so it is enforced at the tool surface rather than requested in a prompt" — `model.md` §7.1 (things 55, 56).
- "Derived tool surface for the coordinator: read the fact projection · write plans · dispatch" — `domain-design.md` §9.3.
- "Nothing requires a CLI fetch to render all N + E" — `model.md` §7.

**Development-mode apparatus**
- Note CRUD "asks a short confirmation **during development**", the toggle, and the arbitrary N=5 exit condition — `model.md` §8.1 (thing 44).
- The `question` parameter's retirement condition, scoped "within the development cycle", measured "across one full three-run arm", threshold 80% flagged arbitrary — `model.md` §4.1 (thing 56).
- The observation-earns-its-place gate, "testable by running the same task with and without the observation" — `domain-design.md` §9.2 (thing 28).

**Repo ceremony and rituals**
- `/wrap` as capture point; "build repos contain nothing else, which is why it has always worked there" — `domain-design.md` §9.6 (thing 74).
- `/promote` as the schema-evolution gate — `domain-design.md` §6 (thing 31).
- "Course ≠ domain": registry entry, episodes, /wrap, /standup, ack protocol as "repo-level ceremony" — `domain-design.md` §5 (thing 49).
- "Manual markdown maintenance is out", naming this repo's `devlog/` discipline — `domain-design.md` §1.3, §0.4 (thing 79).
- Sequencing inverted / the B-layer template / the originating dispatch — `domain-design.md` §0.1, §1.1 (thing 82).
- `memory/calibration.md` cited as the in-repo precedent for a preference store — `domain-design.md` §8.

**Boundaries drawn against a human user**
- "Ingestion is out of scope. Billy is the fetcher — he opens Avenue, downloads PDFs. The system's boundary starts at the endpoint" — `domain-design.md` §1.5 (thing 61).
- Live intake is "Billy **pasting a screenshot**" — `domain-design.md` §10.7 ruling 5 — and the screenshot upgraded "from convenience to dependency" — `model.md` §10.7 (thing 69).
- "The system declares nothing outward"; the audit surface ruled out — `domain-design.md` §1.10, §7 (thing 5).
- "Co-location is enough because **Billy is in the loop reading it**" — `domain-design.md` §10.7 ruling 2 (thing 41).
- Confirmation policy stratified by operation, counted per semester — `domain-design.md` §4, §10.3 (thing 64).
- "No proactivity, no cron, no 24/7 … Billy's own urge to check is the scheduler" — `domain-design.md` §2 (thing 84).
- "'Sync' is the wrong model" — `domain-design.md` §1.4 (thing 80).

**Infrastructure and external systems**
- Calendar goes to Notion; Notion as projection not authority — `domain-design.md` §1.8, §7 (thing 77).
- Relationship to the existing PA db, "fall26 gets its own tables in the same database" — `domain-design.md` §7 (thing 78).
- pgvector 0.8.0 / HNSW; one-time embedding at material drop; per-course buckets — `domain-design.md` §1.9, §10.1 (thing 10).
- "The coupling surface between skeleton and store is exactly one field: `chunk.node_id`" — `model.md` §6 (thing 11).
- Store by-handle / by-query as ANN infrastructure — `model.md` §5 (thing 8).
- "The ingestion endpoint is multimodal from day one" — `domain-design.md` §10.7 ruling 5.

---

# Coverage

**Read in full, twice-passed:** both files, all 1,508 lines.

- `/Users/billywu/Documents/Projects/fall26/records/domain/model.md` — lines 1–709. Every section (header banners, §1–§10, `## Changelog`) was read and is cited above.
- `/Users/billywu/Documents/Projects/fall26/records/domain/domain-design.md` — lines 1–799. Every section (header banners, §0–§10, `## Changelog`) was read and is cited above.

**Both `## Changelog` sections were read in full and are quoted where they bear on a thing.** `model.md` has 6 entries (three dated 2026-08-28, three dated 2026-08-25); `domain-design.md` has 5 (one 2026-08-28, four 2026-08-25). Most things below §10 in either file have **no** changelog entry; where I write "Changelog: silent" that is a positive finding, not an omission — the changelogs cover only the 2026-08-25 import housekeeping and the 2026-08-28 corrections, so the reasoning for everything decided 08-21 through 08-24 lives in in-place banners rather than in the changelog. Two things are recorded **only** in a changelog and not in the body: the ±1–2 week window's resolution to `today-7d .. today+14d` (`domain-design.md` changelog 2026-08-28) and the reason §6's table was flagged rather than rewritten.

**Skimmed rather than parsed line-by-line:** nothing. The two evidence tables (`domain-design.md` §10.1's probe list, `model.md` §3's course table) were read as data and their verdicts are quoted rather than re-derived.

**Could not account for — all of it outside the boundary, none of it read:**

- **The ruling field grains.** `spec/schema.md` §4.5 (the `progress` field grain, cited by `model.md` §8.2 and `domain-design.md` §6.2) and `spec/ring-0.md` (the ring-0 membership test, the active/known bands, the field set, and the `today-7d .. today+14d` window). Thing 52's four-way disagreement about ring 0's fields **cannot be closed from inside this corpus** — the authority is `spec/ring-0.md`.
- **The schema graveyard.** Both files refer to six fields being "in the schema graveyard" without listing what the graveyard is or where it lives beyond `spec/schema.md`.
- **`spec/write-rules.md` §4.2** — the worked compression producing "~90 characters", the benchmark `model.md` §10.5's measurement is against.
- **The 08-23 demotion of `progress` to a sticky-note kind.** Referenced and overturned in both files; **written out in neither**. Its two grounds are quoted but the ruling itself is not in this corpus.
- **The evidence folders**, all cited and none read: `openclaw:fall26/2026-08-22-derivation/FINDINGS.md` (the source of every §8 score and the three falsifications), `openclaw:fall26/2026-08-22-modeling/PLAN.md`, `openclaw:fall26/2026-08-22-step-minus-1/` (P1–P6), and the whole `openclaw:fall26/2026-08-23-slice-1/` tree — `FINDINGS.md`, `INCONSISTENCIES.md`, `experiments/NOTE-MECHANISM.md`, `experiments/E10R-RESULTS.md`, `experiments/OBSERVATION-SPACE.md`, `experiments/FAITHFULNESS.md`, `doubt/RECONCILE.md`. Where a numeric claim below rests on one of these (60 runs, 38% of faithfulness failures, 53 spec-edge instances, 5 of 55 announcements), I recorded the number as the record states it and did not verify it.
- **`records/archive/build-plan-2026-08-27.md`** — the "plan of record", cited in `model.md`'s header with the instruction "**§9 first**".
- **`spec §10.9 item 3` and the 2026-09-01 ruling** it names, referenced by `domain-design.md` §6.1 as the thing being overturned. The date 2026-09-01 is **in the future relative to every other date in the corpus** and I could not resolve what it refers to; it is recorded verbatim as the file has it.
- **`RECONCILE.md` §5**, which both files say "still lists it as open and is stale on that point" (D6b). Both files agree it is stale; neither can fix it, and neither could I.

**One structural caveat about this survey.** The unit I inventoried is "the thing an ADR would be about", and several entries could reasonably be split or merged — `label` and "what a Node summary is for" are arguably one question about node identity (things 7, 36); `workload`, `status` and `weight` are arguably one question about the obligation's field set (things 32, 33, 35); ring 0's residency, the symmetry rule and the discard rule are arguably one question about the coordinator's observation contract (things 51, 53, 54). I split them where the records themselves ruled on them separately, and cross-referenced rather than merging. Anyone landing these in a single source of truth should re-cut that boundary deliberately.
