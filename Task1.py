class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        
    def get_info(self):
        print("Product Name :", self.name)
        print("Product Price :", self.price)
        print("Product Category :", self.category)
        
    def apply_discount(self, percent):
        return self.price - (self.price * percent / 100)
    
# Creating Object
p1 = Product("Laptop",120000,"Electronics")
p2 = Product("Mobile",100000,"Electronics")

# Display Product info
p1.get_info() 
p2.get_info()

# Apply Discount
print("Discounted Price :", p1.apply_discount(10))
print("Discounted Price :", p2.apply_discount(5))
            
        