# Research Method

How a measurement, an experiment or a blind derivation on this project is designed, run and scored. These are rules about the project's own research; nothing here says anything about what the semester manager must do.

## Pre-register before the run

Write the pre-registration down before the run starts, and do not touch it afterwards. It must fix:

- **The sampling rule, written before any file's content is opened.** Choosing what to look at after seeing it is the failure this rule exists to prevent.
- **The verdict thresholds.** State them before the run and never adjust them after. A result obtained without pre-registration cannot be retrofitted with one - if you find yourself wanting to set a threshold now, the run is exploratory and must be reported as exploratory.
- **Which hypotheses are judgment calls** rather than adjudicated by data or arithmetic. Say it up front rather than discovering it afterwards. A run judged only by Billy and the agent has no external adjudicator, so everything it produces is an assertion until a later test touches it.
- **What you expect to be wrong about.** The origin sessions rated that expectation as worth more than the individual findings.

**Ambiguous judgements resolve against the proposition being tested**, never for it. This is the anti-cheat rule: it is what stops a run from converging on the answer that was wanted.

## Score a pre-registered exercise on unpredicted yield

A blind exercise is scored on what it found that was **not** predicted. A predicted item that is found is a known hole, not evidence the method works. Scoring recall against the prediction list measures the predictor rather than the instrument, which is the rejected alternative and the obvious one.

A pre-registration that is never scored produces no verdict. The 2026-08-27 tier-recut prediction was never scored, because the adjudication file it names was never written - the exercise ran, and its output is still an unscored assertion.

## Brief a blind agent by withholding the analysis, not the material

**A blind agent is withheld the prior session's analysis and conclusions. It is not withheld the material.** The independence worth having is independence from a session's framing, not independence from the facts.

The rejected alternative - withholding the material - was tried and failed: a cold session cannot derive birth rules at all, and this is why the abstract write-rules mandate stalled for two months and was never executed as written. A session handed the prior session's findings inherits its conclusions; a session handed nothing derives nothing.

The working form of this: four subagents blind to each other and blind to the two records that stated the current position, all reading the same material.

## Blind-run hygiene: copies, never symlinks

**A blind run receives a copy of every input file, never a symlink, with document metadata stripped.**

This is an earned correction, not a preference. The 2026-08-22 seal was built from symlinks, and `ls -la` prints symlink targets - so the first command a shell-using agent naturally runs defeated it. Two agents hit the leak and both self-reported. One had seen the ground truth verbatim, so its induced partition is contaminated and only its structural findings stand. For the other, no re-run was ordered, because the grouping it was asked to induce had three carriers and only one was sealed: the folder name was sealed, but the PDF `Title` metadata and the rendered title slide carried the same grouping, and one of those carriers is the content itself. **A property carried by the content was never withholdable, and sealing the filename does not make it so** - check the carriers before you claim a run was blind.

**A named carrier, found the same way and in the same class: the run's own tool source.** `tools.py` was readable in every run directory of the 2026-08-23 read-cycle material, so a run could learn what a verb would return without calling it - an apparatus leak present since the first run, and one a deployed assistant would not have. The harness itself read `tools.py` before calling anything, so it saw the clock, the log call and a truncation constant. **A run directory is part of the run's context: what is on disk beside the agent is a carrier, not scaffolding.**

Two further constraints on any blind extraction run:

- **No re-picking. A bad extraction is a finding**, and it is reported as one. Swapping in a better input after seeing the result destroys the run.
- **2c03 is no longer a blind fixture.** Its extracted records were edited by hand to produce the write rules, so an extraction run against it measures nothing.

## Keep the raw artifacts

**Preserve what cannot be reconstructed; record the recipe for what can.** A full-text extraction is not preserved when the exact command that regenerates it from unchanged sources is written down. A scoring key is preserved, because without it, which document an agent saw under which neutral name is unrecoverable.

The reason to keep anything at all: **a conclusion whose evidence was deleted is not auditable.**

## No design vocabulary in a raw pass

An agent doing a raw pass over material is given no design vocabulary - not the node kinds, not the link kinds, not the schema's field names. **Having the word "concept node" available is enough to start hallucinating them.** If a raw pass returns the project's own terms, suspect the brief before you believe the finding.

## Repair a defective measurement rather than bannering it

When a measured number is wrong, **fix the defect, re-run the affected configurations, and delete or exclude the originals. Do not leave the wrong number in place with a banner beside it.** A wrong number left in place gets cited; a banner is not read by the reader who arrives via a quotation.

Both halves of this were applied: nine configurations were re-run after a crashing tool was fixed, with the defective originals kept out of citation, and a wrong column in an omission matcher was deleted rather than annotated.

## Derive a rule from worked instances, not in the abstract

**Writing rules in the abstract stalled this project for two months.** The write rules that exist came from Billy editing one course's extracted records by hand: **the rule is what he did, and the before-and-after is the evidence.**

So: when a rule is owed, produce it by doing the work on real instances and reading back what you did. State each rule in the direction it came from - what has to be true for the thing to come out right - and never from what some source document happens to say.

## Provenance

- Pre-registration and anti-cheat: `openclaw:fall26/2026-08-22-step-minus-1/TASK.md` §Anti-cheat rules · `openclaw:fall26/README.md` §"Rules of the road" · `openclaw:fall26/2026-08-22-derivation/TASK.md` §preamble · `openclaw:fall26/2026-08-22-modeling/PLAN.md` §"This cycle's own failure mode"
- Scoring on unpredicted yield: `fall26:evidence/2026-08-27-tier-recut/PREREGISTRATION.md` §"The rule for reading this afterwards"
- Blind briefing: `fall26:evidence/2026-08-27-tier-recut/derivations/README.md` · Billy, 2026-08-26, in-sitting
- The seal and its leak: `openclaw:fall26/2026-08-22-derivation/FINDINGS.md` §0 · `openclaw:fall26/2026-08-22-derivation/apparatus/README.md` §"The seal leaked" · `openclaw:fall26/2026-08-22-derivation/BRIEF.md` §THE SEAL
- No re-picking, copies not symlinks (found independently): `fall26:records/archive/slice-1-plan-2026-08-27.md` §7
- Preservation: `openclaw:fall26/2026-08-22-derivation/apparatus/README.md` §"What is deliberately NOT here"
- No design vocabulary in a raw pass: `openclaw:fall26/2026-08-22-derivation/BRIEF.md` rule 1 · `openclaw:fall26/2026-08-22-derivation/TASK.md` §2 rule 2
- Repair over bannering: `fall26:records/findings/read-cycle.md` §0 items 1 and 3, `[R]` Billy 2026-08-23
- Rules from worked instances: `fall26:records/spec/write-rules.md` header, 2026-08-28; the stalled abstract mandate is frozen at `fall26:records/plan/write-rules.md`
