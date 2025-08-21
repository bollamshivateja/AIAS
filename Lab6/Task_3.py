def classify_age(age):
    if age >= 0:  # valid age
        if age < 13:
            print("Child")
        elif age < 20:
            print("Teenager")
        elif age < 60:
            print("Adult")
        else:
            print("Senior Citizen")
    else:
        print("Invalid age")


# Example usage
age = int(input("Enter your age: "))
classify_age(age)