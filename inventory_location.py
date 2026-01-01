"""
InventoryLocation class to represent a storage location (pantry or fridge).
"""
from typing import Dict, Optional
from food_item import FoodItem


class InventoryLocation:
    """Represents a storage location for food items."""
    
    def __init__(self, name: str):
        """
        Initialize an inventory location.
        
        Args:
            name: Name of the location (e.g., 'Pantry', 'Fridge')
        """
        self.name = name
        self.items: Dict[str, FoodItem] = {}
    
    def add_item(self, name: str, quantity: float = 1.0, unit: str = "unit"):
        """
        Add an item to the location or update quantity if it exists.
        
        Args:
            name: Name of the food item
            quantity: Quantity to add (default: 1.0)
            unit: Unit of measurement (default: 'unit')
        """
        name_lower = name.lower()
        if name_lower in self.items:
            self.items[name_lower].update_quantity(quantity)
        else:
            self.items[name_lower] = FoodItem(name, quantity, unit)
    
    def remove_item(self, name: str, quantity: float = None) -> bool:
        """
        Remove an item or reduce its quantity.
        
        Args:
            name: Name of the food item
            quantity: Quantity to remove. If None, removes entire item.
        
        Returns:
            True if item was removed/updated, False if item not found
        """
        name_lower = name.lower()
        if name_lower not in self.items:
            return False
        
        if quantity is None:
            del self.items[name_lower]
            return True
        
        self.items[name_lower].update_quantity(-quantity)
        if self.items[name_lower].quantity <= 0:
            del self.items[name_lower]
        
        return True
    
    def get_item(self, name: str) -> Optional[FoodItem]:
        """
        Get a food item by name.
        
        Args:
            name: Name of the food item
        
        Returns:
            FoodItem if found, None otherwise
        """
        name_lower = name.lower()
        return self.items.get(name_lower)
    
    def list_items(self):
        """
        Get a list of all items in the location.
        
        Returns:
            List of FoodItem objects
        """
        return list(self.items.values())
    
    def __str__(self):
        """String representation of the location."""
        if not self.items:
            return f"{self.name}: (empty)"
        
        items_str = "\n  ".join(str(item) for item in sorted(self.items.values(), key=lambda x: x.name))
        return f"{self.name}:\n  {items_str}"
