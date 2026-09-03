"""#80 variants: how does a render structure a collection of nodes?

THROWAWAY. Renders the same corpus under variants that differ along one axis:
WHAT CARRIES THE GROUPING - a named container, an attribute on each member,
plain ordering, or sections of different depth.
"""

import sys
sys.path.insert(0, sys.path[0] or ".")
import corpus
from corpus import AS_OF, BACK_DAYS, FWD_DAYS
from datetime import date

W = 100


def d(s):
    return date(int(s[0:4]), int(s[5:7]), int(s[8:10]))


ASOF = d(AS_OF)


def near(v):
    """0042's window, exactly: [today-7d, today+14d]."""
    if v is None:
        return False
    return -BACK_DAYS <= (d(v) - ASOF).days <= FWD_DAYS


def band(o, state):
    """0042's three independent triggers. Band A is active, band B is known."""
    if state == "in_progress":
        return "A"
    if near(o["due"]) or near(o["done_by"]):
        return "A"
    return "B"


LINKS = []


def has_more(o, notes):
    """0092: the set of link kinds present on the node, drawn from 0012's table."""
    kinds = {"about" for n in notes if n["about"] == o["id"]}
    kinds |= {l["role"] for l in LINKS if l["from"] == o["id"] or l["to"] == o["id"]}
    return " ".join(sorted(kinds))


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace('"', "&quot;")


def a(name, value):
    """Absence is written, never omitted (0082). Booleans render lowercase."""
    if value is None:
        v = ""
    elif isinstance(value, bool):
        v = str(value).lower()
    else:
        v = str(value)
    return f'{name}="{esc(v)}"'


class Corpus:
    def __init__(self):
        self.courses, self.obs, self.notes, self.prog, self.links = corpus.load_all()
        global LINKS
        LINKS = self.links
        self.state = {}
        for p in self.prog:
            self.state[p["about"]] = p["state"]
        for o in self.obs:
            o["_state"] = self.state.get(o["id"], "not_started")
            o["_band"] = band(o, o["_state"])
            o["_more"] = has_more(o, self.notes)

    def sorted_obs(self, rows):
        # 0082: the material's key, tiebroken by the handle, never array order.
        # A null due has no key. Ordering it is not ruled anywhere; nulls last here.
        return sorted(rows, key=lambda o: (o["due"] is None, o["due"] or "", o["id"]))

    def of(self, cid):
        return [o for o in self.obs if o["course"] == cid]

    def notes_on(self, nid):
        return [n for n in self.notes if n["about"] == nid]

    def prog_on(self, nid):
        return [p for p in self.prog if p["about"] == nid]

    def links_on(self, nid):
        """0017: a link is a record with a role. Direction is the record's."""
        out = []
        for l in self.links:
            if l["from"] == nid:
                out.append((l["role"], l["to"], "out"))
            elif l["to"] == nid:
                out.append((l["role"], l["from"], "in"))
        return out


C = Corpus()


# ---------------------------------------------------------------- glance forms

def glance_a(o, indent, extra=""):
    """Band A: 0038's seven routing fields."""
    return (f'{indent}<glance kind="obligation" {a("id", o["id"])} {a("course", o["course"])} '
            f'{a("name", o["name"])} {a("due", o["due"])} {a("state", o["_state"])} '
            f'{a("optional", o["optional"])} {a("done_by", o["done_by"])} '
            f'{a("has-more", o["_more"])}{extra}/>')


def glance_b(o, indent, extra=""):
    """Band B: course, name, due, state."""
    return (f'{indent}<glance kind="obligation" {a("id", o["id"])} {a("course", o["course"])} '
            f'{a("name", o["name"])} {a("due", o["due"])} {a("state", o["_state"])}{extra}/>')


def glance_for(o, indent, extra=""):
    return (glance_a if o["_band"] == "A" else glance_b)(o, indent, extra)


# --------------------------------------------- 0082-conformant glance forms
# Two of the seven band A fields are NOT atomic scalars, so rule 1 and rule 2 send
# them to elements, not attributes:
#   obligation.course  is a Ref   (kinds.ts) -> rule 2
#   has-more           is a SET   (0092)     -> rule 1
# A glance carrying either cannot be self-closing, which CONTEXT.md's `the line`
# says it is. That conflict is #80's to resolve; both forms render below.

