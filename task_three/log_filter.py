"""Log filter module"""

def filter_logs_by_level(logs: list, level: str) -> list:
    """Filters logs by level.

    Args:
        logs:
            List of logs' dictionaries.
        level:
            String with log level.
    
    Returns:
        List of logs' dictionaries filtered by level.
    """
    return list(filter(lambda log: log and log['level'] == level.upper(), logs))
