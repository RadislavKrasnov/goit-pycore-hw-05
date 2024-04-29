"""Read log files"""

import re

def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, 'r') as file:
        logs = [parse_log_line(line.strip()) for line in file]
    return logs

def parse_log_line(line: str) -> dict:
    pattern = re.compile(
        r'(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})\s(?P<level>\w+)\s(?P<message>.+)', 
        re.I
    )
    match = re.match(pattern, line)
    line = {
        "date": match['date'],
        "time": match['time'],
        "level": match['level'],
        "message": match['message']
    }
    return line
