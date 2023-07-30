from .manager import dict, sessions
from .manager.browser import Browser
from .manager.dict import DictManager, HeaderManager, ParamManager
from .models.struct import Struct
from .http import HTTPClient
from .client import GetMan
from . import version

__version_info__ = version.VERSION
__version__ = version.VERSION_TEXT

__all__ = [
    "GetMan",
    "HTTPClient",
    "DictManager",
    "ParamManager",
    "HeaderManager",
    "Struct",
    "Browser",
]