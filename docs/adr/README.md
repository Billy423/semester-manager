# Decision records

**This index is the reading path; the records themselves are reference.** Scan a group, open what applies.

Each record is a title plus one to three sentences and a provenance path. The title states the decision, not the topic, so it can be triaged without opening the file.

A `Source:` line names where the decision was originally made - the predecessor corpus at `~/Documents/Projects/fall26` or the `openclaw` checkout for a migrated record, the issue it was ruled in for one ruled here. It is an **audit trail, not a reading instruction**: every record stands on its own, and needing to open the source to act on one is a defect in that record.

## Purpose and trust — `0001`–`0007` · `0081`

What the system is for, and what it refuses to claim. Every other decision is judged against these.

| | |
|---|---|
| [`0001`](0001-three-jobs-not-precise-answers.md) | The system's job is three jobs, and precise question-answering is not one of them |
| [`0002`](0002-no-outward-completeness-assertion.md) | The system makes no assertions about its own completeness |
| [`0003`](0003-job-three-is-set-difference-not-recall-tuning.md) | Surfacing what Billy did not ask about is a deterministic set-difference query, not recall-tuned retrieval |
| [`0004`](0004-expansion-cost-is-the-size-gate.md) | The size gate is expansion cost, not total graph size |
| [`0005`](0005-the-store-accumulates-it-is-never-synced.md) | The store accumulates; it is never synchronised against a source |
| [`0006`](0006-under-model-deliberately.md) | Under-model deliberately: the relationships cannot be written today |
| [`0007`](0007-park-with-a-wake-condition.md) | Undecided and unimportant questions are parked with the condition that would wake them |
| [`0081`](0081-negative-answer-names-its-boundary.md) | A negative answer names the boundary it speaks for; a bare "it is not known" shifts the burden to the reader |

## The graph — `0008`–`0023`

Nodes, links, layers, and the two things that are persisted. The vocabulary the rest of the corpus speaks.

| | |
|---|---|
| [`0008`](0008-a-course-is-a-node.md) | A course is a node, not a namespace |
| [`0009`](0009-layered-graph-not-a-tree.md) | The skeleton is a layered graph; the model may not cut edges to force a tree |
| [`0010`](0010-modelling-layer-is-stateless.md) | The modelling layer is stateless: system-inferred mastery is forbidden |
| [`0011`](0011-artifact-existence-is-not-a-field.md) | An artifact's existence is not a field; absence is the absence of store content |
| [`0012`](0012-the-closed-link-kind-set.md) | Links are a closed typed set, each with an endpoint signature; a relation earns a row only with three real instances and a nameable query |
| [`0013`](0013-closure-is-single-source-reachability.md) | `closure` is single-source reachability from one node, not an all-pairs matrix |
| [`0014`](0014-no-supersedes-link.md) | There is no `supersedes` link; revisions replace in place and are dated |
| [`0015`](0015-an-announcement-is-a-provenance-value.md) | An announcement is a provenance value, not a node and not a link |
| [`0016`](0016-relations-are-records-not-fields.md) | Relations are records, not fields on the related thing |
| [`0017`](0017-link-identity-is-a-natural-key.md) | A link's identity is its natural key, `locator` is part of it, and a link has no update |
| [`0018`](0018-a-ref-is-not-a-foreign-key.md) | A ref is not a foreign key: a ref may name something that is not there, and nothing cascades |
| [`0019`](0019-two-persisted-things-one-coupling-field.md) | Exactly two persisted things, coupled by one field; ring 0 is not a third |
| [`0020`](0020-the-purity-cut-is-enforced-by-return-type.md) | The purity cut is enforced by return type, not by tool registry or prompt |
| [`0021`](0021-the-skeleton-carries-no-time-axis.md) | The skeleton carries no time axis; time is a separate projection, not nodes and edges |
| [`0022`](0022-materialization-reports-empty-extraction-not-ocr.md) | A materialization pass must report that it recovered nothing; it does not OCR |
| [`0023`](0023-one-lecture-is-one-node-with-a-file-list.md) | One lecture is one node with a file list, not one node per file |

## Fields and identity — `0024`–`0037`

What a field is, when one exists, how a thing is named, and what was removed and must not come back.

