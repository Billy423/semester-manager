# Components share state through the store, never through a protocol

There is no orchestrator and no control relationship, only a scope parameter: **the store is the channel.** Extraction writes and the coordinator sees it on its next read; a subagent returns a conclusion, never state. There is no queue, no ack and no cursor, because **there is no second party that might be asleep**.

**One domain, not one per course.** What differs between courses is a working-instruction bundle that loads with the scope, not an agent. Per-course expert agents were rejected on the same ground: the difference is instructions, and instructions are not an agent.

Source: fall26:records/domain/domain-design.md §5, §8, §9.4 (2026-08-21)
