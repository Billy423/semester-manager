# Pre-registration: two blind reviews of the #85 resolution draft

Written 2026-09-05 before either reviewer was dispatched. Not edited afterwards.

## What is reviewed

`resolution-85.md` in this directory - the draft resolution comment for issue #85. Both reviewers receive the draft and full read access to the repository at `F:\projects\semester-manager` (ADRs, `CONTEXT.md`, `docs/agents/`, and `gh` for issues). Both are withheld this session's transcript, its reasoning and its rejected framings - the analysis, not the material. They are blind to each other.

## Sampling rule

No sampling. Lens 1 opens every record and issue the draft cites. Lens 2 reads the draft, `CONTEXT.md`, `0001`, `0039`, `0043`, `0046`, `0070`, `0100`, the #84 body and comment, and #85-#88, then tries to break the definition against them.

## Lenses

- **Lens 1 - attribution.** Does every cited record say what the draft attributes to it, for the aspect the draft uses it for (`docs/agents/reading-records.md`)? Does any landed record contradict a ruling in the draft that §9 does not already list for repair?
- **Lens 2 - falsification.** Find a judgment the coordinator must make (from `0001`, `CONTEXT.md`'s opening, #84's scenarios, or the sibling tickets) that the four generators cannot serve; find a generator the test admits that should be excluded, or excludes that should be admitted; find any step in the draft that reasons from an existing artifact back to the purpose; find any decision the draft makes that §10 says it does not.

## Verdict thresholds

A finding is **blocking** if it (a) shows a cited record does not support the claim it is cited for and the claim is a ruling, or (b) exhibits a coordinator judgment that no composition of the four generators serves and `0043` bars assembling, or (c) shows a ruling in the draft contradicting a landed record not listed in §9. A finding is **repair** if it changes an attribution, a wording or a table cell without changing any ruling. **Ambiguous resolves to blocking.** The draft posts only after every blocking finding is either resolved in the text or ruled on by Billy, and every repair finding is applied.

## Judgment calls, named up front

Whether a given intent is structural or by-content at the margin; whether the `0059` addition in §9.6 is a repair or a decision. Both are Billy's, not adjudicated by the reviewers.

## What I expect to be wrong about (predictions - the yield is what is found beyond these)

- P1. `0084`'s *"service read over an indexed field"* is over-read as licensing every unanchored filter; it licensed one.
- P2. §2's *"band A's `has-more` is the discovery channel"* cites a field whose render location `0096` moved to ring 0's own render, which #82 has not decided.
- P3. S1 and S2's *"served today"* is overstated: `0096`'s `direction` example is `builds-on`; that `look_at(concept)` renders inbound `covers` edges is not ruled, and the concept and artifact layers do not exist.
- P4. The test's clause (a) fails for the absence generator if composition admits set difference (filter minus one-hop); composition needs to be defined as chaining, not set operations.
- P5. The `0001` rewrite demotes *manage cross-course information* below what #14 allows - #14 says plan generation *is* coordination, an activity.
- P6. The `0017`/`0096` deviation row glosses a real contradiction between `0025`'s *one id space shared by every kind that can be a link endpoint* and an edge carrying an id.
- P7. *Ring 0 is one standing routing result* trips `0100`'s and `CONTEXT.md`'s bar on *materialized view* vocabulary.

## Scoring

Each reviewer's findings are listed against P1-P7. A finding matching a prediction is a known hole and is fixed. A finding outside the list is the exercise's yield and is what the review is judged to have been worth.
