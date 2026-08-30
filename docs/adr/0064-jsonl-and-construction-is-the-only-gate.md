# JSONL with a `schema_version`, and construction is the only gate

The skeleton persists as `nodes.jsonl` + `links.jsonl`, each carrying a `schema_version` - JSONL enforces nothing and construction is the only gate, so without a version a stale file fails as an unexplained validation error. Vectors go to a **side binary store keyed by node id, never into the JSONL**. **A constructor sees one line**, so any rule ranging over more than one record - the id space, one-current-value-per-target, link identity - belongs to the services rather than to construction.

**The hole, which must travel with this decision:** construction is not currently part of the load. Measured, not inferred - a store carrying `due: 'April 2026'` and a stray `concept` node loaded without error and was rewritten intact. A malformed record survives a round trip silently. Closing that needs a load-time construct pass owned by the application tier; what a version mismatch should do is a separate open question.

Source: fall26:records/spec/schema.md §8 (2026-08-27, corrected 2026-08-28)
