"""
Unit tests for FoodItem class.
"""
import unittest
from datetime import datetime
from food_item import FoodItem


class TestFoodItem(unittest.TestCase):
    """Test cases for FoodItem class."""
    
    def test_init_default(self):
        """Test FoodItem initialization with default values."""
        item = FoodItem("Apple")
        self.assertEqual(item.name, "Apple")
        self.assertEqual(item.quantity, 1.0)
        self.assertEqual(item.unit, "unit")
        self.assertIsInstance(item.added_time, datetime)
    
    def test_init_with_params(self):
        """Test FoodItem initialization with custom values."""
        item = FoodItem("Milk", quantity=2.5, unit="gallons")
        self.assertEqual(item.name, "Milk")
        self.assertEqual(item.quantity, 2.5)
        self.assertEqual(item.unit, "gallons")
    
    def test_update_quantity_add(self):
        """Test adding to quantity."""
        item = FoodItem("Bread", quantity=2.0)
        item.update_quantity(3.0)
        self.assertEqual(item.quantity, 5.0)
    
    def test_update_quantity_remove(self):
        """Test removing from quantity."""
        item = FoodItem("Eggs", quantity=12.0)
        item.update_quantity(-4.0)
        self.assertEqual(item.quantity, 8.0)
    
    def test_str_representation(self):
        """Test string representation."""
        item = FoodItem("Cheese", quantity=1.5, unit="lbs")
        str_repr = str(item)
        self.assertIn("Cheese", str_repr)
        self.assertIn("1.5", str_repr)
        self.assertIn("lbs", str_repr)
    
    def test_repr_representation(self):
        """Test repr representation."""
        item = FoodItem("Butter", quantity=2.0, unit="sticks")
        repr_str = repr(item)
        self.assertIn("FoodItem", repr_str)
        self.assertIn("Butter", repr_str)
        self.assertIn("2.0", repr_str)
        self.assertIn("sticks", repr_str)


if __name__ == '__main__':
    unittest.main()
