# Semester Manager

A knowledge base over five concurrent courses, modelled so that what is owed, what each obligation requires you to know, and where the material that teaches it lives are all answerable without reloading five courses' context by hand. It is packaged as a set of components an agent uses, not as an app a person operates.

The names below are the **engineering** names. The product-facing verb names are undecided, and obviously cannot be `ring 0` and `skeleton`.

## Language

### The two persisted things

**skeleton**:
The graph of nodes and links: what exists, how it relates, and a handle to content. One of the two persisted things.
_Avoid_: facts layer · compartment · *the graph* (bare) · *skeleton kinds* meaning the three layered kinds

**store**:
Materialized artifact content - chunks and embeddings - addressed either by a node handle or by similarity. It holds semantic, decontextualized facts about course materials, and is the other persisted thing.
_Avoid_: corpus layer · the corpus · *RAG store* (names only the by-query half) · `Store` as an interface name

### Nodes, links and pointers

**node**:
A record with a `kind`, an id in the single id space, and that kind's declared field set; anything that can be an endpoint of a link.
_Avoid_: entity · *record* used interchangeably

**link**:
A typed, directed relation between two refs, stored as its own record rather than as a field on either end.
_Avoid_: edge

**link kind**:
The named, signature-constrained relation type a link carries. The set is closed.
_Avoid_: edge type · relation type

**id**:
An opaque, monotone value assigned by the system from one id space shared by every kind that can be a link endpoint. It says nothing about the record it names, is never reused, and is obtained only by reading it back.
_Avoid_: key · slug · *handle* used for the stored value · any id derived from a name

**Ref**:
A pointer to a node: its kind plus its id, drawn from the one id space. It may name something that does not exist.
_Avoid_: *foreign key* (it is explicitly not one) · *pointer* as the noun

**handle**:
What a render carries so the level below stays reachable. The `id` is what the store holds; the handle is what a surface prints or resolves.
_Avoid_: using *handle* and *id* interchangeably · a handle that appears in one render branch and not another

**locator**:
The fragment a link points into - a section, a page, a method, a question - held verbatim as the source string.
_Avoid_: citation · fragment · anchor

**closure**:
The set of nodes reachable from one node by following one link kind transitively. It is single-source, and it is never an all-pairs matrix.
_Avoid_: *transitive closure* as a matrix · *reachability* used for the one-hop walk

### The two axes

**kind**:
The named record schema a node's payload conforms to, carried on the node as a required discriminator whose value is the kind's own name. Current set: `course` · `obligation` · `sticky_note` · `progress` · `concept` · `artifact`.
_Avoid_: type · node type · layer · metadata

**layer**:
One of the three strata of the domain graph - `obligation`, `concept`, `artifact`. Only those three kinds have one.
_Avoid_: *skeleton kinds*, say **layered kinds** (`course` and `sticky_note` are also nodes in the skeleton) · *layer* for the coarse content-versus-time split, which is **the skeleton** versus **the time projection** · *layer* used for `kind` · content layer · time layer

### The kinds

**course**:
A kind, and a node: the unit a term's obligations are owed to. Its id is the supplied course code rather than an assigned one, because the source issues a canonical unique one.
_Avoid_: namespace · scope · treating it as a container rather than a node

**obligation**:
A thing with a deadline. The only layer that carries time, and the same nodes ring 0 is a projection of.
_Avoid_: task · assignment · *deadline* as the noun

**concept**:
A unit of subject matter the course teaches, independently addressable.
_Avoid_: topic · "a thing the student understands or does not" (retracted)

**artifact**:
A thing the course delivers and that is opened independently.
_Avoid_: file · document · resource · "a thing that exists on disk" (falsified)

**annotation**:
A node kind whose record is a single dated claim about another node, reached by an `about` link rather than by a field. A tag over `sticky_note` and `progress`, not a type hierarchy.
_Avoid_: *note* used for both kinds · metadata · treating it as a supertype with subtypes

