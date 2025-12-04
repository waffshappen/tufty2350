try:
    __import__("/main")
except ImportError:
    __import__("/system/main")
