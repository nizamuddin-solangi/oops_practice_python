from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CardPayment(PaymentMethod):
    def pay(self, amount):
        if amount > 0:
            print("Card payment: Rs.", amount)
        else:
            print("Amount must be positive.")

    def refund(self, amount):
        if amount > 0:
            print("Card refund: Rs.", amount)
        else:
            print("Amount must be positive.")


class WalletPayment(PaymentMethod):
    def pay(self, amount):
        if amount > 0:
            print("Wallet payment: Rs.", amount)
        else:
            print("Amount must be positive.")

    def refund(self, amount):
        if amount > 0:
            print("Wallet refund: Rs.", amount)
        else:
            print("Amount must be positive.")


class BankTransferPayment(PaymentMethod):
    def pay(self, amount):
        if amount > 0:
            print("Bank transfer payment: Rs.", amount)
        else:
            print("Amount must be positive.")

    def refund(self, amount):
        if amount > 0:
            print("Bank transfer refund: Rs.", amount)
        else:
            print("Amount must be positive.")


class CashPayment(PaymentMethod):
    def pay(self, amount):
        if amount > 0:
            print("Cash payment: Rs.", amount)
        else:
            print("Amount must be positive.")

    def refund(self, amount):
        if amount > 0:
            print("Cash refund: Rs.", amount)
        else:
            print("Amount must be positive.")


def process_transaction(method, amount):
    method.pay(amount)


card = CardPayment()
wallet = WalletPayment()
bank = BankTransferPayment()
cash = CashPayment()
process_transaction(card, 2500)
process_transaction(wallet, 1500)
process_transaction(bank, 5000)
process_transaction(cash, 700)
card.refund(2500)
wallet.refund(-100)
