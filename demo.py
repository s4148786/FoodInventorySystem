#!/usr/bin/env python3
"""
Demo script to showcase Food Inventory System functionality.
"""
from food_inventory_system import FoodInventorySystem

# Change to trigger commit
def main():
    print("="*60)
    print("FOOD INVENTORY SYSTEM - DEMO")
    print("="*60)
    
    # Create a new system
    system = FoodInventorySystem()
    
    print("\n1. Initial State (Empty)")
    print(system.show_inventory())
    
    # Add items to pantry
    print("\n" + "="*60)
    print("2. Adding Items to Pantry")
    print("="*60)
    system.add_to_pantry("Rice", quantity=5.0, unit="lbs")
    system.add_to_pantry("Pasta", quantity=3.0, unit="boxes")
    system.add_to_pantry("Beans", quantity=4.0, unit="cans")
    system.add_to_pantry("Flour", quantity=10.0, unit="lbs")
    print("Added: Rice, Pasta, Beans, Flour")
    print(system.pantry)
    
    # Add items to fridge
    print("\n" + "="*60)
    print("3. Adding Items to Fridge")
    print("="*60)
    system.add_to_fridge("Milk", quantity=2.0, unit="gallons")
    system.add_to_fridge("Eggs", quantity=24.0, unit="eggs")
    system.add_to_fridge("Chicken", quantity=3.0, unit="lbs")
    system.add_to_fridge("Vegetables", quantity=2.0, unit="bags")
    print("Added: Milk, Eggs, Chicken, Vegetables")
    print(system.fridge)
    
    # View full inventory
    print("\n" + "="*60)
    print("4. Full Inventory")
    print("="*60)
    print(system.show_inventory())
    
    # Make a meal
    print("\n" + "="*60)
    print("5. Making a Meal (Pasta with Chicken)")
    print("="*60)
    ingredients = {
        'pantry': [
            {'name': 'Pasta', 'quantity': 1.0}
        ],
        'fridge': [
            {'name': 'Chicken', 'quantity': 1.0}
        ]
    }
    results = system.make_meal(ingredients)
    print("Meal ingredients removed:")
    for location, items in results.items():
        for item in items:
            status = "✓" if item['success'] else "✗"
            print(f"  {status} {item['name']} from {location}")
    
    print("\nUpdated inventory:")
    print(system.show_inventory())
    
    # Add shopping
    print("\n" + "="*60)
    print("6. Adding Shopping Items")
    print("="*60)
    shopping = {
        'pantry': [
            {'name': 'Cereal', 'quantity': 2.0, 'unit': 'boxes'},
            {'name': 'Bread', 'quantity': 2.0, 'unit': 'loaves'}
        ],
        'fridge': [
            {'name': 'Yogurt', 'quantity': 6.0, 'unit': 'cups'},
            {'name': 'Cheese', 'quantity': 1.0, 'unit': 'block'}
        ]
    }
    system.add_shopping(shopping)
    print("Shopping added: Cereal, Bread, Yogurt, Cheese")
    print(system.show_inventory())
    
    # Remove items
    print("\n" + "="*60)
    print("7. Removing Items")
    print("="*60)
    print("Removing 2.0 lbs of Rice from pantry...")
    system.remove_from_pantry("Rice", quantity=2.0)
    print("Removing 6 eggs from fridge...")
    system.remove_from_fridge("Eggs", quantity=6.0)
    print("\nUpdated inventory:")
    print(system.show_inventory())
    
    # Case insensitive test
    print("\n" + "="*60)
    print("8. Case-Insensitive Test")
    print("="*60)
    print("Adding 'RICE' (uppercase) to pantry...")
    system.add_to_pantry("RICE", quantity=1.0, unit="lbs")
    print("Rice quantity should increase (case-insensitive):")
    rice_item = system.pantry.get_item("rice")
    if rice_item:
        print(f"  Rice: {rice_item.quantity} {rice_item.unit}")
    
    print("\n" + "="*60)
    print("DEMO COMPLETE")
    print("="*60)


if __name__ == '__main__':
    main()
