# Food Inventory System

A Python-based tool to track food items in your pantry and fridge, with timestamps and quantities. Easily manage your inventory by adding items after shopping and removing them when making meals.

## Features

- **Track Food Items**: Store food items with name, quantity, unit, and timestamp
- **Dual Storage Locations**: Manage separate inventories for pantry and fridge
- **Add Items**: Add single or multiple items after shopping
- **Remove Items**: Remove single or multiple items when making meals
- **View Inventory**: Display current inventory with timestamps
- **Case-Insensitive**: Item names are handled case-insensitively for convenience

## Installation

No external dependencies required! This project uses only Python standard library.

```bash
git clone https://github.com/ryanjcronin5/FoodInventorySystem.git
cd FoodInventorySystem
```

## Usage

### Interactive CLI

Run the interactive command-line interface:

```bash
python main.py
```

The CLI provides the following options:
1. View current inventory
2. Add item to pantry
3. Add item to fridge
4. Remove item from pantry
5. Remove item from fridge
6. Make a meal (remove multiple items)
7. Add shopping (add multiple items)
8. Exit

### Programmatic Usage

You can also use the system programmatically in your Python code:

```python
from food_inventory_system import FoodInventorySystem

# Create a new inventory system
system = FoodInventorySystem()

# Add items to pantry
system.add_to_pantry("Rice", quantity=5.0, unit="lbs")
system.add_to_pantry("Pasta", quantity=3.0, unit="boxes")

# Add items to fridge
system.add_to_fridge("Milk", quantity=1.0, unit="gallon")
system.add_to_fridge("Eggs", quantity=12.0, unit="eggs")

# View inventory
print(system.show_inventory())

# Remove items when making a meal
system.remove_from_pantry("Rice", quantity=1.0)
system.remove_from_fridge("Eggs", quantity=4.0)

# Make a meal with multiple ingredients
ingredients = {
    'pantry': [
        {'name': 'Pasta', 'quantity': 1.0},
    ],
    'fridge': [
        {'name': 'Milk', 'quantity': 0.5}
    ]
}
system.make_meal(ingredients)

# Add shopping items
shopping = {
    'pantry': [
        {'name': 'Flour', 'quantity': 5.0, 'unit': 'lbs'},
        {'name': 'Sugar', 'quantity': 2.0, 'unit': 'lbs'}
    ],
    'fridge': [
        {'name': 'Cheese', 'quantity': 1.0, 'unit': 'block'}
    ]
}
system.add_shopping(shopping)
```

## Project Structure

```
FoodInventorySystem/
├── food_item.py                    # FoodItem class
├── inventory_location.py           # InventoryLocation class (Pantry/Fridge)
├── food_inventory_system.py        # Main system class
├── main.py                         # Interactive CLI application
├── test_food_item.py               # Unit tests for FoodItem
├── test_inventory_location.py      # Unit tests for InventoryLocation
├── test_food_inventory_system.py   # Unit tests for FoodInventorySystem
└── README.md                       # This file
```

## Running Tests

Run all tests using Python's unittest:

```bash
# Run all tests
python -m unittest discover -v

# Run specific test file
python -m unittest test_food_item.py -v
python -m unittest test_inventory_location.py -v
python -m unittest test_food_inventory_system.py -v
```

## Classes

### FoodItem
Represents a single food item with:
- `name`: Name of the item
- `quantity`: Quantity of the item
- `unit`: Unit of measurement
- `added_time`: Timestamp when item was added

### InventoryLocation
Represents a storage location (pantry or fridge) with methods to:
- Add items (updates quantity if item exists)
- Remove items (partial or complete removal)
- Get item by name
- List all items

### FoodInventorySystem
Main system class that manages both pantry and fridge, with methods to:
- Add items to pantry or fridge
- Remove items from pantry or fridge
- Make meals (remove multiple items at once)
- Add shopping (add multiple items at once)
- Display full inventory

## Examples

### Example 1: Weekly Shopping

```python
system = FoodInventorySystem()

# Add weekly shopping
shopping = {
    'pantry': [
        {'name': 'Rice', 'quantity': 5.0, 'unit': 'lbs'},
        {'name': 'Pasta', 'quantity': 3.0, 'unit': 'boxes'},
        {'name': 'Beans', 'quantity': 4.0, 'unit': 'cans'}
    ],
    'fridge': [
        {'name': 'Milk', 'quantity': 2.0, 'unit': 'gallons'},
        {'name': 'Eggs', 'quantity': 24.0, 'unit': 'eggs'},
        {'name': 'Chicken', 'quantity': 3.0, 'unit': 'lbs'}
    ]
}
system.add_shopping(shopping)
```

### Example 2: Making Dinner

```python
# Making pasta with chicken
dinner = {
    'pantry': [
        {'name': 'Pasta', 'quantity': 1.0}
    ],
    'fridge': [
        {'name': 'Chicken', 'quantity': 1.0}
    ]
}
results = system.make_meal(dinner)
```

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.