def _more_children(o, indent, form):
    """Two candidate shapes for a set-valued has-more."""
    kinds = o["_more"].split() if o["_more"] else []
    if form == "repeat":
        if not kinds:
            return [f"{indent}<has-more/>"]
        return [f'{indent}<has-more kind="{k}"/>' for k in kinds]
    if not kinds:
        return [f"{indent}<has-more/>"]
    return ([f"{indent}<has-more>"]
            + [f"{indent}  <link-kind>{k}</link-kind>" for k in kinds]
            + [f"{indent}</has-more>"])


def glance_struct(o, indent, form="repeat", extra=""):
    """0082 applied to the band's field set, rather than flattened into attributes."""
    head = (f'{indent}<glance kind="obligation" {a("id", o["id"])} {a("name", o["name"])} '
            f'{a("due", o["due"])} {a("state", o["_state"])}')
    if o["_band"] == "A":
        head += f' {a("optional", o["optional"])} {a("done_by", o["done_by"])}'
    head += f'{extra}>'
    out = [head, f'{indent}  <course ref="{o["course"]}"/>']
    if o["_band"] == "A":
        out += _more_children(o, indent + "  ", form)
    out.append(f"{indent}</glance>")
    return out


def A6_structured_named_container():
    """A1's shape, with 0082 obeyed inside each member."""
    out = ["<ring-0>"]
    for b, tag in (("A", "band-a"), ("B", "band-b")):
        out.append(f"  <{tag}>")
        for o in C.sorted_obs([x for x in C.obs if x["_band"] == b]):
            out += glance_struct(o, "    ")
        out.append(f"  </{tag}>")
    out.append("</ring-0>")
    return out


def A7_structured_depth_is_the_band():
    """A3/A4's shape, with 0082 obeyed inside each member."""
    out = ["<ring-0>"]
    for b in ("A", "B"):
        for o in C.sorted_obs([x for x in C.obs if x["_band"] == b]):
            out += glance_struct(o, "  ")
    out.append("</ring-0>")
    return out


def A8_structured_nested_has_more():
    """A6, with has-more as one element carrying repeated <link-kind> children."""
    out = ["<ring-0>"]
    for b, tag in (("A", "band-a"), ("B", "band-b")):
        out.append(f"  <{tag}>")
        for o in C.sorted_obs([x for x in C.obs if x["_band"] == b]):
            out += glance_struct(o, "    ", form="nest")
        out.append(f"  </{tag}>")
    out.append("</ring-0>")
    return out


def B4_structured(cid="2c03"):
    """The composed obligation list, members at 0082-conformant glance depth."""
    out = [_course_open(cid)]
    for o in C.sorted_obs(C.of(cid)):
        out += glance_struct(o, "  ")
    out.append("</course>")
    return out


# ------------------------------------------------------------- A: ring 0

def A0_incumbent():
    """PR #69's container habit extended to a collection: wrap, then flag."""
    out = ["<ring-0>", "  <obligations>"]
    for o in C.sorted_obs(C.obs):
        out.append(glance_for(o, "    ", f' band="{o["_band"]}"'))
    out += ["  </obligations>", "</ring-0>"]
    return out


def A1_named_container_per_band():
    out = ["<ring-0>"]
    for b, tag in (("A", "band-a"), ("B", "band-b")):
        out.append(f"  <{tag}>")
        for o in C.sorted_obs([o for o in C.obs if o["_band"] == b]):
            out.append(glance_for(o, "    "))
        out.append(f"  </{tag}>")
    out.append("</ring-0>")
    return out


def A2_attribute_flat():
    out = ["<ring-0>"]
    for o in C.sorted_obs(C.obs):
        out.append(glance_for(o, "  ", f' band="{o["_band"]}"'))
    out.append("</ring-0>")
    return out


def A3_pure_ordering():
    """No marker at all: band A first, band B after, boundary implicit."""
    out = ["<ring-0>"]
    for b in ("A", "B"):
        for o in C.sorted_obs([o for o in C.obs if o["_band"] == b]):
            out.append(glance_for(o, "  "))
    out.append("</ring-0>")
    return out


