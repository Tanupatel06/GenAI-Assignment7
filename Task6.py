class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"Product({self.name}, {self.price}, {self.category})"

    def __add__(self, other):
        return self.price + other.price

# Creating two objects
p1 = Product("Laptop", 50000, "Electronics")
p2 = Product("Mobile", 20000, "Electronics")

# Using __str__()
print(p1)

# Using operator overloading
total = p1 + p2

print("Total Price:", total)