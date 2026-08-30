# Four conventions that range over every kind

`null` means **no record**, never a default, and must render as absence; there is **at most one free-text field per kind**, and `course` has zero, which is a cap and not a quota; **every field is individually CRUD-able**, so landing performs partial update and never whole-record replacement; timestamps are ISO 8601, with `added_at` on `course` and `obligation` and `created_at`/`updated_at` on the annotation kinds. The cap is only tractable because there is no catch-all `notes` field: a negative definition cannot be non-overlapping, which is ADR `0024` seen from the field end.

```
null       -> no record. Never a default. Must render as absence.
free text  -> at most one field per kind. course: zero.
mutability -> field grain; landing = partial update, never whole-record replacement
timestamps -> ISO 8601; added_at on course, obligation; created_at + updated_at on annotations
```

Source: fall26:records/spec/schema.md §1; fall26:records/domain/domain-design.md §6; fall26:records/spec/architecture.md §7
