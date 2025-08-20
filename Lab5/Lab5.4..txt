import getpass

def collect_user_data():
    """
    Collects user data (name, age, email) with password protection.
    The password input is hidden for security.
    The email is masked when displaying the collected data.
    """
    # Prompt for password (input is hidden)
    password = getpass.getpass("Enter password to protect your data: ")

    # Collect user details
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")

    # Mask the email (hide the part before '@')
    def mask_email(email):
        at_index = email.find('@')
        if at_index <= 1:
            return '*' * at_index + email[at_index:]
        else:
            return '*' * at_index + email[at_index:]

    masked_email = mask_email(email)

    # Display collected data with masked email
    print("\nCollected Data:")
    print(f"Name : {name}")
    print(f"Age  : {age}")
    print(f"Email: {masked_email}")

# Run the function if this file is executed directly
if __name__ == "__main__":
    collect_user_data()