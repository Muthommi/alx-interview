#!/usr/bin/python3
import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0


def print_metrics():
    """Print the total file size."""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        if len(parts) < 7:
            continue

        try:
            file_size = int(parts[-1])
            status_code = int(parts[-2])
        except (ValueError, IndexError):
            continue

            if status_code in status_codes:
                total_size += file_size
                status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_metrics()

except KeyboardInterrupt:
    print_metrics()
    raise

if line_count > 0:
    print_metrics()
