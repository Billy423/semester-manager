# Spec records survey - an inventory of what they rule on

**What I read.** All five files in `/Users/billywu/Documents/Projects/fall26/records/spec/`, each in full, body and `## Changelog`: `design.md` (268 lines), `schema.md` (253), `write-rules.md` (180), `architecture.md` (136), `ring-0.md` (104).

**Boundary observed.** Nothing else. I did not open `records/domain/`, `records/plan/`, `records/archive/`, `findings/`, `evidence/`, the openclaw repo, or any code. Where a spec record cites one of those, I record the citation as the spec record states it and mark it unverified. I did not read the semester-manager repo other than to confirm `research/` exists as the output location.

**What this is not.** No adjudication. Where two passages disagree I give both sides and stop. Where a record asserts a status I quote the marker verbatim rather than assessing it. "Superseded" appears below only where a record says so about itself or about another record.

**Vocabulary note.** The records name things in backticks (`done_by`, `about`, `has-more`) and in prose ("the store", "the skeleton", "ring 0", "the walk"). I use their names. Where two names exist for one thing I say so in the thing's own entry.

**Status markers used in this corpus, verbatim.** Changelog lines end in one of `ruled` · `measured` · `agent-drafted` · `mixed, marked per section`. Bodies carry `[R]` (architecture.md §6 only), `OWED` / `owed`, `Not decided`, `Unruled`, `estimated`, `not measured`, `conditions:`, `weaker than this directory implies`. Attribution is `Billy`, `agent`, `Billy (direction) / agent (the table)`, or absent.

---

# A. Identity and record shape

## T1. `id` - the identity scheme

**Named as:** `id`; the convention section calls it "Identity" (`schema.md` §1.1). The retired scheme is named `<course_id>-slug(name)`.

**Revisions**

| claim | where | date | who | status |
|---|---|---|---|---|
| `id := <course_id>-slug(name)`, derived from the material, so a reference can be constructed before its target exists | retired scheme, described only in its obituary at `schema.md` §1.1 and `design.md` §3.2 property 3 | pre-2026-08-28 | unattributed in these files | retired |
| "An `id` is **opaque, monotone, and assigned by the system**. It says nothing about the record it names, and nothing derives one from the material." | `schema.md` §1.1 | 2026-08-28 | Billy | `ruled` |
| "`id := the next unused value in ONE id space, shared by every kind that can be an edge endpoint`" | `schema.md` §1.1 | 2026-08-28 | Billy | `ruled` |
| "**It is never reused, a delete included.** A monotone counter closes the route by which a freed id silently adopts links that still point at the old record." | `schema.md` §1.1 | 2026-08-28 | Billy | `ruled` |
| "**An id is obtained by reading it back; nothing constructs one.**" and "**Every read that returns records therefore returns their ids**, or the rule cannot be followed." | `schema.md` §1.1 | 2026-08-28 | Billy | `ruled` |
| "identity: the line from `name` to `id` is cut. An id is minted once at creation and never re-derived... A mint collision appends a disambiguator and never merges." | `schema.md` changelog | 2026-08-27 | Billy | `ruled` |
| "Uniqueness on `(obligation_id, course_id)` was considered and rejected: a ref has no room for a third element, and course-local ids are the colliding scheme the convention exists to avoid." | `schema.md` changelog | 2026-08-27 | Billy | `ruled` |
| "**An id is opaque, monotone and assigned**, so it says nothing about the record and changing a `name` cannot move it." | `design.md` §3.2 property 1 | 2026-08-28 | Billy | `ruled` |
| "id minting" is an application-tier responsibility | `architecture.md` §1, §7 | 2026-08-27 | Billy (§1) | `ruled` |
| "It does not address records by raw identifier and does not construct one." | `architecture.md` §3 | 2026-08-27 | Billy | `[R]`, `ruled` |

**Changelog reasoning.** `schema.md` 2026-08-28: the derived scheme is retired because "real material defeats that: one course names the same series `ChildMath A1` and `ChildsMath A4`, another spells one row `Week 2 Lab deliverables` and the next `Week 3 Lab diliverables`." The second reason is the load-bearing one for supersession: "It also contradicted `architecture.md` §3, which had already ruled that the agent never constructs an identifier - **a divergence between two ruled records that nobody had propagated**." `design.md` 2026-08-28 records the same change from the other side and adds the constraint it violated: constructing the target's id "contradicted `architecture.md` §3's ruling that the agent never constructs an identifier". `schema.md` §1.1 names the failure class: "Constructing an id is a bet on reproducing another writer's spelling - a cognition problem wearing a mechanism's clothes."

**Idempotency, explicitly held harmless.** "Idempotency is unaffected: it always rested on the caller supplying an id it had read, never on derivability, and a slug collision explicitly appended a disambiguator rather than merging" (`schema.md` changelog 2026-08-28; restated in body §1.1).

**Supersession.** Explicit and two-way: the derived scheme is superseded by the opaque serial, and the ruling that superseded it (`architecture.md` §3) predated the record it corrected by one day without being propagated.

## T2. `course.id` - the exception to opacity

**Named as:** `course.id`, "the **supplied course code**" (`schema.md` §2), value `2c03`.

**Revisions**

- "`course.id` stays the supplied course code, and the id space is deliberately not uniformly opaque" - `schema.md` changelog 2026-08-28 - Billy - `ruled`.
- "**Supplied rather than assigned** (§1.1): the source issues a canonical unique code, so there is nothing for the system to invent." - `schema.md` §2 - 2026-08-28 - Billy - `ruled`.
- "**An id is assigned only where the material supplies no identifier of its own** - which today is every kind but `course`." - `schema.md` §1.1.
- Scope limit stated in the body: "This is scoped to the kinds that exist. It settles nothing about `concept` or `artifact`, whose own material has not been read for this question." (`schema.md` §1.1, and the changelog repeats "it does not pre-decide `concept` or `artifact`").
- `write-rules.md` §2 carries `course.id` as a **pointer, not a rule**: "none. *That* it is supplied rather than assigned is `schema.md`'s §1.1... Noted here only so the slot is not read as empty."

**Changelog reasoning.** `schema.md` 2026-08-28: "The distinction is a property of the material rather than of the kind: a course code is a canonical unique identifier the source itself issues, while an obligation's name is whatever one document happened to print. Assignment is what a kind falls back to when the material supplies no such identifier." `write-rules.md` 2026-08-28: this was demoted out of the write-rules table because "Sitting in a `records/spec/` table was giving an agent recommendation `ruled` standing by placement" - agent - `measured`.

## T3. `kind` - the node discriminator

**Named as:** `kind`. Two definitions coexist and the records mark the relationship: `kind` as *a named record schema* (`design.md` §3.1) and `kind` as *a discriminator field on every record* (`schema.md` §1). They are the same thing seen as type and as wire field.

**Revisions**

- "`kind := name + ordered field set, each field: name · type · definition · required?`" - `design.md` §3.1.
- "**Every node record carries a discriminator field named `kind`**, whose value is that kind's own name; a serialized record cannot be constructed without it" - `design.md` §3.1, `schema.md` §1.
- "`kind` is **data on the node, never control flow** - trigger B" - `design.md` §3.1. Restated: "**It is not metadata.** An enum is only its wire form; what it actually does is **select which declared field set the node's payload has**. Metadata annotates an object and can be removed; remove this and the node has no shape."
- "Without it a reader must infer the kind from **which fields are present**, and dispatching on a record's shape is precisely the control flow `design.md` §3.1's trigger B forbids" - `schema.md` §1.
- Slice membership: "Slice 1 introduces `course` · `obligation` · `sticky_note` · `progress`; slice 2 adds `concept` · `artifact`" - `design.md` §3.1. `architecture.md` §7 corroborates "each of the four kinds".
- "A discriminated union over `kind` is §3.1's own mechanism as a language feature, and its exhaustiveness check is what makes that promise checkable" - `architecture.md` §6.

**Changelog reasoning.** `schema.md` 2026-08-27 - Billy - `ruled`: "every node record carries a discriminator named `kind`, and `sticky_note.kind` is renamed `category`. Without a discriminator a serialized line cannot be constructed and cold start cannot begin; the failing case is legal and minimal, a progress record with a null state, which carries no detail and so has no distinguishing field at all." `schema.md` 2026-08-28 amends the *argument* without amending the rule: "`kind`'s argument now rests on shape-sniffing being dispatch rather than on a degenerate record" - because the null-state case it had rested on was itself removed (see T14).

## T4. `layer` - a different axis, not in slice 1

- "`layer` is a *different axis* and is **not introduced in slice 1**: only the three skeleton kinds have one, `course` and `sticky_note` do not. Introducing it early is precisely how the two axes get conflated." - `design.md` §3.1.
- "no `layer` field" is named in the must-not-build list - `design.md` §4.
- Note a small internal ambiguity: `design.md` §3.1 names slice 1's four kinds as `course` · `obligation` · `sticky_note` · `progress`, then says "only the three skeleton kinds" have a layer and names two that do not. `progress` is unaccounted for in that sentence. No record resolves it.

## T5. The conventions block - `null`, free text, mutability, timestamps

**Named as:** `schema.md` §1 "Conventions". Four rulings that range over every kind.

| convention | claim | where | status |
|---|---|---|---|
| `null` | "means *no record*, never a default, and **must render as absence**. Rendered as a default, a null `grade_share_conditional` becomes an assertion that the stored share is a stated fact when no source said so - measured as the largest single class of unfaithful claim." | `schema.md` §1 | body rule, no separate changelog line |
| `null` exception | "**`progress` is the one deliberate exception and it is not one of these nulls:** its `state` is not nullable at all, so there is no null to render (§4.5)." | `schema.md` §1 | added by the 2026-08-28 `progress.state` ruling - Billy - `ruled` |
| free text | "at most one field per kind. `course` has **zero** - a cap, not a quota" | `schema.md` §1 | body rule |
| mutability | "**every field is individually CRUD-able.** Landing performs partial update, never whole-record replacement" | `schema.md` §1 | body rule; `architecture.md` §7 says "`schema.md` §1 has always implied it" and that "That clause had never been translated into a method set" |
| timestamps | "ISO 8601. `added_at` on `course` and `obligation`; the annotation kinds carry `created_at` and `updated_at` instead, because a note is modifiable and a record's birth is not its last claim" | `schema.md` §1 | corrected 2026-08-28 - agent - `measured` |

**Changelog reasoning.** `schema.md` 2026-08-28 - agent - `measured`: "§1's `added_at` on every node is corrected to `course` and `obligation`. Neither annotation kind's field table carried it, so the blanket sentence was false as stated and would have misled a slice-2 kind author."

**Container-sensitive.** "must render as absence" is a rendering rule sitting in the record that declares itself the application tier (`schema.md` conditions line: "A rule about what an agent should DO is presentation tier and does not belong here"). The rule is about a surface, and the surface is the CLI (`architecture.md` §5).

---

# B. `obligation` and its fields

## T6. `obligation` as ring 0's substrate

- "Ring 0 **is** this kind. It is not a separate store; residency is an access policy over these nodes." - `schema.md` §3.
- "**ring 0** | the obligation layer's typed fields | **not separately** - the obligation layer **is** ring 0. Ring 0 is the obligation-kind nodes' payload, and residency is an access policy over them" - `design.md` §3.0.
- "**Ring 0 is the obligation layer**, held **resident** by the coordinator. It is not a separate store: residency is an access policy over `obligation` nodes" - `ring-0.md` §1.

Three files, one claim, no drift. This is the most stable statement in the corpus.

## T7. `obligation.course` - a field, not an edge

- "The course this is owed to. **A field, not an edge**, and a property of `obligation` rather than of every node - a concept is not per-course" - `schema.md` §3.
- "`obligation.course` is a field, not an edge." - `design.md` §3.3.
- Changelog `schema.md` 2026-08-27 - Billy - `ruled`: "`obligation.course` stays a field and does not become a typed edge. Course membership is single-valued, mandatory and monomorphic, and nobody walks it; the capability *list this course's obligations* is an enumeration either way. The rule that relations are records exists to stop a **polymorphic** target becoming a field, and this target is not polymorphic."
- **Mutability is unruled.** `write-rules.md` §3: "*That* it is set at create and not updatable is an application-tier question, still open at `../plan/application-tier.md` §7.1 as a recommendation with no ruling. **The code implements the recommendation; this record does not decide it.**" Demoted to a pointer 2026-08-28 - agent - `measured`.

## T8. `obligation.due`

- "**The moment this obligation is anchored to.** For something handed in that is the deadline; for a sitting it is when it starts - a narrower definition is false for the 3 of 22 rows that are exam sittings, and the system is open by nature and should not over-constrain." - `schema.md` §3.
- Type: "`Date | DateTime`, nullable". "A `Date` resolves to **`23:59`** at read time; **which surface applies that resolution is presentation tier**, and the stored value is always returned raw. A `DateTime` is a stated time and is never overwritten by that default."
- "The midterm pattern - a date first, a time later - is a CRUD of `Date` into `DateTime`."
- Changelog `schema.md` 2026-08-27 - **"Billy 2026-08-24 via `archive/changelog-2026-08-24-slice-1.md:241`"** - `ruled`: "`due`'s date-only resolution is `23:59`, the ruled value, restored over the prose *'the end of that day'* which lost the number." This is the only changelog line in the corpus that attributes to a dated prior record outside `records/spec/`; I did not open it.
- Graveyard consequences: "**coarse dates** (*'April 2026'*, the Final Exam) | Not represented: a date that is not fixed is null. The term's largest obligation therefore stores a null `due`" and "`due_precision` as a separate flag | Not carried: the distinction lives in `due`'s own type" (`schema.md` §7).
- Ring 0 uses it as "the primary routing fact" and "the primary key, not `min(due, done_by)`" (`ring-0.md` §4, §5).

## T9. `done_by` (formerly `finished_by`)

**Two names, and the corpus says which is real.** `done_by` is current; `finished_by` is the name it replaced.

