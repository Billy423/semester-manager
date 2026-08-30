# Classification - Cluster B: shape (layers, node kinds, edges, the store)

**What this is.** A routing proposal for M13-M39. Nothing here is created: no `CONTEXT.md` entry, no ADR file, no issue. Destinations are `CONTEXT` · `ADR` · `DEFER` · `DROP`, one per thing.

**Standing rule applied throughout.** Sequencing is not spec. The corpus assigns almost every shape thing to "slice 1" / "slice 2" / "slice 3"; fall26's own CLAUDE.md says there is no plan of record and the pre-split plans are frozen. Every slice assignment below is stripped and said so. What survives is the ruling the slice assignment was attached to.

**Two words this cluster owns and the corpus uses inconsistently.** Both are resolved in the term list and flagged for Billy:

1. **`layer`** is used in three incompatible senses - the three strata of the graph (`design.md §3.1`), the 08-21 facts/corpus split (dead), and Billy's 08-29 "content layer vs time layer". I reserve `layer` for the first and name the collision.
2. **"skeleton kinds"** in `design.md §3.1` means the three *layered* kinds, but `course` and `sticky_note` are also nodes in the skeleton. The phrase is a trap and is put under `_Avoid_`.

---

## M13. Two layers, three compartments - facts / corpus, skeleton / store / ring 0

**Destination: `CONTEXT`.**

This thing's whole content, once `design.md §3.0` settles it, is *what the pieces are called and what each one is*. That is the glossary's job. The decision it rests on (exactly two persisted things, one coupling field) is routed at **M32** so the two do not duplicate.

**Proposed terms.**

