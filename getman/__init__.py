from .manager import dict, sessions
from .manager.browser import Browser
from .manager.dict import DictManager, HeaderManager, ParamManager
from .models.struct import Struct
from .http import HTTPClient
from .client import GetMan
from . import version

__title__ = version.TITLE
__description__ = version.DESCRIPTION
__author__ = version.AUTHOR
__license__ = version.LICENSE
__version_info__ = version.version
__version__ = version.VERSION_TEXT
__copyright__ = version.COPYRIGHT

__all__ = [
    "GetMan",
    "HTTPClient",
    "DictManager",
    "ParamManager",
    "HeaderManager",
    "Struct",
    "Browser",
]