- "**The date chosen to have this finished by.** Null means no record; a planner wanting a work-back date computes `due − 7 days` as a **derived** value under its own name, and computes nothing when `due` is null. A stored value therefore always means it was chosen." - `schema.md` §3.
- "**The name is a mechanism, not a label:** rendered as a *start* date the field is misread and work is scheduled to begin at the target, which is the misread `finish 17 : start 1`." - `schema.md` §3.
- "The reason for 7 days: a draft finished a week early makes urgency arrive while slack remains, which is **the one place the system's anxiety-removal goal reaches the schema**." - `schema.md` §3, quoted again at `ring-0.md` §3.
- Changelog `schema.md` 2026-08-27 - Billy - `ruled`: "`finished_by` renamed `done_by`. The ruled name was always `done_by` and the rename is a measured mechanism, not a label: rendered as a start date the field was misread in every prior run, and renaming it fixed the misread `finish 17 : start 1` **across six runs**. `finished_by` never had a ruling behind it."
- Ring 0: band-A trigger and band-A-only projection field; "out of band A it has already failed the trigger" (`ring-0.md` §3, §4). "**triggering and ordering are different jobs** and one field can do the first without doing the second" (`ring-0.md` §5).
- `write-rules.md` §3: "`due` · `done_by` | none yet. §1.1 governs an inferred one".

## T10. `grade_share` - the standing exemption

- "**Approximate** share of the final course grade, in percent. **Reference only** - never an input to a computed ranking, because workload is judged from progress plus size rather than from the percentage. **This is a standing EXEMPTION from the rule every other field passes** - no mechanism reads it, and the exemption is the point rather than an oversight". Reader column: "none, by exemption". - `schema.md` §3.
- Changelog `schema.md` 2026-08-27 - agent - `measured`: "`grade_share` is recorded as a ruled EXEMPTION from *a field is typed iff a mechanism reads it*, rather than as a field with a human reader."
- Excluded from ring 0 on measurement (`ring-0.md` §6, see T29).
- Used in ring 0 as the ground for refusing an importance heuristic: "The system holds no notion of an obligation's importance - `grade_share` has no reader by standing exemption - so a rule that promoted 'important' undated rows would be asserting a judgment the system is ruled not to make" (`ring-0.md` §3).
- **The field's name is not settled.** "The `weight` / `grade_share` field's name... the field's own name is not settled. Owner: the user." - `design.md` §7 item 1. No other record mentions the open name; all four use `grade_share` throughout.

## T11. `grade_share_conditional`

- "bool, **nullable**. True when the stored number is **one reading of a rule the course states conditionally or as a bound**, not a stated fact. **Null means unknown**, never *not conditional*." Reader: "any reader of `grade_share`". - `schema.md` §3.
- "The rule **may optionally** be left on a one-line sticky note; requiring one is not a rule, because a schema rule that manufactures a conflict nobody would care about is a defect in the rule."
- "Covers both `10/10/30 or 0/0/50` and *'worth at least 30%'* - a bound is the same defect as a conditional."
- Changelog `schema.md` 2026-08-27 - Billy - `ruled`: "`grade_share_conditional` does not REQUIRE an attached note. The rule may optionally be left on a one-line note. A schema rule that manufactures a conflict nobody would care about is a defect in the rule." This is the schema-side instance of `architecture.md` §3's "The system must not chase the agent" (T36).
- Changelog `schema.md` 2026-08-27 - Billy - `ruled`: "`optional` and `grade_share_conditional` become nullable, and null means UNKNOWN. A non-nullable bool forced the system to assert what no source stated, which is the same defect as rendering a null `progress.state` as `not_started`." **Note the ground:** the analogy it rests on was itself reversed the next day (T14).
- `design.md` §7 item 1: "The conditional-weighting fix ships as `grade_share_conditional` (`schema.md` §3)".

## T12. `parts`

**The most-revised field in the corpus.**

| claim | where | date | who | status |
|---|---|---|---|---|
| "[string], possibly empty. **What this obligation contains**, in whatever terms the course uses... **No controlled vocabulary**... **It carries the CONCEPTS the obligation's source carries**, as raw strings, **never as pointers to concept nodes**." Reader: "concept carriage - exactly one reader" | `schema.md` §3 | 2026-08-27 | Billy | `ruled` |
| "`parts` carries the CONCEPTS the obligation's source carries. This settles the two-position question the field has had since 2026-08-24. The competing responsibility - *let size be judged ordinally* - is itself ruled and is **not** retired by this, so the field now has **two readers** and which one drives the wording is owed." | `schema.md` changelog | 2026-08-27 | Billy | `ruled` |
| "`parts` carries concepts only; the ordinal size-judgment reader is not designed. It is deferred until a size-judgment need actually arises... **This closes the two-readers question instead of leaving it owed.**" | `schema.md` changelog | 2026-08-27 | Billy | `ruled` |
| "Nothing writes this field yet: its write rule is owed (§6, §9)" | `schema.md` §3 | | | `owed` |
| "**`parts`.** Its reader exists; its writer does not. The portal screenshot cannot produce it - it is **extraction with judgment**... It is declared anyway because acceptance (a) is otherwise untestable: 12 of the 22 fixture obligations carry parts." | `schema.md` §6 | | | declared-not-produced |
| "A part is a **concept worth capturing because it might occur elsewhere in the system** - on another obligation, in another course. That test does the whole job." | `write-rules.md` §3.4 | 2026-08-28 | Billy | `ruled` |
| "**Write the canonical, singular name of the concept, not the phrase the source used.**" `Stacks and Queues` → `Stack` · `Queue`; `Properties of Big-O` → `Big-O`. "Effect on one real course: 50 candidate strings became 28." | `write-rules.md` §3.4 | 2026-08-28 | Billy | `ruled` |
| "**`parts` carries concepts, and it does not carry size.** **Two readers, and they pull the same way:** the coordinator learns which concepts an obligation contains without opening anything, and the whole corpus's `parts` is the surface a corpus-wide fuzzy find would run over." | `write-rules.md` §3.4 | 2026-08-28 | Billy | `ruled` |
| Excluded from ring 0: "it answers *what is this about*, not *where do I look next*, and under `write-rules.md` §3.4 it carries concepts rather than size so it does not answer *how much* either. **Excluded from the projection is not unreadable.**" | `ring-0.md` §4 | 2026-08-28 | Billy (direction) / agent (table) | `mixed, marked per section` |
| "**A part is a raw string, not a node**, and that half is decided." | `design.md` §4 | | | decided |
| Still listed as blocking: "**`parts` birth rules + prompt** (§6) - before anything writes the field. Its **target** is settled: it carries concepts. What is owed is what counts as one, what context the writer must hold, and what the wording is for." | `schema.md` §9 item 1 | | | `Blocking a writer` |

**Changelog reasoning.** `write-rules.md` 2026-08-28 - Billy - `ruled`: the archive's §14.4 "had recorded the responsibility as unpicked between *let size be judged ordinally* and *be the connection point to concepts*, and recommended the first; the second is now ruled and the recommendation is dead. **This vindicates the test §3.4 was already written to, which had picked the un-recommended candidate without anyone noticing the divergence.**" Then, the same day, a correction to that entry - agent - `measured`: "the entry below claiming `parts`'s responsibility was unpicked **is wrong about the history**, and the rule it landed is not. Billy had already closed it on 2026-08-27, twice, in `schema.md`'s own changelog... **The error: the archive's §14.4 was read as the current state of the question without opening the changelog of the record that owns the field.**"

That correction is the single clearest instance in the corpus of a superseded record still reading as authority.

## T13. `optional`

- "bool, **nullable**. True when nothing is lost by not doing it. **Null means unknown**, never *not optional* - a non-nullable bool forces the system to assert what no source stated, and here no source often does. Without it a plan ranks a +1% survey among required work purely by date." - `schema.md` §3.
- Changelog `schema.md` 2026-08-27 - Billy - `ruled`: made nullable (same line as T11).
- Changelog `schema.md` 2026-08-27 - agent - `agent-drafted`: "the `optional` tally is dropped. A count belongs in the body only where it is load-bearing, as `due`'s three exam sittings are. This one supported nothing, was contested between two readings, and **counted a fixture that was rejected as a golden set**. The rule survives without it."
- `write-rules.md` §3.5 - 2026-08-28 - Billy - `ruled`: "**`optional` defaults to false unless a source states otherwise.** The field stays nullable and null still means *unknown* - `schema.md` §3 is unchanged. **This is a rule about the writer, not about the field**... A stored null therefore means the writer genuinely could not tell, which is rarer than a source being silent."
- Changelog `write-rules.md` 2026-08-28: "Landed as a write rule and NOT as a schema change - the field stays nullable and null still means unknown. The 2026-08-27 ruling that made it nullable stands; what is added is an instruction to the writer, which is where a rule about producing a value belongs."
- `write-rules.md` §1.2 generalises it as **OWED**: "**Absent is not unknown when a person would not hesitate - OWED.** §3.5 is the first instance of a pattern that probably generalises... Whether that is one rule or one rule per field is not settled."
- Ring 0: band A only, "changes whether to act at all, and only matters once a row is in play" (`ring-0.md` §4).

## T13b. `added_at`

- "timestamp. When the record entered the system. **No mechanism reads it** - it is carried deliberately, against a future reader, and is a declared exemption from the rule above rather than an oversight" (`schema.md` §2, `course`); on `obligation` (§3) the same field carries the additional clause "A record-level timestamp cannot say when a **source** asserted any one field, because fields are updated independently; that meaning is carried on annotations, where a record is a single claim".
- Changelog `schema.md` 2026-08-27 - Billy - `ruled`: "`added_at` is kept on `course` and `obligation`, and is settled as the moment the record entered the system. **Kept deliberately rather than because a reader was found** - no mechanism reads it, and it is deleted when that is clearly permanent. **The competing reading is closed:** a record-level timestamp cannot mean *when the source asserted this*... Per-field assertion times are not carried and are not wanted."
- Scope corrected 2026-08-28 - agent - `measured` (see T5).

## T13c. `course.name`, `course.term`

- Changelog `schema.md` 2026-08-27 - agent - `measured`: "`course.name`, `term` and `added_at` are recorded as having **no affirmative birth reason**. They survive because the 2026-08-24 ruling deleted the other four fields and left them standing. **That is an answer, not a gap.**"
- "Four fields beyond the discriminator, and no free text. Their upstream reader is scope loading." - `schema.md` §2.
- `write-rules.md` §2: "`name` | none yet" · "`term` | none yet".

---

# C. Annotations - `sticky_note` and `progress`

## T14. `progress.state` - the reversal

**The one ruling in the corpus that reverses a prior ruling that was itself grounded in a measured incident.**

| claim | where | date | who | status |
|---|---|---|---|---|
| null must render as absence, never as `not_started` (the prohibition) | described only in its obituary | pre-2026-08-28, from "a measured incident in which a run invented that default" | unattributed | reversed |
| "enum `not_started \| in_progress \| done`, **not nullable**... **There is no unknown state.** An obligation with no progress record reads as `not_started`, because that is what a thing nobody has touched is" | `schema.md` §4.5 | 2026-08-28 | Billy | `ruled` |
| "a nullable state would make the system announce it does not know and give an agent a reason to ask, which `architecture.md` §3 rules a defect in the rule" | `schema.md` §4.5 | 2026-08-28 | Billy | `ruled` |
| "Nothing needs to be written at creation - absence carries the default. The stored vocabulary is fixed; the rendering is per kind of target - *Submitted* for an assignment, *Written* for an exam" | `schema.md` §4.5 | 2026-08-28 | Billy | `ruled` |
| "**It is never null and never absent from the projection:** an obligation with no progress record projects as `not_started`" | `ring-0.md` §4 | 2026-08-28 | Billy (direction) / agent (table) | `mixed` |

**Changelog reasoning.** `schema.md` 2026-08-28 - Billy - `ruled`: "The prohibition this reverses (*null must render as absence, never as `not_started`*) came from a measured incident in which a run invented that default; **a defined default is not an invention.** The ground for reversing it is `architecture.md` §3: a nullable state makes the system announce it does not know, which gives an agent a reason to ask *have you started this yet* - the system chasing the agent, which §3 rules a defect in the rule. **Four body sites that used this case as their canonical example are rewritten**; `kind`'s argument now rests on shape-sniffing being dispatch rather than on a degenerate record."

**Blast radius, stated by the record.** Four sites rewritten, plus `kind`'s justification (T3), plus the `null` convention's carve-out (T5). The 2026-08-27 nullability ruling for `optional` and `grade_share_conditional` (T11, T13) cited this case as its analogy and was **not** revisited when the analogy flipped.

## T15. `progress` as a kind, and its three rules

- "An **annotation**, like `sticky_note` - the same shape, distinguished by its `kind` value rather than by a type hierarchy. Its target is an `about` link, not a field, so a progress record can hang on an obligation now and on a concept once concepts exist." - `schema.md` §4.5.
- "**`progress` is its own kind, a sibling of `sticky_note`** - not a value of `sticky_note.category`." - `schema.md` §4.5; corroborated at §4 ("**`progress` is not one of these values**").
- The three rules: "**one current value per target** · **only the owner authors it** - system-inferred mastery is forbidden, so an agent may surface a progress claim for confirmation but never resolve one · **no `about` link is legal**, and means progress on a free topic named in `detail`, which is how a topic inside a chapter carries progress with no deliverable attached before concepts exist."
- Enforcement points table (`schema.md` §4.5): `detail` requires `state` → **construction**; one current value per target → **the service**; only the owner authors it → **nowhere, deliberately** ("It is a rule about the caller, and `architecture.md` §1 forbids a method from defending itself against one").
- Changelog `schema.md` 2026-08-28 - agent - `measured`: "§4.5's three rules are given their real enforcement points... **The record had asserted all three were validated at construction.**"
- `design.md` §3.7 carries the same three differences as a table (cardinality / who may write / enters the projection) and the staleness rule: "a claim only the owner can know, *'I've done part 1 of A6'*, may only be **surfaced for confirmation, never resolved**."

## T16. `progress.detail`

- "free text. How far along the work is and how much is left. **An elaboration of `state`, and illegal without one** - a `detail` with no `state` is just a sticky note, which is the overlap this rule exists to prevent. On the same record as `state` **on purpose**: two records would be free to drift apart, and one cannot." - `schema.md` §4.5.
- `design.md` §3.7 states the same closing argument: "which is also why `detail` lives on the progress record instead of on a separate note: two records would be free to drift apart, and one cannot."
- Excluded from the resident projection (`schema.md` §4.6, `design.md` §3.7, `ring-0.md` §7).

## T17. `origin` - one field across both annotation kinds

