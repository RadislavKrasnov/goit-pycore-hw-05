"""Read log files"""

import re

def load_logs(file_path: str) -> list:
    """Loads logs.

    Args:
        file_path:
            String with the path to log file to read.

    Returns:
        List of dictionaries with logs from file 
        ex. {
                "date": "2024-01-22",
                "time": "08:30:01",
                "level": "INFO",
                "message": "User logged in successfully."
            }
    """
    logs = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            logs = [parse_log_line(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(f'File {file_path} not found!')
    return logs

def parse_log_line(line: str) -> dict:
    """Parses log line.

    Args:
        line:
            String that is line of log from file.
    
    Returns:
        Dictionary with log's line parsed data: date, time, level, message.
    """
    pattern = re.compile(
        r'(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})\s(?P<level>\w+)\s(?P<message>.+)', 
        re.I
    )
    match = re.match(pattern, line)
    line = dict()
    
    if match:
        line = {
            "date": match.group('date'),
            "time": match.group('time'),
            "level": match.group('level'),
            "message": match.group('message')
        }
    return line
