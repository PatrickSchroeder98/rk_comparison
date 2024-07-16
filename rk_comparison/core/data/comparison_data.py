class ComparisonData:
    """Class to hold comparison data of numerical methods with analytical solution."""

    def __init__(self):
        """Constructor sets up the empty lists."""
        self.compareRK1 = []
        self.compareRK2 = []
        self.compareRK3 = []
        self.compareRK4 = []
        self.compareRK5 = []
        self.compareRK6 = []

        self.compareFRK5 = []
        self.compareFRK6 = []
        self.compareFRK7 = []
        self.compareFRK8 = []

        self.min_values = []
        self.max_values = []
        self.mean_values = []

    def clean_data(self):
        """Method to clean all of the lists by calling constructor."""
        self.__init__()

    def set_compareRK1(self, compareRK1):
        """Method to set the element of compareRK1 list."""
        self.compareRK1.append(compareRK1)

    def get_compareRK1(self):
        """Method to get the compareRK1 list."""
        return self.compareRK1

    def set_compareRK2(self, compareRK2):
        """Method to set the element of compareRK2 list."""
        self.compareRK2.append(compareRK2)

    def get_compareRK2(self):
        """Method to get the compareRK2 list."""
        return self.compareRK2

    def set_compareRK3(self, compareRK3):
        """Method to set the element of compareRK3 list."""
        self.compareRK3.append(compareRK3)

    def get_compareRK3(self):
        """Method to get the compareRK3 list."""
        return self.compareRK3

    def set_compareRK4(self, compareRK4):
        """Method to set the element of compareRK4 list."""
        self.compareRK4.append(compareRK4)

    def get_compareRK4(self):
        """Method to get the compareRK4 list."""
        return self.compareRK4

    def set_compareRK5(self, compareRK5):
        """Method to set the element of compareRK5 list."""
        self.compareRK5.append(compareRK5)

    def get_compareRK5(self):
        """Method to get the compareRK5 list."""
        return self.compareRK5

    def set_compareRK6(self, compareRK6):
        """Method to set the element of compareRK6 list."""
        self.compareRK6.append(compareRK6)

    def get_compareRK6(self):
        """Method to get the compareRK6 list."""
        return self.compareRK6

    def set_compareFRK5(self, compareFRK5):
        """Method to set the element of compareFRK5 list."""
        self.compareFRK5.append(compareFRK5)

    def get_compareFRK5(self):
        """Method to get the compareFRK5 list."""
        return self.compareFRK5

    def set_compareFRK6(self, compareFRK6):
        """Method to set the element of compareFRK6 list."""
        self.compareFRK6.append(compareFRK6)

    def get_compareFRK6(self):
        """Method to get the compareFRK6 list."""
        return self.compareFRK6

    def set_compareFRK7(self, compareFRK7):
        """Method to set the element of compareFRK7 list."""
        self.compareFRK7.append(compareFRK7)

    def get_compareFRK7(self):
        """Method to get the compareFRK7 list."""
        return self.compareFRK7

    def set_compareFRK8(self, compareFRK8):
        """Method to set the element of compareFRK8 list."""
        self.compareFRK8.append(compareFRK8)

    def get_compareFRK8(self):
        """Method to get the compareFRK8 list."""
        return self.compareFRK8

    def set_min_values(self, min_values):
        """Method to set the element of min_values list."""
        self.min_values.append(min_values)

    def get_min_values(self):
        """Method to get the min_values list."""
        return self.min_values

    def set_max_values(self, max_values):
        """Method to set the element of max_values list."""
        self.max_values.append(max_values)

    def get_max_values(self):
        """Method to get the max_values list."""
        return self.max_values

    def set_mean_values(self, mean_values):
        """Method to set the element of mean_values list."""
        self.mean_values.append(mean_values)

    def get_mean_values(self):
        """Method to get the mean_values list."""
        return self.mean_values
