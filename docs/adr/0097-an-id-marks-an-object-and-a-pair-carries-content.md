# An `id` marks an addressable object, an open/close pair carries content, and a member omits what its container fixes

Three rules about **when an element opens and what may sit inside it**. `0082`'s four rules place a field; none of them says whether the thing at that position is another object or a part of this one, and a reader has to know which before it can decide to spend a call.

**A tag carrying an `id` is an addressable object; a tag without one is a field of the node being rendered.**

```xml
<course id="2c03"/>                                  <- another object; look_at reaches it
<grade_share conditional="true">10</grade_share>     <- a field of this obligation
```

`0082` rule 2 only half-covers this. A `Ref` is an element, but so is `<parts>`, and `<parts>` is no object. **The `id` is the marker, not the element name**, and it doubles as the signal for which things can be passed to `look_at`.

**An open/close pair carries content.** A pointer and a projection are not content, so a line is self-closing and what it was carrying moves onto the element that owns it - which is how `0096`'s `<edge>` came to hold `type` and `direction`. An element with a text field and no sections closes itself too: a `progress` with no `detail` is `<progress id="70" state="done" …/>`, not an empty pair.

**A member omits what its container already fixes.** Inside `<obligations>` under a course, no row restates its `course`; inside `<neighbours>`, which is heterogeneous, every row keeps it. This is **not** an exception to `0082`'s *absence is written, never omitted*: that rule is about a field whose **value is null**, and this is about a field whose value is **determined by position**. An omitted-because-null attribute is invisible; an omitted-because-fixed one is recoverable from one line up.

## Where this bites

The rules are cheap individually and load-bearing together: they are what keeps a line from growing into a block. A neighbour that opened a pair to hold a pointer would be one edit away from holding a section, and `0095`'s bound - the only unbounded thing in a return is the node itself - would stop being structural.

Source: ruled at #80 (Billy, 2026-09-03).
