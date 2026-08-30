# The projection's order is derived from the material, never from write history

The projection groups by `course` by default and the grouping key is a parameter, because symmetry is scoped to the set the judgment ranges over. Within a group, order by `due` ascending, nulls last; among nulls by `done_by`; ties broken by the handle - **never by file order, because array order is insertion order is write history**. `due` is the primary key, not `min(due, done_by)`: triggering and ordering are different jobs, and nulls-last gives an undated obligation a defined position that a bare date order does not.

**The defendant, carried inline because it lives only in a findings record:** the order measured in the implementation was array order. A swapped-cause control moved the notes and changed nothing else, and the same item still came first, **3 of 3**. The projection was **violating** this rule, not lacking one.

Source: fall26:records/spec/ring-0.md §5 (Billy, 2026-08-28); the swapped-cause control at fall26:records/findings/read-cycle.md §4
