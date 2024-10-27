#!/usr/bin/python3
"""
a script that reads stdin line by line and computes metrics:
"""
import sys
import signal


# Initialize global counters and dictionaries
total_file_size = 0
status_counts = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
line_count = 0


def print_stats():
    """Print the current statistics."""
    print(f"File size: {total_file_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def process_line(line):
    """Process a single line to extract metrics."""
    global total_file_size, status_counts, line_count

    parts = line.split()
    if len(parts) != 7:
        return  # Skip if the line format is incorrect

    try:
        # Parse the status code and file size
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update total file size and status code counts
        total_file_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

        line_count += 1
    except (ValueError, IndexError):
        pass  # Skip lines with parsing issues


def handle_interrupt(signal, frame):
    """Handle keyboard interrupt (CTRL + C)."""
    print_stats()
    sys.exit(0)


# Set up the interrupt handler
signal.signal(signal.SIGINT, handle_interrupt)

# Read input line by line
try:
    for line in sys.stdin:
        process_line(line)
        if line_count % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
