class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive value.")
        else:
            print("Insufficient funds for withdrawal.")

    def check_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")

if __name__ == "__main__":
    print("Welcome to the Basic Banking System!")

    # Create a bank account
    account_holder = input("Enter your name: ")
    initial_balance = float(input("Enter initial balance (default is 0): ") or 0)
    user_account = BankAccount(account_holder, initial_balance)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            deposit_amount = float(input("Enter the deposit amount: "))
            user_account.deposit(deposit_amount)
        elif choice == "2":
            withdrawal_amount = float(input("Enter the withdrawal amount: "))
            user_account.withdraw(withdrawal_amount)
        elif choice == "3":
            user_account.check_balance()
        elif choice == "4":
            print("Exiting the Basic Banking System. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
