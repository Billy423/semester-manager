# A test that reads the store directly, or reaches the repository past the service, satisfies no criterion

The rejected alternative - reading the file - is the obvious cheap check, and it is given up so that the criterion measures the thing it names. The cost is slower and more coupled tests, and it is hard to reverse once a suite exists.

Source: fall26:records/plan/application-tier.md §5 (the definition of "landed" at fall26:records/spec/architecture.md §4 rules out neither shortcut; the stricter form is this one)
