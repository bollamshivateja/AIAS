def main():
    # Take input from the user as a string of numbers separated by spaces
    user_input = input("Enter numbers separated by spaces: ")
    # Split the input string into a list of strings
    num_list_str = user_input.strip().split()
    # Convert the list of strings to a list of integers
    try:
        num_list = [int(num) for num in num_list_str]
    except ValueError:
        print("Please enter valid integers only.")
        return
    # Sort the list using the built-in sorted() function
    sorted_list = sorted(num_list)
    # Output the sorted list
    print("Sorted numbers:", sorted_list)

if __name__ == "__main__":
    main()
