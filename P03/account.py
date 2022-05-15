class Account:

    def __init__(self, number, holder, balance, limit):
        print(f"Building the object {self}")
        self.number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit
