

class _Error:
    """
    Type representing an api error.
    """
    Last = None

    def __init__(self, code, msg):
        """
        Initialize a new api error using its code and a message.
        :param code:
        :param msg:
        """
        self.code = code
        self.msg = msg

    @property
    def error_object(self) -> Exception | None:
        """
        The python Exception instance corresponding to the api error,
        or None when there is no exception set.
        """
        last = type(self).Last
        if last is None:
            return
        etype: type[Ellipsis] | type[Exception] | None = error_codes.get(last.code, Ellipsis)
        if etype is None:
            return
        if etype is Ellipsis:
            raise LookupError(f"Can't find error code {last.code} in registry.")
        return etype(last.msg)


error_codes = {
    0: None,  # code 0: no error (success)
}
"""
Registry of error codes for apis we use.
The keys are the error codes, and the values
are python exception types that errors correspond to.

Commented explanations for these error codes are welcome.
"""


def set_last_error(*, code=None, msg=""):
    """
    Set last error according to 'code' and 'msg' keyword arguments.
    This function never fails.
    """
    if code is None:
        _Error.Last = None
    else:
        _Error.Last = _Error(code, msg)


def get_last_error():
    """
    Return an _Error instance that stores data about the last error.
    """
    if _Error.Last is None:
        return
    return _Error.Last


def raise_last_error():
    """
    Raise a python exception corresponding to the last error.
    """
    raise get_last_error().error_object

