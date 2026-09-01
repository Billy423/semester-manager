# `progress.state` is non-nullable and defaults to `not_started`, so the agent has no reason to ask, and it lives on `progress` rather than on `obligation`

`state` is a non-nullable enum `not_started | in_progress | done` with **no unknown state**: an obligation with no progress record reads as `not_started`, because that is what a thing nobody has touched is. A nullable state is honest and was given up because it makes the system announce it does not know, which gives an agent a reason to ask *have you started this yet*. A **defined** default is not an invention; the measured incident that produced the prohibition recorded a run inventing a default where none was specified.

```
state : not_started | in_progress | done      NOT nullable

detail illegal without a state         -> enforced at construction
one current value per target           -> enforced by the service
only the owner authors it              -> enforced nowhere, deliberately
no `about` link is legal               -> means progress on a free topic named in `detail`
```

Nothing is written at creation - absence carries the default. The stored vocabulary is fixed and the rendering is per kind of target: *Submitted* for an assignment, *Written* for an exam.

**Why `state` sits on `progress` and not as a field of `obligation`.** Two reasons, and the second is load-bearing on the kind set. `state` and `detail` are on one record **on purpose**, because *"two records would be free to drift apart, and one cannot"* - a `detail` reading *half done* beside an `obligation.state` of `not_started` is unreachable while they share a record. And `state` is what **separates `progress` from `sticky_note`**, which carries the same `origin`, the same timestamps and its own free-text field: stripped of `state`, `progress` differs from a sticky note by `category` and the discriminator alone, so moving the field is closer to deleting a kind than to relocating one.


Source: fall26:records/spec/schema.md §4.5 (Billy, 2026-08-28); fall26:records/domain/model.md §8.2; the projection consequence at fall26:records/spec/ring-0.md §4
