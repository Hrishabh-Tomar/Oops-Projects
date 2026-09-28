"""
Small E-Commerce Application - Product Class
Demonstrates: class, objects, __init__, instance methods,
static method, and input validation.
"""


class Product:
    def __init__(self, product_id, name, price, category, stock_quantity):
        # Use the static method to validate before creating the object
        if not Product.is_valid_price(price):
            raise ValueError(f"Invalid price for '{name}': {price}. Price must be greater than 0.")
        if stock_quantity < 0:
            raise ValueError(f"Stock for '{name}' cannot be negative.")

        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity

    # ---------- Static method ----------
    @staticmethod
    def is_valid_price(price):
        """Return True if price is a number greater than zero, else False."""
        return isinstance(price, (int, float)) and price > 0

    # ---------- Instance methods ----------
    def display_product(self):
        """Print a single product row."""
        status = "In stock" if self.stock_quantity > 0 else "OUT OF STOCK"
        print(f"{self.product_id:<6} {self.name:<22} {self.category:<12} "
              f"${self.price:>9,.2f} {self.stock_quantity:>6}   {status}")

    def update_stock(self, quantity):
        """
        Change stock by `quantity`.
        Positive = restock, negative = remove items.
        Stock can never drop below zero.
        """
        if self.stock_quantity + quantity < 0:
            print(f"Stock update failed for {self.name}: only "
                  f"{self.stock_quantity} left, cannot remove {abs(quantity)}.")
            return False
        self.stock_quantity += quantity
        action = "Restocked" if quantity > 0 else "Removed"
        print(f"{action} {abs(quantity)} x {self.name}. "
              f"Stock now: {self.stock_quantity}")
        return True

    def calculate_total_price(self, quantity):
        """Return the total cost for `quantity` units."""
        if quantity <= 0:
            return 0.0
        return self.price * quantity

    def buy(self, quantity):
        """Purchase: validate quantity, check stock, charge, reduce stock."""
        if quantity <= 0:
            print(f"Purchase failed: quantity must be at least 1 (got {quantity}).")
            return 0.0
        if quantity > self.stock_quantity:
            print(f"Purchase failed: requested {quantity} x {self.name}, "
                  f"only {self.stock_quantity} available.")
            return 0.0
        total = self.calculate_total_price(quantity)
        self.update_stock(-quantity)
        print(f"Purchased {quantity} x {self.name} for ${total:,.2f}")
        return total


def show_inventory(products):
    print(f"{'ID':<6} {'Name':<22} {'Category':<12} {'Price':>10} {'Stock':>6}   Status")
    print("-" * 75)
    for p in products:
        p.display_product()


# ---------------- Demo ----------------
if __name__ == "__main__":
    print("=== Static method: Product.is_valid_price() ===")
    for test_price in (499.99, 0, -25, 10):
        print(f"is_valid_price({test_price}) -> {Product.is_valid_price(test_price)}")

    # Create 5 products
    inventory = [
        Product("P101", "Wireless Mouse", 25.99, "Electronics", 50),
        Product("P102", "Mechanical Keyboard", 89.50, "Electronics", 20),
        Product("P103", "Cotton T-Shirt", 15.00, "Clothing", 100),
        Product("P104", "Python Crash Course", 39.95, "Books", 8),
        Product("P105", "Coffee Mug", 12.49, "Home", 3),
    ]

    print("\n=== Trying to create a product with an invalid price ===")
    try:
        Product("P999", "Broken Item", -5, "Misc", 10)
    except ValueError as err:
        print(f"Error: {err}")

    print("\n=== Initial Inventory ===")
    show_inventory(inventory)

    mouse, keyboard, tshirt, book, mug = inventory

    print("\n=== Price Calculation ===")
    print(f"3 x {keyboard.name} = ${keyboard.calculate_total_price(3):,.2f}")
    print(f"5 x {tshirt.name} = ${tshirt.calculate_total_price(5):,.2f}")

    print("\n=== Customer Purchases ===")
    cart_total = 0
    cart_total += mouse.buy(2)
    cart_total += keyboard.buy(1)
    cart_total += tshirt.buy(5)
    cart_total += book.buy(10)   # more than stock -> blocked
    cart_total += mug.buy(3)     # buys all remaining -> out of stock
    cart_total += mug.buy(1)     # now out of stock -> blocked
    cart_total += tshirt.buy(0)  # invalid quantity -> blocked
    print(f"\nOrder total: ${cart_total:,.2f}")

    print("\n=== Restocking (update_stock) ===")
    mug.update_stock(25)
    book.update_stock(12)
    keyboard.update_stock(-50)   # would go negative -> blocked

    print("\n=== Final Inventory ===")
    show_inventory(inventory)