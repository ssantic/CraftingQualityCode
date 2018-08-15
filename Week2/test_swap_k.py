import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_longer_list(self):
    """Test from the function docstring."""
    	lst = [1, 2, 3, 4, 5, 6]

    	actual = a1.swap_k(lst, 2)
    	expected = [5, 6, 3, 4, 1, 2]

    	self.assertEqual(actual, expected)

    def test_empty_list(self):
    """Test passing in an empty list."""
        lst = []

        actual = a1.swap_k(lst, 1)
        expected = []

        self.assertEqual(actual, expected)

    def test_even_elements(self):
    """Test passing in an even number of elements."""
        lst = [1, 2, 3, 4]

        actual = a1.swap_k(lst, 2)
        expected = [3, 4, 1, 2]

        self.assertEqual(actual, expected)

    def test_odd_elements(self):
    """Test passing in an odd number of elements."""
        lst = [1, 2, 3]

        actual = a1.swap_k(lst, 1)
        expected = [3, 2, 1]

        
if __name__ == '__main__':
    unittest.main(exit=False)
