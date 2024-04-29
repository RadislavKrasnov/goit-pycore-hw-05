"""Application entry point"""

import sys
from log_reader import load_logs
from log_counter import count_logs_by_level
from log_output import display_log_counts, display_log_details_by_level

def main() -> None:
    file_path = sys.argv[1]
    error_level = sys.argv[2]
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    print()
    display_log_details_by_level(logs, error_level)

if __name__ == "__main__":
    main()
