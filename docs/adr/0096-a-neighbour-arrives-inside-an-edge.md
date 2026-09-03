# A neighbour arrives inside an `<edge>`, and the projection `has-more` carried is absorbed by it

`0082` had a neighbour arrive as one self-closing element carrying the target's line plus *"the link's `role`"*. That dissolves a **record into another record**: `0016` makes a relation a record rather than a field on either end, `0017` gives it a natural key, and `0082` itself calls `role` *"a `Link` field"*. A field of the link cannot ride on the target and still be the link's.

**So the edge gets its own element, and the neighbour's line sits inside it.**

```xml
<neighbours>
  <edge id="138" type="builds-on" direction="pointed-by">
    <obligation id="51" course="2c03" name="Midterm 2" due="2026-03-13" state="not_started"/>
  </edge>
</neighbours>
```

**`<neighbours>` and `<edge>`, not `<links>` and `<link>`**, by `0093` criterion 2: `link` is `CONTEXT.md`'s name for the internal record - *"A typed, directed relation between two refs, stored as its own record"* - which is an edge described in the schema's own words. The graph vocabulary names the same thing from the reader's side and is nobody's internal structure.

**The edge carries an `id`.** `0017`'s natural key is a uniqueness constraint, not a statement that the record is unaddressable, and `0061` puts addressing at the surface. Without it `attach` and `detach` have nothing to name.

**`direction` says what it means.** `points-at` and `pointed-by`, not `out` and `in`, because the frame of reference of `out` is stated nowhere. Before this the two directions rendered identically and an inbound edge was invisible.

**`type`, not `role`, for the edge's kind.** `0012` gives `spec` a `role ∈ {given, owed}`, so `role` is an occupied word naming a different thing on the same record - `0024` seen from the field end.

## `has-more` is absorbed here, which answers the second of #62's two carried items

`0092` rules that `has-more` holds *"the set of link kinds present on that node"*. **`<neighbours>` strictly contains that set** - the kinds are readable off the edges it lists - so a render carrying both states one fact twice, which `0024` bars.

**So `has-more` has no place in a node's render at all.** Its own ground in `0092` is that *"ring 0 cannot list a node's neighbourhood, so without this field the coordinator's next call is a gamble"*, and that ground holds **only** where the neighbourhood cannot be listed. That is ring 0, and the field's surface name travels there with ring 0's own render. `0092`'s value ruling is untouched; what moves is where it appears.

## A rejected shape, recorded because it caused a visible defect

The projection was briefly rendered as `<link role="…"/>` elements **inside** the neighbour's line, on the reasoning that a `<link>` with a target is the edge and one without is the presence of that kind. Adjacent elements sharing a name and meaning two things read as *this pair is connected by two kinds*, which is false and which `0012` makes almost unconstructible - only `covers` and `applies` share a signature, and both wait on the artifact and concept layers.

Source: ruled at #80 (Billy, 2026-09-03). `0082`'s neighbour element and `0093`'s names table are repaired at source.
