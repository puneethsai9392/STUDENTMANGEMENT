class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.marks = []
        self.attendance = set()

    def update_marks(self, subject_marks):
        self.marks = subject_marks
        print(f"Marks updated successfully for {self.name}!")

    def mark_attendance(self, date):
        self.attendance.add(date)
        print(f"Attendance marked for {self.name} on {date}.")

    def view_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Attendance Dates: {self.attendance}")


class StudentManagementSystem:
    def __init__(self):
        self.students = {}

    def add_student(self, name, roll_number):
        if roll_number in self.students:
            print("Student with this roll number already exists.")
        else:
            student = Student(name, roll_number)
            self.students[roll_number] = student
            print("Student added successfully!")

    def delete_student(self, roll_number):
        if roll_number in self.students:
            del self.students[roll_number]
            print("Student data deleted successfully!")
        else:
            print("Student with this roll number does not exist.")

    def view_student_details(self, roll_number):
        if roll_number in self.students:
            self.students[roll_number].view_details()
        else:
            print("Student with this roll number does not exist.")

    def update_marks(self, roll_number, subject_marks):
        if roll_number in self.students:
            self.students[roll_number].update_marks(subject_marks)
        else:
            print("Student with this roll number does not exist.")

    def mark_attendance(self, roll_number, date):
        if roll_number in self.students:
            self.students[roll_number].mark_attendance(date)
        else:
            print("Student with this roll number does not exist.")


# Main Menu
if __name__ == "__main__":
    system = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Marks")
        print("3. Mark Attendance")
        print("4. View Student Details")
        print("5. Delete a Student Record")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            roll_number = input("Enter roll number: ")
            system.add_student(name, roll_number)

        elif choice == '2':
            roll_number = input("Enter roll number: ")
            subject_marks = list(map(int, input("Enter marks for subjects separated by spaces: ").split()))
            system.update_marks(roll_number, subject_marks)

        elif choice == '3':
            roll_number = input("Enter roll number: ")
            date = input("Enter attendance date (YYYY-MM-DD): ")
            system.mark_attendance(roll_number, date)

        elif choice == '4':
            roll_number = input("Enter roll number: ")
            system.view_student_details(roll_number)

        elif choice == '5':
            roll_number = input("Enter roll number: ")
            system.delete_student(roll_number)

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")
