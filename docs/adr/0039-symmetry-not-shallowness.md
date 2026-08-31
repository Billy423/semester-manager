# The observation invariant is symmetry, not shallowness, and it is scoped to the set the judgment ranges over

Observe anything you can afford for every course at once; never observe anything you can only afford for one - the second case is `dispatch`'s entrance, and its result must come back in the same shape as the others. Asymmetry that comes from the material is legitimate; asymmetry from interaction history is not, because **asymmetric depth biases allocation and visible work masquerades as important work** - the failure mode observed in a live running system, not derived. Symmetry is scoped to the set the judgment ranges over, not unconditionally to all five courses. **What fixes affordability is the owed length bound, and it is therefore load-bearing on this rule** - eight one-line summaries can be pulled for a comparison set, eight paragraphs cannot. The bound is owed at issue #12 item 6, and ADR `0079` voids the evidence base it was previously going to be read from.

```
observe(X) is permitted for a judgment over set S
  iff X is affordable for every member of S
  else dispatch(X, member) -> a value in the same shape as every other member's
```

The invariant was never shallowness. What forced the restatement: a blind run gave the planner an observation space of deadlines and weights alone and it produced a date-ordered queue, which says more about the observation space than about ring 0. **Ring 0 returns to being the layer that is resident, not the definition of what is observable.** ADR `0040` applies the same rule to the renderer.

Source: fall26:records/domain/domain-design.md §9.2 and fall26:records/domain/model.md §7 (Billy, ruled 2026-08-23); made operative at fall26:records/spec/ring-0.md §5; the failure mode at fall26:records/domain/domain-design.md §1 ruling 12
