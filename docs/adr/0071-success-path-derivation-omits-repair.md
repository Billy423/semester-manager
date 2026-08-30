# A method set derived only from success paths cannot produce a repair method

Two independent derivations of one method set - a closure over the field set, and eleven real interaction traces - between them produced zero corrections, deletions, re-lands or crash paths, and the method that actually broke a system invariant came from neither. Completeness over success paths is not completeness.

- Route A enumerates over fields.
- Route B's eleven traces are all success paths.
- `retarget` is in neither A nor B, and `retarget` is the method that broke *one current value per target*.

This is where the term **repair method** is defined in use: an operation that exists to correct a mistake - a retarget, a delete, a re-land - as opposed to one that advances a success path.

## Considered Options

Accepting the two-route union as a completeness argument, which is what the derivation record was written to assert. Rejected: two routes that share a blind spot agree, and their agreement is not evidence. `0070` supplies the direction each route was derived in.

Source: fall26:records/plan/application-tier.md §2.4b
