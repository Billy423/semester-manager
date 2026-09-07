# Active is three independent triggers on one question, and they are the coordinator's judgment rule rather than ring 0's partition

An obligation is *active* if any one of three things holds. **Breadth is never treated as a defect:** a request for a whole semester that gets a whole semester is answering what was asked, and the useful window is a requirement Billy stated rather than a fix the system applies on his behalf.

```
active := due     ∈ [today-7d, today+14d]
       OR done_by ∈ [today-7d, today+14d]
       OR state   == in_progress
```

**The three triggers are the coordinator's judgment rule, not a partition of ring 0 - ruled at #86 (`0103`).** This record first ruled them as ring 0's partition into two bands, band A carrying three more fields than band B, on the ground that not every concern deserves attention. Every row entered; the partition chose what a row carried. Under `0101` a routing result carries one field set per kind, which is stricter than `0039`'s symmetry rule and is what the partition fails, so the bands dissolve and the concern changes hands: the coordinator holds a symmetric set, judges which members are active by these triggers, spends `look_at` on those, and drops what it fetched (`0043`). It may widen the date window in an exam week without the system changing. No ruled source names a judgment that ranges over *the active ones* as a set.

An undated obligation is in the resident set and that is not a hazard: **it is present, it is routable**, and its detail is one call away. The standing intent's range is every obligation, dated or not (`0103`). **The system holds no notion of an obligation's importance** - `grade_share` has no reader by standing exemption - so a rule promoting "important" undated rows would assert a judgment the system is ruled not to make. #82 authorised #86 to overturn this sentence once routing was defined, and #86 did not: it bars a promotion rule, and the coordinator deciding what to do next with inputs the system supplies is not one.

Source: fall26:records/spec/ring-0.md §3 and changelog (Billy, 2026-08-28); the window's earlier standing at fall26:records/domain/domain-design.md §2 and changelog 2026-08-28; the partition dissolved and the triggers re-homed at #86 (Billy, 2026-09-07), `0103`
