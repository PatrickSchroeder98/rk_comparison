class Statistics:

    def min_max_value(self, comparison_data, min):
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
        result = 0.0
        for i in range(len(comparison_data)):
            result = result + comparison_data[i]
        return result/len(comparison_data)
