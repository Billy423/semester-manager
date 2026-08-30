# A note is an entity that points at a node; `category` is an open string set on purpose, and provenance confers no immutability

A `sticky_note` is an entity that points at a node rather than a property of one, so attach, detach and modify are cheap and symmetric and **maintenance happens at the read**. `category` is an open string set, deliberately not an enumeration, because the cases cannot be enumerated - the price is that the field stores whatever it is given and its write rule is owed (deferral `D24`). `origin` records how the annotation came to exist and **does not confer immutability**: an annotation may be edited, and an edit carries `origin` forward by default.

```
sticky_note := kind · id · category · body · origin · created_at · updated_at
category    : string, OPEN SET, write rule OWED
body        : the kind's ONE free-text field
target      : an `about` link, never a field
```

Source: fall26:records/spec/schema.md §4 (2026-08-27/28); fall26:records/domain/model.md §8.1 (Billy, 2026-08-23) and fall26:records/domain/domain-design.md §10.7 ruling 2; the owed write rules at fall26:records/spec/write-rules.md §4
