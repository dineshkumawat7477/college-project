import csv
from datetime import datetime

filename = "attendance.csv"

try:
    with open(filename, "x", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Student Name", "Status"])
except:
    pass

def mark_attendance():
    name = input("Enter student name: ")
    status = input("Present or Absent (P/A): ").upper()

    if status == "P":
        status = "Present"
    else:
        status = "Absent"

    date = datetime.now().strftime("%Y-%m-%d")

    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([date, name, status])

    print("Attendance marked successfully!\n")

def show_attendance():
    print("\n--- Attendance Records ---")
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())
    print("--------------------------\n")


while True:
    print("1. Mark Attendance")
    print("2. Show Attendance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        mark_attendance()
    elif choice == "2":
        show_attendance()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again!\n")
    