# test_exchangedatacore.py
"""
Tests for ExchangeDataCore module.
"""

import unittest
from exchangedatacore import ExchangeDataCore

class TestExchangeDataCore(unittest.TestCase):
    """Test cases for ExchangeDataCore class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ExchangeDataCore()
        self.assertIsInstance(instance, ExchangeDataCore)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ExchangeDataCore()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
