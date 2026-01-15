#report card preparation using the functions.
def calculate_result(marks):
    if marks >= 60:
        return "Pass"
    else:
        return "Fail"

def prepare_report_card(student_name, subjects):
    print("\nReport Card for", student_name)
    print("-------------------------------")
    print("Subject\tMarks\tResult")
    print("-------------------------------")

    total_marks = 0
    for subject, marks in subjects.items():
        result = calculate_result(marks)
        print(f"{subject}\t{marks}\t{result}")
        total_marks += marks

    average_marks = total_marks / len(subjects)
    overall_result = "Pass" if average_marks >= 60 else "Fail"

    print("-------------------------------")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(f"Overall Result: {overall_result}")
    print("-------------------------------")

def main():
    student_name = input("Enter student name: ")
    num_subjects = int(input("Enter number of subjects: "))
    subjects = {}

    for i in range(num_subjects):
        subject = input(f"Enter subject {i+1} name: ")
        marks = float(input(f"Enter marks for {subject}: "))
        subjects[subject] = marks

    prepare_report_card(student_name, subjects)

if __name__ == "__main__":
    main()