# The agent-facing operation set is defined once, not once per kind

Adding a kind adds a **render**, never a verb. `0082` already makes `look_at` *"abstract over every kind"*, deriving what it returns from that kind's field table; a `land` batch may carry several kinds at once; and `set`, `attach` and `detach` range over **fields and links**, which are axes that cut across kinds rather than along them. The deciding fact is that **no kind today has an operation another kind lacks** - every one of the six has fields, links and a render, and nothing else.

**This is not obvious, because the tier below is shaped the other way.** `0059` gives the application tier *"CRUD services at field grain **per kind**"*, so mirroring it at the surface is the natural move and it is wrong: `0059` also holds that *"the application tier holds no rule about what deserves to exist"*, which puts those rules at the surface, and a surface that is a mirror of the tier below has nowhere to put them.

**What `0060` actually forbids, sharpened.** It is neither a verb count nor a noun-prefixed spelling. A regular `<noun> <verb>` grammar in which the verbs repeat across nouns - `docker container start/stop/ls/rm` - is routed by *what you want to do*, not by reading each subcommand's description, and it passes. What fails `0060` is an operation set that **grows when a kind is added**, because then each kind's verbs are learned separately, which is the *"forty subcommands each needing `--help` to know when it applies"* shape.

**So a noun prefix is transport, and this record does not decide it.** `0060`: *"The grammar is the early and expensive decision; transport is late and cheap."* A CLI may spell a call `obligation set <id> …` over a kind-agnostic operation set, and doing so buys one refusal point - the server can refuse a kind that does not match the id, which is `0063`'s posture. The reverse does not hold: designing the operation set per kind to get that spelling is an expensive decision made on cheap grounds.

## The residual, which this record bounds rather than removes

`0060`'s ground is a measurement - *rewording one docstring moved a verb's call count from 1 to 9 with data availability held constant* - and that was a **rewording**, not an overlap and not a kind being added. Neither this record nor `0093`'s criterion 3 reaches it: a fixed set of non-overlapping verbs still routes by description, so **the exposure is smaller, not gone.** The default is to proceed and measure it, and it cannot be measured before #58's second standing constraint allows an evaluation involving an agent at all.

## Considered Options

**One tool whose argument is a command string.** `0060` names this shape and grants it the same composability. Rejected on **where refusal lives**: `0085` records that the `question` parameter was required *"so that it is enforced at the tool surface rather than requested in a prompt"*, and `0063`'s ground for the whole language choice is that a compiler can refuse. A command string moves every refusal into a parser, which refuses later and less.

**An operation set defined per kind.** Rejected above.

## Consequences

A noun axis earns its place the first time a kind acquires an operation another kind lacks - materializing an `artifact` is the visible candidate. `0068` says to build the instance and generalize afterwards, so it is added then and not reserved now.

Source: ruled at #62 (Billy, 2026-09-02).
