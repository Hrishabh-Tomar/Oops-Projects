"""
Mini Vehicle Rental Application
Demonstrates: parent class, multiple child classes (hierarchical
inheritance), super(), method overriding, and a static method.

    Vehicle
       |
       +---- Car   (adds number of seats)
       |
       +---- Bike  (adds engine capacity)
"""


# ================= Parent Class =================
class Vehicle:
    def __init__(self, vehicle_number, brand, model, rent_per_day):
        if rent_per_day <= 0:
            raise ValueError("Rental price per day must be greater than 0.")
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.model = model
        self.rent_per_day = rent_per_day
        self.is_available = True

    # ---------- Static method ----------
    @staticmethod
    def is_valid_duration(days):
        """Return True if days is a whole number greater than zero."""
        return isinstance(days, int) and days > 0

    # ---------- Instance methods ----------
    def calculate_rent(self, days):
        """Return total rent for `days`, or None if the duration is invalid."""
        if not Vehicle.is_valid_duration(days):
            print(f"Invalid rental duration: {days}. Days must be a whole number greater than 0.")
            return None
        return self.rent_per_day * days

    def display_details(self):
        """Print details common to every vehicle."""
        print(f"Type         : {type(self).__name__}")
        print(f"Vehicle No.  : {self.vehicle_number}")
        print(f"Brand/Model  : {self.brand} {self.model}")
        print(f"Rent per day : ${self.rent_per_day:,.2f}")
        print(f"Status       : {'Available' if self.is_available else 'Rented out'}")

    def rent(self, customer, days):
        """Rent the vehicle: check availability, validate days, bill customer."""
        if not self.is_available:
            print(f"Booking failed: {self.brand} {self.model} ({self.vehicle_number}) is already rented.")
            return None
        total = self.calculate_rent(days)
        if total is None:
            print(f"Booking failed for {customer}.")
            return None
        self.is_available = False
        print(f"Booked {self.brand} {self.model} for {customer}: "
              f"{days} day(s) x ${self.rent_per_day:,.2f} = ${total:,.2f}")
        return total

    def return_vehicle(self):
        """Mark the vehicle as available again."""
        self.is_available = True
        print(f"{self.brand} {self.model} ({self.vehicle_number}) returned and available.")


# ================= Child Class 1 =================
class Car(Vehicle):
    def __init__(self, vehicle_number, brand, model, rent_per_day, seats):
        super().__init__(vehicle_number, brand, model, rent_per_day)
        self.seats = seats

    def display_details(self):
        super().display_details()
        print(f"Seats        : {self.seats}")


# ================= Child Class 2 =================
class Bike(Vehicle):
    def __init__(self, vehicle_number, brand, model, rent_per_day, engine_cc):
        super().__init__(vehicle_number, brand, model, rent_per_day)
        self.engine_cc = engine_cc

    def display_details(self):
        super().display_details()
        print(f"Engine       : {self.engine_cc} cc")


def show_fleet(fleet):
    for v in fleet:
        print("-" * 38)
        v.display_details()
    print("-" * 38)


# ================= Demo =================
if __name__ == "__main__":
    # 2 cars + 2 bikes
    fleet = [
        Car("MP07-CA-1001", "Toyota", "Innova Crysta", 60.00, seats=7),
        Car("MP07-CA-1002", "Hyundai", "i20", 35.00, seats=5),
        Bike("MP07-BK-2001", "Royal Enfield", "Classic 350", 18.00, engine_cc=349),
        Bike("MP07-BK-2002", "Honda", "Activa 6G", 8.00, engine_cc=110),
    ]
    innova, i20, enfield, activa = fleet

    print("=== 1. Fleet ===")
    show_fleet(fleet)

    print("\n=== 2. Static method: Vehicle.is_valid_duration() ===")
    for d in (3, 0, -2, 1.5):
        print(f"is_valid_duration({d}) -> {Vehicle.is_valid_duration(d)}")

    print("\n=== 3. Rent quotes (calculate_rent inherited from Vehicle) ===")
    for v in fleet:
        print(f"{v.brand + ' ' + v.model:<26} 5 days -> ${v.calculate_rent(5):,.2f}")

    print("\n=== 4. Bookings ===")
    revenue = 0
    for result in (
        innova.rent("Aarav", 4),
        enfield.rent("Priya", 3),
        activa.rent("Rohan", 0),      # invalid duration
        innova.rent("Neha", 2),       # already rented
        i20.rent("Neha", 2),          # alternative car
    ):
        revenue += result or 0
    print(f"\nTotal revenue booked: ${revenue:,.2f}")

    print("\n=== 5. Returns ===")
    innova.return_vehicle()
    innova.rent("Neha", 1)            # available again

    print("\n=== 6. Fleet Status ===")
    show_fleet(fleet)

    print("\n=== 7. Inheritance checks ===")
    print(f"isinstance(innova, Vehicle)  -> {isinstance(innova, Vehicle)}")
    print(f"isinstance(activa, Car)      -> {isinstance(activa, Car)}")
    print(f"issubclass(Bike, Vehicle)    -> {issubclass(Bike, Vehicle)}")
    print(f"Car has engine_cc?           -> {hasattr(innova, 'engine_cc')}")
    print(f"Bike has seats?              -> {hasattr(activa, 'seats')}")