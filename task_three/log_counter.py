"""Counts log files"""

from collections import defaultdict

def count_logs_by_level(logs: list) -> dict:
    """Counts logs by level.

    Args:
        logs:
            List of logs' dictionaries.
    
    Returns:
        Dictionary with each log level counts ex. {"ERROR": 3}
    """
    errors_count = defaultdict(int)
    for log in logs:
        if log:
            errors_count[log['level']] += 1
    return dict(errors_count)
