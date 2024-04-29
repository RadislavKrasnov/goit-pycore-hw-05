"""Counts log files"""

from collections import defaultdict

def count_logs_by_level(logs: list) -> dict:
    errors_count = defaultdict(int)
    for log in logs:
        if log:
            errors_count[log['level']] += 1
    return dict(errors_count)
