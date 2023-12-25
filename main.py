class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Error: Balance cannot be negative.")
        else:
            self._balance = value
            print(f"Balance updated: {self._balance}")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited: {amount}")
            print(f"New Balance: {self._balance}")
        else:
            print("Error: Deposit amount should be greater than 0.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"Withdrew: {amount}")
            print(f"New Balance: {self._balance}")
        elif amount <= 0:
            print("Error: Withdrawal amount should be greater than 0.")
        else:
            print("Error: Insufficient funds.")


initial_balance = float(input("Enter initial balance for the bank account: "))
account = BankAccount(initial_balance)


deposit_amount = float(input("Enter the deposit amount: "))
account.deposit(deposit_amount)

withdraw_amount = float(input("Enter the withdrawal amount: "))
account.withdraw(withdraw_amount)

account.balance = -100
