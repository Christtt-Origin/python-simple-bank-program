class Account:

    accounts = []

    def __init__(self, account_id, account_name):
        self.account_id = account_id
        self.account_name = account_name

    @staticmethod
    def new_account():
        account_id = input("Enter account ID: ")
        if any(char.isalpha() for char in account_id):
            print("Invalid input, can only contain digits!")
        account_name = input("Enter account name: ")
        account = Account(account_id, account_name)
        Account.accounts.append(account)

    @staticmethod
    def verify_account():
        account_id = input("Enter account ID to verify: ")

        if any(char.isalpha() for char in account_id):
            print("Invalid input, can only contain digits!")

        for account in Account.accounts:
            if account.account_id == account_id:
                print(f"Account ID: {account.account_id}\nAccount Name: {account.account_name}")
                print("Account verified successfully.")
                return account
            print("Account not found!")

    @staticmethod
    def quit():
        print("Exiting the program.")
        print("Thank you for using the program!")
        quit()
