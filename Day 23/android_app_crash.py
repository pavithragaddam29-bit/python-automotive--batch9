import os
from collections import Counter

# ================================
# Android Logcat Crash Analyzer
# Automotive Infotainment Edition
# ================================

LOG_FILE = "android_logcat.txt"


# . Data Collection Layer

def read_logcat_file():
    if not os.path.exists(LOG_FILE):
        print(" Error: Android logcat file not found!")
        return []

    with open(LOG_FILE, "r") as file:
        return file.readlines()

# 1. Crash Detection Layer 
def extract_crash_reasons(log_lines):
    crash_reasons = []
  
    for i in range(len(log_lines)):
        line = log_lines[i].strip()
        
        # Look for the crash trigger
        if "FATAL EXCEPTION" in line or "Error" in line:
            if i + 1 < len(log_lines):
                error_detail = log_lines[i+1].strip()
                clean_reason = error_detail.split(":")[0]
                crash_reasons.append(clean_reason)
            else:
                crash_reasons.append(line)

    return crash_reasons
# . Crash Frequency Analysis
def analyze_crashes(crash_list):
    return Counter(crash_list)
# 2. Display Report Layer
def display_results(crash_data):
    print("\n ANDROID APP CRASH REPORT")
    print("----------------------------------")

    if not crash_data:
        print(" No crashes detected. Check if 'android_logcat.txt' is empty or formatted correctly.")
        return

    # Sort and display results
    for crash, count in crash_data.most_common():
        print(f"Type: {crash.ljust(35)} | Count: {count}")

    print("----------------------------------")
    print("  Top Diagnostic Priority:")
    print(f">> {crash_data.most_common(1)[0][0]}")

# 3 Main Infotainment Diagnostic
def main():
    print(" Android Infotainment Crash Analyzer Started...\n")

    log_data = read_logcat_file()
    
    if log_data:
        crashes = extract_crash_reasons(log_data)
        crash_stats = analyze_crashes(crashes)
        display_results(crash_stats)

if __name__ == "__main__":
    main()