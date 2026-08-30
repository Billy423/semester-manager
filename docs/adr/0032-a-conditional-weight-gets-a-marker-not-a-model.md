# A conditional grade weight gets a marker, not a model, and the pointer to the rule is optional

`grade_share_conditional` is true when the stored share is one reading of a rule the course states conditionally or as a bound - *"10/10/30 or 0/0/50, whichever works out better for you"*, and equally *"worth at least 30%"*, since a bound is the same defect as a conditional. The general form - a `weighting_scheme` naming the alternatives with a derived weight - was rejected as over-built for one concrete calculation, and the *required* pointer to the rule was later made optional because a schema rule manufacturing a conflict nobody would care about is a defect in the rule. **The narrowing must not be smoothed: the pointer was half of what made the marker actionable.**

Source: fall26:records/domain/model.md §10.9 (Billy, 2026-08-23); the narrowing at fall26:records/spec/schema.md §3 and changelog 2026-08-27
