import math


class NuclearDecay:
    """This class contains the differential equation and analytical solution to the nuclear decay problem.
    Tau is a mean lifetime of a radioactive particle before decay.
    """

    def __init__(self):
        self.tau = 1.0
        self.nuclei = 100.0

    def equation(self, t, nu):
        """Differential equation describing the nuclear decay problem. Source: [6] in bibliography."""
        return -(nu / self.get_tau())

    def equation_analytical(self, nu0, t):
        """Analytical solution to the nuclear decay problem. Source: [6] in bibliography."""
        return nu0 * pow(math.e, -(t / self.get_tau()))

    def set_tau(self, tau):
        """Tau can be set by user with this method."""
        self.tau = tau

    def get_tau(self):
        """Returns the tau value."""
        return self.tau

    def set_nuclei(self, nuclei):
        """Initial number of nuclei can be set by user with this method."""
        self.nuclei = nuclei

    def get_nuclei(self):
        """Returns the number of nuclei."""
        return self.nuclei
