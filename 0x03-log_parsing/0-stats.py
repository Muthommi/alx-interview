#!/usr/bin/python3
"""
Script that reads stdin line by line.
"""

import sys
import signal
from typing import Dict, Union


def print_stats(total_size: int, status_codes: dict[int, int]) -> None:
    """Print the stats."""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def validate_line(line: str) -> Union[tuple, None]:
    """
    Validate and extract information from a line.
    """
    try:
        parts = line.split()

        if len(parts) < 7:
            return None

        status_code = int(parts[-2])
        file_size = int(parts[-1])

        if status_code not in [200, 301, 400, 401, 403, 404, 405, 500]:
            return None

        return (file_size, status_code)
    except (ValueError, IndexError):
        return None


def main():
    """Main function to process the input."""
    total_size = 0
    line_count = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }

    def signal_handler(sig, frame):
        """Handles keyboard interrupt."""
        print_stats(total_size, status_codes)
        sys.exit(0)

    signal.signal(signal.SIGINT, signal_handler)

    try:
        for line in sys.stdin:
            line = line.strip()
            result = validate_line(line)

            if result:
                file_size, status_code = result
                total_size += file_size
                status_codes[status_code] += 1
                line_count += 1

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
