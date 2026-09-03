"""Corpus for the #80 render prototype: real 2c03, hand-made progress, four synthetic courses.

THROWAWAY. Not a fixture, not evidence. See README.md for what is real and what is not.
"""

import json

REAL_2C03 = "/Users/billywu/Documents/Projects/fall26/app/tests/fixtures/2c03.json"

AS_OF = "2026-02-09"   # winter-2026 is past, so an as-of date had to be chosen
BACK_DAYS, FWD_DAYS = 7, 14   # 0042 rules the window: [today-7d, today+14d]

_next_id = 40


def mint():
    """Opaque assigned id, per 0025. Course ids are material-supplied, per 0026."""
    global _next_id
    _next_id += 1
    return str(_next_id)


def load_real():
    d = json.load(open(REAL_2C03))
    course = {"kind": "course", "id": d["course"]["id"], "name": d["course"]["name"],
              "term": d["course"]["term"]}
    obs, notes = [], []
    by_name = {}
    for o in d["obligations"]:
        rec = dict(o, kind="obligation", id=mint(), course=course["id"])
        by_name[o["name"]] = rec["id"]
        obs.append(rec)
    for n in d["notes"]:
        target = course["id"] if n["about"] == "course" else by_name[n["about"]]
        notes.append({"kind": "sticky_note", "id": mint(), "category": n["category"],
                      "origin": n["origin"], "body": n["body"], "about": target})
    return course, obs, notes


# Hand-made, per Billy's ruling at #80: this ticket looks at the render, not at
# whether the state is true of the world. 0035 governs the shape - state is
# non-nullable and absence carries not_started, so only non-default rows exist.
HAND_PROGRESS = [
    ("Assignment 4", "in_progress", "Stack done, Queue not started."),
    ("Assignment 3", "done", ""),
    ("Assignment 2", "done", ""),
    ("Assignment 1", "done", ""),
    ("Midterm 1", "done", ""),
    ("IDEA Conference", "in_progress", "Registered, abstract not written."),
]


def attach_progress(obs):
    out = []
    ix = {o["name"]: o["id"] for o in obs}
    for name, state, detail in HAND_PROGRESS:
        out.append({"kind": "progress", "id": mint(), "state": state,
                    "detail": detail, "origin": "owner", "about": ix[name]})
    return out


# DERIVED. Shape only - no count taken from these rows may enter the answer (0077).
SYNTH = [
    ("2aa4", "Computer Architecture", [
        ("Lab 1", "2026-01-20T23:59", 4, ["Datapath"], False),
        ("Lab 2", "2026-02-03T23:59", 4, ["ALU"], False),
        ("Lab 3", "2026-02-24T23:59", 4, ["Pipelining", "Hazards"], False),
        ("Lab 4", "2026-03-17T23:59", 4, ["Cache"], False),
        ("Quiz 1", "2026-01-28T09:30", 5, ["Number representation"], False),
        ("Quiz 2", "2026-02-11T09:30", 5, ["Single-cycle datapath"], False),
        ("Quiz 3", "2026-03-11T09:30", 5, ["Memory hierarchy"], False),
        ("Midterm", "2026-02-18T19:00", 20, ["Datapath", "Control", "Pipelining"], False),
        ("Final Exam", None, 40, [], False),
        ("Peer Feedback Form", "2026-03-30", 1, [], True),
    ]),
    ("2px3", "Professional Communication for Engineers", [
        ("Reflection 1", "2026-01-19T23:59", 3, ["Audience analysis"], False),
        ("Reflection 2", "2026-01-26T23:59", 3, ["Genre"], False),
        ("Reflection 3", "2026-02-02T23:59", 3, ["Revision"], False),
        ("Reflection 4", "2026-02-09T23:59", 3, ["Ethics"], False),
        ("Reflection 5", "2026-02-23T23:59", 3, ["Visual design"], False),
        ("Reflection 6", "2026-03-02T23:59", 3, ["Collaboration"], False),
        ("Team Charter", "2026-01-30T23:59", 5, ["Roles", "Conflict process"], False),
        ("Proposal Draft", "2026-02-13T23:59", 8, ["Problem statement", "Scope"], False),
        ("Proposal Peer Review", "2026-02-20T23:59", 4, [], False),
        ("Proposal Final", "2026-03-06T23:59", 15, ["Problem statement", "Scope", "Budget"], False),
        ("Oral Presentation", "2026-03-24T13:30", 20, ["Slides", "Delivery"], False),
        ("Portfolio", "2026-04-08T23:59", 25, [], False),
        ("Attendance", None, 5, [], False),
        ("Workshop Sign-up", "2026-01-15", None, [], True),
    ]),
    ("2fa3", "Discrete Mathematics", [
        ("Problem Set 1", "2026-01-21T23:59", 6, ["Induction"], False),
        ("Problem Set 2", "2026-02-04T23:59", 6, ["Relations", "Functions"], False),
        ("Problem Set 3", "2026-02-25T23:59", 6, ["Graph theory"], False),
        ("Problem Set 4", "2026-03-18T23:59", 6, ["Counting", "Probability"], False),
        ("Term Test 1", "2026-02-12T18:30", 15, ["Logic", "Proof techniques"], False),
        ("Term Test 2", "2026-03-19T18:30", 15, ["Graphs", "Trees"], False),
        ("Final Exam", None, 40, [], False),
        ("Tutorial Participation", None, 6, [], False),
        ("Course Evaluation", "2026-04-03", 0, [], True),
    ]),
    ("3mi3", "Machine Learning", [
        ("Assignment 1", "2026-01-23T23:59", 10, ["Linear regression"], False),
        ("Assignment 2", "2026-02-13T23:59", 10, ["Classification", "Regularization"], False),
        ("Assignment 3", "2026-03-13T23:59", 10, ["Neural networks"], False),
        ("Project Proposal", "2026-02-06T23:59", 5, [], False),
        ("Project Checkpoint", "2026-03-06T23:59", 10, [], False),
        ("Project Report", "2026-04-10T23:59", 30, ["Method", "Results", "Discussion"], False),
        ("Midterm", "2026-02-20T14:30", 20, ["Supervised learning", "Model selection"], False),
        ("Kaggle Bonus", "2026-04-10T23:59", 2, [], True),
    ]),
]

