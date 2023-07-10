"""
-------------------------------------------------------------------------------
INTERFACE SEGREGATION principle
-------------------------------------------------------------------------------

Make interfaces (parent abstract classes) more specific, rather than
generic.

e.g. Create more interfaces (classes) if needed and/or provide objects to
constructors
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


class SmsAuto:
    authorized = False

    def verify_code(self, code):
        print(f"Verifying code: {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: SmsAuto):
        self.security_code = security_code
        self.authorizer = authorizer

    def auto_sms(self, code):
        print(f"Cod verificat! {code}")

    def pay(self, security_code, order):

        if not self.authorizer.is_authorized():
            raise Exception("Cod neverificat!")

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
    def __init__(self, email_address, authorizer: SmsAuto):
        self.email_address = email_address
        self.authorizer = authorizer

    def auto_sms(selfself, code):
        print(f"Cod verificat! {code}")

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Cod neverificat")

        print("Processing PayPal payment type")
        print(f"Verifying email_address: {self.email_address}")
        order.status = "paid"

order = Order()
order.add_item("Jeans", 1, 100)
order.add_item("Shirt", 2, 80)
print(f"The status of the order is: {order.status}" )

print(f"The total price is: {order.total_price()}")
sms_verif = SmsAuto()
sms_verif.verify_code("2235")
processor = DebitPaymentProcessor("123456", sms_verif)
processor.pay(order)
print(f"Order status is: {order.status}")