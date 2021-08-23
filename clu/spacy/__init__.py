try:
    from .info import info
    __version__ = info.version
except:
    pass