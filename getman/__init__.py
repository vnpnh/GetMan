from .models.struct import Struct
from .manager.dict import DictManager, HeaderManager, ParamManager
from .manager.sessions import SessionManager
from .client import GetMan
from . import version

__version_info__ = version.VERSION
__version__ = version.VERSION_TEXT

ALL = [
	"Struct",
]
