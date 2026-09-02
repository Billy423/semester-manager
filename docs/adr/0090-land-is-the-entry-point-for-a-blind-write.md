# `land()` is the entry point for a write whose author has not read the target

The write side has two entry points, and the axis that separates them is neither material against no-material nor bulk against one item. It is **whether the author of the write has read the row it lands on.**

**`land()` takes a blind write.** `0086` bars both extractors from skeleton knowledge, so a candidate fact is produced without ever seeing the skeleton and carries no handle. `land()` is the one place a source-shaped thing becomes skeleton-shaped.

**The coordinator's direct write is not blind.** `0025` makes an id opaque and *"obtained only by reading it back"*, and `0061` makes every read return it, so the coordinator cannot name a row it never read - `0026` exempting `course`, whose id the material supplies. Its write is skeleton-shaped on arrival and never needs that transformation.

**`0024` is what makes this two verbs rather than one.** A single write verb would take an input that sometimes needs its central transformation and sometimes does not, and a verb whose purpose is stated with that disjunction has two purposes. The parameter would have to be a union of a source-shaped bundle and a claim about a held row, which is a catch-all seen from the parameter end.

## What follows from blindness, rather than standing separately

Matching and conflict handling are usually stated as two more properties of landing. They are the same property as this one. Because the author never read the target, someone else must decide which row a candidate fact belongs to, and `0059` consequence 4 puts that decision at the surface: *"matching two records is an interaction at the presentation tier, not an algorithm in the application tier."* `0051` then requires that a shallow conflict be resolved **and reported**, and a deep one be put to the user first.

**A script can do neither, so `0086`'s offline pass cannot land its own output.** This does not conflict with that record: what may not enter a session is the page-image, and a candidate fact is small text. **The material does not enter a session; the facts do.** Which agent performs the matching - the coordinator, or a task session - is not decided here.

```
extraction   a script, or the session the material arrived in   -> candidate fact, no handle
matching     an agent, at the surface                            -> a handle, or "this is new"
land()       idempotent, field-grain partial update, conflict-detecting
```

## Considered Options

**One write entry point.** Argued twice during the ruling and withdrawn twice. Its strongest form was that after matching the two inputs converge in shape, and that `0051` puts the owner's own claim under the same conflict discipline anyway. The second half is true and does not reach the conclusion: `0051` constrains **discipline**, not which entry point exists, and two verbs can both honour it. See `0091`.

**Splitting on material against no-material**, following `0087`'s own framing. Rejected as the wrong cut for the surface: `0087` explains where a write *originates*, and both origins can end at a row the writer has read.

Source: ruled at #62 (Billy, 2026-09-02). `0086`'s extractor prohibition and `0087`'s ownership are unchanged; this records which surface each reaches.
