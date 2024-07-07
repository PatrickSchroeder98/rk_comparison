from PyQt6 import QtWidgets
from rk_comparison.interface.design.ui_inputwindow import Ui_InputWindow
from rk_comparison.interface.ui.errorwindow import ErrorWindow


class InputWindow(QtWidgets.QDialog, Ui_InputWindow):

    def __init__(self, parent=None):
        super(InputWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.apply.clicked.connect(self.apply_clicked)
        self.cancel.clicked.connect(self.cancel_clicked)

    def initialize_controller(self, controller):
        self.controller = controller

    def apply_clicked(self):
        self.popup = QtWidgets.QDialog()
        self.popup_ui = ErrorWindow()
        self.popup_ui.set_message("This feature is not \n implemented yet.")
        self.popup_ui.exec()

    def cancel_clicked(self):
        self.close()

