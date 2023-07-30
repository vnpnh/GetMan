from dataclasses import dataclass
from enum import StrEnum, auto


@dataclass
class HttpMethod(StrEnum):
	GET = auto()
	POST = auto()
	PUT = auto()
	DELETE = auto()
	PATCH = auto()

class PlatformOS(StrEnum):
	WINDOWS = auto()
	DARWIN = auto()
	LINUX = auto()
	UNKNOWN = auto()
