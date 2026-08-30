# Classification pass - Cluster F: the container (M97-M114)

**Proposals only.** Nothing here is created. Two sibling passes are running on clusters A-E and a reconciliation follows.

**The correction this cluster carries.** Lifetime is two questions. The **code process** is per-invocation (`design.md §5` conclusion 1, which states it in its own words and warns against reintroducing the other reading: *"The skeleton and its verbs are invoked on demand; every call may be a new process"*). The **agent conversation** is long-running on a scale of days to weeks (`domain-design.md §9.5`: *"do not try to make it survive a semester. Its long-running scale is days-to-weeks"*). `ring-0.md §7`'s residency claim is about the conversation's context window, not a process's heap. Verified at source; the records already agree with each other. Wherever "the coordinator's lifetime" appears below, it is named.

**Method note.** I zoomed to source for M97-M106 (`records/spec/architecture.md` in full, `design.md` §1, §3.6, §4-§7) and for M107-M113 (`records/domain/domain-design.md` §0.1, §0.6, §1, §5, §6, §7, §8, §9.4, §9.5). Two things changed as a result and are marked per entry.

---

## M97. The three-tier split

**Destination: `ADR`**

**Proposed title.** Three tiers, and a tier is designed only against a tier that already exists.

**Tests.**

- *Hard to reverse* - **yes.** The split is directory structure plus an import-resolving boundary test; unwinding it means rewriting every call site. The record's own §7 shows what re-homing one operation set costs.
- *Surprising without context* - **yes, but not where you would expect.** The split itself is ordinary and the record says so (*"adopted because it is the ordinary one and not because this system is unusual"*). What a future reader will stop at is the ownership line: **every rule about what an agent should do is presentation**, the application tier holds no rule about what deserves to exist, and **a service method does not defend itself against a caller that should not have called it.** That last one reads as a bug until you know the split.
- *Real trade-off* - **yes.** The rejected alternative is the one the project had actually been running: a graph-generic operation set with behaviour rules mixed into the schema, and descriptions written for methods that did not exist.

**Body.** The system is split presentation / application / persistence: the surface, the rendering and every rule about what an agent should do are presentation; the field set, the kinds, construction-time validation, id minting and CRUD at field grain are application; the serialized files and the adjacency index are persistence. The application tier has no surface and does not defend itself - when its methods are called we expect them to be called correctly. **A tier is designed against the tier below it, and that tier must already exist**: designing the surface first is how this project spent three cycles specifying descriptions for methods that do not exist.

**Shape riding inside.** The three-row tier table from `architecture.md §1`, with "the CLI" replaced by "the surface" (see M100).

**Container verdict: both, high confidence.** The tier scheme, the ownership line and the sequencing rule are container-independent - they are about where a rule lives relative to a compiled boundary. Only the word "CLI" in the presentation row is a container fact, and it is replaceable in place. The corpus's own statement that `../domain/` gets tier "none - it is the material both tiers are derived from" (C77) is a merge fact about the fall26 records, not a decision to carry.

**Sequencing stripped.** None. The sequencing rule here is a dependency claim (a tier needs the tier below it to exist), not slice ordering.

**Touched by Billy's rulings.** Ruling 9 is downstream of this ADR and is its strongest confirmation: write rules have not landed, prompt and docstring work has not landed, and the surface does not exist - which is exactly the gate this rule imposes.

**Cross-cluster.** Strong merge candidate with M98. The application tier's "no defensive validation" claim reaches cluster C (construction is the only gate, `schema.md §8`) and cluster B (`design.md` trigger D, the purity cut).

**Zoomed.** Yes, `architecture.md` in full. Changed: the inventory summary makes the split look like the ruling; at source the load-bearing sentences are the ownership line and the sequencing rule, and the split is explicitly disclaimed as unremarkable.

---

## M98. The four §3 consequences

**Destination: `ADR`**

**Proposed title.** No rule about what deserves to exist lives below the surface.

**Tests.**

