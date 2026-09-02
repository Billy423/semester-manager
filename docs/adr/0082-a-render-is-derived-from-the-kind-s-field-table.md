# A node's render is derived from its kind's field table by four rules, not designed per kind

`look_at` is abstract over every kind, and what it returns is **derived** rather than chosen: the element name is the kind, `id` and `kind` are attributes because they **address** rather than describe (`schema.md` §1.1: an id *"says nothing about the record it names"*), and every other field is placed by four rules.

```
repeats                          -> element        (an attribute cannot repeat)
structured, a Ref                -> element        (a Ref is kind AND id; an attribute holds one)
the kind's ONE free-text field   -> the element's text content
any other atomic scalar          -> attribute
```

**The third rule is the load-bearing one, and it is the schema's own.** `0028` caps free text at **one field per kind**; an element has **one** text content. The two limits coincide because both are the position for *what the thing itself is*. Without it the attribute/element line is taste, and taste drifts.

**One exception, and only where the schema declares it.** Where a field's stated reader is *"any reader of"* another field, the qualified field becomes an element carrying its value and the qualifier becomes its attribute - `<grade_share conditional="true">10</grade_share>`. Today `grade_share` / `grade_share_conditional` is the sole instance of *that* exception. **A second exception, declared at #62.** Two things the line carries come from no field table at all and are therefore not produced by the four rules: **`has-more`**, which is a fact about the node's neighbourhood rather than about the node (`0092` rules what it holds), and **`role`**, which is a `Link` field (`0017`). Both are render-computed and both are named here so that a reader does not take the four rules as exhaustive over the line.

**The render may not invent a relationship the schema does not declare**; doing so makes the render a second, undeclared model, which is the failure this repository exists to escape.

**A neighbour and a `Ref`-typed field do two jobs, and after #62 they no longer share a word.** A **neighbour** arrives as `<glance>`, one self-closing element carrying that kind's line - obligation's is ring 0's band plus `has-more` and the link's `role`, course's is `id` `name` `term` - and answers only *is this worth one call*. A **`Ref`-typed field** is a bare pointer, `<course ref="2c03"/>`, and answers *which one is this*, not *should I go there*. This record originally named both `<ref>`, which is the `0024` overlap `0093` renamed away. `locator` is not on either: it says where you land after walking, which does not bear on whether to walk.

**A defaulted `progress` carries no `id`, and that absence is the signal.** `0035` makes absence carry `not_started`; a default is not a record, so `0061` asks no handle of it.

**Absence is written, never omitted.** `done_by=""` rather than a missing attribute: the reader is a token stream, so an omitted attribute is invisible rather than visibly empty, and `0028` requires a null to be readable as *no record* rather than confusable with *this kind has no such field*.

**Order is inherited, not invented here:** the material's key, tiebroken by the handle, **never array order** - `ring-0.md` §5's *"Array order is insertion order is write history"* and `0041`'s inline retraction. `parts` by source order, annotations by `created_at`, a composed obligation list by `due`, links by `role`.

**A risk this record carries rather than hides.** XML was chosen partly because the reader is a known Claude coordinator, which makes this surface **model-dependent**; #58's first standing constraint warns against generalising across topologies. And obligation's line is ring 0's band by a **transfer of the field set, not of a render**: `0038` chose that field set for residency, and it is reused here because `ring-0.md` §1 states the same criterion - *"which node is worth one `look_at`, and which is merely known to exist"* - for both. The transfer is a decision made here, not something `0038` says. **It says nothing about how a *collection* of obligations renders** - ring 0 is not a sequence of lines by anything written here, and these four rules, deriving as they do from one kind's field table, do not reach a collection at all.

Source: ruled at #60 (Billy, 2026-09-01). Supersedes the withdrawn `{ summary, annotations[], edges[] }` triple carried at `fall26:records/spec/design.md` §3.7 and withdrawn at #12 item 4; the field tables it derives over are `fall26:records/spec/schema.md` §2-§4.5.
