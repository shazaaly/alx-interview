#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics
"""

import sys, re

lines = []

def use_regex(input_text):
    pattern = re.compile(r'^(\d{1,3}(\.\d{1,3}){3}) - (.*?) "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')
    return pattern.match(input_text)


try:
    while True:
        line = input()
        lines.append(line)
except EOFError:
    pass
except KeyboardInterrupt:
    pass

possible_status_codes = {
    "200" : 0,
    "301" : 0,
    "400" : 0,
    "401" : 0,
    "403" : 0,
    "404" : 0,
    "405" : 0,
    "500" : 0,
}

total_file_size = 0
try:

    for line in lines:
        match = use_regex(line)
        if match:
            ip_address = match.group(1)
            date = match.group(3)
            status_code = match.group(4)
            if str(status_code) in possible_status_codes:
                possible_status_codes[status_code] += 1


            file_size = match.group(5)
            total_file_size += int(file_size)
            #print(f"File size: {total_file_size}")
except EOFError:
    pass
except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {total_file_size}\t")
    for status_code, count in possible_status_codes.items():
        print(f"{status_code}: {count}")









