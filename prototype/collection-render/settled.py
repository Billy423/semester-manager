"""The render as it stands after #80's rulings. THROWAWAY prototype.

WHAT IS RULED HERE, and by what:

  SELECTION - which fields enter the render at all.
    THIS IS THE FOURTH HOLE. 0082's four rules PLACE a field; they do not SELECT
    one, and #60 waved selection through with "every other field". Two rulings
    exist and they go opposite ways:
      created_at / updated_at  IN   - 0046 puts an annotation's whole body in the
        block, and schema.md 4.5: "Without `updated_at` a January answer is
        indistinguishable from today's, and that silent influence is the actual
        harm". Removing them voids the field's entire purpose.
      added_at                 OUT  - it describes THE ROW, not the thing, and
        look_at's purpose is to say what the NODE is. Its own ruling calls it
        kept deliberately with no mechanism reading it. This is an exclusion and
        the burden was on the excluder.

  PLACEMENT - 0082's four rules, unchanged.

  SECTIONS - cut by source: 0045 (IS, not SAYS), 0046 (own channel), 0084 (a
    composed batch is reached by no edge, so it is a fourth source).

  NAMING - the element name IS the kind (0082's first clause), so a neighbour is
    <obligation .../> and the attribute `kind` never appears. <links> becomes
    <neighbours> and <link> becomes <edge>, because CONTEXT.md's `link` is the
    internal record's name. Direction says what it means: points-at / pointed-by.
    A Ref-typed field carries `id`, not `ref`, which 0093 already rejected once.
    Spelling: snake case marks an internal name, so nothing in an outward render
    carries it.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import corpus

RENDERED = {
    "course": ["name", "term"],
    "obligation": ["course", "name", "due", "done-by", "grade-share", "parts", "optional"],
    "sticky_note": ["category", "origin", "created-at", "updated-at", "body"],
    "progress": ["state", "origin", "created-at", "updated-at", "detail"],
}
FORM = {"course": "ref", "parts": "repeat", "grade-share": "qualified",
        "body": "freetext", "detail": "freetext"}
LINE = {"obligation": ["course", "name", "due", "state"], "course": ["name", "term"]}
COMPOSES = {"course": ["obligations"]}


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")


def at(k, v):
    v = "" if v is None else (str(v).lower() if isinstance(v, bool) else str(v))
    return f'{k}="{esc(v)}"'


def wrap(s, n=74):
    words, cur, out = str(s).split(), "", []
    for w in words:
        cur, out = (w, out + [cur]) if len(cur) + len(w) + 1 > n else (f"{cur} {w}".strip(), out)
    return out + ([cur] if cur else [])


class Store:
    def __init__(self):
        self.courses, self.obs, self.notes, self.prog, self.links = corpus.load_all()
        self.by_id = {x["id"]: x for x in self.courses + self.obs + self.notes + self.prog}
        for o in self.obs:
            o["state"] = next((p["state"] for p in self.prog if p["about"] == o["id"]),
                              "not_started")
        # MADE UP, same licence as the progress records: the fixture carries no
        # timestamps, and without them the field whose whole purpose is read-time
        # dating cannot be seen. updated-at differs from created-at on one note.
        for i, n in enumerate(self.notes):
            n["created-at"] = f"2026-01-{12 + (i % 17):02d}T09:{10 + i:02d}"
            n["updated-at"] = n["created-at"]
        self.notes[3]["updated-at"] = "2026-02-02T16:40"
        for i, p in enumerate(self.prog):
            p["created-at"] = f"2026-01-{14 + (i % 15):02d}T20:{5 + i:02d}"
            p["updated-at"] = f"2026-02-{1 + (i % 8):02d}T21:{5 + i:02d}"
        for ann in self.notes + self.prog:
            ann["kind"] = "sticky_note" if "body" in ann else "progress"
            self.links.append({"id": "e" + ann["id"], "role": "about",
                               "from": ann["id"], "to": ann["about"]})
        for o in self.obs:
            o["done-by"], o["grade-share"] = o["done_by"], o["grade_share"]
            o["grade-share_conditional"] = o["grade_share_conditional"]
            o["kind"] = "obligation"
        for c in self.courses:
            c["kind"] = "course"

    def annotations(self, nid, ind):
        rows = [a for a in self.prog + self.notes if a["about"] == nid]
        if not rows:
            return [f"{ind}<annotations/>"]
        out = [f"{ind}<annotations>"]
        for a in sorted(rows, key=lambda a: a["created-at"]):
            out += block(a["kind"], a, self, ind + "  ", sections=False)
        return out + [f"{ind}</annotations>"]

    def neighbours(self, nid, ind):
        edges = []
        for l in self.links:
            if l["from"] == nid:
                other, d = l["to"], "points-at"
            elif l["to"] == nid:
                other, d = l["from"], "pointed-by"
            else:
                continue
            if l["role"] == "about" and d == "pointed-by":
                continue          # 0046: it arrived through <annotations> already
            edges.append((l, self.by_id[other], d))
        if not edges:
            return [f"{ind}<neighbours/>"]
        out = [f"{ind}<neighbours>"]
        for l, n, d in sorted(edges, key=lambda x: (x[0]["role"], x[1]["id"])):
            out.append(f'{ind}  <edge {at("id", l["id"])} {at("type", l["role"])} '
                       f'{at("direction", d)}>')
            out += line(n["kind"], n, ind + "    ")
            out.append(f"{ind}  </edge>")
        return out + [f"{ind}</neighbours>"]

    def composed(self, nid, section, ind):
        rows = sorted([o for o in self.obs if o["course"] == nid],
                      key=lambda o: (o["due"] is None, o["due"] or "", o["id"]))
        if not rows:
            return [f"{ind}<{section}/>"]
        out = [f"{ind}<{section}>"]
        for o in rows:
            out += line("obligation", o, ind + "  ", fixed=("course",))
        return out + [f"{ind}</{section}>"]


def block(kind, rec, store, ind="", sections=True):
    """A node's own render. An open/close pair carries content; a pointer does not."""
    head, kids, text = [f"{ind}<{kind}", at("id", rec["id"])], [], None
    for f in RENDERED[kind]:
        form, v = FORM.get(f), rec.get(f)
        if form == "ref":
            kids.append(f'{ind}  <{f} {at("id", v)}/>')
        elif form == "repeat":
            kids += ([f"{ind}  <{f}/>"] if not v else
                     [f"{ind}  <{f}>"] + [f"{ind}    <{f[:-1]}>{esc(x)}</{f[:-1]}>" for x in v]
                     + [f"{ind}  </{f}>"])
        elif form == "qualified":
            kids.append(f'{ind}  <{f} {at("conditional", bool(rec.get(f + "_conditional")))}>'
                        f"{esc(v)}</{f}>")
        elif form == "freetext":
            text = v
        else:
            head.append(at(f, v))
    body = list(kids)
    if sections:
        body += store.annotations(rec["id"], ind + "  ")
        body += store.neighbours(rec["id"], ind + "  ")
        for s in COMPOSES.get(kind, []):
            body += store.composed(rec["id"], s, ind + "  ")
    open_tag = " ".join(head)
    lines = ([f"{ind}  {l}" for l in wrap(text)] if text else []) + body
    if not lines:
        return [f"{open_tag}/>"]      # an open/close pair must carry content
    return [f"{open_tag}>"] + lines + [f"{ind}</{kind}>"]


def line(kind, rec, ind="", fixed=()):
    """The element name IS the kind, so `kind` never appears as an attribute."""
    parts = [f"{ind}<{kind}", at("id", rec["id"])]
    for f in LINE[kind]:
        if f not in fixed:
            parts.append(at(f, rec.get(f)))
    return [" ".join(parts) + "/>"]


if __name__ == "__main__":
    S = Store()
    W = 100
    print(__doc__)
    for kind, rec in [("course", next(c for c in S.courses if c["id"] == "2c03")),
                      ("obligation", next(o for o in S.obs if o["name"] == "Midterm 1"
                                          and o["course"] == "2c03")),
                      ("sticky_note", next(n for n in S.notes if "LRW B1007" in n["body"]))]:
        out = "\n".join(block(kind, rec, S))
        print(f"\n{'-' * W}\n{kind}   {len(out)} chars\n{'-' * W}\n{out}")
