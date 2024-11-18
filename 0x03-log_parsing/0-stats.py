#!/usr/bin/python3
"""
Module to write a script that reads stdin line by line.
"""
import sys

total_size = 0
status_counts = {}
valid_status_codes = ['200', '301', '400', 401, '403', '404', '405', '500']
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        try:
            file_size = int(parts[-1])
            total_size += file_size

            status_code = parts[-2]
            if status_code in valid_status_codes:
                if status_code not in status_counts:
                    status_counts[status_code] = 0
                status_counts[status_code] += 1

        except (IndexError, ValueError):
            continue

        if line_count % 10 == 0 or line_count == 1:
            print(f"File size: {total_size}")
            for code in sorted(status_counts.keys()):
                print(f"{code}: {status_counts[code]}")

except KeyboardInterrupt:
    pass
finally:
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")
