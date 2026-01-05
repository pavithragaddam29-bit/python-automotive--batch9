from collections import defaultdict, deque
from log_analyzer import process_log_line

def test_alert_triggered():
    state = defaultdict(deque)
    logs = [
        "2026-01-05 10:01:00 IP=1.1.1.1 STATUS=FAIL",
        "2026-01-05 10:02:00 IP=1.1.1.1 STATUS=FAIL",
        "2026-01-05 10:03:00 IP=1.1.1.1 STATUS=FAIL",
        "2026-01-05 10:04:00 IP=1.1.1.1 STATUS=FAIL",
        "2026-01-05 10:05:00 IP=1.1.1.1 STATUS=FAIL",
        "2026-01-05 10:06:00 IP=1.1.1.1 STATUS=FAIL"
    ]

    alert = None
    for line in logs:
        alert = process_log_line(line, state)

    assert alert == "1.1.1.1"
