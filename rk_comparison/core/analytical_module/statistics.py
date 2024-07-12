class Statistics:

    def min_max_value(self, comparison_data, min):
        """Method returns minimal or maximal value of given list. Depends on given boolean attribute."""
        result = comparison_data[1]
        for i in range(1, len(comparison_data)):
            if min:
                if result > comparison_data[i]:
                    result = comparison_data[i]
            else:
                if result < comparison_data[i]:
                    result = comparison_data[i]
        return result

    def mean(self, comparison_data):
        """Method returns mean value of elements in given list."""
        result = 0.0
        for i in range(len(comparison_data)):
            result = result + comparison_data[i]
        return result/len(comparison_data)