def A4_depth_is_the_band():
    """0038's field sets already differ. The depth IS the partition; no flag needed."""
    out = ["<ring-0>"]
    for o in C.sorted_obs([o for o in C.obs if o["_band"] == "A"]):
        out.append(glance_a(o, "  "))
    for o in C.sorted_obs([o for o in C.obs if o["_band"] == "B"]):
        out.append(glance_b(o, "  "))
    out.append("</ring-0>")
    return out


def A5_grouped_by_course():
    """The shape CONTEXT.md's `reload` argues against. Rendered so it can be judged."""
    out = ["<ring-0>"]
    for c in C.courses:
        out.append(f'  <course {a("id", c["id"])} {a("name", c["name"])}>')
        for o in C.sorted_obs(C.of(c["id"])):
            out.append(glance_for(o, "    "))
        out.append("  </course>")
    out.append("</ring-0>")
    return out


# ------------------------------------------------- B: look_at(course), 2c03 only

def _course_open(cid):
    c = [x for x in C.courses if x["id"] == cid][0]
    return f'<course {a("id", c["id"])} {a("name", c["name"])} {a("term", c["term"])}>'


def B0_incumbent(cid="2c03"):
    out = [_course_open(cid), "  <obligations>"]
    for o in C.sorted_obs(C.of(cid)):
        out.append(glance_for(o, "    "))
    out += ["  </obligations>", "</course>"]
    return out


def B1_no_container(cid="2c03"):
    out = [_course_open(cid)]
    for o in C.sorted_obs(C.of(cid)):
        out.append(glance_for(o, "  "))
    out.append("</course>")
    return out


def B2_banded(cid="2c03"):
    out = [_course_open(cid)]
    for b in ("A", "B"):
        for o in C.sorted_obs([o for o in C.of(cid) if o["_band"] == b]):
            out.append(glance_for(o, "  "))
    out.append("</course>")
    return out


def B3_dated_vs_undated(cid="2c03"):
    """Surfaces where a null `due` sorts, which 0082's ordering rule does not say."""
    rows = C.of(cid)
    out = [_course_open(cid), "  <scheduled>"]
    for o in C.sorted_obs([o for o in rows if o["due"]]):
        out.append(glance_for(o, "    "))
    out += ["  </scheduled>", "  <undated>"]
    for o in C.sorted_obs([o for o in rows if not o["due"]]):
        out.append(glance_for(o, "    "))
    out += ["  </undated>", "</course>"]
    return out


# ------------------------------- B5/C4: the source cut, applied to both kinds
# #60 Step 2: sections are cut BY SOURCE, and the cut is two landed rulings -
#   0045  the coordinator sees what a node IS, never what someone SAYS about it
#   0046  annotations arrive through their own channel, NEVER as ordinary neighbours
# Step 3 gives each section its own depth:
#   own fields  -> all of them   (0038: excluded from the projection is not unreadable)
#   annotations -> full text     (0046: an annotation has no identity apart from its target)
#   neighbours  -> one line      (0060: one level deeper is one more call)
#
# HOLE 3, which #60 left and nothing since has filled: 0084 rules that a course
# COMPOSES obligations.list(course), but never says where that batch lands. The
# cut is by source, and a composed batch is a FOURTH source - it is not the node
# itself, it is not something said about it, and 0084 says it is reached by no
# edge, so it is not a neighbour. By the same rule that made 0046 give
# annotations their own channel, it gets its own section.

def _annotations_section(nid, indent):
    out, prog, notes = [], C.prog_on(nid), C.notes_on(nid)
    if not prog and not notes:
        return [f"{indent}<annotations/>"]
    out.append(f"{indent}<annotations>")
    for pr in prog:
        out.append(_prog_el(pr, indent + "  "))
    for n in notes:
        out.append(_note_el(n, indent + "  "))
    out.append(f"{indent}</annotations>")
    return out


def _links_section(nid, indent):
    ix = {x["id"]: x for x in C.obs}
    nbrs = [(role, ix[o]) for role, o, _d in C.links_on(nid) if o in ix]
    if not nbrs:
        return [f"{indent}<links/>"]
    out = [f"{indent}<links>"]
    for role, n in nbrs:
        out += glance_struct(n, indent + "  ", extra=f' role="{role}"')
    out.append(f"{indent}</links>")
    return out