- *Hard to reverse* - **yes, indirectly.** These four are the cited grounds for field-level rulings already made (`schema.md §1.1`'s opaque id, `§3`, `§4.5`). Reversing one reopens the field set, not just a prompt.
- *Surprising without context* - **yes.** A schema that deliberately refuses to encode *the value must be what the source stated*, and an agent that will not auto-add a row it can plainly see, both look like omissions.
- *Real trade-off* - **yes.** The alternative was schema-enforced provenance and auto-capture, rejected because the enforcement point does not exist (JSONL enforces nothing, a constructor sees one line) and because auto-capture fills the store with rows nobody asked for.

**Body.** The field set says what a legal value is; how to produce one, and whether a row should exist at all, live at the surface. The agent never auto-adds anything unless the user has made it clear they want it tracked, and it works by listing then acting on what it saw - so **identifiers need not be human-facing, and matching two records is an interaction at the surface, not an algorithm in the application tier.**

**Shape riding inside.** The four consequences, with two amendments that must travel with them and are not in either body today: consequence 1's absolute phrasing (*"a write rule never refers to the source"*) was withdrawn on 2026-08-28 - the real distinction is **the direction a rule is derived from**, and three of the five written rules do refer to a source (C78). Consequence 3 (*"the system must not chase the agent"*) survives as a stance but its concrete form is re-ruled by Billy (below).

**Container verdict: consequences 2 and 4 are domain, high confidence; consequence 1 is domain, high confidence; consequence 3 is both, medium confidence.** Consequence 3 is quoted from Billy in the first person about **daily usage** by a person (C79), and it is the ground two field-level rulings rest on. Its premise is a person's tolerance for being asked, which does not change with the container - what changes is who does the asking and how often, and that is now an eval question rather than a schema question.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Rulings 2, 4, 5 and 7 all land here. Ruling 2: the work need not be a functional one-pass - the agent notices from the skeleton and ring 0 and asks when needed; ask-frequency is an acceptance/eval item measurable only after the system is roughly built. Ruling 4: `progress.state` defaults to `not_started` **precisely so the agent does not keep asking**, and proactivity is written too rigidly at present. Ruling 7 refines consequence 3 into something concrete: two conflicting statements must never coexist; shallow conflicts the agent resolves itself **but must report afterwards**, deeper ones it asks about first. **The stance is carried; the ask-design is not, and belongs with cluster D/E's asking thread.**

**Cross-cluster.** Consequence 1 belongs to cluster E (write rules) and carries the C78 correction with it. Consequence 3's downstream uses are cluster C (`schema.md §4.5`, `§3`). Consequence 4's structural half is already cashed as cluster C's opaque id. Merge candidate with M97.

**Zoomed.** Yes. Changed: the inventory quotes consequence 1 in its withdrawn absolute form without the 08-28 correction adjacent; at source both bodies still carry the withdrawn phrasing, so the correction has to be written into whatever carries this forward or it will be lost twice.

---

## M99. The migration list - what the tier split moved

**Destination: `DEFER`**

**Precondition that wakes it.** All four items are presentation-tier work, and ruling 9 states the gate verbatim: write rules have not landed, prompt and docstring work has not landed, ring 0 and the skeleton have no exposed surface, and the product-facing verb names are not decided. **Wake when a surface exists with named verbs and written descriptions.** At that point: `land()`'s description and the read operations' descriptions get written, the verb-routing evaluation becomes runnable, and the screenshot-extraction evaluation becomes runnable.

**What is dropped inside this deferral, as an old-container artifact.** The clause *"the MCP adapter is at most an adapter over the CLI's grammar, and may never be built."* It depended on the CLI being the primary surface with a human in front of it, so an agent protocol was a secondary export that might never be needed. In the successor the agent is the only caller and there is no human-operated CLI beneath it, so the demotion has nothing to demote from. **What replaces it is not "build MCP" but M100's ruling unchanged**: the grammar is the early and expensive decision, transport is late and cheap, and this container simply fixes the transport earlier than the record expected.

**Container verdict: both, high confidence.** The re-homing (descriptions and evaluations are presentation) is container-independent and survives intact. The adapter's ranking is pure old container.

**Sequencing stripped.** The ordering claim "write rules precede the presentation tier" is a dependency, not slice ordering, and is folded into M97's ADR rather than carried here.

**Touched by Billy's rulings.** Ruling 9 supplies the precondition and is the reason this is `DEFER` and not `DROP`.

**Cross-cluster.** The write-rules dependency is cluster E's. The two evaluations are eval-mode items and will collide with whatever cluster A/D produce on acceptance criteria.

**Zoomed.** Yes, `architecture.md §4`. No change to the inventory's reading.

---

## M100. The surface is a CLI, and the grammar beats N verbs

**Destination: `ADR`**

**Proposed title.** One composable grammar with progressive disclosure, not N described verbs.

**Tests.**

- *Hard to reverse* - **yes, and the record says so in its own words**: *"the grammar is the early and expensive decision."* Every level of render and every call signature follows from it.
- *Surprising without context* - **yes.** The obvious build for an agent-facing tool in 2026 is a tool per operation with a good description on each. This deliberately does the opposite.
- *Real trade-off* - **yes, and it is the only ruling in the corpus decided by a measurement of the successor container.** N single-purpose verbs, each deciding when it is called from its own description, were rejected because **rewording one docstring moved a verb's call count from 1 to 9 with data availability held constant**.

**Body.** What is rejected is a shape, not a protocol: N single-purpose verbs, each routed by its own description, measured as fragile (one docstring reword, call count 1 to 9, data availability held constant). What replaces it is one composable grammar with progressive disclosure - each level renders what is around it, and going one level deeper is one more call. **The distinction is independent of transport**: a server exposing exactly one tool whose argument is a command string has the same property, and a CLI with forty subcommands each needing `--help` has the old defect.

**Container verdict: both, and it contains its own bridge - high confidence.** "The surface is a CLI" is a container fact and is stripped. Everything else is not: the transport-independence clause was written for exactly this situation, and the 1-to-9 measurement is a measurement of an LLM routing over tool descriptions, i.e. **evidence about the successor container obtained in the old one** (C81). This is the clearest case in my cluster of a ruling that looks container-bound and is not.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 9: the product-facing verb names are not decided and *"obviously cannot be 'ring 0' and 'skeleton'"*. The ADR records the shape; naming stays open and belongs with M99's deferral.

**Cross-cluster.** The progressive-disclosure levels (list returns ring 0's summary; drilling into a course is a call; drilling into a node is the walk) touch cluster D (ring 0) and cluster B (the walk).

**Zoomed.** Yes, `architecture.md §5`. No change; the inventory's reading of the bridge clause is exactly right.

---

## M101. Addressing at the surface

**Destination: `ADR`**

**Proposed title.** Addressing belongs to the surface; every read returns handles.

**Tests.**

- *Hard to reverse* - **yes.** It is the other half of the opaque id. If any surface form has to mean something to the layers below, the id stops being opaque and the schema acquires an addressing concern.
- *Surprising without context* - **yes.** A reader seeing renders that never print an id, and a schema whose id is deliberately meaningless, will ask how anything is ever addressed twice.
- *Real trade-off* - **yes.** The alternative is human-meaningful identifiers in the schema, rejected because it puts a presentation concern in the field set; the cost is a binding constraint that is easy to violate silently.

**Body.** The surface may render a record however it likes and resolve at call time, the way a materialized view does; the `id` is opaque precisely so nothing at the surface has to mean anything to the layers below. **One constraint binds it: nothing constructs an id, so every read that returns records must return their handles** - a handle absent from the render makes the level below unreachable.

**What is dropped inside it, as an old-container artifact.** The two-branch rule: *"human-readable by default, a machine branch for machine consumption, and any locator the next call needs must appear in the human render too - never only in the machine branch."* That mechanism exists because a CLI has stdout for a person and a `--json` flag for a program, and the risk it guards is a locator surviving only in the branch a human never reads. **In the successor there is one channel: the agent reads the render and Billy reads the same transcript.** The two-branch structure has nothing to separate. The constraint underneath it - every read returns handles - survives and is strengthened, because there is no longer a second branch to hide a handle in (C82).

**Container verdict: both, high confidence.** The addressing ruling is domain-independent and survives; the render-branch mechanism is a CLI artifact and dies. Note this is the opposite of the inventory's framing, which reads the successor as *inverting* which branch is the default. It does not invert it - it collapses the two into one, which is why the binding constraint gets easier rather than harder.

**Sequencing stripped.** The two consequences in `architecture.md §5` are marked "neither in the first build"; that is build ordering and is not carried.

**Touched by Billy's rulings.** Ruling 9 indirectly - the render does not exist yet, so this ADR records a constraint on a surface not yet built.

**Cross-cluster.** Depends on cluster C's opaque-`id` ruling (`schema.md §1.1`) and will collide with it if that cluster proposes an ADR of its own; they are two halves of one decision. The withdrawn composed-summary recommendation in the same section is cluster B's (`model.md §7.1`, summaries exist only for artifacts).

**Zoomed.** Yes, `architecture.md §5` and its 08-28 changelog entry. **Changed my call**: reading the two-branch rule in place, it is a stdout-versus-`--json` mechanism, not a claim about who the primary reader is. That turned this from a probable drop into an ADR with a named sub-drop.

---

## M102. The acceptance criterion - 22 obligations across two courses, then one course

**Destination: `DEFER`**

**Precondition that wakes it.** Extract the remaining courses **when the presentation tier and the write rules exist**. The reason is stated at source and is not arbitrary: every contested field (`parts`, a note's `category`, `origin`, whether a note is worth keeping at all) needs a write rule; a write rule is derived from what a value must be for a node to render well; the render does not exist. **Reading three more courses without those rules produces three more courses of noise and does not produce the rules.** Ruling 9 restates the same gate from the other side.

**What must travel with the deferral.** The number is **14 for 2c03**, not 22. The 22 came from a transcription since superseded and included a row the graveyard forbids (recurring tutorial attendance), so **22 is not reachable by re-running the old route**. `schema.md` still counts in 22s in §3, §6 and §7 and `design.md §1` F5 still states it; neither correction propagated (C83). The live criterion is: the field set holds **one course's real obligations, landed through the write operations and read back** - "landed" meaning written through the write operations, not through `land()` specifically.

**Container verdict: domain, high confidence.** Nothing about this criterion depends on a human at a CLI. It is a verification-mode item, not a decision.

**Sequencing stripped.** "Not before the presentation tier" is the deferral's precondition rather than a plan step, so it is carried as the wake-up condition and not as ordering. Nothing else.

**Touched by Billy's rulings.** Ruling 9's gate is the same gate. Ruling 1 (v1's boundary is coursework inside academics) does not change the count but does bound what "real obligations" means.

**Cross-cluster.** **Live collision:** every count in cluster C's graveyard (M62) is stated over 22. Whoever carries the graveyard needs the 14 correction or the counts will be re-stated wrong.

**Zoomed.** Yes, `architecture.md §4`. No change; the reasoning at source is fuller than the inventory's summary and is quoted above.

---

## M103. The skeleton does not need a database

**Destination: `ADR`**

**Proposed title.** The skeleton is files plus an index rebuilt at load, not a database.

**Tests.**

- *Hard to reverse* - **yes.** Adopting a graph engine later is a migration of every read path; the record treats it as a hard boundary rather than an optimisation.
- *Surprising without context* - **yes.** A graph model with edges, traversal and a walk, and no graph database, reads as an oversight until you see the numbers.
- *Real trade-off* - **yes, with the alternatives named and the numbers stated**, including a market fact held explicitly at arm's length.

**Body.** The skeleton needs a durable serialization plus an adjacency index rebuilt at load; all three graph operations are scans over that index, and **the load is cheap enough that per-invocation and resident are indistinguishable** - measured, 2c03's 138-node/137-link graph is 52 KB and parses in 0.27 ms. A graph engine would buy query planning for three hand-writable queries over ~2,200 edges. **The store is a different case and gets a different mechanism**: 62 MB of vectors should not be re-parsed per invocation and chunk text wants random access, so the store wants storage - not an ANN index, and not necessarily the same engine.

**Shape riding inside.** The deciding facts (~640-1,600 nodes / ~2,200-3,700 links at five courses; conclusions survive a 2-3x error; one writer; 0.27 ms cold load) and **the overturning conditions, which are the reason this is worth writing down**: the corpus growing an order of magnitude · multi-device sync becoming real · the skeleton growing far past ~640 nodes · **and one more that the container change adds - a second concurrent writer** (see M114).

**Container verdict: domain, high confidence, and this survives the container change better than anything else in my cluster.** Its argument is explicitly per-invocation, so the code-process lifetime question is already settled inside it: *"The coordinator's lifetime is not a deciding fact here, and must not be reintroduced as one: the one-persistent-session decision is about the conversation's lifetime ... and says nothing about a process holding the graph in memory."* That sentence at source is the correction my brief carries, written by the record itself.

**Sequencing stripped.** "Slice 3" as the home of the store's engine decision is dropped as ordering; the substance - **the engine and the serialization format are deliberately not decided** - is carried.

**Touched by Billy's rulings.** None of the nine directly.

**Cross-cluster.** The pgvector/PostgreSQL PASS result (`domain-design.md §10.1`, `step-minus-1/FINDINGS.md §P1`) belongs to the store and is cluster B/E's; it does not conflict with this (C84), the two are about different halves, and only this record says so. The single-writer fact below is the one that needs a home outside cluster F.

**Zoomed.** Yes, `design.md §5` and §6 in full. Changed: the inventory does not carry the asymmetry paragraph, which is the part that makes the store's different treatment a boundary rather than tuning, and it is in the body above.

---

## M104. The language - TypeScript

**Destination: `ADR`**

**Proposed title.** TypeScript, because two of this design's own mechanisms need a compiler that can refuse.

**Tests.**

- *Hard to reverse* - **yes.** Language choice with the ordinary lock-in.
- *Surprising without context* - **yes.** The project embeds documents, the embedding ecosystem is Python's, and the agent that analysed it recommended Python and then reversed. A future reader will assume Python was the obvious answer and want to know why it was not taken.
- *Real trade-off* - **yes, and derived rather than preferred.** Rust "fits the data shapes best" and was rejected on iteration speed for a solo build; Go satisfies the enforcement requirement and was rejected the same way; runtime type erasure is stated as a real cost and explicitly called "a wash" rather than argued away.

**Body.** TypeScript, settled by what this design already claims about itself: `design.md §3.5` defuses trigger D *"by type, not by restraint"* and `schema.md §8` makes construction the only enforcement point there is - **both are claims about a compiler that can refuse.** Python cannot refuse (any module may import any other, so the purity cut degrades into discipline, and adding a kind raises no error at the sites that must change), so trigger B's promise would be hoped for rather than checked. **The embedding ecosystem stays Python and does not cross a tier boundary**: the store couples to the skeleton through the single field `chunk.node_id`, and `ingest.py` remains an offline pass in no tier.

**Container verdict: domain, high confidence.** The argument is entirely about the design's own enforcement claims, not about who invokes the code. A Claude Code container runs either language equally well, so it supplies no reason to revisit.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine.

**Cross-cluster.** Depends on cluster B's trigger D / purity cut and cluster C's "construction is the only gate". `design.md §1`'s constraint line still reads *"directly-callable Python, no MCP, no Postgres, no `PA_SOURCE`"* and is stale (C85) - it is what a reader hits first in that record, and nothing in the successor should inherit it. The `PA_SOURCE` half of that same line is M109's.

**Zoomed.** Yes, `architecture.md §6`. No change.

---

## M105. Packaging - packages, then directories

**Destination: `ADR`**

**Proposed title.** Tier boundaries are directories enforced by a test, because an npm manifest cannot refuse.

**Tests.**

- *Hard to reverse* - **weakest of the three, and I flag it.** Changing directories back to packages is a day's work. What is hard to reverse is the knowledge: without this written down, someone re-proposes packages on the same false ground within a month.
- *Surprising without context* - **yes.** A reader sees directories and a test and assumes the boundary is a convention that was never enforced properly. It is the opposite: packages were tried first and are the weaker enforcement here.
- *Real trade-off* - **yes, and it is the corpus's cleanest reversal**: ruled and reversed within 24 hours on a checkable fact, with the replacement's limits stated in place rather than discovered later.

**Body.** The tiers are directories under one source root, not separate packages. The original ground - a manifest cannot be waived, a lint rule can - **is false under npm: workspace dependencies hoist, so any package resolves any other whether or not it declares it, and a manifest states an intent it cannot refuse.** What actually refuses is `app/tests/boundary.test.ts`, which resolves every relative import and fails one reaching a tier at or above the importer's own level; **it has been shown to fail**, which is the only thing separating it from a convention.

**Shape riding inside.** The test's stated limits: it sees relative specifiers only, and it scans `src/`, not `tests/`. Both are fine while there is one package and no path aliases, and both stop being fine the moment either changes.

**Container verdict: neither domain nor container - it is a build-tooling fact, high confidence.** It survives exactly as long as M104 survives.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine.

**Cross-cluster.** None outside F. **Merge candidate with M104** - one ADR "TypeScript, directories, and a boundary test" is defensible and may read better than two.

**Zoomed.** Yes, `architecture.md §6` and both changelog entries. No change.

---

## M106. Serialization - JSONL, `schema_version`, and where validation happens

**Destination: `ADR`**

**Proposed title.** JSONL with a `schema_version`, and construction is the only gate.

**Tests.**

- *Hard to reverse* - **yes.** The on-disk format and the single enforcement point determine where every constraint can live.
- *Surprising without context* - **yes, twice.** Vectors are forbidden from the JSONL and go to a side binary store keyed by node id; and **validation deliberately does not happen at load**, with a measured consequence that looks like a bug.
- *Real trade-off* - **yes.** Validating at load costs a pass owned by the application tier and was parked rather than paid; the price is a malformed record that survives a round trip silently.

**Body.** The skeleton persists as `nodes.jsonl` + `links.jsonl`, each file carrying a `schema_version` - JSONL enforces nothing and construction is the only gate, so without a version a stale file fails as an unexplained validation error. Vectors, if they ever arrive, go to a **side binary store keyed by node id, never into the JSONL**. **Construction is the only place a record's own shape is checked, and a constructor sees one line**, so any rule ranging over more than one record - the id space, one-current-value-per-target, link identity - belongs to the services and not to the constructor.

**The hole, which must travel with the ADR.** Construction is **not currently part of the load**. Measured, not inferred: a store carrying `due: 'April 2026'` and a slice-2 `concept` node **loaded without error and was rewritten intact**. Closing it needs a load-time pass owned by the application tier, parked at `../plan/backlog.md`. The code block in `schema.md §8` still carries an inline `-- validation happens HERE` comment directly above prose saying the opposite; that comment must not be copied forward.

**Container verdict: domain, high confidence.** Nothing here depends on who invokes the process. If anything the per-invocation container makes the silent-round-trip hole sharper, because every invocation is a fresh load that could have caught it.

**Sequencing stripped.** "Nothing closes it in slice 1" is ordering; the substance - it is open and has an owner - is carried.

**Touched by Billy's rulings.** None of the nine directly. Ruling 7 (two conflicting statements must never coexist in the system) has an uncomfortable edge here: a malformed record that loads silently is a statement the system holds and cannot check.

**Cross-cluster.** Cluster C owns `schema.md §8` and will very likely propose the same ADR. Flag for merge; if cluster C carries it, cluster F should carry nothing here.

**Zoomed.** No - the inventory's account is quoted from `schema.md §8` and its changelog and is self-consistent, and the measurement is stated as measured.

---

## M107. Session topology; no fold; course != domain; the store is the channel

**Destination: `ADR`**

**Proposed title.** Components share state through the store, never through a protocol.

**Tests.**

- *Hard to reverse* - **yes.** It decides that there is no message protocol at all - no queue, no cursor, no ack, no fold, no orchestrator holding state about who is awake. Adding one later is a new subsystem.
- *Surprising without context* - **yes.** The obvious design for a multi-component agent system is an orchestrator that dispatches and collects, and the sibling system this was modelled on has exactly that.
- *Real trade-off* - **yes, and stated as such:** *"steal the shape, not the mechanism."* The rejected alternative is Fairy's dispatch/ack/fold, rejected because it solves **delivery** (did the fact arrive, is the other side awake) and this system has no delivery problem - one human, one store.

**Body.** There is no orchestrator and no control relationship, only a scope parameter: **the store is the channel.** Ingestion writes to the facts layer and the coordinator sees it on its next read; a subagent returns a conclusion, never state. **One domain, not one per course** - per-course ceremony would be the cloned-repo-furniture mistake, and what actually differs between courses is a working-instruction bundle that loads with the scope, not an agent.

**What is dropped inside it, as old-container artifacts.** The vocabulary the ruling is phrased in - registry entry, episodes, `/wrap`, `/standup`, ack protocol, fold, cursor, "domain" in the build-repo sense - is the old container's, and the sibling system it is measured against (Fairy) is not inherited by the successor. The three-scope **session** table (semester / course / task) is dropped as container: it describes what a session is in a repo that no longer exists, and its one durable clause - *"just-enough depth: enough to triage, not enough to work"* - is cluster D's depth rule, not this thing's.

**Container verdict: both, medium-high confidence.** I nearly dropped this whole thing and changed my mind at source. The reason: `§9.4`'s argument is not *"we have no protocol because we are one repo"*, it is *"there is no second party that might be asleep."* That is still true in the successor, where subagents are spawned by the conversation rather than living beside it. The literal phrase "never through a call" needs care - a Claude Code subagent does return a value to its parent - so the ADR says **state** is exchanged through the store and a return is a conclusion, which is what `§9.3`'s subagent contract already says.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 8 bears on it: the content layer and the time layer must be separate, and query-by-time-period is not ring 0's or the skeleton's responsibility - which is another instance of the same move, refusing to add a coordination mechanism for something the store can answer later.

**Cross-cluster.** `§9.3`'s responsibility table and the subagent return contract (*"subagents swallow the process and emit only conclusions"*) are cluster D's; this ADR depends on them. `§9.5`'s disposability criterion is cluster A's (M11) and carries the conversation-lifetime half of my brief's correction. The "reads all of it every time" premise is narrowed but not fatal (C86) and is cluster D's ring-0 territory.

**Zoomed.** Yes, `domain-design.md §5`, §8, §9.4, §9.5. **Changed my call** from `DROP` to `ADR`, on §9.4's reason.

---

## M108. Calendar goes to Notion; is Notion authority or projection

**Destination: `ADR`**

**Proposed title.** The calendar is a projection to an outside surface, not something this system renders.

**Tests.**

- *Hard to reverse* - **yes.** It is a scope boundary, and it has already removed a node kind from the model.
- *Surprising without context* - **yes.** A semester manager that will not show you a calendar is the first thing a reader will question.
- *Real trade-off* - **yes.** The alternative was owning the calendar rendering; it was rejected to keep one authority, because a writable second surface reproduces the two-sources-of-truth pathology.

**Body.** Calendar rendering leaves this system and lands on a calendar surface Billy already uses. **One authority - the facts layer - and many views**; a view that is also writable would put the deadline-moved-on-one-side pathology back in a new place. Which outside surface it is remains open, and so does whether that surface is ever built.

**The original justification is dropped and replaced.** `domain-design.md §1.8`'s ground was *"that removes the only human-facing rendering requirement from this repo"* - **false, and demonstrably so within a week** (C88): `model.md §2` defers which spine a view renders as a UX decision, `§7.2` rules a note renders with its summary, `§10.5` measures what rendering the course level costs in characters, and `architecture.md §5` makes rendering the presentation tier's entire content including *"every one-line summary"*. The boundary survives on a different and better ground, which is Billy's ruling 3: **calendar things belong on the calendar.**

**Container verdict: domain, high confidence.** Notion is Billy's own external tool, not openclaw furniture, and survives the container change untouched. What dies is the false premise, which was a claim about a repo.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** Ruling 3 directly and decisively: *"`time_point` is out because its reader, the calendar projection, is out - not because nothing reads it. Calendar things belong on the calendar."* That both reaffirms the boundary and puts the projection itself out of v1, which is why the target surface stays unnamed here.

**Cross-cluster.** `time_point`'s graveyarding is cluster C's and its reason is this ruling - they must not be written as independent. **A separate small `DEFER` may be warranted for "which outside calendar surface, and is the projection ever built", woken when the calendar projection re-enters scope**; I flag it rather than propose it, because the projection's scope is cluster A's boundary question. The "ruled by an unattributed agent doc one day after Billy deferred it" problem (C87) affects the Notion half only, and under merge rule 4 that document is weighed on content: two of its three bullets were reversed within five days, and only *"Notion is a projection"* still stands unchallenged.

**Zoomed.** Yes, `domain-design.md §1` ruling 8 and §7. No change to the facts; the replacement ground is Billy's ruling 3, not the record's.

---

## M109. Relationship to the existing PA db

**Destination: `DEFER`**

**Precondition that wakes it.** Billy's ruling 1: **v2, after the system proves useful and genuinely extensible.** v1's boundary is coursework inside academics, so there is no cross-domain surface for an obligation to project into. Wake when a cross-domain requirement re-enters - which is the same wake-up as `domain-design.md §0.6`'s offering-term/prereq requirement, and the two should wake together or not at all.

**What travels with the deferral, and what does not.** Travels: **an obligation is not a todo.** Todos are flat and cross-domain, carry no course, no source and no externally-driven status transitions; overloading them pollutes the cross-domain work-trace. And the shape of the eventual answer is already stated and matches M108's: **the academic layer is authoritative, the cross-domain surface is a view.** Does not travel: **PA itself.** The personal-assistant database is a system in the old container; the deferral is about whatever cross-domain surface exists at v2, not about that schema. `design.md §1`'s *"no `PA_SOURCE`"* constraint is therefore not a ruling to inherit, it is a note about a system that is gone.

**Container verdict: both, high confidence.** The distinction (an obligation is not a todo) is domain and durable. The integration target is old container and dies.

**Sequencing stripped.** None; the deferral is scope-conditioned, not order-conditioned.

**Touched by Billy's rulings.** Ruling 1, which supplies both the v1 exclusion and the v2 wake-up.

**Cross-cluster.** **Pairs with cluster A/C's `course.offering_term` and `course.prereq` deferral** - same ruling, same wake-up condition, and `domain-design.md §0.6` is the strongest statement in the corpus of why the boundary might be wider than one semester. If the two clusters write different wake-up conditions for the same v2, that is a reconciliation defect.

**Zoomed.** Yes, `domain-design.md §7`. No change.

---

## M110. Repo rituals - `/wrap`, `/promote`, manual markdown, `memory/calibration.md`

**Destination: `ADR`** - for one of the four items. The other three are old-container drops, named below.

**Proposed title.** Markdown notes are not the store.

**Tests.**

- *Hard to reverse* - **yes.** It is the reason there is a typed store, a schema and tooling at all rather than a folder of notes.
- *Surprising without context* - **yes, and especially here.** Every neighbouring project of Billy's runs on hand-maintained markdown records, including the repo this classification lives in. A reader will ask why this one does not.
- *Real trade-off* - **yes.** The cheap answer was available and rejected on a specific ground: the information granularity is too fine and too time-sensitive for a hand-maintained discipline.

**Body.** Manual markdown maintenance is out as the system of record: the information granularity is too fine and too time-sensitive for a `devlog/`-style discipline, and the failure mode is not that notes are wrong but that they are not updated on the day a deadline moves. **The store is typed and written by the system; markdown remains a fine medium for decisions about the system and a bad one for facts inside it.**

**The three old-container drops in this thing.**

1. **`/promote` as the schema-evolution gate.** It is a slash command in a repo that no longer exists, and two rulings lean on it as their escape valve (`domain-design.md §6`, `model.md §10.9`'s *"`/promote` promotes it if it recurs"`). What dies is the carrier. **What must survive is the mechanism, and it is not cluster F's**: schema evolution is gated on recurrence, not anticipated, and **only typed fields make migrations, so deferring a field decision is free** - which is what dissolves the over-determination worry. That belongs with cluster B/C's rigidity rule (M26). If cluster F drops this and cluster B/C does not pick the mechanism up, a load-bearing clause vanishes.
2. **`/wrap` as the capture-point ritual.** Same reason; the capture-point ruling itself is cluster E's (M95) and does not depend on the command existing.
3. **`memory/calibration.md`'s propose-then-confirm discipline.** A file in the old repo, cited only to say the discipline is too heavy at fall26's volume. The argument survives inside M111 and needs no carrier.

**Container verdict: mixed, high confidence per item.** The markdown ruling is domain (it is about the granularity of academic facts, not about a repo). All three rituals are pure old container - each is a command or file whose existence was assumed and whose successor equivalent is a live design question, not an inheritance (C89).

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine directly. Ruling 9's observation that onboarding is undefined - who does it and how information arrives - is the same class of question `/wrap` used to answer, and is where a successor capture ritual would be decided.

**Cross-cluster.** The `/promote` mechanism to cluster B/C (M26). The `/wrap` capture point to cluster E (M95). Flagged as **the highest-risk drop in my cluster**, because two live rulings name a dead command as their escape valve.

**Zoomed.** Yes, `domain-design.md §6` and §1 ruling 3. Changed: at source the `/promote` clause carries *"only typed fields make migrations, so deferring a decision is free"* and *"a tiny mechanical core plus everything else free, not vagueness everywhere"* - which is far more load-bearing than a ritual and is why the drop needs the hand-off above.

---

## M111. Preferences are a fact type, not a layer

**Destination: `DEFER`**

**Precondition that wakes it.** **A mechanism must read a preference.** That is the rigidity rule applied to its own case: a field earns typing if and only if some mechanism reads it, and today none does - `preference` is not a kind in slice 1 or slice 2 and appears nowhere in `records/spec/`. The concrete wake-up: when scope loading actually loads a per-course working-instruction bundle, the thing it loads needs a home, and this is it.

**Two things that must be re-checked when it wakes, and not assumed.** First, **the analogy it rests on has broken**: *"structurally identical to `progress`"* was written when `progress` was a fact type; `progress` has since moved out of the fact-type table into an annotation kind, and no record asks whether preferences follow (C90). Second, **the successor container supplies a preference store of its own** - an agent's own memory and instruction files - which is a genuinely new option the corpus never had, and it is the option the ruling most needs to weigh, because the whole argument here is *take the mechanism (passive extraction from conversation), reject the separate store*, and a container-native store is exactly a separate store wearing different clothes.

**What is not carried.** `domain-design.md §6`'s table already types a `preference` row and `§9.3` already assigns it a close-of-session extractor. **The corpus half-adopted an unruled draft**, and that half-adoption should not travel - under merge rule 3 a self-declared draft stays a draft.

**Container verdict: both, medium confidence.** The content (preferences are facts, not a layer; passive extraction beats a write discipline) is domain. The `memory/calibration.md` comparison it argues against is old container. And the successor container changes the option set, which is unusual - most of my cluster's container-sensitivity runs the other way, toward things dying.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine directly. Ruling 4's shape applies: proactivity is written too rigidly at present and should be designed when needed - passive extraction is proactivity, and the same "design it when it bites" posture fits.

**Cross-cluster.** Depends on cluster C's `progress`-as-annotation ruling (M51), which is what broke the analogy. The per-course working-instruction bundle is cited in cluster D's multiagent material (`§8`'s rejection of per-course expert agents) and in M107 above.

**Zoomed.** Yes, `domain-design.md §8` and the §6 table. No change to the facts; the container-supplies-a-store observation is mine and is flagged as such.

---

## M112. Method and apparatus - pre-registration, anti-cheat, the seal

**Destination: `ADR`**

**Proposed title.** Hypotheses are pre-registered and their evidence is kept.

**Tests.**

- *Hard to reverse* - **yes, and asymmetrically.** A result obtained without pre-registration cannot be retro-fitted with one, and a contaminated run cannot be uncontaminated. The seal's failure proves it: one agent *"saw the 2aa4 ground truth verbatim"*, and its induced partition stayed contaminated - the only remedy available was to establish that the leak could not have mattered for that particular grouping, not to undo it.
- *Surprising without context* - **yes.** A solo project running anti-cheat rules against its own agents, and refusing to adjust a threshold after seeing the data, looks like ceremony until you see what it caught.
- *Real trade-off* - **yes.** Judging after the run is faster and was available; it was rejected because the second cycle had no external adjudicator, so *"everything it produces is an assertion until W1/W2 test it."*

**Body.** Sampling rules, verdict thresholds and which judgments are admitted as judgment calls are written **before** any file content is opened, and are not adjusted afterwards; **ambiguous judgments resolve against the proposition.** Raw artifacts are kept, because a conclusion whose evidence was deleted is not auditable, and design vocabulary is kept out of raw passes - having the word available is enough to start hallucinating instances. **Preserve what cannot be reconstructed; record the recipe for what can.**

**Shape riding inside.** The one correction the apparatus has already earned: **copies, never symlinks, and strip document metadata** - the seal was built from symlinks and `ls -la` prints symlink targets, so the first command a shell-using agent naturally runs defeats it.

**Container verdict: neither domain nor container - it is method, high confidence.** This is the corpus's own verdict on itself and it holds. The successor container inherits it for free and, unusually, gains from it: the discipline is what makes agent-produced findings in a new repo worth anything.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** **Ruling 9 is this method being applied.** Structure-only reading of 2px3 was rejected because *"when the instrument cannot reflect the ideal case, its result is untrustworthy"* - that is ambiguity-resolves-against-the-proposition, six days later, on a live question.

**Cross-cluster.** `write-rules.md`'s 08-28 method statement is the same discipline in the other repo (*abstract rule-writing "stalled for two months"; the rules came from Billy editing one course's records by hand, so the rule is what he did and the before-and-after is the evidence*) and belongs to **cluster E**. If cluster E carries that, the two are one ADR. **Also flag:** this may belong in `docs/agents/` or a skill rather than `docs/adr/`, since it governs how sittings run rather than what the system is. I propose ADR because it is a constraint not visible in the code, but I would not argue against the other home.

**Zoomed.** No - the inventory's account is dense with verbatim quotes from `step-minus-1/TASK.md`, `derivation/TASK.md`, `BRIEF.md` and `README.md`, and nothing in it turns on interpretation.

---

## M113. Sequencing - fall26 first, the template afterwards

**Destination: `ADR`**

**Proposed title.** Build the instance; the general contract is whatever survives generalization.

**Tests.**

- *Hard to reverse* - **yes.** Designing the general contract first is a different codebase, and the record names the specific failure it avoids: cloning three build-repo instances outward.
- *Surprising without context* - **yes, and the telos is what makes it surprising.** The stated goal is *"every aspect of Billy's life managed under one contract"*, so the obvious move is to derive the contract first. This does the opposite on purpose.
- *Real trade-off* - **yes.** Generalizing up front buys reuse and costs a contract fitted to nothing; generalizing afterwards costs a rewrite of whatever did not survive.

**Body.** The instance comes first and forces the template: this design **is** the general work, and the contract is whatever survives generalization afterwards, not something derived up front. Do not clone outward from existing instances. The same posture applies inside the system, at a smaller scale, wherever a second case is tempting before the first one renders.

**Container verdict: both, high confidence.** B-layer, dispatch and build-repo instances are old-container structure and are stripped from the wording. **The posture is domain-independent and the successor already runs on it** - this repo exists because one instance was built and is now being generalized, which is the ruling executing itself.

**Sequencing stripped.** **Yes, and deliberately.** The second half of this thing - `architecture.md §4`'s *"do not extract more courses before the presentation tier exists"* - is a build-order gate and is carried as **M102's deferral precondition**, not as part of this ADR. The v1/v2 ordering under Billy's ruling 1 is likewise a scope condition carried by M109 and by cluster A, not an ordering carried here. What is left in this ADR is the posture only.

**Touched by Billy's rulings.** Ruling 1 restates it at the current scale: v1's boundary is coursework inside academics, and the cross-domain requirement is **deferred to v2, after the system proves useful and genuinely extensible** - which is *"the template is whatever survives generalization afterwards"*, applied to the successor's own scope question.

**Cross-cluster.** Cluster A owns the goal function and the `§0.6` cross-domain requirement; this ADR is the posture that makes deferring `§0.6` coherent rather than an abandonment. M109 shares its wake-up.

**Zoomed.** Yes, `domain-design.md §0.1` and §1 ruling 1. No change.

---

## M114. Scale is out of scope

**Destination: `DROP`**

**Which kind.** Both **exposition** and **old container**. As exposition: it is a scoping preamble that discards work rather than deciding anything, and it fails two of the three ADR tests outright - a solo personal tool having no horizontal-scaling requirement is not surprising, and nothing was traded away to reach it. As old container: the premise it rests on is *"one user, one machine, **one session at a time**"*, which was true because a person sat at a CLI and ran one thing. **That is precisely the assumption the successor puts in question** - a Claude Code conversation spawns subagents, and more than one process can be live at once. The record states it as a discard with no falsifier attached, which is the shape that makes it unsafe to inherit.

**The one live residue, and where it goes.** `design.md §5` lists **"writers: one"** among the facts that decide the no-database conclusion. That fact is still true, but in the successor it is true **by design rule rather than by container**: `§9.3`'s subagent contract gives subagents no fact writes, and `§5` says subagents return conclusions. So single-writer now depends on a rule someone could relax without noticing. **I propose adding "a second concurrent writer" to M103's overturning conditions**, where it sits beside multi-device sync, rather than keeping M114 alive to hold it.

**Container verdict: old container, high confidence** - with the caveat that its conclusion (no failover, no horizontal scaling, no load estimation) remains trivially true and loses nothing by being dropped. Only the premise is dangerous, and only because it is load-bearing one record away.

**Sequencing stripped.** None.

**Touched by Billy's rulings.** None of the nine.

**Cross-cluster.** The single-writer flag goes to whoever carries M103 (cluster F, me) and to cluster D, which owns the subagent return contract that now guarantees it.

**Zoomed.** Yes, `design.md` header and §5's facts table. **Changed my call**: the header alone reads as harmless scoping; the "writers: one" row in §5 is what makes it worth a paragraph in the drop reason.

---

## Summary

**Counts.**

| destination | count | things |
|---|---|---|
| `CONTEXT` | **0** | - |
| `ADR` | **13** | M97, M98, M100, M101, M103, M104, M105, M106, M107, M108, M110, M112, M113 |
| `DEFER` | **4** | M99, M102, M109, M111 |
| `DROP` | **1** | M114 |

**Zero `CONTEXT` terms, and that is the expected result.** Tiers, TypeScript, JSONL, packaging, sessions and transports are general engineering vocabulary, not project-specific domain terms. The only candidates I weighed were "presentation tier" and "the store is the channel", and both are decisions rather than nouns a newcomer needs defined. Every genuinely project-specific noun in this corpus - ring 0, the skeleton, the store, an obligation, an annotation - lives in another cluster.

**Old-container deaths: 1 whole thing plus 6 named sub-drops.** M114 dies whole. Inside surviving things: M99's *"the MCP adapter may never be built"*; M100's *"the surface is a CLI"*; M101's two-branch render rule; M107's Fairy vocabulary and the three-scope session table; M108's *"the only human-facing rendering requirement"* premise; M110's `/promote`, `/wrap` and `memory/calibration.md`; M109's PA database as the integration target. **The pattern: in this cluster the container almost never kills a ruling - it kills the ruling's carrier, its vocabulary, or its justification, and the ruling itself is repaired and carried.** M100 and M101 are the clearest cases, and M100 anticipated its own repair in writing.

**Why the ADR count is high and where I would cut first.** The brief predicted this cluster would be both the richest ADR source and the biggest graveyard; it turned out to be much more the former. Three ADRs are the ones to demote if the reconciliation wants fewer: **M98** (strong merge candidate with M97 - they are one decision seen twice), **M105** (weak on hard-to-reverse; reads naturally as a rider on M104), **M112** (may belong in `docs/agents/` or a skill rather than `docs/adr/`).

**Least sure.**

1. **M107** - I had it as a drop until I read `§9.4` at source. The whole thing is phrased in dead vocabulary, and the surviving argument is one sentence: *"there is no second party that might be asleep."* If that sentence is judged to be about a repo rather than about the system, the ADR goes away.
2. **M110** - a defensible ADR wrapped around three drops, one of which (`/promote`) is the escape valve two live rulings in another cluster depend on. If cluster B/C does not pick up the recurrence-gate mechanism, this drop loses something real.
3. **M112** - I am confident it survives; I am not confident `docs/adr/` is where it belongs.

**Every cross-cluster flag, in one list.**

1. **M97 / M98** merge with each other; both reach cluster B (trigger D, the purity cut) and cluster C (construction as the only gate).
2. **M98 consequence 1** belongs to **cluster E** (write rules) and must carry the 08-28 correction: the absolute phrasing was withdrawn, the real distinction is the direction a rule is derived from.
3. **M98 consequence 3**'s ask-design half belongs to **cluster D/E**'s asking thread, re-ruled by Billy's rulings 2, 4 and 7.
4. **M99**'s "write rules precede the presentation tier" depends on **cluster E**; its two evaluations will collide with **cluster A/D** on acceptance criteria.
5. **M102**: **cluster C's graveyard counts (M62) are all stated over 22.** The correct figure is 14 for 2c03, and 22 is not reachable by re-running the old route. This is the most concrete cross-cluster error risk in my set.
6. **M103**: the pgvector/PostgreSQL PASS belongs to the store and to **cluster B/E**; it does not conflict, and only `design.md §5` says why.
7. **M104**: `design.md §1`'s stale constraint line (*"directly-callable Python, no MCP, no Postgres, no `PA_SOURCE`"*) must not be inherited by anyone.
8. **M106** will very likely be proposed by **cluster C** as well (`schema.md §8`); if so, cluster F carries nothing there.
9. **M101** is one half of **cluster C's** opaque-`id` decision; do not write them as independent ADRs.
10. **M107** depends on **cluster D's** subagent responsibility table and return contract; `§9.5`'s disposability criterion is **cluster A's** M11.
11. **M108**: `time_point`'s graveyarding (**cluster C**) has this ruling as its reason. A small `DEFER` for "which outside calendar surface, and is the projection ever built" may be warranted; its scope question is **cluster A's**.
12. **M109** shares a wake-up condition with **cluster A/C's** `course.offering_term` / `course.prereq` v2 deferral. Different wake-up wordings for the same v2 would be a reconciliation defect.
13. **M110**: the `/promote` recurrence gate hands off to **cluster B/C's** rigidity rule (M26); `/wrap`'s capture point hands off to **cluster E** (M95).
14. **M111** depends on **cluster C's** `progress`-as-annotation ruling (M51), which is what broke its analogy.
15. **M112** is the same discipline as `write-rules.md`'s 08-28 method statement, which is **cluster E's**; one ADR may cover both.
16. **M114**: add **"a second concurrent writer"** to M103's overturning conditions, and note to **cluster D** that single-writer is now guaranteed by the subagent contract rather than by the container.
