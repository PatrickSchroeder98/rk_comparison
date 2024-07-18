import pytest
from PyQt6 import QtWidgets
from unittest.mock import MagicMock
from rk_comparison.interface.ui.inputwindow import InputWindow
from rk_comparison.core.controller.controller import Controller


class TestInputWindow:
    """Tests for the InputWindow class."""

    def test_init(self, qtbot):
        """Tests the types of attributes and the buttons connection to methods."""
        iw = InputWindow()
        qtbot.add_widget(iw)

        assert iw.controller is None
        assert iw.popup is None
        assert iw.popup_ui is None
        assert iw.apply.clicked.connect(iw.apply_clicked)
        assert iw.cancel.clicked.connect(iw.cancel_clicked)
        del iw

    def test_initialize_data(self, qtbot):
        """Tests the method to initialize data in the input window."""
        iw = InputWindow()
        qtbot.add_widget(iw)

        controller = MagicMock()
        controller.id.get_t_min.return_value = 0.0
        controller.id.get_dt.return_value = 1.0
        controller.id.get_t_max.return_value = 10.0
        controller.nd.get_tau.return_value = 5.0
        controller.nd.get_nuclei.return_value = 100.0
        controller.id.get_truth_table.return_value = [
            True,
            False,
            True,
            False,
            True,
            False,
            True,
            False,
            True,
            False,
        ]

        iw.initialize_data(controller)

        assert iw.line_t_min.text() == "0.0"
        assert iw.line_delta.text() == "1.0"
        assert iw.line_t_max.text() == "10.0"
        assert iw.line_tau.text() == "5.0"
        assert iw.line_nuclei.text() == "100.0"
        assert iw.truth[0].isChecked() is True
        assert iw.truth[1].isChecked() is False
        assert iw.truth[2].isChecked() is True
        assert iw.truth[3].isChecked() is False

        del iw

    def test_apply_clicked_valid_data(self, qtbot, monkeypatch):
        """Tests the apply_clicked method with valid input data."""
        iw = InputWindow()
        qtbot.add_widget(iw)

        controller = MagicMock()
        iw.initialize_data(controller)

        iw.line_t_min.setText("0.0")
        iw.line_delta.setText("1.0")
        iw.line_t_max.setText("10.0")
        iw.line_tau.setText("5.0")
        iw.line_nuclei.setText("100.0")

        for i, checkbox in enumerate(iw.truth):
            checkbox.setChecked(True if i % 2 == 0 else False)

        iw.checks.min_max_check = MagicMock(return_value=None)
        iw.checks.check_delta = MagicMock(return_value=None)
        iw.checks.check_truth_table = MagicMock(return_value=None)
        iw.change_type = MagicMock(return_value=True)

        iw.data_placeholders = [
            0.0,
            1.0,
            10.0,
            100.0,
            5.0,
            [True, False, True, False, True, False, True, False, True, False],
        ]
        iw.apply_clicked()

        iw.checks.min_max_check.assert_called_once()
        iw.checks.check_delta.assert_called_once()
        iw.checks.check_truth_table.assert_called_once()

        controller.initialize.assert_called_once_with(
            0.0,
            1.0,
            10.0,
            100.0,
            5.0,
            [True, False, True, False, True, False, True, False, True, False],
        )
        assert iw.close()
        del iw

    def test_apply_clicked_invalid_data(self, qtbot, monkeypatch):
        """Tests the apply_clicked method with invalid input data."""
        iw = InputWindow()
        qtbot.add_widget(iw)

        iw.line_t_min.setText("invalid")
        iw.line_delta.setText("1.0")
        iw.line_t_max.setText("10.0")
        iw.line_tau.setText("5.0")
        iw.line_nuclei.setText("100.0")

        iw.checks.str_to_float = MagicMock(return_value="error")
        iw.raise_error = MagicMock()

        iw.apply_clicked()

        iw.raise_error.assert_called_once()
        del iw

    def test_cancel_clicked(self, qtbot):
        """Tests the method to cancel and close the input window."""
        iw = InputWindow()
        qtbot.add_widget(iw)

        iw.cancel_clicked()

        assert iw.close()
        del iw

    def test_raise_error(self, qtbot, monkeypatch):
        """Tests the method to raise an error message."""
        iw = InputWindow()
        qtbot.add_widget(iw)

        mock_error_window = MagicMock()
        monkeypatch.setattr(
            "rk_comparison.interface.ui.inputwindow.ErrorWindow",
            lambda: mock_error_window,
        )

        iw.raise_error("Test error message")

        mock_error_window.set_message.assert_called_once_with("Test error message")
        mock_error_window.exec.assert_called_once()
        del iw


if __name__ == "__main__":
    pytest.main()
