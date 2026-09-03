# Each section carries its own depth, and that shape is what enforces the discard

`0094` cuts a render into sections by source. **The sections are not uniform in depth, and each one's depth is a different landed record's.**

```
the node's own fields   -> in full      0038
<annotations>           -> full text    0046
<neighbours>            -> one line     0060
a composed section      -> one line     0060
```

**Own fields in full**, because `0038` says of ring 0's exclusions that *"excluded from the projection is **not unreadable**: ring 0 governs residency, and `parts` comes back with any read of the obligation record"*. Residency and readability are different questions, and a block answers the second.

**Annotations in full text**, because an annotation has no identity apart from its target - it is delivered through its own channel precisely so that it arrives *with* the thing it is about. Carrying it as a line would make the reader spend a call to learn what a note says, which is the opposite of why `0046` gave it a channel.

**Anything reachable, one line**, because `0060` fixes the cost of depth: *"each level renders what is around it, and going one level deeper is one more call"*. A neighbour and a composed member are both one `look_at` away, so both are lines.

**The consequence is that `0043`'s discard is enforced by shape rather than by discipline.** `0043` requires that what is fetched is dropped and warns that *"in a long-running agent conversation the discard is **not** automatic - compaction is lossy and unpredictable, not a discipline"*. Under this record **the only unbounded thing in a return is the node itself**; everything reachable from it is bounded to a line. A return cannot accumulate a neighbourhood, so there is nothing for the conversation to fail to discard.

## The line's field set is not derivable, and this record does not supply one

`0082` sets obligation's line by a **transfer** - `0038` chose that field set for **residency**, and it is reused for *is this worth one call* because `ring-0.md` §1 states the same criterion for both. Course's line is all of its fields because it has few. **No rule generates a new kind's line**: the criterion is clear, the field set is one ruling per kind, and `artifact` and `concept` will each need one when their layers land (#20, #19, #17).

What **is** decided: a line is **one** field set per kind and does not vary per row. `0082` calls obligation's line *"ring 0's band plus `has-more`"*, and band A already carries `has-more`, so *the band* is band B. A line that picked each row's own band would import `0038`'s **residency** computation into a **read**.

Source: ruled at #80 (Billy, 2026-09-03).
