"""
Professional Inventory Management System
-----------------------------------------
Features:
- Tabulated output
- Strong defensive validation
- Centralised file handling
- Clean modular design
- Manager-friendly reporting
"""

from tabulate import tabulate

FILE_NAME = "inventory.txt"

# Global list storing Shoe objects
shoes_list = []



# Shoe Class


class Shoe:
    """Represents a shoe item in inventory."""

    def __init__(self, country, code, product, cost, quantity):
        self.country = country.strip()
        self.code = code.strip()
        self.product = product.strip()
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Return shoe cost."""
        return self.cost

    def get_quantity(self):
        """Return shoe quantity."""
        return self.quantity

    def __str__(self):
        """Readable string representation."""
        return (
            f"{self.country} | {self.code} | "
            f"{self.product} | R{self.cost:.2f} | {self.quantity}"
        )



# Utility Functions


def get_valid_number(prompt, number_type=float):
    """Validate numeric user input."""
    while True:
        try:
            value = number_type(input(prompt))
            if value < 0:
                print("Value cannot be negative.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def save_to_file():
    """Rewrite entire inventory file safely."""
    try:
        with open(FILE_NAME, "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")
            for shoe in shoes_list:
                file.write(
                    f"{shoe.country},{shoe.code},"
                    f"{shoe.product},{shoe.cost},{shoe.quantity}\n"
                )
    except Exception as error:
        print(f"File update failed: {error}")



# Core Functional Requirements


def read_shoes_data():
    """Load shoes from inventory.txt."""
    try:
        with open(FILE_NAME, "r") as file:
            next(file)  # Skip header

            for line in file:
                try:
                    country, code, product, cost, quantity = line.strip().split(",")
                    shoes_list.append(
                        Shoe(country, code, product, cost, quantity)
                    )
                except ValueError:
                    print("Warning: Skipping corrupted line.")

        print("Inventory successfully loaded.\n")

    except FileNotFoundError:
        print("inventory.txt not found. Starting empty.\n")


def capture_shoes():
    """Capture new shoe data from user."""
    print("\n--- Add New Shoe ---")

    country = input("Country: ").strip()
    code = input("Code: ").strip()

    # Prevent duplicate codes
    if any(shoe.code.lower() == code.lower() for shoe in shoes_list):
        print("Error: Shoe code already exists.\n")
        return

    product = input("Product Name: ").strip()
    cost = get_valid_number("Cost: ", float)
    quantity = get_valid_number("Quantity: ", int)

    new_shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(new_shoe)
    save_to_file()

    print("Shoe added successfully.\n")


def view_all():
    """Display all inventory in table format."""
    if not shoes_list:
        print("No inventory available.\n")
        return

    table = [
        [s.country, s.code, s.product, f"R{s.cost:.2f}", s.quantity]
        for s in shoes_list
    ]

    print("\n--- Current Inventory ---")
    print(tabulate(table,
                   headers=["Country", "Code", "Product", "Cost", "Quantity"],
                   tablefmt="grid"))
    print()


def re_stock():
    """Restock shoe with lowest quantity."""
    if not shoes_list:
        print("No inventory available.\n")
        return

    lowest_shoe = min(shoes_list, key=lambda s: s.quantity)

    print("\nLowest Stock Item:")
    print(lowest_shoe)

    decision = input("Restock this item? (yes/no): ").lower()

    if decision == "yes":
        additional_qty = get_valid_number("Add quantity: ", int)
        lowest_shoe.quantity += additional_qty
        save_to_file()
        print("Stock successfully updated.\n")
    else:
        print("Restock cancelled.\n")


def search_shoe():
    """Search for shoe by code."""
    code = input("Enter shoe code: ").strip().lower()

    for shoe in shoes_list:
        if shoe.code.lower() == code:
            print("\nShoe Found:")
            print(tabulate(
                [[shoe.country, shoe.code, shoe.product,
                  f"R{shoe.cost:.2f}", shoe.quantity]],
                headers=["Country", "Code", "Product", "Cost", "Quantity"],
                tablefmt="grid"
            ))
            print()
            return shoe

    print("Shoe not found.\n")
    return None


def value_per_item():
    """Display total value of each shoe item."""
    if not shoes_list:
        print("No inventory available.\n")
        return

    table = [
        [s.product, s.code, s.quantity,
         f"R{(s.cost * s.quantity):.2f}"]
        for s in shoes_list
    ]

    print("\nInventory Value Report")
    print(tabulate(table,
                   headers=["Product", "Code", "Quantity", "Total Value"],
                   tablefmt="grid"))
    print()


def highest_qty():
    """Display product with highest quantity for sale."""
    if not shoes_list:
        print("No inventory available.\n")
        return

    highest = max(shoes_list, key=lambda s: s.quantity)

    print("\n*** ON SALE ***")
    print(tabulate(
        [[highest.country, highest.code,
          highest.product, f"R{highest.cost:.2f}",
          highest.quantity]],
        headers=["Country", "Code", "Product", "Cost", "Quantity"],
        tablefmt="grid"
    ))
    print()



# Menu System


def menu():
    """Main program menu."""
    read_shoes_data()

    options = {
        "1": view_all,
        "2": capture_shoes,
        "3": re_stock,
        "4": search_shoe,
        "5": value_per_item,
        "6": highest_qty
    }

    while True:
        print("INVENTORY MENU")
        print("1. View All Shoes")
        print("2. Add New Shoe")
        print("3. Restock Lowest Quantity")
        print("4. Search Shoe")
        print("5. Value Per Item")
        print("6. Highest Quantity (For Sale)")
        print("7. Exit")
        print("---------------------------------------")

        choice = input("Select option (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break
        elif choice in options:
            options[choice]()
        else:
            print("Invalid selection. Choose 1–7.\n")


if __name__ == "__main__":
    menu()