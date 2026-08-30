# A date without a time means `23:59` by schema rule, not by parser default

`due` is `Date | DateTime`, nullable, and is the moment this obligation is anchored to - the deadline for something handed in, the start for a sitting. A `Date` **means** `23:59` as a schema-level rule rather than at a parser's discretion, and it is **applied at read time** with the stored value always returned raw; a `DateTime` is a stated time and is never overwritten by that default. `T00:00` is the parser default and was what the system actually did, silently, in all 60 runs.

```
due : Date | DateTime | null
Date            -> means 23:59; applied at read time; stored value returned raw
DateTime        -> a stated time; never overwritten by the default
Date -> DateTime -> ordinary field-grain CRUD (the midterm pattern: a date first, a time later)
which surface applies the resolution -> deferred, D3 item 2
```

Source: fall26:records/spec/schema.md §3 and changelog 2026-08-27 (Billy, via fall26:records/archive/changelog-2026-08-24-slice-1.md); the measured incident at fall26:records/domain/model.md §8.3
