from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PlottingWindow(object):
    def setupUi(self, PlottingWindow, controller):
        self.controller = controller

        PlottingWindow.setObjectName("PlottingWindow")
        PlottingWindow.resize(278, 278)
        self.plot_result = QtWidgets.QPushButton(parent=PlottingWindow)
        self.plot_result.setGeometry(QtCore.QRect(70, 30, 141, 51))
        self.plot_result.setObjectName("plot_result")
        self.plot_comparison = QtWidgets.QPushButton(parent=PlottingWindow)
        self.plot_comparison.setGeometry(QtCore.QRect(70, 110, 141, 51))
        self.plot_comparison.setObjectName("plot_comparison")
        self.cancel_button = QtWidgets.QPushButton(parent=PlottingWindow)
        self.cancel_button.setGeometry(QtCore.QRect(70, 190, 141, 51))
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(PlottingWindow)
        QtCore.QMetaObject.connectSlotsByName(PlottingWindow)

        self.PlottingWindow = PlottingWindow
        self.plot_result.clicked.connect(self.plot_results_clicked)
        self.plot_comparison.clicked.connect(self.plot_comparison_clicked)
        self.cancel_button.clicked.connect(self.cancel_clicked)

    def retranslateUi(self, PlottingWindow):
        _translate = QtCore.QCoreApplication.translate
        PlottingWindow.setWindowTitle(_translate("PlottingWindow", "Plotting"))
        self.plot_result.setText(_translate("PlottingWindow", "Plot result"))
        self.plot_comparison.setText(_translate("PlottingWindow", "Plot comparison"))
        self.cancel_button.setText(_translate("PlottingWindow", "Cancel"))

    def plot_results_clicked(self):
        self.controller.plot(True, self.controller.results_rk, "Nuclear Decay [nuclei]", "Nuclear Decay")

    def plot_comparison_clicked(self):
        self.controller.plot(False, self.controller.compare_rk, "Analytical - RK [nuclei]", "RK Comparison")

    def cancel_clicked(self):
        self.PlottingWindow.close()