| | |
|---|---|
| [`0024`](0024-non-overlapping-field-and-verb-definitions.md) | Every field and every verb has exactly one purpose |
| [`0025`](0025-ids-are-opaque-assigned-and-never-constructed.md) | An id is opaque, assigned and never constructed; one id space, and every read returns handles |
| [`0026`](0026-ids-are-supplied-where-the-material-supplies-one.md) | The id space is deliberately not uniformly opaque: an id is assigned only where the material supplies none |
| [`0027`](0027-kind-is-a-discriminator-layer-is-another-axis.md) | `kind` is a required discriminator, not metadata, and `layer` is a different axis |
| [`0028`](0028-four-conventions-over-every-kind.md) | Four conventions that range over every kind |
| [`0029`](0029-course-membership-is-a-field.md) | Course membership is a field, because the rule that relations are records exists to stop a polymorphic target becoming one |
| [`0030`](0030-a-date-without-a-time-is-2359.md) | A date without a time means `23:59` by schema rule, not by parser default |
| [`0031`](0031-nullable-means-unknown-and-the-writer-defaults-it.md) | A nullable bool means unknown; the writer supplies the obvious default, not the schema |
| [`0032`](0032-a-conditional-weight-gets-a-marker-not-a-model.md) | A conditional grade weight gets a marker, not a model, and the pointer to the rule is optional |
| [`0033`](0033-parts-carries-recurring-concepts-not-size.md) | `parts` carries the concepts that recur, as canonical singular names, and does not carry size |
| [`0034`](0034-an-annotation-is-a-tag-not-a-type-hierarchy.md) | An annotation is a tag over two kinds, not a type hierarchy |
| [`0035`](0035-progress-state-is-non-nullable.md) | `progress.state` is non-nullable and defaults to `not_started`, so the agent has no reason to ask, and it lives on `progress` rather than on `obligation` |
| [`0036`](0036-a-note-points-at-a-node-and-its-category-is-open.md) | A note is an entity that points at a node; `category` is an open string set on purpose, and provenance confers no immutability |
| [`0037`](0037-the-graveyard.md) | The graveyard: removed fields, their reasons, and a standing rule against re-adding them |

## The observation contract — `0038`–`0046` · `0082`–`0085`

What the coordinator holds while it decides, what it walks, and what it discards.

| | |
|---|---|
| [`0038`](0038-ring-0-carries-seven-routing-fields.md) | Ring 0 carries seven routing fields; `parts` and `grade_share` are excluded, and `grade_share`'s exclusion is measured |
| [`0039`](0039-symmetry-not-shallowness.md) | The observation invariant is symmetry, not shallowness, and it is scoped to the set the judgment ranges over |
| [`0040`](0040-renderer-truncation-is-asymmetry.md) | Renderer-introduced truncation is asymmetry, so a fixed-width table is not the course level's shape |
| [`0041`](0041-projection-order-comes-from-the-material.md) | The projection's order is derived from the material, never from write history |
| [`0042`](0042-active-is-three-independent-triggers.md) | Active is three independent triggers on one question, not a time window with exceptions |
| [`0043`](0043-expansions-are-discarded-never-sedimented.md) | What is fetched is dropped; depth never comes back into the conversation |
| [`0044`](0044-the-coordinator-holds-ring-0-not-the-skeleton.md) | The coordinator holds ring 0 in its context and queries the skeleton on demand |
| [`0045`](0045-store-output-enters-only-as-a-conclusion.md) | Store output enters the coordinator only as a conclusion; the context that produced it is discarded, and who produced it is irrelevant |
| [`0046`](0046-the-coordinator-walks-edges-it-does-not-search.md) | The coordinator reaches material by walking a node's edges, never by searching the corpus, and annotations arrive through their own channel |
| [`0082`](0082-a-render-is-derived-from-the-kind-s-field-table.md) | A node's render is derived from its kind's field table by four rules, not designed per kind |
| [`0083`](0083-one-render-serves-both-readers.md) | The render is XML, and one render serves both readers, replacing the human-branch / machine-branch split |
| [`0084`](0084-look-at-is-a-composed-view-not-a-pure-walk.md) | `look_at` is a composed view whose content each kind decides, not a pure edge walk |
| [`0085`](0085-the-question-parameter-is-instrumentation.md) | The `question` parameter is development instrumentation and is not in the production signature |

## Inbound — `0047`–`0058` · `0086`–`0087`

How material and corrections arrive, what the system does with a conflict, and what it never fetches.

