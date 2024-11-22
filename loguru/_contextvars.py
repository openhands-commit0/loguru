import sys

def load_contextvar_class():
    if sys.version_info >= (3, 7):
        from contextvars import ContextVar
        return ContextVar
    else:
        try:
            from aiocontextvars import ContextVar
            return ContextVar
        except ImportError:
            class ContextVar:
                def __init__(self, name, *, default=None):
                    self._name = name
                    self._default = default
                    self._value = default

                def get(self, default=None):
                    return self._value if self._value is not None else default

                def set(self, value):
                    old_value = self._value
                    self._value = value
                    return old_value

            return ContextVar

ContextVar = load_contextvar_class()