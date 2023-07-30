from dataclasses import field
from typing import Optional

import browser_cookie3

from getman.constant import PlatformOS
from getman.manager.browser.manager import BrowserManager
from getman.manager.platform import Platform
from getman.utils.decorators import platform_checker


@platform_checker
class Browser(Platform, BrowserManager):
    """
    Represents a web browser platform.

    Attributes:
    path (Optional[str]): The path to the browser executable, if available.
    """
    path: Optional[str] = field(default=None)

    @classmethod
    def cookiejar_to_dict(cls, cookiejar) -> dict:
        cookie_dict = {}
        for cookie in cookiejar:
            cookie_dict[cookie.name] = cookie.value
        return cookie_dict

    def get_chrome_cookies(self, url: str) -> dict:
        return self.cookiejar_to_dict(browser_cookie3.chrome(domain_name=url))

    def get_firefox_cookies(self, url: str) -> dict:
        if self.platform == PlatformOS.WINDOWS:
            return self.firefox.get_cookies_by_url(url)
        return self.cookiejar_to_dict(browser_cookie3.firefox(domain_name=url))

    def get_safari_cookies(self, url: str) -> dict:
        return self.cookiejar_to_dict(browser_cookie3.safari(domain_name=url))

    def get_edge_cookies(self, url: str) -> dict:
        return self.cookiejar_to_dict(browser_cookie3.edge(domain_name=url))
