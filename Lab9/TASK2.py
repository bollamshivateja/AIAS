class SRU_Student:
    """
    SRU_Student represents a student at SRU with attributes for name, roll number, hostel status, and fee management.
    Attributes:
        name (str): The name of the student.
        roll_no (str/int): The roll number of the student.
        hostel_status (str): Indicates if the student is a hostel resident.
        fee (int/float): The total fee paid by the student.
    Methods:
        _init_(name, roll_no, hostel_status):
            Initializes a new SRU_Student instance with the given name, roll number, and hostel status.
        fee_update(amount):
            Updates the student's fee by adding the specified amount.
            Prints an error message if the amount is negative.
        display_details():
            Displays the student's details including name, roll number, hostel status, and total fee paid.
    """
    def _init_(self, name, roll_no, hostel_status):  # Initialize student attributes
        self.name = name  # Student's name
        self.roll_no = roll_no  # Student's roll number
        self.hostel_status = hostel_status  # Hostel status (Yes/No)
        self.fee = 0  # Initial fee paid is set to 0

    def fee_update(self, amount):  # Update the student's fee
        if amount < 0:  # Check if the amount is negative
            print("Fee amount cannot be negative.")  # Print error for negative amount
        else:
            self.fee += amount  # Add amount to total fee
            print(f"Fee updated. Current total fee: {self.fee}")  # Print updated fee

    def display_details(self):  # Display all student details
        print("\n ----- Student Details -----")  # Header
        print(f"Name         : {self.name}")  # Print student's name
        print(f"Roll No.     : {self.roll_no}")  # Print student's roll number
        print(f"Hostel Status: {self.hostel_status}")  # Print hostel status
        print(f"Total Fee Paid : {self.fee}")  # Print total fee paid
        print("-----------------------------\n")  # Footer


# Taking input
name = input("Enter student name: ")  # Get student's name from user
roll_no = input("Enter roll number: ")  # Get student's roll number from user
hostel_status = input("Hostel status (Yes/No): ")  # Get hostel status from user

student = SRU_Student(name, roll_no, hostel_status)  # Create SRU_Student object with user input

try:
    fee_amount = float(input("Enter fee amount to update: "))  # Get fee amount from user and convert to float
    student.fee_update(fee_amount)  # Update fee for the student
except ValueError:
    print("Invalid input. Please enter a numeric fee amount.")  # Handle non-numeric input error

student.display_details()  # Display all details of the student
