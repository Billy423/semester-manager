# Five named rewrites, and exactly enough committed now to defuse each

The question was answered by naming what would *force* a rewrite when the graph layers land, and committing to exactly enough to defuse each; everything else stays unbuilt. The rejected alternative was to defer all five and refactor later, and it loses because a forced rewrite costs more than five minimal commitments. **Four of the five are argued at length elsewhere and this is where they are named together; the fifth is argued nowhere else.**

| trigger | the minimal commitment that defuses it | argued at |
|---|---|---|
| A - identity | one id space for anything that can be a link endpoint | `0025` |
| B - dispatch on type | `kind` is data with a typed payload, never control flow | `0027` |
| C - linkage | relations are records, not fields | `0016` |
| D - the store boundary | the purity cut is a property of the interface's shape, not of restraint | `0020` |
| **E - persistence coupling** | **a repository interface with one implementation** | **nowhere else** |

Trigger E is claimed by no other record and argued in no other record. Without this ADR it is lost.

Source: fall26:records/spec/design.md §2
