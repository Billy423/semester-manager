# The size gate is expansion cost, not total graph size

Nothing ever renders the whole graph, so total size is the wrong quantity to budget: what must stay bounded is the cost of going one level deeper. Each level renders what is around it, and one level deeper is one more call.

Source: fall26:records/domain/model.md §7; fall26:records/spec/architecture.md §5
