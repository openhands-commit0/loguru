import os
import sys
import platform

def load_ctime_functions():
    if platform.system() == 'Windows':
        try:
            from win32_setctime import setctime
            def get_ctime(filepath):
                return os.path.getctime(filepath)
            def set_ctime(filepath, timestamp):
                setctime(filepath, timestamp)
            return get_ctime, set_ctime
        except ImportError:
            pass

    def get_ctime(filepath):
        try:
            stat = os.stat(filepath)
            return stat.st_birthtime  # macOS
        except AttributeError:
            return stat.st_mtime  # Linux and others

    def set_ctime(filepath, timestamp):
        os.utime(filepath, (timestamp, os.path.getmtime(filepath)))

    return get_ctime, set_ctime

get_ctime, set_ctime = load_ctime_functions()