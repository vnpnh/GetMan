import json
from dataclasses import dataclass, field
from typing import Optional

import pycookiecheat
from rich.console import Console
from rich.theme import Theme

from getman.constant import HttpMethod
from getman.decorators import deprecated
from getman.http import HTTPClient
from getman.manager.dict import DictManager
from getman.settings import Settings


@dataclass
class GetMan(HTTPClient):
	baseURL: str
	version: Optional[str] = ""
	token: Optional[str] = None
	settings: Settings = field(default_factory=Settings)
	console: Console = field(init=False)

	def __post_init__(self):
		self.console = Console(theme=Theme(self.settings.style), color_system=self.settings.color_system)

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
		url_parts = [self.baseURL, self.version] + list(args)
		url = "/".join(filter(None, url_parts))
		return url

	def perform_request(
			self,
			method: HttpMethod,
			routes: str,
			header: dict or DictManager = None,
			params: dict or DictManager = None,
			data: dict or DictManager = None,
	):
		match method:
			case HttpMethod.GET:
				return self.get(url=routes, headers=header, params=params, settings=self.settings)
			case HttpMethod.POST:
				return self.post(url=routes, headers=header, data=data)
			case HttpMethod.DELETE:
				return self.delete(url=routes, headers=header)
			case HttpMethod.PUT:
				return self.put(url=routes, headers=header, data=data)
			case HttpMethod.PATCH:
				return self.patch(url=routes, headers=header, data=data)
			case _:
				raise ValueError("Method not allowed, only get, post, delete, put, patch")

	@deprecated
	def run(self, method: str, routes: str, expected: dict[str, list], headers: list[dict],
	        query_params: list[dict] = None):
		total = len(expected.get('name'))
		success = 0
		failed = 0

		params = {}
		header = headers[0]
		for i in range(total):
			if query_params is not None:
				params = query_params[i]

			if len(headers) > 1:
				header = headers[i]

			r = self.perform_request(method, routes, header, params)
			data = r.json()
			key = data.keys()
			key = list(key)[0]
			flag_failed = False
			if expected.get("total_data"):
				if len(data.get(key)) != expected["total_data"][i]:
					flag_failed = True
					self.console.print(
						"{} Failed (total data)!\tExpected: {}, Actual: {}".format(expected["name"][i],
						                                                           expected["total_data"][i],
						                                                           len(data.get(key))),
						style="failed")
			# self.console.print(data, ":vampire:")

			if r.status_code != expected["status_code"][i]:
				self.console.print(
					"{} Failed!\tExpected: {}, Actual: {}".format(expected["name"][i], expected["status_code"][i],
					                                              r.status_code), style="failed")
				# self.console.print(data, ":vampire:")
				flag_failed = True

			if flag_failed:
				failed += 1
				continue

			self.console.print("{} Passed!".format(expected["name"][i]), style="success")
			# self.console.print(data, ":vampire:")
			success += 1

		self.console.print("Success: {}, Failed: {}, total: {}".format(success, failed, total), style="info")

	def get_report(self, data, show_cookies: bool = False):
		url = data.url
		status_code = data.status_code
		elapsed_time = data.elapsed.total_seconds()

		report = f"URL: {url}\n"
		if show_cookies:
			report += f"Cookies: {self.get_cookie()}\n"
		report += f"Status Code: {status_code} ({data.reason})\n"

		try:
			json_response = json.dumps(data.json(), indent=2)
			report += f"JSON Response: {json_response}\n"
		except json.JSONDecodeError:
			report += "Invalid JSON Response\n"

		report += f"Elapsed Time (seconds): {elapsed_time}\n"
		self.console.print(report, style="info")

		return report

	def get_chrome_cookies(self, set_cookies: bool = True) -> dict:
		cookies = pycookiecheat.chrome_cookies(self.baseURL)
		if set_cookies:
			self.add_cookies(cookies)
		return cookies
