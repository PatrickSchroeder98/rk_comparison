import unittest
from unittest.mock import MagicMock
from rk_comparison.core.analytical_module.fehlbergrungekutta import FehlbergRungeKutta
from rk_comparison.core.analytical_module.nuclear_decay import NuclearDecay


class TestFehlbergRungeKutta(unittest.TestCase):
    """Tests for the FehlbergRungeKutta class."""

    def test_fehlbergrungekutta5(self):
        """Tests the FRK5 method."""
        nd = NuclearDecay()
        frk = FehlbergRungeKutta()
        t = [0.0]
        y = [100.0]
        nd.equation = MagicMock()
        frk.fehlbergrungekutta5(nd.equation, t, y, 3, 1)

        self.assertEqual(nd.equation.call_count, 24)
        nd.equation.assert_any_call(0.0, 100.0)
        nd.equation.assert_any_call(1.0, y[1])
        nd.equation.assert_any_call(2.0, y[2])
        self.assertEqual([0.0, 1.0, 2.0, 3.0], t)
        self.assertEqual(4, len(y))
        del nd, frk

    def test_fehlbergrungekutta6(self):
        """Tests the FRK6 method."""
        nd = NuclearDecay()
        frk = FehlbergRungeKutta()
        t = [0.0]
        y = [100.0]
        nd.equation = MagicMock()
        frk.fehlbergrungekutta6(nd.equation, t, y, 3, 1)

        self.assertEqual(nd.equation.call_count, 30)
        nd.equation.assert_any_call(0.0, 100.0)
        nd.equation.assert_any_call(1.0, y[1])
        nd.equation.assert_any_call(2.0, y[2])
        self.assertEqual([0.0, 1.0, 2.0, 3.0], t)
        self.assertEqual(4, len(y))
        del nd, frk

    def test_fehlbergrungekutta7(self):
        """Tests the FRK7 method."""
        nd = NuclearDecay()
        frk = FehlbergRungeKutta()
        t = [0.0]
        y = [100.0]
        nd.equation = MagicMock()
        frk.fehlbergrungekutta7(nd.equation, t, y, 3, 1)

        self.assertEqual(nd.equation.call_count, 39)
        nd.equation.assert_any_call(0.0, 100.0)
        nd.equation.assert_any_call(1.0, y[1])
        nd.equation.assert_any_call(2.0, y[2])
        self.assertEqual([0.0, 1.0, 2.0, 3.0], t)
        self.assertEqual(4, len(y))
        del nd, frk

    def test_fehlbergrungekutta8(self):
        """Tests the FRK8 method."""
        nd = NuclearDecay()
        frk = FehlbergRungeKutta()
        t = [0.0]
        y = [100.0]
        nd.equation = MagicMock()
        frk.fehlbergrungekutta8(nd.equation, t, y, 3, 1)

        self.assertEqual(nd.equation.call_count, 51)
        nd.equation.assert_any_call(0.0, 100.0)
        nd.equation.assert_any_call(1.0, y[1])
        nd.equation.assert_any_call(2.0, y[2])
        self.assertEqual([0.0, 1.0, 2.0, 3.0], t)
        self.assertEqual(4, len(y))
        del nd, frk


if __name__ == "__main__":
    unittest.main()
