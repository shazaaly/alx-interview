#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics
"""

import sys, re

lines = []

def use_regex(input_text):
    pattern = re.compile(r'^(\d{1,3}(\.\d{1,3}){3}) - (.*?) "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')
    return pattern.match(input_text)


while True:
    try:
        line = input()
        lines.append(line)
    except EOFError:  # This will catch the Ctrl+D
        break

for input in lines:
    match = use_regex(input)
    if match:
        print(match.group(1))
        print(match.group(3))
        print(match.group(4))
        print(match.group(5))
    else:
        print('No match found')






