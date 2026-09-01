# The render is XML, and one render serves both readers, replacing the human-branch / machine-branch split

`fall26:records/spec/architecture.md` §5 ruled **human-readable by default with a machine branch**, plus a guard: *"any locator the next call needs must appear in the human render too - never only in the machine branch."* That guard exists because two branches drift, and *"what is omitted for readability is what the next call needs."* **One markup render removes the branch, so the guard becomes unbreakable rather than something to observe.**

**XML rather than JSON, on the rule JSON cannot express.** Of `0082`'s four rules, JSON carries three natively - a repeat is an array, a `Ref` is a nested object, a scalar is a key. **It has no position for the third.** In JSON the kind's one free-text field is another key, indistinguishable from `category` or `state`, so rules 3 and 4 collapse and the line between *what the thing itself is* and *a fact about it* disappears. An element's single text content is that position, and it is not a special case: `0028`'s cap is repository-wide - *"at most one free-text field per kind, and `course` has zero, which is a cap and not a quota"* - reaching `sticky_note.body`, `progress.detail`, and `artifact.summary` when that layer lands.

XML also carries **both containment and attributes**, which `0082` uses to separate *another value* from *a qualifier on this value*, and YAML and TOML have containment only. That is a convenience rather than the ground: the qualifier distinction has exactly one instance today.

**This does not re-assert the JSON premise `0060` rejected.** That record's correction reads: *"an agent-protocol tool result **can** carry rendered text and not only JSON"*, aimed at a future reader who re-opens the surface decision by assuming JSON. Markup is text that carries its own structure, which is the third option neither the JSON premise nor plain prose covers - and prose is ruled out independently, because a node's own typed fields must **arrive at a stated position** (#12 item 4) and prose dissolves the field structure.

The predecessor record is frozen and is not edited; it stands as provenance, and this record is the current statement.

Source: ruled at #60 (Billy, 2026-09-01), superseding `fall26:records/spec/architecture.md` §5's format split. The rejected-JSON-premise correction is `0060`.