- "**The annotation provenance field, shared with `progress` (§4.5).** How this annotation came to exist - an announcement, someone saying so (`stated`), or the system having asked (`asked`). **Provenance does not confer immutability:** an annotation may be edited, and an edit carries `origin` forward by default." - `schema.md` §4.
- "**The same field as `sticky_note.origin` (§4), not a second one** - one concept, one name, across both annotation kinds... An asked answer persists stated prominently, so that an agent cannot read a historical answer as a current fact." - `schema.md` §4.5.
- `write-rules.md` §4: "`origin` | **OWED** - the schema's prose says *how the claim was obtained*; both passes reached for *what document class it came from*." A named divergence between the schema's definition and what two write passes actually produced.

## T18. `sticky_note.category` (formerly `sticky_note.kind`)

**Two names, one renamed into the other.**

- "string, **open set**. What sort of note this is - `correction`, `policy`, `erratum`, … **Deliberately not an enumeration**, because the cases cannot be enumerated. **The values in use are not yet a usable vocabulary:** across the 11 notes that exist, one value holds 8 of them and the boundaries between the others do not reproduce, so a write rule for this field is owed (§9)." - `schema.md` §4.
- Changelog `schema.md` 2026-08-27 - Billy - `ruled`: renamed from `kind` because "`kind` is kept for the node because the design of record already uses it that way; the note's own field is the newcomer and moves."
- `schema.md` §9 item 2, "**Blocking a writer**": "A write rule for `sticky_note.category` (§4) - before anything writes the field."
- `write-rules.md` §4: "`category` | **OWED** - **two independent passes produced two non-overlapping vocabularies.** No rule; the field stores what it is given."
- The two records give **different evidence for the same owed item**: `schema.md` cites a distribution over 11 notes; `write-rules.md` cites two non-overlapping vocabularies from two passes. Neither cites the other.

## T19. `sticky_note` shape, timestamps, and the length bound

- "Cheap to attach, modify and detach, because a note is **an entity that points at a node, not a property of one**. Maintenance happens at the read." - `schema.md` §4.
- "**Target is not a field.** It is an `about` link (§5), which is how a note attaching to a course holds without a polymorphic field." - `schema.md` §4.
- Timestamps: "Both, because a note is modifiable - and because the pair plus the maintenance-at-read rule is **what makes a time-bound statement safe to store at all**: an undated sentence from the start of term goes on influencing judgment forever. **The reader is the read-time maintenance pass**... **In slice 1 that comparison has no input**, because the revision date belongs to a kind that does not exist yet."
- Changelog `schema.md` 2026-08-27 - agent - `measured`: "`sticky_note`'s timestamps get their real reader. *'Both, because a note is modifiable'* was the whole stated reason; the actual reader is the read-time maintenance pass."
- **The length bound.** `schema.md` conditions line: "the sticky-note length bound (§4) **has no settled standing and no measured number**." Body §4: "**A length bound exists** and is a strict upper bound; its number is owed (§9). The primary lever is the prompt that writes the note, not a truncation. **The number is load-bearing: it gates whether the symmetry rule is affordable.**"
- Changelog `schema.md` 2026-08-25 - agent - `agent-drafted`: "the sticky-note length bound (§4) **demoted from `[R]` to owed**. No ledger anywhere supports the ruled standing, and every other record has it as *owed*; demoting to the level the evidence supports is the conservative move. Both the standing and the number are Billy's."
- `schema.md` §9 item 3: "**It covers two routes, not one** - `sticky_note.body` and the second unbounded route into the resident skeleton... eight one-line summaries can be pulled for a comparison set, eight paragraphs cannot."
- `write-rules.md` §4.2 gives the bound its shape without a number: "This is also the shape the owed length bound (`schema.md` §9 item 3) has to take: **the bound follows from what a rendered node can carry, not from a number chosen in advance.**"

## T19b. `annotation` - the tag, and why not inheritance

- "Both kinds are **about a node** rather than a relation to another node of interest; both render co-located with their target; both attach, modify and detach cheaply; both carry free text, provenance and timestamps; both target polymorphically. That shared shape has a name - **annotation**." - `design.md` §3.7.
- Three reasons against inheritance, decisive one first: "**Inheritance is a language feature; a `kind` tag is a data feature.** The target form is a CLI, possibly compiled, and the implementation language is not committed to Python - Rust and Go have no inheritance." Second: "**The architecture already has this mechanism.**" Third: the three differences "would express as a subtype tightening its parent's contract - a Liskov violation".
- "**The three differences therefore become construction-time validation rules on each kind, not a type hierarchy**" - `design.md` §3.7. **Contradicted by `schema.md` §4.5's enforcement-point table** (T15, and D6 below): only one of the three can run at construction.
- Changelog `design.md` 2026-08-25 - agent - `measured`: "§3.7's rendering-surface argument no longer quotes the dead *label/due/status/workload* grain. Only the clause it actually rests on (*no free text*) survives; **the field list was decoration and is now wrong.** Found by the migration's citation sample, not by the edit that marked §9.1 dead."

---

# D. The graph - refs, links, operations

## T20. The five refactor triggers

**Named as:** "the five refactor triggers" (`design.md` §2), labelled **A** Identity, **B** Dispatch on type, **C** Linkage, **D** The store boundary, **E** Persistence coupling.

The commitments, verbatim: "**One id space for anything that can be an endpoint**" · "**`kind` is data with a typed payload, never control flow** (OCP)" · "**Relations are records, not fields on the related thing**" · "**The purity cut is a property of the interface's shape, not of restraint**" · "**A repository interface with one implementation** (DIP)".

Explicitly held stable through the tier re-scoping: "**The five refactor triggers and §3's abstractions are unaffected.**" - `design.md` changelog 2026-08-27 - Billy - `ruled`.

## T21. `Ref`

- "`Ref := (kind, id)` - e.g. `('obligation', '137')`, `('course', '2c03')` - where `id` is unique in **one** id space across every kind that can be an endpoint, and is opaque." - `design.md` §3.2.
- Three properties: opaque/monotone/assigned (T1) · "**The kind tag makes a ref resolvable without a lookup**, which is what lets a link be *validated at write time* against its signature" · "**A ref may name something that is not there**, so a ref is not a foreign key and deleting a record does not have to cascade."
- Property 3's mechanism was removed: "**What this is no longer for:** it used to carry forward reference - A8's handout names A9 before A9 exists - by letting a writer *construct* A9's id from its name. That route is closed (§3.2 property 1), and the observation it rested on is handled without it: **list before linking, surface an untracked target to the user rather than auto-adding it, or resolve a batch ingest in two passes.**"
- "**A course IS a node**, so `get(Ref('course','2c03'))` resolves and an `about` link to a course is an ordinary link with no special case. **This is forcing in slice 1, not slice 2:** course-level notes - the late-day budget, the snow-day credit, the conditional-weighting rule - must land and read back for F5 to pass."
- "**Cost, stated:** a ref is not a foreign key, so nothing enforces that its target exists. Recovered by a validation pass over the link set - cheap at ~2,200 links, and it is a real operation the design owes, not a hand-wave."
- `schema.md` §1: "A pointer that may name something not present. The kind tag is what permits a ref to a `course` **whether or not courses ever join the node set**" - a hedge the `design.md` §3.2 blockquote does not carry, since `design.md` states flatly that a course is a node.
- Changelog `design.md` 2026-08-28 - Billy - `ruled`: "A ref may still dangle; that is now a **consequence of deletion** rather than a mechanism for forward reference."

## T22. `Link` identity and `locator`

- "`Link := from: Ref · to: Ref · kind: LinkKind · role?: string · locator?: string`" · "`identity := (from, to, kind, role, locator)` -- a natural key; no surrogate id" - `design.md` §3.3; restated at `schema.md` §5.
- "**`locator` is in the identity, and leaving it out silently destroys edges.** Computed over the source graphs: without it **7 real edges collapse** - `s1 → textbook` is cited **four** times from one deck with four different locators (*'Section 4.1'*, *'section 2.1'*, *'Text Section 1.2'*, *'Text Section 2.5'*), `s6 → week-6-code` three times with three different method names, `s3 → textbook` twice, and `singleton → part-of → stupid-concept` twice in 2aa4. Nodes are typed and edges are bare pairs, so **the highest-frequency relation in the corpus cannot be stored without it.**"
- "**The residual is correct rather than a gap:** two citations from the same source into the same target at the *same* locator are one edge."
- "A surrogate id was considered and rejected - idempotent re-landing needs a natural key regardless, so a surrogate would add a second identity without removing the first."
- "`role` and `locator` are optional and **unused in slice 1**; `locator` is listed because **28** instances were measured in 2c03 carrying the source string verbatim (22 `cites` + 6 `example-code`)... and it is an edge payload rather than an edge type."
- `schema.md` §5 repeats the 7-edge collapse as the whole justification.

## T23. `LinkKind` - the set and the signatures

`design.md` §3.3's table, with the measured counts it carries:

| LinkKind | signature | slice | measured (as stated) |
|---|---|---|---|
| `about` | `annotation → any` (`annotation` = `sticky_note` or `progress`) | **1** | "18 instances measured, targets across all three layers, **zero at course level in the material** - the course case comes from the late-day budget living on a note" |
| `covers` | `artifact → concept` | 2 | ~150 (2c03) · 118 (2aa4) |
| `applies` | `artifact → concept` | 2 | "split out of `covers`; the split is what dissolved the phantom hub" |
| `requires` | `concept → concept` | 2 | ≥7 |
| `requires` | `obligation → concept` | 2 | 46 enumerated (2c03) |
| `spec` | `obligation → artifact`, `role ∈ {given, owed}` | 2 | ~45 (2c03) · 8 (2aa4) |
| `prepares-for` | `artifact → obligation` | 2 | "13, **both agents in 2c03**; 2aa4 has zero. One course, not two" |
| `builds-on` | `obligation → obligation` | 2 | 3 explicit |
| `part-of` | `concept → concept` (**a DAG**) | 2 | ~35 · ~30 |

- "**Slice 1 implements exactly one row of this table.** The rest is here to show that adding them is a table entry plus a signature - trigger C defused - not a schema change." - `design.md` §3.3.
- `schema.md` §5: "Slice 1 has exactly one kind" - `about`, "`annotation → any Ref`", payload "none used in slice 1".
- `write-rules.md` §6: "`about` | none yet."
- `design.md` §1 forecasts slice 2 as "an edge set of ~8 surviving types".

## T24. The skeleton operations - and where they went

**Two names for one thing:** `design.md` §3.4 calls them "Skeleton operations"; `architecture.md` §7 calls them "the slice-1 verbs".

`design.md` §3.4's set, as written:

| operation | serves |
|---|---|
| `get(ref) -> Node?` | resolve a ref, including one whose target does not exist |
| `nodes(kind, course?) -> [Node]` | enumerate a kind; the projection, the read-back, and `nodes_without`'s first half |
| `links(ref, link_kind?, direction?) -> [(Link, Node)]` - one hop | **the walk** |
| `closure(ref, link_kind, direction) -> {Ref}` | the `requires` closure |
| `nodes_without(node_kind, link_kind, direction) -> [Node]` | set difference |

`architecture.md` §7's re-homing:

| slice-1 operation | tier | what it actually is |
|---|---|---|
| `get(ref)` | **persistence** | fetch by key |
| `links(...)` | **persistence** | a scan of the adjacency index |
| `nodes(kind, course?)` | **not one operation** | "two service reads wearing one coat: `courses.list()` and `obligations.list(course)`" |
| `closure`, `nodes_without` | application, **slice 2** | business queries over persistence traversal |
| `look_at(node, question)` | **presentation** | a composed view |
| `land(candidates) -> Diff` | application, but **not a primitive** | "a batch composition over entity CRUD; `Diff`'s conflict question is a presentation adjudication" |

- "**What the application tier is made of is CRUD at field grain.**" - `architecture.md` §7. "That clause had never been translated into a method set, and **its absence is why an operation list belonging to the graph was mistaken for the tier's contents.**"
- "**`land()` is not wrong and is not the bottom.** Its signature is determined by the caller above it... and that caller does not exist. It is therefore not in the first build." - `architecture.md` §7.
- `design.md` §3.4 was marked in place rather than deleted: "**Re-homed by `architecture.md` §7.** ... What follows is still correct about the *graph*, and is no longer a tier's contents."
- Changelog `design.md` 2026-08-27 - **Billy (direction) / agent (the re-homing)** - `ruled`. Changelog `architecture.md` 2026-08-27 - **Billy (direction) / agent (table)** - `ruled`, adding: "The error being corrected: an operation list written before the split existed was taken as the tier's contents."
- Slice-1 subset: "**Slice 1 needs `get`, `nodes` and `links`**... `closure` and `nodes_without` are slice 2." - `design.md` §3.4.

## T25. `closure` is single-source, not all-pairs

- "**`closure` is single-source reachability, not an all-pairs matrix.** Recorded because the misreading is natural and the cost difference is three orders of magnitude." - `design.md` §3.4.
- The comparison: Floyd-Warshall O(V³) ≈ 2.6 × 10⁸ recomputed on every write, assuming a dense graph, versus "**single-source**, from one ref", O(V+E) ≈ 2,900 steps, per query, stateless, over a sparse graph - "~2,240 links over ~640 nodes, mean degree ≈ 3.4 (a dense graph here would carry ~200,000)".
- "**No query on this graph needs all-pairs.** Even the set-difference query, if it is taken transitively along `requires`, is a **multi-source** BFS from every obligation at once - equivalent to one virtual super-source, still O(V+E)."
- "**All three are index scans over an adjacency map built from the link set**, microseconds in any language."
- Naming rulings attached: "**`links` is named for what it walks:** the operation walks **edges**, not nodes, and its return type is edge-and-far-endpoint." · "**`nodes_without` takes a node kind:** the query scans one layer... and it means **no link of that kind in that direction** - never 'a node lacking a kind'."
- Note an internal number: §3.4 opens with "Two queries earn their keep at **N≈300**" while §5 and the cost table use ~640 nodes / V=640. No record reconciles the two figures.

---

# E. Ring 0 - the resident projection

## T26. What ring 0 is, and its inherited constraints

