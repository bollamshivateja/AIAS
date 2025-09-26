def cm_to_inches(cm):
    """
    Convert centimeters to inches.

    Parameters:
        cm (float): The length in centimeters.

    Returns:
        float: The length in inches.
    """
    return cm * 0.39

def main():
    print("=== Centimeter to Inches Converter ===")
    try:
        cm = float(input("Enter length in centimeters: "))
        inches = cm_to_inches(cm)
        print(f"{cm} cm is equal to {inches:.2f} inches.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

if __name__ == "__main__":
    main()
