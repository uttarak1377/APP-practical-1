# Strategy Classes
class CreditCard:

    def pay(self):
        print("Payment made using Credit Card")


class DebitCard:

    def pay(self):
        print("Payment made using Debit Card")


class UPI:

    def pay(self):
        print("Payment made using UPI")


# Context Class
class Payment:

    def __init__ (self, strategy):
        self.strategy = strategy

    def process(self):
        self.strategy.pay()


# Main Program
print("Select Payment Method:")
print("1. Credit Card")
print("2. Debit Card")
print("3. UPI")

choice = int(input("Enter your choice: "))

if choice == 1:
    payment = Payment(CreditCard())
elif choice == 2:
    payment = Payment(DebitCard())
elif choice == 3:
    payment = Payment(UPI())
else:
    print("Invalid choice")
    exit()

payment.process()