try:
    from .spacy.info import info
    __version__ = info.version
except:
    pass