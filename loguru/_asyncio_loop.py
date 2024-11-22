import asyncio
import sys

def load_loop_functions():
    if sys.version_info >= (3, 7):
        # Python 3.7+ has get_running_loop()
        def get_task_loop(task):
            return task.get_loop()
        return get_task_loop, asyncio.get_running_loop
    else:
        # For Python < 3.7
        def get_task_loop(task):
            return task._loop
        def get_running_loop():
            loop = asyncio._get_running_loop()
            if loop is None:
                raise RuntimeError('no running event loop')
            return loop
        return get_task_loop, get_running_loop

get_task_loop, get_running_loop = load_loop_functions()