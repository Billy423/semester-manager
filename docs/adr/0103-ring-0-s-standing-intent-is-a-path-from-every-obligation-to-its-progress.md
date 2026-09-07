# Ring 0's standing intent is a path from every obligation to its progress, and its rows carry one field set

`0101` rules that ring 0 is one routing result held resident by policy, and leaves what that result is to #86. This record is that result, derived from the judgments the coordinator must make rather than from `0038`'s field table, together with the formalisation of `0101`'s test and the two type questions its first application left open. Everything here was ruled at #86; the derivation, its drafts and its blind reviews are at `docs/evidence/2026-09-06-issue-86/`.

```
START(obligation) · MOVE(about, pointed-by)[kind = progress]?
```

Every obligation is a start; its progress record is reached by one optional crossing of `about`; an obligation with no record keeps its path with an empty position, which `0035` reads as `not_started`. `course` is a Ref-typed field on the row, a bare pointer whose `id` is the supplied course code (`0026`). The row carries `id · name · due · done_by · optional · course · has-more` at the obligation position and `id · state · origin · updated_at` at the progress position. That is `0038`'s seven with `state` re-typed as a position, reached from the judgments rather than from the field table, which is the direction `0070` asks and `0100` found `0038` did not run.

## The test's formalisation

`0101`'s test: *a form belongs in routing's domain if and only if some judgment the coordinator must make ranges over a set that cannot be produced in one return without it.* Its first application exposed three questions; a fourth arose in review.

- **A form is counted at the grain where removing it changes what a chain can produce.** `FILTER(P and Q)` is a spelling of `FILTER(P) · FILTER(Q)`, so `and` is not a form; `START(ref)` is a spelling of `START(K) · FILTER(id = X)`. `or` is a form, since without it a disjunction is a union and two returns; `not` and `exists` are each a form. Counting is not admission: `or` is counted and not admitted.
- **Two chains produce the same set relative to a judgment**: they produce the same set if and only if they differ only at positions the judgment does not range over. Each must-judgment therefore declares what it ranges over.
- ***Without it* is read over the candidate forms minus the one under test, including inside `exists`.** Two spellings of one production are one form, so a candidate can never be excluded by a spelling of itself; `nodes_without` is a spelling of `START · FILTER(not exists(MOVE))`, and whether it is separately named at the surface is #88's.
- **A superset that carries the discriminator does not produce the set.** A judgment's set is the set as the judgment defines it; otherwise no `FILTER` would ever be necessary at a width the coordinator can hold. Wherever a resolve returns a member the coordinator then judges out, either no must-judgment ranges over the narrower set, or the reading under which the member is in is stated and waked.

## The two type questions

**A crossing may be optional.** A member whose crossing finds no relation is kept with an empty position that names the relation it ranged over, because *what each obligation requires you to know* is a must-judgment and a mandatory crossing would leave the reader unable to tell *requires nothing recorded* from *out of range*, the silence `0081` forbids; the complement fetched separately is two returns. Two consequences the must-list forces: optionality scopes over the crossing together with any selection on its target or its link, so an optional step is empty when nothing satisfies the step's whole selection; and a step from an empty position yields an empty position with the member kept. A path may therefore end at an empty position; every non-empty node position is addressable. The spelling is the grammar's.

**A non-endpoint node position carries one field set per kind, of line depth, derived by the criterion for the judgment.** `0039`'s symmetry is scoped to the set the judgment ranges over, and a judgment over paths may range over any of their positions, so `0101`'s criterion runs at every node position: a position carrying only an id would cost one `look_at` per intermediate, which the one-return premise forbids, and a position carrying a block would carry depth `0043` and `0095` bar. One kind at two positions of one result carries one set. A position's field set is not the kind's line; obligation's differ in both directions. What a relation position carries, when `kind` rides a node position, and obligation's line's field set are the grammar's and are owed; the derivation's draft treatment of them is kept as input at `docs/evidence/2026-09-06-issue-86/drafts/v10.md` §5b.

## The judgments the coordinator must be able to make

A judgment is *must* if it rests on a ruling - `CONTEXT.md`'s opening sentence, `0001` as rewritten, or a ruling Billy makes in session. #14's three-bucket evidence bounds the list and is not a source of it; Billy's raw decomposition in #84 and #85's scenarios are candidates, each derived or parked with a wake.

