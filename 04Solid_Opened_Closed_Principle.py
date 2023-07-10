"""
-------------------------------------------------------------------------------
OPENED/CLOSED principle
-------------------------------------------------------------------------------

Be able to add new functionality to existing code easily without modifying
existing code.

e.g. Use abstract classes. These can define what the subclasses will
require and strengthen Principle 1 by separating code duties
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

    def pay(self, security_code, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class DebitPaymentProcessor(PaymentProcessor):

    def pay(self, security_code, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

class PayPalPaymentProcessor(PaymentProcessor):

    def pay(self, security_code, order):
        print("Processing PayPal payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

order = Order()
order.add_item("Jeans", 1, 100)
order.add_item("Shirt", 2, 80)
print(f"The status of the order is: {order.status}" )

print(f"The total price is: {order.total_price()}")
# order.pay("debit", "06533")

processor = DebitPaymentProcessor()
processor.pay("12345", order)
print(f"The status of the order is: {order.status}")

p = PayPalPaymentProcessor()
p.pay("2323", order)