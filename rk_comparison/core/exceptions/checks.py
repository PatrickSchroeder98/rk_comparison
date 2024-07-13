from rk_comparison.core.exceptions.exceptions import (
    StrToFloatError,
    MinHigherThanMax,
    DeltaIsZero,
    DeltaIsNegative,
    TooLargeDelta,
    NoMethodChosen,
)


class Checks:
    """Class containing checks for input data."""

    def str_to_float(self, data, value):
        """Method returns float number. If unsuccessful, it returns an exception message."""
        try:
            num = float(value)
        except ValueError:
            return data + ": " + StrToFloatError().get_message()
        else:
            return num

    def min_max_check(self, t_min, t_max):
        """Method returns None or  if the start of time period is smaller or equal to it's end. It returns exception
        message if provided numbers cannot satisfy this condition.
        """
        if t_min >= t_max:
            return MinHigherThanMax().get_message()
        else:
            return

    def check_delta(self, t_min, delta, t_max):
        """Method checks the correctness of delta attribute value. Returns None if it's correct or one of the exception
        message.
        """
        if delta == 0:
            return DeltaIsZero().get_message()
        elif delta < 0:
            return DeltaIsNegative().get_message()
        else:
            if (t_max - t_min) < delta:
                return TooLargeDelta().get_message()
            else:
                return

    def check_truth_table(self, truth_table):
        """Method returns None if the truth table attribute has at least one True appended. Otherwise it returns
        the error message.
        """
        if True not in truth_table:
            return NoMethodChosen().get_message()
        else:
            return
