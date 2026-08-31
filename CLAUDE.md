# semester-manager - how to work in this repo

## Agent skills

### Issue tracker

Issues and specs live as GitHub issues, driven through the `gh` CLI. `docs/agents/issue-tracker.md` is the contract: it carries the exact invocations, and the wayfinding operations (map, child, blocking, frontier, claim, resolve). Read it rather than guessing.

What is in the tracker, by label:

- **`wayfinder:grilling`** — decisions that are Billy's. Rule one by commenting the ruling and closing the issue; the comment is the record and its timestamp is the date.
- **`deferred`** — decisions deliberately not made, each carrying the precondition that wakes it. **These are not tasks.** Nobody picks one up; you check whether its wake condition has been met. Eleven gates fire most of them, and a gate fires several at once.

**Updates go in comments, not in body edits.** The body is the current statement; the comments are its history.

### Triage labels

The five canonical triage roles, used verbatim as GitHub label strings. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context: `CONTEXT.md` and `docs/adr/` at the repo root. See `docs/agents/domain.md`.

`docs/adr/README.md` is the index and the reading path; the records themselves are reference. A `Source:` line in a record is an audit trail, not a reading instruction.

## Working discipline

Inherited from the two-week design effort this repo succeeds, and kept because each rule was earned by a specific failure.

### Running a measurement or a blind exercise

Pre-registration, anti-cheat, scoring, and the hygiene rules a leaked seal taught. See `docs/agents/research-method.md`.

### Reading an inherited record

What a record is authority for, and where its changelog stops covering it. See `docs/agents/reading-records.md`.

### Writing your own output

Drafts never self-lock, `[R]` is not yours to apply, and BLOCKED beats guessing. See `docs/agents/drafts-and-rulings.md`.

## Where the corpus went

The design corpus of the predecessor effort lives at `~/Documents/Projects/fall26` and is **provenance only**. Everything decided there that still stands has been landed here: terms in `CONTEXT.md`, decisions in `docs/adr/`, deliberately-deferred decisions as issues. A `fall26:` path in an ADR is an audit trail, not a reading instruction — if you need to open it to act, that is a defect in the ADR, not a step in the work.

The migration's own working files are in `research/`. They are **scaffolding: written once, never maintained.** Anyone updating them is building a second corpus.