- "Its job is **routing, not deciding**. From ring 0 alone the coordinator must be able to tell **where to look next** - which node is worth one `look_at`, and which is merely known to exist. Depth lives in the skeleton and is fetched on demand; ring 0 is the map that makes the fetch targeted." - `ring-0.md` §1.
- Three inherited constraints, all cited to `domain-design.md` (outside my boundary, unverified): fixed-shape and uniform-depth, "never deepens... What is fetched is dropped, never sedimented" (§9.1) · "**isomorphic across courses.** Asymmetry that comes from the material is legitimate; asymmetry that comes from interaction history is not" (§9.2) · "losing the coordinator costs **one projection read** to rebuild. That is ring 0's size bound: roughly 55 obligations at five courses" (§9.5).
- `ring-0.md` conditions: "This record fills a vacuum: `../domain/domain-design.md` §9.1 states that its own field grain is dead and that **no replacement is ruled**. **It supersedes nothing; it answers what §9.1 left open.**"
- Changelog `ring-0.md` 2026-08-28 - **Billy (direction) / agent (the test and the table)** - `mixed, marked per section`: "created, filling the vacuum `domain-design.md` §9.1 left when its field grain died with no replacement."

## T27. The membership test

- "> **A field belongs in ring 0 if and only if, without it, the coordinator cannot decide where to look next.**" - `ring-0.md` §2. Attributed in the changelog as "**agent-drafted**".
- It explicitly declines the domain record's test: "it is deliberately **not** the test `domain-design.md` §9.2 offers (*an observation earns its place iff a judgment demonstrably changes when it is present*). **That one has been run and returned nothing:** `findings/read-cycle.md` §4 reports `parts`, `grade_share`, the skeleton, a complete ring 0 and `progress` as **each read, each rendered, none changing the plan's shape**."
- The null result is refused in both directions: "**That null result does not license removing the fields, and it does not confirm the routing test either.** The instrument could not have detected the effect: every run was a memoryless `claude -p` cold start, and the design's coordinator is long-running... all ~40 runs used one fixed prompt, *help me plan for the rest of this semester*... and the two courses are the same shape. **A device that cannot exercise routing returns 'nothing changed' whether or not routing matters.**"

## T28. The two bands and the active window

```
band A  "active"   any one of:
                     due      in  today-7d .. today+14d
                     done_by  in  the same window
                     state    == in_progress

band B  "known"    everything else, including obligations with no date
```

- Changelog `ring-0.md` 2026-08-28 - **Billy (the window) / agent (`done_by`)** - `ruled`: "the active window is `today-7d .. today+14d`, and `done_by` triggers it alongside `due`. **The window's own standing is new:** `domain-design.md` §9.1 had recorded the +/-1-2 week observation as *a requirement Billy may state, not a failure to fix*, and **it was never ruled until now.**"
- Changelog `ring-0.md` 2026-08-28 - Billy - `ruled`: "`state == in_progress` promoted to a band-A trigger in its own right: working ahead of the dated window is being active, so the partition is not a time window with exceptions but three independent triggers on one question."
- "**Two bands do not violate uniform depth.** The partition is computed from material facts plus one rule applied identically to every course, so it carries no interaction history."
- "**An undated obligation is in band B, and that is not a hazard.**" (grounds at T10).

## T29. The ring 0 field set, and `has-more`

| field | band A | band B |
|---|---|---|
| `course` | ✅ | ✅ |
| `name` | ✅ | ✅ |
| `due` | ✅ | ✅ |
| `state` | ✅ | ✅ |
| `optional` | ✅ | ❌ |
| `done_by` | ✅ | ❌ |
| **has-more** | ✅ | ❌ |
| `parts` | ❌ | ❌ |
| `grade_share` · `grade_share_conditional` | ❌ | ❌ |

- "**`has-more` is new and nothing writes it yet.** Its motivation is measured on the real corpus: **6 of 14 obligations carry an annotation and 8 carry none**, so a `look_at` costs the same call and returns nothing new on more than half the rows. Whether it is a boolean, a count, or a set of present link kinds is not decided here." - `ring-0.md` §4. The table's own why-column calls it "**the only one here that no record has yet declared**".
- `name`: "the label a person recognises the row by. **It is not the handle and nothing is derived from it**" - the post-T1 restatement.
- **`grade_share`'s exclusion, on measurement** (`ring-0.md` §6): "conditional weighting printed as a fixed number is **24 claims across 17 runs**, and with a stated bound restated as a point value it is **29 of 77 unsupported-or-contradicted claims - 38% of every measured faithfulness failure**. It is the only defect kind appearing in **every** configuration group, which is what makes it a property of the schema rather than of a configuration."
- **The standing of that number is qualified in the record itself:** "it is a count, not a reading of one run's prose, and it comes from the faithfulness grader rather than from either of the two harness detectors known to have been wrong. **It has not been re-derived structurally**, which `CAVEATS.md` §7 asks for before any metric in that folder is trusted."
- A second, measurement-free ground: "across 2c03's real rows the column sums to 95 while the 5% it is missing (tutorial attendance) **has no row at all**, and two rows carrying 1% are bonuses added outside the 100. A rendered column of shares therefore reads as a partition that it is not."
- Changelog `ring-0.md` 2026-08-28 - agent - `measured`: "§4's annotation counts are wrong... the counts were **6 of 14 carrying an annotation, 8 without** - not 5 and 9, and not *two rows in three*. Both found by the next sitting reading the corpus rather than this record."

## T30. Grouping and order

- "**Grouped by `course` by default, and the grouping key is a parameter.** It is not a constant because `domain-design.md` §9.2 scopes the symmetry rule to *the set the judgment ranges over*... asked *what is due across every course this week*, the set is a different one and the grouping has to follow it. **That second read is the one `evidence/2026-08-27-tier-recut/derivations/L3-surface.md` records as missing entirely.**" - `ring-0.md` §5.
- "**Within a group, order by `due` ascending, nulls last; among nulls by `done_by`; ties broken by the handle.**"
- "**`due` is the primary key, not `min(due, done_by)`.**" · "**Nulls last gives an undated obligation a defined position**, which a bare date order does not have and which is the recorded objection to date ordering."
- "**The tiebreak is the handle, never file order.** Array order is insertion order is write history, and §9.2 rules out asymmetry that comes from interaction history rather than from the material. **The order measured in `findings/read-cycle.md` was array order, so the projection has been violating that rule rather than lacking a rule.**"
- Changelog `ring-0.md` 2026-08-28 - Billy - `ruled`.

## T30b. What ring 0 does not carry

- "**`time_point` and 'the current plan'**, both named by `domain-design.md` §9.1 as part of the projection. `time_point` is not in slice 1 (`schema.md` §7); **the plan has no representation anywhere**, and this record does not invent one." - `ring-0.md` §7.
- "**Free text of any kind.** A note's body is reached by `look_at` **on the node it hangs on**, and that node is not always the course: of the 11 notes in the corpus, **4 hang on the course** and **7 hang on individual obligations**."
- Changelog `ring-0.md` 2026-08-28 - agent - `measured`: the prior clause "handed all 11 notes to the course level, when only the 4 hanging on the course node belong there."
- **An explicit non-ruling:** "**What this record does NOT establish, and must not be read as establishing: that the course level is worth a call.** *Ring 0's complement* says what would be in it, which is a **negative definition** and not a justification. Measured on the corpus, both readings are uncomfortable: all 11 notes in one call is **1,881 characters**, while the 4 course-scoped ones alone are **871**... **The missing term is that ring 0 is resident for the coordinator and for nobody else** - a person at the surface holds nothing, so the same call is redundant to one reader and the only view of a course to the other... **Unruled**, and it is the presentation cycle's question rather than this record's."

## T30c. The no-free-text-in-the-projection rule

Stated three times, identically, and it is one of the few claims that survives every revision:

|  | resident projection | `look_at` |
|---|---|---|
| `progress.state` | ✅ "the 'at a glance'" | ✅ |
| `progress.detail` | ❌ | ✅ |
| `sticky_note.body` | ❌ | ✅ |

`design.md` §3.7 · `schema.md` §4.6 · `ring-0.md` §7. `design.md` adds the framing: "the high-level/detail split is not two mechanisms - it is **one record seen through two surfaces**."

---

# F. Persistence, serialization, and the store

## T31. The skeleton does not need a database

- "**The skeleton does not need a database.** It needs a durable serialization plus an adjacency index rebuilt at load. All three operations are scans over that index, and **the load is cheap enough that per-invocation and resident are indistinguishable**." - `design.md` §5 conclusion 1.
- The facts it rests on: "~640-1,600 nodes · ~2,200-3,700 links at five courses. Base: 256 nodes / 224 links enumerated over two. Enumeration is **15-25% of observed links**... **The conclusions survive a 2-3× error, which is why the range is quoted**" · "cold-load cost | **measured**: 2c03's 138-node / 137-link graph is 52 KB and parses in **0.27 ms**" · writers: one · degradability: "each side must work while the other is broken".
- A guard against a misreading, stated in the body: "**The coordinator's lifetime is not a deciding fact here, and must not be reintroduced as one:** the one-persistent-session decision is about the **conversation's** lifetime... and says nothing about a process holding the graph in memory. The skeleton and its verbs are **invoked on demand**; every call may be a new process."
- A prior heuristic explicitly refused: a general "*few writers means no database*" heuristic "does not decide this either: its stated justification is that a database's concurrency machinery buys nothing, which is a **concurrency** argument... Two of its *supporting* reasons do transfer... so a conclusion may coincide while the heuristic still does not apply." (`design.md` §5 preamble.)
- "**A market fact that bears on 1.** The obvious embedded-graph-database answer is gone: Kùzu is archived and its team acqui-hired, and the survivors are forks (LadybugDB, RyuGraph, bighorn) roughly one year old... **which is a reason to be glad conclusion 1 holds, not the reason it holds.**"
- "**What would overturn this:** the corpus growing an order of magnitude · multi-device sync becoming real (a MacBook plus the deferred Mac Mini) · the skeleton growing far past ~640 nodes."
- "**Not decided, on purpose:** the actual serialization format and the store's engine."

## T32. Serialization - JSONL, `schema_version`, and where validation happens

- "Each file carries a **`schema_version`**: JSONL enforces nothing and construction is the only gate, so without a version a stale file fails as a validation error with no explanation. `nodes.jsonl` + `links.jsonl`; vectors, if they ever arrive, go to a **side binary store keyed by node id**, never into the JSONL." - `schema.md` §8.
- Two-phase cold start: "`nodes.jsonl → parse → construct by kind` -- validation happens HERE" / "`links.jsonl → parse → build adjacency index` -- the graph operations run on THIS".
- "**Construction is the only place a record's own shape is checked**, because JSONL enforces nothing."
- "**Two things it is not.** A rule that ranges over more than one record cannot run there - a constructor sees one line - so the id space, one-current-value-per-target and link identity belong to the services. And **construction is not currently part of the load**: the cold start parses and indexes, and each record is constructed lazily by whichever read touches it. **A malformed line therefore loads without complaint and is rewritten intact by the next flush.** Closing that needs a load-time pass owned by the application tier... it is parked at `../plan/backlog.md`."
- Changelog `schema.md` 2026-08-28 - agent - `measured`: "§8 no longer claims that validation happens at load... **Measured, not inferred: a store carrying `due: 'April 2026'` and a slice-2 `concept` node loaded without error and was rewritten intact.**"
- Note the residual: the code block in §8 still carries the inline comment "`-- validation happens HERE`" on the construct-by-kind line, which is consistent with the correction (construction is the gate) but sits directly above prose saying construction is not part of the load.

## T33. The store - two modes and one coupling field

- "**Not built until slice 3**; described here because slice 1 must not foreclose it. `Chunk := id · node_id · ordinal · text · locator? · embedding`, where `node_id` is the **entire** coupling surface to the skeleton and everything else is store-internal, which is what lets one fail while the other works." - `design.md` §3.5.
- Two modes: "**by-handle** | a node ref | a lookup on `chunk.node_id`. Deterministic, no similarity" · "**by-query** | text | nearest-neighbour over embeddings, for when you do not know where to go".
- "**The coordinator holds neither.** It sits above both store modes - it sees what a node **is**, never what it **says**. Structurally: the coordinator holds the skeleton interface and does not hold the store interface, and the skeleton's return type has no field a chunk could arrive in. **Trigger D defused by type, not by restraint.**"
- "**Not decided, and load-bearing for slice 3:** one position attaches embeddings to the **concept layer** as the entry point, with chunks in the artifact layer - `query → nearest concept → walk covers → read artifact by-handle`. That implies **two** embedding sets, not one." Owner named at `design.md` §7 item 4: "the build, slice 3".
- "**The store does want real storage**... 62 MB of vectors should not be re-parsed per invocation, and chunk text wants random access. But brute-force cosine over 10⁴ vectors is milliseconds, so what it needs is **storage, not an ANN index** - that is a slice-3 decision with a measurable trigger." (`design.md` §5 conclusion 2.)
- "**Separate engines are permitted and probably preferable**, because degradability wants them independent and the coupling is one field." (conclusion 3.)
- "**And the asymmetry between 1 and 2 is a hard boundary, not an optimisation.**... Under a resident-process assumption that difference reads as tuning; under the real one it is the reason the two sides get different mechanisms."
- Store sizing is flagged as unmeasured: "~10,200 chunks (**estimated** at 3 chunks/page over 3,400 page-images - **not measured**), ~62 MB of float32 embeddings, ~15 MB of text."

## T34. "Exactly TWO persisted things", and the name `Store`

- "**Nothing here is called `Store`.** That name is already taken: *the store* means materialized artifact content. The naming rule that governs fields governs interfaces too." - `design.md` §3.0.
- **the skeleton** = the graph: nodes and links, "**yes - thing one**" · **the store** = materialized artifact content: chunks and embeddings, "**yes - thing two**, and it does not exist until slice 3" · **ring 0** = "**not separately**".
- "The two are coupled by exactly one field, `chunk.node_id`, so that each degrades without the other, and **slice 1 touches the skeleton only**."

---

# G. Architecture - tiers, language, packaging, surface

## T35. The three-tier split

- `architecture.md` conditions: "**none. This record governs every other record in `records/spec/`**, and it re-scopes `design.md`, whose bounded question was written before the split existed." Standing line: "The split itself and the four consequences in §3 are `[R]` Billy."

| tier | what lives here | who calls it |
|---|---|---|
| **presentation** | "the CLI, which is the surface (§5) · a thin adapter over the same grammar, if one is ever built · the bundled skill · **rendering, including every one-line summary** · every rule about **what an agent should do**" | the user, and the agent |
| **application** | "the field set · the kinds and links · construction-time validation · **CRUD services at field grain, per kind** (§7) · id minting" | the presentation tier |
| **persistence** | "the serialized files and the adjacency index · fetch-by-key and one-hop traversal. Pure persistence methods" | the application tier |

