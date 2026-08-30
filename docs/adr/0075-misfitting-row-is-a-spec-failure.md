# A real row that does not fit the field set is a spec failure, not a fixture patch

The rejected alternative - patching the fixture so the build can continue - is invisible once taken and destroys the evidence that the spec was wrong. The cost is that one row can stop a build.

What happens to the interrupted work afterwards is not ruled here.

Source: fall26:records/plan/application-tier.md §5 (nothing in the domain or spec records states what happens when real material does not fit)