| | judgment | source | served by |
|---|---|---|---|
| J0 | what to do next, across five courses | Billy, in session | its set by the standing intent; two observations besides (below) |
| J1 | what is owed, across five courses, dated or not | opening sentence | the standing intent |
| J2 | which concepts each obligation requires | opening sentence | `START(obligation) · MOVE(requires, points-at)?`; whether one hop or the closure is #88's, with J2 as its candidate |
| J3 | where the material that teaches those concepts lives | opening sentence; `covers` is the teaching relation | `· MOVE(covers, pointed-by)?` |
| J4 | which obligations require the same concept, and which concept, across the set | `0001` job 2 | `START(obligation) · MOVE(requires, points-at)? · MOVE(requires, pointed-by)?[kind = obligation]`; the same-course pair stays in and the self-pair is out, each a stated reading with a wake |
| J6 | which concepts no artifact covers | `0001` job 3, via `0003` | `START(concept) · FILTER(not exists(MOVE(covers, pointed-by)))` |
| J7 | which artifact states this obligation's requirements | `0001`'s requirements sentence | `MOVE(spec, points-at)[role = given]?`; that `given` names the stating artifact is this record's reading of `0012`'s enum, waked on a gloss |
| J8 | which obligations build on which, across the set | `0001` job 2 | `START(obligation) · MOVE(builds-on, points-at)?` |

*Which items need Billy* (#14's third bucket) is a candidate with an owed predicate; Billy's own comments, lecture progress, and material reached by `spec`'s `owed` role or `prepares-for` are candidates parked with wakes. J5's number is kept vacant so the evidence stays readable.

## Why the intent is what it is

**From `obligation`, not from `course`.** A start from `course` would let a course with no obligation speak for itself, and it silently loses an obligation whose `course` ref dangles - legal by `0018`, produced by landing before the course, by a course's deletion, or by a code no course has (`0026`, `0091`). An owed member kept with a bad pointer beats an owed member dropped; the dangling ref is a defect `0018`'s owed validation pass repairs, extended to Ref-typed fields. A union of two starts is outside the vocabulary and two returns.

**No predicate.** No ruled source names a judgment over *the active ones* as a set; which obligations are near is the coordinator's judgment against today, made with `due`, `done_by` and `state`. Four readings are stated, each waking on the first real decision observed by hand: an `optional = true` obligation is owed (`0031`'s null is in on the same reading); a `done` obligation stays in the set, the system being a knowledge base and not a reminder system; one term, since no record confines the skeleton to a term and whether `course` carries a term field at all is a conflict between `CONTEXT.md`'s *the line* and `0094` on one side and `0037` row 11 on the other, reported and parked on a second term landing; one progress record per obligation, read from `0035`'s *one current value per target*.

**To `progress`.** *What is owed* turns on whether a thing is done, and `state` is `progress`'s field by `0035`, which argues against moving it (#71 holds the question). `0046` is a delivery rule about a node's neighbourhood and this is not that read: the progress position carries a field set and not content, which still arrives only through `look_at`'s channel.

**Width.** Roughly 55 obligations for five courses, a fall26 number, not auditable from this checkout, whose evidence base excludes the obligation-dense course; #80's 6,482 and 7,598 characters at that row count are a floor, since every row grows by `done_by`, `optional`, `has-more` and the progress position. `0101` leaves the width gate unruled and this record does not rule it; the bet is recorded, waking on a measurement that includes the dense course or on a second term landing.

**The time projection is not resident**; it is an on-demand intent over `due`, and what it holds is #13's. `refresh()` returns rows, and a change at the progress position is a change to the row.

## What a row carries

Under the criterion - a field belongs on a position if and only if, without it, the coordinator cannot form its next intent or cannot decide whether to spend the next call - for J0 and J1, over field lists assembled from `0025`, `0027`, `0028`, `0029`, `0031`, `0032`, `0033`, `0035`, `0036`, `0037`, `0038` and `CONTEXT.md`, since no landed record carries either kind's table:

