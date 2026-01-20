import csv
import os
import datetime

FILE = "office_key_log.csv"

# -----------------------------
# Initialize file with headers
# -----------------------------
def init_file():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "Employee",
                "Taken Time",
                "Returned Time",
                "Duration (minutes)",
                "Status"
            ])

# -----------------------------
# Helpers
# -----------------------------
def read_all():
    with open(FILE, "r", newline="") as f:
        return list(csv.DictReader(f))

def write_all(rows):
    with open(FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

def get_current_holder():
    rows = read_all()
    for row in reversed(rows):
        if row["Status"] == "TAKEN":
            return row
    return None

# -----------------------------
# 3 Core Features
# -----------------------------
def take_key():
    if get_current_holder():
        print("Key already taken")
        return

    name = input("Enter employee name: ")
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, now, "", "", "TAKEN"])

    print("Key issued")

def return_key():
    rows = read_all()

    for row in reversed(rows):
        if row["Status"] == "TAKEN":
            taken_time = datetime.datetime.fromisoformat(row["Taken Time"])
            returned_time = datetime.datetime.now()
            duration = int((returned_time - taken_time).total_seconds() / 60)

            row["Returned Time"] = returned_time.strftime("%Y-%m-%d %H:%M:%S")
            row["Duration (minutes)"] = duration
            row["Status"] = "RETURNED"

            write_all(rows)
            print(" Key returned & logged")
            return

    print("No active key holder")

def show_holder():
    holder = get_current_holder()
    if holder:
        print(f" Current holder: {holder['Employee']}")
        print(f" Taken at: {holder['Taken Time']}")
    else:
        print(" Key is available")

def show_history():
    with open(FILE, "r") as f:
        print("\n===== Key History =====")
        print(f.read())

# -----------------------------
# Menu
# -----------------------------
def menu():
    init_file()
    while True:
        print("\n===== Office Key Tracker =====")
        print("1. Take Key")
        print("2. Return Key")
        print("3. Show Current Holder")
        print("4. Show Full History")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            take_key()
        elif choice == "2":
            return_key()
        elif choice == "3":
            show_holder()
        elif  choice == "4":
            show_history()
        elif choice == "5":
            break
        else:
            print(" Invalid choice")

menu()
