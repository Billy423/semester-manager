# Active is three independent triggers on one question, not a time window with exceptions

An obligation is in band A if any one of three things holds; everything else, including obligations with no date, is band B. **Breadth is never treated as a defect:** a request for a whole semester that gets a whole semester is answering what was asked, and the useful window is a requirement Billy stated rather than a fix the system applies on his behalf. Two bands do not violate uniform depth, because the partition is computed from material facts plus one rule applied identically to every course, so it carries no interaction history.

```
active := due     ∈ [today-7d, today+14d]
       OR done_by ∈ [today-7d, today+14d]
       OR state   == in_progress
```

An undated obligation is in band B and that is not a hazard: it is present, it is routable, and its detail is one call away. **The system holds no notion of an obligation's importance** - `grade_share` has no reader by standing exemption - so a rule promoting "important" undated rows would assert a judgment the system is ruled not to make.

Source: fall26:records/spec/ring-0.md §3 and changelog (Billy, 2026-08-28); the window's earlier standing at fall26:records/domain/domain-design.md §2 and changelog 2026-08-28
