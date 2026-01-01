"""
FoodInventorySystem class to manage pantry and fridge inventories.
"""
from inventory_location import InventoryLocation


class FoodInventorySystem:
    """Main system for managing food inventory across pantry and fridge."""
    
    def __init__(self):
        """Initialize the food inventory system with pantry and fridge."""
        self.pantry = InventoryLocation("Pantry")
        self.fridge = InventoryLocation("Fridge")
    
    def add_to_pantry(self, name: str, quantity: float = 1.0, unit: str = "unit"):
        """
        Add an item to the pantry.
        
        Args:
            name: Name of the food item
            quantity: Quantity to add (default: 1.0)
            unit: Unit of measurement (default: 'unit')
        """
        self.pantry.add_item(name, quantity, unit)
    
    def add_to_fridge(self, name: str, quantity: float = 1.0, unit: str = "unit"):
        """
        Add an item to the fridge.
        
        Args:
            name: Name of the food item
            quantity: Quantity to add (default: 1.0)
            unit: Unit of measurement (default: 'unit')
        """
        self.fridge.add_item(name, quantity, unit)
    
    def remove_from_pantry(self, name: str, quantity: float = None) -> bool:
        """
        Remove an item from the pantry.
        
        Args:
            name: Name of the food item
            quantity: Quantity to remove. If None, removes entire item.
        
        Returns:
            True if item was removed/updated, False if item not found
        """
        return self.pantry.remove_item(name, quantity)
    
    def remove_from_fridge(self, name: str, quantity: float = None) -> bool:
        """
        Remove an item from the fridge.
        
        Args:
            name: Name of the food item
            quantity: Quantity to remove. If None, removes entire item.
        
        Returns:
            True if item was removed/updated, False if item not found
        """
        return self.fridge.remove_item(name, quantity)
    
    def make_meal(self, ingredients: dict):
        """
        Remove multiple ingredients for making a meal.
        
        Args:
            ingredients: Dictionary with structure:
                {
                    'pantry': [{'name': 'item', 'quantity': 1.0}, ...],
                    'fridge': [{'name': 'item', 'quantity': 1.0}, ...]
                }
        """
        results = {'pantry': [], 'fridge': []}
        
        if 'pantry' in ingredients:
            for ingredient in ingredients['pantry']:
                name = ingredient['name']
                quantity = ingredient.get('quantity')
                success = self.remove_from_pantry(name, quantity)
                results['pantry'].append({'name': name, 'success': success})
        
        if 'fridge' in ingredients:
            for ingredient in ingredients['fridge']:
                name = ingredient['name']
                quantity = ingredient.get('quantity')
                success = self.remove_from_fridge(name, quantity)
                results['fridge'].append({'name': name, 'success': success})
        
        return results
    
    def add_shopping(self, items: dict):
        """
        Add multiple items after shopping.
        
        Args:
            items: Dictionary with structure:
                {
                    'pantry': [{'name': 'item', 'quantity': 1.0, 'unit': 'unit'}, ...],
                    'fridge': [{'name': 'item', 'quantity': 1.0, 'unit': 'unit'}, ...]
                }
        """
        if 'pantry' in items:
            for item in items['pantry']:
                self.add_to_pantry(
                    item['name'],
                    item.get('quantity', 1.0),
                    item.get('unit', 'unit')
                )
        
        if 'fridge' in items:
            for item in items['fridge']:
                self.add_to_fridge(
                    item['name'],
                    item.get('quantity', 1.0),
                    item.get('unit', 'unit')
                )
    
    def show_inventory(self):
        """
        Display the current inventory of both pantry and fridge.
        
        Returns:
            String representation of the entire inventory
        """
        return f"\n{self.pantry}\n\n{self.fridge}"
    
    def __str__(self):
        """String representation of the system."""
        return self.show_inventory()
