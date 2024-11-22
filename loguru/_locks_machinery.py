import os
import threading
import weakref

logger_locks = weakref.WeakSet()
handler_locks = weakref.WeakSet()

def acquire_locks():
    for lock in logger_locks:
        lock.acquire()
    for lock in handler_locks:
        lock.acquire()

def release_locks():
    for lock in reversed(list(handler_locks)):
        lock.release()
    for lock in reversed(list(logger_locks)):
        lock.release()

def create_logger_lock():
    lock = threading.Lock()
    logger_locks.add(lock)
    return lock

def create_handler_lock():
    lock = threading.Lock()
    handler_locks.add(lock)
    return lock

if hasattr(os, 'register_at_fork'):
    os.register_at_fork(before=acquire_locks, after_in_parent=release_locks, after_in_child=release_locks)