**sticky_note**:
An annotation carrying one free-text statement about its target, with an open category and a recorded origin. It points at a node rather than being a property of one, so attaching, modifying and detaching are cheap.
_Avoid_: *note* (bare) · comment · correction layer · corpus override

**progress**:
An annotation stating how far along its target's work is, carrying a state and a prose detail. A target with no progress record reads as `not_started`.
_Avoid_: *status* - `obligation.status` is dead and `progress.state` is live; the two are not the same word · completion · mastery · a `sticky_note.category` value

### Fields that carried several names

**name**:
The short label a person recognises a record by, held exactly as the source prints it. It is not the handle, and nothing is derived from it.
_Avoid_: label · title · description

**due**:
The moment an obligation is anchored to - the deadline for something handed in, the start for a sitting. A date without a time is the **end** of that day, `23:59`.
_Avoid_: *deadline* as the field name · date · assuming a date-only value is the start of the day

**done_by**:
The date the owner chose to have an obligation finished by. A stored value always means it was chosen; nothing computes one.
_Avoid_: target_date · finished_by · rendering it as a *start* date

**grade_share**:
The approximate share of the final course grade an obligation carries, in percent, held for a person to read and never as an input to a computed ranking.
_Avoid_: weight · worth_percent · reading a column of shares as a partition of 100

**parts**:
The concepts an obligation's source carries, as raw strings written in canonical singular form, kept only where a concept might recur elsewhere. It carries no size, no status and no score.
_Avoid_: sub-items · components · treating the strings as pointers to concept nodes · using it to judge how much work something is

**origin**:
How an annotation came to exist - an announcement, someone saying so, or the system having asked. One field with one name across both annotation kinds, and it does not confer immutability.
_Avoid_: source · *provenance* as the field name · a second copy per kind

### Two link kinds that need distinguishing by name

**covers**:
The relation asserting that an artifact teaches a concept as its subject. It is the rendered relation.
_Avoid_: using `covers` for a mention - full-text finds mention, title-scoped finds coverage

**applies**:
The relation asserting that an artifact uses a concept without teaching it. It feeds closure and is never rendered.
_Avoid_: uses · *mentions* (that name belonged to the cut announcement link)

### The store's vocabulary

**materialization**:
The one-time pass turning an artifact's raw content into stored readable form - normalize, chunk, summarize, tag. Paid once, and it happens whether or not anything is embedded.
_Avoid_: ingestion (retired as a word of this project) · indexing · embedding

**chunk**:
A unit of an artifact's materialized content, held in the store against the node it belongs to.
_Avoid_: *chunk* meaning a course's coarse grouping, such as a week or a module

**by-handle**:
The store access mode that fetches the chunks a known node points at. Deterministic, no similarity.
_Avoid_: JOIN mode · direct read

**by-query**:
The store access mode that searches by similarity when you do not know where to go. The only half of the store that is RAG.
_Avoid_: *RAG* used for the whole store · search

### The two written objects

**summary**:
A written one-line object carried only by a node whose identity is content the skeleton does not hold; in the current kind set, the `artifact` alone.
_Avoid_: node summary · concise summary

**materialized summary**:
The per-artifact summary the materialization pass produces. It lives in the store and the coordinator never sees it, which makes it a different object from `summary`.
_Avoid_: calling it `summary` unqualified

### Residency and the read path

**ring 0**:
The obligation layer under a residency policy: the fixed-shape, uniform-depth set of obligation fields the coordinator holds in its conversation context so it can tell where to look next. It governs **residency, not readability**, is field-grained rather than node-grained, and is not a third persisted thing.
_Avoid_: *the projection* (bare) · *the obligation layer* as a synonym · the resident projection · ring 0 meaning what is **observable** · ring 0 meaning what is **readable**

**band A** / **band B**:
The two halves of ring 0's partition. **Band A, "active"**, is any obligation triggered by a near `due`, by a near `done_by`, or by work already in progress; **band B, "known"**, is everything else, including obligations with no date.
_Avoid_: *the active window* for band A - the window is one of three triggers, not the partition · urgent / backlog

