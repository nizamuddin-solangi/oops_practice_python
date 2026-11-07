class BankAccount:
    def __init__(self, name, balance, pin):
        self.name = name
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Deposit must be greater than zero.")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Incorrect PIN.")
        elif amount <= 0 or amount > self.__balance:
            print("Invalid withdrawal amount.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def get_balance(self, pin):
        if pin == self.__pin:
            print("Balance: Rs.", self.__balance)
        else:
            print("Incorrect PIN.")


account = BankAccount("Ahmed", 5000, 1234)
account.deposit(2000)
account.withdraw(1500, 1234)
account.withdraw(10000, 1234)
account.withdraw(500, 9999)
account.get_balance(1234)

# Double underscores only hide the variable name. They are not real security.
