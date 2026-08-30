# Two conflicting statements never coexist, and how a conflict closes depends on what is in conflict

Two conflicting statements never coexist in the system: landing detects a conflict instead of overwriting - *"you told me this, the record says that, which holds"* - and a conflict is closed at write time rather than left for a reader to reconcile. A shallow collision the agent may resolve itself, but it **must report the resolution afterwards** and never resolve transparently; a deeper one it must put to the user before resolving. The owner's own claim is not exempt - it is surfaced against the held record - and **an inferred value is asked about, not annotated; an update is an update.**

| depth | examples | what the agent does |
|---|---|---|
| **shallow** | a due date · a room | resolves it, then **reports the resolution**. Never silently |
| **deep** | an assignment's spec or requirements · a concept · an exam's time or place | **asks before resolving** |

Requirement this places on the field set: depth is a property of what a statement collides with, so the discriminator lives on the record.

**The two-tier maintenance rule, landed here and flagged:** *a target revised later than the note is evidenced staleness the agent may act on in passing, while anything else may be surfaced for confirmation and never resolved.* It is the corpus's only existing shallow/deep policy. Whether *in passing* survives *never silently* is an open decision for Billy, and its input does not exist until a kind carries a revision date (ADR `0053`).

Source: fall26:records/domain/model.md §8.1 (Billy, 2026-08-23); fall26:records/spec/design.md §1 F2; fall26:records/spec/write-rules.md §1.1; the two-tier maintenance rule at fall26:records/spec/schema.md §4
