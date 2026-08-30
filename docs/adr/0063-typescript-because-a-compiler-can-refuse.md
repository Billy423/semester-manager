# TypeScript, because two of this design's own mechanisms need a compiler that can refuse

TypeScript, settled by what this design already claims about itself: the purity cut is defused *by type, not by restraint*, and construction is the only enforcement point there is - **both are claims about a compiler that can refuse.** Python cannot refuse, because any module may import any other and adding a kind raises no error at the sites that must change, so the dispatch-on-type commitment would be hoped for rather than checked. **The embedding ecosystem stays Python and does not cross a tier boundary**: the store couples to the skeleton through one field.

**The requirement, in the form a future re-opening needs:** algebraic data types, plus exhaustiveness checking, plus enforceable module boundaries. *"OOP native"* was the wrong label for it and was corrected in the sitting - this design spends a whole section rejecting inheritance. Arguing from *a compiler that can refuse* reconstructs the requirement in prose each time; the three-part form does not need reconstructing.

## Consequences

Runtime type erasure is a wash and is not a reason to prefer either language. Rust fits the data shapes best and was not chosen, on iteration speed for a solo build.

Source: fall26:records/spec/architecture.md §6 (Billy, 2026-08-27) · fall26:evidence/2026-08-27-tier-recut/NOTES.md correction 3 for the three-part form
