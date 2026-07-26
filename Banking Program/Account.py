from Function import decoration


class Account:

    accounts = {}
    next_uid = 100000

    def __init__(self, full_name, username, password):
        self.full_name = full_name
        self.username = username
        self.password = password

        self.uid = Account.next_uid
        Account.next_uid += 1
        self.history = []
        self.balance = 0

    @staticmethod
    def valid_username():

        while True:
            username = input("Create username: ").lower()
            if not username:
                print("Username required!")
            elif len(username) <= 3:
                print("Username too short!")
            elif any(char.isdigit() for char in username):
                print("Username can't have digits!")
            else:
                return username

    @staticmethod
    def valid_password():

        while True:
            password = input("Create password: ")
            if not password:
                print("Password required!")
            elif len(password) <= 3:
                print("Password too short!")
            else:
                return password

    @staticmethod
    def register():

        full_name = input("Enter full name: ").capitalize()
        if not full_name:
            decoration()
            print("Full name required!")
        elif any(char.isdigit() for char in full_name):
            decoration()
            print("Your full name can't have numbers!")

        username = Account.valid_username()
        password = Account.valid_password()

        if username and password:
            new_account = Account(full_name, username, password)
            Account.accounts[username] = new_account
            decoration()
            print("Successfully registered!")
            return full_name
        else:
            decoration()
            print("Something went wrong!")

    @staticmethod
    def login():

        username = input("Enter username: ").lower()
        password = input("Enter password: ")

        if username in Account.accounts:
            account = Account.accounts.get(username)
            if account and account.password == password:
                return account
            else:
                decoration()
                print("Username or password is wrong!")
                return
        else:
            decoration()
            print("Username does not exists")
            return

    @staticmethod
    def quit():
        decoration()
        print("Thanks for using this program!")
        exit()
