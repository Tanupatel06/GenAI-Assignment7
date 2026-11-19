class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)

    def __add__(self, other):
        return self.price + other.price

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product added successfully!")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print("Product removed successfully!")
                return

        print("Product not found!")

    def get_total_value(self):
        total = 0

        for product in self.products:
            total = total + product.price

        return total

    def show_all_products(self):
        for product in self.products:
            product.get_info()
            print()

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()

    def add_new_product(self):
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        category = input("Enter product category: ")

        p = Product(name, price, category)

        self.inventory.add_product(p)

    def show_summary(self):
        print("\nStore Name:", self.store_name)

        print("Total Products:",
              len(self.inventory.products))

        print("Total Inventory Value:",
              self.inventory.get_total_value())

# Creating Store object
store = Store("Electronics Store")

# Adding three products
store.add_new_product()
store.add_new_product()
store.add_new_product()

# Displaying all products
print("\nAll Products:")
store.inventory.show_all_products()

# Displaying summary
store.show_summary()

# Testing product removal
store.inventory.remove_product("Mobile")

# Updated summary
store.show_summary()

# Testing operator overloading
p1 = Product("Laptop", 50000, "Electronics")
p2 = Product("Mobile", 20000, "Electronics")

print("Combined Price:", p1 + p2)