# Drafts and Rulings

What an agent's own output on this project may assert, and what it may not.

## Draft; never self-lock

**An agent drafts. It does not rule.** A finding, a proposal, an analysis or a recommendation you produce is a draft until Billy rules on it, and your output must say so in its own words rather than leaving a reader to infer standing from tone.

The failure this prevents is measured, not hypothetical: in the source corpus an unmarked agent passage was taken for a ruling, or allowed to override one, **three times in a single day**, which is why several of its sections carry a banner saying the section is agent-authored and carries no ruling marker.

**Do not reintroduce the `[R]` marker convention.** That convention belongs to the records repo it came from, and this repo carries standing differently: a decision that has been ruled is an ADR in `docs/adr/`, and a decision that has not been made is an open issue. If a claim fits in neither place, it is a draft and it stays in your report.

## Demote to the level the evidence supports

When you find that a claim's standing is weaker than its record asserts, **lower the claim to what the evidence supports rather than defending the higher standing.** The corpus did this to itself once by name: a length bound marked as ruled was demoted to owed, because no ledger anywhere supported the ruled standing.

The same move applies to your own work in progress. Report the weaker claim you can support, not the stronger one you set out to make.

## BLOCKED beats guessing

**A blocked agent that asks one sharp question is worth more than a finished one that assumed.** When the input is ambiguous, a boundary is unclear, or a record you need is missing, stop and return the question. Do not fill the gap with a plausible value and carry on.

The other half of the same permission: **you may judge the model.** A finding that overturns the design is the most valuable thing you can return, and returning it is not out of scope. Where a ruling is Billy's to make, list every real instance you found, so that the ruling is made on real instances rather than on one hypothetical.

## Every number quoted from fall26 carries a standing caveat

Any output of yours that cites a fall26 measurement inherits this:

> Most of this project's measured numbers are NOT auditable from this checkout. The evidence behind them stayed in the openclaw checkout by ruling.

State it wherever such a number is load-bearing. It is a weaker property than auditable-here, and a reader who wants to check a number has to go to that other checkout. **The caveat attaches to this migration's own plan**, which cites fall26 rather than copying it, so it reaches most of what carries a figure in this repo.

## Provenance

- Agents draft and never self-lock: `openclaw:fall26/2026-08-22-step-minus-1/p5-induction/TASK.md` §Explicit non-goals · `fall26:records/domain/model.md` §4 banner (`STANDING MARKED 2026-08-24`)
- Demoting to the level the evidence supports: `fall26:records/spec/schema.md` changelog, 2026-08-25
- BLOCKED beats guessing, and judging the model: `openclaw:fall26/2026-08-22-derivation/BRIEF.md` rules 5-6 · `openclaw:fall26/2026-08-22-step-minus-1/p5-induction/TASK.md` §Reduction targets
- The standing caveat on fall26 numbers: `fall26:evidence/README.md`
