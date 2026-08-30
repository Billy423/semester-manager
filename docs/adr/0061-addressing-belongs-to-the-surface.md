# Addressing belongs to the surface; every read returns handles

The surface may render a record however it likes and resolve at call time, the way a materialized view does; the `id` is opaque precisely so that nothing at the surface has to mean anything to the layers below. **One constraint binds it: nothing constructs an id, so every read that returns records must return their handles** - a handle absent from the render makes the level below unreachable.

Source: fall26:records/spec/architecture.md §5 (Billy, 2026-08-28)
