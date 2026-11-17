from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def process_payment(self, amount):
        print("Payment through Credit Card:", amount)

class UPIPayment(Payment):
    def process_payment(self, amount):
        print("Payment through UPI:", amount)

# Creating objects
p1 = CreditCardPayment()
p2 = UPIPayment()

# Calling methods
p1.process_payment(5000)
p2.process_payment(2000)