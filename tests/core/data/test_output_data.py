import unittest
from rk_comparison.core.data.output_data import OutputData


class TestOutputData(unittest.TestCase):
    """Tests for the OutputData class."""

    def test_init(self):
        """Test to check constructor while creating the object."""
        data = OutputData()
        self.assertEqual([], data.resultRK1)
        self.assertEqual([], data.resultRK2)
        self.assertEqual([], data.resultRK3)
        self.assertEqual([], data.resultRK4)
        self.assertEqual([], data.resultRK5)
        self.assertEqual([], data.resultRK6)

        self.assertEqual([], data.resultFRK5)
        self.assertEqual([], data.resultFRK6)
        self.assertEqual([], data.resultFRK7)
        self.assertEqual([], data.resultFRK8)

        self.assertEqual([], data.resultAnalytical)
        self.assertEqual([], data.time)
        del data

    def test_set_result(self):
        """Test to check the method calling all set methods."""
        data = OutputData()
        data.set_results(50.0, 1.0)
        self.assertEqual([50.0], data.resultRK1)
        self.assertEqual([50.0], data.resultRK2)
        self.assertEqual([50.0], data.resultRK3)
        self.assertEqual([50.0], data.resultRK4)
        self.assertEqual([50.0], data.resultRK5)
        self.assertEqual([50.0], data.resultRK6)

        self.assertEqual([50.0], data.resultFRK5)
        self.assertEqual([50.0], data.resultFRK6)
        self.assertEqual([50.0], data.resultFRK7)
        self.assertEqual([50.0], data.resultFRK8)

        self.assertEqual([1.0], data.time)
        del data

    def test_set_result_analytical(self):
        """Tests the method to set the empty list for analytical results."""
        data = OutputData()
        data.set_result_analytical()
        self.assertEqual([], data.resultAnalytical)
        del data

    def test_get_result_analytical(self):
        """Tests the method to get the list of analytical results."""
        data = OutputData()
        self.assertEqual([], data.get_result_analytical())
        del data

    def test_set_resultRK1(self):
        """Tests the method to set the first element of list for RK1 results."""
        data = OutputData()
        data.set_resultRK1(1.0)
        self.assertEqual([1.0], data.resultRK1)
        del data

    def test_get_resultRK1(self):
        """Tests the method to get the list for RK1 results."""
        data = OutputData()
        self.assertEqual([], data.get_resultRK1())
        del data

    def test_set_resultRK2(self):
        """Tests the method to set the first element of list for RK2 results."""
        data = OutputData()
        data.set_resultRK2(1.0)
        self.assertEqual([1.0], data.resultRK2)
        del data

    def test_get_resultRK2(self):
        """Tests the method to get the list for RK2 results."""
        data = OutputData()
        self.assertEqual([], data.get_resultRK2())
        del data

    def test_set_resultRK3(self):
        """Tests the method to set the first element of list for RK3 results."""
        data = OutputData()
        data.set_resultRK3(1.0)
        self.assertEqual([1.0], data.resultRK3)
        del data

    def test_get_resultRK3(self):
        """Tests the method to get the list of RK3 results."""
        data = OutputData()
        self.assertEqual([], data.get_resultRK3())
        del data

    def test_set_resultRK4(self):
        """Tests the method to set the first element of list for RK4 results."""
        data = OutputData()
        data.set_resultRK4(1.0)
        self.assertEqual([1.0], data.resultRK4)
        del data

    def test_get_resultRK4(self):
        """Tests the method to get the list of RK4 results."""
        data = OutputData()
        self.assertEqual([], data.get_resultRK4())
        del data

    def test_set_resultRK5(self):
        """Tests the method to set the first element of list for RK5 results."""
        data = OutputData()
        data.set_resultRK5(1.0)
        self.assertEqual([1.0], data.resultRK5)
        del data

    def test_get_resultRK5(self):
        """Tests the method to get the list of RK5 results."""
        data = OutputData()
        self.assertEqual([], data.get_resultRK5())
        del data

    def test_set_resultRK6(self):
        """Tests the method to set the first element of list for RK6 results."""
        data = OutputData()
        data.set_resultRK6(1.0)
        self.assertEqual([1.0], data.resultRK6)
        del data

    def test_get_resultRK6(self):
        """Tests the method to get the list of RK6 results."""
        data = OutputData()
        self.assertEqual([], data.get_resultRK6())
        del data

    def test_set_resultFRK5(self):
        """Tests the method to set the first element of list for FRK5 results."""
        data = OutputData()
        data.set_resultFRK5(1.0)
        self.assertEqual([1.0], data.resultFRK5)
        del data

    def test_get_resultFRK5(self):
        """Tests the method to get the list of FRK5 results."""
        data = OutputData()
        self.assertEqual([], data.get_resultFRK5())
        del data

    def test_set_resultFRK6(self):
        """Tests the method to set the first element of list for FRK6 results."""
        data = OutputData()
        data.set_resultFRK6(1.0)
        self.assertEqual([1.0], data.resultFRK6)
        del data

    def test_get_resultFRK6(self):
        """Tests the method to get the list of FRK6 results."""
        data = OutputData()
        self.assertEqual([], data.get_resultFRK6())
        del data

    def test_set_resultFRK7(self):
        """Tests the method to set the first element of list for FRK7 results."""
        data = OutputData()
        data.set_resultFRK7(1.0)
        self.assertEqual([1.0], data.resultFRK7)
        del data

    def test_get_resultFRK7(self):
        """Tests the method to get the list of FRK7 results."""
        data = OutputData()
        self.assertEqual([], data.get_resultFRK7())
        del data

    def test_set_resultFRK8(self):
        """Tests the method to set the first element of list for FRK8 results."""
        data = OutputData()
        data.set_resultFRK8(1.0)
        self.assertEqual([1.0], data.resultFRK8)
        del data

    def test_get_resultFRK8(self):
        """Tests the method to get the list of FRK8 results."""
        data = OutputData()
        self.assertEqual([], data.get_resultFRK8())
        del data

    def test_set_time(self):
        """Tests the method to set the first element of time list."""
        data = OutputData()
        data.set_time(0.0)
        self.assertEqual([0.0], data.time)
        del data

    def test_get_time(self):
        """Tests the method to get the time list."""
        data = OutputData()
        self.assertEqual([], data.get_time())
        del data

    def test_set_time_final(self):
        """Tests the method to set the time list."""
        data = OutputData()
        data.set_time_final([0.0, 1.0, 2.0])
        self.assertEqual([0.0, 1.0, 2.0], data.time)
        del data


if __name__ == "__main__":
    unittest.main()
