def creating(number, holder, balance, limit):
    account = {
        "number": number,
        "holder": holder,
        "balance": balance,
        "limit": limit
    }
    return account


def deposit(account, value):
    account["balance"] += value


def withdraw(account, value):
    account["balance"] -= value


def extract(account):
    print(f"Your balance is {account.balance}")
