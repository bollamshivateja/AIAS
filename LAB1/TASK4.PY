class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self.roll_number}")
        print(f"Marks: {self.marks}")

# Read student details from user
name = input("Enter student's name: ")
roll_number = input("Enter roll number: ")
marks = float(input("Enter marks: "))

student = Student(name, roll_number, marks)
student.display_details()