# One lecture is one node with a file list, not one node per file

One lecture may be several files, so an artifact carries a file list with a `variant` tag rather than splitting into several nodes or acquiring a version link. Union is required, not subsumption: in 2 of 11 measured pairs each side holds content the other lacks. **Filename similarity must never imply a relation** - one same-named pair was two different lectures (Jaccard 0.21).

```
artifact := ... · files[]{ variant, text_extractable } · revised_at
```

Source: fall26:records/domain/model.md §8, §9
