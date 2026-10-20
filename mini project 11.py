# ==========================================
# PROJECT: STUDENT MANAGEMENT SYSTEM
# Concepts: List, Tuple, Set, Dictionary, Function
# ==========================================

# LIST: Store multiple student records
students_dic = [
    {
        "id": "S101",
        "name": "Rahim",
        "age": 21,
        "department": "CSE",
        "marks": 85
    },
    {
        "id": "S102",
        "name": "Nadia",
        "age": 22,
        "department": "EEE",
        "marks": 92
    },
    {
        "id": "S103",
        "name": "Karim",
        "age": 21,
        "department": "CSE",
        "marks": 88
    }
]

# Fixed message for missing data
DEFAULT_MESSAGE = "Data Not Available"


# FUNCTION: Find student by ID
def find_student(student_id):
    for student in students_dic:
        if student["id"].lower() == student_id.lower():
            return student

    return None


# FUNCTION + TUPLE: Return fixed identity information
def get_student_identity(student):
    return (student["id"], student["name"])


# FUNCTION: Add a new student
def add_student():
    print("\n--- Add New Student ---")

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if find_student(student_id) is not None:
        print("This Student ID already exists!")
        return

    name = input("Enter Name: ").strip()
    department = input("Enter Department: ").strip()

    try:
        age = int(input("Enter Age: "))
        marks = float(input("Enter Marks (0-100): "))

        if age <= 0 or not 0 <= marks <= 100:
            print("Invalid age or marks.")
            return

    except ValueError:
        print("Please enter valid numeric values.")
        return

    # DICTIONARY: Store one student's information
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "department": department,
        "marks": marks
    }

    # LIST: Add the dictionary to the list
    students_dic.append(student)

    print("Student added successfully!")


# FUNCTION: Search student
def search_student():
    student_id = input("Enter Student ID to search: ").strip()
    student = find_student(student_id)

    if student is None:
        print(DEFAULT_MESSAGE)
        return

    identity = get_student_identity(student)

    print("\n--- Student Found ---")
    print("ID:", identity[0])
    print("Name:", identity[1])
    print("Age:", student.get("age", DEFAULT_MESSAGE))
    print("Department:",
          student.get("department", DEFAULT_MESSAGE))
    print("Marks:", student.get("marks", DEFAULT_MESSAGE))


# FUNCTION: Update student marks
def update_marks():
    student_id = input("Enter Student ID: ").strip()
    student = find_student(student_id)

    if student is None:
        print(DEFAULT_MESSAGE)
        return

    try:
        marks = float(input("Enter New Marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    student["marks"] = marks
    print("Marks updated successfully!")


# FUNCTION: Delete student
def delete_student():
    student_id = input("Enter Student ID to delete: ").strip()
    student = find_student(student_id)

    if student is None:
        print(DEFAULT_MESSAGE)
        return

    students_dic.remove(student)
    print("Student deleted successfully!")


# FUNCTION: Display all students
def display_students():
    if not students_dic:
        print("No student records available.")
        return

    print("\n========== STUDENT LIST ==========")

    for student in students_dic:
        identity = get_student_identity(student)

        print(
            f"ID: {identity[0]} | "
            f"Name: {identity[1]} | "
            f"Department: "
            f"{student.get('department', DEFAULT_MESSAGE)} | "
            f"Marks: {student.get('marks', DEFAULT_MESSAGE)}"
        )


# FUNCTION + SET: Show unique departments
def show_departments():
    if not students_dic:
        print("No departments available.")
        return

    # SET: Automatically removes duplicates
    departments = {
        student["department"]
        for student in students_dic
        if student.get("department")
    }

    print("\nUnique Departments:")

    for department in sorted(departments):
        print("-", department)


# FUNCTION: Generate report
def generate_report():
    if not students_dic:
        print("No records available for the report.")
        return

    total_marks = sum(
        student.get("marks", 0)
        for student in students_dic
    )

    average_marks = total_marks / len(students_dic)

    # SET: Count unique departments
    departments = {
        student["department"]
        for student in students_dic
        if student.get("department")
    }

    print("\n========== STUDENT REPORT ==========")
    print("Total Students:", len(students_dic))
    print("Total Departments:", len(departments))
    print(f"Average Marks: {average_marks:.2f}")

    top_student = max(
        students_dic,
        key=lambda student: student.get("marks", 0)
    )

    print("Top Student:", top_student["name"])
    print("Top Marks:", top_student["marks"])


# MAIN FUNCTION: Menu-driven program
def main():
    while True:
        print("\n" + "=" * 35)
        print("   STUDENT MANAGEMENT SYSTEM")
        print("=" * 35)
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Marks")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Show Departments")
        print("7. Generate Report")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            update_marks()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_students()
        elif choice == "6":
            show_departments()
        elif choice == "7":
            generate_report()
        elif choice == "0":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid option. Please try again.")


# Start the program
if __name__ == "__main__":
    main()