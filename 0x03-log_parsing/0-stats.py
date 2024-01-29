#!/usr/bin/python3
""" a script to generate stdout logs"""


import sys
import re

def use_regex(input_text):
    """ a function to generate stdout logs"""
    pattern = re.compile(r'^(\d{1,3}(\.\d{1,3}){3}) - (.*?) "GET /projects/260 HTTP/1\.1" (\d{3}) (\d+)$')
    return pattern.match(input_text)

possible_status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0,
}

total_file_size = 0
lines_count = 0

try:
    for line in sys.stdin:
        lines_count += 1


        match = use_regex(line)
        if match:
            status_code = match.group(4)
            if status_code in possible_status_codes.keys():
                possible_status_codes[status_code] += 1

            file_size = int(match.group(5))
            total_file_size += file_size
        if lines_count == 10:
            lines_count = 0
            print(f"File size: {total_file_size}")
            for status_code, count in possible_status_codes.items():
                print(f"{status_code}: {count}")

finally:
        #if lines_count == 10:
            print(f"File size: {total_file_size}")
            for status_code, count in possible_status_codes.items():
                print(f"{status_code}: {count}")
