"""Custom exception classes for ansible-creator."""


class CreatorError(Exception):
    """Class representing exceptions raised from creator code."""

    def __init__(self, message=None):
        """Instantiate an object of this class.

        :param message: The exception message.
        """
        super().__init__(message)
        self._message = message

    @property
    def message(self):
        """Craft and return the CreatorError message.

           Includes the 'cause' when raised from another exception.

        :returns: An exception message.
        """
        msg = self._message
        if getattr(self, "__cause__", ""):
            msg += f"\n{str(self.__cause__)}"
        return msg

    def __str__(self):
        """Return a string representation of the exception.

        :returns: The exception message as a string.
        """
        return self.message
