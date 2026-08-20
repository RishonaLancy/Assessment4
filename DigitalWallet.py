#1st
class DigitalWallet:
    def __init__(self, name, balance, daily_limit):
        self.name = name
        self.balance = balance
        self.daily_limit = daily_limit
        self.daily_total = 0
        self.transactions = []
        self.failed_pins = 0

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return
        self.balance += amount
        self.transactions.append(("Deposit", amount))
        print("Deposit successful:", amount)

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        if self.daily_total + amount > self.daily_limit:
            print("Daily transaction limit exceeded")
            return

        self.balance -= amount
        self.daily_total += amount
        self.transactions.append(("Withdrawal", amount))

        if amount > 50000:
            print("Suspicious transaction: Large amount")

        print("Withdrawal successful:", amount)

    def transfer(self, amount):
        if amount <= 0:
            print("Invalid transfer amount")
            return
        if amount > self.balance:
            print("Insufficient balance")
            return
        if self.daily_total + amount > self.daily_limit:
            print("Daily transaction limit exceeded")
            return

        self.balance -= amount
        self.daily_total += amount
        self.transactions.append(("Transfer", amount))

        if amount > 50000:
            print("Suspicious transaction: Large transfer")

        print("Transfer successful:", amount)

    def verify_balance(self):
        print("Current Balance:", self.balance)

    def history(self):
        print("\nTransaction History:")
        for t in self.transactions:
            print(t[0], ":", t[1])

    def failed_pin(self):
        self.failed_pins += 1
        if self.failed_pins >= 3:
            print("Suspicious transaction: Multiple failed PIN attempts")


wallet = DigitalWallet("Rishona", 100000, 100000)

print("Account created for:", wallet.name)

wallet.deposit(10000)
wallet.withdraw(15000)
wallet.transfer(20000)

wallet.failed_pin()
wallet.failed_pin()
wallet.failed_pin()

wallet.withdraw(60000)

wallet.verify_balance()
wallet.history()

