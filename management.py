import csv
import os

# Define global variables
student_fields = ['roll', 'name', 'age', 'email', 'phone']
student_database = 'students.csv'

# Ensure the CSV file exists
if not os.path.exists(student_database):
    with open(student_database, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(student_fields)

def display_menu():
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

def add_student():
    print("\nAdd New Student")
    student_data = []
    for field in student_fields:
        value = input(f"Enter {field}: ")
        student_data.append(value)
    with open(student_database, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(student_data)
    print("Student added successfully.")

def view_students():
    print("\nStudent Records:")
    with open(student_database, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(", ".join(row))

def update_student():
    roll = input("\nEnter roll number of student to update: ")
    updated_data = []
    with open(student_database, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == roll:
                print(f"Updating record for {row[1]}")
                for i, field in enumerate(student_fields):
                    value = input(f"Enter new {field} (leave blank to keep '{row[i]}'): ")
                    updated_data.append(value if value else row[i])
                row = updated_data
            with open(student_database, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(row)
    print("Student updated successfully.")

def delete_student():
    roll = input("\nEnter roll number of student to delete: ")
    rows = []
    with open(student_database, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = [row for row in reader if row[0] != roll]
    with open(student_database, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    print("Student deleted successfully.")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        print("Exiting system.")
        break
    else:
        print("Invalid choice. Please try again.")
