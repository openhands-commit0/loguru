import os
import sys

def should_colorize(stream):
    try:
        return stream.isatty()
    except Exception:
        return False

def should_wrap(stream):
    if not should_colorize(stream):
        return False

    if 'PYCHARM_HOSTED' in os.environ:
        return False

    if sys.platform == 'win32':
        return True

    if 'TERM' in os.environ and os.environ['TERM'] == 'dumb':
        return False

    return True