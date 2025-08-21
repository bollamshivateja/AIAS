# Define the Student class
class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = int(marks)  # Convert marks to integer
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 75:
            return 'B'
        elif self.marks >= 60:
            return 'C'
        else:
            return 'Fail'

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_number}")
        print(f"Marks: {self.marks}")
        print(f"Grade: {self.grade}")

# Read data from console
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = input("Enter marks: ")

# Create Student object and display details
student = Student(name, roll_no, marks)
student.display_details()