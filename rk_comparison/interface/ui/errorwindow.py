from PyQt6 import QtWidgets
from rk_comparison.interface.design.ui_errorwindow import Ui_ErrorWindow


class ErrorWindow(QtWidgets.QDialog, Ui_ErrorWindow):
    """Class for setting up the error window."""

    def __init__(self, parent=None):
        """Constructor calls setup method that builds the widget."""
        super(ErrorWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ok_clicked)

    def set_message(self, message):
        """Label can display a message given in argument."""
        self.label.setText(message)

    def ok_clicked(self):
        """User can close the window by clicking the button."""
        self.close()
