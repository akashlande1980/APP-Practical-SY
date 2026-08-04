class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal")

class PaymentContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)
credit = CreditCardPayment()
payment = PaymentContext(credit)
payment.pay(1000)

paypal = PayPalPayment()
payment.set_strategy(paypal)
payment.pay(500)

print("======== Payment Processing System ======")
amount = float(input("Enter amount: "))
print("Select Payment Method")
print("1. Credit Card")
print("2. PayPal")

choice = int(input("Enter your choice: "))

if choice == 1:
    strategy = CreditCardPayment()
elif choice == 2:
    strategy = PayPalPayment()
else:
    print("Invalid Choice")
    exit()

payment = PaymentContext(strategy)
payment.pay(amount)
