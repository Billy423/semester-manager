# Reconciled classification - one coherent set from six parallel passes

**What this is.** Six agents classified 115 things from the fall26 design corpus, one cluster each, blind to each other. This pass merges the six proposals into one set that can be written to disk without collisions. **Nothing here is created:** no `CONTEXT.md`, no ADR file, no issue, and no ADR numbers. Slugs only.

A second reconciler is separately handling the residue - rulings no cluster classified. Everything below is inside the six tables. Orphans raised by a cluster but carrying no M-number are named where they bear on a thing I carry, and routed onward otherwise.

**Counts, before and after.**

| destination | proposed | final | change |
|---|---|---|---|
| `CONTEXT.md` terms | ~41 | **46** | +5 |
| `CONTEXT.md` things | 13 | **13** | - |
| `docs/adr/` ADRs | 68 proposals | **61 ADRs** | −7 |
| `docs/adr/` things | 68 | **67** | −1 (M112 re-homed) |
| Deferral issues | ~27 proposals over 26 things | **17 issues** | −10 |
| Not carried | 8 | **9** | +1 (M112) |

**The headline finding, and it cuts against the hypothesis.** Billy's reading was that 115 things cut fine for lookup would map to ADRs as a group-and-merge, and that the high ADR count is an artifact of the cut. Tested item by item against the strict rule - *same rejected alternatives and same reason* - **the hypothesis is only weakly supported.** Six merges survived the test out of roughly twenty proposed. Two proposals had to be **split** because a cluster had bundled two trade-offs, one ADR had to be **created** because a decision existed with no owner, and one was routed out of `docs/adr/` entirely. The net is 68 → 61, a 10% reduction, not the halving the framing anticipated.

The reason is worth stating: most of the near-merges share a **subject** (one field, one record, one section of `schema.md`) and not a trade-off. The fine cut was not an artifact. It tracked something real - the corpus made many small decisions about the same objects, on different evidence, on different days.

Where the count *did* collapse is the deferral set: 26 things to 17 issues. Deferrals merge on one wake-up condition, and the corpus has far fewer distinct gates than it has open questions. Four gates (a surface exists · the instrument can run · the concept kind exists · v2) account for eleven of the twenty-six things.

---

## The term set

46 terms, grouped under twelve subheadings. The grouping scheme is stated in the next section. Where a cluster's definition was amended to satisfy a dependent in another cluster, the amendment is marked **[amended]** and explained in `Dependencies satisfied` at the end of this section.

**One statement that belongs at the top of `CONTEXT.md`, per cluster D:** these are the **engineering** names. Ruling 9 says the product-facing verb names are undecided and "obviously cannot be `ring 0` and `skeleton`". Saying that once at the top of the file removes the need to say it in six entries.

### The two persisted things

| term | definition | _Avoid_ |
|---|---|---|
| **skeleton** | The graph of nodes and links: what exists, how it relates, and a handle to content. One of the two persisted things. | *facts layer* · *compartment* · *the graph* (bare) · *skeleton kinds* meaning the three layered kinds |
| **store** **[amended]** | Materialized artifact content - chunks and embeddings - addressed either by a node handle or by similarity. It holds semantic, decontextualized facts about course materials. The other persisted thing. | *corpus layer* · *the corpus* · *RAG store* (names only the by-query half) · `Store` as an interface name |

### Nodes, links and pointers

| term | definition | _Avoid_ |
|---|---|---|
| **node** | A record with a `kind`, an id in the single id space, and that kind's declared field set; anything that can be an endpoint of a link. | *entity* · *record* used interchangeably |
| **link** | A typed, directed relation between two refs, stored as its own record rather than as a field on either end. | **edge** |
| **link kind** | The named, signature-constrained relation type a link carries; the set is closed and extended only by adding a row. | *edge type* · *relation type* |
| **id** **[amended]** | An opaque, monotone value assigned by the system from **one id space shared by every kind that can be a link endpoint**. It says nothing about the record it names, is never reused, and is obtained only by reading it back. | *key* · *slug* · *handle* used for the stored value · any id derived from a name |
| **Ref** **[amended]** | A pointer to a node: its kind plus its id, drawn from the one id space `id` defines. It may name something that does not exist. | *foreign key* (it is explicitly not one) · *pointer* as the noun |
| **handle** *(newly claimed)* | What a render carries so the level below stays reachable. The `id` is what the store holds; the handle is what a surface prints or resolves, and every read that returns records returns one. | using *handle* and *id* interchangeably · a handle that appears in one render branch and not another |
| **locator** | The fragment a link points into - a section, a page, a method, a question - stored verbatim as the source string. | *citation* · *fragment* · *anchor* |

### The two axes

| term | definition | _Avoid_ |
|---|---|---|
| **kind** | The named record schema a node's payload conforms to, carried on the node as a required discriminator field whose value is the kind's own name. Current set: `course` · `obligation` · `sticky_note` · `progress` · `concept` · `artifact`. | *type* · *node type* · *layer* · *metadata* |
| **layer** **[amended]** | One of the three strata of the domain graph - `obligation`, `concept`, `artifact`. Only those three kinds have one. Billy's coarser content-versus-time distinction is **the skeleton** versus **the time projection**, not two layers. | *skeleton kinds* (say **layered kinds**) · *content layer* · *time layer* |

### The kinds

| term | definition | _Avoid_ |
|---|---|---|
| **course** | A kind, and a node: the unit a term's obligations are owed to. Its id is the supplied course code rather than an assigned one, because the source issues a canonical unique one. | *namespace* · *scope* · treating it as a container rather than a node |
| **obligation** | A thing with a deadline. The only layer that carries time, and the same nodes ring 0 is a projection of. | *task* · *assignment* · *deadline* as the noun |
| **concept** | A unit of subject matter the course teaches, independently addressable. | *topic* · "a thing the student understands or does not" (retracted) |
| **artifact** | A thing the course delivers and that is opened independently. | *file* · *document* · *resource* · "a thing that exists on disk" (falsified) |
| **annotation** | A node kind whose record is a single dated claim about another node, reached by an `about` link rather than by a field. A tag over `sticky_note` and `progress`, not a type hierarchy. | *note* used for both kinds · *metadata* · treating it as a supertype with subtypes |
| **sticky_note** | An annotation carrying one free-text statement about its target, with an open-set `category` and a provenance `origin`. Cheap to attach, modify and detach, because it points at a node rather than being a property of one. | *note* (bare) · *comment* · *correction layer* · *corpus override* |
| **progress** **[amended]** | An annotation stating how far along its target's work is, carrying a non-nullable `state` and a prose `detail`. A target with no progress record reads as `not_started`. | *status* - **`obligation.status` is dead and `progress.state` is live**; the two are not the same word · *completion* · *mastery* · a `sticky_note.category` value |

### Fields that carried several names