def line(o, indent, extra="", drop_course=False):
    """THE LINE, read literally off 0082: "ring 0's band PLUS `has-more` and the
    link's `role`". Band A already carries has-more, so "plus has-more" is only
    non-redundant if "the band" means band B. The line is therefore ONE field set -
    course, name, due, state, has-more, role - and does not vary per row. A per-row
    band would import 0038's RESIDENCY computation into a READ, which is the same
    transfer hazard 0082 flags about itself."""
    head = (f'{indent}<glance kind="obligation" {a("id", o["id"])} {a("name", o["name"])} '
            f'{a("due", o["due"])} {a("state", o["_state"])}{extra}>')
    out = [head]
    if not drop_course:
        out.append(f'{indent}  <course ref="{o["course"]}"/>')
    out += _more_children(o, indent + "  ", "repeat")
    out.append(f"{indent}</glance>")
    return out


def B6_uniform_line(cid="2c03"):
    """B5 with the line read as one field set, and the redundant course ref dropped."""
    c = [x for x in C.courses if x["id"] == cid][0]
    out = [f'<course {a("id", c["id"])} {a("name", c["name"])} {a("term", c["term"])}>']
    out += _annotations_section(cid, "  ")
    out += _links_section(cid, "  ")
    out.append("  <obligations>")
    for o in C.sorted_obs(C.of(cid)):
        out += line(o, "    ", drop_course=True)
    out += ["  </obligations>", "</course>"]
    return out


def B7_uniform_line_keeps_course(cid="2c03"):
    """B6 keeping <course ref> on every member, so the redundancy can be judged."""
    c = [x for x in C.courses if x["id"] == cid][0]
    out = [f'<course {a("id", c["id"])} {a("name", c["name"])} {a("term", c["term"])}>']
    out += _annotations_section(cid, "  ")
    out += _links_section(cid, "  ")
    out.append("  <obligations>")
    for o in C.sorted_obs(C.of(cid)):
        out += line(o, "    ")
    out += ["  </obligations>", "</course>"]
    return out


def B5_source_cut(cid="2c03"):
    """look_at(course), sections derived from the source cut rather than chosen."""
    c = [x for x in C.courses if x["id"] == cid][0]
    out = [f'<course {a("id", c["id"])} {a("name", c["name"])} {a("term", c["term"])}>']
    out += _annotations_section(cid, "  ")
    out += _links_section(cid, "  ")
    out.append("  <obligations>")           # the fourth source: composed, per 0084
    for o in C.sorted_obs(C.of(cid)):
        out += glance_struct(o, "    ")
    out += ["  </obligations>", "</course>"]
    return out


def C4_source_cut():
    """The same three sections on an obligation, so both kinds sit on one sketch."""
    o = [x for x in C.obs if x["name"] == BLOCK and x["course"] == "2c03"][0]
    out = [f'<obligation {a("id", o["id"])} {a("name", o["name"])} {a("due", o["due"])} '
           f'{a("done_by", o["done_by"])} {a("optional", o["optional"])}>',
           f'  <course ref="{o["course"]}"/>',
           f'  <grade_share conditional="{str(o["grade_share_conditional"]).lower()}">'
           f'{o["grade_share"]}</grade_share>',
           "  <parts>"]
    out += [f"    <part>{esc(pt)}</part>" for pt in o["parts"]]
    out.append("  </parts>")
    out += _annotations_section(o["id"], "  ")
    out += _links_section(o["id"], "  ")
    out.append("</obligation>")
    return out


# ------------------------------------------------------------- C: the block

BLOCK = "Midterm 1"


def _block_parts():
    o = [x for x in C.obs if x["name"] == BLOCK and x["course"] == "2c03"][0]
    head = (f'<obligation {a("id", o["id"])} {a("name", o["name"])} {a("due", o["due"])} '
            f'{a("done_by", o["done_by"])} {a("optional", o["optional"])}>')
    ref = f'  <course ref="{o["course"]}"/>'
    share = f'  <grade_share conditional="{str(o["grade_share_conditional"]).lower()}">{o["grade_share"]}</grade_share>'
    parts = [f"    <part>{esc(p)}</part>" for p in o["parts"]]
    prog = [p for p in C.prog_on(o["id"])]
    notes = C.notes_on(o["id"])
    ix = {x["id"]: x for x in C.obs}
    nbrs = [(role, ix[other]) for role, other, _dir in C.links_on(o["id"])]
    return o, head, ref, share, parts, prog, notes, nbrs


