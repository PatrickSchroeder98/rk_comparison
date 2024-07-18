import unittest
from pytestqt import qtbot
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt
from unittest.mock import MagicMock, patch
from rk_comparison.interface.ui.mainwindow import MainWindow
from rk_comparison.core.controller.controller import Controller
from rk_comparison.interface.ui.inputwindow import InputWindow
from rk_comparison.interface.ui.plottingwindow import PlottingWindow


class TestMainWindow:
    """Tests for the MainWindow class."""

    def test_init(self, qtbot):
        """Tests the types of attributes and the buttons connection to methods."""
        mw = MainWindow()
        qtbot.add_widget(mw)
        controller = Controller()

        assert type(mw.controller) == type(controller)
        assert mw.popup is None
        assert mw.popup_ui is None
        assert mw.input_button.clicked.connect(mw.input_clicked)
        assert mw.calculate_button.clicked.connect(mw.calculate_clicked)
        assert mw.exit_button.clicked.connect(mw.exit_clicked)
        del mw, controller

    @patch('rk_comparison.interface.ui.mainwindow.InputWindow')
    def test_input_clicked(self, mock_input_window, qtbot):
        """Tests the input_clicked method to ensure the input window is displayed correctly."""
        mw = MainWindow()
        qtbot.add_widget(mw)

        mock_dialog = MagicMock()
        mock_input_window.return_value = mock_dialog

        qtbot.mouseClick(mw.input_button, Qt.MouseButton.LeftButton)

        mock_input_window.assert_called_once()
        mock_dialog.initialize_data.assert_called_once_with(mw.controller)
        mock_dialog.exec.assert_called_once()
        popup = QtWidgets.QDialog()
        assert type(mw.popup) == type(popup)
        assert mw.popup_ui == mock_dialog
        del mw

    def test_calculate_clicked(self, qtbot):
        """Tests the calculate_clicked method to ensure calculations are performed and plot window is displayed."""
        mw = MainWindow()
        qtbot.add_widget(mw)

        mw.controller.id.set_t_min(0.0)
        mw.controller.id.set_dt(0.1)
        mw.controller.id.set_t_max(1.0)
        mw.controller.nd.set_nuclei(100)
        mw.controller.nd.set_tau(1.0)
        mw.controller.id.set_truth_table([True] * 10)

        mw.controller.calculate = MagicMock()
        mw.controller.calculate_analytical = MagicMock()
        mw.controller.compare = MagicMock()

        qtbot.mouseClick(mw.calculate_button, Qt.MouseButton.LeftButton)

        mw.controller.calculate.assert_called_once()
        mw.controller.calculate_analytical.assert_called_once()
        mw.controller.compare.assert_called_once()

        assert isinstance(mw.popup, QtWidgets.QDialog)
        assert isinstance(mw.popup_ui, PlottingWindow)

        mw.popup.close()
        del mw

    def test_exit_clicked(self, qtbot):
        """Test of the button to close the main window."""
        mw = MainWindow()
        qtbot.add_widget(mw)
        mw.exit_button.click()
        assert mw.close()
        del mw



if __name__ == "__main__":
    unittest.main()
