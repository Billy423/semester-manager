# Store output enters the coordinator only as a conclusion; the context that produced it is discarded, and who produced it is irrelevant

The invariant is a data-flow rule, not an agent topology: store output enters the coordinator only as a conclusion, the context that produced it is then discarded, and who produced it is irrelevant - a spawned subagent, a session Billy opens himself and a task session are all implementations. **The coordinator sees what a node IS; it never sees what a node SAYS.** Rendering a node's own summary is a skeleton read and is allowed.

*"No corpus retrieval, no file reads, no fact writes"* is a purity restriction **on materials**, not an enumeration of the coordinator's reads: `look_at(course)` is a call the coordinator makes, or plan generation is blind.

Source: fall26:records/domain/model.md §7 (Billy, 2026-08-22); the superseded responsibility table at fall26:records/domain/domain-design.md §9.3; re-cut onto tiers at fall26:records/spec/architecture.md §1 and §7
