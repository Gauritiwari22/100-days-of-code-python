# Project 13

"Debugging a program"

print("STUDENT RESULT MANAGEMENT SYSTEM")

students = {}

def add_student(name, marks):
    if name in students:
        print("Student already exists")
    else:
        students[name] = marks
        print("Student added succesfully")

def calculate_average():
    if len(students) == 0:
        return None
    total = 0
    for mark in students.values():
        total += mark
    avg = total / len(students)
    return avg

def get_topper():
    top_marks = 0
    topper = ""
    for name, marks in students.items():
        if marks > top_marks:
            top_marks = marks
            topper = name
    return topper, top_marks


while True:
    print("\n1. Add Student")
    print("2. Calculate Average Marks")
    print("3. Get Topper")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number")
        continue


    if choice == 1:
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))
        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100")
            continue

        add_student(name, marks)

    elif choice == 2:
        print("Average marks:", calculate_average())

    elif choice == 3:
        name, marks = get_topper()
        print("Topper is", name, "with marks", marks)

    elif choice == 4:
        break

    else:
        print("Invalid choice")


"Debugged the following"
# Menu input crash	
# Division by zero	
# Wrong data type
# Invalid marks
# Dictionary iteration	