class Account:

    def __init__(self, number, holder, balance, limit):
        print(f"Building the object {self}")
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit

    def extract(self):
        print(f"The total balance is {self.balance} from the holder {self.holder}")

    def deposit(self, value):
        self.balance += value

    def withdraw(self, value):
        self.balance -= value
