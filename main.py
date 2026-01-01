#!/usr/bin/env python3
"""
Interactive CLI application for Food Inventory System.
"""
from food_inventory_system import FoodInventorySystem


def print_menu():
    """Print the main menu."""
    print("\n" + "="*50)
    print("FOOD INVENTORY SYSTEM")
    print("="*50)
    print("1. View Inventory")
    print("2. Add Item to Pantry")
    print("3. Add Item to Fridge")
    print("4. Remove Item from Pantry")
    print("5. Remove Item from Fridge")
    print("6. Make a Meal (Remove Multiple Items)")
    print("7. Add Shopping (Add Multiple Items)")
    print("8. Exit")
    print("="*50)


def view_inventory(system):
    """Display the current inventory."""
    print("\n" + "="*50)
    print("CURRENT INVENTORY")
    print("="*50)
    print(system.show_inventory())
    print("="*50)


def add_item_to_location(system, location):
    """Add an item to a specific location."""
    print(f"\n--- Add Item to {location} ---")
    name = input("Item name: ").strip()
    if not name:
        print("Error: Item name cannot be empty.")
        return
    
    try:
        quantity = float(input("Quantity (default 1.0): ").strip() or "1.0")
    except ValueError:
        print("Error: Invalid quantity. Using default 1.0")
        quantity = 1.0
    
    unit = input("Unit (default 'unit'): ").strip() or "unit"
    
    if location == "Pantry":
        system.add_to_pantry(name, quantity, unit)
    else:
        system.add_to_fridge(name, quantity, unit)
    
    print(f"✓ Added {quantity} {unit} of {name} to {location}")


def remove_item_from_location(system, location):
    """Remove an item from a specific location."""
    print(f"\n--- Remove Item from {location} ---")
    name = input("Item name: ").strip()
    if not name:
        print("Error: Item name cannot be empty.")
        return
    
    remove_all = input("Remove entire item? (y/n, default n): ").strip().lower()
    
    if remove_all == 'y':
        quantity = None
    else:
        try:
            quantity = float(input("Quantity to remove: ").strip())
        except ValueError:
            print("Error: Invalid quantity.")
            return
    
    if location == "Pantry":
        success = system.remove_from_pantry(name, quantity)
    else:
        success = system.remove_from_fridge(name, quantity)
    
    if success:
        if quantity is None:
            print(f"✓ Removed {name} from {location}")
        else:
            print(f"✓ Removed {quantity} of {name} from {location}")
    else:
        print(f"✗ Item '{name}' not found in {location}")


def make_meal(system):
    """Remove multiple items for making a meal."""
    print("\n--- Make a Meal ---")
    ingredients = {'pantry': [], 'fridge': []}
    
    print("\nPantry ingredients (press Enter with empty name when done):")
    while True:
        name = input("  Item name: ").strip()
        if not name:
            break
        
        remove_all = input("  Remove entire item? (y/n, default n): ").strip().lower()
        if remove_all == 'y':
            quantity = None
        else:
            try:
                quantity = float(input("  Quantity: ").strip())
            except ValueError:
                print("  Error: Invalid quantity. Skipping this item.")
                continue
        
        ingredients['pantry'].append({'name': name, 'quantity': quantity})
    
    print("\nFridge ingredients (press Enter with empty name when done):")
    while True:
        name = input("  Item name: ").strip()
        if not name:
            break
        
        remove_all = input("  Remove entire item? (y/n, default n): ").strip().lower()
        if remove_all == 'y':
            quantity = None
        else:
            try:
                quantity = float(input("  Quantity: ").strip())
            except ValueError:
                print("  Error: Invalid quantity. Skipping this item.")
                continue
        
        ingredients['fridge'].append({'name': name, 'quantity': quantity})
    
    if not ingredients['pantry'] and not ingredients['fridge']:
        print("No ingredients specified.")
        return
    
    results = system.make_meal(ingredients)
    
    print("\n--- Meal Results ---")
    for location, items in results.items():
        if items:
            print(f"\n{location.capitalize()}:")
            for item in items:
                status = "✓" if item['success'] else "✗"
                print(f"  {status} {item['name']}")


def add_shopping(system):
    """Add multiple items after shopping."""
    print("\n--- Add Shopping ---")
    items = {'pantry': [], 'fridge': []}
    
    print("\nPantry items (press Enter with empty name when done):")
    while True:
        name = input("  Item name: ").strip()
        if not name:
            break
        
        try:
            quantity = float(input("  Quantity (default 1.0): ").strip() or "1.0")
        except ValueError:
            print("  Error: Invalid quantity. Using default 1.0")
            quantity = 1.0
        
        unit = input("  Unit (default 'unit'): ").strip() or "unit"
        items['pantry'].append({'name': name, 'quantity': quantity, 'unit': unit})
    
    print("\nFridge items (press Enter with empty name when done):")
    while True:
        name = input("  Item name: ").strip()
        if not name:
            break
        
        try:
            quantity = float(input("  Quantity (default 1.0): ").strip() or "1.0")
        except ValueError:
            print("  Error: Invalid quantity. Using default 1.0")
            quantity = 1.0
        
        unit = input("  Unit (default 'unit'): ").strip() or "unit"
        items['fridge'].append({'name': name, 'quantity': quantity, 'unit': unit})
    
    if not items['pantry'] and not items['fridge']:
        print("No items specified.")
        return
    
    system.add_shopping(items)
    print("\n✓ Shopping items added successfully!")


def main():
    """Main application loop."""
    system = FoodInventorySystem()
    
    print("\nWelcome to the Food Inventory System!")
    print("Track food in your pantry and fridge with ease.")
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            view_inventory(system)
        elif choice == '2':
            add_item_to_location(system, "Pantry")
        elif choice == '3':
            add_item_to_location(system, "Fridge")
        elif choice == '4':
            remove_item_from_location(system, "Pantry")
        elif choice == '5':
            remove_item_from_location(system, "Fridge")
        elif choice == '6':
            make_meal(system)
        elif choice == '7':
            add_shopping(system)
        elif choice == '8':
            print("\nThank you for using Food Inventory System!")
            print("Goodbye!\n")
            break
        else:
            print("\n✗ Invalid choice. Please enter a number between 1 and 8.")
        
        input("\nPress Enter to continue...")


if __name__ == '__main__':
    main()
