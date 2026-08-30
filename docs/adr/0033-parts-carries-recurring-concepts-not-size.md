# `parts` carries the concepts that recur, as canonical singular names, and does not carry size

`parts` carries the concepts an obligation's source carries, as raw strings and never as pointers to concept nodes. A part is **a concept worth capturing because it might occur elsewhere in the system**, and the writer writes the canonical singular name rather than the phrase the source used; **recurrence decides whether a string becomes a concept and separability decides at what grain it is cut - two tests, two jobs.** It does not carry size: the replacement for the removed ordinal-size mechanism is not another field but an interaction.

```
parts : [string]   -- concepts, raw strings, never Refs

kept:    Graph · Queue · Big-O · Linked List
dropped: Multiple Choice · Problem Solving   (noise, caught by separability not recurrence)
         Monte-Carlo · A5Tree               (one-off, local)
```

Source: fall26:records/spec/write-rules.md §3.4 (Billy, 2026-08-28); fall26:records/spec/schema.md §3 and changelog ×2 2026-08-27; the ring-0 exclusion at fall26:records/spec/ring-0.md §4
