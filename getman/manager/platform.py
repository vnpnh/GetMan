import platform
from dataclasses import dataclass, field
from typing import Dict

from getman.constant import PlatformOS


@dataclass
class Platform:
    """
    Represents the platform on which the application is running.

    Attributes:
        platform (PlatformOS): The platform on which the application is running.
                               If not provided, it will be automatically detected.
    """
    platform: PlatformOS = field(default=None)

    def __post_init__(self):
        if self.platform is None:
            self.platform = self.get_os_version()

    @classmethod
    def get_os_version(cls):
        """
       Get the current operating system version.

       Returns:
           PlatformOS: The detected operating system platform.
       """
        system = platform.system()

        os_mapping: Dict[str, PlatformOS] = {
            'Windows': PlatformOS.WINDOWS,
            'Linux': PlatformOS.LINUX,
            'Darwin': PlatformOS.DARWIN
        }

        return os_mapping.get(system, PlatformOS.UNKNOWN)
