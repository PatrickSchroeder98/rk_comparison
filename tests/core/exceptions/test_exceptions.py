import unittest
from rk_comparison.core.exceptions.exceptions import (
    StrToFloatError,
    MinHigherThanMax,
    DeltaIsZero,
    DeltaIsNegative,
    TooLargeDelta,
    NoMethodChosen,
)


class TestExceptions(unittest.TestCase):
    """Tests for the exceptions classes."""

    def test_str_to_float_error(self):
        """Test for message when a character is not a number."""
        exception = StrToFloatError()
        self.assertEqual("Provided character is not a number.", exception.get_message())

    def test_min_higher_than_max(self):
        """Test for message when start of time period is greater than it's end."""
        exception = MinHigherThanMax()
        self.assertEqual("Beginning of the time period is greater than the end.", exception.get_message())

    def test_too_large_delta(self):
        """Test for message when delta value is too big."""
        exception = TooLargeDelta()
        self.assertEqual("Delta is too large for this time period.", exception.get_message())

    def test_delta_is_zero(self):
        """Test for message when delta value is equal to zero."""
        exception = DeltaIsZero()
        self.assertEqual("Delta is equal to 0.", exception.get_message())

    def test_delta_is_negative(self):
        """Test for message when delta value is a negative number."""
        exception = DeltaIsNegative()
        self.assertEqual("Delta is negative.", exception.get_message())

    def test_no_method_chosen(self):
        """Test for message when no numerical method was chosen."""
        exception = NoMethodChosen()
        self.assertEqual("No numerical method chosen.", exception.get_message())


if __name__ == "__main__":
    unittest.main()
