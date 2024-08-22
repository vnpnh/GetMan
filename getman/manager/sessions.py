from typing import Any, Optional

import requests


class SessionManager:
    """
    A class that manages HTTP sessions and cookies.
    """
    session: requests.Session = requests.Session()

    def get_cookie(self, key: Optional[str] = None) -> Optional[str]:
        """
        Get the value of a specific cookie by its name, or retrieve all cookies as a dictionary.

        Args:
            key (Optional[str]): The name of the cookie to retrieve. If None, returns all cookies.

        Returns:
            Optional[str]: The value of the cookie if found, or None if the cookie doesn't exist.
                If no key is provided, returns a dictionary containing all cookies.
        """
        if key is None:
            return self.session.cookies.get_dict()
        return self.session.cookies.get(key)

    def add_cookie(self, key: str, value: Any):
        """
        Add a header to the existing headers.

        Args:
            key (str): The header key.
            value (Any): The header value.
        """
        self.session.cookies.set(key, value)

    def add_cookies(self, data: dict):
        """
        Add a header to the existing headers.

        Args:
            data (dict): The data of dict.
        """
        for key, value in data.items():
            self.session.cookies.set(key, value)

    def update_cookie(self, key: str, value: Any):
        """
        Update a cookie value in the existing cookies.

        Args:
            key (str): The cookie key.
            value (Any): The new cookie value.
        """
        if key in self.session.cookies:
            self.session.cookies[key] = value
        else:
            self.add_cookie(key, value)
            raise KeyError(f"Cookie '{key}' does not exist. Set automatically")

    def remove_cookies(self, key: Optional[str] = None):
        """
        Remove cookies from the session.

        Args:
            key (Optional[str]): The key of the cookie to remove.
             If None, all cookies will be cleared.
        """
        if key is None:
            self.session.cookies.clear()
        else:
            self.session.cookies.pop(key, None)
