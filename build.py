#!/usr/bin/env python3
"""Build the self-contained Clinical Chemistry CAT website from data/questions.csv.
Standard library only; no runtime server or separate asset paths required.
"""
from pathlib import Path
import argparse
import csv
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "data" / "questions.csv"
TEMPLATE = ROOT / "site" / "index.template.html"
DEFAULT_OUTPUT = ROOT / "index.html"
MANDATORY = ["id", "section", "question", "A", "B", "C", "D", "answer", "rationale", "status", "difficulty"]

def read_bank(path=CSV):
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        missing = [k for k in MANDATORY if k not in (reader.fieldnames or [])]
        if missing: raise ValueError(f"Missing CSV columns: {missing}")
        data = list(reader)
    ids = set()
    ready = []
    review = []
    for rowno, row in enumerate(data, start=2):
        rid = (row.get("id") or "").strip()
        if not rid: raise ValueError(f"Missing question ID at row {rowno}")
        if rid in ids: raise ValueError(f"Duplicate question ID: {rid}")
        ids.add(rid)
        if row.get("status", "").strip().lower() != "ready":
            review.append(rid)
            continue
        fields = ["section", "question", "A", "B", "C", "D", "answer", "rationale", "difficulty"]
        if any(not (row.get(k) or "").strip() for k in fields):
            raise ValueError(f"Ready question {rid} contains missing fields; set status=review or fix")
        correct = row["answer"].strip().upper()
        if correct not in "ABCD" or len(correct) != 1:
            raise ValueError(f"Question {rid}: invalid correct answer")
        opts = [(row[k] or "").strip() for k in "ABCD"]
        if len(set(x.casefold() for x in opts)) != 4:
            raise ValueError(f"Question {rid}: duplicated choices")
        try: d = int(row["difficulty"])
        except (TypeError, ValueError): raise ValueError(f"Question {rid}: invalid difficulty")
        if not 1 <= d <= 5: raise ValueError(f"Question {rid}: difficulty must be 1–5")
        ready.append({"id":rid,"topic":row["section"].strip(),"question":row["question"].strip(),
                      "options":opts,"answer":correct,"rationale":row["rationale"].strip(),"difficulty":d})
    if len(ready) < 100:
        raise ValueError(f"Only {len(ready)} ready questions; at least 100 required")
    return ready, review, len(data)

def build(outfile=DEFAULT_OUTPUT):
    questions, review, total = read_bank()
    payload = {"version":hashlib.sha256(json.dumps(questions,sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:14],
               "questions":questions}
    embedded = json.dumps(payload,ensure_ascii=False,separators=(",",":"))
    # Prevent a question's text from closing the application/json script element.
    embedded = embedded.replace("</", "<\\/").replace("<!--", "<\\!--")
    template = TEMPLATE.read_text(encoding="utf-8")
    if template.count("__QUESTION_DATA__") != 1: raise RuntimeError("Template marker missing/duplicated")
    path=Path(outfile);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(template.replace("__QUESTION_DATA__",embedded),encoding="utf-8")
    print(f"Built {path} | bank: {total} indexed, {len(questions)} ready, {len(review)} needing review | version {payload['version']}")

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--out",type=Path,default=DEFAULT_OUTPUT,help="output HTML path")
    args=parser.parse_args()
    try: build(args.out)
    except Exception as e:
        print("BUILD ERROR:",e,file=sys.stderr)
        sys.exit(1)
