# The size gate is expansion cost, not total graph size

Nothing ever renders the whole graph, so total size is the wrong quantity to budget: what must stay bounded is the cost of going one level deeper. Each level renders what is around it, and one level deeper is one more call.

**Amended at #85 (`0101`).** Both sentences above hold for **fetch** - one block per call - and not for **resolve**, which returns a chain's paths in one call however many crossings it spans. A resolve result is bounded in depth and as wide as the graph makes it; what gates that width is not yet ruled, and total size is the wrong quantity only for the block.

Source: fall26:records/domain/model.md §7; fall26:records/spec/architecture.md §5
