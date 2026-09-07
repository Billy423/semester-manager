# Routing is the resolving half of the query: a system-held function from an intent to the paths that satisfy it

`CONTEXT.md` states ring 0's purpose - *"so it can tell where to look next"* - and `0100` found that nothing was derived from it because the mechanism the sentence names, routing, was undefined. This record defines it.

```
routing : intent -> { path }
```

The query has two halves. **Fetch** takes an address and returns its render - `look_at(id)`, a read. **Resolve** takes an intent the caller can state in the skeleton's structural vocabulary and returns the paths that satisfy it, each ending at a position, which is an address where it is non-empty (`0103`). **Routing is resolve.** Fetch may compose a resolve step into a render - `0084`'s `obligations.list(course)` inside `look_at(course)`, and the neighbourhood section `0094` places in every block - which is resolve entering through fetch and not fetch becoming routing.

**Who holds what.** The system holds routing, and holds by policy one standing intent whose result is ring 0 - a path from every obligation to its progress record, ruled at `0103`. The coordinator holds the intents it forms and that one result resident. A dispatch target holds nothing. No new holder is introduced.

**Routing is not prompt-driven.** *Unprompted* does not mean *without the owner*: it means an intent must be formable from the vocabulary plus what the current render exposes. The vocabulary - the current kind set, and the closed link-kind set with its signatures (`0012`) - reaches the coordinator out of band, by a carrier #79 decides. Which of it applies *here* reaches the coordinator in-band: `0098` spells names back, `0096`'s `<edge>` carries `type` and `direction`, and `0092`'s `has-more` lists a row's link kinds wherever ring 0's render places it. `look_at` is this system's introspection over a vocabulary the coordinator already has.

**What routing is not.** Not a search (`0046`); not the delivery of an answer, which is fetch; not a judgment of importance, since a judgment is made *with* operations and is never an element of an operation set; not a statement about renders. Mechanistic reachability - that a path exists in the skeleton - is a property of the schema, deliberately not universal, and not routing's.

## Input: an intent, a chain over the vocabulary's relations

An intent is stated in the skeleton's structural vocabulary: a node's kind, id and fields, `kind` itself a field (`0027`); Ref-typed fields (`0018`); links as records of their own (`0016`, `0017`); the closed link-kind set (`0012`); `points-at` and `pointed-by` (`0096`); annotations as node kinds reached by `about`. The vocabulary contains no set operations and no content.

**An intent is a chain over the relations the vocabulary names** - link kinds in their directions, and Ref-typed fields in either direction - **with predicates over the vocabulary that may join**: a predicate may itself contain a chain from the member it tests. Chaining is one call. Set operations are not composition.

**The domain is bounded by this vocabulary, not derived from it.** Which steps a chain may contain, what a chain carries from step to step, what a predicate may reference on the path behind the member, and how any of it is spelled - all of that is the query grammar, which #84 places after the map that ruled this record, and which is decided by the judgments #86-#88 supply under the test below. Whether a crossing may be optional is ruled at `0103`: it may, and an optional step is empty when nothing satisfies its whole selection. The first application of the test, with the forms it used, is a draft in #85's resolution and is not part of this record.

**Outside the domain by type:** an intent by content. No predicate ranges over content. Who serves such an intent is #87's. **Placed but not admitted:** the store's by-handle read, a step onto the other persisted thing across `0019`'s one coupling field; whether it enters routing's domain is #87's.

**An address** is a handle fetch accepts: a node's `id`. Whether an edge's `id` is one turns on whether the two ids share one space, which `0025` scopes to link endpoints and no record settles.

## Output: paths, not endpoints

**Routing returns a set of paths.** A path is the chain a member arrived by - node, relation, node, … - ending at a position, which is an address where it is non-empty, and each node position carries what decides whether it is worth the next call (`0103`). Paths, because a judgment across obligations is a judgment about their **relations**: `0100` grounds the flat-render defect on `0001`'s second job, *"a statement about relations across obligations rather than about any one of them"*, and a set of endpoints has no position for a relation. Obligations sharing a concept, as endpoints, is `{A, B, D}` with the pairing gone; as paths it is *A - requires → c - requires ← B* and the judgment can be made. What a non-endpoint node position carries is ruled at `0103` - one field set per kind, of line depth, derived by the criterion for the judgment; what a relation position carries, whether a path may repeat a node, and how paths are deduplicated are the path's precise type, which is the grammar's.

