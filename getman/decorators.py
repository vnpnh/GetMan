import requests
import time
from functools import wraps
import functools
import warnings


def deprecated(func):
	"""
	This is a decorator which can be used to mark functions
	as deprecated. It will result in a warning being emitted
	when the function is used.
	"""

	@functools.wraps(func)
	def new_func(*args, **kwargs):
		warnings.warn(f"Call to deprecated function {func.__name__}.", DeprecationWarning, stacklevel=2)
		return func(*args, **kwargs)

	return new_func


def retry_request():
	def decorator_request(func):
		@wraps(func)
		def wrapper_request(*args, **kwargs):
			max_retries = kwargs.get("settings").retries
			retry_delay_seconds = kwargs.get("settings").delay
			for retry in range(max_retries):
				try:
					response = func(*args, **kwargs)
					# Process the response
					print(response.status_code)
					return response
				except (requests.Timeout, requests.ConnectionError) as e:
					# Handle timeout or connection errors
					print(f"Retry {retry + 1}: {e}")
					if retry < max_retries - 1:
						# Wait for the specified delay before the next retry
						time.sleep(retry_delay_seconds)
			print("Request failed after maximum retries.")
			return None

		return wrapper_request

	return decorator_request
