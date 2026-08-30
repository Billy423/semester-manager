# Exactly two persisted things, coupled by one field; ring 0 is not a third

There are exactly two persisted things: the skeleton (nodes and links) and the store (chunks and embeddings). Ring 0 is not a third: residency is an access policy over **obligation nodes' fields**, not a separate store. The coupling surface between the two is exactly one field, `chunk.node_id`, which is what lets each degrade without the other.

```
ring 0   - not separately persisted
skeleton - persisted
store    - persisted
```

Source: fall26:records/domain/model.md §6; fall26:records/spec/design.md §3.0; ring 0's field grain at fall26:records/spec/ring-0.md §4
