class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.__price = price
        self.category = category

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print("Price updated successfully")
        else:
            print("Invalid price")

    def get_info(self):
        print("Name:", self.name)
        print("Price:", self.__price)
        print("Category:", self.category)

# Creating object
p1 = Product("Laptop", 50000, "Electronics")

p1.get_info()

# Updating price
p1.set_price(55000)

# Getting updated price
print("Updated Price:", p1.get_price())