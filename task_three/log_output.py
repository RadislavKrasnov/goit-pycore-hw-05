"""Log output module"""

from log_filter import filter_logs_by_level

def display_log_counts(counts: dict) -> None:
    """Displays log counts.

    Args:
        counts:
            Dictionary with counts of each level ex. {ERROR: 3}.

    Returns:
        None.
    """
    header = """
Рівень логування | Кількість
-----------------|----------"""
    print(header)
    for status, count in counts.items():
        print(f"{status:<16} | {count:<10}")

def display_log_details_by_level(logs: list, level: str) -> None:
    """Displays log details by level.

    Args:
        logs:
            List of logs dictionaries.
        level:
            String that contains logs level.

    Returns:
        None.
    """
    filtered_logs = filter_logs_by_level(logs, level)

    if filtered_logs:
        print(f'Деталі логів для рівня {level.upper()}:')
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} {log['level']} {log['message']}")
