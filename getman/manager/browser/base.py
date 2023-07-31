import os
import sqlite3
from dataclasses import field, dataclass
from typing import Optional

from getman.manager.browser.constant import System


@dataclass
class BrowserBase:
    """
    Represents a web browser platform.

    Attributes:
    path (Optional[str]): The path to the browser executable, if available.
    """
    path: Optional[str] = field(default=None)
    app_data: str = os.getenv(System.APPDATA.value.upper())
    local_app_data: str = os.getenv(System.LOCALAPPDATA.value.upper())

    def get_cookies_by_url(self, url: str):
        pass

    @classmethod
    def connect_sql_lite3(cls, cookies):
        return sqlite3.connect(cookies)
