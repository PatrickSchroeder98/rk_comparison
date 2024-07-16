import unittest
from rk_comparison.core.data.comparison_data import ComparisonData


class TestComparisonData(unittest.TestCase):
    """Tests for the ComparisonData class."""

    def test_init(self):
        """Tests the constructor initializing empty lists."""
        data = ComparisonData()
        self.assertEqual([], data.get_compareRK1())
        self.assertEqual([], data.get_compareRK2())
        self.assertEqual([], data.get_compareRK3())
        self.assertEqual([], data.get_compareRK4())
        self.assertEqual([], data.get_compareRK5())
        self.assertEqual([], data.get_compareRK6())
        self.assertEqual([], data.get_compareFRK5())
        self.assertEqual([], data.get_compareFRK6())
        self.assertEqual([], data.get_compareFRK7())
        self.assertEqual([], data.get_compareFRK8())
        self.assertEqual([], data.get_min_values())
        self.assertEqual([], data.get_max_values())
        self.assertEqual([], data.get_mean_values())
        del data

    def test_clean_data(self):
        """Tests the method to clean all data lists."""
        data = ComparisonData()
        data.compareRK1 = [1.0]
        data.compareRK2 = [1.0]
        data.compareRK3 = [1.0]
        data.compareRK4 = [1.0]
        data.compareRK5 = [1.0]
        data.compareRK6 = [1.0]
        data.compareFRK5 = [1.0]
        data.compareFRK6 = [1.0]
        data.compareFRK7 = [1.0]
        data.compareFRK8 = [1.0]
        data.min_values = [1.0]
        data.max_values = [1.0]
        data.mean_values = [1.0]
        data.clean_data()
        self.assertEqual([], data.get_compareRK1())
        self.assertEqual([], data.get_compareRK2())
        self.assertEqual([], data.get_compareRK3())
        self.assertEqual([], data.get_compareRK4())
        self.assertEqual([], data.get_compareRK5())
        self.assertEqual([], data.get_compareRK6())
        self.assertEqual([], data.get_compareFRK5())
        self.assertEqual([], data.get_compareFRK6())
        self.assertEqual([], data.get_compareFRK7())
        self.assertEqual([], data.get_compareFRK8())
        self.assertEqual([], data.get_min_values())
        self.assertEqual([], data.get_max_values())
        self.assertEqual([], data.get_mean_values())
        del data

    def test_set_compareRK1(self):
        """Tests the method to set compareRK1 element."""
        data = ComparisonData()
        data.set_compareRK1(1.0)
        self.assertEqual([1.0], data.compareRK1)
        del data

    def test_get_compareRK1(self):
        """Tests the method to return the compareRK1 list."""
        data = ComparisonData()
        self.assertEqual([], data.get_compareRK1())
        del data

    def test_set_compareRK2(self):
        """Tests the method to set compareRK2 element."""
        data = ComparisonData()
        data.set_compareRK2(1.0)
        self.assertEqual([1.0], data.compareRK2)
        del data

    def test_get_compareRK2(self):
        """Tests the method to return the compareRK2 list."""
        data = ComparisonData()
        self.assertEqual([], data.get_compareRK2())
        del data

    def test_set_compareRK3(self):
        """Tests the method to set compareRK3 element."""
        data = ComparisonData()
        data.set_compareRK3(1.0)
        self.assertEqual([1.0], data.compareRK3)
        del data

    def test_get_compareRK3(self):
        """Tests the method to return the compareRK3 list."""
        data = ComparisonData()
        self.assertEqual([], data.get_compareRK3())
        del data

    def test_set_compareRK4(self):
        """Tests the method to set compareRK4 element."""
        data = ComparisonData()
        data.set_compareRK4(1.0)
        self.assertEqual([1.0], data.compareRK4)
        del data

    def test_get_compareRK4(self):
        """Tests the method to return the compareRK4 list."""
        data = ComparisonData()
        self.assertEqual([], data.get_compareRK4())
        del data

    def test_set_compareRK5(self):
        """Tests the method to set compareRK5 element."""
        data = ComparisonData()
        data.set_compareRK5(1.0)
        self.assertEqual([1.0], data.compareRK5)
        del data

    def test_get_compareRK5(self):
        """Tests the method to return the compareRK5 list."""
        data = ComparisonData()
        self.assertEqual([], data.get_compareRK5())
        del data

    def test_set_compareRK6(self):
        """Tests the method to set compareRK6 element."""
        data = ComparisonData()
        data.set_compareRK6(1.0)
        self.assertEqual([1.0], data.compareRK6)
        del data

    def test_get_compareRK6(self):
        """Tests the method to return the compareRK6 list."""
        data = ComparisonData()
        self.assertEqual([], data.get_compareRK6())
        del data

    def test_set_compareFRK5(self):
        """Tests the method to set compareFRK5 element."""
        data = ComparisonData()
        data.set_compareFRK5(1.0)
        self.assertEqual([1.0], data.compareFRK5)
        del data

    def test_get_compareFRK5(self):
        """Tests the method to return the compareFRK5 list."""
        data = ComparisonData()
        self.assertEqual([], data.get_compareFRK5())
        del data

    def test_set_compareFRK6(self):
        """Tests the method to set compareFRK6 element."""
        data = ComparisonData()
        data.set_compareFRK6(1.0)
        self.assertEqual([1.0], data.compareFRK6)
        del data

    def test_get_compareFRK6(self):
        """Tests the method to return the compareFRK6 list."""
        data = ComparisonData()
        self.assertEqual([], data.get_compareFRK6())
        del data

    def test_set_compareFRK7(self):
        """Tests the method to set compareFRK7 element."""
        data = ComparisonData()
        data.set_compareFRK7(1.0)
        self.assertEqual([1.0], data.compareFRK7)
        del data

    def test_get_compareFRK7(self):
        """Tests the method to return the compareFRK7 list."""
        data = ComparisonData()
        self.assertEqual([], data.get_compareFRK7())
        del data

    def test_set_compareFRK8(self):
        """Tests the method to set compareFRK8 element."""
        data = ComparisonData()
        data.set_compareFRK8(1.0)
        self.assertEqual([1.0], data.compareFRK8)
        del data

    def test_get_compareFRK8(self):
        """Tests the method to return the compareFRK8 list."""
        data = ComparisonData()
        self.assertEqual([], data.get_compareFRK8())
        del data

    def test_set_min_values(self):
        """Tests the method to set min_values element."""
        data = ComparisonData()
        data.set_min_values(1.0)
        self.assertEqual([1.0], data.min_values)
        del data

    def test_get_min_values(self):
        """Tests the method to return the min_values list."""
        data = ComparisonData()
        self.assertEqual([], data.get_min_values())
        del data

    def test_set_max_values(self):
        """Tests the method to set max_values element."""
        data = ComparisonData()
        data.set_max_values(1.0)
        self.assertEqual([1.0], data.max_values)
        del data

    def test_get_max_values(self):
        """Tests the method to return the max_values list."""
        data = ComparisonData()
        self.assertEqual([], data.get_max_values())
        del data

    def test_set_mean_values(self):
        """Tests the method to set mean_values element."""
        data = ComparisonData()
        data.set_mean_values(1.0)
        self.assertEqual([1.0], data.mean_values)
        del data

    def test_get_mean_values(self):
        """Tests the method to return the mean_values list."""
        data = ComparisonData()
        self.assertEqual([], data.get_mean_values())
        del data


if __name__ == "__main__":
    unittest.main()
