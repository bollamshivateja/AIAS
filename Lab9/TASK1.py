def sum_even_odd_from_input():
    """
    Prompts the user to enter a sequence of integers separated by spaces.
    Calculates and prints the sum of even and odd numbers separately.
    If the input contains non-integer values, an error message is displayed.

    Steps:
        1. User enters numbers separated by spaces (e.g., "1 2 3 4 5").
        2. The input is split and converted to integers.
        3. The sum of even and odd numbers is calculated and printed.
        4. If any input is not an integer, an error message is shown.
    Returns:
        None
    """
    try:
        user_input = input("Enter numbers separated by spaces: ")  # Prompt user for input
        numbers = list(map(int, user_input.strip().split()))  # Convert input string to list of integers

        even_sum = sum(num for num in numbers if num % 2 == 0)  # Calculate sum of even numbers
        odd_sum = sum(num for num in numbers if num % 2 != 0)  # Calculate sum of odd numbers

        print(f"Sum of even numbers: {even_sum}")  # Print sum of even numbers
        print(f"Sum of odd numbers: {odd_sum}")  # Print sum of odd numbers
    except ValueError:
        print("Please enter only integers separated by spaces.")  # Handle non-integer input error

sum_even_odd_from_input()  # Call the function to execute the logic