class OutputData:
    """Class to hold output data: results of RK, FRK, analytical solution and time. Every variable has it's own set
    and get method. Set methods are clearing the lists and and appending the initial data needed for RK and FRK
    to start calculations.
    """

    def __init__(self):
        """Constructor creates empty lists for results."""
        self.resultRK1 = []
        self.resultRK2 = []
        self.resultRK3 = []
        self.resultRK4 = []
        self.resultRK5 = []
        self.resultRK6 = []

        self.resultFRK5 = []
        self.resultFRK6 = []
        self.resultFRK7 = []
        self.resultFRK8 = []

        self.resultAnalytical = []

        self.time = []

    def set_results(self, result0, t_min):
        """Method that calls all the set methods, preparing the program to make calculations. Arguments result0
        and t_min are the initial data provided by user.
        """
        self.set_result_analytical()
        self.set_resultRK1(result0)
        self.set_resultRK2(result0)
        self.set_resultRK3(result0)
        self.set_resultRK4(result0)
        self.set_resultRK5(result0)
        self.set_resultRK6(result0)
        self.set_resultFRK5(result0)
        self.set_resultFRK6(result0)
        self.set_resultFRK7(result0)
        self.set_resultFRK8(result0)
        self.set_time(t_min)

    def set_result_analytical(self):
        """Analytical solution doesn't need initial data, it's calculated from formula without the usage of numerical
        methods
        """
        self.resultAnalytical = []

    def get_result_analytical(self):
        """Gets the analytical result."""
        return self.resultAnalytical

    def set_resultRK1(self, result0):
        """Sets the start RK1 results."""
        self.resultRK1 = []
        self.resultRK1.append(result0)

    def get_resultRK1(self):
        """Gets the RK1 results."""
        return self.resultRK1

    def set_resultRK2(self, result0):
        """Sets the start RK2 results."""
        self.resultRK2 = []
        self.resultRK2.append(result0)

    def get_resultRK2(self):
        """Gets the RK2 results."""
        return self.resultRK2

    def set_resultRK3(self, result0):
        """Sets the start RK3 results."""
        self.resultRK3 = []
        self.resultRK3.append(result0)

    def get_resultRK3(self):
        """Gets the RK3 results."""
        return self.resultRK3

    def set_resultRK4(self, result0):
        """Sets the start RK4 results."""
        self.resultRK4 = []
        self.resultRK4.append(result0)

    def get_resultRK4(self):
        """Gets the RK4 results."""
        return self.resultRK4

    def set_resultRK5(self, result0):
        """Sets the start RK5 results."""
        self.resultRK5 = []
        self.resultRK5.append(result0)

    def get_resultRK5(self):
        """Gets the RK5 results."""
        return self.resultRK5

    def set_resultRK6(self, result0):
        """Sets the start RK6 results."""
        self.resultRK6 = []
        self.resultRK6.append(result0)

    def get_resultRK6(self):
        """Gets the RK6 results."""
        return self.resultRK6

    def set_resultFRK5(self, result0):
        """Sets the start FRK5 results."""
        self.resultFRK5 = []
        self.resultFRK5.append(result0)

    def get_resultFRK5(self):
        """Gets the FRK5 results."""
        return self.resultFRK5

    def set_resultFRK6(self, result0):
        """Sets the start FRK6 results."""
        self.resultFRK6 = []
        self.resultFRK6.append(result0)

    def get_resultFRK6(self):
        """Gets the FRK6 results."""
        return self.resultFRK6

    def set_resultFRK7(self, result0):
        """Sets the start FRK7 results."""
        self.resultFRK7 = []
        self.resultFRK7.append(result0)

    def get_resultFRK7(self):
        """Gets the FRK7 results."""
        return self.resultFRK7

    def set_resultFRK8(self, result0):
        """Sets the start FRK8 results."""
        self.resultFRK8 = []
        self.resultFRK8.append(result0)

    def get_resultFRK8(self):
        """Gets the FRK8 results."""
        return self.resultFRK8

    def set_time(self, t_min):
        """Sets the start of time scale."""
        self.time = []
        self.time.append(t_min)

    def get_time(self):
        """Gets the time scale."""
        return self.time

    def set_time_final(self, time):
        """Sets the time attribute."""
        self.time = time
