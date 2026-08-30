# `progress.state` is non-nullable and defaults to `not_started`, so the agent has no reason to ask

`state` is a non-nullable enum `not_started | in_progress | done` with **no unknown state**: an obligation with no progress record reads as `not_started`, because that is what a thing nobody has touched is. A nullable state is honest and was given up because it makes the system announce it does not know, which gives an agent a reason to ask *have you started this yet*. A **defined** default is not an invention; the measured incident that produced the prohibition recorded a run inventing a default where none was specified.

```
state : not_started | in_progress | done      NOT nullable

detail illegal without a state         -> enforced at construction
one current value per target           -> enforced by the service
only the owner authors it              -> enforced nowhere, deliberately
no `about` link is legal               -> means progress on a free topic named in `detail`
```

Nothing is written at creation - absence carries the default. The stored vocabulary is fixed and the rendering is per kind of target: *Submitted* for an assignment, *Written* for an exam.

Source: fall26:records/spec/schema.md §4.5 (Billy, 2026-08-28); fall26:records/domain/model.md §8.2; the projection consequence at fall26:records/spec/ring-0.md §4
