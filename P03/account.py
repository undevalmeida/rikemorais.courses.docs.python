class Account:

    def __init__(self, number, holder, balance, limit):
        print(f"Building the object {self}")
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def extract(self):
        print(f"The total balance is {self.__balance} from the holder {self.__holder}")

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        self.__balance -= value

    def transfer(self, value, receiver):
        self.withdraw(value)
        receiver.deposit(value)

    @property
    def balance(self):
        return self.__balance

    @property
    def holder(self):
        return self.__holder

    @property
    def limit(self):
        return self.__limit

    @limit.setter
    def limit(self, limit):
        self.__limit = limit
