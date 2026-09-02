# The primitive reports what it replaced; the surface adjudicates

`0051` requires that two conflicting statements never coexist and that landing detect a conflict instead of overwriting. **That is a rule about discipline, not about which entry point exists**, and the application tier already implements it in the only form it can: `service.ts`'s `Replaced<T>` returns `before`, `after` and `changed`, and its own docstring gives the reason - *"What an update replaced, so the tier above can adjudicate rather than discover."*

So the primitive never decides. It reports, and what the report means depends on who called it:

- **From the coordinator's direct write**, `Replaced` confirms a resolution that has already happened. The coordinator could not name the row without having read it (`0090`), so by the time it writes, it has seen the held value and its write *is* the resolution.
- **From `land()`**, `Replaced` is a real conflict, because the author was blind, and `0051`'s shallow-or-deep handling runs.

**`0051` therefore needs no revision.** Its guarantee holds on both routes by different mechanisms, and neither route overwrites silently.

## Two limits, stated in place rather than discovered later

**Read-before-write is structural for every kind but `course`.** It rests on an id being opaque and obtained only by reading it back, and `0026` supplies `course.id` from the material. A coordinator can therefore name a course row it never read.

**It is not structural at field grain.** Ring 0 carries the band and excludes `parts` and `grade_share` (`0038`), so a coordinator correcting an out-of-band field holds a handle without having seen that field's held value. Closing that gap is a rule about when to `look_at` before correcting, which is a rule about what an agent should do and therefore presentation (`0059`); which issue owns it is not settled.

## Considered Options

**Sinking conflict detection into the primitives, so the invariant is structural rather than conventional.** It is implementable - a differing held value is detectable at field grain, and `0051`'s depth discriminator *"lives on the record"* - and `0059`'s adjudication rule leans that way by putting authority downward. Rejected because the coordinator's write is already post-resolution: detection there would re-open, at every correction, an interaction the coordinator has just had with the owner.

Source: ruled at #62 (Billy, 2026-09-02).
