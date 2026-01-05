from collections import defaultdict, deque
from datetime import datetime, timedelta

# Threshold configuration
FAILURE_LIMIT = 5
TIME_WINDOW = timedelta(minutes=10)

def analyze_logs(log_file_path):
    """
    Reads log file line by line, tracks failed logins per IP,
    and triggers alert if failures exceed threshold.
    """

    # Dictionary to store IP -> failure timestamps
    ip_failures = defaultdict(deque)

    with open(log_file_path, "r") as file:
        for line in file:
            # Process only failed login entries
            if "FAIL" not in line:
                continue

            # Expected log format:
            # YYYY-MM-DD HH:MM:SS IP=xxx.xxx.xxx.xxx STATUS=FAIL
            parts = line.strip().split()
            timestamp = datetime.strptime(
                parts[0] + " " + parts[1],
                "%Y-%m-%d %H:%M:%S"
            )
            ip_address = parts[2].split("=")[1]

            # Add failure timestamp for IP
            ip_failures[ip_address].append(timestamp)

            # Remove timestamps older than 10 minutes
            while (
                ip_failures[ip_address]
                and timestamp - ip_failures[ip_address][0] > TIME_WINDOW
            ):
                ip_failures[ip_address].popleft()

            # Trigger alert
            if len(ip_failures[ip_address]) > FAILURE_LIMIT:
                print(f"ALERT: Suspicious IP detected -> {ip_address}")

def main():
    # Path to log file
    log_file = "T.Day 16/server.log"
    analyze_logs(log_file)

if __name__ == "__main__":
    main()
