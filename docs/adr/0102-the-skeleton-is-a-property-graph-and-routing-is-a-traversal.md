# The skeleton is a property graph and routing is a traversal over it; HNSW was scaffolding

#84 carried HNSW's layering as a candidate lens for routing, to be written down as a commitment if routing turned out to be *enter sparse, descend dense*, and removed if not. **It is removed.** The analogy failed on its subject, not on the reservations #84 recorded: HNSW is an index structure for similarity retrieval, and what this system needed named is a query model over typed links. Its descent story describes the coordinator's loop - fetch, form an intent, resolve, fetch - which is not routing; routing (`0101`) is one half of that loop.

**The commitment that replaces it.** The skeleton's data model is a property graph - labelled nodes (`kind`), typed directed links with fields (`role`, `locator`) - and routing is a traversal over it: a start, filter steps, a `where` carrying a sub-traversal, crossings over typed links, and a `path` result. `0059`'s persistence tier already holds the two primitives such a traversal is built from, *fetch-by-key and one-hop traversal*. **The commitment's value is that it states the read side's asymmetry in one line:** the write side is `create · set · attach · detach · delete` (`0093`'s primitives); the read side is `V(id)` with one hop composed into it and no traversal as an operation.

**The commitment is bounded by these deviations, each a ruling it may not override:**

| a graph database | this system | record |
|---|---|---|
| an edge requires both endpoints; delete cascades | a ref may dangle; nothing cascades | `0018` |
| an edge's identity is a surrogate; properties update | identity is the natural key with `locator`, for idempotent re-landing; no update, detach + attach; an `id` for addressing only | `0017` `0096` |
| schema optional or loose | link kinds a closed set with endpoint signatures; a compiler refuses | `0012` `0063` |
| membership is an edge | course membership is a Ref-typed field (`0029`, on cardinality; its changed status is held at `0084`). For routing a Ref-typed field is crossable in the vocabulary; whether the crossing is admitted is #86's | `0029` `0084` |
| time on vertices | no time axis in the skeleton | `0021` |
| labels are flat | three semantic layers | `0009` `0027` |
| an engine with a planner | files plus an adjacency index over links rebuilt at load, and an indexed field for the one Ref crossing that exists | `0062` `0084` |
| a vector index on the graph | two persisted things coupled by one field | `0019` |
| any caller, full depth | an observation contract: symmetry, discard, residency by policy | `0039` `0043` `0044` |
| every traversal renders | `applies` is never rendered as a neighbour; on a path it appears as the crossing that reached a position | `CONTEXT.md` |

**The ninth row is the boundary of the whole analogy.** A graph database has no concept of what its caller may hold, and half of this repository's records are about that. The commitment covers the skeleton and routing; it does not cover the system.

**Swapping in an engine is refused on this table.** An engine provides planning and transactions, which `0062`'s size and the single-writer contract do not need, and it requires the opposite of the first two rows. Arriving at the property-graph model from the material is evidence that the modelling was sound, not that it was copied: every row of `0012`'s table was earned by three real instances and a nameable query.

Source: ruled at #85 (Billy, 2026-09-06); #84's own protocol for the lens - commitment or scaffolding, recorded either way.
