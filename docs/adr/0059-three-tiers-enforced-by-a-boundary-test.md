# Three tiers, no rule about what deserves to exist below the surface, and a test that can refuse

The system is split presentation / application / persistence. The field set says what a *legal value* is; how to produce one, and whether a row should exist at all, live at the surface - which is why the agent never auto-adds. The boundary is directories plus a test that has been shown to fail, because an npm manifest cannot refuse: workspace dependencies hoist, so a manifest cannot refuse an import it does not declare.

| tier | holds |
|---|---|
| presentation | the surface, the rendering including every one-line summary, and **every rule about what an agent should do** |
| application | the field set, the kinds and links, construction-time validation, id minting, CRUD services at field grain per kind |
| persistence | the serialized files and the adjacency index, fetch-by-key and one-hop traversal |

**The design-order rule this carries:** a tier is designed against the tier below it, and that tier must already exist. This is a rule about order, not an order.

**The four consequences, with the 2026-08-28 correction.**

1. ~~*A write rule never refers to the source.*~~ **Withdrawn** - three of five written rules do refer to a source, and the real distinction is the direction a rule is derived from. What survives is that the field set says what a legal value is and how to produce one lives in the tool description or the bundled skill.
2. The agent never auto-adds anything unless it is clear the user wants it. What gets a row is what the user wants tracked, and the user triggers it; the application tier holds no rule about what deserves to exist.
3. The system must not chase the agent - it exists to help, not to raise questions, conflicts or concerns nobody will care about in daily use.
4. The agent works by listing, then acting on what it saw: identifiers need not be human-facing, and matching two records is an interaction at the presentation tier, not an algorithm in the application tier.

**The boundary test's limits, stated in place:** it resolves relative specifiers only, and it scans `src/`, not `tests/`. Both are fine while there is one package and no path aliases, and both stop being fine the moment either changes.

**The adjudication rule, which no source record states:** when the application tier and the presentation tier disagree about a value or a rule, **the application tier is right and the divergence is a defect in the presentation tier.**

Source: fall26:records/spec/architecture.md conditions, §1, §2, §3 (Billy, 2026-08-27), §6 reversed 2026-08-28 · fall26:evidence/2026-08-26-interface-contract/NOTES.md §Cycle 1 Rulings (Billy, 2026-08-26) for the adjudication rule
