# Course membership is a field, because the rule that relations are records exists to stop a polymorphic target becoming one

`obligation.course` is a `Ref` field on `obligation`, not an edge, and a property of `obligation` rather than of every node - a concept is not per-course. The rule that relations are records exists to stop a **polymorphic** target becoming a field, and this target is not polymorphic: course membership is single-valued, mandatory and monomorphic. **Whether the field is mutable is not ruled** - the code implements an application-tier recommendation (*set at create, not updatable*) that no record decides.

Source: fall26:records/spec/schema.md §3, fall26:records/spec/design.md §3.3; the unruled mutability recommendation at fall26:records/plan/application-tier.md §7.1
