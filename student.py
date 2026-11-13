import json
import os


class Student:

    def __init__(self, student_id, name, age, course, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    @property
    def total_marks(self):
        return sum(self.marks)

    @property
    def average(self):
        return self.total_marks / len(self.marks)

    @property
    def grade(self):
        avg = self.average

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 40:
            return "D"
        else:
            return "F"

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "course": self.course,
            "marks": self.marks
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["student_id"],
            data["name"],
            data["age"],
            data["course"],
            data["marks"]
        )

    def display(self):
        print("\n----------------------------")
        print("Student ID:", self.student_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print("Total Marks:", self.total_marks)
        print("Average:", round(self.average, 2))
        print("Grade:", self.grade)
        print("----------------------------")


class StudentManager:

    def __init__(self, filename="student_data.txt"):
        self.filename = filename
        self.students = []
        self.load_students()

    # Load student records
    def load_students(self):

        if not os.path.exists(self.filename):
            self.save_students()
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            self.students = [
                Student.from_dict(item) for item in data
            ]

        except json.JSONDecodeError:
            print("Warning: Data file is invalid.")
            self.students = []

    # Save student records
    def save_students(self):

        with open(self.filename, "w") as file:
            data = [student.to_dict() for student in self.students]
            json.dump(data, file, indent=4)

    # Add student
    def add_student(self, student):

        if self.get_student_by_id(student.student_id):
            raise ValueError("Student ID already exists!")

        self.students.append(student)
        self.save_students()

    # Display all students
    def display_all_students(self):

        if not self.students:
            print("No student records found!")
            return

        for student in self.students:
            student.display()

    # Search student by ID
    def get_student_by_id(self, student_id):

        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    # Update student
    def update_student(self, student_id, name=None,
                       age=None, course=None, marks=None):

        student = self.get_student_by_id(student_id)

        if student is None:
            return False

        if name is not None:
            student.name = name

        if age is not None:
            student.age = age

        if course is not None:
            student.course = course

        if marks is not None:
            student.marks = marks

        self.save_students()
        return True

    # Delete student
    def delete_student(self, student_id):

        student = self.get_student_by_id(student_id)

        if student is None:
            return False

        self.students.remove(student)
        self.save_students()
        return True

    # Search by name
    def search_by_name(self, name):

        results = [
            student for student in self.students
            if name.lower() in student.name.lower()
        ]

        if not results:
            print("No matching students found!")
            return

        for student in results:
            student.display()

    # Sort students by marks
    def sort_by_marks(self):

        if not self.students:
            print("No student records found!")
            return

        sorted_students = sorted(
            self.students,
            key=lambda student: student.average,
            reverse=True
        )

        print("\nStudents sorted by highest average:")

        for student in sorted_students:
            student.display()

    # Calculate class average
    def class_average(self):

        if not self.students:
            print("No student records found!")
            return

        total = sum(student.average for student in self.students)

        average = total / len(self.students)

        print("Class Average:", round(average, 2))