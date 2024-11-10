import argparse
from datetime import datetime

# Script Description
"""
This script searches a specified log file for lines containing specific keywords 
and within a defined date range, making it useful for targeted log analysis.
"""

# Function to filter log entries by keyword and date range
def search_logs(file_path, keyword, start_date=None, end_date=None):
    with open(file_path, 'r') as file:
        for line in file:
            if keyword in line:
                try:
                    log_date_str = line.split()[0]
                    log_date = datetime.strptime(log_date_str, "%Y-%m-%d")
                    
                    if start_date and log_date < start_date:
                        continue
                    if end_date and log_date > end_date:
                        continue
                    print(line.strip())
                except ValueError:
                    continue  # Skip lines with invalid date formats

# Main function to parse arguments
def main():
    parser = argparse.ArgumentParser(description="Search a log file for specific keywords and date range")
    parser.add_argument("file_path", help="Path to the log file")
    parser.add_argument("keyword", help="Keyword to search for in the log file")
    parser.add_argument("--start_date", help="Start date in YYYY-MM-DD format", type=lambda s: datetime.strptime(s, "%Y-%m-%d"))
    parser.add_argument("--end_date", help="End date in YYYY-MM-DD format", type=lambda s: datetime.strptime(s, "%Y-%m-%d"))
    
    args = parser.parse_args()
    search_logs(args.file_path, args.keyword, args.start_date, args.end_date)

if __name__ == "__main__":
    main()
