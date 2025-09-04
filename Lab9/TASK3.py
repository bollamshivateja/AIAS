def add(x, y):  # Add two numbers
    return x + y  # Return the sum

def subtract(x, y):  # Subtract second number from first
    return x - y  # Return the difference

def multiply(x, y):  # Multiply two numbers
    return x * y  # Return the product

def divide(x, y):  # Divide first number by second
    if y == 0:  # Check for division by zero
        return "Cannot divide by zero."  # Return error message
    return x / y  # Return the quotient


def calculator():
    """
    Displays a simple calculator interface in the console, allowing the user to choose an arithmetic operation
    (Add, Subtract, Multiply, Divide) and input two numbers. Performs the selected operation and prints the result.
    Handles invalid numeric input and invalid operation choices.
    Raises:
        ValueError: If the user inputs non-numeric values for the numbers.
    """
    print("Simple Calculator")
    print("Choose operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = input("Enter choice (1/2/3/4): ").strip()  # Get operation choice from user
        num1 = float(input("Enter first number: "))  # Get first number and convert to float
        num2 = float(input("Enter second number: "))  # Get second number and convert to float

        if choice == '1':  # Addition
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':  # Subtraction
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':  # Multiplication
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':  # Division
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")  # Handle invalid operation choice

    except ValueError:
        print("Invalid input. Please enter numeric values.")  # Handle non-numeric input error


while True:  # Main loop to keep calculator running
    calculator()  # Run calculator function
    cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()  # Ask user to continue
    if cont != 'yes':  # Exit if user does not want to continue
        print("Exiting calculator. Have a great day!")  # Exit message
        break  # Break the loop to end program