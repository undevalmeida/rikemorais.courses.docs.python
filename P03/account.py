class Account:

    def __init__(self, number, holder, balance, limit):
        print(f"Building the object {self}")
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit
        self.__bank_code = "001"

    def extract(self):
        print(f"The total balance is {self.__balance} from the holder {self.__holder}")

    def deposit(self, value):
        self.__balance += value

    def withdraw(self, value):
        if self.__release_loot(value):
            self.__balance -= value
        else:
            print(f"Amount {value} has exceeded your withdrawal limit.")

    def __release_loot(self, withdrawal_amount):
        available_value = self.__balance + self.__limit
        return withdrawal_amount <= available_value

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

    @staticmethod
    def bank_code():
        return "001"

    @staticmethod
    def bank_codes():
        return {
            'BB': '001',
            'Caixa': '104',
            'Bradesco': '237'
        }
