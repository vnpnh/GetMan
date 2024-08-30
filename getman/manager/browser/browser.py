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
    path: Optional[str] = None

    @classmethod
    def cookiejar_to_dict(cls, cookiejar) -> dict:
        """
        Convert a CookieJar object into a dictionary where cookie names are keys and
        cookie values are the corresponding values.

        Args:
            cookiejar: A CookieJar object containing cookies.

        Returns:
            dict: A dictionary representation of the cookies in the CookieJar.
        """
        cookie_dict = {}
        for cookie in cookiejar:
            cookie_dict[cookie.name] = cookie.value
        return cookie_dict

    def get_chrome_cookies(self, url: str) -> dict:
        """
        Retrieve cookies for a specified URL from the Chrome browser.

        Args:
            url (str): The URL for which to retrieve cookies.

        Returns:
            dict: A dictionary of cookie names and values.
        """
        return self.cookiejar_to_dict(browser_cookie3.chrome(domain_name=url))

    def get_firefox_cookies(self, url: str) -> dict:
        """
        Retrieve cookies for a specified URL from the Firefox browser.

        If the platform is Windows, it retrieves cookies using the custom method
        `get_cookies_by_url`. Otherwise, it uses the browser_cookie3 library.

        Args:
            url (str): The URL for which to retrieve cookies.

        Returns:
            dict: A dictionary of cookie names and values.
        """
        if self.platform == PlatformOS.WINDOWS:
            return self.firefox.get_cookies_by_url(url)
        return self.cookiejar_to_dict(browser_cookie3.firefox(domain_name=url))

    def get_safari_cookies(self, url: str) -> dict:
        """
        Retrieve cookies for a specified URL from the Safari browser.

        Args:
            url (str): The URL for which to retrieve cookies.

        Returns:
            dict: A dictionary of cookie names and values.
        """
        return self.cookiejar_to_dict(browser_cookie3.safari(domain_name=url))

    def get_edge_cookies(self, url: str) -> dict:
        """
        Retrieve cookies for a specified URL from the Edge browser.

        Args:
            url (str): The URL for which to retrieve cookies.

        Returns:
            dict: A dictionary of cookie names and values.
        """
        return self.cookiejar_to_dict(browser_cookie3.edge(domain_name=url))