- "**The application tier has no surface.** Its methods sit there as callable service methods, and **when they are called we expect them to be called correctly.** A method does not defend itself against a caller that should not have called it." (Cited by `schema.md` §4.5 as the reason "only the owner authors it" is enforced nowhere.)
- "**A tier is designed against the tier below it, and that tier must already exist.** Designing the presentation surface before the application tier is built is how this project spent three cycles specifying descriptions for methods that do not exist."
- Per-record assignment (§2): `schema.md` → application · `design.md` → application and persistence, "its passages on docstrings and the MCP adapter are presentation" · `../domain/` → "none - it is the material both tiers are derived from, and it predates the split" · the CLI, tool descriptions, the skill → presentation, "none of these exists yet".
- Changelog `architecture.md` 2026-08-27 - **Billy (§1, §3) / agent (§2, §4)** - `mixed, marked per section`.

## T36. The four §3 consequences

All four carry `[R]` in the body. All four are Billy, 2026-08-27, and none has been amended since.

1. "**A write rule never refers to the source.** `[R]` The field set says what a legal value is; **how to produce one lives in the tool description or the bundled skill**, split by operation... A schema rule of the form *the value must be what the source stated* is unenforceable by construction and does not belong here." **See D1 - this phrasing is contradicted by `write-rules.md`'s own rules and by its own changelog.**
2. "**The agent never auto-adds anything unless it is clear the user wants it.** `[R]` What gets a row is what the user wants tracked, and the user triggers it. This is a presentation-tier behavioural rule; the application tier holds no rule about what deserves to exist."
3. "**The system must not chase the agent.** `[R]` *'The system is designed to help me, not to raise questions, conflicts or concerns that no one will ever care about in daily usage. The schema-level rules shouldn't be a burden that keeps chasing the agent.'* A schema rule that manufactures a conflict a person would not care about is a defect in the rule." Cited as grounds by `schema.md` §4.5 (T14) and §3 (T11).
4. "**The agent works by listing, then acting on what it saw.** `[R]` It does not address records by raw identifier and does not construct one... Two things follow: **identifiers need not be human-facing**, and **matching two records is an interaction at the presentation tier, not an algorithm in the application tier.**" Cited as grounds by `schema.md` §1.1 (T1) and by both records' "no near-match matching in this tier" clauses.

## T37. The migration list - what the split moved

`architecture.md` §4, opening line: "**Recorded because a plan that predates the split still reads as authority.**"

- "**`land()`'s docstring and the read operations' descriptions** are presentation. The 2026-08-26 ruling that write rules precede the build **still holds and its target changed**: they precede the *presentation* tier, not the application tier."
- "**The MCP adapter** is presentation, and needs its own design against a built application tier. §5 further demotes it: it is at most an adapter over the CLI's grammar, **and may never be built.**"
- "**The verb-routing evaluation**... tests descriptions, so it is presentation and cannot be run against an application tier that has no descriptions."
- "**The screenshot-extraction evaluation** tests an agent producing candidate facts, which is presentation."

## T38. The acceptance criterion - 22 across two courses, then one course

| claim | where | date | who | status |
|---|---|---|---|---|
| "Ring 0 holds all **22** real obligations with **no free-text escape hatch**" (F5) | `design.md` §1 | imported 2026-08-25, body rewritten 2026-08-27 | unattributed | still in the body |
| "the field set holds **one course's real obligations**, landed and read back through the operations rather than hand-written. **'Landed' means written through the write operations**, not through `land()` specifically" | `architecture.md` §4 | 2026-08-28 | Billy | `ruled` |
| "The 22 came from a transcription that has since been superseded: a fresh extraction from source found **14** for 2c03, and the old count included **a row the graveyard forbids** (recurring tutorial attendance), so **22 is not reachable by re-running the old route.**" | `architecture.md` §4 | 2026-08-28 | Billy | `ruled` |
| "**extracting the other three courses is not worth doing before the presentation tier exists.** Every contested field - `parts`, a note's `category`, `origin`, whether a note is worth keeping at all - needs a write rule, and a write rule is derived from what a value must be for a node to render well. Reading three more courses without those rules produces three more courses of noise and does not produce the rules." | `architecture.md` §4 | 2026-08-28 | Billy | `ruled` |

**`schema.md` still counts in 22s** throughout §3 ("3 of 22 rows that are exam sittings"), §6 ("12 of the 22 fixture obligations carry parts"), §7 ("one instance in 22", "across the 22 fixture rows", "one week-relative obligation in 22"). See D2.

## T39. The language - TypeScript

- "**TypeScript**, and **the tiers are directories under one source root**." - `architecture.md` §6.
- The argument: "The language is settled by what this design already claims about itself. `design.md` §3.5 says trigger D is *'defused by type, not by restraint'*, and `schema.md` §8 says construction is the only enforcement point there is. **Both are claims about a compiler that can refuse.** Python cannot refuse: any module may import any other, so the purity cut degrades into discipline; and adding a kind in slice 2 raises no error at the sites that must change, so trigger B's promise is hoped for rather than checked."
- Costs stated: types erased at runtime, needing a runtime parser - "**this item is a wash and is not a reason to prefer either**" · "**The embedding ecosystem is Python's**... the store may be Python without crossing a tier boundary. `fall26/ingest.py` stays Python as an offline pass and **is in no tier**" · "**Rust fits the data shapes best**... and Go satisfies the enforcement requirement. Neither is chosen, on iteration speed for a solo build."
- Changelog `architecture.md` 2026-08-27 - Billy - `ruled`: "Billy raised the language question; **the agent had recommended Python and reversed**, because the two mechanisms this design claims for itself... both presuppose a compiler that can refuse."
- **`design.md` §1's constraint line still reads "directly-callable Python, no MCP, no Postgres, no `PA_SOURCE`"** and was not edited. See D3.

## T40. Packaging - packages, then directories

**The corpus's fastest reversal: ruled and reversed within 24 hours.**

- 2026-08-27 - Billy - `ruled`: "TypeScript, and **the tiers are separate packages in one workspace**... Packaging ruled by Billy: a package boundary is enforcement, a lint rule is a convention."
- 2026-08-28 - Billy - `ruled`: "**§6 reversed: the tiers are directories under one source root, not separate packages.** The original ruling's ground was that a manifest cannot be waived; **under npm that is false, because workspace dependencies hoist and a manifest cannot refuse an import it does not declare.** The enforcement is `app/tests/boundary.test.ts`, which resolves every relative import and **has been shown to fail**. Its limits are stated in §6 rather than left to be discovered."
- Body §6: "**That test has been shown to fail**, which is the only thing that separates it from a convention. Its known limits: it sees relative specifiers only, and it scans `src/`, not `tests/`. Both are fine while there is one package and no path aliases, and both stop being fine the moment either changes."

## T41. The surface is a CLI, and the grammar

- "The presentation tier is a **CLI**. An adapter for an agent protocol is at most a thin shell over the same grammar, and may never be built." - `architecture.md` §5.
- "**What is rejected is a shape, not a protocol:** N single-purpose verbs, each deciding when it is called from its own description. This project has measured how fragile that is - **rewording one docstring moved a verb's call count from 1 to 9 with data availability held constant** (`design.md` §3.6)."
- "What replaces it is **one composable grammar with progressive disclosure**: each level renders what is around it, and going one level deeper is one more call. Listing returns ring 0's summary; drilling into a course is a further call; drilling into a single node is the walk."
- "**The distinction is independent of transport, which is why transport is a late and cheap decision.** A server exposing exactly ONE tool whose argument is a command string has the same property; a CLI with forty subcommands, each needing `--help` to know when it applies, has the old defect. **The grammar is the early and expensive decision.**"
- Changelog `architecture.md` 2026-08-27 - Billy - `ruled`.

## T41b. Addressing at the surface

- "**Addressing is the presentation tier's, not the schema's.** §3 rules that identifiers need not be human-facing; the other half is that **the surface may render a record however it likes and resolve at call time, the way a materialized view does.** The `id` is opaque precisely so that nothing at the surface has to mean anything to the layers below. **One constraint binds it:** nothing constructs an id, so **every read that returns records must return their handles** - a handle absent from the render makes the level below unreachable." - `architecture.md` §5, 2026-08-28 - Billy - `ruled`.
- Two consequences, "both presentation-tier work and neither in the first build": "**The render is simultaneously the message and the input to the next call**, and those two pull in opposite directions... The rule: **human-readable by default, a machine branch for machine consumption, and any locator the next call needs must appear in the human render too** - never only in the machine branch."

## T41c. `label` versus `summary`, and the one-line-per-item rule

**Two names for the contested thing:** `label` and `summary`; the corpus calls the open question "`label`-versus-`summary`".

| claim | where | date | who | status |
|---|---|---|---|---|
| nothing in slice 1 is blocked by `label`-versus-`summary` | `design.md` §4, prior text | pre-2026-08-27 | unattributed | **withdrawn** |
| "**`label`-versus-`summary` is deferred, and it is no longer true that nothing is blocked by it.** A navigational surface renders a one-line summary at every level, so the decision is presentation's first one. It stays out of slice 1 because it is presentation, not because nothing needs it." | `design.md` §4 | 2026-08-27 | agent | `measured` |
| "That the summary should be **composed** rather than stored is a recommendation, not a ruling." | `architecture.md` changelog | 2026-08-27 | agent | `measured` |
| "**Every level shows a one line per item, and that line is fields rather than a summary.** A *summary* is a written object, and it is written only where a node's identity is content the skeleton does not hold - **the artifact, and nothing else in the current kind set**. An obligation's line is therefore composed from what it already stores... **The older form of this bullet recommended composing a *summary* from `parts` + `due` + `grade_share`; it is withdrawn**, because it lent the artifact's vocabulary to a kind that has no ingest and so invented a drift problem that does not exist." | `architecture.md` §5 | 2026-08-28 | Billy | `ruled` |

**Changelog reasoning.** `design.md` 2026-08-27 - agent - `measured`: "Found by tracing one of Billy's own example CLI outputs against the field set, which carries no source for *what it is*." `architecture.md` 2026-08-28 - Billy - `ruled`: "The recommendation had borrowed the artifact's mechanism vocabulary for a kind that has no such mechanism, which is where `../plan/backlog.md` B20 came from."

**This ruling collides with `design.md`'s live text.** See D4.

## T41d. Extraction, landing and reading are three concerns

- "`session reads screenshot ──> [candidate facts] ──> land(candidates) ──> Diff`" with outcomes "created · updated · unchanged · CONFLICT" - `design.md` §3.6.
- "They change for unlike reasons - extraction with the material, landing with the schema, reading with agent-engineering practice (SRP). **The third moves on its own, measured: rewording one docstring took a verb's call count from 1 to 9 with data availability held constant.**"
- "**What this record owes is the operation; describing it is presentation tier.**"
- "**`Diff` is the confirmation surface:** the dev-time confirmation toggle reads a `Diff`, and so does F2's conflict question - one return type serves both."
- F2, the requirement it serves: "Landing is idempotent and **detects conflicts instead of overwriting**: *'you told me this, the record says that, which holds'*" - `design.md` §1.

---

# H. Write rules (presentation tier)

## T42. The write-rules record itself - method and partition

