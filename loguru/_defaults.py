from os import environ

def env(key, type_, default):
    if key not in environ:
        return default
    value = environ[key]
    if type_ == bool:
        return value.lower() in ('true', '1', 'yes', 'on')
    return type_(value)

LOGURU_AUTOINIT = env('LOGURU_AUTOINIT', bool, True)
LOGURU_FORMAT = env('LOGURU_FORMAT', str, '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>')
LOGURU_FILTER = env('LOGURU_FILTER', str, None)
LOGURU_LEVEL = env('LOGURU_LEVEL', str, 'DEBUG')
LOGURU_COLORIZE = env('LOGURU_COLORIZE', bool, None)
LOGURU_SERIALIZE = env('LOGURU_SERIALIZE', bool, False)
LOGURU_BACKTRACE = env('LOGURU_BACKTRACE', bool, True)
LOGURU_DIAGNOSE = env('LOGURU_DIAGNOSE', bool, True)
LOGURU_ENQUEUE = env('LOGURU_ENQUEUE', bool, False)
LOGURU_CONTEXT = env('LOGURU_CONTEXT', str, None)
LOGURU_CATCH = env('LOGURU_CATCH', bool, True)
LOGURU_TRACE_NO = env('LOGURU_TRACE_NO', int, 5)
LOGURU_TRACE_COLOR = env('LOGURU_TRACE_COLOR', str, '<cyan><bold>')
LOGURU_TRACE_ICON = env('LOGURU_TRACE_ICON', str, '✏️')
LOGURU_DEBUG_NO = env('LOGURU_DEBUG_NO', int, 10)
LOGURU_DEBUG_COLOR = env('LOGURU_DEBUG_COLOR', str, '<blue><bold>')
LOGURU_DEBUG_ICON = env('LOGURU_DEBUG_ICON', str, '🐞')
LOGURU_INFO_NO = env('LOGURU_INFO_NO', int, 20)
LOGURU_INFO_COLOR = env('LOGURU_INFO_COLOR', str, '<bold>')
LOGURU_INFO_ICON = env('LOGURU_INFO_ICON', str, 'ℹ️')
LOGURU_SUCCESS_NO = env('LOGURU_SUCCESS_NO', int, 25)
LOGURU_SUCCESS_COLOR = env('LOGURU_SUCCESS_COLOR', str, '<green><bold>')
LOGURU_SUCCESS_ICON = env('LOGURU_SUCCESS_ICON', str, '✅')
LOGURU_WARNING_NO = env('LOGURU_WARNING_NO', int, 30)
LOGURU_WARNING_COLOR = env('LOGURU_WARNING_COLOR', str, '<yellow><bold>')
LOGURU_WARNING_ICON = env('LOGURU_WARNING_ICON', str, '⚠️')
LOGURU_ERROR_NO = env('LOGURU_ERROR_NO', int, 40)
LOGURU_ERROR_COLOR = env('LOGURU_ERROR_COLOR', str, '<red><bold>')
LOGURU_ERROR_ICON = env('LOGURU_ERROR_ICON', str, '❌')
LOGURU_CRITICAL_NO = env('LOGURU_CRITICAL_NO', int, 50)
LOGURU_CRITICAL_COLOR = env('LOGURU_CRITICAL_COLOR', str, '<RED><bold>')
LOGURU_CRITICAL_ICON = env('LOGURU_CRITICAL_ICON', str, '☠️')