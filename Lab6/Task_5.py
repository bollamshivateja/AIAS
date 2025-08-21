class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn: {amount}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

account = BankAccount()

while True:
    print("\nOptions: deposit, withdraw, balance, exit")
    choice = input("Enter your choice: ").lower()

    if choice == "deposit":
        amount = float(input("Enter amount to deposit: "))
        account.deposit(amount)
    elif choice == "withdraw":
        amount = float(input("Enter amount to withdraw: "))
        account.withdraw(amount)
    elif choice == "balance":
        account.check_balance()
    elif choice == "exit":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")