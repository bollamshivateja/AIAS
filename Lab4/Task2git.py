def cm_to_inches(cm):
    return cm * 0.39370

if __name__ == "__main__":
    try:
        cm = float(input("Enter length in centimeters: "))
        inches = cm_to_inches(cm)
        print(f"{cm} cm = {inches:.5f} inches")
    except ValueError:
        print("Please enter a valid number.")