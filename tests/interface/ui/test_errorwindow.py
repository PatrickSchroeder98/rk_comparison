import unittest
from pytestqt import qtbot
from rk_comparison.interface.ui.errorwindow import ErrorWindow


class TestErrorWindow:
    """Tests for the ErrorWindow class."""

    def test_init(self, qtbot):
        """Tests the button connection to method."""
        ew = ErrorWindow()
        qtbot.add_widget(ew)
        assert ew.pushButton.clicked.connect(ew.ok_clicked)

    def test_set_message(self, qtbot):
        """Tests the set_message() method."""
        ew = ErrorWindow()
        qtbot.add_widget(ew)
        ew.set_message("Test error message.")
        assert ew.label.text() == "Test error message."
        del ew

    def test_ok_clicked(self, qtbot):
        """Test of the button to close the error window."""
        ew = ErrorWindow()
        qtbot.add_widget(ew)
        ew.pushButton.click()
        assert ew.close()
        del ew


if __name__ == "__main__":
    unittest.main()
