from rk_comparison.interface.design.ui_errorwindow import Ui_ErrorWindow
from PyQt6 import QtWidgets

class ErrorWindow(QtWidgets.QDialog, Ui_ErrorWindow):

    def __init__(self, parent=None):
        super(ErrorWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.ok_clicked)

    def set_message(self, message):
        self.label.setText(message)

    def ok_clicked(self):
        self.close()
