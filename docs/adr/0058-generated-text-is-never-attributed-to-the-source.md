# Never present a generated description as something the source said

A model will import a correct definition that appears nowhere in the source: one arm produced a textbook-accurate definition absent from the page image it was given, and because it is correct, correctness checking cannot catch it and nothing downstream can tell the difference. Generated enrichment is useful and the price of keeping it is that it may never be presented as quotation. This binds v1's screenshot intake, not only the deferred offline materialization of the page-image corpus.

Evidence, measured over the four providers and forty arms available 2026-08-23 - the source partitions its own findings into a perishable half (prices, model names) and a durable half (failure modes), and only the durable half is carried here:

- 39 of 40 arms returned parseable JSON and **none invented a section**. The failure is the other kind: a true sentence the source never wrote.
- **Zero-hallucination is a vendor property, not a tier property.** The tier-matched premium arm scored worst of four; one arm was the only one that stated nothing false.

## Consequences

`0022` is the same hazard from the opposite direction: it catches an extraction that recovered *nothing*, this one catches an extraction that is confidently right but not in the source. Neither absorbs the other.

Source: fall26:records/findings/ingestion-probe.md §"What it gets wrong"
