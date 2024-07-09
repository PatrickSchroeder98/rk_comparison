from PyQt6 import QtWidgets
from rk_comparison.interface.design.ui_plottingwindow import Ui_PlottingWindow
from rk_comparison.core.plotting_module.plot_data import PlotData


class PlottingWindow(QtWidgets.QDialog, Ui_PlottingWindow):

    def __init__(self, parent=None):
        super(PlottingWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.controller = None
        self.pl = PlotData()
        self.plot_result.clicked.connect(self.plot_results_clicked)
        self.plot_comparison.clicked.connect(self.plot_comparison_clicked)
        self.cancel_button.clicked.connect(self.cancel_clicked)
        self.plot_min.clicked.connect(self.min_clicked)
        self.plot_max.clicked.connect(self.max_clicked)
        self.plot_mean.clicked.connect(self.mean_clicked)

    def initialize_controller(self, controller):
        self.controller = controller

    def plot_results_clicked(self):
        self.pl.plot(True, self.controller, self.controller.results_rk, "Nuclear Decay [nuclei]", "Nuclear Decay")

    def plot_comparison_clicked(self):
        self.pl.plot(False, self.controller, self.controller.compare_rk, "Analytical - RK [nuclei]", "RK Comparison")

    def min_clicked(self):
        self.pl.prepare_plot_bar_min(self.controller)

    def max_clicked(self):
        self.pl.prepare_plot_bar_max(self.controller)

    def mean_clicked(self):
        self.pl.prepare_plot_bar_mean(self.controller)

    def cancel_clicked(self):
        self.close()
