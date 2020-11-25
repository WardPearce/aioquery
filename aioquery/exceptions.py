class AioQueryException(Exception):
    """Base exception.
    """

    pass


class UnableToConnect(AioQueryException):
    """Raised when connection fails.
    """

    pass


class DidNotReceive(AioQueryException):
    """Raised when no data received.
    """

    pass


class InvalidServer(AioQueryException):
    """Raised when given server isn't a source server.
    """

    pass
