# What enters the store is decided by what the store is for, not by file type and not by source class

An artifact's content enters the store if and only if it yields semantic, decontextualized facts about course materials that improve the knowledge base's overall quality - a handwritten note qualifies on that test. No source class is admitted or excluded as a class, and no property of the file - its type, or whether its meaning survives linearization - decides the question. The earlier file-level axis was falsified four ways inside one slice: scanned handwriting in a PDF wrapper, a text PDF whose exercises are images, an image file more chunkable than several PDFs, and one diagram held in two formats. **`text_extractable` survives as a materialization outcome, not as an inclusion criterion.**

```
backing         ∈ {materialized_doc, code_project}   -- a node property
text_extractable : bool, per region, default false   -- true only when a pass actually recovered text
```

Source: fall26:records/domain/model.md §9 (the four falsifications); fall26:records/domain/domain-design.md §1 ruling 9 and §10.7 ruling 3 (the superseded source-class rule); the determinant restated by Billy's ruling 6, 2026-08-30
