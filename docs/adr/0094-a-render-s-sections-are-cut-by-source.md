# A render's sections are cut by source, and a composed batch is a fourth source

`0082` derives where a **field** lands from its kind's field table, and says of itself that those four rules *"do not reach a collection at all"*. What they do not reach is **how many sections a render has and what puts a thing in one**. The cut is by **source** - where the material in that position came from - and it is not designed here; one landed record makes it.

**`0046` makes the cut, in one sentence.** *"A read that returns a node's neighbourhood must deliver `sticky_note` and `progress` through their own channel, never as ordinary neighbours."* An **own channel** separates annotations from the node's own fields; **never as ordinary neighbours** separates them from neighbours. Three positions fall out of that one sentence, and the render names them: the node's own fields, `<annotations>`, `<neighbours>`.

**A batch the kind composes is a fourth source, and naming it closes a hole `0084` left.** `0084` ruled that `look_at(course)` composes `obligations.list(course)` and **never said where that batch lands**. It is not the node itself; it is not something said about the node; and `0084`'s own ground is that a course reaches its obligations by **no edge**, so it is not a neighbour either. By the same rule that gave annotations their own channel, it takes its own section, named for what is composed:

```xml
<course id="2c03" name="…" term="winter-2026">
  <annotations>  …full text…       </annotations>
  <neighbours>   …one line each…   </neighbours>
  <obligations>  …one line each…   </obligations>   <- the composed section
</course>
```

**`0045` is not the record doing this work, and an earlier draft of this ruling cited it wrongly.** `0045` says *"The coordinator sees what a node **IS**; it never sees what a node **SAYS**"* - **a node**, not someone about it - and its next sentence, *"Rendering a node's own summary is a skeleton read and is allowed"*, shows the subject is the store boundary. Its scope clause is explicit: *"What this record governs is what enters the coordinator's context, never what the coordinator may do"*, and it names using it one aspect over as *"the error corrected here"*. The misreading also ran against this render: under *never what someone says about it*, `<annotations>` carrying an annotation's full text would be barred, and `0046` requires exactly that.

**Ordering within a section is `0082`'s and is not re-decided here** - the material's key, tiebroken by the handle, never array order. A composed obligation list orders by `due`; where a `due` is null the row has no key, and it sorts last by a decision made in the render rather than by anything `0082` says. **For ring 0 that is not a render decision**: `0041` rules nulls last and the null tiebreak, which this record and #80 both missed (`0100`).

## What this record does not decide

**Ring 0.** It is a projection over obligations rather than a node (`0089`), so no `look_at` returns it, and a live proposal would make it a parameterised query rather than a fixed resident view. Its render, the band's representation and `has-more`'s surface name all travel with it.

Source: ruled at #80 (Billy, 2026-09-03). The hole this closes is `0084`'s, which homed `look_at(course)`'s composition without positioning it.
