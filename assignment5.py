from abc import ABC, abstractmethod

class Priceable(ABC):
    @abstractmethod
    def service_fee(self):
        pass

class Formattable(ABC):
    @abstractmethod
    def format_ticket(self):
        pass
class Ticket(Priceable, Formattable):
    def __init__(self, event, price):
        self.event = event
        self.price = price

        if self.price < 0:
            raise ValueError(f"Invalid price: {self.price}")

    def service_fee(self):
        return round(self.price * 0.12, 2)

    def format_ticket(self):
        return f"{self.event}: ${self.price:.2f} | fee: ${self.service_fee():.2f}"

class EarlyBirdTicket(Ticket):
    def __init__(self, event, price, discount):
        super().__init__(event, price)
        self.discount = discount

    def final_price(self):
        return round(self.price * (1 - self.discount), 2)

    def service_fee(self):
        return round(self.final_price() * 0.12, 2)

    def format_ticket(self):
        d = int(self.discount * 100)
        return f"{self.event}: ${self.price:.2f} -> ${self.final_price():.2f} (-{d}%) | fee: ${self.service_fee():.2f}"

class PremiumTicket(Ticket):
    def __init__(self, event, price, vip_surcharge):
        super().__init__(event, price)
        self.vip_surcharge = vip_surcharge

    def service_fee(self):
        return round(self.price * 0.12 + self.price * self.vip_surcharge, 2)

    def format_ticket(self):
        percent = int(self.vip_surcharge * 100)
        return f"{self.event}: ${self.price:.2f} (premium, surcharge {percent}%) | fee: ${self.service_fee():.2f}"

class CompPass:
    def __init__(self, event, price):
        self.event = event
        self.price = 0.0

    def service_fee(self):
        return 0.0

    def format_ticket(self):
        return f"{self.event}: $0.00 (complimentary) | fee: $0.00"

class TicketOrder:
    def __init__(self, buyer_name):
        self.buyer_name = buyer_name
        self.tickets = []

    def add_ticket(self, ticket):
        self.tickets.append(ticket)

    def finalize(self):
        print(f"Order for {self.buyer_name}")
        subtotal = 0
        total_fees = 0
        for ticket in self.tickets:
            print(f"  {ticket.format_ticket()}")
            price = ticket.price
            fee = ticket.service_fee()
            subtotal += price
            total_fees += fee

        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Total Fees: ${total_fees:.2f}")
        print(f"Grand Total: ${subtotal + total_fees:.2f}")

order = TicketOrder('Nodira')

order.add_ticket(Ticket('Rock Concert', 80))
order.add_ticket(EarlyBirdTicket('Jazz Night', 120, 0.20))
order.add_ticket(PremiumTicket('Opera Gala', 200, 0.30))
order.add_ticket(CompPass('Staff Meeting', 0))

try:
    order.add_ticket(Ticket('Bad Event', -10))
except ValueError as e:
    print(f'Skipped: {e}')

order.finalize()

try:
    p = Priceable()
except TypeError:
    print('Cannot instantiate abstract class')