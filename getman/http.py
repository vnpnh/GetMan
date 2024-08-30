from typing import Dict, Optional

import requests

from getman.manager.sessions import SessionManager
from getman.settings import Settings
from getman.utils.decorators import retry_request


class HTTPClient(SessionManager):
    """
    A client class for performing HTTP requests with retry functionality.

    Inherits from SessionManager to manage HTTP sessions and adds methods for GET, POST, PUT,
    DELETE, PATCH, and OPTIONS requests. Each method supports retries using the `retry_request`
    decorator.
    """

    @retry_request()
    def get(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        settings: Optional[Settings] = None,
        **kwargs,
    ) -> requests.Response:
        """
        Perform an HTTP GET request to the specified URL.

        Args:
            url (str): The URL to send the GET request to.
            params (Optional[Dict[str, str]], optional):
                Optional dictionary of query parameters to include in the request. Defaults to None.
            headers (Optional[Dict[str, str]], optional):
                Optional dictionary of HTTP headers to include in the request. Defaults to None.
            settings (Optional[Settings], optional):
                Settings object that includes timeout and other configurations. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the GET request.
        """
        timeout = settings.timeout if settings else None
        return self.session.get(url, params=params, headers=headers, timeout=timeout,
                                **kwargs)

    @retry_request()
    def post(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        data: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        settings: Optional[Settings] = None,
        **kwargs,
    ) -> requests.Response:
        """
        Perform an HTTP POST request to the specified URL.

        Args:
            url (str): The URL to send the POST request to.
            params (Optional[Dict[str, str]], optional):
                Optional dictionary of query parameters to include in the request. Defaults to None.
            data (Optional[Dict[str, str]], optional):
                Dictionary containing the data to be sent as the body of the request.
            headers (Optional[Dict[str, str]], optional):
                Optional dictionary of HTTP headers to include in the request. Defaults to None.
            settings (Optional[Settings], optional):
                Settings object that includes timeout and other configurations. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the POST request.
        """
        timeout = settings.timeout if settings else None
        return self.session.post(url, params=params, data=data, headers=headers, timeout=timeout,
                                 **kwargs)

    @retry_request()
    def put(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        data: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        settings: Optional[Settings] = None,
        **kwargs,
    ) -> requests.Response:
        """
        Perform an HTTP PUT request to the specified URL.

        Args:
            url (str): The URL to send the PUT request to.
            params (Optional[Dict[str, str]], optional):
                Optional dictionary of query parameters to include in the request. Defaults to None.
            data (Optional[Dict[str, str]], optional):
                Dictionary containing the data to be sent as the body of the request.
            headers (Optional[Dict[str, str]], optional):
                Optional dictionary of HTTP headers to include in the request. Defaults to None.
            settings (Optional[Settings], optional):
                Settings object that includes timeout and other configurations. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the PUT request.
        """
        timeout = settings.timeout if settings else None
        return self.session.put(url, params=params, data=data, headers=headers, timeout=timeout,
                                **kwargs)

    @retry_request()
    def delete(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        data: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        settings: Optional[Settings] = None,
        **kwargs,
    ) -> requests.Response:
        """
        Perform an HTTP DELETE request to the specified URL.

        Args:
            url (str): The URL to send the DELETE request to.
            params (Optional[Dict[str, str]], optional):
                Optional dictionary of query parameters to include in the request. Defaults to None.
            data (Optional[Dict[str, str]], optional):
                Dictionary containing the data to be sent as the body of the request.
            headers (Optional[Dict[str, str]], optional):
                Optional dictionary of HTTP headers to include in the request. Defaults to None.
            settings (Optional[Settings], optional):
                Settings object that includes timeout and other configurations. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the DELETE request.
        """
        timeout = settings.timeout if settings else None
        return self.session.delete(url, params=params, data=data, headers=headers, timeout=timeout,
                                   **kwargs)

    @retry_request()
    def patch(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        data: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        settings: Optional[Settings] = None,
        **kwargs,
    ) -> requests.Response:
        """
        Perform an HTTP PATCH request to the specified URL.

        Args:
            url (str): The URL to send the PATCH request to.
            params (Optional[Dict[str, str]], optional):
                Optional dictionary of query parameters to include in the request. Defaults to None.
            data (Optional[Dict[str, str]], optional):
                Dictionary containing the data to be sent as the body of the request.
            headers (Optional[Dict[str, str]], optional):
                Optional dictionary of HTTP headers to include in the request. Defaults to None.
            settings (Optional[Settings], optional):
                Settings object that includes timeout and other configurations. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the PATCH request.
        """
        timeout = settings.timeout if settings else None
        return self.session.patch(url, params=params, data=data, headers=headers, timeout=timeout,
                                  **kwargs)

    @retry_request()
    def options(
        self,
        url: str,
        params: Optional[Dict[str, str]] = None,
        data: Optional[Dict[str, str]] = None,
        headers: Optional[Dict[str, str]] = None,
        settings: Optional[Settings] = None,
        **kwargs,
    ) -> requests.Response:
        """
        Perform an HTTP OPTIONS request to the specified URL.

        Args:
            url (str): The URL to send the OPTIONS request to.
            params (Optional[Dict[str, str]], optional):
                Optional dictionary of query parameters to include in the request. Defaults to None.
            data (Optional[Dict[str, str]], optional):
                Dictionary containing the data to be sent as the body of the request.
            headers (Optional[Dict[str, str]], optional):
                Optional dictionary of HTTP headers to include in the request. Defaults to None.
            settings (Optional[Settings], optional):
                Settings object that includes timeout and other configurations. Defaults to None.

        Returns:
            requests.Response: The response object containing the result of the OPTIONS request.
        """
        timeout = settings.timeout if settings else None
        return self.session.options(url, params=params, data=data, headers=headers, timeout=timeout,
                                    **kwargs)
