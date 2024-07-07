from rk_comparison.interface.design.ui_plottingwindow import Ui_PlottingWindow
from PyQt6 import QtWidgets


class PlottingWindow(QtWidgets.QDialog, Ui_PlottingWindow):

    def __init__(self, parent=None):
        super(PlottingWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.plot_result.clicked.connect(self.plot_results_clicked)
        self.plot_comparison.clicked.connect(self.plot_comparison_clicked)
        self.cancel_button.clicked.connect(self.cancel_clicked)

    def initialize_controller(self, controller):
        self.controller = controller

    def plot_results_clicked(self):
        self.controller.plot(True, self.controller.results_rk, "Nuclear Decay [nuclei]", "Nuclear Decay")

    def plot_comparison_clicked(self):
        self.controller.plot(False, self.controller.compare_rk, "Analytical - RK [nuclei]", "RK Comparison")

    def cancel_clicked(self):
        self.close()
