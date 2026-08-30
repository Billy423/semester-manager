# An asked answer is kept, and its provenance is loud

An answer the system asked for is stored, with its timestamp and its provenance, and the provenance is stated prominently at every read. The harm of a stale answer was never that it was recorded - it was that it went on influencing decisions invisibly - so the fix is to make the record loud rather than to drop or expire it.

The write rule for `origin` is owed, and the divergence is already known and measured: the schema's prose says *how the claim was obtained*, and both extraction passes reached for *what document class it came from*. ADR `0057` is why one side of that collision is load-bearing and may not simply be discarded in favour of the other.

Source: fall26:records/domain/domain-design.md §9.6 (Billy, 2026-08-23) · fall26:records/spec/schema.md §4.5 · fall26:records/spec/write-rules.md §4
