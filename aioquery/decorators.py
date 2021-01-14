from functools import wraps
from typing import List


def string_encoding(to_encode: List[str]):
    """Used to encode strings correctly.

    Parameters
    ----------
    to_encode : List[Any]
        List of strings keys to encode.
    """

    def decorator(func):
        @wraps(func)
        def _encode(*args, **kwargs):
            for key in to_encode:
                if key in kwargs and kwargs[key]:
                    kwargs[key] = kwargs[key].encode("utf-8").decode("latin-1")

            return func(*args, **kwargs)

        return _encode

    return decorator
