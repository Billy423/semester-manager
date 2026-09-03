# The render uses the schema's own spelling for every name the coordinator can name back

The render carries two casings - `done_by`, `sticky_note`, `not_started` in snake; `builds-on`, `course-outline`, `points-at` in kebab. **The split is not internal-versus-outward.** It is whether the coordinator can **name the thing back**.

```
written back  -> the schema's own spelling, unchanged
                 kind discriminators   land()
                 field names           set
                 link types            attach
                 enum values           both
invented here -> free
                 <neighbours> · <edge> · <annotations> · points-at / pointed-by
```

**The ground is that a respelled name is one the surface then refuses.** `0088` puts `set`, `attach` and `detach` at the surface over fields and links, and `0090` makes `land()` carry candidate facts. Every one of those calls names a field, a kind or a link type. A render that hands the coordinator `done-by` and a surface that accepts only `done_by` has manufactured a translation step that nothing performs.

**This is the rule that lets `<edge>` stand while `<sticky_note>` keeps its underscore.** The alternative reading - *an id-carrying tag takes the schema spelling* - is falsified by `<edge>` itself, which carries an id while the schema calls the record `Link` (`0096`). `sticky_note` keeps its spelling because it is a **kind discriminator** that goes into a `land()`, not because it carries an id.

**`0093` criterion 2 is unaffected.** It bars naming a **verb or a surface element** after the internal structure - `<links>` fails it, `<neighbours>` passes. It does not reach the spelling of a value the coordinator must reproduce, because there the internal name **is** the interface.

## What is inherited rather than created here

The schema's own split is inconsistent: `progress.state` is `not_started` while `0012`'s link kinds are `builds-on`, and **both are written back**. The render mirrors that rather than normalising it. Normalising belongs to the schema rename, which is cheap only because the schema has not entered this repository - `fall26:records/spec/schema.md` is provenance and `fall26/app` is unported, so there is no data to migrate and no reference to chase.

Source: ruled at #80 (Billy, 2026-09-03), after a pass that kebab-cased every multi-word name in the render and was falsified by `<sticky_note>`.
