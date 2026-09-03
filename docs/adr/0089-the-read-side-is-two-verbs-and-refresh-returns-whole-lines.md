# The read side is two verbs, and the refresh returns whole lines rather than a delta

`look_at(id)` reads one node. A second verb, `refresh()`, refreshes the coordinator's resident view and returns what changed in it.

**The second verb exists because ring 0 has no node to address.** Ring 0 is a projection over obligations, not a node, so no `look_at` returns it and there is no id to pass. `0044` already states the behaviour without saying who triggers it - *"the view refreshes as facts change but never deepens"* - and this record supplies the trigger.

**What `refresh()` returns is a whole **line** per changed obligation, plus an explicit marker for a row that is gone.** Not a field-level delta. The element was written `<glance>` here; #80 retired that name for a node's render (`0096`), and **what element a ring 0 line uses is open**, because ring 0's own render is not decided - see `0094`'s closing section.

**The ground is that a delta is not self-sufficient and fails silently.** A field-level delta means nothing without the baseline it is a delta against, and that baseline would have to be held by the conversation. `0043` states the hazard in place: *"in a long-running agent conversation the discard is **not** automatic - compaction is lossy and unpredictable, not a discipline"*. A conversation whose scale is days to weeks (`0044`) is compacted repeatedly, and a delta whose baseline has been compacted away is not an error, it is unreadable without saying so. A whole line is readable on its own, so losing the baseline costs *what did not change* rather than everything.

A delta also has to answer *against what*. Either the coordinator carries a watermark, or the verb remembers what it last sent - and a component that answers from state it keeps is a second **holder**, whose cost is parked at #66.

## Considered Options

**A signal naming what changed, without content.** Rejected because an assigned id *"says nothing about the record it names"* (`CONTEXT.md`'s `id` entry, from `schema.md` §1.1), so a signal carrying only ids gives the coordinator no basis to decide whether to look. This holds in the scope that matters: `refresh()` ranges over obligations, whose ids are assigned rather than supplied - `0026` exempts only `course`. Made useful, it must carry what decides whether a node is worth one `look_at`, and that is the line. The signal form therefore converges on this one rather than competing with it.

**A full re-render on every refresh.** Self-sufficient, and its cost is linear in the number of refreshes across a conversation that runs for weeks. Rejected on that accumulation, but the deciding variable is **how often a refresh happens**, which is a rule about what an agent should do and therefore presentation (`0059`), and it is not settled here. If that rule turns out to make refreshes rare, the simplicity of a full render is worth re-opening.

**`whats_changed()` as the name.** Rejected: a query-shaped name over an operation that mutates the view misrepresents what the call does. See `0093`.

## Consequences

Whether the view is also materialized as a local file is the **implementation's** choice and is not decided here. Such a file would be a regenerable render serving recovery after compaction, not a source of truth.

Source: ruled at #62 (Billy, 2026-09-02). The trigger `0044` leaves unstated, and the discard hazard at `0043`.