**coordinator**:
The single long-running agent conversation the owner talks to: it holds ring 0, dispatches, walks the graph and writes the plan. A **conversation**, not a process - its scale is days to weeks, and **resident** means held in the conversation's context, never in a process's memory.
_Avoid_: master session · *the agent* (bare) · orchestrator · "the coordinator's lifetime" without saying which one

**the walk**:
The operation that follows a node's edges and reads its neighbours' definitions. Deterministic, and it touches neither the store nor embeddings.
_Avoid_: search · find_material · retrieval · treating the walk and a by-query store read as one operation

**dispatch**:
Sending a question out of the coordinator's context - to a subagent, a task session, or the owner himself - and receiving back a value in the same shape as every peer's. The context that produced the value stays outside.
_Avoid_: delegate · spawn · *ask* - asking the owner is one case of dispatch, not a different mechanism

### The inbound path

**extraction**:
The pass that reads delivered material and produces candidate facts. It changes with the material.
_Avoid_: ingestion · parsing · using it for what happens to the candidates afterwards

**candidate fact**:
A fact extracted from source material but not yet landed, carrying none of the system timestamps that landing assigns.
_Avoid_: extraction output · pre-landing record · staged fact

**landing**:
The write of candidate facts into the skeleton. It is idempotent, it detects conflicts instead of overwriting, and it changes with the schema.
_Avoid_: ingestion · import · `land()` as the name of the concern rather than of one operation

**conflict**:
Two statements the system holds that cannot both be true of the same thing. It is shallow or deep by what is in conflict, and that is what decides whether the agent may close it itself.
_Avoid_: *contradiction* used interchangeably · using it for a mismatch between system and world, which is **staleness** · using it for a progress claim, which is an authorship question

### Rules that are terms

**the rigidity rule**:
The test for whether a field exists: a field is typed if and only if some mechanism reads it. It admits **declared exemptions** (`grade_share`, `added_at`) and is not absolute.
_Avoid_: the typing rule · rigidity follows importance · stating it without the exemption clause

**the non-overlap rule**:
The rule that every field and every verb has exactly one purpose. It is the authority under which a field is deleted and under which two fields are merged.
_Avoid_: single responsibility · the disjointness rule · stating it as a style preference

**the render test**:
The test for whether a note is worth writing: *is it worth being written down so that every time I look at this node, the note comes with it?*
_Avoid_: the note rule · the usefulness test · stating it as *is this true and relevant*

**the write rule**:
An instruction to whoever produces a value for a field whose legal values cannot be enumerated. It is derived from what has to be true for the node to **render well**, never from what a source document happens to say.
_Avoid_: the withdrawn absolute "a write rule never refers to the source" · *validation* - a write rule is enforced nowhere · schema rule

**the graveyard**:
The section of the field-set record listing removed fields with the reason each was removed, under a standing rule that no later session restores one without a new ruling. Its rulings bind; its arithmetic does not.
_Avoid_: deprecated fields · the exclusion list · *deliberately absent* as the section's name in prose

### The project's own words

**faithfulness**:
The system's promise about its own claims, on three axes: every claim traces to a fact the system holds, no relevant held fact is omitted, and nothing is invented. Each holder answers for what it holds, so a negative answer names the boundary it speaks for; the promise is never one of coverage of the world.
_Avoid_: the trust clause · verification · accuracy · *precision and recall* - that framing is voided in place · *a promise of complete recall* - recall is one axis, not the term · a bare "it is not known"

**reload**:
The full reconstruction of a course's context a person performs in order to *interpret* one notice rather than merely read it. Five concurrent courses is five reloads, and collapsing them is what the system exists to do.
_Avoid_: context switch · catching up · treating it as a retrieval problem

### Words for the project's own decisions and methods

**dissolved item**:
A parked question that ceased to exist because a ruling elsewhere removed the condition that created it, as distinct from one that was answered.
_Avoid_: closed item · retired item · obsoleted question

**repair method**:
An operation that exists to correct a mistake - a retarget, a delete, a re-land - as opposed to one that advances a success path.
_Avoid_: corrective operation · recovery method · maintenance method
