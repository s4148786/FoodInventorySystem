"""
Unit tests for FoodInventorySystem class.
"""
import unittest
from food_inventory_system import FoodInventorySystem


class TestFoodInventorySystem(unittest.TestCase):
    """Test cases for FoodInventorySystem class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.system = FoodInventorySystem()
    
    def test_init(self):
        """Test FoodInventorySystem initialization."""
        self.assertIsNotNone(self.system.pantry)
        self.assertIsNotNone(self.system.fridge)
        self.assertEqual(self.system.pantry.name, "Pantry")
        self.assertEqual(self.system.fridge.name, "Fridge")
    
    def test_add_to_pantry(self):
        """Test adding items to pantry."""
        self.system.add_to_pantry("Rice", quantity=5.0, unit="lbs")
        item = self.system.pantry.get_item("Rice")
        self.assertIsNotNone(item)
        self.assertEqual(item.quantity, 5.0)
    
    def test_add_to_fridge(self):
        """Test adding items to fridge."""
        self.system.add_to_fridge("Milk", quantity=1.0, unit="gallon")
        item = self.system.fridge.get_item("Milk")
        self.assertIsNotNone(item)
        self.assertEqual(item.quantity, 1.0)
    
    def test_remove_from_pantry(self):
        """Test removing items from pantry."""
        self.system.add_to_pantry("Flour", quantity=10.0)
        result = self.system.remove_from_pantry("Flour", quantity=3.0)
        self.assertTrue(result)
        item = self.system.pantry.get_item("Flour")
        self.assertEqual(item.quantity, 7.0)
    
    def test_remove_from_fridge(self):
        """Test removing items from fridge."""
        self.system.add_to_fridge("Eggs", quantity=12.0)
        result = self.system.remove_from_fridge("Eggs", quantity=4.0)
        self.assertTrue(result)
        item = self.system.fridge.get_item("Eggs")
        self.assertEqual(item.quantity, 8.0)
    
    def test_remove_nonexistent_item(self):
        """Test removing item that doesn't exist."""
        result = self.system.remove_from_pantry("NonExistent")
        self.assertFalse(result)
    
    def test_make_meal_pantry_only(self):
        """Test making a meal with pantry items only."""
        self.system.add_to_pantry("Pasta", quantity=5.0)
        self.system.add_to_pantry("Sauce", quantity=3.0)
        
        ingredients = {
            'pantry': [
                {'name': 'Pasta', 'quantity': 1.0},
                {'name': 'Sauce', 'quantity': 1.0}
            ]
        }
        
        results = self.system.make_meal(ingredients)
        self.assertTrue(results['pantry'][0]['success'])
        self.assertTrue(results['pantry'][1]['success'])
        self.assertEqual(self.system.pantry.get_item("Pasta").quantity, 4.0)
        self.assertEqual(self.system.pantry.get_item("Sauce").quantity, 2.0)
    
    def test_make_meal_fridge_only(self):
        """Test making a meal with fridge items only."""
        self.system.add_to_fridge("Chicken", quantity=4.0)
        self.system.add_to_fridge("Vegetables", quantity=3.0)
        
        ingredients = {
            'fridge': [
                {'name': 'Chicken', 'quantity': 1.0},
                {'name': 'Vegetables', 'quantity': 1.0}
            ]
        }
        
        results = self.system.make_meal(ingredients)
        self.assertTrue(results['fridge'][0]['success'])
        self.assertTrue(results['fridge'][1]['success'])
        self.assertEqual(self.system.fridge.get_item("Chicken").quantity, 3.0)
        self.assertEqual(self.system.fridge.get_item("Vegetables").quantity, 2.0)
    
    def test_make_meal_both_locations(self):
        """Test making a meal with items from both locations."""
        self.system.add_to_pantry("Rice", quantity=5.0)
        self.system.add_to_fridge("Beef", quantity=3.0)
        
        ingredients = {
            'pantry': [{'name': 'Rice', 'quantity': 1.0}],
            'fridge': [{'name': 'Beef', 'quantity': 1.0}]
        }
        
        results = self.system.make_meal(ingredients)
        self.assertTrue(results['pantry'][0]['success'])
        self.assertTrue(results['fridge'][0]['success'])
    
    def test_make_meal_remove_entire_item(self):
        """Test making a meal that removes entire item."""
        self.system.add_to_pantry("Spice", quantity=1.0)
        
        ingredients = {
            'pantry': [{'name': 'Spice', 'quantity': None}]
        }
        
        results = self.system.make_meal(ingredients)
        self.assertTrue(results['pantry'][0]['success'])
        self.assertIsNone(self.system.pantry.get_item("Spice"))
    
    def test_add_shopping_pantry(self):
        """Test adding shopping items to pantry."""
        items = {
            'pantry': [
                {'name': 'Cereal', 'quantity': 2.0, 'unit': 'boxes'},
                {'name': 'Bread', 'quantity': 1.0, 'unit': 'loaf'}
            ]
        }
        
        self.system.add_shopping(items)
        self.assertEqual(self.system.pantry.get_item("Cereal").quantity, 2.0)
        self.assertEqual(self.system.pantry.get_item("Bread").quantity, 1.0)
    
    def test_add_shopping_fridge(self):
        """Test adding shopping items to fridge."""
        items = {
            'fridge': [
                {'name': 'Yogurt', 'quantity': 6.0, 'unit': 'cups'},
                {'name': 'Cheese', 'quantity': 1.0, 'unit': 'block'}
            ]
        }
        
        self.system.add_shopping(items)
        self.assertEqual(self.system.fridge.get_item("Yogurt").quantity, 6.0)
        self.assertEqual(self.system.fridge.get_item("Cheese").quantity, 1.0)
    
    def test_add_shopping_both_locations(self):
        """Test adding shopping items to both locations."""
        items = {
            'pantry': [{'name': 'Crackers', 'quantity': 3.0}],
            'fridge': [{'name': 'Juice', 'quantity': 2.0}]
        }
        
        self.system.add_shopping(items)
        self.assertIsNotNone(self.system.pantry.get_item("Crackers"))
        self.assertIsNotNone(self.system.fridge.get_item("Juice"))
    
    def test_show_inventory(self):
        """Test showing full inventory."""
        self.system.add_to_pantry("Oats", quantity=1.0)
        self.system.add_to_fridge("Milk", quantity=1.0)
        
        inventory = self.system.show_inventory()
        self.assertIn("Pantry", inventory)
        self.assertIn("Fridge", inventory)
        self.assertIn("Oats", inventory)
        self.assertIn("Milk", inventory)


if __name__ == '__main__':
    unittest.main()
