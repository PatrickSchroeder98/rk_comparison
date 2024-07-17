from rk_comparison.core.plotting_module.plot import Plot


class PlotData:

    def __init__(self):
        """Constructor creates the Plot object."""
        self.pl = Plot()

    def plot(self, compare, controller, functions, y_label, title):
        """Method prepares result data to be displayed on plot and calls method to build and show it."""
        results_list = []
        desc = []
        for i in range(len(functions)):
            if controller.id.get_truth_table()[i]:
                results_list.append(functions[i]())
                desc.append(controller.descriptions[i])
        if compare:
            results_list.append(controller.rs.get_result_analytical())
            desc.append(controller.descriptions[-1])
        self.pl.plot(
            controller.rs.get_time(), results_list, "Time [s]", y_label, desc, title
        )

    def prepare_plot_bar_min(self, controller, x_label, y_label, title):
        """Method prepares result data to be displayed on bar plot and calls method to build and show it."""
        x = []
        for i in range(len(controller.descriptions) - 1):
            if controller.id.get_truth_table()[i]:
                x.append(controller.descriptions[i])

        self.pl.plot_bar(x, controller.cd.get_min_values(), x_label, y_label, title)

    def prepare_plot_bar_max(self, controller, x_label, y_label, title):
        """Method prepares result data to be displayed on bar plot and calls method to build and show it."""
        x = []
        for i in range(len(controller.descriptions) - 1):
            if controller.id.get_truth_table()[i]:
                x.append(controller.descriptions[i])

        self.pl.plot_bar(x, controller.cd.get_max_values(), x_label, y_label, title)

    def prepare_plot_bar_mean(self, controller, x_label, y_label, title):
        """Method prepares result data to be displayed on bar plot and calls method to build and show it."""
        x = []
        for i in range(len(controller.descriptions) - 1):
            if controller.id.get_truth_table()[i]:
                x.append(controller.descriptions[i])

        self.pl.plot_bar(x, controller.cd.get_mean_values(), x_label, y_label, title)
