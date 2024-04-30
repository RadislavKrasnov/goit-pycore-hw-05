"""Application entry point"""

import sys
from log_reader import load_logs
from log_counter import count_logs_by_level
from log_output import display_log_counts, display_log_details_by_level

def main() -> None:
    """Boots the application.
    Contains the logic of the application.

    Returns:
        None.
    """
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        logs = load_logs(file_path)
        if logs:
            counts = count_logs_by_level(logs)
            display_log_counts(counts)
    
    if len(sys.argv) == 3:
        error_level = sys.argv[2]
        print()
        display_log_details_by_level(logs, error_level)

if __name__ == "__main__":
    main()
