class ResultsModel:
    """Class to hold output data: results of RK, FRK, analytical solution and time. Every variable has it's own set
    and get method. Set methods are clearing the lists and and appending the initial data needed for RK and FRK
    to start calculations.
    """

    def __init__(self):
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
        return self.resultAnalytical

    def set_resultRK1(self, result0):
        self.resultRK1 = []
        self.resultRK1.append(result0)

    def get_resultRK1(self):
        return self.resultRK1

    def set_resultRK2(self, result0):
        self.resultRK2 = []
        self.resultRK2.append(result0)

    def get_resultRK2(self):
        return self.resultRK2

    def set_resultRK3(self, result0):
        self.resultRK3 = []
        self.resultRK3.append(result0)

    def get_resultRK3(self):
        return self.resultRK3

    def set_resultRK4(self, result0):
        self.resultRK4 = []
        self.resultRK4.append(result0)

    def get_resultRK4(self):
        return self.resultRK4

    def set_resultRK5(self, result0):
        self.resultRK5 = []
        self.resultRK5.append(result0)

    def get_resultRK5(self):
        return self.resultRK5

    def set_resultRK6(self, result0):
        self.resultRK6 = []
        self.resultRK6.append(result0)

    def get_resultRK6(self):
        return self.resultRK6

    def set_resultFRK5(self, result0):
        self.resultFRK5 = []
        self.resultFRK5.append(result0)

    def get_resultFRK5(self):
        return self.resultFRK5

    def set_resultFRK6(self, result0):
        self.resultFRK6 = []
        self.resultFRK6.append(result0)

    def get_resultFRK6(self):
        return self.resultFRK6

    def set_resultFRK7(self, result0):
        self.resultFRK7 = []
        self.resultFRK7.append(result0)

    def get_resultFRK7(self):
        return self.resultFRK7

    def set_resultFRK8(self, result0):
        self.resultFRK8 = []
        self.resultFRK8.append(result0)

    def get_resultFRK8(self):
        return self.resultFRK8

    def set_time(self, t_min):
        self.time = []
        self.time.append(t_min)

    def get_time(self):
        return self.time
