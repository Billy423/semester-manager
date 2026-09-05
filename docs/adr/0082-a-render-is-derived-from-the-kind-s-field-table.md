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

**A neighbour and a `Ref`-typed field do two jobs, and they no longer share a word.** A **neighbour** arrives inside an `<edge>` (`0096`), as one self-closing element **named for its own kind** - `<obligation id="51" …/>` - carrying that kind's line and answering only *is this worth one call*. A **`Ref`-typed field** is a bare pointer, `<course id="2c03"/>`, and answers *which one is this*, not *should I go there*. This record originally named both `<ref>`; #62 renamed the neighbour to `<glance>`, and #80 retired that too, because this record's own first clause makes the element name the kind. `locator` is not on either: it says where you land after walking, which does not bear on whether to walk.

**Three things in the sentence above were repaired at #80 and the earlier wording is wrong on each.** The neighbour element is no longer `<glance>`; `has-more` is **not** on the line, because `<neighbours>` strictly contains it and `0024` bars stating one fact twice (`0096`); and the link's field on it is `type`, not `role`, because `0012` gives `spec` a `role ∈ {given, owed}`. What survives is the transfer itself - obligation's line is ring 0's **band B** field set, since this record says *band plus `has-more`* and band A already carries it.

**A defaulted `progress` carries no `id`, and that absence is the signal.** `0035` makes absence carry `not_started`; a default is not a record, so `0061` asks no handle of it.

**These four rules PLACE a field; they do not SELECT one.** *"Every other field"* above reads as *all of them* and was never ruled. `0099` records the first cut against it - the annotation timestamps render, `added_at` does not - and states that a selection rule does not yet exist.

**Absence is written, never omitted.** `done_by=""` rather than a missing attribute: the reader is a token stream, so an omitted attribute is invisible rather than visibly empty, and `0028` requires a null to be readable as *no record* rather than confusable with *this kind has no such field*.

**Order is inherited, not invented here:** the material's key, tiebroken by the handle, **never array order** - `ring-0.md` §5's *"Array order is insertion order is write history"* and `0041`'s inline retraction. `parts` by source order, annotations by `created_at`, a composed obligation list by `due`, links by `role`.

**A risk this record carries rather than hides.** XML was chosen partly because the reader is a known Claude coordinator, which makes this surface **model-dependent**; #58's first standing constraint warns against generalising across topologies. And obligation's line is ring 0's band by a **transfer of the field set, not of a render**: `0038` chose that field set for residency, and it is reused here because `ring-0.md` §1 states the same criterion - *"which node is worth one `look_at`, and which is merely known to exist"* - for both. The transfer is a decision made here, not something `0038` says. **It says nothing about how a *collection* of obligations renders** - ring 0 is not a sequence of lines by anything written here, and these four rules, deriving as they do from one kind's field table, do not reach a collection at all. **`0094` and `0095` close that for a node's render** - sections are cut by source and each carries its own depth - and leave ring 0's own render open, because ring 0 is a projection rather than a node. **`0100` reads that projection as a view whose shape is not settled**, so the transfer above stays sound for a **line** while saying nothing about ring 0's own.

Source: ruled at #60 (Billy, 2026-09-01). Supersedes the withdrawn `{ summary, annotations[], edges[] }` triple carried at `fall26:records/spec/design.md` §3.7 and withdrawn at #12 item 4; the field tables it derives over are `fall26:records/spec/schema.md` §2-§4.5.
