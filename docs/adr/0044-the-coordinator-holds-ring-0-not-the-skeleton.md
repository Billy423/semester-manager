# The coordinator holds ring 0 in its context and queries the skeleton on demand

The coordinator holds ring 0 in its conversation context and **queries** the skeleton on demand; it does not hold the skeleton. Its persistent memory holds pointers and summaries, never content, and the view refreshes as facts change but never deepens. **Ring 0 is resident for the coordinator and for nobody else** - depth is just enough to triage, never enough to work.

**Resident means held in the conversation's context.** The code process is per-invocation and its lifetime is not a deciding fact here; the conversation is long-running, days to weeks. Never write "the coordinator's lifetime" without saying which one.

Source: fall26:records/domain/domain-design.md §9.1 and §9.5; fall26:records/domain/model.md §7 (the whole-skeleton-resident draft, retracted); fall26:records/spec/ring-0.md §1 and §7
