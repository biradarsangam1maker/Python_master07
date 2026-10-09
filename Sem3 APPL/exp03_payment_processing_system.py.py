from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Processing Credit Card Payment of ₹{amount}"

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Processing Bitcoin Payment of ₹{amount}"

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Processing PayPal Payment of ₹{amount}"

class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        return f"Processing UPI Payment of ₹{amount}"

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        return self.strategy.pay(amount)

# Main Program
processor = PaymentProcessor(CreditCardPayment())

while True:
    print("\n1. Credit Card")
    print("2. Bitcoin")
    print("3. PayPal")
    print("4. UPI")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank You!")
        break

    amount = float(input("Enter Amount: "))

    if choice == 1:
        processor.set_strategy(CreditCardPayment())
    elif choice == 2:
        processor.set_strategy(BitcoinPayment())
    elif choice == 3:
        processor.set_strategy(PayPalPayment())
    elif choice == 4:
        processor.set_strategy(UPIPayment())
    else:
        print("Invalid Choice")
        continue

    print(processor.process_payment(amount))