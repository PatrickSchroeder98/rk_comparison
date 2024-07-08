from PyQt6 import QtWidgets
from rk_comparison.interface.design.ui_mainwindow import Ui_MainWindow
from rk_comparison.interface.ui.inputwindow import InputWindow
from rk_comparison.interface.ui.plottingwindow import PlottingWindow
from rk_comparison.core.controller.controller import Controller


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.popup = None
        self.popup_ui = None
        self.controller = Controller()
        self.input_button.clicked.connect(self.input_clicked)
        self.calculate_button.clicked.connect(self.calculate_clicked)
        self.exit_button.clicked.connect(self.exit_clicked)

    def input_clicked(self):
        self.popup = QtWidgets.QDialog()
        self.popup_ui = InputWindow()
        self.popup_ui.initialize_data(self.controller)
        self.popup_ui.exec()

    def calculate_clicked(self):
        self.controller.initialize(self.controller.id.get_t_min(),
                                   self.controller.id.get_dt(),
                                   self.controller.id.get_t_max(),
                                   self.controller.nd.get_nuclei(),
                                   self.controller.nd.get_tau(),
                                   self.controller.id.get_truth_table())
        self.controller.calculate()
        self.controller.calculate_analytical()
        self.controller.compare()

        self.popup = QtWidgets.QDialog()
        self.popup_ui = PlottingWindow()
        self.popup_ui.initialize_controller(self.controller)
        self.popup_ui.show()

    def exit_clicked(self):
        self.close()
