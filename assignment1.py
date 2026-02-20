class StudioBooking:
    studio_name = "Harmony Studios"
    total_bookings = 0

    def __init__(self, artist_name, session_id, equipment=None):
        self.artist_name = artist_name
        self.session_id = session_id
        if equipment is None:
            self.equipment = []
        else:
            self.equipment = equipment
        StudioBooking.total_bookings += 1

    def book_equipment(self, item_name):
        if type(item_name) == str and item_name:
            self.equipment.append(item_name)
            print(f"Booked equipment: {item_name}")

    def return_equipment(self, item_name):
        if item_name in self.equipment:
            self.equipment.remove(item_name)
            print(f"Returned equipments: {item_name}")
        else:
            print("Equipment is not booked")

    def display_booking(self):
        print(f"Session {self.session_id} for {self.artist_name} at {StudioBooking.studio_name}")


booking1 = StudioBooking("Daler", "M-501")
booking2 = StudioBooking("Nargiza", "M-502")

booking1.display_booking()
booking1.book_equipment("Guitar")
booking1.book_equipment("Microphone")
booking1.return_equipment("Microphone")

booking2.display_booking()
booking2.return_equipment("Drums")

print(f"Total bookings: {StudioBooking.total_bookings}")