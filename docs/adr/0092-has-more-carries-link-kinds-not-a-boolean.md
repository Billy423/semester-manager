# `has-more` carries the link kinds present on the node, not a boolean and not a count

`0038` puts `has-more` among band A's routing fields without saying what it holds. It holds **the set of link kinds present on that node, drawn from `0012`'s table** - today only `about` and, by signature, `builds-on`; after the artifact and concept layers, also `spec`, `requires` and `prepares-for`.

**The ground is not information content, which today equals a boolean's.** It is that the vocabulary is **derived**. `0012` is a closed table, so the set gains members as those layers land without this field's description changing a word - and by #12 item 8, a tool definition whose description does not change is not a new version. A boolean or a count would each have to be re-ruled at G5 against data that does not exist yet.

**What it answers.** Ring 0 cannot list a node's neighbourhood, so without this field the coordinator's next call is a gamble that this one look holds what it wants. A boolean says only *there is something*; the kind says *what kind of thing is through there*, which is what decides whether the call is worth making.

## Considered Options

**A boolean, or a count.** Rejected above. A count also answers *how much*, which does not route.

**Deferring the field to G5 and shipping band A with six fields.** Argued and withdrawn. It rested on reading `0046` as putting `about` outside this field's scope, which made the field look permanently false. `0046` is a **delivery** rule - annotations reach the reader through their own channel rather than as ordinary neighbours - and it does not bar signalling that one exists. With `about` in scope the field discriminates today: 6 of 14 obligations in the 2c03 fixture carry an annotation. `builds-on` is admissible today too, since `0012`'s signature needs neither deferred layer.

**Reading it as *anything beyond the band's own fields*.** Rejected on measurement: over the 2c03 fixture the union of a non-empty `parts`, a non-null `grade_share` or an attached annotation is 14 of 14, and 21 of 22 over the wider two-course fixture. A field that is true of everything routes nothing. (Those counts are not auditable from this checkout; see `0079`'s standing.)

## What this record does not decide

**What the field is called.** `related-by` was the live proposal after `link-kinds` was rejected for using schema-internal words, and neither survives: `0093` criteria 2 and 4 cannot both be met while the value is a link kind, because any name that honestly says what the value holds uses the schema's vocabulary. The name travels with **ring 0's own render**, which is where the field now lives.

**Where it lives is decided.** #80 ruled it **absorbed** in a node's render: `<neighbours>` lists the edges, so their kinds are readable off them, and carrying the projection beside them states one fact twice - which is the `0024` bite this section anticipated. It survives **only where the neighbourhood cannot be listed**, and that is ring 0. This record's ruling on the field's **value** is untouched; what moved is where it appears (`0096`).

## A gap in `0082` this exposes

`0082` derives a render from a kind's field table by four rules. **`has-more` is in no field table**, and neither is `role`, which is a `Link` field (`0017`). That record declares one exception today, for `grade_share`'s qualifier, and owes a second covering these two.

Source: ruled at #62 (Billy, 2026-09-02). The field's membership in band A is `0038`'s; its value is this record's.
