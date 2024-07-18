from PyQt6 import QtWidgets
from sys import argv, exit
from rk_comparison.interface.ui.mainwindow import MainWindow


def main():
    """Main function of app, shows the Main Window."""
    app = QtWidgets.QApplication(argv)
    w = MainWindow()
    w.show()
    exit(app.exec())


if __name__ == '__main__':
    main()

