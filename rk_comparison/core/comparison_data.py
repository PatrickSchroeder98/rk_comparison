class ComparisonData:
    """Class to hold comparison data of numerical methods with analytical solution."""

    def __init__(self):
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

    def clean_data(self):
        self.__init__()

    def set_compareRK1(self, compareRK1):
        self.compareRK1.append(compareRK1)

    def get_compareRK1(self):
        return self.compareRK1

    def set_compareRK2(self, compareRK2):
        self.compareRK2.append(compareRK2)

    def get_compareRK2(self):
        return self.compareRK2

    def set_compareRK3(self, compareRK3):
        self.compareRK3.append(compareRK3)

    def get_compareRK3(self):
        return self.compareRK3

    def set_compareRK4(self, compareRK4):
        self.compareRK4.append(compareRK4)

    def get_compareRK4(self):
        return self.compareRK4

    def set_compareRK5(self, compareRK5):
        self.compareRK5.append(compareRK5)

    def get_compareRK5(self):
        return self.compareRK5

    def set_compareRK6(self, compareRK6):
        self.compareRK6.append(compareRK6)

    def get_compareRK6(self):
        return self.compareRK6

    def set_compareFRK5(self, compareFRK5):
        self.compareFRK5.append(compareFRK5)

    def get_compareFRK5(self):
        return self.compareFRK5

    def set_compareFRK6(self, compareFRK6):
        self.compareFRK6.append(compareFRK6)

    def get_compareFRK6(self):
        return self.compareFRK6

    def set_compareFRK7(self, compareFRK7):
        self.compareFRK7.append(compareFRK7)

    def get_compareFRK7(self):
        return self.compareFRK7

    def set_compareFRK8(self, compareFRK8):
        self.compareFRK8.append(compareFRK8)

    def get_compareFRK8(self):
        return self.compareFRK8


