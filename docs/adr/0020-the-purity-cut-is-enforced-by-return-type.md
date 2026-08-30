# The purity cut is enforced by return type, not by tool registry or prompt

The store has two access modes - **by-handle** (a lookup on `chunk.node_id`) and **by-query** (nearest-neighbour over embeddings). The coordinator holds neither: it holds the skeleton interface only, and the skeleton's return type has no field a chunk could arrive in. The cut sits above both store modes, not between them, and **the type-level version is preferred because it survives a change of container.**

Source: fall26:records/domain/model.md §5; fall26:records/spec/design.md §3.5
