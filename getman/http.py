import requests

from typing import Dict, Optional

from getman.manager.sessions import SessionManager
from getman.settings import Settings
from getman.utils.decorators import retry_request


class HTTPClient(SessionManager):
	@retry_request()
	def get(
			self,
			url: str,
			params: Optional[Dict[str, str]] = None,
			headers: Optional[Dict[str, str]] = None,
			settings: Settings = None,
			**kwargs,
	) -> requests.Response:
		"""
		Perform an HTTP GET request to the specified URL.

		Args:
			url (str): The URL to send the GET request to.
			params (Optional[Dict[str, str]], optional): Optional dictionary of query parameters to include in the request. Defaults to None.
			headers (Optional[Dict[str, str]], optional): Optional dictionary of HTTP headers to include in the request. Defaults to None.
			settings: settings
		Returns:
			requests.Response: The response object containing the result of the GET request.
		"""
		return self.session.get(url, params=params, headers=headers, timeout=settings.timeout, **kwargs)

	@retry_request()
	def post(
			self,
			url: str,
			params: Optional[Dict[str, str]] = None,
			data: Optional[Dict[str, str]] = None,
			headers: Optional[Dict[str, str]] = None,
			settings: Settings = None,
			**kwargs,
	) -> requests.Response:
		"""
		Perform an HTTP POST request to the specified URL.

		Args:
			url (str): The URL to send the POST request to.
			params (Optional[Dict[str, str]], optional): Optional dictionary of query parameters to include in the request. Defaults to None.
			data (Dict[str, str]): Dictionary containing the data to be sent as the body of the request.
			headers (Optional[Dict[str, str]], optional): Optional dictionary of HTTP headers to include in the request. Defaults to None.
			settings: settings
		Returns:
			requests.Response: The response object containing the result of the POST request.
		"""
		return self.session.post(url, params=params, data=data, headers=headers, timeout=settings.timeout, **kwargs)

	@retry_request()
	def put(
			self,
			url: str,
			params: Optional[Dict[str, str]] = None,
			data: Optional[Dict[str, str]] = None,
			headers: Optional[Dict[str, str]] = None,
			settings: Settings = None,
			**kwargs,
	) -> requests.Response:
		"""
		Perform an HTTP PUT request to the specified URL.

		Args:
			url (str): The URL to send the PUT request to.
			params (Optional[Dict[str, str]], optional): Optional dictionary of query parameters to include in the request. Defaults to None.
			data (Dict[str, str]): Dictionary containing the data to be sent as the body of the request.
			headers (Optional[Dict[str, str]], optional): Optional dictionary of HTTP headers to include in the request. Defaults to None.
			settings: settings
		Returns:
			requests.Response: The response object containing the result of the PUT request.
		"""
		return self.session.put(url, params=params, data=data, headers=headers, timeout=settings.timeout, **kwargs)

	@retry_request()
	def delete(
			self,
			url: str,
			params: Optional[Dict[str, str]] = None,
			data: Optional[Dict[str, str]] = None,
			headers: Optional[Dict[str, str]] = None,
			settings: Settings = None,
			**kwargs,
	) -> requests.Response:
		"""
		Perform an HTTP DELETE request to the specified URL.

		Args:
			url (str): The URL to send the DELETE request to.
			params (Optional[Dict[str, str]], optional): Optional dictionary of query parameters to include in the request. Defaults to None.
			data (Dict[str, str]): Dictionary containing the data to be sent as the body of the request.
			headers (Optional[Dict[str, str]], optional): Optional dictionary of HTTP headers to include in the request. Defaults to None.
			settings: settings
		Returns:
			requests.Response: The response object containing the result of the DELETE request.
		"""
		return self.session.delete(url, params=params, data=data, headers=headers, timeout=settings.timeout, **kwargs)

	@retry_request()
	def patch(
			self,
			url: str,
			params: Optional[Dict[str, str]] = None,
			data: Optional[Dict[str, str]] = None,
			headers: Optional[Dict[str, str]] = None,
			settings: Settings = None,
			**kwargs,
	) -> requests.Response:
		"""
		Perform an HTTP PATCH request to the specified URL.

		Args:
			url (str): The URL to send the PATCH request to.
			params (Optional[Dict[str, str]], optional): Optional dictionary of query parameters to include in the request. Defaults to None.
			data (Dict[str, str]): Dictionary containing the data to be sent as the body of the request.
			headers (Optional[Dict[str, str]], optional): Optional dictionary of HTTP headers to include in the request. Defaults to None.
			settings: settings
		Returns:
			requests.Response: The response object containing the result of the PATCH request.
		"""
		return self.session.patch(url, params=params, data=data, headers=headers, timeout=settings.timeout, **kwargs)

	@retry_request()
	def options(
			self,
			url: str,
			params: Optional[Dict[str, str]] = None,
			data: Optional[Dict[str, str]] = None,
			headers: Optional[Dict[str, str]] = None,
			settings: Settings = None,
			**kwargs,
	) -> requests.Response:
		"""
		Perform an HTTP Options request to the specified URL.

		Args:
			url (str): The URL to send the PATCH request to.
			params (Optional[Dict[str, str]], optional): Optional dictionary of query parameters to include in the request. Defaults to None.
			data (Dict[str, str]): Dictionary containing the data to be sent as the body of the request.
			headers (Optional[Dict[str, str]], optional): Optional dictionary of HTTP headers to include in the request. Defaults to None.
			settings: settings
		Returns:
			requests.Response: The response object containing the result of the PATCH request.
		"""
		return self.session.options(url, params=params, data=data, headers=headers, timeout=settings.timeout, **kwargs)
