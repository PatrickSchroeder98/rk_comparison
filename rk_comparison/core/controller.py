from rk_comparison.core.rungekutta import RungeKutta
from rk_comparison.core.fehlbergrungekutta import FehlbergRungeKutta
from rk_comparison.core.output_data import ResultsModel
from rk_comparison.core.input_data import InputData
from rk_comparison.core.nuclear_decay import NuclearDecay
from rk_comparison.core.plot import Plot


class Controller:
    """Class that calls methods to initialize data and to calculate the problem."""

    def __init__(self):
        self.rk = RungeKutta()
        self.frk = FehlbergRungeKutta()
        self.rs = ResultsModel()
        self.id = InputData()
        self.nd = NuclearDecay()
        self.pl = Plot()

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

    def initialize(self, t_min, dt, t_max, nuclei, tau):
        """Method initializes the variables with values provided by user to start the calculations"""
        self.id.set_t_min(t_min)
        self.id.set_dt(dt)
        self.id.set_t_max(t_max)
        self.id.set_intervals()

        self.nd.set_nuclei(nuclei)
        self.nd.set_tau(tau)

        self.rs.set_results(nuclei, t_min)

    def calculate(self):
        """Method loops through the list of rk and frk methods, calculating the problem and saving the results to the
        proper lists. Added log to console for verification if the data are saved to correct lists. On the last loop
        iteration, the list of time values is not cleared.
        """
        for i in range(len(self.methods_rk)):
            print(
                "From"
                + str(self.methods_rk[i])
                + " results are going to: "
                + str(self.results_rk[i])
                + ", this will be described as: "
                + str(self.descriptions[i])
            )
            self.methods_rk[i](
                self.nd.equation,
                self.rs.get_time(),
                self.results_rk[i](),
                self.id.get_intervals(),
                self.id.get_dt(),
            )
            if i != (len(self.methods_rk) - 1):
                self.rs.set_time(self.id.get_t_min())

    def calculate_analytical(self):
        """Method calculates the nuclear decay problem in analytical way. Requires the time list to be filled with
        results from the numerical calculations."""
        for i in self.rs.get_time():
            self.rs.resultAnalytical.append(
                self.nd.equation_analytical(self.nd.get_nuclei(), i)
            )

    def plot(self):
        """Method prepares result data to be displayed on chart and calls method to plot it."""
        results_list = []
        for element in self.results_rk:
            results_list.append(element())
        results_list.append(self.rs.get_result_analytical())
        self.pl.plot(
            self.rs.get_time(),
            results_list,
            "Time [s]",
            "Nuclear Decay [nuclei]",
            self.descriptions,
            "Nuclear Decay",
        )
