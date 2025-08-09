def register_user(users_db):
    print("=== Register User ===")
    username = input("Enter a new username: ").strip()
    if username in users_db:
        print("Username already exists. Please try a different one.")
        return False
    password = input("Enter a new password: ").strip()
    users_db[username] = password
    print("Registration successful!")
    return True

def login_user(users_db):
    print("=== Login User ===")
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    if users_db.get(username) == password:
        print("Login successful! Welcome,", username)
        return True
    else:
        print("Invalid username or password.")
        return False

# Example usage:
if __name__ == "__main__":
    users_db = {}
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            register_user(users_db)
        elif choice == "2":
            login_user(users_db)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")
