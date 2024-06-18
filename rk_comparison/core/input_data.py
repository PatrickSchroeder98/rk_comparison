class InputData:
    """Class to hold input data from user: beginning and end of time period, delta of the time intervals,
    number of time intervals, initial number of nuclei. Every variable has it's own set and get method.
    """

    t_min = 0
    dt = 1
    t_max = 100
    intervals = 0

    nuclei = 100

    def set_t_min(self, t_min):
        self.t_min = t_min

    def get_t_min(self):
        return self.t_min

    def set_dt(self, dt):
        self.dt = dt

    def get_dt(self):
        return self.dt

    def set_t_max(self, t_max):
        self.t_max = t_max

    def get_t_max(self):
        return self.t_max

    def set_intervals(self):
        """Method counts time intervals based on input data."""
        self.intervals = int((self.t_max - self.t_min) / self.dt)

    def get_intervals(self):
        return self.intervals

    def set_nuclei(self, nuclei):
        self.nuclei = nuclei

    def get_nuclei(self):
        return self.nuclei
