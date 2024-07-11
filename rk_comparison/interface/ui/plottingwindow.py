from PyQt6 import QtWidgets
from rk_comparison.interface.design.ui_plottingwindow import Ui_PlottingWindow
from rk_comparison.core.plotting_module.plot_data import PlotData
from rk_comparison.interface.ui.errorwindow import ErrorWindow
from rk_comparison.core.saving_module.save_data import SaveData

class PlottingWindow(QtWidgets.QDialog, Ui_PlottingWindow):

    def __init__(self, parent=None):
        super(PlottingWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.controller = None
        self.popup = None
        self.popup_ui = None
        self.pl = PlotData()
        self.er = ErrorWindow()
        self.sv = SaveData()
        self.plot_result.clicked.connect(self.plot_results_clicked)
        self.plot_comparison.clicked.connect(self.plot_comparison_clicked)
        self.cancel_button.clicked.connect(self.cancel_clicked)
        self.plot_min.clicked.connect(self.min_clicked)
        self.plot_max.clicked.connect(self.max_clicked)
        self.plot_mean.clicked.connect(self.mean_clicked)
        self.save_button.clicked.connect(self.save_clicked)

    def initialize_controller(self, controller):
        self.controller = controller

    def plot_results_clicked(self):
        self.pl.plot(
            True,
            self.controller,
            self.controller.results_rk,
            "Nuclear Decay [nuclei]",
            "Nuclear Decay",
        )

    def plot_comparison_clicked(self):
        self.pl.plot(
            False,
            self.controller,
            self.controller.compare_rk,
            "Analytical - RK [nuclei]",
            "RK Comparison",
        )

    def min_clicked(self):
        self.pl.prepare_plot_bar_min(
            self.controller,
            "Numerical Methods",
            "Min(Analytical - RK) [nuclei]",
            "Minimal value of comparison",
        )

    def max_clicked(self):
        self.pl.prepare_plot_bar_max(
            self.controller,
            "Numerical Methods",
            "Max(Analytical - RK) [nuclei]",
            "Maximal value of comparison",
        )

    def mean_clicked(self):
        self.pl.prepare_plot_bar_mean(
            self.controller,
            "Numerical Methods",
            "Mean(Analytical - RK) [nuclei]",
            "Mean value of comparison",
        )

    def save_clicked(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setNameFilter("*.csv")
        dialog_successful = dialog.exec()

        if dialog_successful:
            file_location = dialog.selectedFiles()[0]
            try:
                with open(file_location, mode="w", newline='') as file:
                    self.sv.save(file, self.controller)
            except PermissionError as e:
                self.popup = QtWidgets.QDialog()
                self.popup_ui = ErrorWindow()
                self.popup_ui.set_message(str(e)[11:])
                self.popup_ui.exec()

    def cancel_clicked(self):
        self.close()
