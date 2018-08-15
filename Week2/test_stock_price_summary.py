import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_several_values(self):
    """Test a list of different values, from the example."""    	
    	actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
    	expected = (0.14, -0.17)

    	self.assertEqual(actual, expected)

    def test_single_zero(self):
    """Test with just a 0 as input."""
        actual = a1.stock_price_summary([0])
        expected = (0, 0)

        self.assertEqual(actual, expected)

    def test_one_loss(self):
    """Test just one loss as input."""
    	actual = a1.stock_price_summary(-0.16)
    	expected = (0, -0.16)

    	self.assertEqual(actual, expected)

    def test_one_gain(self):
    """Test just one gain as input."""
        actual = a1.stock_price_summary([0.24])
        expected = (0.24, 0)

        self.assertEqual(actual, expected)

    def test_empty_list(self):
    """Test and empty list as input."""
        actual = a1.stock_price_summary([])
        expected = (0,0)

    
if __name__ == '__main__':
    unittest.main(exit=False)
