# Five criteria for a name at the agent-facing surface, and the names they produced

A product-facing name is not a label chosen by taste. Five criteria bind it, and a name that fails one is rejected on that ground rather than argued about.

1. **It must not collide with the sense of a `CONTEXT.md` term.** `layer` and `skeleton kinds` are the two collisions the glossary already had to rule.
2. **It must not be the internal structure's name.** Billy, 2026-08-28. The verbs may not be called `ring 0` or `skeleton`.
3. **The name itself must route** (`0024`). `0060`'s failure mode is an agent deciding which verb applies by reading descriptions, so two names whose purposes overlap re-create it.
4. **The question the name asks must be the question the value answers.**
5. **A name must not present a mutating operation as a query.**

**Criterion 4 makes naming an audit of the shape rather than a labelling pass**, and it earned its place by working: `has-more="about"` asks yes-or-no and answers with an enum, and pursuing that mismatch is what exposed that a collection's render was never derived at all. `0073` is the same move one layer over - a write rule that cannot be said in a docstring is not finished - form constraining content.

**Criterion 5 exists because criterion 4 did not catch `refresh()`.** `whats_changed()` satisfies 4 exactly, and it names a view-mutating call as though it were a query.

## Ring 0 gets no product-facing name

The ban in criterion 2 bites in fewer places than it looks, because the surface never needs the noun: the resident view's initial load is injected rather than requested, the refresh verb is named by what it does, and band A and band B are ordinary words. Inventing a product term for ring 0 would add a glossary entry for a thing the coordinator **holds** and never **refers to**. `0068` also argues against coining it before there is an instance that needs it.

## The names

| | |
|---|---|
| `look_at(id)` | kept. Already the corpus's word at `0082`, `0084` and `0085`; collides with nothing |
| `refresh()` | the resident view's refresh. See `0089` |
| `land(...)` | kept. `CONTEXT.md`'s `landing` entry avoids `land()` only as the name of the **concern**, which endorses it as the name of one operation |
| `set` · `attach` · `detach` · `delete` · `create` | the second-order primitives. `attach` and `detach` are the `sticky_note` entry's own words; `delete` is `repair method`'s; `0059` consequence 2 forbids auto-**add**, not `create` |
| `id` | the read parameter. An id is unique across the one id space; `handle` names no distinction the surface can act on |
| ~~`<glance>`~~ | **retired at #80.** It was a neighbour's render, pairing with `look_at`. `0082`'s own first clause makes the element name the kind, so a neighbour is `<obligation …/>`, and `0096` gives the relation itself `<neighbours>` / `<edge>` |
| `<neighbours>` · `<edge>` | the neighbourhood and one relation in it. `<links>` failed criterion 2 - `link` is `CONTEXT.md`'s name for the internal record. An edge carries `id`, `type` and `direction`; `type` rather than `role`, because `0012` gives `spec` a `role ∈ {given, owed}` |

**`attach` stays a primitive although only annotations use it today.** The primitive set is defined against the kind set that will exist, not against the one use case that exists; the alternative, folding the `about` link into annotation creation, would have to be undone the moment a second link kind acquires a writer.

## Rejected names

| | |
|---|---|
| `whats_changed()` | criterion 5 |
| `sync()` | `0005`: the store is never synchronised against a source |
| `catch_up()` | `CONTEXT.md`'s `reload` entry avoids *catching up* |
| `handle` as the parameter | names no distinction at the surface |
| `<ref>` for a neighbour | `0082` itself admits *"two `ref` forms, because they do two jobs"*, which is criterion 3, and it collides with the `Ref` term |
| `<line>` | the `the line` entry avoids reading *line* as a physical line of output |
| `link-kinds` as an attribute name | `link` and `kind` are schema-internal words, and criterion 2's spirit reaches them: an agent that has not been taught the schema cannot read the name |
| `attention` for the band | a binary partition dressed as an enum: one compressed noun over two values that do not explain themselves |
| `status` / `state` for the band | `CONTEXT.md`'s `progress` entry records `obligation.status` as dead, and `state` is already taken on the same row |

## Repairs this record owes

`<glance>` contradicted two landed records, which named the neighbour element `<ref>` verbatim: `0082`'s *"A **neighbour** arrives as `<ref>`"* and `CONTEXT.md`'s `the line` entry, *"one self-closing `<ref>`"*. Both were repaired at source rather than bannered, per `0084`'s precedent. **#80 then retired `<glance>` itself** and repaired the same two records again, plus `0089` and this table - the second rename in four days, and the reason is that criterion 4's audit reached the element only after `0092` made `has-more` set-valued.

`id` narrows `CONTEXT.md`'s `handle` entry, which defines a handle as what a surface prints or resolves. At the surface the two coincide, and `0061` is amended to say so rather than to leave *"every read must return their handles"* reading as though a second kind of value existed.

Source: ruled at #62 (Billy, 2026-09-02). Criterion 2 is Billy's 2026-08-28 ruling, carried at #62's body.
