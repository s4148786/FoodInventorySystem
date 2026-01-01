"""
FoodItem class to represent an individual food item in the inventory.
"""
from datetime import datetime


class FoodItem:
    """Represents a food item with name, quantity, and timestamp."""
    
    def __init__(self, name: str, quantity: float = 1.0, unit: str = "unit"):
        """
        Initialize a food item.
        
        Args:
            name: Name of the food item
            quantity: Quantity of the item (default: 1.0)
            unit: Unit of measurement (e.g., 'unit', 'lbs', 'oz', 'kg') (default: 'unit')
        """
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.added_time = datetime.now()
    
    def update_quantity(self, amount: float):
        """
        Update the quantity of the food item.
        
        Args:
            amount: Amount to add (positive) or remove (negative)
        """
        self.quantity += amount
    
    def __str__(self):
        """String representation of the food item."""
        return f"{self.name}: {self.quantity} {self.unit} (added: {self.added_time.strftime('%Y-%m-%d %H:%M')})"
    
    def __repr__(self):
        """Repr representation of the food item."""
        return f"FoodItem(name='{self.name}', quantity={self.quantity}, unit='{self.unit}')"
