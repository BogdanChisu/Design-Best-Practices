"""
-------------------------------------------------------------------------------
LISKOV SUBSTITUTION principle
-------------------------------------------------------------------------------

When a class inherits from another class, the program shouldn't need to
hack anything to use the subclass.

e.g. Define constructor arguments to keep inheritance flexible.
"""

from abc import ABC, abstractmethod

class Order:
    items = []
    quantities = []
    prices = []
    status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append((quantity))
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, security_code, order):
        pass

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, security_code, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, security_code, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address):
        self.email_address = email_address

    def pay(self, order):
        print("Processing PayPal payment type")
        print(f"Verifying email_address: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Jeans", 1, 100)
order.add_item("Shirt", 2, 80)
print(f"The status of the order is: {order.status}" )

print(f"The total price is: {order.total_price()}")
# order.pay("debit", "06533")

processor = DebitPaymentProcessor("123456")
processor.pay("12345", order)
print(f"The status of the order is: {order.status}")

p = PayPalPaymentProcessor("bchisu@gmail.com")
p.pay(order)