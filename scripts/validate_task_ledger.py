#!/usr/bin/env python3
"""Basic consistency validator; not a substitute for human review or GitHub access rules."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / 'docs' / 'TASKS_DONE.md'
REVIEW_DIR = ROOT / 'docs' / 'qa'


def fail(msg: str) -> None:
    print('ERROR:', msg, file=sys.stderr)
    sys.exit(1)


def main() -> None:
    if not LEDGER.is_file():
        fail('Missing docs/TASKS_DONE.md')
    content = LEDGER.read_text(encoding='utf-8')
    seen = set()
    rows = []
    for line in content.splitlines():
        if not re.match(r'^\|\s*TASK-\d{3,}\s*\|', line):
            continue
        cols = [s.strip() for s in line.strip().strip('|').split('|')]
        if len(cols) != 6:
            fail('Ledger row must have exactly 6 columns: ' + line)
        task, name, report_rel, sha, pr, date = cols
        if task in seen:
            fail('Duplicate completion entry: ' + task)
        seen.add(task)
        if not name or not re.fullmatch(r'[0-9a-fA-F]{7,40}', sha):
            fail(f'{task}: missing name or invalid reviewed SHA')
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', date):
            fail(f'{task}: invalid completion date')
        if not re.fullmatch(r'(?:https://github\.com/[^\s|]+/pull/\d+|#[0-9]+)', pr):
            fail(f'{task}: merged PR link/# required')
        if not re.fullmatch(r'docs/qa/' + re.escape(task) + r'-review-\d{2,}\.md', report_rel):
            fail(f'{task}: invalid QA report path')
        report = ROOT / report_rel
        if not report.is_file() or REVIEW_DIR not in report.parents:
            fail(f'{task}: missing QA review file')
        rev = report.read_text(encoding='utf-8')
        if not re.search(r'^\*\*Decision:\*\*\s*PASS\s*$', rev, re.M):
            fail(f'{task}: QA review is not PASS')
        m = re.search(r'^\*\*Reviewed commit:\*\*\s*([0-9a-fA-F]{7,40})\s*$', rev, re.M)
        if not m or m.group(1).lower() != sha.lower():
            fail(f'{task}: reviewed SHA differs from ledger')
        rows.append(task)
    print(f'Documentary ledger consistency: PASS ({len(rows)} completed-task entries).')
    print('NOTE: This does not verify real CI, GitHub merge status, human approval, or software behavior.')


if __name__ == '__main__':
    main()
