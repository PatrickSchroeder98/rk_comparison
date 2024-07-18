from csv import writer


class SaveData:
    """Class to prepare and save data to opened file."""

    def save(self, file, controller):
        """Method loops through the nested lists of data and saves it in the csv file. Each list is a column."""
        w = writer(file)

        data = self.prepare_data(controller)
        l = []
        n = len(data[0])
        m = len(data)
        for j in range(n):
            for i in range(m):
                l.append(data[i][j])
            w.writerow(l)
            l = []

    def prepare_data(self, controller):
        """Method calls various methods to prepare parts of results and returns created list. It also adds a time list
        at the beginning. Returns the prepared list."""
        results = [["Time [s]"] + controller.rs.get_time(),
                   [controller.descriptions[-1] + " [nuclei]"] + controller.rs.get_result_analytical()]
        whitespaces_count = len(results[0])
        self.add_space(results, whitespaces_count)
        self.add_results(controller, results, False)
        self.add_space(results, whitespaces_count)
        self.add_results(controller, results, True)
        self.add_space(results, whitespaces_count)
        self.add_statistics_descriptions(controller, results, whitespaces_count)
        self.add_statistics(results, controller.cd.get_min_values(), "Minimal values", whitespaces_count)
        self.add_statistics(results, controller.cd.get_max_values(), "Maximal values", whitespaces_count)
        self.add_statistics(results, controller.cd.get_mean_values(), "Mean values", whitespaces_count)
        self.add_space(results, whitespaces_count)

        return results

    def add_results(self, controller, results, cmp):
        """Method adds lists of results of calculations or comparison to results list."""
        for i in range(len(controller.results_rk)):
            if controller.id.get_truth_table()[i]:
                if cmp:
                    results.append(["Comparison " + controller.descriptions[i] + " [nuclei]"] + controller.compare_rk[i]())
                else:
                    results.append([controller.descriptions[i] + " [nuclei]"] + controller.results_rk[i]())

    def add_space(self, results, whitespaces_count):
        """Method adds list of whitespaces to results."""
        whitespaces = []
        for i in range(whitespaces_count):
            whitespaces.append("")
        results.append(whitespaces)

    def add_statistics_descriptions(self, controller, results, whitespaces_count):
        """Method adds the list with names of methods used during calculations to results list. Whitespaces are added
        for list to match the overall lists length.
        """
        res = ["Method"]
        for i in range(len(controller.descriptions) - 1):
            if controller.id.get_truth_table()[i]:
                res.append(controller.descriptions[i])

        while len(res) < whitespaces_count:
            res.append("")
        results.append(res)

    def add_statistics(self, results, statistics_result, name, whitespaces_count):
        """Method adds a list with one of the statistics results to the results list."""
        res = [name]
        for item in statistics_result:
            res.append(item)

        while len(res) < whitespaces_count:
            res.append("")
        results.append(res)
