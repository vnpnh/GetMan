import asyncio
import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Union

from rich.console import Console
from rich.theme import Theme

from getman.constant import HttpMethod
from getman.http import HTTPClient
from getman.manager import DictManager
from getman.manager.queue import QueueManager
from getman.settings import Settings


@dataclass
class GetMan(HTTPClient, QueueManager):
    """
       A client for managing HTTP requests with queuing and other utilities.
    """
    base_url: str
    version: Optional[str] = ""
    token: Optional[str] = None
    settings: Settings = field(default_factory=Settings)
    console: Console = field(init=False)
    url: Optional[str] = None

    def __post_init__(self):
        self.console = Console(
            theme=Theme(self.settings.style),
            color_system=self.settings.color_system,
        )
        self.url = self.normalized_url(self.base_url, self.version)

    @classmethod
    def normalized_url(cls, *parts: str) -> str:
        """
        Combine multiple URL components ensuring no double slashes.

        Args:
            parts (str): URL components to be combined.

        Returns:
            str: The combined URL.
        """
        cleaned_parts = []

        for part in parts:
            if '://' in part:
                protocol, remaining = part.split('://', 1)
                cleaned_parts.append(f"{protocol}://{remaining.rstrip('/')}")
            else:
                cleaned_parts.append(part.strip('/'))

        return "/".join(cleaned_parts)

    def routes(self, *args) -> str:
        """
            Constructs a URL by concatenating the base URL, version, and additional path components.

            Args:
                *args: Variable number of path components to be appended to the URL.

            Returns:
                str: The constructed URL.

            Example:
                baseURL = "https://example.com"
                version = "v1"
                client = GetMan(baseURL, version)
                route = client.routes("users", "123", "profile")
                # Result: "https://example.com/v1/users/123/profile"
        """

        url_components = [self.base_url]
        if getattr(self, 'version', None):
            url_components.append(self.version)
        url_components.extend(args)
        self.url = self.normalized_url(*url_components)

        return self.url

    async def perform_request(
            self,
            method: Union[str, HttpMethod],
            routes: Optional[str] = None,
            data: Optional[Union[Dict, DictManager]] = None,
            headers: Optional[Union[Dict, DictManager]] = None,
            params: Optional[Union[Dict, DictManager]] = None,
            queue: Optional[bool] = False,
            **kwargs
    ) -> HTTPClient or None:
        """
        Perform an API async request.

        Args:
        - method: The HTTP method to use.
        - routes: The routes for the request.
        - headers: The headers to send with the request.
        - params: The query parameters to send with the request.
        - data: The body data to send with the request.
        - queue: If True, the request will be queued and if False will execute current request

        Raises:
        - ValueError: If the method is not supported.

        Returns:
        - The response of the request or coroutine if queue is true.
        """

        if queue:
            self.enqueue(
                lambda: asyncio.create_task(
                    self.async_request(method, routes, data, headers, params, **kwargs)
                )
            )
            return

        return await self.async_request(method, routes, data, headers, params, **kwargs)

    async def execute_queue(self) -> List[HTTPClient] or None:
        """
        Execute the queued requests.

        Returns:
            A list of responses if the queue is not empty.
        """
        if not self.is_queue_empty():
            tasks = [task_creator() for task_creator in self.get_queues()]
            self.clear_queue()
            results = await asyncio.gather(*tasks)
            return results

    async def async_request(
            self,
            method: Union[str, HttpMethod],
            routes: str = None,
            data: Union[Dict, DictManager] = None,
            headers: Union[Dict, DictManager] = None,
            params: Union[Dict, DictManager] = None,
            **kwargs
    ):
        """
        Perform an asynchronous API request.

        Args:
            method (Union[str, HttpMethod]):
                The HTTP method to use (GET, POST, etc.).
            routes (Optional[str]):
                The API route or endpoint to send the request to. Defaults to None.
            data (Optional[Union[Dict, DictManager]]):
                The data to send in the body of the request. Defaults to None.
            headers (Optional[Union[Dict, DictManager]]):
                The headers to send with the request. Defaults to None.
            params (Optional[Union[Dict, DictManager]]):
                The query parameters to send with the request. Defaults to None.
            **kwargs: Additional keyword arguments to pass to the request method.

        Returns:
            Optional[object]:
                The response from the request method, or None if the request is queued.
        """
        return self.request(method, routes, data, headers, params, **kwargs)

    def request(
            self,
            method: Union[str, HttpMethod],
            routes: str = None,
            data: Union[Dict, DictManager] = None,
            headers: Union[Dict, DictManager] = None,
            params: Union[Dict, DictManager] = None,
            queue: Optional[bool] = False,
            **kwargs
    ) -> HTTPClient or None:
        """
        Perform an API request.

        Args:
            method: The HTTP method to use.
            routes: The routes for the request.
            headers: The headers to send with the request.
            params: The query parameters to send with the request.
            data: The body data to send with the request.
            settings: The settings to use for the request.
            queue: If True, the request will be queued and if False will execute current request

        Returns:
            requests.Response: The response object containing the result of the request.
        """

        routes = routes or self.url

        if queue:
            self.enqueue(
                lambda: asyncio.create_task(
                    self.async_request(method, routes, data, headers, params, **kwargs)
                )
            )
            return

        if isinstance(method, HttpMethod):
            method = method.value

        match method:
            case HttpMethod.GET:
                return self.get(
                    url=routes,
                    headers=headers,
                    params=params,
                    settings=self.settings,
                    **kwargs,
                )
            case HttpMethod.POST:
                return self.post(
                    url=routes,
                    headers=headers,
                    params=params,
                    data=data,
                    settings=self.settings,
                    **kwargs,
                )
            case HttpMethod.DELETE:
                return self.delete(
                    url=routes,
                    headers=headers,
                    params=params,
                    data=data,
                    settings=self.settings,
                    **kwargs)
            case HttpMethod.PUT:
                return self.put(
                    url=routes,
                    headers=headers,
                    params=params,
                    data=data,
                    settings=self.settings,
                    **kwargs,
                )
            case HttpMethod.PATCH:
                return self.patch(
                    url=routes,
                    headers=headers,
                    params=params,
                    data=data,
                    settings=self.settings,
                    **kwargs)
            case HttpMethod.OPTION:
                return self.options(
                    url=routes,
                    headers=headers,
                    params=params,
                    data=data,
                    settings=self.settings,
                    **kwargs,
                )
            case _:
                raise ValueError(
                    "Method not allowed, only get, post, delete, put, patch, and options"
                )


    def get_report(
            self,
            data,
            show_cookies: Optional[bool] = False,
            show_request_header: Optional[bool] = False,
            show_response_header: Optional[bool] = False,
            show_settings: Optional[bool] = False,
    ) -> str:
        """
        Generates a report based on provided data and optional flags.

        :param data: Input data
        :param show_cookies: Flag to determine if cookies should be included in the report
        :param show_request_header: Flag to determine
        if request headers should be included in the report
        :param show_response_header: Flag to determine
        if response headers should be included in the report
        :param show_settings: Flag to determine if settings should be included in the report
        :return: A formatted report string
        """

        if data is None:
            raise ValueError("No data provided to generate a report.")

        if isinstance(data, list):
            for item in data:
                return self.get_report(
                    item,
                    show_cookies,
                    show_request_header,
                    show_response_header,
                    show_settings,
                )

        sections = [
            f"URL: {data.url}",
            f"Method: {data.request.method}",
            f"Status Code: {data.status_code} ({data.reason})",
            f"Cookies: {self.get_cookie()}" if show_cookies else "",
            f"Request Header: {data.request.headers}" if show_request_header else "",
            f"Response Header: {data.headers}" if show_response_header else "",
            f"Settings: {self.settings}" if show_settings else ""
        ]

        try:
            json_response = json.dumps(data.json(), indent=2)
            sections.append(f"JSON Response: {json_response}")
        except json.JSONDecodeError:
            sections.append(f"Response Text: {data.text}")

        sections.append(f"Elapsed Time (seconds): {data.elapsed.total_seconds()}")
        report = "\n".join(filter(bool, sections))
        self.console.print(report, style="info")

        return report
