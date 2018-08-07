import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_one_passenger(self):
    """Test with only one passenger present."""
    actual = a1.num_buses(1)
    expected = 1

    self.assertEqual(actual, expected)

    def test_exact_multiple(self):
    """Test with exactly 50 passengers."""
    actual = a1.num_buses(50)
    expected = 1

    self.assertEqual(actual, expected)

    def test_not_exact_multiple(self):
    """Test with a value that isn't divisible by 50."""
    actual = a1.num_buses(125)
    expected = 3

    self.assertEqual(actual, expected)

    def test_several_multiples(self):
    """Test with a value that is several times over 50."""
    actual = a1.num_buses(300)
    expected = 6

    self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main(exit=False)