| term | definition | _Avoid_ |
|---|---|---|
| **name** | The short label a person recognises a record by, stored exactly as the source prints it. It is not the handle and nothing is derived from it. | **label** · *title* · *description* |
| **due** | The moment an obligation is anchored to - the deadline for something handed in, the start for a sitting. A date without a time is the **end** of that day, `23:59`. | *deadline* as the field name · *date* · assuming a date-only value is the start of the day |
| **done_by** | The date the owner chose to have an obligation finished by. A stored value always means it was chosen; nothing computes one. | **target_date** (Billy's own Notion name for the same field) · **finished_by** · rendering it as a *start* date |
| **grade_share** | The approximate share of the final course grade an obligation carries, in percent, held for the person to read and never as an input to a computed ranking. | **weight** · **worth_percent** · reading a column of shares as a partition of 100 |
| **parts** | The concepts an obligation's source carries, as raw strings written in canonical singular form, kept only where a concept might recur elsewhere. It carries no size, no status and no score. | *sub-items* · *components* · treating the strings as pointers to concept nodes · using it to judge how much work something is |
| **origin** | How an annotation came to exist - an announcement, someone saying so, or the system having asked. One field with one name across both annotation kinds; it does not confer immutability. | *source* · *provenance* as the field name · a second copy per kind |

### Two link kinds that need distinguishing by name

| term | definition | _Avoid_ |
|---|---|---|
| **covers** | The relation asserting that an artifact teaches a concept as its subject. It is the rendered relation. | using `covers` for a mention - full-text finds mention, title-scoped finds coverage |
| **applies** | The relation asserting that an artifact uses a concept without teaching it. It feeds closure and is never rendered. | *uses* · *mentions* (that name belonged to the cut announcement link) |

### The store's vocabulary

| term | definition | _Avoid_ |
|---|---|---|
| **materialization** | The one-time pass turning an artifact's raw content into stored readable form - normalize, chunk, summarize, tag. Paid once, and it happens whether or not anything is embedded. | **ingestion** (retired, see below) · *indexing* · *embedding* |
| **chunk** | A unit of an artifact's materialized content, stored with its node id, an ordinal, its text, an optional locator and its embedding. | *chunk* meaning a course's coarse grouping (a week, a module) |
| **by-handle** | The store access mode that fetches the chunks a known node points at. Deterministic, no similarity. | *JOIN mode* · *direct read* |
| **by-query** | The store access mode that searches by similarity when you do not know where to go. The only half of the store that is RAG. | *RAG* used for the whole store · *search* |

### The two written objects

| term | definition | _Avoid_ |
|---|---|---|
| **summary** | A written one-line object carried only by a node whose identity is content the skeleton does not hold; in the current kind set, the `artifact` alone. Every other kind's line is composed from fields it already stores. | *node summary* · *concise summary* |
| **materialized summary** | The per-artifact summary the materialization pass produces, which lives in the store and which the coordinator never sees. A different object from `summary`. | calling it `summary` unqualified |

### Residency and the read path

| term | definition | _Avoid_ |
|---|---|---|
| **ring 0** **[amended]** | The obligation layer under a residency policy: the fixed-shape, uniform-depth set of **obligation fields** the coordinator holds in its conversation context so it can tell where to look next. It governs **residency, not readability**, is field-grained rather than node-grained, and is not a third persisted thing. | *the projection* (bare) · *the obligation layer* as a synonym · *the resident projection* · ring 0 meaning **what is observable** · ring 0 meaning **what is readable** |
| **band A** / **band B** | The two halves of ring 0's partition. **Band A "active"** is any obligation whose `due` or `done_by` falls in `today-7d .. today+14d` or whose `state` is `in_progress`; **band B "known"** is everything else, including obligations with no date. | *the active window* for band A (the window is one of three triggers, not the partition) · *urgent* / *backlog* |
| **coordinator** | The single long-running agent conversation Billy talks to - it holds ring 0, dispatches, walks the graph and writes the plan. A **conversation**, not a process: its scale is days to weeks, and every call it makes may run in a new process. **Resident** means held in the conversation's context, never in a process's memory. | *master session* · *the agent* (bare) · *orchestrator* · **"the coordinator's lifetime"** without saying which one |
| **the walk** | The operation that follows a node's edges and reads its neighbours' definitions - deterministic, O(degree), no store, no embeddings. Its internal name is `look_at(node_id, question)`; the product-facing name is undecided. | *search* · *find_material* · *retrieval* · treating the walk and a by-query store read as one operation |
| **dispatch** | Sending a question out of the coordinator's context - to a subagent, a task session, or **Billy himself** - and receiving back a value in the same shape as every peer's. The context that produced the value stays outside. | *delegate* · *spawn* · *ask* (asking Billy is one case of dispatch, not a different mechanism) |

### The inbound path

| term | definition | _Avoid_ |
|---|---|---|
| **extraction** | The pass that reads delivered material and produces candidate facts. It changes with the material. | **ingestion** · *parsing* · using it for what happens to the candidates afterwards |
| **landing** | The write of candidate facts into the skeleton. It is idempotent, it detects conflicts instead of overwriting, and it changes with the schema. | **ingestion** · *import* · `land()` as the name of the concern rather than of one operation |
| **conflict** | Two statements the system holds that cannot both be true of the same thing. It is shallow or deep by what is in conflict, and that is what decides whether the agent may close it itself. | *contradiction* used interchangeably · using it for a mismatch between system and world, which is **staleness** · using it for a progress claim, which is an authorship question |

**`ingestion` is retired as a term of this project.** One of its senses names something ruled out of scope (the system does not fetch); the other names three concerns a record already separates because they change for unlike reasons - **extraction** (with the material) · **landing** (with the schema) · reading (with agent-engineering practice) - plus **materialization**, which is correctly named. The word appears only in `_Avoid_`, on all three.

### Rules that are terms

| term | definition | _Avoid_ |
|---|---|---|
| **the rigidity rule** | The test for whether a field exists: a field is typed if and only if some mechanism reads it, which is what makes deferring a schema decision free. It admits **declared exemptions** (`grade_share`, `added_at`); it is not absolute. | *the typing rule* · *rigidity follows importance* · stating it without the exemption clause |
| **the render test** | The test for whether a note is worth writing: *is it worth being written down so that every time I look at this node, the note comes with it?* A note is not a place to put things that are true; it is a thing that appears every time its target is read. | *the note rule* · *the usefulness test* · stating it as *is this true and relevant* |
| **the write rule** | An instruction to whoever produces a value for a field whose legal values cannot be enumerated. It is derived from what has to be true for the node to **render well**, never from what a source document happens to say. | the withdrawn absolute *"a write rule never refers to the source"* · *validation* (a write rule is enforced nowhere) · *schema rule* |
| **the graveyard** | The section of the field-set record listing removed fields with the reason each was removed, under a standing rule that no later session restores one without a new ruling. Its rulings bind; its arithmetic does not. | *deprecated fields* · *the exclusion list* · *deliberately absent* as the section's name in prose |

### The project's own words

| term | definition | _Avoid_ |
|---|---|---|
| **faithfulness** | The system's promise about its own claims: every claim traces to a fact the system holds, no relevant held fact is omitted, and nothing is invented. It is a promise of complete recall over what the system was told, never of coverage of the world. | *the trust clause* · *verification* · *accuracy* · *precision and recall* (that framing is voided in place) |
| **reload** *(newly claimed)* | The full reconstruction of a course's context a person performs in order to *interpret* one notice rather than merely read it. Five concurrent courses is five reloads, and collapsing them is what the system exists to do. | *context switch* · *catching up* · treating it as a retrieval problem |

### Dependencies satisfied

Eleven terms are owned by one cluster and depended on by others. Each surviving definition was checked against its dependents; five needed amendment.

| term | owner | dependents | amendment |
|---|---|---|---|
| **ring 0** | D | B/M32, B/M13 | **Field-grained, not node-grained** (dispute 2). `ring-0.md §4` admits seven of an obligation's fields and excludes two from the same node. B/M32's ADR body inherits the same correction. |
| **store** | B | E/M91, D/M79, B/M37 | Ruling 6's content clause added, so a reader of the term is not left to infer inclusion from "artifact content". |
| **id** | C | B/M31, B/M30, F/M101 | **Owns the one-id-space clause** (dispute 1). `Ref` and `handle` now cite it rather than restating it. |
| **layer** | B | C/M42, D | Billy's coarse sense named as *the skeleton* / *the time projection*; "skeleton kinds" replaced by *layered kinds* (dispute 6). |
| **progress** | C | B/M15, B/M19, D/M76 | `_Avoid_` carries the `obligation.status` / `progress.state` do-not-confuse clause, which no survey stated. |
| **concept** | B | E/M94, C/M49 | **No amendment.** E is right that the definition is incomplete as a *write-side rule* - not every independently addressable unit gets a node, only a recurring one does - but that is an admission rule and belongs in `parts-carries-recurring-concepts-not-size`, not in the definition of what a concept IS. |
| **annotation** | C | B/M22 (`about : annotation → any`) | No amendment; the signature holds as written. |
| **summary** | B | D/M76, C/M55 | No amendment. B's "only the artifact carries a written summary" is what makes the walk's one-hop answer work, and both entries leave the render's naming open. |
| **materialization** | B | E/M81, C/M56 | `ingestion` added to `_Avoid_`. |
| **coordinator** | D | A, F/M103 | Carries the `resident` guard directly, since E1's voidness rests on it (dispute 5). |
| **the rigidity rule** | B | A/M10, C/M43, C/M47, F/M110 | No amendment. F's `/promote` hand-off ("only typed fields make migrations, so deferring a field decision is free") is already inside B's definition. |

---

## Grouping for `CONTEXT.md`

**The scheme: group by what kind of thing the term names, not by which record it came from.** A reader arrives at `CONTEXT.md` holding a word they met in code or in a conversation, and what they know about it is its grammatical role - is it a stored thing, a field, an operation, a rule. They do not know which cluster owned it. Twelve headings, none longer than seven entries, ordered outward from the data to the words the project uses about itself:

1. **The two persisted things** (2) - the top of the model; everything else is inside one of them.
2. **Nodes, links and pointers** (7) - the graph's mechanical vocabulary.
3. **The two axes** (2) - `kind` and `layer`, placed together because conflating them is the named failure mode.
4. **The kinds** (7) - the six node kinds plus `annotation`, the tag over two of them.
5. **Fields that carried several names** (6) - every entry here exists because the corpus used two or three names for one field; the `_Avoid_` line is the point of the entry.
6. **Two link kinds that need distinguishing by name** (2) - `covers` / `applies`, whose difference cannot be read off the link table.
7. **The store's vocabulary** (4).
8. **The two written objects** (2) - two things called "summary".
9. **Residency and the read path** (5).
10. **The inbound path** (3).
11. **Rules that are terms** (4) - named tests invoked by name across records.
12. **The project's own words** (2) - `faithfulness` and `reload`, the two words that carry the product's reason for existing.

Groups 5, 6, 8 and 11 are the ones that justify a glossary at all: each entry exists because a word means two things or a thing has two words. Groups 1-4 are the spine a newcomer reads top to bottom.

---

## The ADR set

61 ADRs. Slugs are kebab-case with no number. **Absorbs** names the M-numbers the ADR carries.

### Purpose and trust

| slug | title | body | shape | absorbs |
|---|---|---|---|---|
| `three-jobs-not-precise-answers` | The system's job is three jobs, and precise question-answering is not one of them | The product is not a reminder system and not an enterprise RAG that answers every question precisely: five concurrent courses produce a fear of not holding the whole picture, and it is *interpreting* a notice, not reading it, that forces a full reload. The three jobs are to remove the anxiety of not finding information, to manage cross-course information in the background, and to locate details Billy does not know to ask about. For unfamiliar material the reload is first construction rather than recall, so helping model an assignment's requirements is in scope. | - | M1 |
| `no-outward-completeness-assertion` | The system makes no assertions about its own completeness | The system never asserts its own completeness or freshness; integrity work runs silently and is not reported as a status. Trust accrues from being useful, and a self-report that can go stale is worse than none because it lies confidently. This is not a rule against speaking: the agent still reports actions it took and still asks before it resolves anything deep. | - | M4 |
| `job-three-is-set-difference-not-recall-tuning` | Surfacing what Billy did not ask about is a deterministic set-difference query, not recall-tuned retrieval | The third job is served by subtraction over the graph, not by loosening retrieval: the query scans one layer and returns nodes that have no link of the named kind in the named direction. It means exactly that, and never "a node lacking a kind". | `nodes_without(node_kind, link_kind, direction) -> [Node]` | M5 |
| `expansion-cost-is-the-size-gate` | The size gate is expansion cost, not total graph size | Nothing ever renders the whole graph, so total size is the wrong quantity to budget: what must stay bounded is the cost of going one level deeper. Each level renders what is around it, and one level deeper is one more call. | - | M6 |
| `the-store-accumulates-it-is-never-synced` | The store accumulates; it is never synchronised against a source | This is not a system kept aligned with a remote, it is a knowledge base that accumulates: things enter, stale or wrong things leave, and everything is classifiable and queryable. There is no full re-read, no diff against a source, and no mirror state, because there is no correspondence to maintain. Accumulation is not permission for two conflicting statements to sit side by side. | - | M8 |
| `under-model-deliberately` | Under-model deliberately: the relationships cannot be written today | The cases cannot be enumerated today and the relationships cannot be written out today, so the design is a tiny mechanical core plus everything else free, which is not vagueness everywhere. Completing the model is satisfying and mostly wrong; a thing enters the typed core when evidence and a reader for it exist, and a graveyarded thing does not come back without a new ruling. | - | M10 |

### Shape - the graph

| slug | title | body | shape | absorbs |
|---|---|---|---|---|
| `a-course-is-a-node` | A course is a node, not a namespace | A `course` is a node, so `get(Ref("course","2c03"))` resolves and an `about` link to a course is an ordinary link with no special case. The forcing case is course-level notes: the late-day budget is not a property of any obligation, and without a course node it has nowhere to land. | - | M16 |
| `layered-graph-not-a-tree` | The skeleton is a layered graph; the model may not cut edges to force a tree | A concept appearing in two places is the truth of the data, not a rendering bug, so the model may not cut edges to force a tree. A file is not the object being modelled: a lecture PDF and a tutorial PDF exist and are used independently, yet both describe one concept. Which spine a view renders is the surface's decision. | - | M17 |
| `modelling-layer-is-stateless` | The modelling layer is stateless: system-inferred mastery is forbidden | The modelling layer records no state about the owner: it presents concepts and leaves judgment to him. Surviving set-difference queries are structural ("this concept has no artifact covering it"), never personal ("you never opened X"). An agent may surface a progress claim for confirmation but may never resolve one. | Enforcement point: **nowhere, deliberately** - it is a rule about the caller. | M19 |
| `artifact-existence-is-not-a-field` | An artifact's existence is not a field; absence is the absence of store content | An artifact does not need a URL or a `present` flag. Absence has no field: it is the absence of store content for that node, read as a join. **Cost, stated inside:** a node with no store content is indistinguishable from a node that was never created - the field question was ruled, the distinguishability question was never put. | - | M20 |
| `the-closed-link-kind-set` | Links are a closed typed set, each with an endpoint signature; a relation earns a row only with three real instances and a nameable query | Every relation is a `Link` with a `LinkKind` whose signature constrains its endpoints, so adding a relation is a table row plus a signature rather than a schema change. A relation earns a row only if the material shows at least three real instances and someone can name the query that reads it. | The nine-row LinkKind table: `about` `annotation→any` · `covers` `artifact→concept` · `applies` `artifact→concept` · `requires` `concept→concept` · `requires` `obligation→concept` · `spec` `obligation→artifact, role ∈ {given, owed}` · `prepares-for` `artifact→obligation` · `builds-on` `obligation→obligation` · `part-of` `concept→concept` (a **DAG**) | M22 |
| `no-supersedes-link` | There is no `supersedes` link; revisions replace in place and are dated | No `supersedes` link kind exists. Every real revision replaced the file at the same path under the same name, so there is no prior version to point at; a `supersedes` link would mistype three shapes and hide a live document. Revision is carried by `revised_at`. | - | M23 |
| `an-announcement-is-a-provenance-value` | An announcement is a provenance value, not a node and not a link | An announcement is the `origin` field of an annotation plus a flat provenance log; it is not a node and there is no `mentions` link. What an announcement carries is almost always a correction against material the system already holds, not new knowledge. | - | M24 |
| `relations-are-records-not-fields` | Relations are records, not fields on the related thing | A relation between two things is its own record, never a field on either end. A note's target is an `about` link, not a `target_id`. The genuine alternative was live and written down - infer relations at read time, "affordable because the layer fits" - and it was overturned by the project's own rigidity rule once `obligation → concept` acquired a mechanism that reads it. | - | M25 |
| `link-identity-is-a-natural-key` | A link's identity is its natural key, and `locator` is part of it | A link's identity is the natural key `(from, to, kind, role, locator)`; there is no surrogate id. `locator` is in the key because omitting it silently destroys edges - one deck cites the textbook four times at four different sections, and those are four links, not one. **Nodes get opaque assigned ids and links get no surrogate id at all; the asymmetry is deliberate.** | `Link := from: Ref · to: Ref · kind: LinkKind · role?: string · locator?: string` / `identity := (from, to, kind, role, locator)` | M30 |
| `a-ref-is-not-a-foreign-key` | A ref is not a foreign key: a ref may name something that is not there | A pointer is a `Ref := (kind, id)` drawn from the one id space. The kind tag makes a ref resolvable without a lookup, which is what lets a link be validated at write time against its signature. A ref may name something that is not there, so it is not a foreign key and deleting a record does not have to cascade. **Owed and unbuilt: the validation pass over the link set.** | - | M31 |
| `two-persisted-things-one-coupling-field` | Exactly two persisted things, coupled by one field; ring 0 is not a third | There are exactly two persisted things: the skeleton (nodes and links) and the store (chunks and embeddings). Ring 0 is not a third: residency is an access policy over **obligation nodes' fields**, not a separate store. The coupling surface between the two is exactly one field, `chunk.node_id`, which is what lets each degrade without the other. | ring 0 - not separately persisted · skeleton - persisted · store - persisted | M32 |
| `the-purity-cut-is-enforced-by-return-type` | The purity cut is enforced by return type, not by tool registry or prompt | The store has two access modes - **by-handle** (a lookup on `chunk.node_id`) and **by-query** (nearest-neighbour over embeddings). The coordinator holds neither: it holds the skeleton interface only, and the skeleton's return type has no field a chunk could arrive in. The cut sits above both store modes, not between them, and **the type-level version is preferred because it survives a change of container.** | - | M33 |
| `the-skeleton-carries-no-time-axis` | The skeleton carries no time axis; time is a separate projection, not nodes and edges | The skeleton is a content and domain graph and has no time axis. The only time on a node is `due`, which belongs to obligation, not artifact. Query-by-time-period is a separate projection over the skeleton the way ring 0 is, and modelling "week N" as a node joined by edges is not the right modelling. A course's own coarse grouping - week for one course, module for another - is deliberately not modelled. | - | M36 |
| `materialization-reports-empty-extraction-not-ocr` | A materialization pass must report that it recovered nothing; it does not OCR | Material with no text layer is a whole class, not an edge case. The requirement is **detection, not OCR**: `text_extractable` defaults false and is set true only when a pass actually recovered text, so an empty extraction is visible rather than silent. **Cost, stated inside:** detection catches *empty*, not *confidently wrong* - one assignment PDF returns the same header string for all six pages. | - | M38 |
| `one-lecture-is-one-node-with-a-file-list` | One lecture is one node with a file list, not one node per file | One lecture may be several files, so an artifact carries a file list with a `variant` tag rather than splitting into several nodes or acquiring a version link. Union is required, not subsumption: in 2 of 11 measured pairs each side holds content the other lacks. **Filename similarity must never imply a relation** - one same-named pair was two different lectures (Jaccard 0.21). | `artifact := ... · files[]{ variant, text_extractable } · revised_at` | M39 |

### Fields and identity

| slug | title | body | shape | absorbs |
|---|---|---|---|---|
| `ids-are-opaque-assigned-and-never-constructed` | An id is opaque, assigned and never constructed; one id space, and every read returns handles | An `id` is opaque, monotone and assigned by the system, taken from **one id space shared by every kind that can be a link endpoint**, and never reused, a delete included. Nothing constructs one: an id is obtained by reading it back, so **every read that returns records must return their ids**. Constructing an id is a bet on reproducing another writer's spelling - a cognition problem wearing a mechanism's clothes. | `id := the next unused value in ONE id space` / `never reused, a delete included` / `obtained by reading it back; nothing constructs one` | M40 |
| `ids-are-supplied-where-the-material-supplies-one` | The id space is deliberately not uniformly opaque: an id is assigned only where the material supplies none | `course.id` is the supplied course code, and the line is drawn by the material rather than by the kind: an id is assigned only where the material supplies no identifier of its own, which today is every kind but `course`. A course code is canonical, unique and consistent wherever it appears, which is exactly what an obligation's name is not. **This is scoped to the kinds that exist and settles nothing about `concept` or `artifact`.** | - | M41 |
| `kind-is-a-discriminator-layer-is-another-axis` | `kind` is a required discriminator, not metadata, and `layer` is a different axis | Every node record carries a required discriminator field named `kind` whose value is that kind's own name; it selects which declared field set the payload has, and a record cannot be constructed without it. Shape-sniffing was the live alternative and loses because dispatching on which fields are present is exactly the control flow trigger B forbids. **`layer` is a different axis** and only three kinds have one. | - | M42 |
| `four-conventions-over-every-kind` | Four conventions that range over every kind | `null` means **no record**, never a default, and must render as absence · **at most one free-text field per kind**, and `course` has zero, which is a cap and not a quota · **every field is individually CRUD-able**, so landing performs partial update and never whole-record replacement · timestamps are ISO 8601, with `added_at` on `course` and `obligation` and `created_at`/`updated_at` on the annotation kinds. **The cap is only tractable because there is no catch-all `notes` field:** a negative definition cannot be non-overlapping. | `null -> no record. Never a default.` / `free text -> at most one field per kind. course: zero.` / `mutability -> field grain; landing = partial update` / `timestamps -> added_at on course, obligation; created_at + updated_at on annotations` | M43, and M63's argument (M63 remains a graveyard row) |
| `course-membership-is-a-field` | Course membership is a field, because the rule that relations are records exists to stop a polymorphic target becoming one | `obligation.course` is a `Ref` field on `obligation`, not an edge, and a property of `obligation` rather than of every node - a concept is not per-course. The rule that relations are records exists to stop a **polymorphic** target becoming a field, and this target is not polymorphic. **Whether the field is mutable is not ruled** - the code implements an application-tier recommendation that no record decides. | - | M44 |
| `a-date-without-a-time-is-2359` | A date without a time resolves to `23:59`, at the schema level and not at the parser's discretion | `due` is `Date \| DateTime`, nullable, and is the moment this obligation is anchored to - the deadline for something handed in, the start for a sitting. A `Date` resolves to **`23:59`** at read time and the stored value is always returned raw; a `DateTime` is a stated time and is never overwritten by that default. `T00:00` is the parser default and was what the system actually did, silently, in all 60 runs. | `due : Date \| DateTime \| null` / `Date -> 23:59 at read time; stored value returned raw` / `Date -> DateTime is ordinary field-grain CRUD` | M45 |
| `nullable-means-unknown-and-the-writer-defaults-it` | A nullable bool means unknown; the writer supplies the obvious default, not the schema | `optional` and `grade_share_conditional` are nullable bools where **null means unknown, never the negative** - a non-nullable bool forces the system to assert what no source stated. A separate **write rule** tells the writer to supply the obvious value where a person would not hesitate, which leaves a stored null meaning the writer genuinely could not tell. This is a rule about the writer, not about the field, and the schema is unchanged by it. | `schema: bool \| null, null = UNKNOWN` / `write rule: default it where the answer is obvious` / `=> a stored null means the writer could not tell` | M50, and M48's nullability half |
| `a-conditional-weight-gets-a-marker-not-a-model` | A conditional grade weight gets a marker, not a model, and the pointer to the rule is optional | `grade_share_conditional` is true when the stored share is one reading of a rule the course states conditionally or as a bound. The general form - a `weighting_scheme` naming the alternatives with a derived weight - was rejected as over-built for one concrete calculation, and the *required* pointer to the rule was later made optional because a schema rule manufacturing a conflict nobody would care about is a defect in the rule. **The narrowing must not be smoothed: the pointer was half of what made the marker actionable.** | - | M48's marker half |
| `parts-carries-recurring-concepts-not-size` | `parts` carries the concepts that recur, as canonical singular names, and does not carry size | `parts` carries the concepts an obligation's source carries, as raw strings and never as pointers to concept nodes. A part is **a concept worth capturing because it might occur elsewhere in the system**, and the writer writes the canonical singular name rather than the phrase the source used. It does not carry size: the replacement for the removed ordinal-size mechanism is not another field but an interaction - the agent sees the skeleton and ring 0, notices, and asks when needed. | `parts : [string]` - concepts, raw strings, never Refs. kept: `Graph` `Queue` `Big-O` `Linked List`. dropped: `Multiple Choice` `Problem Solving` (noise) · `Monte-Carlo` `A5Tree` (one-off, local) | M49 |
| `an-annotation-is-a-tag-not-a-type-hierarchy` | An annotation is a tag over two kinds, not a type hierarchy | `sticky_note` and `progress` are two kinds with one shape, distinguished by their `kind` value: both carry `origin`, both carry `created_at` and `updated_at`, and both reach their target through an `about` link rather than a field. A type hierarchy was the obvious move and is forbidden: a subtype that forbids what its parent permits is a Liskov violation, so the three differences become construction-time validation rules instead. | shared shape: `kind · id · origin · created_at · updated_at`; target is an `about` link, never a field | extracted from M51 + M57 |
| `progress-state-is-non-nullable` | `progress.state` is non-nullable and defaults to `not_started`, so the agent has no reason to ask | `state` is a non-nullable enum `not_started \| in_progress \| done` with **no unknown state**: an obligation with no progress record reads as `not_started`, because that is what a thing nobody has touched is. A nullable state is honest and was given up because it makes the system announce it does not know, which gives an agent a reason to ask *have you started this yet*. A **defined** default is not an invention; the measured incident recorded a run inventing a default where none was specified. | `state : not_started \| in_progress \| done` NOT nullable · `detail` illegal without a `state` (construction) · one current value per target (the service) · only the owner authors it (nowhere, deliberately) · **no `about` link is legal** and means progress on a free topic named in `detail` | M51 |
| `a-note-points-at-a-node-and-its-category-is-open` | A note is an entity that points at a node; `category` is an open string set on purpose, and provenance confers no immutability | A `sticky_note` is an entity that points at a node rather than a property of one, so attach, detach and modify are cheap and symmetric and **maintenance happens at the read**. `category` is an open string set, deliberately not an enumeration, because the cases cannot be enumerated - the price is that the field stores whatever it is given and its write rule is owed. `origin` records how the annotation came to exist and **does not confer immutability**: an annotation may be edited, and an edit carries `origin` forward by default. | `sticky_note := kind · id · category · body · origin · created_at · updated_at` / `category : string, OPEN SET, write rule OWED` / `body : the kind's ONE free-text field` | M57 |
| `the-graveyard` | The graveyard: removed fields, their reasons, and a standing rule against re-adding them | `schema.md §7` lists **sixteen** removals with the reason for each, under a standing rule: *deliberately absent - do not re-add without a new ruling; a later session reading an older document must not restore them.* **The rulings bind; the numbers do not.** Every count in the table is stated over the 22-row fixture or the two-course corpus, both superseded; a later reader must apply the removals and must never re-derive them from the arithmetic. | The 16-row table, with the corrections and additions set out in *The graveyard table* below | M62, and M52, M53, M54, M63 as rows |

### The observation contract

| slug | title | body | shape | absorbs |
|---|---|---|---|---|
| `ring-0-carries-seven-routing-fields` | Ring 0 carries seven routing fields; `parts` and `grade_share` are excluded, and `grade_share`'s exclusion is measured | Ring 0 carries `course`, `name`, `due`, `state`, `optional`, `done_by` and `has-more`; band B drops the last three. `parts` is out because it answers *what is this about* rather than *where do I look next*; `grade_share` is out because a rendered column of shares reads as a partition of the grade that it is not, which is the single largest measured faithfulness defect in the corpus. **Excluded from the projection is not unreadable**: ring 0 governs residency, and `parts` comes back with any read of the obligation record. | band A: `course` `name` `due` `state` `optional` `done_by` `has-more` · band B: `course` `name` `due` `state` · neither band: `parts` `grade_share` `grade_share_conditional` | M67 |
| `symmetry-not-shallowness` | The observation invariant is symmetry, not shallowness, and it is scoped to the set the judgment ranges over | Observe anything you can afford for every course at once; never observe anything you can only afford for one - the second case is `dispatch`'s entrance, and its result must come back in the same shape as the others. Asymmetry that comes from the material is legitimate; asymmetry from interaction history is not, because **asymmetric depth biases allocation and visible work masquerades as important work**. Symmetry is scoped to the set the judgment ranges over, not unconditionally to all five courses. | `observe(X) is permitted for a judgment over set S iff X is affordable for every member of S; else dispatch(X, member) -> a value in the same shape as every other member's` | M69, and A/M9's failure mode (b) as its rationale |
| `projection-order-comes-from-the-material` | The projection's order is derived from the material, never from write history | The projection groups by `course` by default and the grouping key is a parameter, because symmetry is scoped to the set the judgment ranges over. Within a group, order by `due` ascending, nulls last; among nulls by `done_by`; ties broken by the handle - **never by file order, because array order is insertion order is write history**. `due` is the primary key, not `min(due, done_by)`: triggering and ordering are different jobs. | - | M70 |
| `active-is-three-independent-triggers` | Active is three independent triggers on one question, not a time window with exceptions | An obligation is in band A if any one of three things holds; everything else, including obligations with no date, is band B. **Breadth is never treated as a defect:** a request for a whole semester that gets a whole semester is answering what was asked, and the useful window is a requirement Billy stated rather than a fix the system applies on his behalf. Two bands do not violate uniform depth, because the partition is computed from material facts plus one rule applied identically to every course. | `active := due ∈ [today-7d, today+14d] OR done_by ∈ [today-7d, today+14d] OR state == in_progress` | M71 + A/M3 |
| `expansions-are-discarded-never-sedimented` | What is fetched is dropped; depth never comes back into the conversation | Depth is added only inside ephemeral contexts and does not come back: what is fetched is rendered, used and dropped, never accumulated. Holding expansions saves refetches and loses anyway, because without discarding a long-running conversation converges on held-everything **plus** path-dependent bias - both costs, no benefit. The store boundary is the chokepoint for **content**; discard discipline is the chokepoint for **structure**. | In a long-running agent conversation the discard is **not** automatic - compaction is lossy and unpredictable, not a discipline - so the rule is a statement about what the conversation must not be asked to keep, enforced by the tool's return shape. | M72, and A/M9's failure mode (a) as its rationale |
| `the-coordinator-holds-ring-0-not-the-skeleton` | The coordinator holds ring 0 in its context and queries the skeleton on demand | The coordinator holds ring 0 in its conversation context and **queries** the skeleton on demand; it does not hold the skeleton. Its persistent memory holds pointers and summaries, never content, and the view refreshes as facts change but never deepens. **Ring 0 is resident for the coordinator and for nobody else** - depth is just enough to triage, never enough to work. | **Resident means held in the conversation's context.** The code process is per-invocation and its lifetime is not a deciding fact here; the conversation is long-running, days to weeks. Never write "the coordinator's lifetime" without saying which one. | M73 |
| `store-output-enters-only-as-a-conclusion` | Store output enters the coordinator only as a conclusion; the context that produced it is discarded, and who produced it is irrelevant | The invariant is a data-flow rule, not an agent topology: store output enters the coordinator only as a conclusion, the context that produced it is then discarded, and who produced it is irrelevant - a spawned subagent, a session Billy opens himself and a task session are all implementations. **The coordinator sees what a node IS; it never sees what a node SAYS.** Rendering a node's own summary is a skeleton read and is allowed. | *"No corpus retrieval, no file reads, no fact writes"* is a purity restriction **on materials**, not an enumeration of the coordinator's reads: `look_at(course)` is a call the coordinator makes, or plan generation is blind. | M75 |
| `the-coordinator-walks-edges-it-does-not-search` | The coordinator reaches material by walking a node's edges, never by searching the corpus | When the coordinator needs to know what a node is about, it follows that node's edges and reads its neighbours' definitions; it does not search the corpus. The verb returns no sections, no pages, no paragraph and no chunk even where the underlying data holds them - **the boundary is the tool surface, never self-restraint.** Where no edge exists the walk returns nothing, which is a true answer about the material. | The finding: **nothing was missing from the model** - the `obligation → artifact (spec)` edge already existed at ~53 instances across two courses; the operation was wrong. **The return shape is withdrawn, not decided** - see the presentation-surface deferral. | M76 |

### Inbound

| slug | title | body | shape | absorbs |
|---|---|---|---|---|
| `the-system-does-not-fetch` | The system does not fetch; the boundary starts at the endpoint, and the endpoint is multimodal | The system does not fetch anything. The user delivers material and the boundary starts at the endpoint, which moves the trust requirement from coverage of the world to **completeness of recall over what it was given**. Because delivery is a paste, the endpoint is multimodal from the first version, and it records the source's **publication** time and not its arrival time. | - | M81 |
| `inbound-arrives-to-be-known` | Inbound arrives to be known, not to trigger an action | Inbound does not arrive to trigger an action; it arrives to be known. The job is that when the user asks what a week was about, the system holds the surrounding context - not that it executes one operation per input, which is the model that had no correct branch for 55% of real announcements. The cost is taken knowingly: this is one step from a note pile, and the only thing keeping it a designed knowledge base is that the small typed layer stays populated. | - | M83, and M82's falsification as its ground |
| `two-conflicting-statements-never-coexist` | Two conflicting statements never coexist, and how a conflict closes depends on what is in conflict | Two conflicting statements never coexist in the system: landing detects a conflict instead of overwriting, and a conflict is closed at write time rather than left for a reader to reconcile. A shallow collision the agent may resolve itself, but it **must report the resolution afterwards** and never resolve transparently; a deeper one it must put to the user before resolving. The owner's own claim is not exempt - it is surfaced against the held record. | **shallow** (a due date · a room) → the agent resolves, then reports. Never silently. **deep** (an assignment's spec or requirements · a concept · an exam's time or place) → the agent asks before resolving. Requirement on the field set: depth is a property of what a statement collides with, so the discriminator lives on the record. | M85, and M82's counter-argument as its rejected alternative |
| `intake-is-ordered-and-cross-document` | Intake is ordered and cross-document; no artifact is understood alone | The governing artifact is ingested before the artifacts it governs, and no file is understood in isolation. The course outline is the only carrier of grade weights; assignment bodies carry markers that decode only against another document; deadlines hide in the prose of governing documents; and where every handout defers the date to the portal, the pasted portal screenshot is the **primary** deadline path rather than an enrichment of one. | Measured: a full multimodal pass over nine assignment PDFs yields an obligation layer with **zero deadlines** and no error. Extraction is **title-scoped, not full-text** - full-text finds mention, title-scoped finds coverage. | M88 |
| `the-course-site-is-not-a-source-of-truth` | The course site is not a source of truth; the system dates what it holds | The course site cannot be relied on to hold the corrected version, so the system dates what it holds and compares dates at the read rather than deferring to the source. Locally held material is provably stale in both measured courses, current handouts carry errors no announcement ever corrected, and material a year old circulates as current - so "the corrected version is on the portal" is not a mitigation and must not be written as one. | The comparison this rests on - a note's date against its target's revision date - **has no input until a kind carrying a revision date exists.** The hazard this corpus evidenced most heavily is currently unmitigated. | M89 |
| `store-inclusion-is-decided-by-the-store-not-the-file` | What enters the store is decided by what the store is for, not by file type and not by source class | An artifact's content enters the store if and only if it yields semantic, decontextualized facts about course materials that improve the knowledge base's overall quality - a handwritten note qualifies on that test. No source class is admitted or excluded as a class, and no property of the file - its type, or whether its meaning survives linearization - decides the question. **`text_extractable` survives as a materialization outcome, not as an inclusion criterion.** | `backing ∈ {materialized_doc, code_project}` - a node property · `text_extractable: bool, per region, default false` - true only when a pass actually recovered text | **M37 + M91** |
| `delivery-layout-is-not-organization` | Delivery layout is not organization; resolution is semantic | The portal's folder tree shows how files are distributed, not how knowledge is organized, and finding the better organization is why the system exists. A pasted intake screenshot therefore carries **provenance and not position**: a node's parent is resolved semantically and never by a path match. The user's own folders are admissible as evidence of the organization he reaches for under pressure, and never as the course's structure. | - | M92 |
| `an-asked-answer-is-kept-and-loud` | An asked answer is kept, and its provenance is loud | An answer the system asked for is stored, with its timestamp and its provenance, and the provenance is stated prominently at every read. The harm of a stale answer was never that it was recorded - it was that it went on influencing decisions invisibly - so the fix is to make the record loud rather than to drop or expire it. | The write rule for `origin` is owed, and the divergence is known: the schema's prose says *how the claim was obtained* and both extraction passes reached for *what document class it came from*. | M96 |

### The container

| slug | title | body | shape | absorbs |
|---|---|---|---|---|
| `three-tiers-enforced-by-a-boundary-test` | Three tiers, no rule about what deserves to exist below the surface, and a test that can refuse | The system is split presentation / application / persistence: the surface, the rendering and **every rule about what an agent should do** are presentation; the field set, the kinds, construction-time validation, id minting and CRUD at field grain are application; the serialized files and the adjacency index are persistence. The field set says what a *legal value* is; how to produce one, and whether a row should exist at all, live at the surface - which is why the agent never auto-adds and why matching two records is an interaction, not an algorithm. **A tier is designed against a tier that already exists**, and the boundary is directories plus a test that has been shown to fail, because an npm manifest cannot refuse - workspace dependencies hoist. | The three-row tier table. The four consequences, with the 2026-08-28 correction: consequence 1's absolute *"a write rule never refers to the source"* is **withdrawn** - three of five written rules do refer to a source, and the real distinction is the direction a rule is derived from. The boundary test's limits: relative specifiers only, `src/` not `tests/`. | **M97 + M98 + M105** |
| `one-composable-grammar-not-n-verbs` | One composable grammar with progressive disclosure, not N described verbs | What is rejected is a shape, not a protocol: N single-purpose verbs, each routed by its own description, measured as fragile - **rewording one docstring moved a verb's call count from 1 to 9 with data availability held constant**. What replaces it is one composable grammar with progressive disclosure. The distinction is independent of transport: a server exposing one tool whose argument is a command string has the same property, and a CLI with forty subcommands each needing `--help` has the old defect. | - | M100 |
| `addressing-belongs-to-the-surface` | Addressing belongs to the surface; every read returns handles | The surface may render a record however it likes and resolve at call time, the way a materialized view does; the `id` is opaque precisely so nothing at the surface has to mean anything to the layers below. **One constraint binds it: nothing constructs an id, so every read that returns records must return their handles** - a handle absent from the render makes the level below unreachable. | - | M101 |
| `the-skeleton-is-files-plus-an-index` | The skeleton is files plus an index rebuilt at load, not a database | The skeleton needs a durable serialization plus an adjacency index rebuilt at load; all three graph operations are scans over that index, and **the load is cheap enough that per-invocation and resident are indistinguishable** - 2c03's 138-node graph is 52 KB and parses in 0.27 ms. A graph engine would buy query planning for three hand-writable queries over ~2,200 edges. **The store is a different case and gets a different mechanism**: 62 MB of vectors should not be re-parsed per invocation. | Overturning conditions: the corpus growing an order of magnitude · multi-device sync becoming real · the skeleton growing far past ~640 nodes · **a second concurrent writer** (single-writer is now guaranteed by the subagent contract rather than by the container). | M103, and M114's live residue |
| `typescript-because-a-compiler-can-refuse` | TypeScript, because two of this design's own mechanisms need a compiler that can refuse | TypeScript, settled by what this design already claims about itself: the purity cut is defused *by type, not by restraint*, and construction is the only enforcement point there is - **both are claims about a compiler that can refuse.** Python cannot refuse, so trigger B's promise would be hoped for rather than checked. **The embedding ecosystem stays Python and does not cross a tier boundary**: the store couples to the skeleton through one field. | - | M104 |
| `jsonl-and-construction-is-the-only-gate` | JSONL with a `schema_version`, and construction is the only gate | The skeleton persists as `nodes.jsonl` + `links.jsonl`, each carrying a `schema_version` - JSONL enforces nothing and construction is the only gate, so without a version a stale file fails as an unexplained validation error. Vectors go to a **side binary store keyed by node id, never into the JSONL**. **A constructor sees one line**, so any rule ranging over more than one record - the id space, one-current-value-per-target, link identity - belongs to the services. | **The hole, which must travel:** construction is not currently part of the load. Measured - a store carrying `due: 'April 2026'` and a slice-2 `concept` node loaded without error and was rewritten intact. | M106 |
| `the-store-is-the-channel` | Components share state through the store, never through a protocol | There is no orchestrator and no control relationship, only a scope parameter: **the store is the channel.** Extraction writes and the coordinator sees it on its next read; a subagent returns a conclusion, never state. There is no queue, no ack and no cursor, because **there is no second party that might be asleep**. **One domain, not one per course** - what differs between courses is a working-instruction bundle that loads with the scope, not an agent. | - | M107, and M80's one surviving positive |
| `the-calendar-is-an-outside-projection` | The calendar is a projection to an outside surface, not something this system renders | Calendar rendering leaves this system and lands on a calendar surface Billy already uses: **one authority - the facts layer - and many views**, because a writable second surface reproduces the two-sources-of-truth pathology. The original ground (*"that removes the only human-facing rendering requirement from this repo"*) is false and was falsified within a week; the boundary stands on Billy's ruling instead - **calendar things belong on the calendar.** | - | M108 |
| `markdown-is-not-the-store` | Markdown notes are not the store | Manual markdown maintenance is out as the system of record: the information granularity is too fine and too time-sensitive for a `devlog/`-style discipline, and the failure mode is not that notes are wrong but that they are not updated on the day a deadline moves. **The store is typed and written by the system; markdown remains a fine medium for decisions about the system and a bad one for facts inside it.** | - | M110 |
| `build-the-instance-generalize-afterwards` | Build the instance; the general contract is whatever survives generalization | The instance comes first and forces the template: this design **is** the general work, and the contract is whatever survives generalization afterwards, not something derived up front. Do not clone outward from existing instances. The same posture applies inside the system, wherever a second case is tempting before the first one renders. | - | M113 |

### One ADR with no proposer

| slug | title | body | shape | absorbs |
|---|---|---|---|---|
| `the-five-refactor-triggers` | Five named rewrites, and exactly enough committed now to defuse each | The question was answered by naming what would *force* a rewrite when the graph layers land, and committing to exactly enough to defuse each; everything else stays unbuilt. The rejected alternative was to defer all five and refactor later, and it loses because a forced rewrite costs more than five minimal commitments. **Four of the five are argued at length elsewhere and this ADR is where they are named together; the fifth is argued nowhere else.** | A - identity → one id space for anything that can be an endpoint · B - dispatch on type → `kind` is data with a typed payload, never control flow · C - linkage → relations are records, not fields · D - the store boundary → the purity cut is a property of the interface's shape, not of restraint · **E - persistence coupling → a repository interface with one implementation** | trigger E, which no cluster claimed. A-D cite their own ADRs. |

### The graveyard table

The `the-graveyard` ADR carries the table. **Sixteen rows at source, not fifteen** (dispute 7). Fifteen carried as removals, one carried as a marked deferral, four added, five re-reasoned or flagged.

| # | row | disposition |
|---|---|---|
| 1 | `workload` / `hours_estimate` | Carry. Billy-ruled 08-23, verbatim, with the ordinal-size replacement and the adversarial correction (*asking is only a remedy for a quantity the user can answer*). Reaffirmed by ruling 2. **All three names ride in the row** so a later reader recognises the field. |
| 2 | `status.completion` · `files` · `score` · `evaluation` | Carry. The *moots-not-contradicts* clause is the row's whole value. |
| 3 | `count{done, of}` | Carry, **re-reasoned**. Drop "one instance in 22" - it quotes a count this row invalidated. |
| 4 | `stated_in` / `source_ref` | Carry, **flagged**. The only row whose why-column is bare; the no-re-add rule binds it and nothing says why. |
| 5 | `obligation.notes` | Carry. The non-overlap rule; a negative definition cannot be non-overlapping. Cross-reference `four-conventions-over-every-kind`. |
| 6 | release dates | Carry. |
| 7 | per-part weights and per-part scores | Carry. |
| 8 | coarse dates (*"April 2026"*) | Carry, **flagged**. Both readings are defensible and the extraction went the other way; the ruling stands. |
| 9 | recurring / countable obligations | Carry, **re-reasoned**. The `n=1` is no longer n=1 - three further instances exist. The ruling stands under the no-re-add rule; the n=1 must not be restated. See `Needs Billy`. |
| 10 | `status.evaluation` | Carry. The strongest-reasoned row in the table. |
| 11 | `course.offering_term` · `course.prereq` | Carry, **re-reasoned - the row that most needs it**. Both stated reasons fail: "null for both courses" is falsified at source, and "a domain that does not exist" is a container fact. Ruling 1 supplies the replacement: out for v1 because v1's boundary is coursework, deferred to v2. |
| 12 | `course.manifest` | Carry. A measurement that still holds. |
| 13 | `course` free-text field | Carry, **re-reasoned**. "Nothing identifiable would go in it" is too strong - instructor, term boundaries, units, antirequisites and textbook do go in it. The ruling routes them to annotations; the reason as written does not. |
| 14 | `term_start` | Carry, **flagged as the row most likely to need re-opening**. Its whole reason is a count over the dead fixture, and term boundaries are load-bearing for the last-day-of-classes rule. |
| 15 | `due_precision` as a separate flag | Carry. Clean and self-evidencing. |
| 16 | `time_point` | **Carry the row, re-labelled** (dispute 7). It is a deferral, not a removal - its own text says so - so the row states that the no-re-add rule does not bind it and points at the time-projection deferral. Not removed from the table: the graveyard is a standing anti-regression device and thinning it is the move it exists to prevent. |
| +1 | `present` · `external_ref` · `backing: referenced_only` | **Add.** Billy `[R]`. Cross-reference `artifact-existence-is-not-a-field`. |
| +2 | `supersedes` (link kind) | **Add.** Cross-reference `no-supersedes-link`. |
| +3 | `weighting_scheme` | **Add.** Cross-reference `a-conditional-weight-gets-a-marker-not-a-model`. |
| +4 | the `<course_id>-slug(name)` id scheme | **Add.** A killed scheme rather than a field, and the regression this corpus is likeliest to make. |

**Two input corrections that must not be re-inherited:** the table has sixteen rows, not fifteen; and the derived figure *"thirteen of fifteen carry no changelog line"* is over the wrong denominator and should be dropped rather than restated.

---

## Merges performed

Six merges survived the shared-trade-off test. Two splits and one creation accompany them.

| # | merged | shared trade-off, in one line |
|---|---|---|
| 1 | **A/M3 → D/M71** (`active-is-three-independent-triggers`) | One decision: the ±1-2 week window was available as a default narrowing from 08-23 and deliberately not applied until Billy stated it as a requirement, and `in_progress` was promoted from an exception inside the window to a trigger of its own - the rejected alternative in both is *a time window carrying exceptions, applied as a helpful narrowing*. |
| 2 | **B/M37 + E/M91** (`store-inclusion-is-decided-by-the-store-not-the-file`) | One decision: ruling 6 rejects the same two alternatives for the same reason - the source-class rule and the linearization axis both make inclusion a property of the artifact, and the store's nature is the axis neither considered. |
| 3 | **F/M97 + F/M98 + F/M105** (`three-tiers-enforced-by-a-boundary-test`) | One decision: rules about what an agent should do and what deserves to exist may not live below the surface, because **the enforcement point does not exist there** - a constructor sees one line, JSONL enforces nothing, and an npm manifest cannot refuse. The ownership line, its four consequences and the boundary test are one trade-off stated at three grains. |
| 4 | **C/M48's nullability half + C/M50** (`nullable-means-unknown-and-the-writer-defaults-it`) | One ruling on one date over two fields: a non-nullable bool forces the system to assert what no source stated, so both fields are nullable and a write rule supplies the obvious default instead. Same rejected alternative, same reason, one 08-27 ruling. |
| 5 | **C/M51 + C/M57 → an extracted third ADR** (`an-annotation-is-a-tag-not-a-type-hierarchy`) | The shared shape both kinds carry is one decision with one rejected alternative - a type hierarchy - rejected for one reason: a subtype forbidding what its parent permits is a Liskov violation, so the differences become construction-time validation rules. |
| 6 | **B/M63's argument → C/M43** (`four-conventions-over-every-kind`) | The one-free-text-field cap and the removal of `obligation.notes` are one argument from two ends: the cap is nominal unless there is no catch-all field, because a negative definition cannot be non-overlapping. M63 remains a graveyard row; only its argument moves. |

**Two splits.** Both are cases where a cluster bundled two trade-offs, and the merge test forced them apart:

- **C/M48 splits.** Its nullability half merges into #4; its **marker-not-a-model** half becomes `a-conditional-weight-gets-a-marker-not-a-model`, because that decision's rejected alternative is `weighting_scheme` and its reason is *over-built for one concrete calculation* - neither shared with the nullability ruling.
- **C/M51 + C/M57 split three ways.** The shared annotation shape becomes #5; `progress.state`'s non-nullability keeps its own ADR (rejected: a nullable state; reason: it gives an agent a reason to ask); `sticky_note`'s open `category` and non-immutable provenance keep theirs.

**One creation.** `the-five-refactor-triggers`. `design.md §2` names five commitments made in one act to defuse five named rewrites - one rejected alternative (defer all five), one reason (a forced rewrite costs more). Four are argued elsewhere and cite this ADR. **The fifth, trigger E (a repository interface with one implementation), is argued nowhere and is claimed by no cluster**; without this ADR it is lost. This resolves dispute 9.

**One re-homing.** F/M112 leaves `docs/adr/` - see dispute 10.

**Clause de-duplications** (not merges; one statement, several citations):

- *"Filename similarity implies nothing"* - stated once in `one-lecture-is-one-node-with-a-file-list` (where it was measured, with the Jaccard 0.21 collision); cited by `no-supersedes-link` and `delivery-layout-is-not-organization`.
- *"Surface for confirmation, never resolve"* - appears in four things across three clusters. Stated once in `progress-state-is-non-nullable`'s shape (the authorship rule); cited by `modelling-layer-is-stateless` and the trust-contract deferral. **It is an authorship rule, not a conflict rule**: `two-conflicting-statements-never-coexist` does not license an agent to resolve a progress claim.
- *"One level deeper is one more call"* - stated once in `expansion-cost-is-the-size-gate`; `one-composable-grammar-not-n-verbs` cites it rather than restating the gate.
- *"One id space"* - stated once in `ids-are-opaque-assigned-and-never-constructed` (dispute 1); cited by `a-ref-is-not-a-foreign-key` and `the-five-refactor-triggers`.
- *"The coordinator sees what a node IS; it never sees what a node SAYS"* - moved from B/M33 into `store-output-enters-only-as-a-conclusion`, per D's accepted split.
- **The enforcement taxonomy** (construction / the service / nowhere) - stated once in `jsonl-and-construction-is-the-only-gate`; `progress-state-is-non-nullable` carries the three progress rules and cites the taxonomy.
- **A/M9's two failure modes** ride as one-clause rationales inside `symmetry-not-shallowness` (b) and `expansions-are-discarded-never-sedimented` (a). A's drop was conditional on exactly this and the condition is met.

---

## Merges rejected

Every merge a cluster proposed or entertained that failed the test, and which test it failed. **Sharing a subject, a field, a record or a section of one file does not count.**

| proposed merge | failed on |
|---|---|
| **C/M40 + C/M41** (ids) - C called it "the strongest merge pair in my cluster" | **Different rejected alternatives.** M40 rejects a derived `<course_id>-slug(name)` scheme because constructing an id is a bet on spelling; M41 rejects *uniform* opacity because inventing an identifier where the source issues a canonical one adds a mapping nobody needs. They sit in one section of `schema.md §1.1`, which is a record, not a trade-off. |
| **C/M40 + F/M101** - F called M101 "the other half of the opaque id" | **Different trade-offs.** M40 decides how an id is formed; M101 decides where addressing lives (surface, not schema). The clause they share - *every read returns handles* - is stated once in M40 and cited by M101. |
| **B/M25 + C/M44** (relations are records / course membership is a field) | **Different rejected alternatives.** M25 rejects inferring relations at read time; M44 rejects a typed edge for course membership. The rule and its declared boundary, cross-referenced in both bodies so neither reads as an inconsistency. |
| **B/M25 + C/M42 + the triggers** - both B and C suspected the five triggers should be one ADR | **Partially upheld** (dispute 9). The triggers ADR is created and names all five, but does not absorb M25, M42, M40 or M33: each has its own rejected alternative argued at length in a different record. Merging them would produce an ADR that can state none of the four real reasons. |
| **B/M23 + B/M24** (`supersedes` cut / announcement cut) | **The brief's own calibration case.** Both cut an edge - a shared subject. One was cut on five agents, two courses, zero instances; the other because a proposition about announcements was falsified in both courses. Different evidence, different reasoning. |
| **B/M17 + E/M92** (layered graph / folder tree) - B proposed one ruling with two consequences | **Different reasons** (dispute 4). M17's is *a course's knowledge does not nest*; M92's is *distribution is not organization*. Settled in E's favour, with the pairing corrected: M92's sibling is the announcements-as-channel family. |
| **A/M8 + B/M23** (sync is the wrong model / `supersedes`) - A suspected one ADR | **Different rejected alternatives.** M8 rejects sync, diffing and mirror state because there is no correspondence to maintain; M23 rejects a link kind on zero measured instances. |
| **A/M6 + D/M73** (the size gate / what is held resident) | **Different trade-offs**, and both clusters agreed. A owns which quantity is budgeted; D owns what is held versus queried. |
| **D/M72 + D/M73** - D called it "the strongest merge candidate in the cluster" | **Different rejected alternatives**, though the same underlying hazard. M72 rejects keeping expansions (which saves refetches); M73 rejects holding the whole skeleton (no fetch latency). The rule requires both halves to match; a shared reason is not enough. |
| **D/M69 + D/M70**, **D/M70 + D/M71** | **Different trade-offs**; both flagged and neither proposed. M69 decides what a judgment may observe, M70 what order things come back in, M71 what counts as active. |
| **D/M67 + C/M47** (`grade_share` excluded / `grade_share` exempt) | **Different trade-offs on one field.** D's exclusion is measured (38% of faithfulness failures); C's exemption is from the rigidity rule on *no reader*. Both must exist and each cites the other. |
| **F/M104 + F/M105** (TypeScript / packaging) | **Different rejected alternatives** - a language versus a packaging mechanism - even though the reason is verbally identical (*it cannot refuse*). M105 was instead absorbed into the tier ADR, where it is the enforcement clause for a boundary that ADR asserts. |
| **E/M85 + E/M96** (conflict policy / an asked answer persists) | **Different rejected alternatives.** M85 rejects store-and-tag with read-time reconciliation; M96 rejects not persisting and rejects expiring. The shared principle - *the system may act, and may store, but never invisibly* - is named in one line in both. |
| **E/M83 + E/M92** | **Different rejected alternatives** (the operations model / the folder tree). Cross-referenced on the shared *delivery scaffolding is not knowledge* principle. |
| **E's "five extraction rules in four clusters"** | **Not one trade-off** - five different rejected alternatives. The concern is discoverability, not ADR structure. Two of the five (title-scoped extraction, canonical singular names) already ride inside other ADRs; the natural single home for the set is a write-rules record, which the `write rule` term already names. |
| **E/M86 + E/M90** (retention / the correction seam) | **Not one wake-up condition.** Each has two independent triggers, sharing one. Merging produces an issue that wakes on four things, which defeats the point of a wake-up condition. |
| **B/M21 + E/M87 + F/M102** - E argued "shared precondition, not a merge, since the four hypotheses are unrelated" | **Overruled - these merge.** The deferral rule is one wake-up condition, and they have one. See the deferral set. |

---

## The deferral set

17 issues over 26 things. Every issue carries its wake-up condition; a deferral without one would have been moved.

### 1. Asking - unprompted speech, confirmation, and asking at the read

**Absorbs A/M7, E/M84, E/M95.** Three faces of one question.
**Wake-up:** the system is roughly built - skeleton and ring 0 behind an exposed surface, so interaction rounds can be run - and **ask-frequency has been measured over real rounds**. Ruling 2 states the interpretation: if the agent must ask constantly, either something needs persisting or the design has a seam, and either finding is a design change rather than a tuning.
**Three acceptance items:** unprompted speech and its frequency · confirmation before a write · asking at the read for a fact with no generating event.
**Must travel:** the corpus holds two of Billy's own positions in tension (*no proactivity, Billy's own urge to check is the scheduler* against *让系统从 waiting for input 变为 asking for input*) and ruling 4 declines to pick today. The **shape** of an ask is settled even though its frequency is not - a confirmation presents the resolved target (*"changing assignment 3's due from Wed to Fri"*), never a yes/no, because the hard part of a rewrite is resolving the target. The old **stratification axis died with the operations model**; ruling 7 restratifies by conflict depth, and nothing should carry the filing/rewriting split forward. The **third class is real**: a deadline is generated when the professor posts it, a progress state is generated by nothing, so forgetting to supply it is structural rather than a lapse. The **governor** is *only ask what changes a decision*, and the gate that decides what belongs in the observation space is the same gate. **`progress.state`'s default is settled and is not re-opened by this issue.**
**Dropped inside:** `/wrap` as a ritual (old container; its diagnosis survives - *it was never a problem with the ritual, it was a problem with the material*) · the dev-time confirmation toggle and its N=5 exit (self-declared arbitrary) · every confirmation count (~30, ~115, 1-2 per course), which measure a rewrite regime that no longer exists.

### 2. Instrument readiness - the hypotheses that cannot be tested yet

**Absorbs B/M21 (H1), E/M87 (H3), F/M102 (the acceptance criterion), and A/M2's untested-recall residue.**
**Wake-up:** **the instrument can reflect the ideal case** - concretely, write rules have landed, prompt and docstring work has landed, ring 0 and the skeleton have an exposed surface with product-facing verb names, and rendering exists, so an end-to-end run is runnable on real material. Ruling 9 states it and rejects the cheap escape hatch: reading a further course for structure only, producing no records, is refused, because when the instrument cannot reflect the ideal case its result is untrustworthy.
**Four acceptance items, each with its own additional precondition:**
- **H1** - is course type per-layer *density* rather than *structure*? Falsifier: read a course of a different shape and ask whether it needs a node kind or link kind the current set lacks.
- **H3** - can a multimodal pass find a partition a course does not state? Additional precondition: **a course whose material does not state its own outline is in the corpus.** Both measured courses state theirs, so the PASS measures the courses and not the pass - the agents' own words: *"the partition is not induced, it is transcribed."* Second, independent reason the result is uninformative, from no record: H3 was scored against a ground truth built from Billy's own folder renames and study guide, so it is a pass against *Billy's* partition and must never be reported as a pass against the course's.
- **Extracting the remaining courses.** Every contested field needs a write rule; a write rule is derived from what a value must be for a node to render well; the render does not exist. **Reading three more courses without those rules produces three more courses of noise and does not produce the rules.**
- **The recall half of faithfulness.** The 08-23 measurement (60 runs, zero omissions) was taken at a scale where omission was not possible; the recall side was never loaded.
**Must travel:** the live acceptance criterion is **one course's real obligations, landed through the write operations and read back**, and the number is **14 for 2c03, not 22** - the 22 included a row the graveyard forbids, so 22 is not reachable by re-running the old route. **H3's stated fallback**: if structure extraction fails, retrieval falls back to whole-document plus course/week metadata, which costs precision and changes nothing structural.

### 3. The presentation surface

**Absorbs C/M59 (the length bound), C/M61 (`has-more`'s shape), D/M77 (the `question` parameter), F/M99 (the migration list), plus open riders from C/M45, B/M14 + C/M55, and D/M76.** This is the largest merge in the pass, and the corpus already bundled five of its items as one cycle's mandate whose product record does not exist on disk.
**Wake-up:** **a surface exists with named product-facing verbs and written descriptions.** Ruling 9 states the gate: write rules have not landed, prompt and docstring work has not landed, ring 0 and the skeleton have no exposed surface, and the verb names are undecided and *"obviously cannot be `ring 0` and `skeleton`"*.
**Eight acceptance items:**
1. **The render's naming** - `label` or `summary` for the one-line-per-item render. Presentation's first decision. Neither the `summary` nor the `name` term closes it.
2. **Which layer applies `due`'s `23:59` resolution.** One line; a defensible default exists, so it is not a gate.
3. **`has-more`'s shape** - boolean, count, or set of present link kinds. Its meaning is settled and its motivation is measured (6 of 14 obligations carry an annotation, 8 carry none). **Re-measure rather than re-cite: the counts were wrong once already** (5 and 9, corrected to 6 and 14).
4. **`look_at`'s return shape**, and where a node's own typed fields arrive. Both stated triples are withdrawn; reading one as complete is what made `obligation.parts` look homeless, with a demonstrated cost.
5. **The `question` parameter and its retirement shape.** The ruling is durable and must not be lost - Billy 08-23: *"预期猜测这个问题，不如 dev 模式让它调用的时候问出这个问题"* - the question is stated at call time, not predicted, and the parameter is **required so it is enforced at the tool surface rather than requested in a prompt**. It gains force in an agent container, where a tool signature is what the harness enforces. Two honesty caveats travel: it **perturbs what it measures**, and it doubles as a test of read-time filtering. **The retirement condition is Billy's; the ≥80% threshold is an agent proposal explicitly flagged as arbitrary and does not survive** - what survives is *retire it when it stops surfacing new question kinds*.
6. **The length bound on free text entering the resident skeleton**, over **two** routes: `sticky_note.body` and the ingest-written summary. The bound is issued **down from affordability** - what the coordinator can pull for five courses at once, and whether the real policy statements survive that budget - not from a number chosen in advance. Its qualitative half is **the render test**, and it is the bound `symmetry-not-shallowness` names as owed.
7. **`land()`'s and the read operations' descriptions.**
8. **The verb-routing and screenshot-extraction evaluations**, both re-homed to presentation.
**The issue's first action item, and it is not optional.** **Billy ruled on 2026-08-29 that the corpus cannot justify a length bound, and the ruling has not reached the record it invalidates.** The `records.json` note bodies are a subagent's own compressions produced with no write rule to follow, and the file is agent output partly overwritten by Billy with nothing saying which body is which. The line drawn: **the corpus is evidence about what the material contains; it is not evidence about what a record should look like.** `model.md §10.5`'s `MEASURED 2026-08-28` banner rests entirely on the withdrawn numbers and **still stands uncorrected at source.** Every character count is void - 87-278, 871, 1,010, 459. **Placement facts survive** (4 notes on the course, 7 on obligations; 6 of 14 carrying an annotation), which is why item 3's motivation is intact where item 6's number is not.
**Dropped inside:** *"the MCP adapter is at most an adapter over the CLI's grammar and may never be built"* - it depended on a human-operated CLI beneath an agent protocol, and there is no longer anything to demote from. The replacement is not "build MCP" but the grammar ruling unchanged: the grammar is the early and expensive decision, transport is late and cheap.

### 4. The time projection

**Absorbs C/M60 part 1 (`time_point`), B/M36's flagged companion deferral, and F/M108's flagged calendar-surface question.**
**Wake-up:** **the schema, the API and the CLI shape have settled**, and then it gets its own design sitting (ruling 3).
**Must travel:** `time_point` is a kind for a moment that is not an obligation - an exam sitting, a review session, a conference are three real instances - and it is separate from `obligation` because **only obligations consume the weekly hours**. It is out because its reader, the calendar projection, is out, **not because nothing reads it**, and its graveyard row says so in exactly those words. The unresolved sub-question **which outside calendar surface, and whether the projection is ever built** rides here rather than becoming its own issue. A live instance exists: a conference currently carries an obligation row *"only because that is the only row-bearing kind available."*

### 5. The plan

**Absorbs D/M75b and C/M60 part 2.** Both clusters wrote the wake-up to merge, deliberately and in the same words.
**Wake-up:** **schema, API and CLI shape settle**, then the plan gets its own grilling session. Ruling 3: it is a real requirement but is not settleable now.
**Must travel:** `domain-design.md §9.1` ruled the projection carries **obligations · time-points · the current plan**, and §9.3 names plan generation the coordinator's **only substantive work, because it *is* coordination**. **The plan has no representation anywhere in the corpus** and `ring-0.md §7` says so and declines to invent one. **Two of the three named entities are missing and one of them is the system's only output** - and a retraction still standing in the domain corpus rests on that three-entity list, so nobody should later read the equation as evidence that all three exist. The corpus has exactly one template for what an output must look like: *a value in the same shape as the other four*. Ruling 2 bears on it: if size is judged from progress and load rather than stored, the plan is where that judgment gets written down, or nowhere.
**This deferral is a different kind from `time_point`'s:** `time_point`'s reader is out; the plan's requirement is real and undesigned.

### 6. The v2 cross-domain surface

**Absorbs C/M64 and F/M109.** Both clusters used the same wake-up wording deliberately, and F flagged that divergent wordings would be a reconciliation defect.
**Wake-up:** **v2, after the system proves useful and genuinely extensible** (ruling 1). v1's boundary is coursework inside academics, so there is no cross-domain surface for offering-term, prereq or an obligation to project into. It wakes when a cross-domain requirement re-enters.
**Must travel:** the requirement is **not dead**. `domain-design.md §0.6` asks that the academic domain hold **course offering-terms and prerequisite structure**, because that graph gates other domains' decisions - the instance is that winter-only mandatory courses ruled out a winter-27 co-op and thereby set the entire recruiting target to summer 27, and no system held that fact because no home existed for a constraint spanning academics and career. §0.6 is the strongest statement in the corpus that this is not a deadline tracker. Also: **an obligation is not a todo** - todos are flat and cross-domain, carry no course, no source and no externally-driven status transitions. The shape of the eventual answer is already stated: **the academic layer is authoritative, the cross-domain surface is a view.** **The PA database itself does not travel** - it is a system in the old container, and the deferral is about whatever cross-domain surface exists at v2.

### 7. What must be in the agent's context before it decides anything

**D/M68, the membership test. Attach to the existing issue #7 - do not open a second ticket.**
**Wake-up:** issue #8 lands - the by-hand observation, waiting on the first real decision of the fall 2026 semester. As of 2026-08-29 there are none.
**Must travel:** **the test may already be written** - *an observation earns its place iff a judgment demonstrably changes when it is present* - but it is marked an agent formulation, obtained by lifting the rigidity rule one level, **not separately ruled**. **The competing test is also unruled**: *a field belongs in ring 0 iff, without it, the coordinator cannot decide where to look next* is agent-drafted per its own changelog and declines the first. Both are agent formulations and neither is ruled; that is the merge finding neither survey could make and it is why this defers. **The null result stays refused on two independent grounds**: the runs were memoryless cold starts against a long-running conversation, and the fixture is written to a dead schema with three of its six launch-shaped values synthesized rather than observed. **Anti-merge, honoured:** the rigidity rule is a *different* test - it asks whether a field exists at all, this asks whether an existing field must be in the window. Ruling 2 names what the answer will be tested against: ask-frequency.

### 8. The surviving hub

**B/M28.**
**Wake-up:** the first time an artifact is ingested and `covers` gets a writer - concretely, **when a single artifact's extraction would produce `covers` edges to more than about half the concepts in a course.** A narrower and later trigger than the concept-layer deferral's, which is why it is separate.
**Must travel:** a review deck covers 26 of 26 concepts and the textbook covers all of them, and their honest relation is *"indexes the whole course"*, not N peer `covers` edges. **Dropped alongside:** the H2 gate itself (*is expansion cost bounded*) - it was invalid as posed, three agents returned three verdicts and the synthesis picked a fourth, and the record says it measured our own choices rather than the material.

### 9. Whether `produced` splits off `spec`

**B/M29.**
**Wake-up:** the first read that must distinguish what was *given to you* from what you *handed in* on the same obligation - the named query is *"show me what I handed in for A8"*. If that query can be served by filtering `spec` on `role`, the split does not happen; if serving it needs a second traversal or a special case, it does.
**Must travel:** the derivation's own synthesis **misreported its agent**, claiming one concluded a role attribute suffices when it concluded the opposite, and a later record restored the actual position without noticing it was correcting anything. One line in the issue so the misreport is not re-inherited.

### 10. Where the vector index attaches

**B/M35.**
**Wake-up:** the first time a text query must route to a node without a handle - i.e. when the store is built and by-query is implemented. At that point the cost of two embedding sets kept in step is payable or not.
**Must travel:** **per-course buckets and a concept-layer entry point are not in conflict**, which no record says - a bucket is a partition of the index, an entry point is a routing decision. Without that sentence it will be re-litigated as a conflict. Ruling 6 constrains without settling: if the store holds semantic decontextualized facts, what is embedded is fact-grain, which leans the answer without deciding between one set and two.
**Dropped inside:** pgvector 0.8.0, HNSW, PostgreSQL 17.6 and the managed instance are properties of a database the old container owned. What survives is the probe's **finding shape** - an embedded vector store is available and cheap at this scale - not the stack.

### 11. The materialization pass

**Absorbs C/M56, and the pipeline half E/M91 could not settle.**
**Wake-up:** **the `artifact` kind acquires a writer** - an ingest pass exists that produces candidate fields. Before anything writes `tags`, the enum set has to be settled or declared open, and that is the first decision the pass forces.
**Must travel:** what a pass writes and which reader each part serves - `summary` (read by the coordinator) · `tags` (implies an enum set, deliberately not settled) · `sections + pages` (explicitly not the coordinator's responsibility). Plus the three questions ruling 6 does **not** settle: **pass granularity, whether page images are kept, and math-equation chunking** (deferred at the outset as a known industry problem). What is settled and must not be re-litigated: *§5 ruled out a **manual** taxonomy, not an LLM pass at ingest* - since a multimodal pass must run anyway for scans, `.docx` and `.pptx`, section labels are its byproduct.
**Does not travel:** P2's extraction figures (39/40 slide-shaped, 12/26 prose-shaped). They measure an apparatus, the record discounts them from two directions, and the honest verdict is *the cheap method fails on prose*, not *prose extraction fails*.

### 12. A shape for returned conclusions

**D/M78.**
**Wake-up:** **a caller exists** - either the presentation tier gets a confirmation surface, or the plan gets designed. `land()`'s signature is determined by the caller above it, and that caller does not exist.
**Must travel:** *emit only conclusions* is a promise, not a mechanism, until the return value has a required form; the template is *a value in the same shape as the other four*. It was **extended to the user, ruled**: asking Billy is dispatch with the user as target, and the return contract is unchanged, so the shape must work for a human answer as well as a subagent's. **One instance exists and no survey connected it to the owed item**: `land(candidates) -> Diff`, outcomes *created · updated · unchanged · CONFLICT*, and `Diff` is the only typed return contract in the corpus. **Ruling 7 gives CONFLICT a branch it did not have** - *resolved-and-reported* versus *asked-first* - so `Diff` is not a one-shape return. **One ruling, two consequences:** the conflict ADR owns the write policy, this issue owns the return type that carries the answer back, and ruling 7 must not land in two records with two vocabularies.

### 13. The trust contract for generated content

**D/M79.**
**Wake-up, a conjunction:** **`concept` exists** (the motivating case is a proposed concept partition, and nothing generates one yet) **and H3 is exercised** - because where a course states its own outline the concept layer is extraction rather than inference, which correspondingly narrows what the contract has to cover.
**Must travel:** the trust clause covers **completeness of recall over what Billy told it** and **does not cover content the system generates**. The agent's unruled position: the system proposes a partition, Billy disposes, and a wrong proposal must be cheap - it degrades grouping, never destroys anything. **It already has a concrete reader**: `text_extractable`'s reading mechanism *is* this contract - distinguishing a **quotation** from a **generated description** - so this is a live field whose semantics are undefined until the contract lands. That is the strongest reason not to drop the item. **The contract governs the materialized summary and never the node `summary`**; write that boundary in so the word collision does not reappear inside the issue.

### 14. Retention of raw inbound

**E/M86.**
**Wake-up:** ruling 5 - wait until the mechanism bites. Concretely, either **a discarded correction is observed to have left the corpus quietly wrong**, or **the class of source ruling 5 names enters the system**: Billy's own products - a running assignment, sources for work in progress, leftovers from an engineering project. Ruling 5 says that class is not in the system yet.
**Must travel:** **the asymmetry, which nothing has answered** - wrongly discarding a correction leaves the corpus quietly wrong, while wrongly attaching one costs a little noise, so a misjudgment costs retrieval reach, not data. Both later rulings that cut against retention (*never auto-add*, *the render test*) are about making a row or a note and neither touches whether the text is kept. **The reconciliation nobody has performed**, carried as the leading candidate rather than as a ruling: retain the *text* against the course, do not make a *row* or a *note*. **Ruling 6 shrinks this deferral**: raw announcement text mostly is not semantic decontextualized fact - one course reproduces a stale copy-paste three weeks later, which indexed announcement text would return as current - so the store-side answer is a fairly firm no, and what remains open is only whether it is kept somewhere that is not the store.

### 15. The correction seam

**E/M90.**
**Wake-up:** ruling 5's posture, with two triggers - **Billy's own products enter the system**, or **the instance count grows past twelve** (which sits behind the same extraction block as issue 2).
**Must travel: the four origins, because two appear in no record and will otherwise be lost.** (1) A correction arrives as an announcement - designed for. (2) The user states one - designed for. (3) **The corpus disagrees with itself** - two held documents contradict each other, nothing was delivered, and the conflict is inert until someone reads both in one sitting. Its own author recorded it as *"the one nothing in MODEL detects"* and declined to propose a mechanism. (4) **The author shipped the correction inside the artifact** - a caveat that a tutorial targets an older library version; two of one course's five real notes are this, so a sticky note is not only an inbound-correction mechanism.
**What ruling 7 changes, and it is the sharpest content here:** origin 3 is two conflicting statements in **source material**, which ruling 7 does not reach - but **the moment both sides are extracted they are two conflicting statements in the system**, which ruling 7 forbids. So ruling 7 converts origin 3 from an undetected nice-to-have into a **write-time obligation on any intake that reads both documents**, and detecting it at write time is precisely what nothing does. **Ruling 5 is the counterweight**: ruling 7 constrains what happens when a conflict is met and does **not** authorise a corpus-wide contradiction hunter, which is exactly the mechanism ruling 5 predicts will ask repeatedly and persist noise.

### 16. The concept layer - where its edges come from, and how they are refined

**Absorbs E/M93 and E/M94.** E recommended the merge; the wake-up is one.
**Wake-up:** **the `concept` kind exists and something writes into it.**
**Two acceptance items:** where concept nodes and cross-layer edges come from and who draws them (M93) · the refinement operations - split, merge, rename - and what they do to identity and to existing links (M94). Origin and refinement are two faces of one question, separated in the corpus only because they sit in different items of one owed list.
**Must travel:** **not at setup** - at setup the user does not yet know the concept structure, he knows it at the end. **But "not at setup" is not "not by Billy":** he authors concept edges by hand, unprompted, mid-semester - the measured instance is ink over a tutorial exercise naming three concepts, at fragment grain, on a page with no text layer, in a form the system can never read. **Nothing in any record designs for this origin, and it is the origin most likely to be right.** **Edges are authored in bulk from single sentences** - one clause creates 9 prerequisite edges, one slide creates 26 - so the assumption that cross-layer edges are drawn item by item is false, and the corollary is a hazard: an edge is only as current as its sentence, and that sentence's document may be a year old. **Refining concepts is not the falsified operations model returning** - that model was external inbound destructively rewriting a held fact, irreversible, author not the reader; this is the owner refining his own model, lossless and reversible. Without this sentence the operations-model drop will be read as forbidding refinement. **The deferral is narrower than it looks**: admission and granularity are already ruled - see dispute 8.

### 17. Preferences

**F/M111.**
**Wake-up:** **a mechanism reads a preference** - the rigidity rule applied to its own case. Concretely: when scope loading actually loads a per-course working-instruction bundle, the thing it loads needs a home.
**Two things to re-check when it wakes, and not assume:** the analogy it rests on has **broken** - *"structurally identical to `progress`"* was written when `progress` was a fact type, and `progress` has since moved into an annotation kind with nothing asking whether preferences follow. And **an agent container supplies a preference store of its own** - memory and instruction files - which is a genuinely new option the corpus never had, and the one the ruling most needs to weigh, because the whole argument is *take the mechanism (passive extraction from conversation), reject the separate store*, and a container-native store is a separate store wearing different clothes.
**Not carried:** the corpus half-adopted an unruled draft - a `preference` row in one table and a close-of-session extractor in another. A self-declared draft stays a draft, and the half-adoption does not travel.

---

## The drop set

9 things. **Four kinds**, one more than the brief names: the fourth, **working discipline (re-homed)**, is used for exactly two things and means *not carried into `CONTEXT.md`, an ADR or a deferral - carried in `docs/agents/` instead*. Cluster A invented the distinction for M12 without labelling it; F asked for a ruling on M112 and consistency requires the same answer.

| thing | kind | reason |
|---|---|---|
| **M9** - the two observed failure modes | exposition | These are the observations that ground rulings, not rulings. **The drop is conditional and the condition is met:** failure mode (b) - asymmetric depth biases allocation, and visible work masquerades as important work - rides as the one-clause rationale inside `symmetry-not-shallowness`, and failure mode (a) grounds `expansions-are-discarded-never-sedimented`. Both are drawn from watching a live system rather than from introspection, which is worth the clause. |
| **M11** - disposability as the acceptance criterion | agent draft never ruled | `domain-design.md §9`'s header names §9.0 and §9.3-9.5 agent drafts, and on 2026-08-23 Billy went through this exact section after an adversarial review and promoted **§9.1 and §9.2 only**, recording why and saying it was marked so it need not be asked again. A ruling pass that touched the neighbours and left §9.5 a draft is a decision about §9.5. **Verified at source.** See dispute 3 and `Needs Billy`. |
| **M12** - agents draft and never self-lock | **working discipline (re-homed)** | The `[R]` marker system, the drafts-versus-rulings header convention and `BLOCKED beats guessing` are the working discipline of a records-based repo with a document taxonomy. This repo's discipline is written elsewhere and differently, and `BRIEF.md` is explicit that inventing a document taxonomy is the failure mode that killed the last two attempts. **Not abandoned - re-homed to `docs/agents/`.** Nothing in this repo should reintroduce the `[R]` convention. |
| **M18** - which layer is a tree | exposition | The ruling it produced is a typed property of one link kind - `part-of \| concept → concept \| a DAG` - and rides in the LinkKind table. **The positive claim being dropped on purpose:** *"the artifact layer is the tree"* has **no reader**. No mechanism consumes it and no query is named for it, so by the rigidity rule it must not become a field or a structure. |
| **M65** - where the reasoning lives, the changelog gap | exposition | A property of the corpus, not a ruling about the system. It carries no decision, no term and no deferral. Both rulings it located have been re-homed, so the finding has done its work. **The corpus's four statements of its own hazard belong in this repo's working instructions, not in `CONTEXT.md` or an ADR** - the sharpest being *"before treating any list as exhaustive, state what question it was written to answer."* |
| **M80** - multiagent, one justified use and two rejected | agent draft never ruled, and superseded by generalisation | Its own section header says *"Raised by Billy; analysis below is draft, not ruled"* - verified at source. It is also superseded by the 08-22 generalisation off topology: *the invariant is a data-flow rule, not an agent topology*. **Nothing is lost:** the one surviving positive (context-isolated deep reads) is fully contained in `store-output-enters-only-as-a-conclusion`, and its rejected option - *what differs between courses is a working-instruction bundle that loads with the scope, "Not an agent"* - is carried by `the-store-is-the-channel`. |
| **M82** - the operations model | exposition, over a model falsified by measurement | 53 of 137 operations reduce and 76 do not; the deadline move the whole routing design was built around happened once in a semester; 21 of 22 executed rewrites were additive appends. Not repairable - the insert-versus-rewrite axis had no correct branch for 55% of real announcements. **Its three residues are relocated, not lost:** the falsification grounds `inbound-arrives-to-be-known`, the counter-argument becomes `two-conflicting-statements-never-coexist`'s rejected alternative (and is upheld by ruling 7), and the p5 method is a research-method ruling that goes with the method thread. |
| **M112** - method and anti-cheat apparatus | **working discipline (re-homed)** | Passes all three ADR tests but is not a decision *about the system* - it governs how the project's own research is conducted. See dispute 10. **Not abandoned - re-homed to `docs/agents/` or a skill**, alongside M12. Its one earned correction travels with it: **copies, never symlinks, and strip document metadata** - the seal was built from symlinks and `ls -la` prints symlink targets, so the first command a shell-using agent naturally runs defeats it. |
| **M114** - scale is out of scope | exposition, **and** old container | A scoping preamble that discards work rather than deciding anything, failing two ADR tests outright. Its premise - *one user, one machine, **one session at a time*** - is precisely what an agent container puts in question. **Its live residue is carried**: *writers: one* becomes an overturning condition on `the-skeleton-is-files-plus-an-index`, because single-writer is now true by design rule rather than by container. **A second residue F missed, caught here:** the same paragraph carries *"the only sizing number that matters is that ring 0 for five courses is roughly 55 obligations"*, which is the independent home of the ~55 figure. It must ride into `ring-0-carries-seven-routing-fields` before this paragraph is dropped. |

---

## Disputes settled

### 1. The id space - B/M31 versus C/M40

**Ruling: C is right. `ids-are-opaque-assigned-and-never-constructed` owns the one-id-space clause; `a-ref-is-not-a-foreign-key` cites it.**

**Zoomed to `schema.md §1` and §1.1.** The id space is stated inside §1.1's definition of `id`, in its shape block: `id := the next unused value in ONE id space, shared by every kind that can be an edge endpoint`. §1's `Ref` convention row reads in full: *"`(kind, id)`. A pointer that may name something not present. The kind tag is what permits a ref to a `course` whether or not courses ever join the node set."* It does not restate the id space. B proposed the reverse split; the record does not support it.

The `Ref` ADR keeps what is genuinely the pointer's: kind-tagging, dangling, and not-a-foreign-key. **The asymmetry both clusters wanted stated once** - nodes get opaque assigned ids, links get no surrogate id at all and are identified by a natural key - goes in `link-identity-is-a-natural-key`, where the natural key is argued, per C's own recommendation.

### 2. Ring 0's grain - D corrects B

**Ruling: D is right. Ring 0 is an access policy over obligation nodes' *fields*, not over whole nodes. Propagated to the `ring 0` term and to `two-persisted-things-one-coupling-field`'s body.**

**Zoomed to `ring-0.md` in full.** §1 says *"residency is an access policy over `obligation` nodes"*, which reads node-grained and is loose. §4 is a per-field table over one kind: seven fields are admitted, `parts` and `grade_share`/`grade_share_conditional` are excluded, on the same node. A node-grained policy cannot produce that table.

**The record itself carries the correction that makes the grain matter**, in §4's `parts` row: *"Excluded from the projection is not unreadable: it is an ordinary field of the obligation and comes back with any read of that record."* That is Billy's 08-29 *residency, not readability* ruling written into the spec, and it closes an agent error that ran two rounds. Both the term and the ADR carry it.

### 3. Disposability - A's DROP versus D's objection

**Ruling: A's DROP stands. D's objection is upheld on its factual half and does not reach A's reason. The residue goes to `Needs Billy`, not into an ADR body.**

Three findings, and the brief's framing needs one correction:

**(a) D is right about the ~55 figure, and the brief's summary is right that this voids something - but it voids A's *worry*, not A's *reason*.** A's stated DROP reason was standing: §9.5 is a declared draft. A separately volunteered, against its own call, that dropping M11 would orphan the ~55 bound. **Zoomed to `design.md`:** the number is stated independently at line 8 - *"The only sizing number that matters is that ring 0 for five courses is roughly 55 obligations"* - and §6 lists *"whether residency still holds at five courses (~55 obligations, versus the 14 rows every read-side measurement was taken over)"* as a revisit condition. `ring-0.md §1` does credit §9.5, but §9.5 supplies only the bound's **shape** (*one projection read*), never the number. A's worry is void. Its reason is untouched.

**(b) A's reason is confirmed at source and is stronger than A knew.** `domain-design.md §9`'s header names §9.0 and §9.3-9.5 agent drafts. Billy's 08-23 `[R]` promoted **§9.1 and §9.2 only**, and it says explicitly that the header *"was silent on these two, which left their status underivable"* - so the header's naming of §9.5 was never in doubt and was not revisited. That is a ruling pass that looked directly at this section and left §9.5 a draft.

**(c) D asks me to fold the residue into `the-coordinator-holds-ring-0-not-the-skeleton` as its acceptance clause. I decline.** Putting a declared draft's sentence into a ruled ADR launders it into a ruling, which is exactly the failure merge rule 3 exists to stop, and it is the failure the corpus itself commits twice (an agent document promoting a deferral to a ruling; a plan listing a draft under *do not re-litigate*). **D's substantive case is good** - in a container where compaction is routine and unpredictable, *nothing of value may live only in the conversation* is specific and checkable, not a general engineering principle - and it is a good enough case that it deserves a ruling rather than a laundering. One question to Billy.

**One thing does survive without any ruling**, because it is already ruled elsewhere: `expansions-are-discarded-never-sedimented` carries the container note that in a long-running agent conversation the discard is not automatic, and that the enforcer is the tool's return shape rather than the agent's restraint. That is a consequence of the return-type ADR, not of §9.5.

### 4. B/M17 versus E - what M92's sibling is

**Ruling: E is right, with the record. No merge, and B's proposed pairing is corrected.**

**Zoomed to `model.md §9`.** The portal-tree bullet says, verbatim: *"This is `domain/domain-design.md` §10.6's finding one level up — announcements are a delivery channel, and the portal tree is a delivery layout."* The record names its own sibling and it is the announcements finding, not the layered graph.

The merge fails on the trade-off test independently: M17's reason is *a course's knowledge does not nest*; M92's is *distribution is not organization*. Two ADRs, cross-referenced with `inbound-arrives-to-be-known` and `an-announcement-is-a-provenance-value` on the shared *delivery scaffolding is not knowledge* principle.

**E's second point is also upheld and matters more than the pairing.** `model.md §8` and §9 paraphrase §10.6 as the flat proposition *announcements are a delivery channel* - which is the proposition **§10.6 records as falsified in both courses**, 5 of 55 and 6 of 38 knowledge after discounting redundancy, with the bias pre-registered against the convenient answer so the figure is a floor. Anything quoting `model.md` on announcements is quoting a mis-citation. The correct one-line statement, and the one `an-announcement-is-a-provenance-value` carries: *announcements are mostly a channel, and the 9-16% that is not is almost always a correction against material the system already holds.*

### 5. E1 is void - propagated

**Ruling: accepted. E1 as posed is void, and the two references to it as live are corrected.**

Lifetime is two questions and the records already agree. **Verified at `design.md §5` conclusion 1, which says it in its own words:** *"The coordinator's lifetime is not a deciding fact here, and must not be reintroduced as one: the one-persistent-session decision is about the **conversation's** lifetime … and says nothing about a process holding the graph in memory. The skeleton and its verbs are invoked on demand; every call may be a new process."* The code process is per-invocation; the agent conversation is long-running, days to weeks. **Resident means held in the conversation's context.**

**F never had the error** - F's own header carries the correction, independently zoomed. **A did, in three places, and all three are re-checked:**

- **A/M6.** A stripped the residency premise *"so the gate does not inherit E1"*. The strip is still correct and its justification is restated: the gate is independent of residency because *nothing renders the whole graph* does not depend on what persists. The ADR is unchanged.
- **A/M11.** A's fallback - *"the right correction is to fold it into cluster D's E1 deferral"* - is void, because there is no E1 deferral to fold into. Under dispute 3 the route is `Needs Billy`.
- **A's flag 6** (*"E1 has no owner and cluster D should be proposing a deferral for it"*) is void. What survives is the narrower question - *what must be in the agent's context before it decides anything* - already tracked as issue #7 and carried by deferral 7. **E1 did not block the observation contract; #7 does not block it either.**

The guard against re-making the error lives in the `coordinator` term's `_Avoid_` line and in `the-coordinator-holds-ring-0-not-the-skeleton`'s lifetime clause.

### 6. `layer`'s three senses, and "skeleton kinds"

**Ruling: both settled here. Neither is escalated.**

**`layer` is reserved for the three strata** - `obligation`, `concept`, `artifact` - and Billy's coarser 08-29 distinction is named **the skeleton** versus **the time projection**. **`design.md §3.1`'s "skeleton kinds" becomes "layered kinds"**, because `course` and `sticky_note` are also nodes in the skeleton and the phrase is a trap.

**Why this is not Billy's to rule, which is the part B hesitated on.** `CONTEXT.md` is an engineering glossary, and choosing which of three senses a glossary reserves for a word is what a glossary is for. **Ruling 8's content is untouched**: content and time stay separate, query-by-time-period is not the skeleton's responsibility, and modelling *week N* as a node joined by edges is still not the right modelling. Nothing about the ruling changes; only the name of the thing it names does, and the alternative - a glossary in which `layer` means three different things - is not a live option.

The second collision is easier: *"skeleton kinds"* is a phrase inside an agent-written spec section, not Billy's, and it is straightforwardly wrong about its own referent.

**Both go under `_Avoid_` on `layer`, where a reader meets them before making the mistake.** D's related collision - **"the projection"** with three referents (ring 0's, the calendar projection, the time projection) - is settled the same way: ring 0 never needs the word, and *the time projection* keeps it.

### 7. The graveyard - 16 rows, and where `time_point` sits

**Ruling: C's count is right; C's disposal of `time_point` is not, and a third option is better than either.**

**Zoomed to `schema.md §7` and counted: sixteen `| absent | why |` rows.** The inventory's fifteen is wrong, and the derived statistic *"thirteen of fifteen carry no changelog line"* sits over the wrong denominator and should be dropped rather than restated.

**`time_point` stays in the table, re-labelled.** C is right about the diagnosis - the row's own text (*"the type is out because the projection is, not because nothing reads it"*) contradicts the *do not re-add without a new ruling* header it sits under - and right that filing a deferral under that header mis-files it. But C's remedy thins the table, and the graveyard is the corpus's only standing anti-regression device: a later session reading an older document restores what it finds there, and the older documents are still in the repo. **Removing a row is the move the table exists to prevent, even when the row is mis-filed.** So the row stays, states in its own text that it is a deferral rather than a removal, and points at deferral 4. Nothing is thinned and nothing is mis-filed. This is C's own stated fallback and it is the better of the two.

**The rest of C's proposal is adopted:** four rows re-reasoned (`count`, `recurring obligations`, `course.offering_term`/`prereq`, `course` free-text), two flagged (`stated_in`/`source_ref` with no reason at all, coarse dates), one flagged as most likely to need re-opening (`term_start`), four added (`present`/`external_ref`/`backing`, `supersedes`, `weighting_scheme`, the `<course_id>-slug(name)` id scheme). The full table is in *The graveyard table* above.

**The caveat that must not be softened, and it is the ADR's most important sentence:** the graveyard's **rulings bind; its evidence base is self-disqualified.** Three rows say so about themselves in their own text.

### 8. C21, concept granularity - closed or carried

**Ruling: closed, and E's sharpening is adopted. It does not travel into reconciliation as an open escalation.**

**Zoomed to `write-rules.md §3.4`, ruled by Billy 2026-08-28.** The operative test is **recurrence**: *"A part is a concept worth capturing because it might occur elsewhere in the system - on another obligation, in another course. That test does the whole job."* The worked rows keep `Big-O`, `Graph`, `Queue`, `Priority Queue` and drop `Monte-Carlo`, `A5Tree` and `Life on the River` as one-off and local. A recurrence test forbids the per-topic split, so the agent's objection - *do not rescue the first hub by splitting into per-topic analysis concepts; Big-O of Quicksort and Big-O of Dijkstra are the same skill* - is upheld by a later Billy ruling. B and C both concluded this independently and both are right. **C21 is closed.**

**E's refinement is correct and is adopted, because B and C overstated the finding.** The recurrence test decides **whether** a string becomes a concept; it does not state **at what grain** one is cut. The worked table proves it: `Multiple Choice` and `Problem Solving` are dropped as *noise - the paper's structure rather than its content*, and `Multiple Choice` recurs constantly. Recurrence does not catch it; separability does. So the two tests are two jobs and both are needed, and `parts-carries-recurring-concepts-not-size` states them as two halves of one rule rather than as one rule doing a second job. **Neither record says the rule does either job, which is the finding that survives.**

### 9. The five refactor triggers

**Ruling: B's worry is correct, and the answer is a new ADR rather than a merge.**

**Zoomed to `design.md §2`.** Five triggers, A-E, introduced by one sentence that is the trade-off: *"The question is answerable by naming what would force a rewrite when slice 2 lands, and committing to exactly enough to defuse each. Everything else stays unbuilt."* One rejected alternative (defer all five and refactor later), one reason (a forced rewrite costs more than five minimal commitments). That satisfies the merge rule, with the five rows as the shape.

**But it does not absorb the four triggers that were argued separately.** Trigger A is argued at length in `schema.md §1.1` against course-local ids; trigger B in `schema.md §1`/§8 against shape-sniffing; trigger C in `domain-design.md §6` against read-time inference; trigger D in `architecture.md §6` against prompt and tool-registry enforcement. Four different rejected alternatives. Absorbing them would produce an ADR that can state none of the four real reasons - the exact failure the brief's calibration pair warns about.

**Trigger E is the reason the ADR is worth creating.** *Persistence coupling → a repository interface with one implementation (DIP)* is argued nowhere else and **is claimed by no cluster**. F's tier ADR is adjacent and does not state it; C's field work does not reach it. Without this ADR it is lost.

**Net: recording one trigger while its siblings scatter was indeed worse than recording all five once - and the fix is a naming ADR that all five cite, not a merge that dissolves four arguments.** B's and C's instinct is upheld; their proposed mechanism is not.

### 10. M112 - is `docs/adr/` its home

**Ruling: no. Not carried into any of the four destinations; re-homed to `docs/agents/` or a skill. F's own alternative is the right one.**

M112 passes all three ADR tests - a result obtained without pre-registration cannot be retrofitted with one; a solo project running anti-cheat against its own agents is surprising; judging after the run was available and rejected. **That is not the question.** The four destinations partition decisions about *what the system is*. M112 governs *how agents working on the project conduct research* - pre-registration, anti-cheat, the seal, keeping raw artifacts, keeping design vocabulary out of raw passes. A future reader opening `docs/adr/` to learn what the semester manager is would find a rule about how a sitting is run.

**Consistency is the decisive argument.** Cluster A already ruled the same class the same way: M12 (the `[R]` convention, drafts-versus-rulings, `BLOCKED beats guessing`) is not carried into `CONTEXT.md`, an ADR or a deferral, and A said explicitly that this means re-homed, not abandoned. This repo's own `CLAUDE.md` names `docs/agents/` as where agent working discipline lives. Two things in the 115 are of that class and they should not land in two different places.

**Nothing is lost, and one thing is gained.** The apparatus's own earned correction - **copies, never symlinks, and strip document metadata**, because the seal was built from symlinks and `ls -la` prints symlink targets - is an operational instruction that reads far better in a skill than in an ADR. And F's flag that `write-rules.md`'s 08-28 method statement is the same discipline (*abstract rule-writing stalled for two months; the rules came from Billy editing one course's records by hand, so the rule is what he did and the before-and-after is the evidence*) means the re-homed document has a second member waiting for it.

---

## Needs Billy

Four items. Each is a question with the evidence on both sides, and none of them is work I could have decided.

**1. Disposability - is it a standing acceptance criterion in the new container?**
*"If losing the coordinator session loses information, the design is wrong. Any change that makes losing the coordinator painful is moving backwards."*
**For carrying it:** in a container where compaction is routine, lossy and unpredictable, *nothing of value may live only in the conversation* is a specific, checkable constraint rather than a general principle, and it is the natural acceptance clause for the residency ADR. Two later records already treat it as binding.
**Against:** `domain-design.md §9`'s header names §9.5 an agent draft, and your 08-23 pass through that exact section promoted §9.1 and §9.2 **by name** and left §9.5 alone, recording that the omission mattered. I will not launder a declared draft into a ruled ADR.
**The question:** does §9.5 become a ruling in the successor's terms, or stay a draft? One word either way. If it becomes a ruling, its home is `the-coordinator-holds-ring-0-not-the-skeleton`.

**2. `grade_share`'s field name.**
`design.md §7` item 1 records the field's name as **not settled, owner: the user**. All four spec records use `grade_share`, and your 08-27 and 08-29 rulings both use it. Cluster C's proposal - which I have adopted - is to ship the term as `grade_share` and let you overwrite the string, on the ground that a deferral issue for one word is not worth opening. **This is on the list because the record assigns it to you by name, not because it is hard.**

**3. Three graveyard rows and one live field stand over questions already addressed to you.**
`evidence/2026-08-28-corpus/2c03/RULINGS-NEEDED.md` puts five field decisions on your desk, dated 08-28, and **no survey read it**. Three of them bear on things in this set and none has been chosen:
- **R1** - tutorial attendance gets no row and it is 5% of the grade. Three options offered (hold the graveyard / re-open by ruling / defer to four courses); none chosen. It supplies the second, third and fourth instances the `count` row's `n=1` lacked. **The row stands under the no-re-add rule until you lift it**, which is why it is carried - but it is carried knowing the evidence moved.
- **R2** - **`grade_share` cannot hold a bonus, and this is a live schema defect.** 2c03's real shares sum to 100 and the course grants two bonuses that are **additive, outside the 100**; storing `1` asserts something false and `optional: true` does not carry additive semantics. The file's own note: *"Four independent spec reviews missed it, because seeing it requires the arithmetic."* It has no M-number and no home in the 115.
- **R4** - `course` has zero free text by rule, so the outline's instructor, term boundaries, units, antirequisites and textbook can reach the system only as annotations - and **term boundaries are load-bearing** for the last-day-of-classes rule. The graveyard row routes them to annotations; whether that is acceptable for a load-bearing value is not ruled.

**4. One correction is a deliverable and has not been made.**
Your 2026-08-29 ruling - *the corpus is evidence about what the material contains; it is not evidence about what a record should look like* - withdraws every character count taken from `records.json` and names correcting `model.md §10.5`'s `MEASURED 2026-08-28` entry as *"a deliverable of this cycle, not a side note."* **I checked at source: the banner is still there, uncorrected.** It is the first action item of the presentation-surface deferral. Flagged here because it is a Billy ruling that has not reached the record it invalidates, and any cluster quoting 87-278 / 871 / 1,010 / 459 is quoting a withdrawn number.

**Deliberately not on this list.** The `layer` and "skeleton kinds" namings (settled - dispute 6, naming a glossary is not adjudicating a ruling) · the product-facing verb names (already inside deferral 3, where ruling 9 put them) · `M112`'s home (settled - dispute 10) · whether `time_point` leaves the graveyard (settled - dispute 7). **Ruling 9's onboarding question** - who does onboarding and how information arrives - has no owner in any of the six tables and no M-number; it goes to the residue reconciler, not here.

---

## Coverage

All 115 things, by M-number, each in exactly one destination.

**`CONTEXT.md` - 13 things, 46 terms.**
M2 · M13 · M14 · M15 · M26 · M27 · M34 · M46 · M47 · M55 · M58 · M66 · M74

**`docs/adr/` - 67 things, 61 ADRs.**
*A (7):* M1 · M3 · M4 · M5 · M6 · M8 · M10
*B (16):* M16 · M17 · M19 · M20 · M22 · M23 · M24 · M25 · M30 · M31 · M32 · M33 · M36 · M37 · M38 · M39
*C (16):* M40 · M41 · M42 · M43 · M44 · M45 · M48 · M49 · M50 · M51 · M52 · M53 · M54 · M57 · M62 · M63
*D (8):* M67 · M69 · M70 · M71 · M72 · M73 · M75 · M76
*E (8):* M81 · M83 · M85 · M88 · M89 · M91 · M92 · M96
*F (12):* M97 · M98 · M100 · M101 · M103 · M104 · M105 · M106 · M107 · M108 · M110 · M113

Four of these are carried as **rows of the graveyard ADR** rather than as ADRs of their own: M52, M53, M54, M63. Three are carried inside a **merged** ADR: M3 (in M71's), M37 (with M91), M98 and M105 (with M97). Two are carried as **splits across two ADRs**: M48 and M51.

**Deferral issues - 26 things, 17 issues.**
M7 · M21 · M28 · M29 · M35 · M56 · M59 · M60 · M61 · M64 · M68 · M75b · M77 · M78 · M79 · M84 · M86 · M87 · M90 · M93 · M94 · M95 · M99 · M102 · M109 · M111

M60 supplies two deferrals to two different issues (`time_point` → issue 4, the plan → issue 5) and is counted once.

**Not carried - 9 things.**
M9 · M11 · M12 · M18 · M65 · M80 · M82 · M112 · M114

**Arithmetic.** 13 + 67 + 26 + 9 = **115.** ✅

**Routed to the residue reconciler, not carried here.** Raised by a cluster but holding no M-number, so outside the six tables: the `closure` ruling (single-source reachability, not an all-pairs matrix) · `write-rules.md §1.1` (an inferred value is asked about, not annotated - ruling 7's invariant written at field level eight days early; E recommends adopting it into the conflict ADR) · `schema.md §4.6` (annotations arrive through their own channel) · `design.md §3.6` (extraction, landing and reading are three concerns) · `ring-0.md §7`'s negative-definition caveat · *"before treating any list as exhaustive, state what question it was written to answer"* · ruling 9's onboarding question. Where one of these bears on a thing I carry it is named inside that thing, but the routing decision is the other reconciler's.
