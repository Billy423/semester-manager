# A nullable bool means unknown; the writer supplies the obvious default, not the schema

`optional` and `grade_share_conditional` are nullable bools where **null means unknown, never the negative** - a non-nullable bool forces the system to assert what no source stated. A separate **write rule** tells the writer to supply the obvious value where a person would not hesitate, which leaves a stored null meaning the writer genuinely could not tell. This is a rule about the writer, not about the field, and the schema is unchanged by it.

```
schema     : bool | null, null = UNKNOWN (never "not optional", never "not conditional")
write rule : default it where the answer is obvious (optional defaults to false unless a source states otherwise)
=> a stored null means the writer could not tell
```

Source: fall26:records/spec/schema.md §3; the write rule at fall26:records/spec/write-rules.md §3.5, its owed generalisation at §1.2
