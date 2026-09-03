# `0082` places a field; it does not select one, and the first selection cut is the timestamps

`0082`'s four rules answer **where a field lands**. They do not answer **which fields enter the render at all**, and #60 passed over that question in one clause - *"every other field is placed by four rules"* - which reads as *all of them* without ruling it.

**Selection is a separate rule and it does not exist yet.** This record does not supply one. It records the first cut made against the implicit *all of them*, so that the next cut is made against a stated position rather than against silence.

## `created_at` and `updated_at` render, and they are load-bearing

`0046` puts an annotation's **whole body** in the block. `schema.md` §4.5: *"Without `updated_at` a January answer is indistinguishable from today's, and **that silent influence is the actual harm**"*, and §4: the pair *"is what makes a time-bound statement safe to store at all"* - *"an undated sentence from the start of term goes on influencing judgment forever"*.

**The harm is a read-time harm and the render is that read.** Removing the pair from the render voids the field's entire purpose while leaving the field in place. (`schema.md` §4 also names a maintenance-at-read pass as their reader, which has no input until a later kind exists; that does not carry this ruling, because the second harm lands directly on the agent reading the body.)

## `added_at` does not render, and this is a ruling rather than a derivation

Not on the ground that nothing reads it - `grade_share` has no reader by standing exemption and is in the schema. On the ground the schema's own changelog gives:

> `added_at` is kept... **Kept deliberately rather than because a reader was found - no mechanism reads it, and it is deleted when that is clearly permanent.** ... **Per-field assertion times are not carried and are not wanted. What survives of the concern lives on annotations**, where the record IS a single claim.

Two things follow. It is **held pending deletion**, which is a storage-side reason and not a reason to carry it on every read. And the meaning a reader would want from it - *when was this asserted* - is routed by the schema to the annotation timestamps above.

**The dividing line the schema's own wording draws:**

| | |
|---|---|
| `due` | the moment **this obligation** is anchored to |
| `grade_share` | a share of the final course grade - about **this obligation** |
| `added_at` | when **the record** entered the system - about **this row** |

`look_at`'s purpose is to say what the **node** is, not what the **row** is.

**One downstream consequence, stated rather than acted on.** If the render omits it and no mechanism reads it, then nothing reads it - which is the deletion condition its own ruling names. This record does not delete it; it notes that excluding it brings that condition into view.

Source: ruled at #80 (Billy, 2026-09-03); the timestamp arguments and the `added_at` changelog at `fall26:records/spec/schema.md` §1, §4 and §4.5. Those sources do not migrate, so the quotations are carried here.
