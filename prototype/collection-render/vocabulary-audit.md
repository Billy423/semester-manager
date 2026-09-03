# What the render shows a reader, audited term by term

Every element name, attribute name and enum value that appears in the rendered output, against `0093`'s two testable criteria:

- **C1** - must not collide with the **sense** of a `CONTEXT.md` term (reuse at the same sense is fine; the failure is one word, two senses)
- **C2** - must not be the internal structure's name

Verdicts are `ok` / `RENAME` / `RULE` (nobody has decided whether it renders at all).

## Element names

| shown | verdict | ground |
|---|---|---|
| `<obligation>` `<course>` `<progress>` `<sticky_note>` | ok | domain nouns, and `0082` makes the element name the kind |
| `<annotations>` | ok | `0046`'s own channel; a reader gets it without the schema |
| `<parts>` `<part>` | ok | `0033`'s domain word |
| `<grade_share>` | ok | `CONTEXT.md`'s own field name, domain-side |
| `<links>` | **RENAME → `<neighbours>`** | `link` is a `CONTEXT.md` term for the internal record (C2). The graph word names the same thing from the reader's side |
| `<link>` | **RENAME → `<edge>`** | same. `CONTEXT.md`'s `link` is *"a typed, directed relation between two refs, stored as its own record"* - which is an edge, with an id at birth |
| `<glance>` | **RULE** | `0093` ruled it as *a neighbour's render*, pairing with `look_at`. Under `<edge>` the thing inside is the neighbour node itself, and `0082`'s first clause says **the element name is the kind** - so `<obligation .../>` self-closing would carry it and `kind=` would disappear from the render entirely. Not decided here |

## Attribute names

| shown | verdict | ground |
|---|---|---|
| `id` `name` `due` `done_by` `term` `optional` `category` `state` | ok | same sense as `CONTEXT.md`'s |
| `conditional` | ok | `0032`'s marker, reads as English |
| `kind` | **RENAME** | `CONTEXT.md`: *"The named record schema a node's payload conforms to, carried on the node as a required discriminator"* - the internal structure's word (C2). It also appears twice in one render at two senses: `<glance kind="obligation">` is a node's kind, `<link kind="builds-on">` is an edge's type (C1) |
| `ref` | **RENAME** | `0093` already rejected `<ref>` as an element because it *"collides with the `Ref` term"*. The same collision as an attribute |
| `direction` | **RULE** | `in`/`out` relative to what is stated nowhere. Either the values say it (`points-at` / `pointed-at-by`) or the render is ambiguous |
| `origin` | ok | `CONTEXT.md`'s own field, one name across both annotation kinds |
| `added_at` `created_at` `updated_at` | **RULE** | `0028` rules they exist; **nothing rules they render.** `0082` sends every other atomic scalar to an attribute with no usefulness filter, so by the rule they appear - and PR #69's sample silently omitted `added_at`. They also decide nothing a coordinator routes on |

## Enum values

| shown | verdict | ground |
|---|---|---|
| `about` `builds-on` | ok | `0012`'s closed table; both read as English from the edge's own direction |
| `not_started` `in_progress` `done` | ok | readable |
| `policy` `clarification` `logistics` `correction` | ok | `0036` leaves the category open; these are the corpus's own |
| `announcement` `course-outline` `owner` | ok | `CONTEXT.md`'s `origin` entry names these |
| `given` / `owed` | **not yet shown** | `0012` gives `spec` a `role ∈ {given, owed}`, so **`role` is already an occupied word** and must not be reused for an edge's type. Arrives with the artifact layer |

## Spelling

The render carries two casings - `done_by`, `sticky_note`, `not_started` in snake; `builds-on`, `course-outline`, `points-at` in kebab - and **the split is not internal-versus-outward.** It is whether the coordinator can **name the thing back**:

- **written back → the schema's own spelling.** Kind discriminators go into `land()`, field names into `set`, link types into `attach`, enum values into both. A render that respelled them would hand the coordinator a word the surface then refuses.
- **invented by the render → free.** `<neighbours>`, `<edge>`, `<annotations>`, `points-at` / `pointed-by`. Nobody writes these back.

This is the rule that lets `<edge>` stand while `<sticky_note>` keeps its underscore. *An id-carrying tag takes the schema spelling* cannot do that job: `<edge>` carries an id and the schema calls the record `Link`.

The schema's own split - `not_started` snake, `builds-on` kebab, both written back - is inherited, not created here. Normalising it is the schema-rename effort's, not this ticket's.

## What this audit is not

It tests the two criteria that can be applied mechanically. `0093`'s criteria 3, 4 and 5 are about whether a name **routes** and whether it asks the question its value answers - those need the value in hand and are rulings, not checks. The projection's name (`has-more` / `related-by`) fails 4 and has no passing candidate: its value is a link kind, so any honest name uses schema-internal vocabulary, which C2 bars. That bind is `#80`'s to resolve or to hand on.


## Settled at #80 (Billy, 2026-09-03)

| was | is | ground |
|---|---|---|
| `<glance kind="obligation" …/>` | `<obligation …/>` | a render reads intuitively rather than mapping the schema 1:1. `kind` stays an internal word and never appears in the output, which also retires `<glance>` |
| `<links>` `<link>` | `<neighbours>` `<edge>` | `link` is `CONTEXT.md`'s name for the internal record. An edge has an id at birth, so `attach`/`detach` have something to address |
| `direction="in\|out"` | `points-at` / `pointed-by` | the value says what it means instead of leaving the frame of reference unstated |
| `ref="2c03"` | `<course id="2c03"/>` | `0093` rejected `<ref>` once for colliding with the `Ref` term; the attribute collided the same way |
| `role=` for an edge's type | `type=` | `0012` gives `spec` a `role ∈ {given, owed}`, so `role` was already occupied |
| *(spelling)* | unchanged | **every name the coordinator writes back keeps the schema's spelling.** An earlier pass kebab-cased them all; `<sticky_note>` broke it, and `<edge>` shows why the rescue is *written back* rather than *carries an id* |
| `has-more` / `related-by` | *absorbed* | the edge carries the relation, so the projection has no place in a node's render. It survives only where neighbours cannot be listed, which is ring 0 |

`created_at` / `updated_at` **render**; `added_at` **does not**. The two are not one decision: `0046` puts an annotation's whole body in the block, and *"without `updated_at` a January answer is indistinguishable from today's"* - the field's entire purpose is the read. `added_at` describes **the row**, and `look_at`'s purpose is to say what the **node** is.

## The fourth hole

`0082`'s four rules are a **placement** rule, not a **selection** rule. They say where a field lands, never which fields enter, and #60 waved selection through with *"every other field"*. Excluding `added_at` is the first cut against that, and it had to be argued rather than derived - which is the same shape as the three holes #60 left: the line is not derivable, a collection was never reached, and a composed batch had no position.
