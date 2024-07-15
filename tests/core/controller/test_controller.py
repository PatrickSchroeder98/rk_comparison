import unittest
from rk_comparison.core.controller.controller import Controller


class TestController(unittest.TestCase):
    """Tests for the Controller class."""

    def test_init(self):
        """Test chosen attribute from controller class."""
        controller = Controller()
        descriptions = [
            "RK1",
            "RK2",
            "RK3",
            "RK4",
            "RK5",
            "RK6",
            "FRK5",
            "FRK6",
            "FRK7",
            "FRK8",
            "Analytical",
        ]
        self.assertEqual(descriptions, controller.descriptions)
        del controller

    def test_initialize(self):
        """Tests method to initialize new data."""
        controller = Controller()
        truth_table = [
            False,
            False,
            False,
            True,
            True,
            False,
            False,
            False,
            False,
            False
        ]
        controller.initialize(5.0, 1.0, 10.0, 500.0, 2.0, truth_table)
        self.assertEqual(5.0, controller.id.get_t_min())
        self.assertEqual(1.0, controller.id.get_dt())
        self.assertEqual(10.0, controller.id.get_t_max())
        self.assertEqual(500.0, controller.nd.get_nuclei())
        self.assertEqual(2.0, controller.nd.get_tau())
        self.assertEqual(truth_table, controller.id.get_truth_table())
        del controller

    def test_calculate(self):
        """Tests the calculate() method with default values."""
        controller = Controller()
        controller.id.truth_table = [
            False,
            False,
            False,
            True,
            False,
            False,
            False,
            False,
            False,
            False
        ]
        controller.rs.time = [0.0]
        controller.rs.resultRK4 = [100.0]
        controller.id.intervals = 100
        self.assertEqual(1, len(controller.rs.resultRK4))
        self.assertEqual(1, len(controller.rs.time))
        controller.calculate()
        self.assertEqual(101, len(controller.rs.resultRK4))
        self.assertEqual(101, len(controller.rs.time))
        del controller

    def test_calculate_analytical(self):
        """Tests the calculate_analytical() method with default values and custom time period."""
        controller = Controller()
        controller.rs.time = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.assertEqual(0, len(controller.rs.resultAnalytical))
        controller.calculate_analytical()
        self.assertEqual(5, len(controller.rs.resultAnalytical))
        del controller

    def test_compare(self):
        """Tests the method that compares RK and FRK results with analytical solution."""
        controller = Controller()
        controller.id.truth_table = [
            False,
            False,
            False,
            True,
            False,
            False,
            False,
            False,
            False,
            False
        ]
        controller.rs.resultAnalytical = [30.0, 20.0, 10.0]
        controller.rs.resultRK4 = [33.0, 22.0, 11.0]
        self.assertEqual([], controller.cd.compareRK4)
        controller.compare()
        self.assertEqual([3.0, 2.0, 1.0], controller.cd.compareRK4)
        del controller


if __name__ == "__main__":
    unittest.main()
