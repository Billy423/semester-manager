# A materialization pass must report that it recovered nothing; it does not OCR

Material with no text layer is a whole class, not an edge case. The requirement is **detection, not OCR**: `text_extractable` defaults false and is set true only when a pass actually recovered text, so an empty extraction is visible rather than silent. **Cost, stated inside:** detection catches *empty*, not *confidently wrong* - one assignment PDF returns the same header string for all six pages, and the other direction is ADR `0058`.

Source: fall26:records/domain/model.md §9
