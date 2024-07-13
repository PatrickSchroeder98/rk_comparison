import unittest
from rk_comparison.core.exceptions.checks import Checks


class TestChecks(unittest.TestCase):
    """Tests for the Checks class."""

    def test_str_to_float(self):
        """Test for successful conversion to flat."""
        data = Checks()
        result = data.str_to_float("T_min", "1.0")
        self.assertEqual(1.0, result)
        del data

    def test_str_to_float_fail(self):
        """Test for unsuccessful conversion to flat."""
        data = Checks()
        result = data.str_to_float("T_min", "x")
        self.assertEqual("T_min: Provided character is not a number.", result)
        del data

    def test_min_max_check(self):
        """Test for method checking if the start of time period is smaller or equal to it's end, for data that can
         satisfy this condition.
         """
        data = Checks()
        result = data.min_max_check(1.0, 2.0)
        self.assertIsNone(result)
        del data

    def test_min_max_check_fail(self):
        """Test for method checking if the start of time period is smaller or equal to it's end, for data that cannot
         satisfy this condition.
         """
        data = Checks()
        result = data.min_max_check(2.0, 1.0)
        self.assertEqual("Beginning of the time period is greater than the end.", result)
        del data

    def test_check_delta_zero(self):
        """Test for method checking delta, where the value is 0."""
        data = Checks()
        result = data.check_delta(1.0, 0.0, 5.0)
        self.assertEqual("Delta is equal to 0.", result)
        del data

    def test_check_delta_negative(self):
        """Test for method checking delta, where the value is negative."""
        data = Checks()
        result = data.check_delta(1.0, -1.0, 5.0)
        self.assertEqual("Delta is negative.", result)
        del data

    def test_check_delta_too_large(self):
        """Test for method checking delta, where the value is too large."""
        data = Checks()
        result = data.check_delta(1.0, 5.0, 5.0)
        self.assertEqual("Delta is too large for this time period.", result)
        del data

    def test_check_delta(self):
        """Test for method checking delta, where the value is correct."""
        data = Checks()
        result = data.check_delta(1.0, 1.0, 5.0)
        self.assertIsNone(result)
        del data

    def test_check_truth_table(self):
        """Test for method checking the truth table."""
        data = Checks()
        truth_table = [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            True
        ]
        result = data.check_truth_table(truth_table)
        self.assertIsNone(result)
        del data

    def test_check_truth_table_fail(self):
        """Test for method checking the truth table, where an incorrect one is given."""
        data = Checks()
        truth_table = [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False
        ]
        result = data.check_truth_table(truth_table)
        self.assertEqual("No numerical method chosen.", result)
        del data


if __name__ == "__main__":
    unittest.main()
