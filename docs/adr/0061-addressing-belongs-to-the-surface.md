# Addressing belongs to the surface; every read returns handles

The surface may render a record however it likes and resolve at call time, the way a materialized view does; the `id` is opaque precisely so that nothing at the surface has to mean anything to the layers below. **One constraint binds it: nothing constructs an id, so every read that returns records must return their handles** - a handle absent from the render makes the level below unreachable.

**At the surface the handle *is* the `id`, ruled at #62.** This record's *handle* is not a second kind of value the surface mints or shortens: an id is **unique across the one id space and nothing constructs one**, so the surface prints it and takes it back unchanged, and the read parameter is named `id`. **Opacity is not the property doing the work here, and claiming it would be wrong**: `0026` records that the id space is deliberately *not* uniformly opaque, `course.id` being the supplied course code. A render prints the value unchanged whether or not it means something, and `2c03` is the proof. What survives here is the constraint, which is that a render omitting the addressable value makes the level below unreachable.

Source: fall26:records/spec/architecture.md §5 (Billy, 2026-08-28); the handle/`id` narrowing ruled at #62 (Billy, 2026-09-02)
