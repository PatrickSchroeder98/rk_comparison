from rk_comparison.core.analytical_module.rungekutta import RungeKutta
from rk_comparison.core.analytical_module.fehlbergrungekutta import FehlbergRungeKutta
from rk_comparison.core.data.output_data import OutputData
from rk_comparison.core.data.input_data import InputData
from rk_comparison.core.analytical_module.nuclear_decay import NuclearDecay
from rk_comparison.core.data.comparison_data import ComparisonData
from rk_comparison.core.analytical_module.statistics import Statistics


class Controller:
    """Class that calls methods to initialize data, to calculate the problem and to plot the results."""

    def __init__(self):
        """Constructor sets up default values of attributes."""
        self.rk = RungeKutta()
        self.frk = FehlbergRungeKutta()
        self.rs = OutputData()
        self.id = InputData()
        self.nd = NuclearDecay()
        self.cd = ComparisonData()
        self.st = Statistics()

        self.methods_rk = [
            self.rk.rungekutta1,
            self.rk.rungekutta2,
            self.rk.rungekutta3,
            self.rk.rungekutta4,
            self.rk.rungekutta5,
            self.rk.rungekutta6,
            self.frk.fehlbergrungekutta5,
            self.frk.fehlbergrungekutta6,
            self.frk.fehlbergrungekutta7,
            self.frk.fehlbergrungekutta8,
        ]
        self.results_rk = [
            self.rs.get_resultRK1,
            self.rs.get_resultRK2,
            self.rs.get_resultRK3,
            self.rs.get_resultRK4,
            self.rs.get_resultRK5,
            self.rs.get_resultRK6,
            self.rs.get_resultFRK5,
            self.rs.get_resultFRK6,
            self.rs.get_resultFRK7,
            self.rs.get_resultFRK8,
        ]
        self.descriptions = [
            "RK1",
            "RK2",
            "RK3",
            "RK4",
            "RK5",
            "RK6",
            "FRK5",
            "FRK6",
            "FRK7",
            "FRK8",
            "Analytical",
        ]
        self.compare_rk = [
            self.cd.get_compareRK1,
            self.cd.get_compareRK2,
            self.cd.get_compareRK3,
            self.cd.get_compareRK4,
            self.cd.get_compareRK5,
            self.cd.get_compareRK6,
            self.cd.get_compareFRK5,
            self.cd.get_compareFRK6,
            self.cd.get_compareFRK7,
            self.cd.get_compareFRK8
        ]

    def initialize(self, t_min, dt, t_max, nuclei, tau, truth_table):
        """Method initializes the variables with values provided by user to start the calculations"""
        self.id.set_t_min(t_min)
        self.id.set_dt(dt)
        self.id.set_t_max(t_max)
        self.id.set_intervals()

        self.id.set_truth_table(truth_table)

        self.nd.set_nuclei(nuclei)
        self.nd.set_tau(tau)

        self.rs.set_results(nuclei, t_min)

    def calculate(self):
        """Method loops through the list of rk and frk methods, calculating the problem and saving the results to the
        proper lists. Added optional log to console for verification if the data are saved to correct lists. On the
        last loop iteration, the list of time values is saved to temporary variable and after loop finishes, it is
        assigned back to time output data.
        """
        temp = []
        for i in range(len(self.methods_rk)):
            if self.id.get_truth_table()[i]:
                # print(
                #     "From"
                #     + str(self.methods_rk[i])
                #     + " results are going to: "
                #     + str(self.results_rk[i])
                #     + ", this will be described as: "
                #     + str(self.descriptions[i])
                # )
                self.methods_rk[i](
                    self.nd.equation,
                    self.rs.get_time(),
                    self.results_rk[i](),
                    self.id.get_intervals(),
                    self.id.get_dt(),
                )
                if len(self.rs.get_time()) > 1:
                    temp = self.rs.get_time()

                self.rs.set_time(self.id.get_t_min())
        self.rs.set_time_final(temp)

    def calculate_analytical(self):
        """Method calculates the nuclear decay problem in analytical way. Requires the time list to be filled with
        results from the numerical calculations."""
        for i in self.rs.get_time():
            self.rs.resultAnalytical.append(
                self.nd.equation_analytical(self.nd.get_nuclei(), i)
            )

    def compare(self):
        """Method subtract RK results from analytical solution and saves the results to ComparisonData attributes."""
        self.cd.clean_data()
        for result, compare, value in zip(self.results_rk, self.compare_rk, self.id.get_truth_table()):
            if value:
                for i in range(len(self.rs.get_result_analytical())):
                    compare().append(abs(self.rs.get_result_analytical()[i] - result()[i]))

        for j in range(len(self.compare_rk)):
            if self.id.get_truth_table()[j]:
                self.cd.set_min_values(self.st.min_max_value(self.compare_rk[j](), True))
                self.cd.set_max_values(self.st.min_max_value(self.compare_rk[j](), False))
                self.cd.set_mean_values(self.st.mean(self.compare_rk[j]()))
