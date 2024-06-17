import matplotlib.pyplot as plt


class Plot:
    """Class with method to plot data on a chart."""

    def plot(self, x, _y, x_label, y_label, legend, title):
        """Method shows the plot in window, allows displaying multiple data on one plot.
        Data to display must be passed in _y argument in form of nested list;
        x is a list;
        title, x_label, y_label and legend are a string.
        """
        for y in _y:
            plt.plot(x, y)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(legend)
        plt.show()
