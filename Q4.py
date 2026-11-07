class Vehicle:
    def __init__(self, brand, model, daily_rate):
        self.brand = brand
        self.model = model
        self.daily_rate = daily_rate

    def calculate_rent(self, days):
        if days <= 0:
            print("Days must be greater than zero.")
            return None
        return self.daily_rate * days


class Car(Vehicle):
    def calculate_rent(self, days):
        rent = super().calculate_rent(days)
        if rent is not None:
            return rent + 1000


class Bike(Vehicle):
    def calculate_rent(self, days):
        rent = super().calculate_rent(days)
        if rent is not None:
            return rent * 0.90


car = Car("Toyota", "Corolla", 5000)
bike = Bike("Honda", "CD 70", 1000)

print("Car rent for 3 days: Rs.", car.calculate_rent(3))
print("Bike rent for 3 days: Rs.", bike.calculate_rent(3))
car.calculate_rent(0)
