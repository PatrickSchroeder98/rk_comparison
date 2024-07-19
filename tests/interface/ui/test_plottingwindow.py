import unittest
from unittest.mock import MagicMock, patch, mock_open
from pytestqt import qtbot
from PyQt6 import QtWidgets
from rk_comparison.interface.ui.plottingwindow import PlottingWindow
from rk_comparison.core.controller.controller import Controller
from rk_comparison.core.plotting_module.plot_data import PlotData
from rk_comparison.interface.ui.errorwindow import ErrorWindow
from rk_comparison.core.saving_module.save_data import SaveData


class TestPlottingWindow:
    """Tests for the PlottingWindow class."""

    def test_init(self, qtbot):
        """Tests the types of attributes and the buttons connection to methods."""
        pw = PlottingWindow()
        qtbot.add_widget(pw)
        controller = Controller()

        assert pw.controller is None
        assert isinstance(pw.pl, PlotData)
        assert isinstance(pw.er, ErrorWindow)
        assert isinstance(pw.sv, SaveData)
        assert pw.plot_result.clicked.connect(pw.plot_results_clicked)
        assert pw.plot_comparison.clicked.connect(pw.plot_comparison_clicked)
        assert pw.cancel_button.clicked.connect(pw.cancel_clicked)
        assert pw.plot_min.clicked.connect(pw.min_clicked)
        assert pw.plot_max.clicked.connect(pw.max_clicked)
        assert pw.plot_mean.clicked.connect(pw.mean_clicked)
        assert pw.save_button.clicked.connect(pw.save_clicked)
        del pw, controller

    def test_initialize_controller(self, qtbot):
        """Tests the initialize_controller method."""
        pw = PlottingWindow()
        qtbot.add_widget(pw)
        controller = Controller()

        pw.initialize_controller(controller)
        assert pw.controller == controller
        del pw, controller

    def test_plot_results_clicked(self, qtbot):
        """Tests the plot_results_clicked method."""
        pw = PlottingWindow()
        qtbot.add_widget(pw)
        controller = Controller()
        pw.initialize_controller(controller)

        pw.pl.plot = MagicMock()
        pw.plot_result.click()

        pw.pl.plot.assert_called_once_with(
            True,
            pw.controller,
            pw.controller.results_rk,
            "Nuclear Decay [nuclei]",
            "Nuclear Decay",
        )
        del pw, controller

    def test_plot_comparison_clicked(self, qtbot):
        """Tests the plot_comparison_clicked method."""
        pw = PlottingWindow()
        qtbot.add_widget(pw)
        controller = Controller()
        pw.initialize_controller(controller)

        pw.pl.plot = MagicMock()
        pw.plot_comparison.click()

        pw.pl.plot.assert_called_once_with(
            False,
            pw.controller,
            pw.controller.compare_rk,
            "Analytical - RK [nuclei]",
            "RK Comparison",
        )
        del pw, controller

    def test_min_clicked(self, qtbot):
        """Tests the min_clicked method."""
        pw = PlottingWindow()
        qtbot.add_widget(pw)
        controller = Controller()
        pw.initialize_controller(controller)

        pw.pl.prepare_plot_bar_min = MagicMock()
        pw.plot_min.click()

        pw.pl.prepare_plot_bar_min.assert_called_once_with(
            pw.controller,
            "Numerical Methods",
            "Min(Analytical - RK) [nuclei]",
            "Minimal value of comparison",
        )
        del pw, controller

    def test_max_clicked(self, qtbot):
        """Tests the max_clicked method."""
        pw = PlottingWindow()
        qtbot.add_widget(pw)
        controller = Controller()
        pw.initialize_controller(controller)

        pw.pl.prepare_plot_bar_max = MagicMock()
        pw.plot_max.click()

        pw.pl.prepare_plot_bar_max.assert_called_once_with(
            pw.controller,
            "Numerical Methods",
            "Max(Analytical - RK) [nuclei]",
            "Maximal value of comparison",
        )
        del pw, controller

    def test_mean_clicked(self, qtbot):
        """Tests the mean_clicked method."""
        pw = PlottingWindow()
        qtbot.add_widget(pw)
        controller = Controller()
        pw.initialize_controller(controller)

        pw.pl.prepare_plot_bar_mean = MagicMock()
        pw.plot_mean.click()

        pw.pl.prepare_plot_bar_mean.assert_called_once_with(
            pw.controller,
            "Numerical Methods",
            "Mean(Analytical - RK) [nuclei]",
            "Mean value of comparison",
        )
        del pw, controller

    def test_save_clicked(self, qtbot, monkeypatch):
        """Tests the save_clicked method."""
        pw = PlottingWindow()
        qtbot.add_widget(pw)
        controller = Controller()
        pw.initialize_controller(controller)

        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setNameFilter = MagicMock()
        file_dialog.exec = MagicMock(return_value=True)
        file_dialog.selectedFiles = MagicMock(return_value=["test.csv"])

        monkeypatch.setattr(QtWidgets, "QFileDialog", lambda: file_dialog)

        pw.sv.save = MagicMock()

        m_open = mock_open()
        with patch("builtins.open", m_open):
            pw.save_button.click()

        pw.sv.save.assert_called_once()
        m_open.assert_called_once_with("test.csv", mode="w", newline='')

        del pw, controller

    def test_cancel_clicked(self, qtbot):
        """Tests the cancel_clicked method."""
        pw = PlottingWindow()
        qtbot.add_widget(pw)

        pw.cancel_button.click()
        assert pw.close()
        del pw


if __name__ == "__main__":
    unittest.main()
