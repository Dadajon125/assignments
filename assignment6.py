def track_change(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[STOCK] {result}")
        return result
    return wrapper

class Medicine:
    _all_medicines = []
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        Medicine._all_medicines.append(self)

    @track_change
    def receive(self, amount):
        self.quantity += amount
        return f"{self.name}: received {amount}, now {self.quantity}"
    
    @track_change
    def dispense(self, amount):
        if amount > self.quantity:
            return f"Not enough {self.name} available"
        self.quantity -= amount
        return f"{self.name}: dispensed {amount}, now {self.quantity}"
    
    def total_value(self):
        return float(round(self.price * self.quantity, 2))
    
    @classmethod
    def from_supplier(cls, entry):
        name, price, quantity = entry.split(":")
        return cls(name, float(price), int(quantity))
    
    @staticmethod
    def is_valid_code(code):
        if not isinstance(code, str):
            return False
        if code[:4] != "MED-":
            return False
        return code[4:].isdigit()
    
    @classmethod
    def pharmacy_value(cls):
            total = sum(d.total_value() for d in cls._all_medicines)
            return float(round(total, 2))
    
m1 = Medicine("Paracetamol", 8.75, 50)
m2 = Medicine.from_supplier("Ibuprofen:12.30:30")

m1.receive(20)
m1.dispense(45)
m1.dispense(100)
m2.dispense(10)

print(f"{m1.name}: value = ${m1.total_value()}")
print(f"{m2.name}: value = ${m2.total_value()}")

print(f"Valid code 'MED-045': {Medicine.is_valid_code('MED-045')}")
print(f"Valid code 'RX-100': {Medicine.is_valid_code('RX-100')}")
print(f"Pharmacy total: ${Medicine.pharmacy_value()}")