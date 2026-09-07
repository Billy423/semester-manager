# A ref is not a foreign key: a ref may name something that is not there, and nothing cascades

A pointer is a `Ref := (kind, id)` drawn from the one id space; the kind tag makes a ref resolvable without a lookup, which is what lets a link be validated at write time against its signature. A ref may name something that is not there, so it is not a foreign key: **deleting a course does not cascade to its obligations and deleting an obligation does not remove notes about it.** A dangling ref is legal and is recovered by the link-set validation pass, which is **owed and unbuilt** and which reaches Ref-typed fields as well as links - an obligation whose `course` names no node is kept in ring 0 and repaired here, not dropped (`0103`).

The two cascade cases:

| delete | what survives |
|---|---|
| `course` | its obligations survive |
| `obligation` | `about` annotations survive, dangling |

Source: fall26:records/spec/design.md §3.2; the two cascade cases at fall26:records/plan/application-tier.md §2.1
