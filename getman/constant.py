from dataclasses import dataclass
from enum import StrEnum, auto


@dataclass
class HttpMethod(StrEnum):
	GET = auto()
	POST = auto()
	PUT = auto()
	DELETE = auto()
	PATCH = auto()
