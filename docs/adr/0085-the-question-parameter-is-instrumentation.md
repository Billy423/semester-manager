# The `question` parameter is development instrumentation and is not in the production signature

`look_at(node_id, question)` carries a required second parameter, ruled by Billy on 2026-08-23 and recorded with its reason: the question is *"not to be predicted but stated at call time"*, and required **so that it is enforced at the tool surface rather than requested in a prompt**. Its purpose was to find out **why an agent was calling the verb**. **It is an instrument, and the production signature is `look_at(node_id)`.**

Two consequences.

**The return shape is not filtered by it.** `0028`'s null rule and the symmetry rule both presuppose a fixed element set per kind; a return that varies with the question is renderer-introduced asymmetry, and the parameter's own record already admits it *"perturbs what it measures"*. Welding a known perturbation into the contract is not a trade worth making.

**#12 item 5 changes shape.** That item carries the parameter's *retirement condition*, which presumes it ships and later leaves. It never ships. What survives from that item is the prohibition, and it is unaffected: **the deliberateness the parameter induces must never later be reported as a finding.** The `>=80%` threshold was already deleted there as an arbitrary agent proposal.

Source: ruled at #60 (Billy, 2026-09-01). The parameter and its stated reason are at `fall26:records/domain/model.md` §7.1 and §4.1; the caveats travel at #12 item 5.