**Not bare ids**, because an assigned id says nothing about the record it names (`CONTEXT.md`, `id`). Each position carries its own kind's deciding fields - one set per kind - and no depth; which fields decide the call for an obligation is downstream, and for `concept` and `artifact` it is the debt #17, #19 and #20 carry. **The set is symmetric**: every position at one depth, and where paths differ in shape that asymmetry comes from the material, which `0039` calls legitimate. **The set is unordered**; arrangement is ring 0's clause. **An empty result names what it ranged over**, so a reader can tell *not in this range* from *not known* (`0081`); an intent the system cannot yet serve is refused, never returned empty.

**Affordability is a separate question the type does not answer.** A resolve over a whole kind, or a repeat, may be too wide to hold. `0039`'s affordability is per-member depth and #12 item 6's bound is on free text; no landed record bounds a result's width. **What is known about cost:** a start by ref and one crossing is O(degree) (`0046`); a start by kind is O(kind); a join costs one sub-chain per member; a repeat is closure-sized. These are the only cost statements bearing on the open width gate, and #88 needs them for the repeat.

## The premise and the test

**A judgment ranges over a set, and the set arrives in one return.** This is a direct ruling, stricter than either of its grounds alone: the effectiveness constraint - **the coordinator's call count may not grow with the graph** - and `0043`'s discard, under which pieces of a set fetched separately do not survive to be joined. Effectiveness alone would permit a union of k fixed chains in k calls; the ruling does not. Whether dispatch calls count against the effectiveness constraint is not decided.

> **A form belongs in routing's domain if and only if some judgment the coordinator must make ranges over a set that cannot be produced in one return without it.**

The test is the instrument #86-#88 apply. A finding there that it admits what it should not, or excludes what it should not, revises it. **Its formalisation was #86's first task and is ruled at `0103`**: *without it* is read over the candidate forms minus the one under test, including inside `exists`; two chains produce *the same set* relative to the judgment that ranges over it; a form is counted where removing it changes what a chain can produce; and a superset carrying the discriminator does not produce the set. The test admits by what a form lets a chain produce, so two spellings that produce the same thing are one form to it, and it says nothing about which spellings a surface carries. **A repair read** - finding a dangling ref for `0018`'s owed validation pass, or the link a `detach` must name - is not a judgment the coordinator must make, and `0071` warns that a success-path derivation provably misses such methods; this test does not reach them.

**The criterion on a position**, which is #16's second membership test ruled here and which `0103` runs at every node position: **a field belongs on a routing result's position if and only if, without it, the coordinator cannot form its next intent or cannot decide whether to spend the next call.** #16's first test is the general form of which this is the instance for one judgment; it needs an observation to apply and stays at #16.

## What this makes ring 0

**Ring 0 is one routing result, held resident by policy.** An unprompted coordinator needs somewhere to stand when nothing has been fetched, and `0043` drops what is fetched, so a standing result is held by policy - which `0019` already calls residency. This threads `0100`'s *"`0043` bars a resident view from being a query"* rather than contradicting it: what `0043` bars is a view the coordinator **formed** by querying and then kept; the standing intent is fixed and system-held, the coordinator only triggers its re-execution (`0089`'s trigger for `refresh()`), and the result is resident by policy, not by having been fetched into the conversation. What the standing intent is and which fields its rows carry are ruled at `0103`, where `0100`'s admission and selection clauses are re-derived from this record and its banding dissolves; how the rows are arranged is #82's, and no clause's present content constrains routing. `0021`'s time projection is a routing result too; whether it is resident is not decided. A projection is a result, not a persisted thing; what routing ranges over is the persisted things.

## Considered and rejected

**Routing as a position the coordinator holds**, and **routing as the whole loop** (fetch, form an intent, resolve, fetch). Both make routing a property of something static - a render, a resident view - rather than an operation the system performs; the loop is the coordinator's use of routing, not routing.

**Routing as an enumerated set of read verbs.** Four drafts enumerated the domain from landed reads and extended it under review; each extension was a grammar decision. Rejected on `0100`'s diagnosis of `0038` - construction bottom-up - and on #84's placement of the grammar after the map.

**A reachability guarantee as part of routing.** Mechanistic reachability is the schema's, already satisfied by `0012`'s table for what `CONTEXT.md`'s opening sentence names, and deliberately not universal.

Source: ruled at #85 (Billy, 2026-09-06), in that issue's resolution comment, after eight drafts and six blind reviews whose pre-registration, reports and drafts are kept at `docs/evidence/2026-09-06-issue-85/`. Six rulings first recorded there: spontaneity, the effectiveness constraint and the one-return premise, the `0001` rewrite, the wildcard crossing's exposure through `look_at`, paths as the output, and one-call chaining (which amends `0060` and `0004`).
