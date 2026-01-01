"""
Unit tests for InventoryLocation class.
"""
import unittest
from inventory_location import InventoryLocation


class TestInventoryLocation(unittest.TestCase):
    """Test cases for InventoryLocation class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.pantry = InventoryLocation("Pantry")
    
    def test_init(self):
        """Test InventoryLocation initialization."""
        self.assertEqual(self.pantry.name, "Pantry")
        self.assertEqual(len(self.pantry.items), 0)
    
    def test_add_item_new(self):
        """Test adding a new item."""
        self.pantry.add_item("Rice", quantity=5.0, unit="lbs")
        self.assertEqual(len(self.pantry.items), 1)
        item = self.pantry.get_item("Rice")
        self.assertIsNotNone(item)
        self.assertEqual(item.quantity, 5.0)
        self.assertEqual(item.unit, "lbs")
    
    def test_add_item_existing(self):
        """Test adding to an existing item."""
        self.pantry.add_item("Pasta", quantity=2.0, unit="boxes")
        self.pantry.add_item("Pasta", quantity=3.0, unit="boxes")
        item = self.pantry.get_item("Pasta")
        self.assertEqual(item.quantity, 5.0)
        self.assertEqual(len(self.pantry.items), 1)
    
    def test_add_item_case_insensitive(self):
        """Test that item names are case-insensitive."""
        self.pantry.add_item("Beans", quantity=1.0)
        self.pantry.add_item("beans", quantity=2.0)
        self.pantry.add_item("BEANS", quantity=1.0)
        self.assertEqual(len(self.pantry.items), 1)
        item = self.pantry.get_item("BeAnS")
        self.assertEqual(item.quantity, 4.0)
    
    def test_remove_item_complete(self):
        """Test removing an entire item."""
        self.pantry.add_item("Flour", quantity=10.0)
        result = self.pantry.remove_item("Flour")
        self.assertTrue(result)
        self.assertEqual(len(self.pantry.items), 0)
    
    def test_remove_item_partial(self):
        """Test removing partial quantity."""
        self.pantry.add_item("Sugar", quantity=5.0, unit="lbs")
        result = self.pantry.remove_item("Sugar", quantity=2.0)
        self.assertTrue(result)
        item = self.pantry.get_item("Sugar")
        self.assertEqual(item.quantity, 3.0)
    
    def test_remove_item_all_quantity(self):
        """Test removing all quantity removes the item."""
        self.pantry.add_item("Salt", quantity=2.0)
        self.pantry.remove_item("Salt", quantity=2.0)
        self.assertEqual(len(self.pantry.items), 0)
    
    def test_remove_item_not_found(self):
        """Test removing non-existent item."""
        result = self.pantry.remove_item("NonExistent")
        self.assertFalse(result)
    
    def test_get_item_exists(self):
        """Test getting an existing item."""
        self.pantry.add_item("Oil", quantity=1.5, unit="bottles")
        item = self.pantry.get_item("Oil")
        self.assertIsNotNone(item)
        self.assertEqual(item.name, "Oil")
    
    def test_get_item_not_exists(self):
        """Test getting a non-existent item."""
        item = self.pantry.get_item("NonExistent")
        self.assertIsNone(item)
    
    def test_list_items_empty(self):
        """Test listing items when empty."""
        items = self.pantry.list_items()
        self.assertEqual(len(items), 0)
    
    def test_list_items_multiple(self):
        """Test listing multiple items."""
        self.pantry.add_item("Item1", quantity=1.0)
        self.pantry.add_item("Item2", quantity=2.0)
        self.pantry.add_item("Item3", quantity=3.0)
        items = self.pantry.list_items()
        self.assertEqual(len(items), 3)
    
    def test_str_representation_empty(self):
        """Test string representation when empty."""
        str_repr = str(self.pantry)
        self.assertIn("Pantry", str_repr)
        self.assertIn("empty", str_repr)
    
    def test_str_representation_with_items(self):
        """Test string representation with items."""
        self.pantry.add_item("Coffee", quantity=1.0, unit="bag")
        str_repr = str(self.pantry)
        self.assertIn("Pantry", str_repr)
        self.assertIn("Coffee", str_repr)


if __name__ == '__main__':
    unittest.main()