SYNTH_PROGRESS = [
    ("2aa4", "Lab 3", "in_progress"), ("2aa4", "Lab 1", "done"), ("2aa4", "Lab 2", "done"),
    ("2aa4", "Quiz 1", "done"), ("2aa4", "Quiz 2", "in_progress"),
    ("2px3", "Reflection 4", "in_progress"), ("2px3", "Reflection 1", "done"),
    ("2px3", "Reflection 2", "done"), ("2px3", "Reflection 3", "done"),
    ("2px3", "Team Charter", "done"), ("2px3", "Proposal Draft", "in_progress"),
    ("2fa3", "Problem Set 2", "in_progress"), ("2fa3", "Problem Set 1", "done"),
    ("2fa3", "Term Test 1", "in_progress"),
    ("3mi3", "Assignment 2", "in_progress"), ("3mi3", "Assignment 1", "done"),
    ("3mi3", "Project Proposal", "done"),
]

SYNTH_NOTES = [
    ("2aa4", "Midterm", "logistics", "Midterm is in ETB 227, not the lecture hall."),
    ("2aa4", "Lab 3", "clarification", "Hazard detection is graded on the writeup, not the code."),
    ("2px3", "Oral Presentation", "logistics", "Presentation slots are assigned, not chosen."),
    ("2px3", "Portfolio", "policy", "No late submissions accepted on the portfolio."),
    ("2fa3", "Term Test 2", "clarification", "Trees are in scope; network flow is not."),
    ("3mi3", "Project Report", "policy", "Groups of at most three, declared by the checkpoint."),
]


# Hand-made, same licence as HAND_PROGRESS. The real corpus holds ZERO non-annotation
# links, so without these the block's neighbour container is not exercised at all.
# 0012's signature admits `builds-on` today; 0017 makes a link a record with a role.
HAND_LINKS = [
    ("2c03", "Midterm 1", "builds-on", "Assignment 2"),
    ("2c03", "Midterm 1", "builds-on", "Assignment 3"),
    ("2c03", "Midterm 2", "builds-on", "Midterm 1"),
    ("2c03", "Assignment 5", "builds-on", "Assignment 4"),
]


def load_all():
    """Real 2c03 with hand-made progress, plus four derived courses."""
    course, obs, notes = load_real()
    courses = [course]
    prog = attach_progress(obs)

    for cid, cname, rows in SYNTH:
        c = {"kind": "course", "id": cid, "name": cname, "term": "winter-2026"}
        courses.append(c)
        ix = {}
        for name, due, share, parts, optional in rows:
            rec = {"kind": "obligation", "id": mint(), "course": cid, "name": name,
                   "due": due, "done_by": None, "grade_share": share,
                   "grade_share_conditional": False, "parts": parts, "optional": optional}
            ix[name] = rec["id"]
            obs.append(rec)
        for c2, name, state in SYNTH_PROGRESS:
            if c2 == cid:
                prog.append({"kind": "progress", "id": mint(), "state": state, "detail": "",
                             "origin": "owner", "about": ix[name]})
        for c2, name, cat, body in SYNTH_NOTES:
            if c2 == cid:
                notes.append({"kind": "sticky_note", "id": mint(), "category": cat,
                              "origin": "announcement", "body": body, "about": ix[name]})

    by = {(o["course"], o["name"]): o["id"] for o in obs}
    links = [{"kind": "link", "id": mint(), "role": role,
              "from": by[(cid, src)], "to": by[(cid, dst)]}
             for cid, src, role, dst in HAND_LINKS]
    return courses, obs, notes, prog, links
