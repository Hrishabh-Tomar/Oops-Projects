# Task 6: Mini Vehicle Rental Application (Python OOP)

A vehicle rental system that uses **hierarchical inheritance**: one `Vehicle` parent class with two child classes, `Car` and `Bike`. Rent calculation is written once in the parent and shared by every vehicle type.

```
Vehicle
   |
   +---- Car   (adds number of seats)
   |
   +---- Bike  (adds engine capacity)
```

## Features

- Add cars and bikes to the rental fleet
- Calculate the rent for any number of days
- Check that the rental duration is a whole number of days greater than 0, using a static method
- Rent a vehicle. Booking is refused if the vehicle is already rented or the duration is invalid.
- Return a vehicle so it can be rented again
- Display each vehicle's details and whether it's available

## OOP Concepts Covered

| Concept | Implementation |
|---|---|
| **Parent class** | `Vehicle` stores `vehicle_number`, `brand`, `model`, `rent_per_day` |
| **Child classes** | `Car(Vehicle)` adds `seats` and `Bike(Vehicle)` adds `engine_cc` |
| **Hierarchical inheritance** | Two child classes share one parent |
| **`super()` and overriding** | Each child's `display_details()` prints the parent's details and adds its own field |
| **Static method** | `Vehicle.is_valid_duration(days)` |
| **Instance methods** | `calculate_rent()`, `rent()`, `return_vehicle()`, `display_details()` |
| **Objects** | 2 cars + 2 bikes |

## Project Structure

```
.
├── vehicle_rental.py   # Vehicle, Car, Bike classes + demo
└── README.md
```

## Requirements

- Python 3.6 or newer
- No other libraries needed

## How to Run

```bash
# Mac / Linux
python3 vehicle_rental.py

# Windows
python vehicle_rental.py
```

## Usage Example

```python
from vehicle_rental import Vehicle, Car, Bike

print(Vehicle.is_valid_duration(3))    # True
print(Vehicle.is_valid_duration(0))    # False

car = Car("MP07-CA-1001", "Toyota", "Innova Crysta", 60.00, seats=7)
bike = Bike("MP07-BK-2001", "Royal Enfield", "Classic 350", 18.00, engine_cc=349)

print(car.calculate_rent(5))    # 300.0
bike.rent("Priya", 3)           # booked: $54.00
bike.rent("Rohan", 2)           # refused: already rented
bike.return_vehicle()
```

## Sample Output

```
=== 3. Rent quotes (calculate_rent inherited from Vehicle) ===
Toyota Innova Crysta       5 days -> $300.00
Hyundai i20                5 days -> $175.00
Royal Enfield Classic 350  5 days -> $90.00
Honda Activa 6G            5 days -> $40.00

=== 4. Bookings ===
Booked Toyota Innova Crysta for Aarav: 4 day(s) x $60.00 = $240.00
Booked Royal Enfield Classic 350 for Priya: 3 day(s) x $18.00 = $54.00
Invalid rental duration: 0. Days must be a whole number greater than 0.
Booking failed for Rohan.
Booking failed: Toyota Innova Crysta (MP07-CA-1001) is already rented.
Booked Hyundai i20 for Neha: 2 day(s) x $35.00 = $70.00

Total revenue booked: $364.00
```

## Method Reference

| Method | Class | Description |
|---|---|---|
| `__init__(vehicle_number, brand, model, rent_per_day)` | Vehicle | Creates a vehicle. The daily price must be above 0. |
| `is_valid_duration(days)` | Vehicle (static) | Returns `True` for a whole number of days greater than 0 |
| `calculate_rent(days)` | Vehicle | Returns `rent_per_day × days`, or `None` if the duration is invalid |
| `rent(customer, days)` | Vehicle | Checks availability and duration, then books the vehicle |
| `return_vehicle()` | Vehicle | Marks the vehicle as available again |
| `display_details()` | Vehicle / Car / Bike | Prints the shared details. Car adds seats and Bike adds engine size. |

## Possible Enhancements

- Add a `Truck` class that charges extra for load weight
- Give weekly rental discounts
- Search for available vehicles by type or price
