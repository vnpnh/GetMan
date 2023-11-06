import functools
import time
import warnings

import requests

from getman.constant import PlatformOS


def platform_checker(cls):
    def wrapper(*args, **kwargs):
        # Check if the platform exists and is not Windows, Linux, or Darwin
        print(kwargs)
        if 'platform' in kwargs and kwargs['platform'] not in [PlatformOS.WINDOWS, PlatformOS.LINUX, PlatformOS.DARWIN]:
            unsupported_platform = kwargs['platform']
            warnings.warn(
                f"Unsupported platform '{unsupported_platform}'. The platform will be automatically determined based on the operating system.")
            kwargs.pop('platform')
        return cls(*args, **kwargs)

    return wrapper


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
        @functools.wraps(func)
        def wrapper_request(*args, **kwargs):
            settings = kwargs.get("settings")
            max_retries = settings.retries
            retry_delay_seconds = settings.delay
            timeout_increment = settings.timeout_increment
            for retry in range(max_retries):
                try:
                    response = func(*args, **kwargs)
                    return response
                except (requests.Timeout, requests.ConnectionError) as e:
                    # Handle timeout or connection errors
                    print(f"Retry {retry + 1}: {e}")
                    settings.timeout += timeout_increment
                    kwargs['settings'] = settings
                    if retry < max_retries - 1:
                        # Wait for the specified delay before the next retry
                        time.sleep(retry_delay_seconds)
            print("Request failed after maximum retries.")
            return None

        return wrapper_request

    return decorator_request
