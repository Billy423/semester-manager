# Ring 0 carries seven routing fields; `parts` and `grade_share` are excluded, and `grade_share`'s exclusion is measured

Ring 0 carries `course`, `name`, `due`, `state`, `optional`, `done_by` and `has-more`; band B drops the last three. `parts` is out because it answers *what is this about* rather than *where do I look next*; `grade_share` is out because a rendered column of shares reads as a partition of the grade that it is not, which is the single largest measured faithfulness defect in the corpus. **Excluded from the projection is not unreadable**: ring 0 governs residency, and `parts` comes back with any read of the obligation record.

```
band A "active" : course · name · due · state · optional · done_by · has-more
band B "known"  : course · name · due · state
neither band    : parts · grade_share · grade_share_conditional
```

**The only sizing number that matters is that ring 0 for five courses is roughly 55 obligations.**

**The measurement behind `grade_share`'s exclusion, carried inline because its source does not migrate:** the share-as-partition defect is 24 claims across 17 runs; with a floor restated as a point value it is 29 of 77, **38% of every measured faithfulness failure**, and the only defect kind appearing in every configuration group. All 60 runs were graded by an independent grader given the run's own tool output and its answer and nothing else: over 870 run-item pairs, **77 unsupported · 32 contradicted · 449 well-handled**. **Standing: these numbers have not been re-derived structurally, which the source's own warranty asks for before any of its metrics is trusted.** An independent corpus argument survives without them - one course's share column sums to 95, the missing 5% has no row, and two 1% bonuses sit outside the 100.

Source: fall26:records/spec/ring-0.md §4 (field set) and §6 (the exclusion); the measurement at fall26:records/findings/read-cycle.md §5, carried a second time at fall26:records/domain/model.md §10 item 9
