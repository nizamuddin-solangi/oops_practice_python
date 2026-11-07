class RegularCustomer:
    def final_price(self, amount):
        if amount < 0:
            print("Bill amount cannot be negative.")
            return None
        return amount * 0.95


class PremiumCustomer:
    def final_price(self, amount):
        if amount < 0:
            print("Bill amount cannot be negative.")
            return None
        return amount * 0.90


class VIPCustomer:
    def final_price(self, amount):
        if amount < 0:
            print("Bill amount cannot be negative.")
            return None
        return amount * 0.80


class GoldCustomer:
    def final_price(self, amount):
        if amount < 0:
            print("Bill amount cannot be negative.")
            return None
        return amount * 0.85


def print_receipt(customer, amount):
    price = customer.final_price(amount)
    if price is not None:
        print(customer.__class__.__name__, "final bill: Rs.", price)


bill = 10000
print_receipt(RegularCustomer(), bill)
print_receipt(PremiumCustomer(), bill)
print_receipt(VIPCustomer(), bill)
print_receipt(GoldCustomer(), bill)
print_receipt(RegularCustomer(), -500)
