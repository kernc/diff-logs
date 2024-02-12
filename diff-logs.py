#!/usr/bin/env python3
"""
Normalize logs so that they can be diffed effectively.

This script is part of the diff-logs CLI tool.
"""
import re
import sys


PATTERNS = {
    # Date/time
    r'\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2}(?:[.,]\d+)?Z?': '2111-11-11 11:11:11',
    r'\w{3,}, \d{1,2} \w{3,} \d{4,4} \d{1,2}(?::\d{1,2}){2} [A-Z]{3}': 'Thu, 11 Nov 2111 11:11:11 GMT',
    r'\d{2}-\d{2}-\d{4} \d{2}(?::\d{2}){2}\.\d+': '11-11-2111 11:11:11.111111',
    # Other timestamp
    r'\b\d+(?:\.\d+)?s(?:ec)?\b': '1.1s',
    r'\b(in|since) \d+\.\d+': 'in 1.1',
    # File/download sizes
    r'(?i)\d+(?:\.\d+)?(?:/\d)? ?(?P<suffix>kb|kib|mb|mib|gb|gib)': r'1 \g<suffix>',
    # TCP / HTTP
    r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b': '11.1.1.1',  # IPv4
    r':\d{5,5}\b': ':11111',                                # Remote port
    r'\bport \d{5,5}\b': 'port 11111',                      # Remote port
    r'\bW/(?P<quote>\\?")[^"]*(?P=quote)': 'W/"ETag"',      # ETag header
    # Common files
    r'/tmp/[^/:"\']{6,}(?:/[^/:"\']+)*/?': '/tmp/106d1ff',
    # Common tools
    r'(?P<step_no>(?:\s|\A)#\d+) \d+\.\d+': r'\g<step_no> 1',  # Docker build steps

    r'(?:[\da-fA-F]{4,}-){4,}[\da-fA-F]{4,}': '106d1ff-106d-1ff1-06d1-ff106d1ff',  # UUID
    r'[\da-fA-F]{7,}': '106D1FF',               # Hash digest
    r'[a-zA-Z0-9]{18,}': 'AAAAAAAAAAAAAAAAAA',  # Long payload
    r'━━━━+': '━━━━',                           # Progress bar
}

assert all(re.match(fr'\A(?:{p})\Z', v)
           for p, v in PATTERNS.items()
           if r'\g<' not in v), \
    next(f'Pattern-replacement pair {p!r} not idempotent!'
         for p, v in PATTERNS.items()
         if r'\g<' not in v and not re.match(fr'\A(?:{p})\Z', v))

if len(sys.argv) > 1:
    raise RuntimeError('Pass file to stdin')

for line in sys.stdin:
    for pattern, replacement in PATTERNS.items():
        line = re.sub(pattern, replacement, line)
    print(line, end='')
