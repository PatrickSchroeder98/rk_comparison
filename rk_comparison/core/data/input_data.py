class InputData:
    """Class to hold input data from user: beginning and end of time period, delta of the time intervals,
    number of time intervals, list of booleans signalizing which numerical methods will be used.
    Every attribute has set and get method.
    """

    def __init__(self):
        """Constructor sets up default values of attributes."""
        self.t_min = 0.0
        self.dt = 0.05
        self.t_max = 5.0
        self.intervals = 0
        self.truth_table = [
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True,
            True
        ]

    def set_t_min(self, t_min):
        """Sets the beginning of time period."""
        self.t_min = t_min

    def get_t_min(self):
        """Gets the beginning of time period."""
        return self.t_min

    def set_dt(self, dt):
        """Sets the time delta."""
        self.dt = dt

    def get_dt(self):
        """Gets the time delta."""
        return self.dt

    def set_t_max(self, t_max):
        """Sets the ending of time period."""
        self.t_max = t_max

    def get_t_max(self):
        """Gets the ending of time period."""
        return self.t_max

    def set_intervals(self):
        """Method counts time intervals based on input data."""
        self.intervals = int((self.t_max - self.t_min) / self.dt)

    def get_intervals(self):
        """Returns the number of time intervals"""
        return self.intervals

    def set_truth_table(self, truth_table):
        """Sets the list of booleans signalizing which numerical methods will be used."""
        self.truth_table = truth_table

    def get_truth_table(self):
        """Gets the list of booleans signalizing which numerical methods will be used."""
        return self.truth_table
