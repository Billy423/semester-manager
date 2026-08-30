# An annotation is a tag over two kinds, not a type hierarchy

`sticky_note` and `progress` are two kinds with one shape, distinguished by their `kind` value: both carry `origin`, both carry `created_at` and `updated_at`, and both reach their target through an `about` link rather than a field. A type hierarchy was the obvious move and is forbidden: a subtype that forbids what its parent permits is a Liskov violation, so the three differences become construction-time validation rules instead.

```
shared shape: kind · id · origin · created_at · updated_at
target:       an `about` link, never a field
```

Source: fall26:records/domain/model.md §8.2 and fall26:records/domain/domain-design.md §6.2 (Billy, 2026-08-24); fall26:records/spec/schema.md §4
