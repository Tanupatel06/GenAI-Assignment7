class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print("Product:", self.name)

class Laptop(Product):
    def get_info(self):
        print("Laptop Details")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)

class Mobile(Product):
    def get_info(self):
        print("Mobile Details")
        print("Name:", self.name)
        print("Price:", self.price)
        print("Category:", self.category)

# Creating objects
l1 = Laptop("HP Laptop", 50000, "Computer")
m1 = Mobile("Samsung", 25000, "Smartphone")

# Polymorphism using loop
products = [l1, m1]

for p in products:
    p.get_info()
    print()