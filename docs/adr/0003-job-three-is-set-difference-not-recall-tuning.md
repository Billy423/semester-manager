# Surfacing what Billy did not ask about is a deterministic set-difference query, not recall-tuned retrieval

The third job is served by subtraction over the graph, not by loosening retrieval: the query scans one layer and returns nodes that have no link of the named kind in the named direction. It means exactly that, and never "a node lacking a kind".

```
nodes_without(node_kind, link_kind, direction) -> [Node]
```

Source: fall26:records/spec/design.md §3.4; fall26:records/domain/model.md §6
