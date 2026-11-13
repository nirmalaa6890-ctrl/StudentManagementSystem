from student import Student, StudentManager


manager = StudentManager()


# Validate integer input
def get_valid_age():

    while True:
        try:
            age = int(input("Enter age: "))

            if age <= 0:
                print("Age must be greater than zero!")
                continue

            return age

        except ValueError:
            print("Please enter a valid integer!")


# Validate marks
def get_valid_marks():

    marks = []

    print("\nEnter marks for 4 subjects:")

    for i in range(1, 5):

        while True:
            try:
                mark = float(input(f"Subject {i}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break

                print("Marks must be between 0 and 100!")

            except ValueError:
                print("Please enter valid numeric marks!")

    return marks


# Get non-empty text
def get_valid_text(message):

    while True:
        value = input(message).strip()

        if value:
            return value

        print("This field cannot be empty!")


# Main application
def main():

    while True:

        print("\n===== STUDENT MANAGEMENT SYSTEM =====")

        print("1. Add New Student")
        print("2. Display All Students")
        print("3. Search Student by ID")
        print("4. Update Student Details")
        print("5. Delete Student")
        print("6. Search Student by Name")
        print("7. Sort Students by Marks")
        print("8. Calculate Class Average")
        print("9. Exit")

        choice = input("\nEnter your choice (1-9): ").strip()

        try:

            # Add student
            if choice == '1':

                student_id = get_valid_text("Enter Student ID: ")
                name = get_valid_text("Enter Name: ")
                age = get_valid_age()
                course = get_valid_text("Enter Course: ")
                marks = get_valid_marks()

                student = Student(
                    student_id, name, age, course, marks
                )

                manager.add_student(student)

                print("Student added successfully!")

            # Display all students
            elif choice == '2':

                manager.display_all_students()

            # Search by ID
            elif choice == '3':

                student_id = input("Enter Student ID: ").strip()

                student = manager.get_student_by_id(student_id)

                if student:
                    student.display()
                else:
                    print("Student not found!")

            # Update student
            elif choice == '4':

                student_id = input("Enter Student ID: ").strip()

                student = manager.get_student_by_id(student_id)

                if student is None:
                    print("Student not found!")
                    continue

                print("\nPress Enter to keep the existing value.")

                name = input(
                    f"New Name [{student.name}]: "
                ).strip()

                age_input = input(
                    f"New Age [{student.age}]: "
                ).strip()

                course = input(
                    f"New Course [{student.course}]: "
                ).strip()

                name = name if name else None
                course = course if course else None

                age = None

                if age_input:
                    age = int(age_input)

                    if age <= 0:
                        raise ValueError("Age must be positive!")

                update_marks = input(
                    "Update marks? (y/n): "
                ).strip().lower()

                marks = None

                if update_marks == 'y':
                    marks = get_valid_marks()

                elif update_marks != 'n':
                    print("Invalid choice!")
                    continue

                manager.update_student(
                    student_id, name, age, course, marks
                )

                print("Student updated successfully!")

            # Delete student
            elif choice == '5':

                student_id = input(
                    "Enter Student ID to delete: "
                ).strip()

                student = manager.get_student_by_id(student_id)

                if student is None:
                    print("Student not found!")
                    continue

                confirm = input(
                    "Are you sure? (y/n): "
                ).strip().lower()

                if confirm == 'y':

                    manager.delete_student(student_id)
                    print("Student deleted successfully!")

                else:
                    print("Deletion cancelled.")

            # Search by name
            elif choice == '6':

                name = get_valid_text("Enter student name: ")

                manager.search_by_name(name)

            # Sort by marks
            elif choice == '7':

                manager.sort_by_marks()

            # Class average
            elif choice == '8':

                manager.class_average()

            # Exit
            elif choice == '9':

                print("Exiting program. Goodbye!")
                break

            else:
                print("Invalid choice! Choose between 1 and 9.")

        except ValueError as error:
            print("Input Error:", error)

        except Exception as error:
            print("Something went wrong:", error)


if __name__ == "__main__":
    main()