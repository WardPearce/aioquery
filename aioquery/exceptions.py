class UnableToConnect(Exception):
    """Raised when connection fails.
    """

    pass


class DidNotReceive(Exception):
    """Raised when no data received.
    """

    pass


class InvalidServer(Exception):
    """Raised when given server isn't a source server.
    """

    pass