| | |
|---|---|
| [`0047`](0047-extraction-landing-reading-are-three-concerns.md) | Extraction, landing and reading are three concerns and they change for unlike reasons |
| [`0048`](0048-the-system-does-not-fetch.md) | The system does not fetch; the boundary starts at the endpoint, and the endpoint is multimodal |
| [`0049`](0049-live-intake-and-corpus-ingestion-are-separate-paths.md) | Live intake and corpus ingestion are two paths, and routing either through the other is a category error |
| [`0050`](0050-inbound-arrives-to-be-known.md) | Inbound arrives to be known, not to trigger an action |
| [`0051`](0051-two-conflicting-statements-never-coexist.md) | Two conflicting statements never coexist, and how a conflict closes depends on what is in conflict |
| [`0052`](0052-intake-is-ordered-and-cross-document.md) | Intake is ordered and cross-document; no artifact is understood alone |
| [`0053`](0053-the-course-site-is-not-a-source-of-truth.md) | The course site is not a source of truth; the system dates what it holds |
| [`0054`](0054-store-inclusion-is-decided-by-the-store-not-the-file.md) | What enters the store is decided by what the store is for, not by file type and not by source class |
| [`0055`](0055-delivery-layout-is-not-organization.md) | Delivery layout is not organization; resolution is semantic |
| [`0056`](0056-an-asked-answer-is-kept-and-loud.md) | An asked answer is kept, and its provenance is loud |
| [`0057`](0057-origin-carries-no-locator.md) | Whatever `origin`'s vocabulary becomes, it may not carry a locator |
| [`0058`](0058-generated-text-is-never-attributed-to-the-source.md) | Never present a generated description as something the source said |
| [`0086`](0086-extraction-emits-candidate-facts-never-skeleton-operations.md) | Extraction emits candidate facts and never skeleton operations, so neither extractor knows the skeleton |
| [`0087`](0087-two-writes-carry-no-material.md) | Two writes carry no material, and they belong to the coordinator |

## The container — `0059`–`0067`

Tiers, the surface's grammar, serialization, and what lives outside the system.

| | |
|---|---|
| [`0059`](0059-three-tiers-enforced-by-a-boundary-test.md) | Three tiers, no rule about what deserves to exist below the surface, and a test that can refuse |
| [`0060`](0060-one-composable-grammar-not-n-verbs.md) | One composable grammar with progressive disclosure, not N described verbs |
| [`0061`](0061-addressing-belongs-to-the-surface.md) | Addressing belongs to the surface; every read returns handles |
| [`0062`](0062-the-skeleton-is-files-plus-an-index.md) | The skeleton is files plus an index rebuilt at load, not a database |
| [`0063`](0063-typescript-because-a-compiler-can-refuse.md) | TypeScript, because two of this design's own mechanisms need a compiler that can refuse |
| [`0064`](0064-jsonl-and-construction-is-the-only-gate.md) | JSONL with a `schema_version`, and construction is the only gate |
| [`0065`](0065-the-store-is-the-channel.md) | Components share state through the store, never through a protocol |
| [`0066`](0066-the-calendar-is-an-outside-projection.md) | The calendar is a projection to an outside surface, not something this system renders |
| [`0067`](0067-markdown-is-not-the-store.md) | Markdown notes are not the store |

## Method and evidence — `0068`–`0080`

How this project derives, measures and judges its own work. These constrain what a test or a fixture may assert.

| | |
|---|---|
| [`0068`](0068-build-the-instance-generalize-afterwards.md) | Build the instance; the general contract is whatever survives generalization |
| [`0069`](0069-the-five-refactor-triggers.md) | Five named rewrites, and exactly enough committed now to defuse each |
| [`0070`](0070-derivation-top-down-construction-bottom-up.md) | Derivation runs top-down and construction runs bottom-up |
| [`0071`](0071-success-path-derivation-omits-repair.md) | A method set derived only from success paths cannot produce a repair method |
| [`0072`](0072-docstrings-are-design-not-documentation.md) | Write rules precede the build, because a verb's docstring and parameter definitions are what the agent sees directly |
| [`0073`](0073-a-write-rule-must-fit-a-docstring.md) | A write rule that cannot be said in a docstring is not finished |
| [`0074`](0074-read-back-only-through-service-methods.md) | A test that reads the store directly, or reaches the repository past the service, satisfies no criterion |
| [`0075`](0075-misfitting-row-is-a-spec-failure.md) | A real row that does not fit the field set is a spec failure, not a fixture patch |
| [`0076`](0076-ambiguous-outcome-resolves-against-the-proposition.md) | An ambiguous outcome resolves against the proposition: "it basically round-trips" is a fail |
| [`0077`](0077-derived-fixture-is-code-not-evidence.md) | A migrated fixture is a test input and therefore code; the original is never edited and stays as provenance |
| [`0078`](0078-derived-record-may-narrow-its-source.md) | A derived record may narrow or drop its source's ruling; provenance is not authority |
| [`0079`](0079-corpus-bounds-content-not-record-shape.md) | Corpus measurements bound what the material contains, never what a record should look like |
| [`0080`](0080-fixture-is-not-a-golden-set.md) | A conformance verdict over a transcription is not a fidelity claim about the material |