def _note_el(n, ind):
    body = "\n".join(f"{ind}  {ln}" for ln in _wrap(n["body"], 72))
    return (f'{ind}<sticky_note {a("id", n["id"])} {a("category", n["category"])} '
            f'{a("origin", n["origin"])}>\n{body}\n{ind}</sticky_note>')


def _prog_el(p, ind):
    if p["detail"]:
        return (f'{ind}<progress {a("id", p["id"])} {a("state", p["state"])} '
                f'{a("origin", p["origin"])}>{esc(p["detail"])}</progress>')
    return f'{ind}<progress {a("id", p["id"])} {a("state", p["state"])} {a("origin", p["origin"])}/>'


def _wrap(s, n):
    words, line, out = s.split(), "", []
    for w in words:
        if len(line) + len(w) + 1 > n:
            out.append(line)
            line = w
        else:
            line = f"{line} {w}".strip()
    if line:
        out.append(line)
    return out


def C0_incumbent():
    """PR #69's sample, modernised only where #62 and 0092 already ruled."""
    o, head, ref, share, parts, prog, notes, nbrs = _block_parts()
    out = [head, ref, share, "  <parts>"] + parts + ["  </parts>", "  <annotations>"]
    for p in prog:
        out.append(_prog_el(p, "    "))
    for n in notes:
        out.append(_note_el(n, "    "))
    out.append("  </annotations>")
    out.append("  <links>")
    for role, n in nbrs:
        out.append(glance_for(n, "    ", f' role="{role}"'))
    out += ["  </links>", "</obligation>"]
    return out


def C1_no_containers():
    o, head, ref, share, parts, prog, notes, nbrs = _block_parts()
    out = [head, ref, share] + [p.replace("    ", "  ") for p in parts]
    for p in prog:
        out.append(_prog_el(p, "  "))
    for n in notes:
        out.append(_note_el(n, "  "))
    for role, n in nbrs:
        out.append(glance_for(n, "  ", f' role="{role}"'))
    out.append("</obligation>")
    return out


def C2_container_where_a_channel_is():
    """A container only where 0046 gives the members their own channel."""
    o, head, ref, share, parts, prog, notes, nbrs = _block_parts()
    out = [head, ref, share] + [p.replace("    ", "  ") for p in parts] + ["  <annotations>"]
    for p in prog:
        out.append(_prog_el(p, "    "))
    for n in notes:
        out.append(_note_el(n, "    "))
    out.append("  </annotations>")
    for role, n in nbrs:
        out.append(glance_for(n, "  ", f' role="{role}"'))
    out += ["</obligation>"]
    return out


def C3_neighbours_container():
    o, head, ref, share, parts, prog, notes, nbrs = _block_parts()
    out = [head, ref, share] + [p.replace("    ", "  ") for p in parts]
    for p in prog:
        out.append(_prog_el(p, "  "))
    for n in notes:
        out.append(_note_el(n, "  "))
    out.append("  <neighbours>")
    for role, n in nbrs:
        out.append(glance_for(n, "    ", f' role="{role}"'))
    out += ["  </neighbours>", "</obligation>"]
    return out


# ------------------------------------------------------------------ driver

