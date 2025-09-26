def is_leap_year(year):
    """
    Check if a given year is a leap year.

    Parameters:
        year (int): The year to check.

    Returns:
        bool: True if leap year, False otherwise.
    """
    if (year % 4 == 0):
        if (year % 100 != 0) or (year % 400 == 0):
            return True
    return False

def main():
    try:
        year = int(input("Enter a year: "))
        if is_leap_year(year):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    except ValueError:
        print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    main()