- **skeleton** - the graph of nodes and links: what exists, how it relates, and a handle to content. One of the two persisted things.
  _Avoid_: **facts layer** (the 08-21 content-type split, whose axis `domain-design.md §10.5` ruled wrong), **compartment** (`model.md §4`'s word for a three-way division that `design.md §3.0` replaced with two), **the graph** used bare (ambiguous with the concept DAG and the artifact tree), **skeleton kinds** meaning the three layered kinds.
- **store** - materialized artifact content: chunks and embeddings, addressed either by a node handle or by similarity. The second and only other persisted thing.
  _Avoid_: **corpus layer** / **the corpus** (the dead split axis; "corpus" now only means the source material), **RAG store** (names only the by-query half - `model.md §5`: "only one of them is RAG"), **`Store`** as an interface or class name (`design.md §3.0` rules the name taken).
- **node** - a record with a `kind`, an id in the single id space, and that kind's declared field set; anything that can be an endpoint of a link.
  _Avoid_: **entity**, **record** used interchangeably (a record is the serialized form).
- **link** - a typed, directed relation between two refs, stored as its own record rather than as a field on either end.
  _Avoid_: **edge**. Both are in the corpus and `design.md §3.4` uses "edge" for the thing `links()` walks, but `Link`, `LinkKind` and `links()` are the committed names and one word should win.

**Sequencing stripped.** "The store does not exist until slice 3" is dropped. What survives is that the store is a second persisted thing coupled by one field, which is a structural claim, not an ordering.

**Touched by Billy's rulings.** #6 - it is now settled what the store is *for* (semantic, decontextualized facts about course materials), which is what makes a one-sentence definition of `store` writable at all. Ruled at **M37**.

**Cross-cluster.** `ring 0` is the third name in this thing and I do **not** claim it: cluster D's M66 defines it. Whatever D writes must be compatible with M32's ADR, which fixes ring 0 as an access policy over `obligation` nodes rather than a third persisted thing. `chunk` is defined at M34.

**Zoomed.** Yes - `design.md §3.0`, `schema.md §1`, `ring-0.md §1`, `model.md §4`. Confirms the inventory: `design.md §3.0` answers the exact question `model.md §4`'s own banner raised and left open. The zoom also surfaced the "skeleton kinds" phrasing trap, which no survey names.

---

## M14. What a Node summary is for

**Destination: `CONTEXT`.**

The 08-28 architecture ruling removed the *object* for every kind but one. That is a definition, not a decision to argue: what a summary IS is now sayable in one sentence, and the surviving open question (`label` versus `summary`) is a different thing owned elsewhere.

**Proposed term.**

- **summary** - a written one-line object carried only by a node whose identity is content the skeleton does not hold; in the current kind set that is the `artifact` alone, and every other kind's one-line render is composed from fields it already stores.
  _Avoid_: **node summary** (the corpus's disambiguator, needed only because a second object shares the word - see below), **concise summary** (a length property, and `model.md §4.1` records a 55-word summary that was still noise).

**A second object with the same name, resolved.** The materialization pass also produces a per-artifact summary (`model.md §4`'s store column: summary / tags / chunks / embeddings). Billy ruled 08-23 that these are **different objects** and the coordinator never sees the second. Proposal: `summary` means the node-level object; the store's is the **materialized summary** and is never called `summary` unqualified.

**Not resolved here, deliberately.** Whether the one-line-per-item render is called a `label` or a `summary` is presentation's first decision and is explicitly deferred (`design.md §4`). Defining `summary` does not pre-empt it: the ruling above says artifacts have a written one; it does not say what the *other* kinds' composed line is named.

**Sequencing stripped.** Nothing. The 08-27 "deferred to slice 1's exclusion list" is a tier dependency (presentation does not exist), not an ordering.

**Touched by Billy's rulings.** None directly.

**Cross-cluster.** Cluster C's M55 (`label`) is the other half of the deferred naming question and must not resolve it either. Cluster D's M76 (`look_at`) returns a summary and D's M79 (trust contract for generated content) governs the materialized one.

**Zoomed.** Yes - `architecture.md §5` and `model.md §4.1`. The zoom changed the framing: `architecture.md §5`'s last bullet explicitly *withdraws* the older recommendation to compose an obligation summary from `parts` + `due` + `grade_share`, on the ground that it lent the artifact's vocabulary to a kind with no ingest. That withdrawal is why `summary` is definable narrowly, and no survey quotes it.

---

## M15. The three node kinds, and the four slice-1 kinds

**Destination: `CONTEXT`.**

This is the cluster's vocabulary core: two orthogonal axes and the names on each.

**Proposed terms.**

- **kind** - the named record schema a node's payload conforms to, carried on the node as a required discriminator field whose value is the kind's own name. The current set is `course` · `obligation` · `sticky_note` · `progress` · `concept` · `artifact`.
  _Avoid_: **type** and **node type** (`type` is the field-level word), **layer** (a different axis - see below), **metadata** (`design.md §3.1`: remove it and the node has no shape).
- **layer** - one of the three strata of the domain graph: `obligation`, `concept`, `artifact`. A property of those three kinds only; `course`, `sticky_note` and `progress` have no layer.
  _Avoid_: **skeleton kinds** used to mean the layered kinds; **content layer** (see the collision note below).
- **obligation** - a thing with a deadline. The one layer that carries time, and the same nodes ring 0 is a projection of.
  _Avoid_: **task**, **assignment**, **deadline** as the noun for the record.
- **concept** - a unit of subject matter the course teaches, independently addressable.
  _Avoid_: **topic** (used descriptively in the corpus and it invites per-topic splitting, which the write rule forbids - see M28), and the retracted definition "a thing the student understands or does not", which presumed state the system must not keep.
- **artifact** - a thing the course delivers and that is opened independently.
  _Avoid_: **file**, **document**, **resource**; and the falsified definition "a thing that exists on disk" (at least 8 of 2aa4's artifacts are not on disk and never will be - see M20).

**The `layer` collision, flagged for Billy.** Billy's 08-29 ruling 8 says "content layer and time layer must be separate". That is a coarser sense of the word than `design.md §3.1`'s. Recommendation: reserve `layer` for the three strata, and name Billy's distinction as **the skeleton versus the time projection**. This is his phrasing, so the rename is a proposal, not a ruling.

**Sequencing stripped.** "Slice 1 introduces four kinds, slice 2 adds two" is dropped whole. Six kinds are declared; which exist first is the next wayfinder session's output. Also dropped: `design.md §3.1`'s residual gap where `progress` is unaccounted for in the sentence "only the three skeleton kinds have a layer" - that gap dissolves once `layer` is defined as a property of three kinds and `progress` is simply not one of them.

**Touched by Billy's rulings.** #8 - forces the `layer` collision above into the open. #1 - scope is coursework inside academics, so no seventh kind is coming for v1.

**Cross-cluster.** **Heavy.** Cluster C's M42 is "`kind` as a discriminator, and `layer` as a separate axis" - a direct duplicate of half this thing. My proposal: C owns the *mechanism* ruling (`kind` is data with a typed payload, never control flow; a discriminated union; construction-time validation) as an ADR; I own the *names*. If C does not produce that ADR, one is owed and its title is **"`kind` and `layer` are separate axes, and only three kinds have a layer"** - `design.md §3.1` names conflating them as the failure mode. C's M51 (`progress`) and M57 (`sticky_note`) should define those two kinds against this list; `course` as a kind is C's M41, `course` as a *node* is my M16.

**Zoomed.** Yes - `model.md §2` and `design.md §3.1`. Confirms both cuts and the corrected concept definition. `model.md §2`'s table is where the three layers and their time property live verbatim.

---

## M16. A course IS a node

**Destination: `ADR`.**

**Proposed title:** *A course is a node, not a namespace.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** Every ref, every link signature and every read path assumes a course resolves; unwinding it means re-homing course-level notes and special-casing the `about` link. |
| Surprising without context | **Yes.** A course reads as a container or a scope field, and the domain corpus had it as one of five *fact types*, not a node. |
| Result of a real trade-off | **Yes.** The alternative - course as a scope field only - is still written into `schema.md §1`'s hedge ("whether or not courses ever join the node set"). It loses because course-level facts (the late-day budget, the snow-day credit, the conditional-weighting rule) have no target otherwise. |

**Body.** A `course` is a node, so `get(Ref("course","2c03"))` resolves and an `about` link to a course is an ordinary link with no special case. The forcing case is course-level notes: the late-day budget is not a property of any obligation, and without a course node it has nowhere to land.

**Sequencing stripped.** "This is forcing in slice 1, not slice 2" is dropped. The forcing *argument* (course-level notes must land and read back) survives; the slice claim does not.

**Touched by Billy's rulings.** None directly. #1 keeps the boundary at coursework, so no course-of-courses or program node arrives to complicate it.

**Cross-cluster.** C's M41 (`course.id` is the exception to id opacity - the code is supplied, not assigned) is the companion and must not contradict this. C's M44 (`obligation.course` is a field, not an edge) is the near-miss a reader will trip on: a course being a node does *not* make course membership a link.

**Zoomed.** Yes - `design.md §3.2` and `schema.md §2`. Confirms the inventory; `schema.md §2`'s field table has caught up with `design.md` ("**A course is a node**, so `get(Ref("course","2c03"))` resolves"), so the hedge in `schema.md §1` is stale phrasing in one place only, not a live second position.

---

## M17. Layered graph, not a tree

**Destination: `ADR`.**

**Proposed title:** *The skeleton is a layered graph; the model may not cut edges to force a tree.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** It is the shape everything else is built on; a tree would remove edges the material requires and they cannot be recovered later. |
| Surprising without context | **Yes.** The obvious model of course material is the folder tree the material actually arrives in, and rendering a tree is strictly easier. |
| Result of a real trade-off | **Yes.** The folder tree was the named rejected alternative, and rendering cost was the price paid - how a view handles a node with two parents is explicitly deferred to the surface. |

**Body.** A concept appearing in two places is the truth of the data, not a rendering bug, so the model may not cut edges to force a tree. A file is not the object being modelled: a lecture PDF and a tutorial PDF exist and are used independently, yet both describe one concept. Which spine a view renders is the surface's decision.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None directly.

**Cross-cluster.** Cluster E's M92 ("the portal's folder tree is not the skeleton's shape") is the same argument aimed at intake. These should be one ADR with two consequences, or two ADRs that cite each other. Recommend: this one is the model ruling, M92 is the ingest consequence.

**Zoomed.** Yes - `model.md §2`. Verbatim Billy `[R]`, uncontested in all four surveys. Nothing changed.

---

## M18. Which layer is a tree - the concept DAG, the artifact tree

**Destination: `DROP` - exposition.**

**Why.** The ruling this thing produced is a typed property of one link kind - `part-of` | `concept → concept` | **a DAG** - and it rides in M22's LinkKind table. What is left is the argument: the falsified draft ("the tree survives inside a layer"), the named instances (Singleton under two parents with opposite valence, Liskov three times, Observer as the mechanism of MVC), and the measurement that 2aa4's 21 lectures partition into 5 groups with none in two and none orphaned.

**The one positive claim I am dropping on purpose.** "The artifact layer is the tree" has **no reader**. No mechanism consumes it, no query is named for it, and by the rigidity rule (M26) it must not become a field or a structure. It is a fact about the material that may become interesting when artifacts get a writer; it is not a thing to carry now.

**Sequencing stripped.** "slice 2" on the `part-of` row.

**Touched by Billy's rulings.** None.

**Cross-cluster.** None. The DAG property is inside M22.

**Zoomed.** Yes - `model.md §2`'s REVISED block. Confirms that the falsified draft is still physically above its own revision in the file, which is a reason the ruling should land somewhere clean rather than be cited to `model.md`.

---

## M19. The modelling layer is stateless; system-inferred mastery is forbidden

**Destination: `ADR`.**

**Proposed title:** *The modelling layer is stateless: system-inferred mastery is forbidden.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** It forecloses a whole product direction; adding inferred mastery later needs a data model, a writer, and a trust story the system has spent its design budget refusing. |
| Surprising without context | **Yes.** A study system that will not track what you know is counterintuitive, and the obvious feature is exactly the forbidden one. |
| Result of a real trade-off | **Yes.** The cost was raised in the same session and overruled: a handwritten Task-1 solution is the densest single record of what was actually understood in the slice, and the model has no place to put it. It was ruled an artifact, not an understanding signal. |

**Body.** The modelling layer records no state about the owner: it presents concepts and leaves judgment to him, and system-inferred mastery is forbidden. Surviving set-difference queries are structural ("this concept has no artifact covering it"), never personal ("you never opened X"). An agent may surface a progress claim for confirmation but may never resolve one.

**Shape that rides.** The enforcement point is **nowhere, deliberately** - it is a rule about the caller, and `architecture.md §1` forbids a method from defending itself against one.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #2 and #4. Ruling 4 explains *why* `progress.state` defaults to `not_started`: so the agent does not keep asking "how far along are you". That is the same constraint from the other side - the system neither infers nor interrogates. Ruling 2's "the agent notices and asks the user when needed" is the permitted third move, and its frequency is an evaluation item, not a design input.

**Cross-cluster.** C's M51 (`progress` - its carrier, kind and default) carries the mechanism; D's M79 (the trust contract for generated content) and E's M84/M86 (confirmation policy, always keep) carry the interaction. Flag: the sentence "surface for confirmation, never resolve" appears in at least four things across three clusters and should be stated once.

**Zoomed.** Yes - `model.md §2`, `schema.md §4.5`, `design.md §3.7`. `design.md §3.7` adds the detail no survey highlights: this rule is *why* `annotation` is a tag rather than a type hierarchy - a subtype forbidding something its parent permits would be a Liskov violation, so the three differences become construction-time validation rules instead.

---

## M20. Artifact existence - no `present` flag, no `external_ref`

**Destination: `ADR`.**

**Proposed title:** *An artifact's existence is not a field; absence is the absence of store content.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** Adding a presence flag later needs a writer, a refresher and a truth-maintenance story for a value that goes stale silently. |
| Surprising without context | **Yes.** Two agents, blind to each other, independently proposed the field, and the set-difference query does read wrongly without it: it reports *have* for things that are merely *named*. |
| Result of a real trade-off | **Yes.** Measured cost: about 13 `referenced_only` instances in one course, and Midterm 2 is a graded obligation with a released grade and literally zero artifacts on disk. Overruled because the resources exist on the portal and knowing what a name refers to is sufficient - he does not want everything stored locally. |

**Body.** An artifact does not need a URL or a `present` flag. Absence has no field: it is the absence of store content for that node, read as a join.

**Cost, stated inside the ADR (do not lose it).** A node with no store content is indistinguishable from a node that was never created. The field question was ruled; the distinguishability question was never put. The query that would separate them was named ("obligations whose posted solutions I never downloaded") and would have flagged seven missing test-script archives and both midterm solution sets.

**Sequencing stripped.** "The artifact kind is slice 2, so nothing is blocked today" is dropped - it is the reason no one had to answer, not a reason the question is not real.

**Touched by Billy's rulings.** #6 indirectly: once the store's inclusion rule is "does it carry semantic facts about course materials" (M37), the absence-as-join reading gets sharper, because a node can be deliberately unembedded *and* present.

**Cross-cluster.** M37 and M38 (mine) are the store side of the same seam. C's M62 (the graveyard) should record `present` / `external_ref` / `backing: referenced_only` as ruled out, so nobody re-adds them.

**Zoomed.** Yes - `model.md §2`. Verbatim Billy `[R]`, with the counts. Nothing changed.

---

## M21. H1 - course type as per-layer density

**Destination: `DEFER`.**

**The deferral.** H1 - that course type is per-layer *density* rather than *structure* - stays not-falsified and untested, and it is not tested now.

**Precondition that wakes it.** Billy's ruling 9 states it as a conjunction, and every clause is checkable:

1. write rules have landed,
2. prompt and docstring work has landed,
3. ring 0 and the skeleton have an exposed surface with product-facing verb names decided,
4. rendering exists, so an end-to-end run is runnable.

When all four hold, run the falsifier: read a course of a different shape (2px3, the `woven` profile) and ask whether it needs a node kind or a link kind the current set lacks.

**What ruling 9 closed.** The cheap escape hatch - reading 2px3 for structure only, producing no records - is **rejected**: when the instrument cannot reflect the ideal case, its result is untrustworthy. So the gate is not reachable by a shortcut, and that is deliberate rather than an oversight.

**Sequencing stripped.** "Gated on slice 2 running the extractor on 2px3" loses the slice; the *content* of the gate (a third course of a different shape, run through the real instrument) survives and is the wake-up test above.

**Touched by Billy's rulings.** #9 decisively - it converts C14/E3 from an accident (two rulings passing in the dark, leaving the model's main hypothesis untestable) into a chosen state with conditions. #2 secondarily: acceptance and evaluation items are measurable only after the system is roughly built.

**Cross-cluster.** Cluster A's M11 (disposability as the acceptance criterion) and F's M102 (the acceptance criterion - 22 obligations across two courses) are the same instrument-readiness question. E's M87 (H3) is the other untested hypothesis and should be deferred on the same precondition or explicitly not.

**Zoomed.** No. The inventory's citations of `model.md`'s header conditions and `architecture.md §4` are quoted at length and ruling 9 supersedes the whole dispute.

---

## M22. The edge set

**Destination: `ADR`.**

**Proposed title:** *Links are a closed typed set, each with an endpoint signature; a relation earns a row only with three real instances and a nameable query.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** The link set determines every query, every write rule and every render. Adding a row is cheap by construction; changing what the existing rows *mean* is not. |
| Surprising without context | **Yes.** Nine rows and no others, including no `supersedes` and no `announcement → node`, and one polymorphic row (`about`) that targets anything. A reader will ask why the set is this small. |
| Result of a real trade-off | **Yes.** The bar was set in advance - at least three real instances and a nameable query - and it cut relations that felt obviously right (`supersedes`) while admitting ones nobody proposed at the start (`prepares-for`, `concept → concept requires`). |

**Body.** Every relation is a `Link` with a `LinkKind` whose signature constrains its endpoints, so adding a relation is a table row plus a signature rather than a schema change. A relation earns a row only if the material shows at least three real instances and someone can name the query that reads it.

**Shape that rides (the slice column deliberately removed).**

| LinkKind | signature |
|---|---|
| `about` | `annotation → any` |
| `covers` | `artifact → concept` |
| `applies` | `artifact → concept` |
| `requires` | `concept → concept` |
| `requires` | `obligation → concept` |
| `spec` | `obligation → artifact`, `role ∈ {given, owed}` |
| `prepares-for` | `artifact → obligation` |
| `builds-on` | `obligation → obligation` |
| `part-of` | `concept → concept` (a **DAG**) |

**Term spun off (belongs in `CONTEXT.md`).** **link kind** - the named, signature-constrained relation type a link carries; the set is closed and extended only by adding a row.

**Sequencing stripped.** **The slice column is removed entirely**, and with it the sentence "slice 1 implements exactly one row of this table". That sentence is the single clearest instance of the failure this project's brief warns about: an ordering that reads as structure. What survives from it is the *reason* it was written - that adding a row is a table entry plus a signature, not a refactor - which is the ADR's body.

**Touched by Billy's rulings.** #8 - no time-bearing link kind is coming; a `week` node joined by edges is explicitly not the right modelling, so the set stays as it is.

**Cross-cluster.** `annotation` (the `about` row's source endpoint) is C's M51/M57 to define and my signature depends on it. `covers` / `applies` are defined as terms at M27 (mine). `locator` and `role` are payload/identity and are at M30 (mine). Cluster A's M5 (`nodes_without`) and the `closure` operation read this table; the ruling that **`closure` is single-source reachability, not an all-pairs matrix** has no M-number in any cluster and is at risk of being lost - flagged for reconciliation as an orphan ADR candidate.

**Zoomed.** Yes - `design.md §3.3`. Confirms nine rows and the signatures. The zoom also confirms `obligation.course` is a field and not an edge, stated in the same paragraph, which is C's M44.

---

## M23. `supersedes` - cut

**Destination: `ADR`.**

**Proposed title:** *There is no `supersedes` link; revisions replace in place and are dated.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes** - not the row itself, but its consequence: once revision history is not recorded at write time, it cannot be reconstructed, because the filesystem destroys it. |
| Surprising without context | **Yes.** A knowledge base with no version relation is surprising, and the reason is non-obvious: "newest wins" *systematically discards the richer file*, because plain-slide exports were batch-produced on one date while notes exports carry real lecture dates. |
| Result of a real trade-off | **Yes.** Five agents, two courses, zero instances, against the intuition that revisions obviously need linking. `revised_at` was chosen instead, and the cost - that the announcement stream becomes the only surviving record of supersession - is stated. |

**Body.** No `supersedes` link kind exists. Every real revision replaced the file at the same path under the same name, so there is no prior version to point at; a `supersedes` link would mistype three shapes and hide a live document. Revision is carried by `revised_at`, and **filename similarity must never imply a relation** - one same-named pair turned out to be two different lectures (Jaccard 0.21).

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #7 decisively, and it strengthens the cut from two directions. "Two conflicting statements must never coexist in the system" removes the state a `supersedes` link would describe. And it kills the last live text on the other side: `domain-design.md §3`'s corpus write mode "append + supersede only" is now superseded twice over and is still unmarked in the record. Ruling 7 also adds what replaces it - the agent resolves shallow conflicts itself but **must report afterwards**, and must ask before resolving deeper ones (assignment spec, requirements, concepts, exam location or time).

**Cross-cluster.** **Heavy.** Ruling 7's resolve-and-report / ask-first split is a write rule and an interaction rule, and belongs with cluster E's M85 (conflict detection) and M90 (the correction seam). My claim here is only the *shape* consequence: no link kind, and `revised_at` as the carrier. C's M62 (graveyard) should list `supersedes`. M39 (mine) shares the Jaccard-0.21 case.

**Zoomed.** No. The inventory quotes the derivation and `model.md §8` at length and `design.md §3.3`'s table (which I did zoom for M22) confirms the absence directly.

---

## M24. `announcement → node (mentions)` - cut into `sticky_note.origin`

**Destination: `ADR`.**

**Proposed title:** *An announcement is a provenance value, not a node and not a link.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** Making announcements first-class later needs a kind, an ingest path and a re-homing of `origin`, and the notes already written would have the wrong shape. |
| Surprising without context | **Yes.** Announcements look like a primary source and the intuition is that they are a body of knowledge. The pre-registered proposition that they are merely a delivery channel was **falsified in both courses** - and the cut survives anyway, on different grounds. |
| Result of a real trade-off | **Yes.** The alternative was an `announcement` node with `mentions` links. It loses because an amendment to a document is not a fact, and because the redundancy defence was checked on disk in both courses and is dead. |

**Body.** An announcement is the `origin` field of an annotation plus a flat provenance log; it is not a node and there is no `mentions` link. What an announcement carries is almost always a correction against material the system already holds, not new knowledge.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #5 and #7. Ruling 5 says the real risk is not two sources disagreeing but the agent asking repeatedly or persisting a small conflict as noise that colours every later read - which is an argument for announcements staying a provenance value rather than becoming records that accumulate. Ruling 7 governs what happens when an announcement *does* collide with held material.

**Cross-cluster.** **Heavy with E.** E's M83 (inbound is to be known, not to trigger an action), M89 (stale material circulates as current; the redundancy defence is dead) and M90 (the correction seam) are the intake side of this thing. My claim is the shape ruling only: no kind, no link kind, `origin` is the carrier. C's M57 (`sticky_note` - `category`, `origin`, `body`) owns the field. Also note for reconciliation: `model.md §8` and `§9` cite `domain-design.md §10.6` **twice in the direction of the falsified proposition**, so anything quoting `model.md` on announcements is quoting a mis-citation.

**Zoomed.** No. S3 read the source probe first-hand and the inventory reproduces the numbers (7/55 and 7/38 gross, 5/55 and 6/38 net) with the bias direction pre-registered against the convenient answer.

---

## M25. "No relationship graph" - overturned

**Destination: `ADR`.**

The overturn *narrative* is dropped as exposition (see below). What is carried is the position that won.

**Proposed title:** *Relations are records, not fields on the related thing.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** This is refactor trigger C by name: if a note's target is a field on the note, targeting concepts, artifacts and courses multiplies the field or makes it polymorphic. |
| Surprising without context | **Yes.** At four kinds, one `target_id` field on the note is the obvious and cheaper implementation, and the record explicitly declined it. |
| Result of a real trade-off | **Yes.** The genuine alternative was live and written down: infer relations at read time, "affordable because the layer fits". It was overturned by the project's own rigidity rule once `obligation → concept` acquired a mechanism that reads it. |

**Body.** A relation between two things is its own record, never a field on either end. A note's target is an `about` link, not a `target_id`.

**Dropped as exposition.** The whole "overturned by its own rule, not violated" story - the 08-21 no-relationship-graph decision, the 08-22 narrowing to "the rule, not the type list", the stale `domain-design.md §6` banner that still says everything else in §6 is unchanged. It is the argument that got here, and the ruling stands without it.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None.

**Cross-cluster.** C's M42 (kind as discriminator) is the sibling trigger (B); C's M43 (conventions - field-grain CRUD) states the mutability half. F's M98 (the four §3 consequences) may restate the trigger list. Recommend the five refactor triggers be recorded **once**, in one ADR, rather than distributed across the things that cite them - flagged for reconciliation.

**Zoomed.** Yes - `design.md §2`. Confirms trigger C is held explicitly unaffected by the 08-27 tier re-scoping, so it is current spec and not domain history.

---

## M26. The rigidity rule, and its two standing exemptions

**Destination: `CONTEXT`.**

**Proposed term.**

- **rigidity rule** - the project's test for whether a field exists: a field is typed if and only if some mechanism reads it. Its consequence is that deferring a schema decision costs nothing.
  _Avoid_: **the typing rule**, **rigidity follows importance** (the rule is explicitly *rigidity follows mechanism, not importance*).

**Two ruled exemptions, which the rule's own statement does not admit.** `grade_share` and `added_at` are carried with no mechanism reading them, and both are declared exemptions rather than oversights. The `CONTEXT.md` entry should say the rule admits *declared* exemptions, or a reader will apply it as absolute - which is exactly how the domain corpus states it.

**Dropped from this thing.** The lifted agent formulation at `domain-design.md §9.2` - "an observation earns its place if and only if a judgment demonstrably changes when it is present" - is an **agent draft never ruled**, self-marked as such, and `ring-0.md §2` explicitly declines to use it and reports that running it returned nothing. Do not carry it.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #2 - `hours_estimate` is not quantifiable and `grade_share` is reference only, never an input. That is a second, independent reason the `grade_share` exemption is the point rather than an oversight: it is carried *for the human to read*, which is a reader the rule does not count.

**Cross-cluster.** C owns both exemptions with their fields (M47 `grade_share`, M43 `added_at`). D's M68 (the membership test) is a *different* test for a different question (routing, not typing) and `ring-0.md §2` says so explicitly - the two must not be merged. E's write rules are where the rule is applied at intake.

**Zoomed.** Yes - `schema.md §2`, `§3`, `ring-0.md §2`. Confirms both exemptions verbatim and confirms that `ring-0.md §2` declines the §9.2 formulation on instrument grounds ("a device that cannot exercise routing returns 'nothing changed' whether or not routing matters").

---

## M27. `covers` / `applies` - why the split, and mention is not coverage

**Destination: `CONTEXT`.**

Two link kinds whose distinction cannot be read off M22's table and whose conflation produced a phantom hub. That is glossary work.

**Proposed terms.**

- **covers** - the relation asserting that an artifact teaches a concept as its subject. It is the rendered relation.
  _Avoid_: using `covers` for a mere mention. Full-text matching finds mention; title-scoped matching finds coverage, and the difference is a degree of ~15 versus ~3 on one concept and 16 versus 2 on another.
- **applies** - the relation asserting that an artifact uses a concept without teaching it. It feeds closure and is never rendered.
  _Avoid_: **uses**, **mentions** (the latter is the cut announcement link's name and must not be recycled).

**Sequencing stripped.** "slice 2" on both rows.

**Touched by Billy's rulings.** None.

**Cross-cluster.** M22 (mine) carries the rows; M28 (mine) carries what the split dissolved and what survived it. E's M88 (extraction scope) is where "title-scoped, not full-text" becomes a write rule.

**Zoomed.** Yes - `design.md §3.3`, which names the split's payoff in place: "split out of `covers`; the split is what dissolved the phantom hub". Uncontested across three records.

---

## M28. The hub - H2, its dissolution, and the one that survives

**Destination: `DEFER`.**

**What is deferred.** How to type and render the artifact-side hub that survives every repair: a review deck covers 26 of 26 concepts and the textbook covers all of them, and their honest relation is "indexes the whole course", not N peer `covers` edges.

**Precondition that wakes it.** The first time an artifact is ingested and `covers` gets a writer. Concretely: when a single artifact's extraction would produce `covers` edges to more than about half the concepts in a course, the question is live and must be answered before those edges are written.

**Dropped alongside, as exposition.** The H2 gate itself ("is expansion cost bounded") is dead - it was invalid as posed, three agents returned three verdicts and the synthesis picked a fourth, and the record says it measured our own choices rather than the material. Carry the constraints, not the gate.

**One conflict I can close rather than defer.** C21 recorded an unresolved contradiction: the adopted granularity rule ("cut concepts at one thing that can be separately asked about or separately taught") is the split one of its own agents forbade ("do not rescue the first hub by splitting into per-topic analysis concepts - Big-O of Quicksort and Big-O of Dijkstra are the *same* skill"). **I zoomed and it is settled, in the agent's favour.** `write-rules.md §3.4` (Billy, ruled 08-27/28) states the operative test as **recurrence**: a part is "a concept worth capturing because it might occur elsewhere in the system", and the worked rows keep `Big-O` while dropping `Monte-Carlo` and `A5Tree` as one-off and local. A recurrence test forbids the per-topic split. Billy's own 08-29 note said this was ruled and should be verified at source; it verifies. **C21 should be closed, not carried.**

**Sequencing stripped.** "The concept layer is slice 2, so low urgency."

**Touched by Billy's rulings.** The 08-29 note on E9(c) closes C21 as above.

**Cross-cluster.** C's M49 (`parts`) is where the recurrence rule physically lives (`write-rules.md §3.4`), so C should be told that this rule is *also* the concept-granularity ruling - the two records do not say so. E's M94 (concept split / merge / rename) is the operational sibling.

**Zoomed.** Yes - `write-rules.md §3.4`, and it changed the outcome: what the inventory carried as a live contradiction needing Billy is a settled ruling in a record neither S1 nor S3 read for this question.

---

## M29. `spec` roles `{given, owed}`, and whether `produced` splits off

**Destination: `DEFER`.**

**What is deferred.** Whether `obligation --produced--> artifact` splits off `spec` as its own link kind, or whether a `role` discriminator suffices.

**Precondition that wakes it.** The first read that must distinguish what was *given to you* from what you *handed in* on the same obligation - the named query is "show me what I handed in for A8". If that query can be served by filtering `spec` on `role`, the split does not happen; if serving it needs a second traversal or a special case, it does.

**Sequencing stripped.** "deferred to slice 2".

**Touched by Billy's rulings.** None.

**Cross-cluster.** M22 (mine) carries the `spec` row with `role ∈ {given, owed}`. The deferral issue should record the positive finding attached to it: the derivation's own synthesis **misreported its agent** (claiming A3 concluded a role attribute suffices when A3 concluded the opposite), and `model.md §7.2` restored A3's actual position without noticing it was correcting anything. That is worth one line in the issue so the misreport is not re-inherited.

**Zoomed.** No. Three records agree on what is open and the inventory quotes A3's conclusion verbatim.

---

## M30. `locator` - from edge payload to link identity

**Destination: `ADR`.**

**Proposed title:** *A link's identity is its natural key, and `locator` is part of it.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** Identity is what idempotent re-landing keys on; changing it later re-identifies every stored link. |
| Surprising without context | **Yes.** A citation's fragment reads like a payload, not like identity, and putting it in the key is not the intuitive move. |
| Result of a real trade-off | **Yes.** A surrogate id was considered and rejected: idempotent re-landing needs a natural key regardless, so a surrogate would add a second identity without removing the first. And leaving `locator` out was measured: **7 real edges collapse**. |

**Body.** A link's identity is the natural key `(from, to, kind, role, locator)`; there is no surrogate id. `locator` is in the key because omitting it silently destroys edges - one deck cites the textbook four times at four different sections, and those are four links, not one. The residual is correct rather than a gap: two citations from the same source into the same target at the same locator are one link.

**Shape that rides.**

```
Link     := from: Ref · to: Ref · kind: LinkKind · role?: string · locator?: string
identity := (from, to, kind, role, locator)   -- a natural key; no surrogate id
```

**Term spun off (belongs in `CONTEXT.md`).** **locator** - the fragment a link points into: a section, a page, a method, a question. It is stored verbatim as the source string.

**Sequencing stripped.** "`role` and `locator` are unused in slice 1" is dropped. They are on the shape; when they are first written is sequencing.

**Touched by Billy's rulings.** None.

**Cross-cluster.** C's M40 (the id scheme) rules that nodes get opaque assigned ids; this ADR is the reason links do **not** - they are identified structurally, and no survey states that the two identity schemes are deliberately different. Flag this to C explicitly. Also: `locator` is what absorbed two edge kinds that S3 recorded as lost (`cites`, 25+ instances, and `example-code`, 15+) - `design.md §3.3`'s 28 measured instances (22 + 6) is the arithmetic that closes it.

**Zoomed.** Yes - `design.md §3.3` and `schema.md §5`. Confirms the key, the 7-edge measurement with the four quoted section strings, and the explicit rejection of a surrogate.

---

## M31. `Ref`, one id space, and refs that dangle

**Destination: `ADR`.**

**Proposed title:** *A ref is not a foreign key: one id space, and a ref may name something that is not there.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** One id space across every endpoint kind is refactor trigger A; splitting it later breaks every link, and course-local ids (where `a1` appears in two courses) is the colliding scheme it exists to avoid. |
| Surprising without context | **Yes.** A pointer that may dangle, and a delete that does not cascade, is the opposite of what a reader expects from a stored graph. |
| Result of a real trade-off | **Yes.** Referential integrity was the alternative and it was given up knowingly; the stated price is a validation pass over the link set, cheap at ~2,200 links, "a real operation the design owes, not a hand-wave". |

**Body.** A pointer is a `Ref := (kind, id)` whose id is unique in one id space shared by every kind that can be a link endpoint. The kind tag makes a ref resolvable without a lookup, which is what lets a link be validated at write time against its signature. A ref may name something that is not there, so it is not a foreign key and deleting a record does not have to cascade.

**Term spun off (belongs in `CONTEXT.md`).** **Ref** - a pointer to a node: its kind plus its id. It may name something that does not exist.
  _Avoid_: **foreign key** (it is explicitly not one), **pointer** used as the noun.

**What this is no longer for, and it must be recorded with it.** A dangling ref used to be the *mechanism* for forward reference - A8's handout names A9 before A9 exists - by letting a writer construct A9's id from its name. That route is closed. Forward reference is handled three ways instead: list before linking · surface an untracked target to the user rather than auto-adding it · resolve a batch ingest in two passes. Dangling is now a consequence of deletion, not a feature.

**Owed, and unbuilt.** The validation pass over the link set.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #7 lends weight to "surface an untracked target to the user rather than auto-adding it" - it is the same never-resolve-silently instinct.

**Cross-cluster.** **Heavy with C's M40** (`id` - opaque, monotone, assigned, never reused). Proposal for the split: C owns the id's *properties*; I own the *ref* and the one-id-space commitment. Both records state "one id space", so reconciliation must pick one home for that clause. C's M41 (`course.id` supplied, not assigned) is the declared exception.

**Zoomed.** Yes - `design.md §3.2` and `schema.md §1.1`. Confirms all three properties and the 08-28 closure of the construct-an-id route, with the `ChildMath A1` / `ChildsMath A4` evidence.

---

## M32. Two persisted things; the coupling surface is one field

**Destination: `ADR`.**

This is where M13's decision lands. M13 supplies the names; this supplies the ruling.

**Proposed title:** *Exactly two persisted things, coupled by one field; ring 0 is not a third.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** If ring 0 becomes its own persisted store, residency stops being an access policy and becomes a synchronization problem, and every read path re-homes. |
| Surprising without context | **Yes.** The design corpus spent a week describing **three** compartments and two *layers*, and a reader arriving at that material will expect three stores. |
| Result of a real trade-off | **Yes.** Three compartments was the live alternative and is still written down. Two wins because degradability requires each side to work while the other is broken, and that requires the coupling to be small enough to name. |

**Body.** There are exactly two persisted things: the skeleton (nodes and links) and the store (chunks and embeddings). Ring 0 is not a third: the obligation layer *is* ring 0, and residency is an access policy over obligation-kind nodes rather than a separate store. The coupling surface between the two is exactly one field, `chunk.node_id`, which is what lets each degrade without the other.

**Shape that rides.**

| term | what it is | persisted? |
|---|---|---|
| **ring 0** | the obligation layer's typed fields | **not separately** - residency is an access policy over `obligation` nodes |
| **the skeleton** | the graph: nodes and links | **yes** |
| **the store** | materialized artifact content: chunks and embeddings | **yes** |

**Sequencing stripped.** "The store does not exist until slice 3" and "slice 1 touches the skeleton only".

**Touched by Billy's rulings.** #6 - the store's purpose is now defined (semantic, decontextualized facts about course materials), which is what makes "two things, one coupling field" a statement about *what they are* rather than about what was built first.

**`⟂container`.** `chunk.node_id` names a table column in a store the standalone app owned. The claim survives the container change as a data-shape claim; the word "column" does not.

**Cross-cluster.** D's M66 (what ring 0 IS) must be written against this: ring 0 is a projection and an access policy, not a store. Whatever D says about residency inherits the "not separately persisted" clause. F's M103 (the skeleton does not need a database) and M106 (serialization) are the persistence consequences and should cite this rather than restate it.

**Zoomed.** Yes - `design.md §3.0` and `ring-0.md §1`. Both confirmed verbatim and they agree.

---

## M33. The store's access modes, and where the purity cut falls

**Destination: `ADR`.**

**Proposed title:** *The purity cut is enforced by return type, not by tool registry or prompt.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** It is the argument the language choice rests on - a compiler that can refuse - so reversing it reopens `architecture.md §6`. |
| Surprising without context | **Yes.** The obvious enforcements are "do not put it in the prompt" and "do not give the agent the tool", and both were tried and named insufficient. |
| Result of a real trade-off | **Yes.** Three mechanisms were live: prompt ("purity cannot be maintained by prompt"), tool surface ("an agent holding a tool will use it"), and type. Type wins because it is the only one that survives a change of container. |

**Body.** The store has two access modes - **by-handle** (a lookup on `chunk.node_id`; deterministic, no similarity) and **by-query** (nearest-neighbour over embeddings). The coordinator holds neither: it holds the skeleton interface only, and the skeleton's return type has no field a chunk could arrive in. The cut sits above both store modes, not between them.

**Terms spun off (belong in `CONTEXT.md`).**

- **by-handle** - the store access mode that fetches the chunks a known node points at.
- **by-query** - the store access mode that searches by similarity when you do not know where to go. This is the only half of the store that is RAG.

**Sequencing stripped.** "Described here because slice 1 must not foreclose it."

**Touched by Billy's rulings.** None directly.

**`⟂container`.** The tool-registry version of this rule assumes control of which tools the coordinator holds; in an agent-as-container that control may relocate rather than dissolve. **The type-level version survives relocation, which is the reason to prefer it** - that sentence belongs in the ADR, because it is the only place the container axis is load-bearing on a shape decision.

**Cross-cluster.** **Heavy with D.** The sentence "the coordinator sees what a node IS; it never sees what a node SAYS" is the observation contract and is D's M75/M73 to state. My claim is the *mechanism*: two store modes, and the cut enforced by return type. F's M104 (TypeScript) rests on this ADR and should cite it. If D also proposes the purity cut, merge in D's favour for the contract and keep this one for the enforcement.

**Zoomed.** Yes - `model.md §5` (both the body and Billy's 08-23 REVISED block, which records that the wrong version misled a session) and `design.md §3.5`, `architecture.md §6`. `architecture.md §6` makes the dependency explicit: TypeScript is chosen because "defused by type, not by restraint" is a claim about a compiler that can refuse.

---

## M34. Materialization is not retrieval indexing

**Destination: `CONTEXT`.**

The whole content is a distinction between two things the corpus once conflated. Naming them apart is the fix.

**Proposed terms.**

- **materialization** - the one-time pass that turns an artifact's raw content into stored readable form: normalize, chunk, summarize, tag. It is paid once so every later read is cheap, and it happens whether or not anything is embedded.
  _Avoid_: **indexing**, **embedding**, **ingestion** (ingestion is the inbound act of getting material in at all; materialization is what is done to it afterwards). The retracted draft "embed ~300 summaries instead of ~20,000 chunks" conflated materialization with retrieval indexing and would have forced a runtime `pdftotext` on every detail read.
- **chunk** - a unit of an artifact's materialized content, stored with its node id, an ordinal, its text, an optional locator and its embedding.
  _Avoid_: **chunk** used for a course's coarse grouping of material (a week, a module). That usage appears in the escalation material and would collide head-on with the store's unit; the coarse grouping has no name and must not borrow this one - see M36.

**Sequencing stripped.** "That is a slice-3 decision." What survives is the ruled *trigger*, which is a real commitment: the store needs **storage, not an ANN index**, until brute-force cosine over the vector set stops being milliseconds. The sizing behind it is flagged estimated rather than measured, and that flag travels with it.

**Touched by Billy's rulings.** #6 - the inclusion rule (M37) determines what materialization even runs on.

**Cross-cluster.** M37 and M38 (mine) are the rules materialization runs under. E's M91 (RAG source classes) is the same seam from intake - see M37's flag. D's M79 (the trust contract owed for generated content) governs the materialized summary.

**Zoomed.** Yes - `model.md §5` and `design.md §5` conclusion 2. Confirms the retraction and the storage-not-ANN trigger.

---

## M35. Where the vector index attaches

**Destination: `DEFER`.**

**What is deferred.** Whether embeddings attach to the concept layer as an entry point (with chunks in the artifact layer for reading) or to chunks alone - which is the difference between **two** embedding sets and one.

**Precondition that wakes it.** The first time a text query must route to a node without a handle, i.e. when the store is actually built and by-query is implemented. At that point the choice is forced and the cost (two embedding sets, kept in step) is payable or not.

**Not in conflict, which the corpus does not say.** Per-course buckets (Billy, 08-21) and a concept-layer entry point (agent, explicitly unruled) are not exclusive: a bucket is a partition of the index, an entry point is a routing decision. The deferral issue should say so, or it will be re-litigated as a conflict.

**Sequencing stripped.** "Owner: the build, slice 3."

**Touched by Billy's rulings.** #6 constrains it without settling it: if the store holds *semantic, decontextualized facts about course materials*, then what is embedded is fact-grain, and that leans the answer but does not decide between one set and two.

**`⟂container` - and this is where I drop something.** pgvector 0.8.0, HNSW, PostgreSQL 17.6 and the managed Supabase instance are properties of a database the standalone app owned. They are **not carried**: artifacts of the old container. What survives is the probe's *finding shape* (an embedded vector store is available and cheap at this scale), not the stack.

**Cross-cluster.** F's M103 (the skeleton does not need a database) and M107 (the store is the channel) are the persistence siblings.

**Zoomed.** No. `design.md §3.5` and `§7` item 4 are quoted in the inventory and I read §3.5 in full for M33; it names the item open with an owner and states the two-sets cost.

---

## M36. The graph has no time axis; `week` is not a field; the navigational handle

**Destination: `ADR`.**

**Proposed title:** *The skeleton carries no time axis; time is a separate layer, not nodes and edges.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** A time axis on nodes means a field on every artifact, a writer for it, and a rewrite of grouping and rendering; and once "week N" nodes exist in a graph, removing them invalidates every edge into them. |
| Surprising without context | **Yes** - maximally so. *"What is week 7 about"* is the sentence Billy uses to describe what the product does, and this ADR says the graph does not model weeks. A future reader will read that as a contradiction unless it is written down. |
| Result of a real trade-off | **Yes.** Four alternatives were live: a `week` field, a renamed `time-anchor`, a `lecture_date` field ("for 2aa4 the only ordering signal that exists"), and week-as-a-node. All rejected. The evidence: 2aa4 has **zero** "Week N" markers in 687 KB of lecture text, so hardcoding either organizing scheme is the failure. |

**Body.** The skeleton is a content and domain graph and has no time axis. The only time on a node is `due`, which belongs to obligation, not artifact. Query-by-time-period is a separate layer that relates to the skeleton the way ring 0 does - a projection over it - and modelling "week N" as a node joined by edges is not the right modelling.

**What this settles that the corpus left open.** The navigational-handle question - whether a course's own name for its coarse grouping (week for one course, module for another) is a modelled property - is settled **against modelling it**. Billy's ruling 8: calendar things belong on the calendar. The dropped `[B1]` proposal ("let the coarse grouping be the primary handle everywhere") and the dropped `lecture_date` field are both **not carried**, and now for a stated reason rather than by silent omission.

**The companion deferral, flagged rather than claimed.** The time layer itself needs designing and cannot be designed yet. Precondition, from rulings 3 and 8: **the schema, the API and the CLI shape have settled**, and then it gets its own session. Whether that is one deferral issue with C's M60 (`time_point`) or two, reconciliation should decide - it is the same wake-up condition.

**Sequencing stripped.** "`time_point` is graveyarded to slice 2." Ruling 3 restates the real reason: `time_point` is out because its reader, the calendar projection, is out - not because nothing reads it.

**Touched by Billy's rulings.** #8 decisively - it converts C27/E8 from "needs Billy" into a ruling, and it rejects the only proposed resolution the corpus contained. #3 supplies the precondition for the companion deferral.

**Cross-cluster.** C's M60 (`time_point`, and "the current plan") is the same deferral seen from the field side and shares ruling 3. F's M108 (calendar goes to Notion) is where "calendar things belong on the calendar" lands as a container fact. M34 (mine) forbids calling the coarse grouping a "chunk".

**Zoomed.** Yes - `model.md §9`'s invariant, verbatim, plus the retraction of `time-anchor` as a renamed `week`. The zoom confirms the invariant is stated as an invariant in the record and not merely inferred by a survey.

---

## M37. `backing`, and `text_extractable`

**Destination: `ADR`.**

**Proposed title:** *What enters the store is decided by what the store is for, not by file type and not by source class.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** The rule determines what the knowledge base contains; a corpus built under the wrong rule has to be rebuilt, and you cannot tell from the outside which entries were wrongly admitted or wrongly excluded. |
| Surprising without context | **Yes.** The obvious rule is by file type or by source class, and this project wrote *both* down before rejecting them - one of them as a Billy `[R]`. |
| Result of a real trade-off | **Yes.** File-type routing was falsified four ways in one slice. The source-class rule (RAG stores slides/pdf/textbook-class sources; handwritten notes excluded) was ruled 08-22 and is **overridden 08-29**. The cost of the replacement is real: inclusion becomes a per-artifact judgment rather than a lookup. |

**Body.** An artifact's content enters the store if and only if it yields semantic, decontextualized facts about course materials that improve the knowledge base's overall quality - a handwritten note qualifies on that test. `backing` cannot be inferred from file type and "chunkable" is the wrong axis: the real property is whether meaning survives linearization, which is a property of the materialization pass rather than of the file.

**Shape that rides.**

```
backing         ∈ {materialized_doc, code_project}      -- a node property
text_extractable: bool, per region, default false       -- true only when a pass actually recovered text
```

**The four falsifications, kept because they are the ADR's teeth.** Scanned handwriting in a PDF wrapper · a text PDF whose exercises are images, so backing is not uniform *within one file* · a `.png` holding a rendered prose block, more chunkable than several PDFs · one diagram held as both `.drawio` and `.png`. And the case that names the axis: in `visitor.png` the labels linearize but **the edges are the content**.

**Sequencing stripped.** "The artifact kind is slice 2, so this is deferred by slice." The rule is not deferred; only its writer is.

**Touched by Billy's rulings.** **#6, decisively.** It resolves C28, which the inventory escalated as needing Billy, and it does so by rejecting *both* recorded positions: not source class (A), and not quite the linearization axis either (B) - linearization is a property of the *pass*, and ruling 6 supplies the criterion the pass is judged against. The concrete change: `domain-design.md §10.7` ruling 3's exclusion of handwritten tutorial notes is **overridden**; those notes qualify if they improve the knowledge base, which matters because the measurement says they are a whole class in a core course, not an edge case. #7 also bears: material that would introduce a conflicting statement cannot simply be embedded alongside the statement it conflicts with.

**Cross-cluster.** **Heavy with E's M91** ("RAG source classes, and what is excluded"), which is the same ruling from the intake side and is now wrong as recorded. Reconciliation must not let both survive. Recommend: this ADR is the rule; E's M91 becomes the intake consequence or is dropped. E's M86 (always keep, judge only linkage) is compatible and worth citing - keeping is not embedding. D's M79 (the trust contract) is `text_extractable`'s reader.

**Zoomed.** No new zoom needed - the inventory quotes `derivation/FINDINGS.md §4.1` and `model.md §9` at length, and ruling 6 is newer than every source and settles it.

---

## M38. Detection of empty extraction, not OCR

**Destination: `ADR`.**

**Proposed title:** *A materialization pass must report that it recovered nothing; it does not OCR.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** Retrofitting detection after a corpus is built means re-materializing everything, because you cannot tell after the fact which entries were empty and which were genuinely thin. |
| Surprising without context | **Yes.** The obvious response to image-only material is OCR, and this rules OCR out while ruling detection in. |
| Result of a real trade-off | **Yes.** OCR, detection, and ignore were the three options. Detection wins because a silent empty index entry makes the corpus lie about its own coverage, which is the one failure the trust clause cannot absorb; OCR is a cost with no ruling behind it. |

**Body.** Material with no text layer is a whole class, not an edge case - four files returned zero extractable text across 27 pages in one course, and another course's tutorial notes are handwritten scans at about 23 extractable characters per page. The requirement this creates is **detection, not OCR**: `text_extractable` defaults false and is set true only when a pass actually recovered text, so an empty extraction is visible rather than silent.

**Cost, stated inside the ADR.** Detection catches *empty*. It does not catch *confidently wrong*: one assignment PDF returns the same header string, `"Course code: SFWRENG 2AA4"`, for all six pages - non-empty, confident, plausible, and wrong. "A silent wrong label is worse than no label" was pre-registered as the failure mode that matters, and this mechanism does not address it.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** #6 - the old collision (handwritten notes excluded by rule, versus handwritten scans being a whole class in a core course) dissolves: they are no longer excluded by class, so detection has to work on them rather than being spared them.

**Cross-cluster.** M37 (mine) owns the inclusion rule and shares `text_extractable`; these two ADRs should cite each other and not restate. D's M79 (the trust contract owed for generated content) is the reader that makes `text_extractable` load-bearing - it is what distinguishes a quotation from a generated description.

**Zoomed.** No. The probe findings are quoted with counts and the pre-registration is recorded in the source's own words.

---

## M39. One lecture, several files; `variant`; filename similarity implies nothing

**Destination: `ADR`.**

**Proposed title:** *One lecture is one node with a file list, not one node per file.*

| test | verdict |
|---|---|
| Hard to reverse | **Yes.** It is node granularity for the artifact layer; changing it re-nodes the layer and re-points every link into it. |
| Surprising without context | **Yes.** One file, one node is the obvious mapping, and it breaks on 9 of 21 lecture nodes in one course. |
| Result of a real trade-off | **Yes.** Three shapes were live: a node per file, a link between variants, and a file list on one node. The list wins because the query reads a list rather than a traversal - which is the rigidity rule applied to structure. |

**Body.** One lecture may be several files, so an artifact carries a file list with a `variant` tag rather than splitting into several nodes or acquiring a version link. Union is required, not subsumption: in 2 of 11 measured pairs each side holds content the other lacks. **Filename similarity must never imply a relation** - one same-named pair was two different lectures (Jaccard 0.21).

**Shape that rides.**

```
artifact := ... · files[]{ variant, text_extractable } · revised_at
```

**Sequencing stripped.** "Spec side silent, slice 2."

**Touched by Billy's rulings.** None directly.

**Cross-cluster.** M23 (mine) shares the Jaccard-0.21 case and the `revised_at` carrier - the "filename similarity implies nothing" clause should be stated once, in whichever of the two ADRs reconciliation prefers. M37 (mine) owns `text_extractable`, which appears in this shape. E's M92 (the portal's folder tree) is the intake sibling.

**Zoomed.** No. The measurements (9 of 21, Jaccard 0.50-0.69 for real variants, 0.21 for the collision, 2 of 11 needing union) are quoted with their source and uncontested across surveys.

---

# The term list

Everything cluster B proposes for `CONTEXT.md`. Clusters C, D and E should classify against this list. Terms marked **(from ADR)** are spun off from a thing routed to `ADR`: the decision lives in the ADR, the name lives here.

## The two persisted things

| term | definition | _Avoid_ |
|---|---|---|
| **skeleton** | The graph of nodes and links: what exists, how it relates, and a handle to content. One of the two persisted things. | *facts layer* · *compartment* · *the graph* (bare) · *skeleton kinds* (meaning the three layered kinds) |
| **store** | Materialized artifact content - chunks and embeddings - addressed either by a node handle or by similarity. The other persisted thing. | *corpus layer* · *the corpus* · *RAG store* (names only the by-query half) · `Store` as an interface name |

## The graph's parts

| term | definition | _Avoid_ |
|---|---|---|
| **node** | A record with a `kind`, an id in the single id space, and that kind's declared field set; anything that can be an endpoint of a link. | *entity* · *record* used interchangeably |
| **link** | A typed, directed relation between two refs, stored as its own record rather than as a field on either end. | **edge** |
| **link kind** *(from ADR, M22)* | The named, signature-constrained relation type a link carries; the set is closed and extended only by adding a row. | *edge type* · *relation type* |
| **Ref** *(from ADR, M31)* | A pointer to a node: its kind plus its id. It may name something that does not exist. | *foreign key* (it is explicitly not one) · *pointer* as the noun |
| **locator** *(from ADR, M30)* | The fragment a link points into - a section, a page, a method, a question - stored verbatim as the source string. | *citation* · *fragment* · *anchor* |

## The two axes

| term | definition | _Avoid_ |
|---|---|---|
| **kind** | The named record schema a node's payload conforms to, carried on the node as a required discriminator field whose value is the kind's own name. Current set: `course` · `obligation` · `sticky_note` · `progress` · `concept` · `artifact`. | *type* · *node type* · *layer* · *metadata* |
| **layer** | One of the three strata of the domain graph - `obligation`, `concept`, `artifact`. Only those three kinds have one. | *skeleton kinds* · *content layer* (see the collision note) |

## The three layers

| term | definition | _Avoid_ |
|---|---|---|
| **obligation** | A thing with a deadline. The only layer that carries time, and the same nodes ring 0 is a projection of. | *task* · *assignment* · *deadline* as the noun |
| **concept** | A unit of subject matter the course teaches, independently addressable. | *topic* · "a thing the student understands or does not" (retracted) |
| **artifact** | A thing the course delivers and that is opened independently. | *file* · *document* · *resource* · "a thing that exists on disk" (falsified) |

## Two link kinds that need distinguishing by name

| term | definition | _Avoid_ |
|---|---|---|
| **covers** | The relation asserting that an artifact teaches a concept as its subject. It is the rendered relation. | using `covers` for a mention (full-text finds mention; title-scoped finds coverage) |
| **applies** | The relation asserting that an artifact uses a concept without teaching it. It feeds closure and is never rendered. | *uses* · *mentions* (that name belonged to the cut announcement link) |

## The store's vocabulary

| term | definition | _Avoid_ |
|---|---|---|
| **materialization** | The one-time pass turning an artifact's raw content into stored readable form - normalize, chunk, summarize, tag. Paid once, and it happens whether or not anything is embedded. | *indexing* · *embedding* · *ingestion* |
| **chunk** | A unit of an artifact's materialized content, stored with its node id, an ordinal, its text, an optional locator and its embedding. | *chunk* meaning a course's coarse grouping (a week, a module) |
| **by-handle** *(from ADR, M33)* | The store access mode that fetches the chunks a known node points at. Deterministic, no similarity. | *JOIN mode* · *direct read* |
| **by-query** *(from ADR, M33)* | The store access mode that searches by similarity when you do not know where to go. The only half of the store that is RAG. | *RAG* used for the whole store · *search* |

## Two written objects

| term | definition | _Avoid_ |
|---|---|---|
| **summary** | A written one-line object carried only by a node whose identity is content the skeleton does not hold; in the current kind set, the `artifact` alone. Every other kind's line is composed from fields it already stores. | *node summary* · *concise summary* |
| **materialized summary** | The per-artifact summary the materialization pass produces, which lives in the store and which the coordinator never sees. A different object from `summary`. | calling it `summary` unqualified |

## One rule that is a term

| term | definition | _Avoid_ |
|---|---|---|
| **rigidity rule** | The test for whether a field exists: a field is typed if and only if some mechanism reads it, which is what makes deferring a schema decision free. It admits **declared exemptions** (`grade_share`, `added_at`); it is not absolute. | *the typing rule* · stating it without the exemption clause |

**21 terms.**

## Terms cluster B depends on but does not claim

- **ring 0** - cluster D (M66). Must be written compatibly with M32: not a third persisted thing, an access policy over `obligation` nodes.
- **annotation** - cluster C (M51/M57). My `about` link's signature is `annotation → any`, so the term must exist.
- **coordinator** - cluster D. Used in M33's ADR.
- **`id`** - cluster C (M40). My `Ref` and one-id-space commitment depend on it, and M30 notes that links are deliberately identified by a *natural key* instead.
- **`course` / `sticky_note` / `progress` as kinds** - cluster C. Named in my `kind` definition.

## The two vocabulary collisions cluster B is escalating

1. **`layer`.** Reserved here for the three strata. Billy's 08-29 ruling 8 uses "content layer / time layer" in a coarser sense. Proposal: say **the skeleton** and **the time projection** instead. This is Billy's own phrasing, so it is a proposal.
2. **"skeleton kinds".** `design.md §3.1` uses it to mean the three layered kinds, but `course` and `sticky_note` are also nodes in the skeleton. Say **layered kinds**.

---

# Summary

**Counts.** `CONTEXT` **6** (M13, M14, M15, M26, M27, M34) · `ADR` **16** (M16, M17, M19, M20, M22, M23, M24, M25, M30, M31, M32, M33, M36, M37, M38, M39) · `DEFER` **4** (M21, M28, M29, M35) · `DROP` **1** (M18). Total **27**.

**Term list: 21 terms**, plus 5 depended-on terms owned by other clusters and 2 escalated collisions.

**Sequencing stripped, gathered.** Slice assignments were dropped from M13, M15, M16, M18, M20, M21, M22, M27, M28, M29, M30, M32, M33, M34, M35, M36, M37, M39. The two heaviest: **M22** loses the LinkKind table's slice column and the sentence "slice 1 implements exactly one row of this table", and **M15** loses "slice 1 introduces four kinds, slice 2 adds two" whole. Both are orderings that read as structure, which is the exact failure this repo's brief warns about.

**Least certain calls.**

1. **M14 as `CONTEXT` rather than `ADR`.** The 08-28 ruling that only artifacts carry a written summary is genuinely surprising and had real alternatives ("is it worth opening", the agent's question-answering amendment, the two-summaries-per-node proposal). I routed it to `CONTEXT` because the surviving content is a definition and because two objects share the word, which is glossary work. A reconciler who prefers the ADR reading has a case.
2. **M18 as `DROP`.** I am dropping the positive claim "the artifact layer is the tree", which is measured and true, on the ground that nothing reads it. If a rendering decision later needs it, it will have to be re-derived from `model.md §2`.
3. **M25's scope.** "Relations are records, not fields on the related thing" is one of five refactor triggers, and the other four are scattered across clusters C and F. Recording one trigger as an ADR while its siblings land elsewhere may be worse than recording all five once.
4. **M13 versus M32.** I split one corpus argument into a `CONTEXT` half (the names) and an `ADR` half (the ruling). It is the right split, but if reconciliation reads M13 and M32 as one thing, the ADR should absorb the names.

**Cross-cluster flags, gathered.**

| from | to | what |
|---|---|---|
| M13 | D (M66) | `ring 0` is D's term; M32 fixes its status as not separately persisted |
| M14 | C (M55), D (M76, M79) | `label` versus `summary` stays deferred; `look_at` returns a summary |
| M15 | **C (M42)** | direct duplicate on `kind` / `layer`. Proposal: C owns the mechanism ADR, B owns the names |
| M15 | C (M41, M51, M57) | `course`, `progress`, `sticky_note` definitions must match this list |
| M16 | C (M41, M44) | `course.id` is supplied, not assigned; course membership is a field, not a link |
| M17 | E (M92) | same argument aimed at intake; should be one ruling with two consequences |
| M19 | C (M51), D (M79), E (M84, M86) | "surface for confirmation, never resolve" appears in four things across three clusters |
| M20 | C (M62) | `present` / `external_ref` / `backing: referenced_only` belong in the graveyard |
| M21 | A (M11), F (M102), E (M87) | instrument readiness is the shared precondition |
| M22 | C (M51/M57), A (M5), **orphan** | `annotation` is a signature endpoint; **`closure` is single-source, not all-pairs, has no M-number in any cluster and will be lost unless someone claims it** |
| M23 | E (M85, M90), C (M62) | ruling 7's resolve-and-report / ask-first split is E's write rule; `supersedes` belongs in the graveyard |
| M24 | E (M83, M89, M90), C (M57) | announcements as intake is E's; `origin` as a field is C's. Also: `model.md §8`/`§9` mis-cite §10.6 |
| M25 | C (M42, M43), F (M98) | the five refactor triggers should be recorded once, in one place |
| M26 | C (M43, M47), D (M68), E | the two exemptions live with their fields; D's membership test is a *different* test and must not merge |
| M28 | C (M49), E (M94) | `write-rules.md §3.4`'s recurrence rule **is** the concept-granularity ruling; neither record says so. **C21 should be closed, not carried** |
| M30 | C (M40) | nodes get opaque assigned ids, links get a natural key - a deliberate asymmetry no survey states |
| M31 | **C (M40, M41)** | both records claim "one id space"; pick one home |
| M32 | D (M66), F (M103, M106) | persistence consequences should cite, not restate |
| M33 | **D (M73, M75)**, F (M104) | the observation contract is D's; the type-level enforcement is B's; TypeScript rests on it |
| M34 | E (M91), D (M79) | materialization versus ingestion is a live word collision |
| M35 | F (M103, M107) | the dropped stack (pgvector, HNSW, Supabase) is a container artifact |
| M36 | **C (M60)**, F (M108) | same deferral, same wake-up condition (ruling 3); calendar goes to the calendar |
| M37 | **E (M91)** | E's record of the source-class rule is now wrong; both must not survive |
| M38 | D (M79), M37 | `text_extractable`'s reader is the trust contract |
| M39 | M23, E (M92), M37 | "filename similarity implies nothing" should be stated once |
