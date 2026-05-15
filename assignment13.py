from abc import ABC,abstractmethod
class Order(ABC):
    def __init__(self,customer):
        self.customer = customer
    @abstractmethod
    def fee(self):
        pass

class Near(Order):
    def fee(self):
        return 5_000
    
class City(Order):
    def fee(self):
        return 12_000

class Outskirts(Order):
    def fee(self):
        return 25_000
    
class Archive(ABC):
    @abstractmethod
    def store(self, deliveries):
        pass

class FileArchive(Archive):
    def store(self,deliveries):
        for order in deliveries:
            print (f"ARCHIVE | {order.customer} | {order.fee()}")

class Dispatcher:
    @abstractmethod
    def call(self,deliveries):
        pass

class PhoneDispatcher(Dispatcher):
    def call(self,deliveries):
        for order in deliveries:
            print (f"[CALL → {order.customer}] Courier dispatched, fee {order.fee()} AUD")

class DeliveryService:
    def __init__(self):
        self.deliveries = []
    def add(self, order):
        self.deliveries.append(order)
    def run(self, archive, dispatcher):
        archive.store(self.deliveries)
        dispatcher.call(self.deliveries)

service = DeliveryService()
service.add(Near("Sam"))
service.add(City("Gimli"))
service.add(Outskirts("Gandalf"))

service.run(FileArchive(), PhoneDispatcher())
