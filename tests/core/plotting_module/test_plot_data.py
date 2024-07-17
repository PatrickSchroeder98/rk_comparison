import unittest
from rk_comparison.core.plotting_module.plot_data import PlotData
from rk_comparison.core.plotting_module.plot import Plot
from rk_comparison.core.controller.controller import Controller
from unittest.mock import MagicMock


class TestPlotData(unittest.TestCase):
    """Tests for the PlotData class."""

    def test_init(self):
        """Tests the constructor."""
        pd = PlotData()
        pl = Plot()
        self.assertEqual(type(pl), type(pd.pl))
        del pd, pl

    def test_plot(self):
        """Tests the plot method."""
        pd = PlotData()
        pd.pl = MagicMock()
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
        controller.cd.compareRK4 = [1.0, 2.0, 3.0]
        controller.rs.time = [1.0, 2.0, 3.0]
        pd.plot(False, controller, controller.compare_rk, "Test y label", "Test title")
        pd.pl.plot.assert_called_once_with([1.0, 2.0, 3.0], [[1.0, 2.0, 3.0]], "Time [s]", "Test y label", ['RK4'], "Test title")
        del pd, controller

    def test_plot_with_compare(self):
        """Tests the plot method with analytical solution included."""
        pd = PlotData()
        pd.pl = MagicMock()
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
        controller.rs.resultRK4 = [1.0, 2.0, 3.0]
        controller.rs.time = [1.0, 2.0, 3.0]
        controller.rs.resultAnalytical = [1.1, 2.2, 3.3]
        pd.plot(True, controller, controller.results_rk, "Test y label", "Test title")
        pd.pl.plot.assert_called_once_with([1.0, 2.0, 3.0], [[1.0, 2.0, 3.0], [1.1, 2.2, 3.3]], "Time [s]", "Test y label", ['RK4', "Analytical"], "Test title")
        del pd, controller


    def test_prepare_plot_bar_min(self):
        """Tests the method preparing data for bar plot with min values."""
        pd = PlotData()
        pd.pl = MagicMock()
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
        controller.cd.min_values = [1.0]
        pd.prepare_plot_bar_min(controller, "Test x label", "Test y label", "Test title")
        pd.pl.plot_bar.assert_called_with(["RK4"], [1.0], "Test x label", "Test y label", "Test title")
        del pd, controller

    def test_prepare_plot_bar_max(self):
        """Tests the method preparing data for bar plot with max values."""
        pd = PlotData()
        pd.pl = MagicMock()
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
        controller.cd.max_values = [1.0]
        pd.prepare_plot_bar_max(controller, "Test x label", "Test y label", "Test title")
        pd.pl.plot_bar.assert_called_with(["RK4"], [1.0], "Test x label", "Test y label", "Test title")
        del pd, controller

    def test_prepare_plot_bar_mean(self):
        """Tests the method preparing data for bar plot with mean values."""
        pd = PlotData()
        pd.pl = MagicMock()
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
        controller.cd.mean_values = [1.0]
        pd.prepare_plot_bar_mean(controller, "Test x label", "Test y label", "Test title")
        pd.pl.plot_bar.assert_called_with(["RK4"], [1.0], "Test x label", "Test y label", "Test title")
        del pd, controller


if __name__ == "__main__":
    unittest.main()
