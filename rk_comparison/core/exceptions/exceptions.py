class StrToFloatError(Exception):
    """Exception raised for errors when string provided by user cannot be changed to float."""

    def __init__(self, message="Provided character is not a number."):
        """Setting custom exception message."""
        self.message = message
        super().__init__(self.message)

    def get_message(self):
        """Gets the exception message."""
        return self.message


class MinHigherThanMax(Exception):
    """Exception raised for errors when t_min is higher than or equal t_max."""

    def __init__(self, message="Beginning of the time period is greater than the end."):
        """Setting custom exception message."""
        self.message = message
        super().__init__(self.message)

    def get_message(self):
        """Gets the exception message."""
        return self.message


class TooLargeDelta(Exception):
    """Exception raised for errors when delta is too large for given time period."""

    def __init__(self, message="Delta is too large for this time period."):
        """Setting custom exception message."""
        self.message = message
        super().__init__(self.message)

    def get_message(self):
        """Gets the exception message."""
        return self.message


class DeltaIsZero(Exception):
    """Exception raised for errors when delta is equal to 0."""

    def __init__(self, message="Delta is equal to 0."):
        """Setting custom exception message."""
        self.message = message
        super().__init__(self.message)

    def get_message(self):
        """Gets the exception message."""
        return self.message


class DeltaIsNegative(Exception):
    """Exception raised for errors when delta is negative."""

    def __init__(self, message="Delta is negative."):
        """Setting custom exception message."""
        self.message = message
        super().__init__(self.message)

    def get_message(self):
        """Gets the exception message."""
        return self.message


class NoMethodChosen(Exception):
    """Exception raised when user didn't choose any numerical methods."""

    def __init__(self, message="No numerical method chosen."):
        """Setting custom exception message."""
        self.message = message
        super().__init__(self.message)

    def get_message(self):
        """Gets the exception message."""
        return self.message
