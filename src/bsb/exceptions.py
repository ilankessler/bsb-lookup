"""Exceptions raised by this package."""


class InvalidBSBException(Exception):

    """Base class for exceptions raised by this package."""

    pass


class InvalidBSBFormatException(InvalidBSBException):

    """Raised when the BSB number is not in a valid format."""

    def __init__(self, bsb: str):
        self.bsb = bsb
        super().__init__(
            f"Invalid BSB format: '{bsb}'. A valid BSB should consist of 6 digits, each ranging from 0 to 9."
        )
