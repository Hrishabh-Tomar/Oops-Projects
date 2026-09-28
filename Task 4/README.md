# Task 4: E-Commerce Product Management (Python OOP)

A `Product` class for a small online store. It handles product display, stock updates, price calculation and purchases. A static method checks that prices are valid.

## Features

- Create products with an ID, name, price, category and stock quantity
- Refuse to create a product with an invalid price or negative stock
- Display the inventory as a formatted table that shows whether each item is in stock
- Update stock: a positive number restocks and a negative number removes items. Stock never goes below 0.
- Calculate the total price for a quantity
- Buy products. Each purchase checks the quantity and the stock, charges the customer and lowers the stock.

## OOP Concepts Covered

| Concept | Implementation |
|---|---|
| **Class** | `Product` |
| **Objects** | 5 products: Mouse, Keyboard, T-Shirt, Book, Mug |
| **Constructor (`__init__`)** | Checks the price with the static method before setting the attributes |
| **Instance methods** | `display_product()`, `update_stock()`, `calculate_total_price()`, `buy()` |
| **Static method** | `Product.is_valid_price(price)` returns `True` if the price is above 0 |

## Project Structure

```
.
├── product_store.py   # Product class + demo
└── README.md
```

## Requirements

- Python 3.6 or newer
- No other libraries needed

## How to Run

```bash
# Mac / Linux
python3 product_store.py

# Windows
python product_store.py
```

## Usage Example

```python
from product_store import Product

print(Product.is_valid_price(499.99))   # True
print(Product.is_valid_price(0))        # False

mouse = Product("P101", "Wireless Mouse", 25.99, "Electronics", 50)
print(f"{mouse.calculate_total_price(3):.2f}")   # 77.97
mouse.buy(2)                            # stock: 48
mouse.update_stock(20)                  # stock: 68
mouse.display_product()
```

## Sample Output

```
=== Static method: Product.is_valid_price() ===
is_valid_price(499.99) -> True
is_valid_price(0) -> False
is_valid_price(-25) -> False

=== Customer Purchases ===
Purchased 2 x Wireless Mouse for $51.98
Purchase failed: requested 10 x Python Crash Course, only 8 available.
Purchased 3 x Coffee Mug for $37.47
Purchase failed: requested 1 x Coffee Mug, only 0 available.

Order total: $253.95

=== Restocking (update_stock) ===
Restocked 25 x Coffee Mug. Stock now: 25
Stock update failed for Mechanical Keyboard: only 19 left, cannot remove 50.
```

## Method Reference

| Method | Type | Description |
|---|---|---|
| `__init__(product_id, name, price, category, stock_quantity)` | Constructor | Creates a product after checking the price and stock |
| `is_valid_price(price)` | Static | Returns `True` if the price is a number greater than 0 |
| `display_product()` | Instance | Prints one inventory row with the stock status |
| `update_stock(quantity)` | Instance | Adds or removes stock. Stock can't go below 0. |
| `calculate_total_price(quantity)` | Instance | Returns price × quantity |
| `buy(quantity)` | Instance | Checks the quantity and stock, returns the total cost and lowers the stock |

## Possible Enhancements

- A `Cart` class that holds several products
- Discount codes and tax calculation
- Low-stock alerts
