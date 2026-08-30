# `kind` is a required discriminator, not metadata, and `layer` is a different axis

Every node record carries a required discriminator field named `kind` whose value is that kind's own name; it selects which declared field set the payload has, and a record cannot be constructed without it. Shape-sniffing was the live alternative and loses because dispatching on which fields are present is exactly the control-flow trigger the refactor commitments forbid. **`layer` is a different axis** and only three kinds have one.

Source: fall26:records/spec/schema.md §1; fall26:records/spec/design.md §3.1
