class Inventory():

    products = []
    next_uid = 100

    def __init__(self, name, price, quantity, account_name):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.account_name = account_name

        self.uid = Inventory.next_uid
        Inventory.next_uid += 1

    @staticmethod
    def restock_product():
        name = input("Product name: ").lower()
        for product in Inventory.products:
            if product.name == name:
                quantity = int(input("Enter quantity: "))
                product.quantity += name if product.quantity > 0 else "Invalid amount"
                print(f"Added Stock: {quantity}")
                print(f"Total Stock: {product.quantity}")
                return

            print("Product not found!")

    @staticmethod
    def sell_product():
        name = input("Product name: ").lower()
        for product in Inventory.products:
            if product.name == name:
                quantity = int(input("Enter quantity: "))
                product.quantity -= name if product.quantity > 0 else "Invalid amount"
                print(f"Sold Stock: {quantity}")
                print(f"Left stock: {product.quantity}")
                return
            
            print("Product not found!")