- **In at the obligation position:** `id` (the address); `name` (an id says nothing about the record); `due` (an obligation is a thing with a deadline, and *near* is judged against it); `done_by` (Billy's chosen target); `optional` (whether it is to be done at all); `course` (a judgment across five courses needs the pointer); `has-more` (the in-band carrier of which vocabulary applies here, `0092`'s value unchanged; that a row whose progress position is non-empty states `about` twice is #82's collapse).
- **Out at the obligation position:** `kind` (fixed by the step; the element's name prints it); `parts` (J2's, not J0's or J1's; returns with any `look_at`); `grade_share` and its qualifier (the criterion's verdict for J0 is open; `0038`'s independent corpus argument closes it - a column of shares reads as a partition it is not); the pointer to a conditional weight's rule (`0032`); `added_at` (`0099`'s row-versus-node ground).
- **In at the progress position:** `id`; `state` (what is owed turns on it); `origin` (whether to spend a call re-confirming an `in_progress` depends on how it came to exist, and `0056` makes an asked answer's provenance loud at every read); `updated_at` (`0099`'s harm, a January answer indistinguishable from today's, lands on a resident `state`).
- **Out at the progress position:** `kind`; `detail` (a position is of line depth, the one bound imported from the render records; content arrives with `look_at`); `created_at`; `has-more`.

A ring 0 **row** is not obligation's **line**. The line is what a neighbour renders as inside an `<edge>`, `0082` set it by transfer from band B, and band B dissolves here, so the line's field set is owed at #90; `0096`'s worked example stands as the landed shape until the criterion is run over a neighbour.

## Size and absorption, and what `0042` becomes

Deciding what to do next needs an obligation's size and the owner's absorption of a concept - Billy's ruling, and he is the only witness. Neither is a form. Absorption is an owner-authored observation on a member, under `0039`'s rule: it is asked per obligation until its record exists, and that record, if it is an annotation at all, would hang on a `concept` node behind a layer that does not exist (#25). Size's route is open: `0037` row 1 bounds the answer to an ordinal comparison and was not written to say whether that is a per-member value. What record holds either answer - kind, location and type - is parked whole; `0033`'s *not another field* and `0037`'s no-re-add rule bind a field, and `0010`'s stateless clause binds a field on `concept`. Wake: the first real decision observed by hand, read for the shape the answer took (`0068`). `0042`'s sentence barring a notion of importance is not overturned - it bars a promotion rule, and J0 is Billy deciding with the system supplying inputs. `0037` row 1 named `parts` as a first source of size against `0033` and `CONTEXT.md`'s `parts` entry; it is repaired on `0033`'s side.

**`0042` was a per-row field-set partition, not an admission clause.** Every obligation entered; the partition chose which rows carried three more fields, because not every concern deserved attention. Under `0101` a result carries one field set per kind, which is stricter than `0039`'s symmetry, and the concern changes hands: the coordinator holds a symmetric set, judges which members are near, spends `look_at` on those and drops what it fetched (`0043`). The three triggers survive as the coordinator's judgment rule; the band names and band B's reduced set dissolve; `0100`'s placement of `0042` under admission is corrected.

## Deliverable 4, and the forms parked

Filtering on a link's own fields is a selection at a relation position - a predicate ranges over the vocabulary, and `0017` puts a link's fields in it - admitted by J7. Crossing a Ref-typed field from a computed set has no must-judgment today and is parked, waking on a must-judgment from a ruled source that needs a course's fields on the path or starts from a computed set of courses; the position comparison is parked, waking on a must-judgment that excludes a member by a value at an earlier position; `or` is parked, waking on a must-judgment that ranges over a union. `0102`'s membership row stays open. `REPEAT` is #88's.

## Considered and rejected

**A three-position path from every `course`**, so that an empty course would speak for itself: it silently loses a dangling-ref obligation, which is the omission axis, and a course with no obligation is a judgment no ruled source names.

**A term predicate as a chain over `course`**: it loses the same obligation, and the value it compares against is held nowhere.

**A reachability constraint on the observation's record**, from which a size field on `progress` followed: it read `0101`'s one-return premise for per-member observations, which are `0039`'s, and chose a field two landed records forbid without a ruling.

**Ruling the grammar-level consequences the derivation used** - what a relation position carries, when `kind` rides a position, obligation's line - in this record: they are the query grammar, which #85 placed after this map, and four review rounds found each rule applied at one seam and not the next until they were demoted.

Source: ruled at #86 (Billy, 2026-09-07), in that issue's resolution comment; seven session rulings first recorded there, and the full statement at `docs/evidence/2026-09-06-issue-86/drafts/v10.md`, whose §5b is a draft and not part of this record.
