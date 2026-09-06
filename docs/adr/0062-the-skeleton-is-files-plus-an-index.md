# The skeleton is files plus an index rebuilt at load, not a database

The skeleton needs a durable serialization plus an adjacency index rebuilt at load; every read is a scan over that index, and **the load is cheap enough that per-invocation and resident are indistinguishable** - a 138-node, 137-link graph is 52 KB and parses in 0.27 ms. A graph engine would buy query planning; the read side is a chain over typed links (`0101`), and the claim - unmeasured, the measurement owed - is that an interpreter for such a chain over the link adjacency index and `0084`'s one indexed field is hand-writable at roughly 2,200 links for five courses. **The store is a different case and gets a different mechanism**: 62 MB of vectors should not be re-parsed per invocation.

**What would overturn this:**

- the corpus growing an order of magnitude;
- multi-device sync becoming real;
- the skeleton growing far past roughly 640 nodes;
- **the interpreter for `0101`'s chains ceasing to be hand-writable**;
- **a second concurrent writer** - single-writer is now guaranteed by the subagent contract rather than by the container, so a change to that contract, not to the container, is what fires this condition.

Deliberately not decided here: the actual serialization format and the store's engine.

Source: fall26:records/spec/design.md §5 conclusion 1 (2026-08-27)
