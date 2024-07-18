from PyQt6 import QtWidgets
from rk_comparison.interface.design.ui_inputwindow import Ui_InputWindow
from rk_comparison.interface.ui.errorwindow import ErrorWindow
from rk_comparison.core.exceptions.checks import Checks


class InputWindow(QtWidgets.QDialog, Ui_InputWindow):
    """Class for setting up the input window."""

    def __init__(self, parent=None):
        """Constructor sets up the required data and connects buttons with methods."""
        super(InputWindow, self).__init__(parent=parent)
        self.setupUi(self)

        self.controller = None
        self.popup = None
        self.popup_ui = None
        self.apply.clicked.connect(self.apply_clicked)
        self.cancel.clicked.connect(self.cancel_clicked)
        self.checks = Checks()

        self.t_min = 0.0
        self.dt = 0.0
        self.t_max = 0.0
        self.nuclei = 0.0
        self.tau = 0.0
        self.truth_table = []

        self.data_names = [
            "Time min",
            "Delta",
            "Time max",
            "Nuclei",
            "Tau"
        ]

        self.data_placeholders = [
            self.t_min,
            self.dt,
            self.t_max,
            self.nuclei,
            self.tau
        ]

        self.data_ui = [
            self.line_t_min,
            self.line_delta,
            self.line_t_max,
            self.line_nuclei,
            self.line_tau
        ]

        self.truth = [
            self.rk1,
            self.rk2,
            self.rk3,
            self.rk4,
            self.rk5,
            self.rk6,
            self.frk5,
            self.frk6,
            self.frk7,
            self.frk8
        ]

    def initialize_data(self, controller):
        """Method reads current data through controller and displays it to user."""
        self.controller = controller
        self.line_t_min.setText(str(controller.id.get_t_min()))
        self.line_delta.setText(str(controller.id.get_dt()))
        self.line_t_max.setText(str(controller.id.get_t_max()))
        self.line_tau.setText(str(controller.nd.get_tau()))
        self.line_nuclei.setText(str(controller.nd.get_nuclei()))
        self.get_truth_table_values()

    def apply_clicked(self):
        """Method does a series of checks on a data provided by user. Any fail results in error message. If all
        checks are passed, the method saves data through controller and closes the window.
        """
        if self.change_type():
            check = self.checks.min_max_check(self.data_placeholders[0],
                                              self.data_placeholders[2])
            if check is None:
                check = self.checks.check_delta(self.data_placeholders[0],
                                                self.data_placeholders[1],
                                                self.data_placeholders[2])
                if check is None:
                    self.build_truth_table()
                    check = self.checks.check_truth_table(self.truth_table)
                    if check is None:
                        self.controller.initialize(
                            self.data_placeholders[0],
                            self.data_placeholders[1],
                            self.data_placeholders[2],
                            self.data_placeholders[3],
                            self.data_placeholders[4],
                            self.truth_table
                        )
                        self.close()
                    else:
                        self.raise_error(check)
                else:
                    self.raise_error(check)
            else:
                self.raise_error(check)

    def cancel_clicked(self):
        """Method closes the input window without data changes."""
        self.close()

    def change_type(self):
        """Method to change type of input variables from string to float. Returns True if successful or False if
        unsuccessful. Before returning False, it also calls the raise_error() method with message as argument.
        Message is being build if str_to_float() fails and returns string with error message instead of number.
        """
        message = ""
        for i in range(len(self.data_names)):
            element = self.checks.str_to_float(self.data_names[i], self.data_ui[i].text())
            if type(element) is str:
                message = message + element + "\n"
            else:
                self.data_placeholders[i] = element

        if len(message) > 0:
            self.raise_error(message)
            return False
        return True

    def get_truth_table_values(self):
        """Method gets the values of truth table from data through controller."""
        for i in range(len(self.truth)):
            if self.controller.id.get_truth_table()[i]:
                self.truth[i].setChecked(True)

    def build_truth_table(self):
        """Method sets up the truth table based on UI elements."""
        self.truth_table = [
            self.rk1.isChecked(),
            self.rk2.isChecked(),
            self.rk3.isChecked(),
            self.rk4.isChecked(),
            self.rk5.isChecked(),
            self.rk6.isChecked(),
            self.frk5.isChecked(),
            self.frk6.isChecked(),
            self.frk7.isChecked(),
            self.frk8.isChecked()
        ]

    def raise_error(self, message):
        """Method shows the widget with error message."""
        self.popup = QtWidgets.QDialog()
        self.popup_ui = ErrorWindow()
        self.popup_ui.set_message(message)
        self.popup_ui.exec()
