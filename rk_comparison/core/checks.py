from rk_comparison.core.exceptions import StrToFloatError, MinHigherThanMax, DeltaIsZero, DeltaIsNegative, TooLargeDelta


class Checks:

    def str_to_float(self, data, value):
        try:
            num = float(value)
        except ValueError:
            return data + ": " + StrToFloatError().message
        else:
            return num

    def min_max_check(self, t_min, t_max):
        if t_min >= t_max:
            return MinHigherThanMax().message
        else:
            return

    def check_delta(self, t_min, delta, t_max):
        if delta == 0:
            return DeltaIsZero().message
        elif delta < 0:
            return DeltaIsNegative().message
        else:
            if (t_max - t_min) < delta:
                return TooLargeDelta().message
            else:
                return
