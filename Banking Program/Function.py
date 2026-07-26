def decoration():
    print("=================================")


def history_deposit(account, amount):
    account.history.append({
        "Type": "Deposit",
        "To": "-",
        "Amount": amount,
        "Balance": int(account.balance)
    })


def history_withdraw(account, amount):
    account.history.append({
        "Type": "Withdraw",
        "To": "-",
        "Amount": amount,
        "Balance": int(account.balance)
    })


def history_transaction(account, amount):
    account.history.append({
        "Type": "Transfer",
        "To": target.username,
        "Amount": amount,
        "Balance": int(account.balance)
    })
