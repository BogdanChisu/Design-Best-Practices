"""
-------------------------------------------------------------------------------
SINGLE Responsibility principle
-------------------------------------------------------------------------------

Every module, class or function in a computer program should have responsibility
over a single part of that program's functionality, which it should encapsulate.

No other modules, classes or functions can be responsible for the same
functionality responsibility
"""

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


class PaymentProcessor:

    def pay_debit(self, security_code, order):
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

    def pay_credit(self, security_code, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = "paid"

order = Order()
order.add_item("Jeans", 1, 100)
order.add_item("Shirt", 2, 80)
print(f"The status of the order is: {order.status}" )

print(f"The total price is: {order.total_price()}")
# order.pay("debit", "06533")
processor = PaymentProcessor()
processor.pay_credit("12345", order)
print(f"The status of the order is: {order.status}")