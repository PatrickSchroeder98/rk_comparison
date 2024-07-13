import unittest
from rk_comparison.core.data.input_data import InputData


class TestInputData(unittest.TestCase):
    """Tests for the InputData class."""

    def test_init(self):
        """Test to check constructor while creating the object."""
        data = InputData()
        self.assertEqual(0.0, data.t_min)
        self.assertEqual(0.05, data.dt)
        self.assertEqual(5.0, data.t_max)
        self.assertEqual(0.0, data.intervals)
        expected = [True, True, True, True, True, True, True, True, True, True]
        self.assertEqual(expected, data.truth_table)
        del data

    def test_set_t_min(self):
        """Tests the method to set the beginning of time period."""
        data = InputData()
        data.set_t_min(1.0)
        self.assertEqual(1.0, data.t_min)
        del data

    def test_get_t_min(self):
        """Tests the method to get the beginning of time period."""
        data = InputData()
        self.assertEqual(0.0, data.get_t_min())
        del data

    def test_set_dt(self):
        """Tests the method to set the delta of time period."""
        data = InputData()
        data.set_dt(0.1)
        self.assertEqual(0.1, data.dt)
        del data

    def test_get_dt(self):
        """Tests the method to get the delta of time period."""
        data = InputData()
        self.assertEqual(0.05, data.get_dt())
        del data

    def test_set_t_max(self):
        """Tests the method to set the ending of time period."""
        data = InputData()
        data.set_t_max(10.0)
        self.assertEqual(10.0, data.t_max)
        del data

    def test_get_t_max(self):
        """Tests the method to get the ending of time period."""
        data = InputData()
        self.assertEqual(5.0, data.get_t_max())
        del data

    def test_set_intervals(self):
        """Tests the method to count the intervals inside the time period."""
        data = InputData()
        data.set_t_min(1.0)
        data.set_t_max(10.0)
        data.set_dt(2.0)
        data.set_intervals()
        self.assertEqual(4, data.intervals)
        del data

    def test_get_intervals(self):
        """Tests the method to get the intervals inside the time period."""
        data = InputData()
        self.assertEqual(0.0, data.get_intervals())
        del data

    def test_set_truth_table(self):
        """Tests the method to set the truth table."""
        data = InputData()
        new_truth_table = [
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
            False,
        ]
        data.set_truth_table(new_truth_table)
        self.assertEqual(new_truth_table, data.truth_table)
        del data

    def test_get_truth_table(self):
        """Tests the method to get the truth table."""
        data = InputData()
        expected_truth_table = [
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
        ]
        self.assertEqual(expected_truth_table, data.get_truth_table())
        del data


if __name__ == "__main__":
    unittest.main()
