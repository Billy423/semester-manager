# Derivation runs top-down and construction runs bottom-up

Interaction requirements decide which capabilities must exist, never what a method looks like, and the discriminating test is the operative half: **if the method changes when the surface changes, the surface has leaked down.** The rejected alternative was reverse-deriving the design from interaction requirements outright. `0059` carries the adjacent rule - *a tier is designed against the tier below it, and that tier must already exist* - which is construction order, the opposite direction and not the same claim; the two together are the method, and only one of them was ever recorded.

**The test's yield:** it is what identified `look_at` and `land`+`Diff` as leaked down from the surface. Anyone re-doing that classification without the test has no test.

Source: fall26:evidence/2026-08-27-tier-recut/NOTES.md correction 2 (Billy asked; the answer was adopted in the sitting and is not tagged as a ruling)
