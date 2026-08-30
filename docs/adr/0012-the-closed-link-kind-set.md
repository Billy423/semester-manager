# Links are a closed typed set, each with an endpoint signature; a relation earns a row only with three real instances and a nameable query

Every relation is a `Link` with a `LinkKind` whose signature constrains its endpoints, so adding a relation is a table row plus a signature rather than a schema change. A relation earns a row only if the material shows at least three real instances and someone can name the query that reads it.

The nine-row `LinkKind` table:

| kind | signature |
|---|---|
| `about` | `annotation → any` |
| `covers` | `artifact → concept` |
| `applies` | `artifact → concept` |
| `requires` | `concept → concept` |
| `requires` | `obligation → concept` |
| `spec` | `obligation → artifact`, `role ∈ {given, owed}` |
| `prepares-for` | `artifact → obligation` |
| `builds-on` | `obligation → obligation` |
| `part-of` | `concept → concept` (a **DAG**) |

Source: fall26:records/spec/design.md §3.3; fall26:records/domain/model.md §8
