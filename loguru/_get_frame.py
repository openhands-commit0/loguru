import sys
from sys import exc_info

def load_get_frame_function():
    if hasattr(sys, '_getframe'):
        def get_frame(depth):
            return sys._getframe(depth)
    else:
        def get_frame(depth):
            try:
                raise Exception
            except Exception:
                frame = exc_info()[2].tb_frame
                for _ in range(depth):
                    frame = frame.f_back
                return frame
    return get_frame

get_frame = load_get_frame_function()