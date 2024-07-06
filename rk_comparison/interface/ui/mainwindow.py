from PyQt6 import QtCore, QtGui, QtWidgets
from rk_comparison.interface.ui.plottingwindow import Ui_PlottingWindow
from rk_comparison.interface.ui.inputwindow import Ui_InputWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow, controller):
        self.controller = controller

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(243, 286)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.input_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.input_button.setGeometry(QtCore.QRect(60, 40, 121, 51))
        self.input_button.setObjectName("input_button")
        self.calculate_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(60, 120, 121, 51))
        self.calculate_button.setObjectName("calculate_button")
        self.exit_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(60, 200, 121, 51))
        self.exit_button.setObjectName("exit_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.MainWindow = MainWindow
        self.input_button.clicked.connect(self.input_clicked)
        self.calculate_button.clicked.connect(self.calculate_clicked)
        self.exit_button.clicked.connect(self.exit_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RK Comparison"))
        self.input_button.setText(_translate("MainWindow", "Input Data"))
        self.calculate_button.setText(_translate("MainWindow", "Calculate"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))

    def input_clicked(self):
        self.popup = QtWidgets.QDialog()
        self.popup_ui = Ui_InputWindow()
        self.popup_ui.setupUi(self.popup, self.controller)
        self.popup.show()

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
        self.popup_ui = Ui_PlottingWindow()
        self.popup_ui.setupUi(self.popup, self.controller)
        self.popup.show()

    def exit_clicked(self):
        self.MainWindow.close()
