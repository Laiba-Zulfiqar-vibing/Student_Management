# -----------------------------
# Student class definition
# -----------------------------
class Student:
    def __init__(self, student_id, name, grade, marks):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.marks = marks

    def display_student_info(self):
        print(f"ID: {self.student_id}, Name: {self.name}, Grade: {self.grade}, Marks: {self.marks}")

    def check_pass(self):
        return self.marks >= 40

    def update_marks(self, change):
        self.marks += change


# -----------------------------
# Teacher class definition
# -----------------------------
class Teacher:
    def __init__(self, teacher_id, name):
        self.teacher_id = teacher_id
        self.name = name
        self.assigned_students = []

    def assign_student(self, student):
        if student.check_pass():
            if student not in self.assigned_students:
                self.assigned_students.append(student)
                print(f"{self.name} assigned '{student.name}'")
            else:
                print(f"'{student.name}' is already assigned to {self.name}.")
        else:
            print(f"'{student.name}' has failed, cannot be assigned.")

    def remove_student(self, student):
        if student in self.assigned_students:
            self.assigned_students.remove(student)
            print(f"{self.name} removed '{student.name}'")
        else:
            print(f"{self.name} does not have '{student.name}' assigned.")


# -----------------------------
# School class definition
# -----------------------------
class School:
    def __init__(self):
        self.students = [
            Student(1, "Zamin", "11th", 84),
            Student(2, "Saira", "12th", 87),
            Student(3, "Manahil", "11th", 75),
            Student(4, "Zahra", "10th", 90)
        ]
        self.teachers = [Teacher(1, "Mam Iqra")]

    def add_student(self, student):
        self.students.append(student)
        print(f"Student '{student.name}' added successfully!")

    def list_students(self):
        if not self.students:
            print("No students available.")
        else:
            for student in self.students:
                student.display_student_info()

    def search_student_by_name(self, name):
        return [s for s in self.students if name.lower() in s.name.lower()]

    def register_teacher(self, teacher):
        if any(t.teacher_id == teacher.teacher_id for t in self.teachers):
            print("Teacher ID already exists!")
        else:
            self.teachers.append(teacher)
            print(f"Teacher {teacher.name} registered successfully!")

    def assign_student(self, teacher_id, student_id):
        teacher = next((t for t in self.teachers if t.teacher_id == teacher_id), None)
        student = next((s for s in self.students if s.student_id == student_id), None)
        if teacher and student:
            teacher.assign_student(student)
        else:
            print("Invalid Teacher ID or Student ID.")

    def remove_student(self, teacher_id, student_id):
        teacher = next((t for t in self.teachers if t.teacher_id == teacher_id), None)
        student = next((s for s in self.students if s.student_id == student_id), None)
        if teacher and student:
            teacher.remove_student(student)
        else:
            print("Invalid Teacher ID or Student ID.")


# -----------------------------
# Main Program
# -----------------------------
def main():
    school = School()

    while True:
        print("\n===== Student Record Management System =====")
        print("1. View All Students")
        print("2. Add Student")
        print("3. Search Student by Name")
        print("4. Register Teacher")
        print("5. Assign Student")
        print("6. Remove Student")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            school.list_students()

        elif choice == '2':
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Name: ")
            grade = input("Enter Grade: ")
            marks = int(input("Enter Marks: "))
            school.add_student(Student(student_id, name, grade, marks))

        elif choice == '3':
            name = input("Enter Name to Search: ")
            results = school.search_student_by_name(name)
            if results:
                for s in results:
                    s.display_student_info()
            else:
                print("No matching students found.")

        elif choice == '4':
            teacher_id = int(input("Enter Teacher ID: "))
            name = input("Enter Teacher Name: ")
            school.register_teacher(Teacher(teacher_id, name))

        elif choice == '5':
            teacher_id = int(input("Enter Teacher ID: "))
            student_id = int(input("Enter Student ID to Assign: "))
            school.assign_student(teacher_id, student_id)

        elif choice == '6':
            teacher_id = int(input("Enter Teacher ID: "))
            student_id = int(input("Enter Student ID to Remove: "))
            school.remove_student(teacher_id, student_id)

        elif choice == '7':
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice! Try again.")


if __name__ == "__main__":
    main()