- `write-rules.md` conditions: "these are **presentation tier**... They say how to produce a legal value; `schema.md` says what one is. **A rule here never refers to the source.**" (**This last sentence is the one the record's own changelog says was corrected. See D1.**) · "**imported:** none." · "**weaker than this directory implies:** every section marked OWED is a slot with no rule in it yet."
- "**Partitioned by kind and field, mirroring `schema.md`, so that a rule added later has one obvious home.** Do not append to the end of this file: put the rule under its field. **A field with no rule still gets its line, because that line is where the next rule goes.**" - 2026-08-28 - Billy - `ruled`.
- "**How the rules here were obtained, because it is the method.** Writing them in the abstract **stalled for two months** - that mandate is frozen at `../plan/write-rules.md`. **These came from Billy editing one course's extracted records by hand: the rule is what he did, and the before-and-after is the evidence.** Each is stated in the direction it comes from - **what has to be true for the thing to render well** - never from what a source document happens to say."
- Changelog 2026-08-28 - Billy - `ruled`: "created. **Four rules authored by Billy as hand edits to `evidence/2026-08-28-corpus/2c03/records.json`, plus two owed.**"
- Its `## Graveyard` is "_Empty._" (as is `architecture.md`'s and `ring-0.md`'s).

## T43. §1.1 - an inferred value is asked about, not annotated

- "When a source does not state a value and the agent infers one, it **asks the user**. It does not write the inference into a note beside the field." - `write-rules.md` §1.1.
- "Measured: the extraction stored a derived final-exam date and attached a note explaining the derivation. Wrong shape - *'when the announcement about an actual date and time comes, the agent should change the time for that obligation, not attach a note saying that a time is inferred.'*"
- "**An update is an update.** A correction changes the field; it does not accumulate commentary beside it."

## T44. §3.1 - `name` needs no convention

- "**There is no system-owned naming convention, and one is not owed.** Write the label the source uses." - `write-rules.md` §3.1.
- "This was owed only because the `id` used to be minted from the name, which made the name carry the addressing load and so demanded a convention that produced good locators. **The id is now opaque and assigned, so nothing downstream depends on how a name is spelled.**"
- Changelog 2026-08-28 - Billy - `ruled`: "**§3.1 is dissolved rather than answered**... Billy's own material is the evidence that a convention would have been fighting the data."
- **Residual:** the §3 field table still reads "`name` | §3.1 - **OWED**" while §3.1 itself is the answer that dissolves it. See D9.

## T45. §4.0 - the render test for whether a note is worth writing

- "> **'Is it worth being written down so that every time I look at this node, the note comes with it?'** That is the whole rule. **A note is not a place to put things that are true; it is a thing that appears every single time its target is read.**" - `write-rules.md` §4.0.
- "Measured on one course: **20 candidate notes became 12.** What failed the test - course-wide administrative policy (an AI prohibition, a submission-naming convention, the last-day-of-classes rule, the MSAF procedure), a restatement of what an assignment consists of, and **every erratum about a handout revision**, which mattered on the day and never again."
- **Note the tension with `schema.md` §4**, which lists `erratum` as an example `category` value while this rule rejects every erratum measured. Neither record cites the other on this point.

## T46. §4.2 - `body` is a concise self-contained summary, never a quotation

- "**Because a note renders inside the node it hangs on.** A paragraph quoted from a handout is a disaster to read there. Short enough to sit in a rendered node; self-contained enough to mean something alone." - `write-rules.md` §4.2.
- "Measured: *'To get the +1 bonus you must fill in every question of the Attendance Survey including the written one at the end (one or two paragraphs). Open until the end of the day Friday, March 27.'* becomes *'+1 bonus for filling in every question. Open until the end of the day Friday, March 27.'*"

## T46b. Slots with no rule

Recorded because the record says the empty line is load-bearing: `course.name`, `course.term`, `obligation.due`/`done_by`, `obligation.grade_share`/`grade_share_conditional` ("none yet"); `obligation.course`, `course.id` (pointers, not rules); `sticky_note.category`, `sticky_note.origin`, `obligation.name` (**OWED**); all of `progress` ("none yet", with "Only the owner authors it, so an agent may surface a claim and never resolve one"); `about` ("none yet").

---

# I. Scope, the graveyard, and the owed list

## T47. What slice 1 must NOT build

- "No `concept` or `artifact` kinds · no `layer` field · no `LinkKind` beyond `about` · no `closure`, no `nodes_without`, no `look_at` · **no store of any form.**" - `design.md` §4.
- "**No answer to whether `time_point` is a node.** §3.2 keeps both resolutions reachable without touching `Link`. **A part is a raw string, not a node**, and that half is decided."
- The governing rule, stated twice: "**build only the slice whose dependencies are derived**" (`design.md` §1 constraints, §4).
- **Scale is discarded whole:** "**Scale is out of scope, stated once:** one user, one machine, one session at a time, so load estimation, horizontal scaling, failover and redundancy are discarded whole. The only sizing number that matters is that ring 0 for five courses is roughly 55 obligations, and the only availability concern is a scratchpad holding the sole copy of an apparatus." - `design.md` header.

## T48. `time_point`

- "**Not in slice 1.** The type is real - an exam sitting, a review session and a conference are three fixture instances - and is separate from `obligation` because **only obligations consume the weekly hours**. Its reader is the **calendar projection**, which is itself out of slice 1; **the type is out because the projection is, not because nothing reads it.**" - `schema.md` §7 (i.e. in the graveyard, but with an explicit reason that is deferral rather than rejection).
- "`time_point` is **not decided** and §3.2 keeps both resolutions reachable." - `design.md` §3.1. Owner named at `design.md` §7 item 3: "the build, slice 2".
- "**`time_point` and 'the current plan'**, both named by `domain-design.md` §9.1 as part of the projection. `time_point` is not in slice 1; **the plan has no representation anywhere**, and this record does not invent one." - `ring-0.md` §7.

## T49. The graveyard - `schema.md` §7

**Header, verbatim:** "**Deliberately absent - do not re-add without a new ruling.** These fields are not carried. **A later session reading an older document must not restore them.**" Record conditions line: "**§7 is the graveyard. Nothing there is re-added without a new ruling.**"

The corpus does not attach dated changelog lines to individual §7 entries, so for most rows the removing ruling is the row's own stated reason. Where another record names the removing event, I give it.

| absent thing | the ruling that removed it, as stated |
|---|---|
| `workload` / `hours_estimate` | "the world does not supply it, it is not a unit anyone thinks in, and its null is not a gap. Size, where it matters, is observed rather than stored". Removed alongside `status` by the 2026-08-24 grain deletion that `design.md` changelog 2026-08-25 calls "the dead *label/due/status/workload* grain"; `schema.md` §9 item 4 confirms "the fields an older grain named - `status` and `workload` - do not exist" |
| `status.completion` · `files` · `score` · `evaluation` | "none of these is the system's burden. **This does not contradict the finding that a three-axis status prevented two live items being erased; it moots it, since nothing is asserted**" |
| `count{done, of}` | "one instance in 22 (tutorial attendance, 10 of 12), and it counts attendance-as-score, which the row above covers". The `n=1` is qualified in the recurring-obligations row below |
| `stated_in` / `source_ref` | "Not carried" - no reason given |
| **`obligation.notes`** | "under the **non-overlap rule**: a **negative** definition (*'everything no mechanism reads'*) cannot be non-overlapping, and across the 22 fixture rows it carried **six unlike purposes**. **All free text lives on annotations**, which carry `created_at`/`updated_at` and a maintenance-at-read rule" |
| **release dates** ("*Starts February 9*", 2 of 9, printed on the acceptance-(b) screenshot itself) | "noise. Nobody cares when an assignment was released, and the system needs it even less" |
| **per-part weights and per-part scores** | "modelling sub-items costs more complexity than it returns. **Measured and knowingly given up** - 2aa4 A1 splits `5% / 2.5% / 2.5% / 5%` and A2 `3.5% / 3.5% / 5.5%` (3 of 7), and 6 of 9 2c03 assignments are two independently assessed parts. **`parts[]` therefore carries no status and no score of its own**" |
| **coarse dates** ("*April 2026*", the Final Exam) | "a date that is not fixed is null. **The term's largest obligation therefore stores a null `due`**" |
| **recurring / countable obligations** (weekly labs, quizzes, tutorial participation) | "keeping them out explicitly is preferred to the complexity of representing them. **Known cost, recorded rather than argued away:** the `n=1` behind not carrying `count` was measured on the two courses least likely to contain recurring items, and 2px3 was excluded throughout". Load-bearing downstream: `architecture.md` §4 uses this row to disqualify the 22-obligation count |
| `status.evaluation` | "reaffirmed against the challenge that *'what do I still owe attention to'* is a deterministic query returning A2 and A9. **That challenge's hidden premise is that unread feedback is worth attention, and the only authority on that says it is not**" |
| `course.offering_term` · `course.prereq` | "null for both courses in the fixture, and `offering_term`'s justification is another domain's need, **in a domain that does not exist**" |
| `course.manifest` | "**exactly redundant with the rows** - 2c03 lists 15 and has 15, 2aa4 lists 7 and has 7. An obligation declared but unscheduled is a row with a null `due`" |
| `course` free-text field | "nothing identifiable would go in it, and such material belongs on a note". Corroborated by §1's "`course` has **zero**" free-text fields |
| `term_start` | "one week-relative obligation in 22" |
| `due_precision` as a separate flag | "the distinction lives in `due`'s own type" |
| `time_point` | See T48 - the only entry whose reason is deferral rather than rejection |

**Note on the evidence base.** Every count in this table is stated over the 22-row fixture or the two-course corpus, both of which `architecture.md` §4 (2026-08-28) says are superseded, and one of which `schema.md`'s own 2026-08-27 changelog calls "a fixture that was rejected as a golden set". The graveyard's ruling stands under `schema.md`'s no-re-add rule; its arithmetic rests on material two other rulings have set aside. Flagged, not adjudicated.

## T50. The owed list - `schema.md` §9

**Blocking a writer:** (1) `parts` birth rules + prompt; (2) a write rule for `sticky_note.category`.
**Owed to a later cycle:** (3) the free-text length bound's number; (4) "**A projection grain, owed to slice 4.** No current grain names the ring 0 fields `done_by`, `grade_share` and `optional`, and the fields an older grain named - `status` and `workload` - do not exist"; (5) "**The domain boundary.** The tier boundary is stated, and with it the rules that follow from it. **What is still unstated is which facts about a semester are this system's burden at all.**"

- Changelog `schema.md` 2026-08-27 - agent - `agent-drafted`: "§9's owed list rewritten against the current model. Four items were added that no list carried - the node-kind discriminator, identity, obligation-to-course linkage, and which of `parts`'s two readers drives the wording - and item 5 is now partly answered by `architecture.md`."
- Changelog `schema.md` 2026-08-25 - agent - `agent-drafted`: "§9 owed item 4 rewritten: `domain/domain-design.md` §9.1 is now marked dead in place, so what remains owed is a REPLACEMENT grain, and it is owed to slice 4 rather than to this batch."
- **Items 1 and 4 read as stale against records created on 2026-08-28.** See D7 and D8.

---

# Disagreements

Ordered by how live they are: unresolved and in the current bodies first, then resolved-with-a-record, then numeric.

## D1. "A write rule never refers to the source" - a ruling contradicted by the rules written under it, and by its own correction

| side | text | where | date | who |
|---|---|---|---|---|
| A | "**A write rule never refers to the source.** `[R]`... A schema rule of the form *the value must be what the source stated* is unenforceable by construction and does not belong here." | `architecture.md` §3 | 2026-08-27 | Billy, `[R]` |
| A (echo) | "A rule here never refers to the source." | `write-rules.md` conditions block, lines 3-4 | still present | unattributed |
| B | "**the condition line's absolute phrasing is corrected.** *'A rule here never refers to the source'* **was contradicted by three of the five rules**; the real distinction is **the direction a rule is derived from**." | `write-rules.md` changelog | 2026-08-28 | agent, `measured` |
| B (instances) | "**store what the material prints**" (§3.1) · "`optional` **defaults to false unless a source states otherwise**" (§3.5) · "When a source does not state a value and the agent infers one, it asks the user" (§1.1) | `write-rules.md` §1.1, §3.1, §3.5 | 2026-08-28 | Billy, `ruled` |

**The sharp part: the correction never landed in the body.** The changelog says the line was corrected; the conditions block still carries the uncorrected sentence verbatim, and `architecture.md` §3 still carries it as a `[R]` ruling. A reader entering either record from the top gets the withdrawn phrasing.

## D2. 22 obligations versus 14, and the fixture's standing

| side | text | where | date | who |
|---|---|---|---|---|
| A | "Ring 0 holds all **22** real obligations with no free-text escape hatch" (F5) | `design.md` §1 | body as of 2026-08-27 | unattributed |
| A | "3 of 22 rows that are exam sittings" · "12 of the 22 fixture obligations carry parts" · "one instance in 22" · "across the 22 fixture rows" · "one week-relative obligation in 22" | `schema.md` §3, §6, §7 | current bodies | unattributed |
| B | "The 22 came from a transcription that has since been superseded: a fresh extraction from source found **14** for 2c03, and the old count included a row the graveyard forbids... **22 is not reachable by re-running the old route.**" | `architecture.md` §4 + changelog | 2026-08-28 | Billy, `ruled` |
| B | the `optional` tally "counted **a fixture that was rejected as a golden set**" | `schema.md` changelog | 2026-08-27 | agent, `agent-drafted` |
| C | "**6 of 14** obligations carry an annotation and 8 carry none" | `ring-0.md` §4 | 2026-08-28 | agent, `measured` |

`design.md` F5 and every count in `schema.md` §7 still stand on the number `architecture.md` disqualified. Note that `schema.md`'s own changelog had already called that fixture rejected the day before `architecture.md` amended the criterion, and neither correction propagated to `schema.md`'s body.

## D3. Python versus TypeScript, in `design.md`'s constraint line

| side | text | where | date | who |
|---|---|---|---|---|
| A | "**Constraints** - **directly-callable Python**, no MCP, no Postgres, no `PA_SOURCE`" | `design.md` §1 | body as of 2026-08-27 | unattributed |
| A | "the implementation language is **not committed to Python** - Rust and Go have no inheritance" | `design.md` §3.7 | 2026-08-27 | unattributed |
| B | "**TypeScript**... **Python cannot refuse**" | `architecture.md` §6 | 2026-08-27, amended 2026-08-28 | Billy, `ruled` |

`design.md` §3.7 is compatible with B (it says "not committed to Python"); §1's constraint line is not, and is the one a reader hits first. `architecture.md` §2 lists `design.md`'s presentation-tier passages as marked, but the language constraint is not among them.

## D4. `look_at`'s return shape, and whether an obligation has a `summary`

| side | text | where | date | who |
|---|---|---|---|---|
| A | "`look_at(node_id, question) -> { summary, annotations[], edges[] }`, each annotation carrying its kind" | `design.md` §3.7 | body as of 2026-08-27 | unattributed |
| A | "`look_at(node_id, question)` returns a node's **summary**, its annotations, and its edges **with roles** plus the neighbours' summaries - a 1-hop neighbourhood, nothing more" | `design.md` §3.4 | body as of 2026-08-27 | unattributed |
| B | "**It does not state the return shape, and the `{ summary, annotations[], edges[] }` it used to quote was not one.** That triple was written for an application-tier verb; `look_at` is presentation, and a **complete** contract has to say where a node's own typed fields arrive, which the triple never did - read as complete, it makes `obligation.parts` look homeless" | `schema.md` §4.6 + changelog | 2026-08-28 | agent, `measured` |
| C | "**a summary is written only where a node's identity is content the skeleton does not hold - the artifact, and nothing else in the current kind set.** An obligation's line is therefore composed from what it already stores" | `architecture.md` §5 + changelog | 2026-08-28 | Billy, `ruled` |

`schema.md` removed the triple from itself and said the shape is not its record's to state. `design.md` still carries the triple in two places. And under C, the `summary` slot in that triple has no referent for an obligation at all. The withdrawal has a **demonstrated cost** attached: `schema.md`'s changelog says "a reader concluded from it that `obligation.parts` had nowhere to be returned."

## D5. Where the three `progress` rules are enforced

| side | text | where | date | who |
|---|---|---|---|---|
| A | "**The three differences therefore become construction-time validation rules on each kind**, not a type hierarchy - which is where `schema.md` §8 puts every other constraint" | `design.md` §3.7 | body as of 2026-08-27 | unattributed |
| B | only `detail`-requires-`state` runs at construction; one-current-value-per-target is "**the service**"; only-the-owner-authors is "**nowhere, deliberately**" | `schema.md` §4.5 | 2026-08-28 | agent, `measured` |
| B (ground) | "A rule that ranges over more than one record cannot run there - a constructor sees one line" | `schema.md` §8 | 2026-08-28 | agent, `measured` |

`schema.md`'s changelog names the error it fixed: "The record had asserted all three were validated at construction." `design.md` §3.7 still asserts it.

## D6. `nodes(kind, course?)` - one operation or two

| side | text | where | date | who |
|---|---|---|---|---|
| A | "`nodes(kind, course?) -> [Node]` \| enumerate a kind; the projection, the read-back, and `nodes_without`'s first half" | `design.md` §3.4 | body | unattributed |
| B | "**not one operation** \| two service reads wearing one coat: `courses.list()` and `obligations.list(course)`" | `architecture.md` §7 | 2026-08-27 | Billy (direction) / agent (table), `ruled` |

Flagged rather than contradictory: `design.md` §3.4 carries a blockquote saying it is re-homed and "no longer a tier's contents", and was "marked in place rather than deleted, because it remains correct about the graph." Recorded here because the operation table is still the only place the signature is written down.

## D7. `parts` - owed or ruled

| side | text | where | date | who |
|---|---|---|---|---|
| A | "**`parts` birth rules + prompt** (§6) - **before anything writes the field.** What is owed is what counts as one, what context the writer must hold, and what the wording is for." | `schema.md` §9 item 1, "**Blocking a writer**" | current body | unattributed |
| A | "Nothing writes this field yet: **its write rule is owed** (§6, §9)" | `schema.md` §3 | current body | unattributed |
| B | §3.4 answers what counts as one (the recurrence test, 50 candidates → 28) and what the wording is for (canonical singular concept name) | `write-rules.md` §3.4 | 2026-08-28 | Billy, `ruled` |

`write-rules.md` was created on 2026-08-28 to be exactly this rule's home; `schema.md`'s owed list was last rewritten 2026-08-27 and does not cite it. The third sub-item ("what context the writing agent must hold") is unanswered in both.

## D8. The projection grain - owed to slice 4, or already written

| side | text | where | date | who |
|---|---|---|---|---|
| A | "**A projection grain, owed to slice 4.** No current grain names the ring 0 fields `done_by`, `grade_share` and `optional`" | `schema.md` §9 item 4 | current body | unattributed |
| B | `ring-0.md` §4 is a grain and names `done_by`, `grade_share` and `optional` explicitly, with a band assignment and a reason for each | `ring-0.md` §4 | 2026-08-28 | Billy (direction) / agent (the table), `mixed, marked per section` |

`ring-0.md`'s own conditions say it "**supersedes nothing**" and "answers what §9.1 left open" - i.e. it positions itself against the *domain* record's dead grain, not against `schema.md` §9 item 4. Neither record cites the other on this. Note also that B *excludes* `grade_share` while A asks for a grain that *names* it; naming and including are not the same, and no record says which A meant.

## D9. `name`'s write rule - OWED or dissolved

| side | text | where |
|---|---|---|
| A | "`name` \| §3.1 - **OWED**" | `write-rules.md` §3 field table |
| B | "**There is no system-owned naming convention, and one is not owed.**" | `write-rules.md` §3.1, ruled 2026-08-28 by Billy |

Same file, adjacent sections. The changelog entry that landed B is explicit ("§3.1 is dissolved rather than answered"); the pointer table was not updated.

## D10. `about` link counts and whether any note hangs on a course

| side | text | where | date |
|---|---|---|---|
| A | "`about` ... **18 instances measured**, targets across all three layers, **zero at course level in the material** - the course case comes from the late-day budget living on a note" | `design.md` §3.3 | imported 2026-08-25 from openclaw evidence |
| B | "of the **11 notes** in the corpus, **4 hang on the course** and **7 hang on individual obligations**" | `ring-0.md` §7 | 2026-08-28, agent, `measured` |
| B | "across the **11 notes** that exist, one value holds 8 of them" | `schema.md` §4 | current body |
| C | "**6 of 14** obligations carry an annotation and 8 carry none" | `ring-0.md` §4 | 2026-08-28 |

18 versus 11 annotations, and "zero at course level" versus "4 hang on the course". The two may be different corpora (`design.md`'s numbers are cited to openclaw evidence that "stayed in openclaw"; `ring-0.md`'s to a 2026-08-28 corpus), but both are stated as the count of `about`-type facts in the material, and no record reconciles them. Load-bearing on both sides: `design.md` §3.2 uses the course case to argue a course must be a node in slice 1; `ring-0.md` §7 uses the 4/7 split to say the course level is owed 4 notes.

## D11. `grade_share`'s reader

| side | text | where |
|---|---|---|
| A | "no mechanism reads it, and the exemption is the point"; reader column "**none, by exemption**" | `schema.md` §3, `grade_share` |
| B | `grade_share_conditional`'s reader column reads "**any reader of `grade_share`**" | `schema.md` §3, adjacent row |

A field with no reader, whose companion field's reader is defined as that field's readers. Internal to one table; no record notices it.

## D12. `N≈300` versus `V=640`

`design.md` §3.4: "Two queries earn their keep at **N≈300**". `design.md` §3.4 cost table and §5: "**V=640**", "~640-1,600 nodes". Same record, same section, unreconciled.

## D13. `erratum` as a `category` value versus every erratum failing the render test

`schema.md` §4 lists `erratum` among `category`'s example values. `write-rules.md` §4.0's measured pass rejected "**every erratum about a handout revision**, which mattered on the day and never again". Not formally contradictory (the schema names a legal value; the write rule says when to write one) but the schema's illustrative example is the class the write rule most consistently discards.

## D14. The coordinator's lifetime

`design.md` §5 conclusion 1: "**The coordinator's lifetime is not a deciding fact here, and must not be reintroduced as one**... The skeleton and its verbs are **invoked on demand**; every call may be a new process." `ring-0.md` §2: "**the design's coordinator is long-running**". Not a contradiction on its own terms - `design.md` distinguishes the conversation's lifetime from a process holding the graph - but the two records use "the coordinator" for different things, and `ring-0.md` §1 and §7 lean on residency ("held **resident** by the coordinator", "resident for the coordinator and for nobody else") in a way that reads against `design.md`'s prohibition unless the distinction is carried forward.

## D15. Resolved in-record, recorded for the trail

- **`progress.state` nullability** (T14): a measured prohibition reversed by a ruling. The reversal's own analogy-consumers (`optional`, `grade_share_conditional`, T11/T13) were not revisited.
- **`sticky_note.kind` → `category`** (T18): resolved by the 2026-08-27 discriminator ruling.
- **`finished_by` → `done_by`** (T9): resolved; the record says `finished_by` "never had a ruling behind it".
- **Packages → directories** (T40): reversed within a day on a checkable fact about npm.
- **Validation at load** (T32): claim withdrawn on measurement.
- **`added_at` on every node** (T5): corrected to two kinds.
- **Annotation counts 5/9 → 6/14** (`ring-0.md` changelog 2026-08-28).
- **`parts` history misread** (`write-rules.md` changelog 2026-08-28): an agent read the archive as current and mis-stated who ruled what.
- **§4.5's "neither has been edited" paragraph** (`schema.md` changelog 2026-08-25): "**stale and told the next session that two live records disagree with this one when they no longer do.** Found by a cold-start reader, not by the edit that made it stale."

---

# Supersession evidence

Every explicit statement of supersession in the corpus, by direction.

## Records superseding other records

| superseding | superseded | statement | where |
|---|---|---|---|
| `architecture.md` | all of `records/spec/` | "**This record governs every other record in `records/spec/`**, and it re-scopes `design.md`, whose bounded question was written before the split existed" | `architecture.md` conditions |
| `architecture.md` §7 | `design.md` §3.4 | "**Re-homed by `architecture.md` §7.**... it is **no longer a tier's contents**" | `design.md` §3.4 blockquote; `architecture.md` §7 |
| `architecture.md` | `design.md`'s presentation passages | "**re-scoped by `architecture.md`**... Its passages about docstrings, verb descriptions and the MCP adapter are **presentation** tier, are not this document's to decide" | `design.md` changelog 2026-08-27 |
| `architecture.md` §3 | `schema.md` §1.1's old id scheme | "It also contradicted `architecture.md` §3, which had already ruled that the agent never constructs an identifier - **a divergence between two ruled records that nobody had propagated**" | `schema.md` changelog 2026-08-28 |
| `architecture.md` §3 | the `progress.state` null prohibition | "The ground for reversing it is `architecture.md` §3" | `schema.md` changelog 2026-08-28 |
| `architecture.md` §5 | `design.md` §4's label/summary claim | "**`design.md` §4's claim that label-versus-summary blocks nothing is no longer true**" | `architecture.md` changelog 2026-08-27 |
| `architecture.md` §4 | the 22-obligation criterion | "**amended from 22 obligations across two courses to one course's real obligations**... The 22 came from a superseded transcription" | `architecture.md` changelog 2026-08-28 |
| `architecture.md` §7 | `land()` as a primitive | "**`land()`... is therefore not in the first build**" | `architecture.md` §7 |
| `schema.md` §4.6 | `design.md`'s `look_at` triple | "the `{ summary, annotations[], edges[] }` it used to quote **was not one**" | `schema.md` §4.6, changelog 2026-08-28 |
| `write-rules.md` §3.4 | `archive/changelog-2026-08-24-slice-1.md` §14.4 | "the second is now ruled and **the recommendation is dead**" | `write-rules.md` changelog 2026-08-28 |
| `ring-0.md` | nothing | "**It supersedes nothing**; it answers what §9.1 left open" | `ring-0.md` conditions |

## Records superseded within themselves

| record | what it retired | statement |
|---|---|---|
| `architecture.md` §6 | its own packaging ruling, 24 hours old | "**§6 reversed**: the tiers are directories under one source root, not separate packages. **The original ruling's ground... under npm that is false**" |
| `architecture.md` §5 | its own composed-summary recommendation | "**§5's composed-summary recommendation is withdrawn**" |
| `schema.md` §1.1 | `<course_id>-slug(name)` | "the `<course>-slug(name)` scheme **is retired**" |
| `schema.md` §4.5 | non-null `state` being illegal | "**The prohibition this reverses**... a defined default is not an invention" |
| `schema.md` §8 | validation-at-load | "**§8 no longer claims that validation happens at load**" |
| `schema.md` §7 | fifteen fields, standing rule against re-adding | "**do not re-add without a new ruling**... A later session reading an older document **must not restore them**" |
| `design.md` §3.2 | property 3's forward-reference mechanism | "**What this is no longer for**... That route is closed" |
| `design.md` §4 | its own "nothing is blocked" claim | "**is withdrawn**" |
| `design.md` §3.7 | the label/due/status/workload field list | "the field list was decoration and **is now wrong**" |
| `write-rules.md` §3.1 | the owed naming convention | "**§3.1 is dissolved rather than answered**" |
| `write-rules.md` conditions | its own absolute phrasing | "the condition line's absolute phrasing **is corrected**" (**the body edit did not land - D1**) |
| `write-rules.md` §3 table | two application-tier facts | "**demoted to pointers**... was giving an agent recommendation `ruled` standing by placement" |

## The corpus naming supersession as a standing hazard

Three passages say, in their own words, that superseded material keeps authority in this repo:

1. "**Recorded because a plan that predates the split still reads as authority.**" - `architecture.md` §4 opening.
2. "**a divergence between two ruled records that nobody had propagated.**" - `schema.md` changelog 2026-08-28.
3. "**The error: the archive's §14.4 was read as the current state of the question without opening the changelog of the record that owns the field.**" - `write-rules.md` changelog 2026-08-28.

And two more where the discovery mechanism is named as an outside reader rather than the edit that caused the staleness: "Found by a cold-start reader, not by the edit that made it stale" (`schema.md` changelog 2026-08-25); "Found by the migration's citation sample, not by the edit that marked §9.1 dead" (`design.md` changelog 2026-08-25); "Both found by the next sitting reading the corpus rather than this record" (`ring-0.md` changelog 2026-08-28).

## Non-supersession, stated explicitly

Worth recording because the corpus is careful about it:

- "**The five refactor triggers and §3's abstractions are unaffected**" by the tier re-scoping - `design.md` changelog 2026-08-27.
- "**Idempotency is unaffected**" by the id change - `schema.md` changelog 2026-08-28.
- "**The 2026-08-26 ruling that write rules precede the build still holds and its target changed**" - `architecture.md` §4.
- "**The 2026-08-27 ruling that made it nullable stands**" - `write-rules.md` changelog 2026-08-28, on `optional`.
- "**`schema.md` §3 is unchanged**" - `write-rules.md` §3.5.
- "**`land()` is not wrong and is not the bottom.**" - `architecture.md` §7.
- "**The competing responsibility... is itself ruled and is not retired by this**" - `schema.md` changelog 2026-08-27, on `parts` (later closed the same day).
- "**This does not contradict the finding that a three-axis status prevented two live items being erased; it moots it**" - `schema.md` §7.

---

# Is the spec tier superseded?

The hypothesis to test: this spec material is likelier to be superseded than the domain material, **especially anything schema-level**. I did not read the domain material, so I cannot compare the two directly; what follows is evidence about the spec tier's own volatility and about where inside it the volatility sits.

## Evidence for

**1. The churn is real, dated, and concentrated.** `schema.md` carries **21 changelog entries across four days** (08-25, 08-27, 08-28), six of them on 2026-08-28 alone. In that window it changed: the id scheme, `course.id`'s exception, `progress.state`'s nullability (a reversal of a measured prohibition), `finished_by` → `done_by`, `sticky_note.kind` → `category`, `optional` and `grade_share_conditional` to nullable, `added_at`'s scope, where validation happens, where `progress`'s three rules are enforced, and `look_at`'s return shape. Nine of those are field-level or wire-level, which is exactly the "schema-level" material the hypothesis singles out.

**2. Reversals reached rulings less than a day old.** `architecture.md` §6's packaging ruling was made 2026-08-27 and reversed 2026-08-28 on a fact about npm that was checkable before the first ruling. `schema.md`'s `parts` responsibility was ruled twice on 2026-08-27, the second closing what the first left owed.

**3. The corpus documents its own unreconciled state, three times** (see Supersession evidence, "standing hazard"). `architecture.md` §4 exists *because* superseded material keeps authority.

**4. Four live contradictions survive in current bodies** (D1-D5): the write-rules condition line whose correction did not land; the 22-obligation count in `design.md` F5 and throughout `schema.md` §7; "directly-callable Python"; the `look_at` triple and the summary-for-an-obligation; the construction-time enforcement claim. In each case the superseding ruling exists and is dated, and the superseded text is still what a reader hits first.

**5. Two owed items are stale against records created to answer them** (D7, D8): `schema.md` §9 items 1 and 4, versus `write-rules.md` §3.4 and `ring-0.md` §4, both dated 2026-08-28.

**6. The evidence base under the schema is itself disqualified.** `architecture.md` §4 says the 22-row transcription is superseded; `schema.md`'s own changelog calls that fixture "rejected as a golden set". Every count in `schema.md` §7's graveyard is stated over it.

**7. Spec ran ahead of code, and the corpus says so.** `write-rules.md` §3: "**The code implements the recommendation; this record does not decide it**" - the code is executing a plan-tier recommendation that no spec record ruled. And `architecture.md` §4's "three cycles specifying descriptions for methods that do not exist" (§1) is the same failure named from the other end.

**8. Container drift is an independent supersession vector.** A large fraction of the corpus rules on properties of a standalone CLI app with a long-running coordinator process (see Container-sensitive rulings). None of those rulings is stale *by time*; they are stale *by container* if the container has changed. The records contain no test for this, because the container was not in question when they were written.

## Evidence against

**1. The reversals are evidence-driven, not taste-driven.** Each of the big ones names the observation that defeated it: real spellings (`ChildMath A1` / `ChildsMath A4`) defeated the derived id; a store with `due: "April 2026"` and a slice-2 `concept` node loading clean defeated validation-at-load; a constructor seeing one line defeated the three-rules-at-construction claim; npm hoisting defeated packages-as-enforcement; a six-run misread defeated `finished_by`. A ruling overturned by a measurement is a different object from a ruling that decayed.

**2. The reversal machinery is complete enough that supersession is recoverable.** Every reversal names what it replaced, why, who ruled it, and what standing the replacement has. Nothing in this corpus is silently gone. That is the property that makes the four live contradictions (D1-D5) findable at all - I found them from the changelogs, not from suspicion.

**3. The abstraction tier did not move.** `design.md` §2's five triggers and §3's abstractions are recorded as explicitly "**unaffected**" by the re-scoping that hit everything around them. `Ref = (kind, id)`, one id space, `kind` as data not control flow, relations as records not fields, `locator` in the link identity, annotation as a tag not a hierarchy - none of these has a reversal entry anywhere in four days of changelogs, and three of them are restated verbatim in a second record. This splits the hypothesis: the **field-level** material churned hard; the **abstraction-level** material did not.

**4. `architecture.md`'s core is untouched.** The three-tier split and the four `[R]` §3 consequences are 2026-08-27 and have not been amended. What was amended in that record is §4, §5 and §6 - the criterion, the summary recommendation, the packaging - not §1 or §3. And §3's four consequences are the grounds cited by the *later* rulings in `schema.md`, which is the shape of load-bearing material rather than of superseded material.

**5. The graveyard has held.** Fifteen entries, a standing rule against re-adding, and no record anywhere re-adds one. The one entry that is deferral rather than rejection (`time_point`) says so explicitly in its own row.

**6. The newest material is the least contradicted.** `ring-0.md` and `write-rules.md` were both created 2026-08-28 and both fill named vacuums (a dead field grain; a two-month-stalled mandate). Neither has been contradicted by anything, and `write-rules.md`'s method - rules derived from Billy's own hand edits rather than written in the abstract - is the one procedural change the corpus records as having broken a stall.

**7. Several rulings triangulate.** Ring 0 as an access policy over `obligation` nodes rather than a separate store appears in three records in near-identical words. The no-free-text-in-the-projection table appears in three records identically. The 7-edge `locator` collapse appears in two. Where three records agree without citing each other, drift has not happened.

## What I can and cannot say

I can say the volatility is **not uniform**, and that its distribution is the opposite of what "the spec tier is superseded" would predict if taken flat: the field-level layer (`schema.md`'s tables, `write-rules.md`'s slots) moved constantly, the tier-level and abstraction-level layers (`architecture.md` §1/§3, `design.md` §2/§3.0-§3.3) did not move at all. The hypothesis's own qualifier - "**especially anything schema-level**" - is the part the evidence supports, and it supports it strongly. The unqualified form is not supported by what these five files contain.

I cannot say whether the spec is *more* superseded than the domain, because I did not read the domain records. What I can report is that the spec records **defer to the domain records repeatedly and never overrule them**: `ring-0.md` inherits three constraints from `domain-design.md` §9.1/§9.2/§9.5 and says it "supersedes nothing"; `architecture.md` §2 places `../domain/` outside the tier scheme as "the material both tiers are derived from"; `schema.md`'s 2026-08-27 changelog restores a mechanism vocabulary (M1-M5) *from* the domain records that "**had never reached this record**". Two data points cut the other way: `ring-0.md` §2 declines `domain-design.md` §9.2's membership test, and `ring-0.md` §5 finds the projection "**has been violating**" §9.2's asymmetry rule. Both are the spec deferring to the domain's authority while disagreeing with a specific instrument, not the spec overruling it.

**The strongest single piece of evidence, in either direction,** is `write-rules.md`'s 2026-08-28 self-correction. An agent read an archived record's §14.4 as the current state of a question, recommended what it recommended, and got the *right rule for the wrong reason* - and the correction says so: "the rule it landed **is not** [wrong]". That is simultaneously proof that superseded spec material actively misleads readers in this repo, and proof that the changelog discipline catches it.

---

# Container-sensitive rulings

Flagged only. The old container is a standalone repo running as an app a human uses; the successor is a set of components an agent (Claude Code) uses. I do not judge which of these survive.

## Rulings about a CLI surface a person operates

- **"The presentation tier is a CLI"** and the whole of `architecture.md` §5 - the composable grammar with progressive disclosure, the rejection of N description-routed verbs, "the grammar is the early and expensive decision".
- **"human-readable by default, a machine branch for machine consumption, and any locator the next call needs must appear in the human render too - never only in the machine branch"** (`architecture.md` §5). This rule presupposes a human reading the primary render and a machine reading a branch. In the successor container the primary reader is the agent.
- **"Every level shows a one line per item"** and the whole label-versus-summary question (`architecture.md` §5, `design.md` §4, T41c). Framed as "a navigational surface renders a one-line summary at every level".
- **`schema.md` §1's "null... must render as absence"** and **§4.5's "the rendering is per kind of target - *Submitted* for an assignment, *Written* for an exam"** - render rules inside the record that declares render rules out of scope.
- **`ring-0.md` §7's unruled content split**, whose missing term is explicitly a human-versus-coordinator asymmetry: "**a person at the surface holds nothing**, so the same call is redundant to one reader and the only view of a course to the other".
- **The whole of `write-rules.md`**, by its own account: every rule is derived from "what has to be true for the thing to **render well**", and §4.0's test is "is it worth being written down so that **every time I look at this node**, the note comes with it?" First person, a human reading.

## Rulings about a long-running in-process coordinator

- **Residency itself.** "held **resident** by the coordinator" (`ring-0.md` §1); "losing the coordinator costs **one projection read** to rebuild" (§1, from `domain-design.md` §9.5); "**ring 0 is resident for the coordinator and for nobody else**" (§7). Residency is a property of a process that persists between reads.
- **`ring-0.md` §2's instrument critique**: "every run was a memoryless `claude -p` cold start, and **the design's coordinator is long-running**". The whole refusal of the null result rests on the container being a persistent coordinator.
- **`design.md` §3.5's purity cut**: "The coordinator holds neither... the coordinator holds the skeleton interface and does not hold the store interface". Trigger D is a statement about what one process's object graph contains.
- **`design.md` §5's per-invocation model**, and its explicit warning in the other direction: "every call may be a new process"; "Under a resident-process assumption that difference reads as tuning; under the real one it is the reason the two sides get different mechanisms". Both the ruling and its stated alternative are container facts.

## Rulings about a specific repo, language and toolchain

- **TypeScript** (`architecture.md` §6), and its argument - "a compiler that can refuse" - which is about the build container, not the domain.
- **"the tiers are directories under one source root"** and **`app/tests/boundary.test.ts`** (`architecture.md` §6), including its stated limits ("it sees relative specifiers only, and it scans `src/`, not `tests/`").
- **`fall26/ingest.py` "stays Python as an offline pass and is in no tier"** (`architecture.md` §6).
- **`design.md` §1's constraints**: "directly-callable Python, no MCP, no Postgres, no `PA_SOURCE`". Every item names a tool or its absence.
- **`schema.md` §8**: `nodes.jsonl` + `links.jsonl`, `schema_version`, "a **side binary store keyed by node id**", "rewritten intact by the next flush". File-layout rulings.
- **`design.md` §5's Kùzu market fact** - a dependency-landscape observation with a shelf life.
- **`design.md` §5's overturning conditions**: "multi-device sync becoming real (a MacBook plus the deferred Mac Mini)". Hardware.

## Rulings about an MCP / tool-description container

- **The 1-to-9 docstring measurement** (`design.md` §3.6, quoted again at `architecture.md` §5) - "rewording one docstring took a verb's call count from 1 to 9 with data availability held constant". This is a measurement of an LLM routing over tool descriptions, and it is the load-bearing evidence for two separate rulings (reading is a separate concern; the grammar beats N verbs).
- **The MCP adapter's demotion** (`architecture.md` §4, §5): "at most an adapter over the CLI's grammar, **and may never be built**". A ruling that an agent protocol is secondary to a human CLI.
- **The verb-routing evaluation and the screenshot-extraction evaluation** (`architecture.md` §4), both re-homed to presentation and both testing agent behaviour against descriptions.
- **`design.md` §1 F1**: "A pasted portal screenshot, **read by the session itself**... **No API call**". The extraction mechanism is a property of the session the app runs inside.
- **`design.md` §3.6**: "**the dev-time confirmation toggle** reads a `Diff`". A development-mode affordance of the old app.

## Rulings about a single human user's daily habits

- **`architecture.md` §3's "The system must not chase the agent"**, quoted from Billy in the first person about "daily usage". This is the ground cited by two later `schema.md` rulings (T11, T14), so its container-sensitivity propagates.
- **`architecture.md` §3's "The agent never auto-adds anything unless it is clear the user wants it. What gets a row is what the user wants tracked, and the user triggers it."**
- **`done_by`'s 7-day rule** and "**the one place the system's anxiety-removal goal reaches the schema**" (`schema.md` §3, `ring-0.md` §3). A schema field justified by a human emotional outcome.
- **`ring-0.md` §3's active window `today-7d .. today+14d`**, whose standing is derived from "the +/-1-2 week observation" recorded as "a requirement **Billy may state**".
- **`design.md`'s scale paragraph**: "one user, one machine, one session at a time".
- **`architecture.md` §6's "Neither is chosen, on iteration speed for a solo build."**
- **`architecture.md` §4's "extracting the other three courses is not worth doing before the presentation tier exists"** - a sequencing ruling about one person's remaining effort.

## Not flagged, for contrast

The following read as properties of the domain rather than the container, and I record that judgment only to show the flag is discriminating: obligations belong to exactly one course; `due` anchors both a hand-in deadline and a sitting's start; a conditional or bounded grade share is not a stated fact; a note is an entity pointing at a node rather than a property of one; only the owner can author progress; `parts` carries concepts that recur; two citations at the same locator are one edge; an id must not be derivable from a name that two documents spell differently.

---

# Coverage

## Read in full

All five files, body and changelog, line 1 to end: `design.md` (268 lines), `schema.md` (253), `write-rules.md` (180), `architecture.md` (136), `ring-0.md` (104). 941 lines total. Every `## Changelog` was read in full; 21 entries in `schema.md`, 13 in `architecture.md`, 8 in `write-rules.md`, 7 in `design.md`, 5 in `ring-0.md` - 54 changelog entries in all, and every claim in the Disagreements and Supersession sections above is sourced to one of them or to a body section I quote.

## Skimmed

Nothing. There is no material in these five files I read at lower resolution than the rest.

## What I could not account for

**Cited but outside the boundary - not read, and every claim I attribute to them is reported as the spec record states it, unverified:**

- `records/domain/model.md` §7.1, §8.2 · `records/domain/domain-design.md` §6.2, §8.2, §9.1, §9.2, §9.5. Load-bearing: ring 0's three inherited constraints, the symmetry rule, the dead field grain, and the "summary is written only for the artifact" ruling all rest on these.
- `records/plan/backlog.md` B19, B20, B27 · `records/plan/write-rules.md` (the frozen two-month mandate) · `records/plan/application-tier.md` §7.1 (the unruled `obligation.course` immutability recommendation that the code implements).
- `records/archive/changelog-2026-08-24-slice-1.md`, cited twice: `:241` (the `23:59` ruling's origin) and §14.4 (the `parts` recommendation that misled a reader).
- `findings/read-cycle.md` §4, §5 - the null result on the judgment-change test, and the 24/17 and 29-of-77 faithfulness counts that carry `grade_share`'s exclusion.
- `evidence/2026-08-27-tier-recut/derivations/L3-surface.md` · `evidence/2026-08-28-corpus/2c03/records.json` (the source of all four write rules).
- `openclaw:fall26/2026-08-22-derivation/` (where `design.md` says its §3.3 and §5 measurements stayed) · `openclaw:fall26/2026-08-23-slice-1/CAVEATS.md` §1, §7 · `openclaw:fall26/2026-08-24-slice-1-write/DESIGN.md` and `SCHEMA.md` (the import sources).
- `app/tests/boundary.test.ts` · `fall26/ingest.py`. No code was read.

**Gaps inside the corpus that no record fills:**

- **Attribution is absent from every body.** By design - three records state it ("the body carries no standing tags, no attributions and no history"). Consequence: for any body claim with no matching changelog line, I could record the claim and its location but not who ruled it or when. That is most of `design.md` §1, §3.0-§3.3, §3.5, §3.6 and §6, and most of `schema.md` §7. I marked these "unattributed" rather than guessing.
- **`design.md` §7's four open items name owners** (the user ×2, the build slice 2, the build slice 3) but no dates and no status markers. I recorded them as stated.
- **`schema.md` §7's fifteen graveyard entries carry no dates and, for thirteen of fifteen, no changelog line.** The task asked what removed each; for most the answer available in this corpus is only the row's own stated reason. Where an external event is named (the 2026-08-24 grain deletion, the `architecture.md` §4 amendment) I said so.
- **The `has-more` field** (`ring-0.md` §4) is declared in a projection but exists in no schema record. `ring-0.md` says this itself: "the only one here that no record has yet declared".
- **`schema.md` §1's `null` convention** cites a measurement ("measured as the largest single class of unfaithful claim") that `ring-0.md` §6 appears to restate with numbers (29 of 77, 38%). Whether these are the same measurement is not stated in either record.
- **Numbers I could not reconcile inside the corpus**, listed at D10 and D12: 18 versus 11 `about` facts; "zero at course level" versus 4; N≈300 versus V=640; 22 versus 14 obligations.

**One thing I deliberately did not do:** the task's context said the repo's status file records that the spec moved ahead of the code twice and was never reconciled. That file is outside the boundary and I did not open it. My evidence on the supersession hypothesis is drawn only from what these five files say about themselves.
