from Inventory import Inventory
from Account import Account


class Product:

    @staticmethod
    def start_program():
        while True:
            print("=" * 20)
            print("1. create account")
            print("2. verify")
            print("3. quit")
            print("=" * 20)
            user = input("Choose an option (1-3): ")
            match user:
                case "1":
                    Account.new_account()
                case "2":
                    account = Account.verify_account()
                    if account:
                        Product.dashboard(account)
                case "3":
                    Account.quit()
                case _:
                    print("Invalid choice!")

    @staticmethod
    def dashboard(account):
        while True:
            print("=" * 20)
            print("1. Register Product")
            print("2. Delete Product")
            print("3. View Product")
            print("4. Check Product")
            print("5. Quit")
            print("=" * 20)
            user = input("Choose an option (1-5): ")
            match user:
                case "1":
                    Product.register(account)
                case "2":
                    Product.delete_product(account)
                case "3":
                    Product.view_product(account)
                case "4":
                    Product.check_product(account)
                case "5":
                    Product.quit(account)
                case _:
                    print("Invalid choice!")

    @staticmethod
    def register(account):
        account_name = Account.accounts
        name = input("Enter product name: ").lower()
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        product = Inventory(name, price, quantity, account_name)

        Inventory.products.append(product)

    @staticmethod
    def delete_product(account):
        uid = int(input("Enter product UID to delete: "))
        for product in Inventory.products:
            if product.uid != uid:
                print(f"Product with UID {uid} not found.")
                break

            Inventory.products.remove(product)
            print(f"Product with UID {uid} deleted successfully.")

    @staticmethod
    def view_product(account):
        print("=" * 60)
        print(f"{'No':<5}{'Name':<10}{'Price':<10}{'Quantity':<10}{'UID':<10}")
        print("=" * 60)
        for i, item in enumerate(Inventory.products, start=1):
            print(
                f"{i:<5}"
                f"{item.name:<10}"
                f"{item.price:<10}"
                f"{item.quality:<10}"
                f"{item.uid:<10}"
            )
            print("-" * 50)
        print("=" * 50)

    @staticmethod
    def check_product(account):
        name = int(input("Searching product: ").lower())
        for product in Inventory.products:
            if product.name != name:
                print(f"Product of {name} not found.")
                break

            print("=" * 20)
            print(f"Found Item: {product.name}")
            print(f"Price: {product.price}")
            print(f"Quantity: {product.quantity}")
            print(f"UID: {product.uid}")
            print("=" * 20)

    @staticmethod
    def quit(account):
        print("You quitted!")
        quit()
