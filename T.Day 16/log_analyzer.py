from collections import defaultdict, deque
from datetime import datetime, timedelta

FAIL_LIMIT = 5
TIME_WINDOW = timedelta(minutes=10)

def process_log_line(line, state):
    if "FAIL" not in line:
        return None

    parts = line.split()
    timestamp = datetime.strptime(parts[0] + " " + parts[1], "%Y-%m-%d %H:%M:%S")
    ip = parts[2].split("=")[1]

    state[ip].append(timestamp)

    while state[ip] and timestamp - state[ip][0] > TIME_WINDOW:
        state[ip].popleft()

    if len(state[ip]) > FAIL_LIMIT:
        return ip
    return None
