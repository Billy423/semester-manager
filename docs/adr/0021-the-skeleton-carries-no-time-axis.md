# The skeleton carries no time axis; time is a separate projection, not nodes and edges

The skeleton is a content and domain graph and has no time axis. The only time on a node is `due`, which belongs to obligation, not artifact. Query-by-time-period is a separate projection over the skeleton the way ring 0 is, and modelling "week N" as a node joined by edges is not the right modelling; a course's own coarse grouping - week for one course, module for another - is deliberately not modelled.

Source: fall26:records/domain/model.md §9; fall26:records/domain/domain-design.md §10.5
