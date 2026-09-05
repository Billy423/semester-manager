# Ring 0's shape is not settled, and reading it as a view is what shows why

`0094` carved ring 0 out of #80 on the ground that it *"is a projection over obligations rather than a node"*, and never said what a projection **is**. This record reads it as a **view** and reports what that reading shows.

**The reading is a lens, declared as one.** It was adopted to answer a single question - *why does ring 0 have no shape a render can be derived from* - and it earns its place by separating parts that three records had each fixed alone. **The four clauses below are not claimed to be exhaustive**, and nothing here is settled by the vocabulary: where the lens and a landed record disagree, the record wins.

**Not a *materialized* view, and the adjective is not a detail.** `0019` rules that ring 0 *"is not a third: residency is an access policy over obligation nodes' fields, not a separate store."* `0089` separately permits a local file as *"the **implementation's** choice"*, a *"regenerable render serving recovery after compaction, not a source of truth"*. Calling ring 0 materialized would decide by vocabulary what `0019` bars and `0089` hands to the implementation.

```
admission    which rows enter        0042   ruled; overturnable, see below
selection    which fields            0038   ruled; not derived
arrangement  how rows are laid out   0041   order ruled; grouping struck at #82
refresh      how it is kept current  0089   ruled on a ground of its own, and not orthogonal
```

The clause names are this repository's own where it has one: **selection** is `0099`'s word - *"`0082` places a field; it does not select one"* - and **refresh** is `0089`'s. *Projection* is deliberately not reused: `0089`, `0094` and `0021` all use it for the whole of ring 0.

## The purpose sentence exists, and nothing is derived from it

`CONTEXT.md` states ring 0's purpose: *"so it can tell where to look next"*. #82 ruled that sentence correct and refused to widen it. **What is undefined is routing** - the mechanism the sentence names - and no clause is derived from either.

`0038` applies the purpose as a **test over `obligation`'s existing field table**: `parts` is out because it answers *what is this about* rather than *where do I look next*. Filtering candidates against a criterion is construction. `0041` grounds its grouping on `0039`'s symmetry rule instead. `0042` partitions on three triggers over the material.

`0070` names the direction this should run: *"Interaction requirements decide which capabilities must exist, never what a method looks like"*, under a title that reads **Derivation runs top-down and construction runs bottom-up**.

**Three of the four clauses come from three sections of one document, and none derives from the section stating the purpose** - `0042` is `ring-0.md` §3, `0038` is §4 and §6, `0041` is §5. That is one defect repeated, not three unrelated gaps. The fourth clause was ruled at #62 and is not part of the pattern.

## What each clause's standing is

**Admission - `0042`, ruled and overturnable.** Three independent triggers put a row in band A; everything else, *"including obligations with no date"*, is band B. #82 ruled that this clause may be overturned once routing is defined, together with what defines *the plan* and what defines *course information*. **`0042` does not itself say that ring 0 ranges over every obligation in a semester**; the nearest statement is `CONTEXT.md`'s `obligation` entry, *"the same nodes ring 0 is a projection of"*, and `0038`'s sizing figure rests on that premise without citing anything.

**Selection - `0038`, ruled and not derived.** Which seven fields are **in** rests entirely on the test above. Its **exclusions carry arguments of their own**, and `grade_share`'s survives audit against the 2c03 corpus: nine assignments at 5 plus 10, 10 and 30 is **95**, the missing 5% is the tutorial requirement whose own note records that it *"has no obligation row"*, and two 1% bonuses sit outside the 100. That corpus was supplied on 2026-09-04 and **is not held in this repository**, so the audit is not reproducible from this checkout. **An argument that stands is still not a derivation**, so neither half of the clause is settled while routing is undefined.

**Arrangement - `0041`, half ruled and half vacant.** The order is ruled and untouched: `due` ascending, nulls last, among nulls by `done_by`, ties broken by the handle, **never array order**, on the ground that array order is insertion order is write history - which owes nothing to routing, and which `0082` inherits. The **grouping** is struck at #82 and struck at source in `0041`: it fixed a value on `0039`'s symmetry rule rather than deriving it from what the view is for.

**Refresh - `0089`, and it is not orthogonal to the others.** Whole lines rather than a field-level delta, because a delta's baseline is eaten silently by compaction (`0043`). That ground is this system's own and needs no purpose. **Two qualifications the lens would otherwise hide:** `0089` parks the refresh **cadence** - *"the deciding variable is how often a refresh happens… it is not settled here"* - and what a refresh **returns** is a line, whose field set is band B, which is the selection clause. Settling selection changes what refresh delivers.

## Why the vacancy was not visible

**Within `docs/adr/`, `0041`'s ruling is cited once, at `0082`, and only for its inline retraction.** `0038`, `0094` and #80 do not cite it. (`research/` reproduces it, but that directory is unmaintained migration scaffolding.) #80's prototype re-derived nulls-last independently and commented *"Ordering it is not ruled anywhere"* at `prototype/collection-render/render.py:80`, while `0041` rules exactly that and rules the null tiebreak too.

**#80 rendered the grouped shape and never judged it on its merits.** `render.py:256` is `A5_grouped_by_course`, whose docstring reads *"The shape CONTEXT.md's `reload` argues against. Rendered so it can be judged."* It implements `0041`'s struck default literally. It is absent from `BANNER.txt`'s itemised list of what #80 ruled against, and ring 0 was carved out of #80 before it was judged. **`0041` and `CONTEXT.md`'s `reload` entry were never read together**, and reconciling them belongs to routing.

## The failure mode a vacant grouping produces

One row per source row, with the relations between rows left to the reader's eye. **The ground for calling that a defect is `0001`'s second job** - *"manage cross-course information in the background"* - which is a statement about relations across obligations rather than about any one of them. **The third job is not available as a ground here**: `0003` routes *what Billy did not ask about* to a deterministic set-difference query, and `0043` bars a resident view from being a query.

**It is not `0040`'s ground, and an earlier draft of this record borrowed it wrongly.** `0040` states *"The ground is not readability - it is the symmetry rule applied to the renderer rather than to the observer"*, and a flat render is uniform across every row, so `0039`'s symmetry rule does not bite it. What transfers from `0040` is its **method**: the table was rendered over real data first and rejected on what it showed.

**A second failure mode, and it is the one that hid the first.** Describing ring 0 as *a set of obligation fields* names the selection clause and invites a node's derivation. `0082` derives a node's render from its kind's field table **because a node's render target is that field table**; ring 0 ranges over `obligation`, which has a field table, but ring 0 is not a kind and has none of its own - `0082` says of its four rules that they *"do not reach a collection at all"*.

## What this record does not decide

**Any clause's content**, and **ring 0's render**, which is not one of the clauses. The render is derived from what the view holds and how it lays rows out, so #82 stays open and is blocked on routing rather than answered here.

**Ring 0's responsibility sentence is not widened.** Making it *supply what the plan needs* was argued at #82 and rejected: *the plan* is undefined, and reaching a plan's inputs across five courses one `look_at` at a time is roughly 55 calls - a figure carrying `0038`'s scope clause, since its evidence base excludes the obligation-dense course. `0039` does not bar such a read; its formalism routes it to **dispatch**. Ring 0 stays narrow on the condition that some cross-node read exists beside it.

Source: ruled at #82 (Billy, 2026-09-04), recorded in that issue's comment. Two blind reviews under four lenses ran over this record before it landed; the first draft claimed ring 0's arrangement had never been specified, which `0041` falsifies, and that claim was retracted rather than weakened.
