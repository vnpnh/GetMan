import platform
from dataclasses import dataclass, field

from getman.constant import PlatformOS


@dataclass
class Platform:
    platform: PlatformOS = field(default=None)

    def __post_init__(self):
        if self.platform is None:
            self.platform = self.get_os_version()

    @classmethod
    def get_os_version(cls):
        system = platform.system()

        if system == 'Windows':
            return PlatformOS.WINDOWS
        elif system == 'Linux':
            return PlatformOS.LINUX
        elif system == 'Darwin':
            return PlatformOS.DARWIN
        else:
            return PlatformOS.UNKNOWN
