import sys


LOG_INFO = 0
LOG_WARN = 1
LOG_ERROR = 2


class Logger:
    def __init__(self, source):
        super().__init__()
        self._source = source

    def log(self, *message, level=0, **kwargs):
        match level:
            case 0:
                level_str = 'INFO'
            case 1:
                level_str = 'WARN'
            case _:
                level_str = 'ERROR'

        print(f'[{self._source}/{level_str}]', *message, **kwargs)

    def fake_throw(self, error, message, file='<unknown>'):
        self.log("Error thrown from", file, ':', level=2, file=sys.stderr)
        try:
            raise error(message)
        except error:
            sys.excepthook(*sys.exc_info())

