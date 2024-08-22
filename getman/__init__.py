from . import version
from .client import GetMan
from .http import HTTPClient
from .manager import sessions
from .manager.browser import Browser
from .manager.dict import HeaderManager, ParamManager
from .models.struct import Struct

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
    "ParamManager",
    "HeaderManager",
    "Struct",
    "Browser",
]
