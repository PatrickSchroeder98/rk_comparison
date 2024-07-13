import unittest
from rk_comparison.core.analytical_module.statistics import Statistics


class TestStatistics(unittest.TestCase):
    """Tests for the Statistics class."""

    def test_min(self):
        """Test for finding minimal value in a list."""
        st = Statistics()
        result = st.min_max_value([3, 9, 6, 1, 2, 5], True)
        self.assertEqual(1, result)
        del st

    def test_max(self):
        """Test for finding maximal value in a list."""
        st = Statistics()
        result = st.min_max_value([3, 9, 6, 1, 2, 5], False)
        self.assertEqual(9, result)
        del st

    def test_mean(self):
        """Test for finding mean value from all elements of list."""
        st = Statistics()
        result = st.mean([3, 9, 10, 1, 2, 5])
        self.assertEqual(5, result)
        del st


if __name__ == '__main__':
    unittest.main()
