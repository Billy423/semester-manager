# A link's identity is its natural key, `locator` is part of it, and a link has no update

A link's identity is the natural key `(from, to, kind, role, locator)`; there is no surrogate id, because idempotent re-landing needs the natural key regardless. `locator` is in the key because omitting it silently destroys edges - one deck cites the textbook four times at four different sections, and those are four links, not one. **It follows that a link has no update: changing any component produces a different link, so every change is detach plus attach.**

```
Link     := from: Ref · to: Ref · kind: LinkKind · role?: string · locator?: string
identity := (from, to, kind, role, locator)
update   := detach + attach
```

**Nodes get opaque assigned ids and links get no surrogate id at all; the asymmetry is deliberate.**

Source: fall26:records/spec/design.md §3.3, fall26:records/spec/schema.md §5; the no-update consequence at fall26:records/plan/application-tier.md §2.1
