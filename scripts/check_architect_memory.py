#!/usr/bin/env python3
"""Check key handoff doc links and fields. Does NOT verify QA, repo permissions or live Git state."""
from pathlib import Path
import sys

root = Path(__file__).resolve().parents[1]
expected = [
    'docs/CHATGPT_ARCHITECT_MEMORY.md',
    'docs/STATUS.md',
    'docs/ROADMAP.md',
    'docs/SESSION_HANDOFF.md',
    'docs/TASKS_DONE.md',
    'docs/QA_PROTOCOL.md',
]
for rel in expected:
    if not (root / rel).is_file():
        sys.exit(f'MISSING: {rel}')

memory = (root / expected[0]).read_text(encoding='utf-8')
for phrase in [
    '## 0. Quick resume',
    '## 1. How ChatGPT must resume',
    '## 3. Verification ledger',
    '## 4. Current task',
    '## 5. Auditor update procedure',
    'docs/TASKS_DONE.md',
    'exact',
]:
    if phrase not in memory:
        sys.exit(f'Architect memory is missing required section/reference: {phrase}')
print('Architect memory skeleton: PASS (existence and headings only, NOT a QA verdict).')
