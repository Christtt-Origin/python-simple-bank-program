from Account import Account
from Function import (decoration, history_deposit,
                      history_withdraw, history_transaction)


class Bank:

    @staticmethod
    def start_program():
        while True:
            print("========== PYTHON BANK ==========")
            print("1. Register")
            print("2. Login")
            print("3. Exit")
            decoration()
            user = input("Choose an option (1-3): ")
            match user:
                case "1":
                    Account.register()
                case "2":
                    account = Account.login()
                    if account:
                        Bank.main_menu(account)
                case "3":
                    Account.quit()
                case _:
                    print("Invalid choice")

    @staticmethod
    def main_menu(account):
        while True:
            print("=========== DASHBOARD ===========")
            print(f"Welcome, {account.full_name}\n")
            print(f"Account UID: {account.uid}")
            print(f"Balance: Rp{int(account.balance)}\n")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Transaction History")
            print("5. Logout")
            decoration()
            user = input("Choose an option (1-6): ")
            match user:
                case "1":
                    Bank.deposit(account)
                case "2":
                    Bank.withdraw(account)
                case "3":
                    Bank.transfer(account)
                case "4":
                    Bank.history(account)
                case "5":
                    Bank.logout()
                case _:
                    print("Invalid choice")

    @staticmethod
    def deposit(account):
        amount = int(input("Deposit: "))
        if amount < 0:
            decoration()
            print("Deposit balance can't be less then 0!")
            return

        account.balance += amount
        decoration()
        print(f"Deposit successful!\n Deposited: Rp{amount}")

        history_deposit(account, amount)

    @staticmethod
    def withdraw(account):
        amount = int(input("Withdraw: "))
        if amount < 0:
            decoration()
            print("Withdraw balance can't be less then 0!")
            return

        fee = amount * 10 / 100

        if amount + fee >= account.balance:
            account.balance -= amount

        account.balance -= (amount + fee)

        decoration()
        print(
            f"Withdraw successful!\nWithdrawed: Rp{amount}\nAfter Tax: Rp{int(account.balance)}")

        history_withdraw(account, amount)

    @staticmethod
    def transfer(account):
        uid = int(input("Enter account UID: "))

        target = None

        for acc in Account.accounts.values():
            if acc.uid == uid:
                target = acc
                break

        if target is None:
            decoration()
            print("Invalid UID!")
            return

        if target.uid == account.uid:
            decoration()
            print("No no no!")
            return

        decoration()
        print(f"Found user: {target.full_name} (@{target.username})")

        amount = int(input("Enter amount: "))
        if amount > account.balance:
            decoration()
            print("Not enough balance!")
            return

        if amount < 0:
            decoration()
            print("Invalid amount!")
            return

        decoration()
        print(f"Transferred: Rp{amount}")
        account.balance -= amount
        target.balance += amount

        history_transaction(account, target, amount)

    @staticmethod
    def history(account):
        print("=" * 60)
        print(f"{'No':<5}{'Type':<12}{'To':<15}{'Amount':<15}{'Balance':<15}")
        print("=" * 60)

        for i, transaction in enumerate(account.history, start=1):
            print(
                f"{i:<5}"
                f"{transaction['Type']:<12}"
                f"{transaction['To']:<15}"
                f"{transaction['Amount']:<15}"
                f"{transaction['Balance']:<15}"
            )
        print("=" * 60)

    @staticmethod
    def logout():
        decoration()
        print("You logged out!")
        Bank.start_program()
