import unittest
from unittest.mock import MagicMock
from rk_comparison.core.analytical_module.rungekutta import RungeKutta
from rk_comparison.core.analytical_module.nuclear_decay import NuclearDecay


class TestRungeKutta(unittest.TestCase):
    """Tests for the RungeKutta class."""

    def test_rungekutta1(self):
        """Tests the RK1 method."""
        nd = NuclearDecay()
        rk = RungeKutta()
        t = [0.0]
        y = [100.0]
        nd.equation = MagicMock()
        rk.rungekutta1(nd.equation, t, y, 3, 1)

        self.assertEqual(nd.equation.call_count, 3)
        nd.equation.assert_any_call(0.0, 100.0)
        nd.equation.assert_any_call(1.0, y[1])
        nd.equation.assert_any_call(2.0, y[2])
        self.assertEqual([0.0, 1.0, 2.0, 3.0], t)
        self.assertEqual(4, len(y))
        del nd, rk

    def test_rungekutta2(self):
        """Tests the RK2 method."""
        nd = NuclearDecay()
        rk = RungeKutta()
        t = [0.0]
        y = [100.0]
        nd.equation = MagicMock()
        rk.rungekutta2(nd.equation, t, y, 3, 1)

        self.assertEqual(nd.equation.call_count, 6)
        nd.equation.assert_any_call(0.0, 100.0)
        nd.equation.assert_any_call(1.0, y[1])
        nd.equation.assert_any_call(2.0, y[2])
        self.assertEqual([0.0, 1.0, 2.0, 3.0], t)
        self.assertEqual(4, len(y))
        del nd, rk

    def test_rungekutta3(self):
        """Tests the RK3 method."""
        nd = NuclearDecay()
        rk = RungeKutta()
        t = [0.0]
        y = [100.0]
        nd.equation = MagicMock()
        rk.rungekutta3(nd.equation, t, y, 3, 1)

        self.assertEqual(nd.equation.call_count, 9)
        nd.equation.assert_any_call(0.0, 100.0)
        nd.equation.assert_any_call(1.0, y[1])
        nd.equation.assert_any_call(2.0, y[2])
        self.assertEqual([0.0, 1.0, 2.0, 3.0], t)
        self.assertEqual(4, len(y))
        del nd, rk

    def test_rungekutta4(self):
        """Tests the RK4 method."""
        nd = NuclearDecay()
        rk = RungeKutta()
        t = [0.0]
        y = [100.0]
        nd.equation = MagicMock()
        rk.rungekutta4(nd.equation, t, y, 3, 1)

        self.assertEqual(nd.equation.call_count, 12)
        nd.equation.assert_any_call(0.0, 100.0)
        nd.equation.assert_any_call(1.0, y[1])
        nd.equation.assert_any_call(2.0, y[2])
        self.assertEqual([0.0, 1.0, 2.0, 3.0], t)
        self.assertEqual(4, len(y))
        del nd, rk

    def test_rungekutta5(self):
        """Tests the RK5 method."""
        nd = NuclearDecay()
        rk = RungeKutta()
        t = [0.0]
        y = [100.0]
        nd.equation = MagicMock()
        rk.rungekutta5(nd.equation, t, y, 3, 1)

        self.assertEqual(nd.equation.call_count, 18)
        nd.equation.assert_any_call(0.0, 100.0)
        nd.equation.assert_any_call(1.0, y[1])
        nd.equation.assert_any_call(2.0, y[2])
        self.assertEqual([0.0, 1.0, 2.0, 3.0], t)
        self.assertEqual(4, len(y))
        del nd, rk

    def test_rungekutta6(self):
        """Tests the RK6 method."""
        nd = NuclearDecay()
        rk = RungeKutta()
        t = [0.0]
        y = [100.0]
        nd.equation = MagicMock()
        rk.rungekutta6(nd.equation, t, y, 3, 1)

        self.assertEqual(nd.equation.call_count, 24)
        nd.equation.assert_any_call(0.0, 100.0)
        nd.equation.assert_any_call(1.0, y[1])
        nd.equation.assert_any_call(2.0, y[2])
        self.assertEqual([0.0, 1.0, 2.0, 3.0], t)
        self.assertEqual(4, len(y))
        del nd, rk


if __name__ == "__main__":
    unittest.main()