VARIANTS = [
    ("A", "ring 0, all five courses, 55 obligations", [
        ("A0", "incumbent extrapolated: <obligations> container + band=\"\" attribute", A0_incumbent),
        ("A1", "a named container per band", A1_named_container_per_band),
        ("A2", "an attribute on each member, one flat list", A2_attribute_flat),
        ("A3", "pure ordering, no marker, no container", A3_pure_ordering),
        ("A4", "depth IS the band - 0038's two field sets, no marker  [BYTE-IDENTICAL TO A3]", A4_depth_is_the_band),
        ("A5", "grouped by course - the shape `reload` argues against", A5_grouped_by_course),
        ("A6", "A1 + 0082 obeyed inside the member: <course ref> and <has-more> are elements",
         A6_structured_named_container),
        ("A7", "A3/A4 + 0082 obeyed inside the member", A7_structured_depth_is_the_band),
        ("A8", "A6 with has-more as one element carrying <link-kind> children",
         A8_structured_nested_has_more),
    ]),
    ("B", "look_at(course) over 2c03, the composed obligation list", [
        ("B0", "incumbent: <obligations> container", B0_incumbent),
        ("B1", "no container, glances as direct children", B1_no_container),
        ("B2", "banded inside the course view", B2_banded),
        ("B3", "sectioned scheduled / undated", B3_dated_vs_undated),
        ("B4", "0082 obeyed inside each composed member", B4_structured),
        ("B5", "THE SOURCE CUT: sections from 0045 + 0046, composed batch as a fourth source",
         B5_source_cut),
        ("B6", "B5 + the line as ONE field set (0082's `band plus has-more`), course ref dropped",
         B6_uniform_line),
        ("B7", "B6 keeping the redundant <course ref> on every member", B7_uniform_line_keeps_course),
    ]),
    ("C", "the block: one obligation's own render, 2c03 Midterm 1", [
        ("C0", "incumbent: <parts> <annotations> <links>", C0_incumbent),
        ("C1", "no containers at all", C1_no_containers),
        ("C2", "a container only where a channel exists", C2_container_where_a_channel_is),
        ("C3", "<neighbours/> for links, annotations flat", C3_neighbours_container),
        ("C4", "THE SOURCE CUT on an obligation - same three sections as B5", C4_source_cut),
    ]),
]


def main():
    print(open(sys.path[0] + "/BANNER.txt").read())
    for group, title, variants in VARIANTS:
        print("\n" + "=" * W)
        print(f"GROUP {group}  {title}")
        print("=" * W)
        for name, desc, fn in variants:
            body = "\n".join(fn())
            print("\n" + "-" * W)
            print(f"{name}  {desc}")
            print(f"     {len(body)} chars")
            print("-" * W)
            print(body)

    print("\n" + "=" * W)
    print("SIZE, over the REAL 2c03 rows only (14 obligations). 0077 bars any count")
    print("taken from the four derived courses; these are the only auditable numbers here.")
    print("=" * W)
    real = C.of("2c03")
    for label, fn in (("band A flat", glance_a), ("band B flat", glance_b)):
        lens = [len(fn(o, "")) for o in real]
        print(f"  {label:22} n={len(lens)}  min={min(lens)}  max={max(lens)}  mean={sum(lens)//len(lens)}")
    for label, band in (("band A structured", "A"), ("band B structured", "B")):
        rows = [o for o in real if o["_band"] == band] or real
        lens = [len("\n".join(glance_struct(dict(o, _band=band), ""))) for o in real]
        print(f"  {label:22} n={len(lens)}  min={min(lens)}  max={max(lens)}  mean={sum(lens)//len(lens)}")
    blk = len("\n".join(C0_incumbent()))
    print(f"  block (Midterm 1, C0)          {blk} chars")
    print(f"  band A count over real 2c03    {sum(1 for o in real if o['_band'] == 'A')} of {len(real)}")
    about_only = sum(1 for o in real if any(n["about"] == o["id"] for n in C.notes))
    print(f"  has-more non-empty, `about` alone   {about_only} of {len(real)}   <- 0092 states 6 of 14")
    print(f"  has-more non-empty, incl hand links {sum(1 for o in real if o['_more'])} of {len(real)}   <- NOT evidence, links are made up")
    flatA = sum(len(glance_a(o, "")) for o in real) / len(real)
    strA = sum(len("\n".join(glance_struct(dict(o, _band="A"), ""))) for o in real) / len(real)
    flatB = sum(len(glance_b(o, "")) for o in real) / len(real)
    strB = sum(len("\n".join(glance_struct(dict(o, _band="B"), ""))) for o in real) / len(real)
    r = sum(1 for o in real if o["_band"] == "A") / len(real)
    print()
    print("  Ring 0 at 55 rows, extrapolated from REAL per-row cost and 2c03's own band ratio")
    print(f"  (band A = {r:.0%} of rows; that ratio comes from ONE course and 2px3 would move it):")
    print(f"    flat        {55 * (r * flatA + (1 - r) * flatB):.0f} chars")
    print(f"    structured  {55 * (r * strA + (1 - r) * strB):.0f} chars"
          f"   (+{(r * strA + (1 - r) * strB) / (r * flatA + (1 - r) * flatB) - 1:.0%})")


if __name__ == "__main__":
    main()
