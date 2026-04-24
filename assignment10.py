class PharmacyError(Exception):
    pass

class MedicineNotFoundError(PharmacyError):
    def __init__(self, medicine_name):
        self.medicine_name = medicine_name
        super().__init__(f"medicine not found: {medicine_name}")

class InsufficientSupplyError(PharmacyError):
    def __init__(self, medicine_name, requested, available):
        self.medicine_name = medicine_name
        self.requested = requested
        self.available = available
        self.shortage = requested - available
        super().__init__(
            f"cannot dispense {requested} of {medicine_name}: only {available} in stock, short by {self.shortage}"
        )

class InvalidQuantityError(PharmacyError):
    def __init__(self, quantity):
        self.quantity = quantity
        super().__init__(f"invalid quantity: {quantity}. must be positive")

class Pharmacy:
    def __init__(self):
        self.medicines = {}

    def add_medicine(self, name, price, quantity):
        if quantity <= 0:
            raise InvalidQuantityError(quantity)

        if name not in self.medicines:
            self.medicines[name] = {
                "price": price,
                "quantity": quantity
            }
        else:
            self.medicines[name]["price"] = price
            self.medicines[name]["quantity"] += quantity

    def dispense(self, name, quantity):
        if quantity <= 0:
            raise InvalidQuantityError(quantity)

        try:
            medicine = self.medicines[name]
        except KeyError:
            raise MedicineNotFoundError(name) from None

        if quantity > medicine["quantity"]:
            raise InsufficientSupplyError(name, quantity, medicine["quantity"])

        total = quantity * medicine["price"]
        medicine["quantity"] -= quantity
        return round(total, 2)

    def total_value(self):
        all_total = sum(med["price"] * med["quantity"] for med in self.medicines.values())
        return round(all_total, 2)
    
ph = Pharmacy()

ph.add_medicine("Aspirin", 5.99, 100)
ph.add_medicine("Insulin", 120.50, 30)
ph.add_medicine("Amoxicillin", 12.75, 60)

print(f"total value: {ph.total_value()}")

cost = ph.dispense("Insulin", 5)
print(f"dispensed 5 insulin for: {cost}")
print(f"total value: {ph.total_value()}")

ph.add_medicine("Aspirin", 6.49, 50)
print(f"total value: {ph.total_value()}")

tests = [
    lambda: ph.dispense("Vitamin D", 10),
    lambda: ph.dispense("Amoxicillin", 100),
    lambda: ph.add_medicine("Paracetamol", 3.99, -20),
]

for test in tests:
    try:
        test()
    except PharmacyError as e:
        print(e)