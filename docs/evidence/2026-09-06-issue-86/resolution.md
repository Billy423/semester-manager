## Resolution - ruled at #86 (Billy, 2026-09-06)

**What this comment is.** The four things this ticket was given under `0101` - the necessity test's formalisation, the two type questions, which judgments the coordinator must be able to make and what they make ring 0, and the two forms the body asked about - plus the plan's scoping point and the `0042` overturn #82 authorised. This comment carries the rulings and the results; the derivation behind each, its ten drafts and its eighteen blind reviews are at `docs/evidence/2026-09-06-issue-86/`, and `drafts/v10.md` there is the full statement this comment summarises. Billy's posting of this comment rules what it lists; everything the derivation used beyond that is a draft input to the grammar and the sibling tickets.

### Rulings made in the session

1. **The plan's representation stays at #14.** This ticket decides only which reads a plan's inputs require; #58's *Out of scope* line gains that one clause.
2. **Size and absorption are observations, not forms.** Deciding what to do next across five courses needs both, and neither is something a chain produces. Absorption is an owner-authored observation on a member, reaching the coordinator by asking until its record exists. Size's route is open: `0037` row 1 bounds its answer to an ordinal comparison and does not say whether that is a per-member value. What record holds either answer is parked whole - kind, location and type - with the first real decision observed by hand as its wake. `0042`'s sentence barring a notion of importance is not overturned.
3. **Ring 0's rows carry one field set.** `0042`'s band partition dissolves; its three triggers become the coordinator's judgment rule for *near*, which it may widen in an exam week without the system changing.
4. **The standing intent starts from `obligation`, with `course` a Ref-typed field on the row and no predicate.** One term is an assumption the width bet carries.
5. **Arrangement is assigned to #82**, widening it from the render to the arrangement clause, with `0041`'s order as its first input.
6. **#14's three-bucket evidence bounds the must-list and is not a source of it.** *Which items need Billy* is a candidate, parked.
7. **An obligation whose `course` ref dangles is kept, not dropped.** `0018` tolerates the ref; a start from `course` would lose the obligation silently, and an owed member kept with a bad pointer beats an owed member dropped.

### The result

Ring 0 is one routing result held resident by policy (`0101`), and this is the result:

```
START(obligation) · MOVE(about, pointed-by)[kind = progress]?
```

Every obligation is a start; its progress record is reached by one optional crossing; an obligation with no record keeps its path with an empty position, which `0035` reads as `not_started`. The row carries `id · name · due · done_by · optional · course · has-more` at the obligation position and `id · state · origin · updated_at` at the progress position, each field admitted by `0101`'s criterion for the judgments the resident result serves. That is `0038`'s seven with `state` re-typed as a position, reached from the judgments rather than from the field table, which is the direction `0070` asks and `0100` found `0038` did not run.

**Four readings are assumed and stated, each with the first real decision as its wake:** an `optional = true` obligation is owed; a `done` obligation stays in the set; one term; one progress record per obligation.

**The must-list** (§3 of the full statement): what to do next across five courses (Billy's ruling); what is owed; which concepts each obligation requires; where the material teaching them lives; which obligations share a concept, and which build on which, across the set (`0001` job 2, from a start by kind); which concepts no artifact covers (`0003`); which artifact states an obligation's requirements (`0001`'s requirements sentence, over `spec`'s `given` role). Each is one chain over the admitted forms. The same-course pair and the self-pair in the concept-sharing judgment are readings, stated and waked.

### The test, and the two type questions

**The formalisation.** A form is counted where removing it changes what a chain can produce, so `and` is a spelling and `or`, `not` and `exists` are forms; two chains produce the same set relative to the judgment that ranges over it; *without it* reads over the candidate forms minus the one under test, including inside `exists`; and a superset that carries the discriminator does not produce the set. The test can now be run; its instrument standing is unchanged.

**A crossing may be optional**, empty when nothing satisfies the step's whole selection, and a step from an empty position keeps the member with another empty position. **A non-endpoint node position carries one field set per kind, of line depth, derived by the criterion for the judgment.** `0101`'s *endpoint* becomes *position*.

**Deliverable 4.** Filtering on a link's own fields is admitted, as a selection at a relation position, by the requirements judgment. Crossing a Ref-typed field from a computed set has no must-judgment today and is parked; so are the position comparison and `or`, each with a wake. `REPEAT` is #88's, with the requirements judgment's hop count as its candidate.

### What binds the sibling tickets

- **#82** - unblocked; receives the standing intent, the row, the arrangement clause with three inputs, `has-more`'s collapse on a row that shows `about` twice, and notice that two items on its *must not be re-opened* list have moved.
- **#88** - the admitted forms are `START(K)`, `MOVE(L, D)` optional or not, a selection at a node or a relation position, `not`, `exists`; three forms parked with wakes; the full statement's §5b is its draft input.
- **#87** - untouched. **#79** - within this map, still blocked on #87 and #88.
- **#16** - its wake gains six readings, each a first real decision observed by hand.
- **#13, #14, #25, #71** - one comment each, as the full statement's §9 lists them.
- **One new deferred issue** - obligation's line's field set, owed since band B dissolved.

### Amendments - ruled by this posting

One new record holding the formalisation, the two type rulings, the must-list, the intent, the row, the stated readings and `0042`'s re-placement. Repaired in place: `0101` (*endpoint* to *position*; its grammar clause split), `0042` (restated), `0038` (restated), `0100` (the clause table and the refresh paragraph), `0037` row 1 (`parts` dropped as a source of size, on `0033`), `0082`, `0095` and `0096` (pointed at the line debt), `0089` (rows, not lines), `0046`, `0019`, `0018`, `0092` (band A struck at source), and `docs/adr/README.md`. `CONTEXT.md` via the domain-modeling skill: `ring 0`, `band A` / `band B`, `obligation`, `path`, `the line`, `applies`, `closure`. Pointer debts listed: `0091`, `0093`, `0094`, `0102`, `0013`, and `0096`'s clause that now bites at #82. The full list, with each edit named, is §10 of the full statement.

### Not decided

The grammar, including everything in the full statement's §5b: what a relation position carries, when `kind` rides a position, obligation's line's field set (owed, new issue), and the spelling of every form. The width gate, and the bet against it. The term predicate and where a current-term value is held, on a second term landing. The record that holds a size or absorption answer, and the shape of size's answer. *Which items need Billy*, lecture progress, and Billy's own comments as judgment inputs. What the time projection holds (#13). `closure` and `REPEAT` (#88). Who serves an intent by content (#87). Whether `state` moves onto `obligation` (#71). Whether dispatch calls count against the effectiveness constraint, now with an instance. The repair reads the test does not reach.

**Standing of the numbers.** The roughly-55 figure, the 6,482 and 7,598 character measurements, the 6-of-6 bucket replication and the 95-of-100 share column are fall26 numbers or rest on a corpus this repository does not hold, and none is auditable from this checkout.

### How it was reached

By grilling, from the judgments outward, then ten drafts and nine rounds of blind review under two lenses. The first three rounds changed the substance, and Billy ruled each change: the start from `obligation`, no term predicate, no chosen location for the observation's record. The next four found one move at four seams - a field set transferred from a render record onto a routing position the criterion should have derived - and each repair added a rule that the next round found applied at one seam and not the next. Those rules are the query grammar, which #85 placed after this map; the eighth draft demoted them to a draft section and ruled only what the ticket was given, after which the attribution lens found nothing blocking and the falsification lens found two single-cell readings per round, each repaired as a stated reading with a wake. Billy stopped the reviews after the ninth round. The pre-registration scored four of seven predictions hit; the yield was outside the list.
