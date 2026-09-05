# The projection's order is derived from the material, never from write history

Order by `due` ascending, nulls last; among nulls by `done_by`; ties broken by the handle - **never by file order, because array order is insertion order is write history**. `due` is the primary key, not `min(due, done_by)`: triggering and ordering are different jobs, and nulls-last gives an undated obligation a defined position that a bare date order does not. **Where a grouping applies this is the order within a group**, and what grouping ring 0 applies is open.

**A grouping clause was struck from this record at #82.** It ruled ring 0 grouped by `course` by default with the key as a parameter, on the ground that symmetry is scoped to the set the judgment ranges over. `0100` records why it went: it fixed a value on `0039`'s symmetry rule without deriving it from what the view is for, and ring 0's routing purpose is undefined. **The order above is unaffected** - its ground is that array order is insertion order is write history, which owes nothing to routing, and `0082` inherits it.

**The defendant, carried inline because it lives only in a findings record:** the order measured was array order, and a swapped-cause control moved the notes and changed nothing else - the same item still came first, **3 of 3**. **There was no implementation.** That material built nothing: no schema, no verb, and the order in question is the order of `items` in a hand-written fixture returned whole by a stub. The evidence supports *an agent handed a JSON list in file order reproduces file order*; it does not support *a projection exists and is violating this rule*.

Source: fall26:records/spec/ring-0.md §5 (Billy, 2026-08-28); the swapped-cause control at fall26:records/findings/read-cycle.md §4
