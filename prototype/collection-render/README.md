# #80 prototype - how a render structures a collection of nodes

**Throwaway. Not a design, not a fixture, not evidence.** Built for [#80](https://github.com/Billy423/semester-manager/issues/80) on the branch `prototype/80-collection-render`. Nothing here is ported; what survives of it is whatever lands as ADRs.

## The question, and why a prototype

`0082` derives a node's render from its kind's field table by four rules, and says of itself that those rules *"do not reach a collection at all"*. `<parts>`, `<annotations>` and `<links>` are three containers no rule produces. #80 asks how a set of nodes becomes a render: how many sections, each section's depth, ordering, headers.

`0040`'s precedent is that a render is worth building when the defect is **emergent** - visible only when real strings meet a real shape. Honestly assessed, only one finding here needed the render: **the cost of structure on a resident view**. The rest were reached by argument against the records, the way #60 was. The renders still earned their place by making the arguments arrive early, but the ticket's own case for the method was only half right.

## Run

```bash
python3 settled.py      # the render as it stands after #80's rulings
python3 render.py       # the rejected variants, kept as a record of what was seen
```

No dependencies. Both read the real 2c03 fixture from the frozen `fall26` checkout by absolute path.

## Material

| | what |
|---|---|
| **real** | 2c03: 14 obligations, 11 sticky notes, from `fall26:app/tests/fixtures/2c03.json` |
| **made up** | every `progress` record, four `builds-on` edges, every timestamp. Ruled admissible by Billy: this ticket looks at the render, not at whether the state is true of the world. Without them `state`, the neighbour section and `updated-at` are not exercised at all |
| **derived** | `2aa4`, `2px3`, `2fa3`, `3mi3` and all their rows. **Shape only** - per `0077` a derived fixture is code, not evidence, so **no count from them may enter the answer** |

`AS_OF = 2026-02-09`, because winter-2026 is a past term. The band window is **not** a free parameter: `0042` rules it as `[today-7d, today+14d]`.

## Files

| | |
|---|---|
| `settled.py` | the render as it stands. Reads a kind's field table and emits the block and the line, so a kind added later is run through it rather than designed |
| `settled-output.txt` | its output over `course`, `obligation` and `sticky_note` |
| `corpus.py` | the material, real and made-up, labelled in place |
| `render.py`, `variants.txt`, `BANNER.txt` | the rejected variants. **Superseded** - `BANNER.txt` lists what each shows that was ruled against. Kept for the reason `fall26:evidence/2026-08-28-ring-0` kept its own rejected table: the rejections were reached by looking at it |
| `vocabulary-audit.md` | every element name, attribute name and enum value in the render, against `0093`'s two mechanically testable criteria |

## What the prototype settled

**Sections are cut by source, and `0046` alone makes the cut.** *"must deliver `sticky_note` and `progress` through their own channel, never as ordinary neighbours"* separates annotations from the node's own fields **and** from neighbours. `0045` is **not** cited: it is a data-flow rule about what enters the coordinator's context - *"the coordinator sees what a node IS; it never sees what a node SAYS"*, **a node**, not someone about it - and its own text says that using it for what the coordinator may **do** is the error it corrects. Each section then takes its own depth: own fields in full (`0038`), annotations in full text (an annotation has no identity apart from its target, so it is not depth), neighbours one line (`0060`, one level deeper is one more call). `0043`'s discard is enforced by that shape rather than by discipline - the only unbounded thing in a return is the node itself.

**A composed batch is a fourth source, which closes the hole `0084` left.** `0084` rules that a course composes `obligations.list(course)` but never says where that batch lands. It is not the node, it is not something said about the node, and `0084` says it is reached by **no edge** - so by the same rule that gave annotations their own channel, it gets its own section.

**A tag carrying an `id` is an addressable object; a tag without one is a field.** `<course id="2c03"/>` versus `<grade-share conditional="true">10</grade-share>`. `0082` rule 2 only half-covered this: a Ref is an element, but so is `<parts>`, which is no object. The id is the marker, not the element name, and it also tells the coordinator which things can be passed to `look_at`.

**Spelling is a separate rule: every name the coordinator can name back keeps the schema's own spelling** - kind discriminators into `land()`, field names into `set`, link types into `attach`, enum values into both. Words the render invents and nobody writes back are free. This is what lets `<edge>` stand while `<sticky_note>` keeps its underscore; *an id-carrying tag takes the schema spelling* cannot, because `<edge>` carries an id and the schema calls the record `Link`.

**An open/close pair carries content.** A pointer and a projection are not content, so the neighbour line is self-closing and what it was carrying moves onto the edge.

**The line is one field set, not two.** `0082` says obligation's line is *"ring 0's band plus `has-more`"*; band A already carries `has-more`, so *the band* means band B. A per-row band would import `0038`'s **residency** computation into a **read**.

**`has-more` is absorbed.** It is the projection of a node's edges onto their kinds, and `<neighbours>` strictly contains it, so carrying both collides with `0024`. It survives only where neighbours cannot be listed - which is ring 0, and travels there.

**Naming**, in `vocabulary-audit.md`: `<links>`/`<link>` become `<neighbours>`/`<edge>`; `kind` and `<glance>` disappear because the element name is the kind; `direction` says `points-at`/`pointed-by`; a Ref-typed field carries `id`, not `ref`; an edge's type is `type`, because `0012` gives `spec` a `role` of given/owed.

## What it did not settle

**Hole 1 - the line is not derivable.** obligation's line is a **transfer** from `0038`'s residency field set; course's is all four fields because it has four. No rule generates a new kind's line. The criterion is clear (*is this worth one `look_at`*); the field set is one ruling per kind, and `artifact` and `concept` will each need one.

**Hole 4 - `0082` is a placement rule, not a selection rule.** The four rules say where a field lands, never which fields enter, and #60 waved selection through with *"every other field"*. Excluding `added_at` while keeping `created_at`/`updated_at` is the first cut against that, and it had to be argued rather than derived.

**Ring 0.** Carved out during this ticket: ring 0 is not a node, and a live proposal to make it a parameterised query rather than a fixed resident projection would redraw what the band even is. It carries its own ticket, along with the band's representation and `has-more`'s final name.

**The schema's own spelling.** `progress.state` is `not_started` while `0012`'s link kinds are `builds-on` - both written back, spelled two ways. The render mirrors that inconsistency rather than creating it, which is correct under the rule above and still worth normalising at source. Renaming the schema's fields and `CONTEXT.md`'s terms is its own effort, cheap only because the schema has not entered this repo yet.
