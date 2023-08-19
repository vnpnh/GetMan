import json
from dataclasses import dataclass, field
from typing import Optional, Union, Dict

from rich.console import Console
from rich.theme import Theme

from getman import DictManager
from getman.constant import HttpMethod
from getman.http import HTTPClient
from getman.settings import Settings


@dataclass
class GetMan(HTTPClient):
	baseURL: str
	version: Optional[str] = ""
	token: Optional[str] = None
	settings: Settings = field(default_factory=Settings)
	console: Console = field(init=False)
	url: Optional[str] = None

	def __post_init__(self):
		self.console = Console(theme=Theme(self.settings.style), color_system=self.settings.color_system)
		self.url = self.normalized_url(self.baseURL, self.version)

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

		url_components = [self.baseURL]
		if getattr(self, 'version', None):
			url_components.append(self.version)
		url_components.extend(args)
		self.url = self.normalized_url(*url_components)

		return self.url

	def perform_request(
			self,
			method: Union[str, HttpMethod],
			routes: Optional[str] = None,
			data: Optional[Union[Dict, DictManager]] = None,
			headers: Optional[Union[Dict, DictManager]] = None,
			params: Optional[Union[Dict, DictManager]] = None,
			**kwargs
	):
		"""
		Perform an API request.

		Args:
		- method: The HTTP method to use.
		- routes: The routes for the request.
		- headers: The headers to send with the request.
		- params: The query parameters to send with the request.
		- data: The body data to send with the request.

		Raises:
		- ValueError: If the method is not supported.

		Returns:
		- The response of the request.
		"""
		routes = routes or self.url

		match method:
			case HttpMethod.GET:
				return self.get(url=routes, headers=headers, params=params, settings=self.settings, **kwargs)
			case HttpMethod.POST:
				return self.post(url=routes, headers=headers, params=params, data=data, settings=self.settings, **kwargs)
			case HttpMethod.DELETE:
				return self.delete(url=routes, headers=headers, params=params, data=data, settings=self.settings, **kwargs)
			case HttpMethod.PUT:
				return self.put(url=routes, headers=headers, params=params, data=data, settings=self.settings, **kwargs)
			case HttpMethod.PATCH:
				return self.patch(url=routes, headers=headers, params=params, data=data, settings=self.settings, **kwargs)
			case HttpMethod.OPTION:
				return self.options(url=routes, headers=headers, params=params, data=data, settings=self.settings, **kwargs)
			case _:
				raise ValueError("Method not allowed, only get, post, delete, put, patch, and options")

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
		:param show_request_header: Flag to determine if request headers should be included in the report
		:param show_response_header: Flag to determine if response headers should be included in the report
		:param show_settings: Flag to determine if settings should be included in the report
		:return: A formatted report string
		"""
		sections = [
			f"URL: {data.url}",
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
