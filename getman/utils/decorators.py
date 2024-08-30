import asyncio
import functools
import time
import warnings
from functools import wraps

import requests

from getman.constant import PlatformOS


def platform_checker(cls):
    """
        A class decorator that checks if the provided platform is supported.

        This decorator will issue a warning if the provided `platform` keyword argument
        is not one of the supported platforms (WINDOWS, LINUX, DARWIN). If the platform
        is unsupported, it will be removed from the keyword arguments.

        Args:
            cls: The class to be decorated.

        Returns:
            The decorated class with platform checking logic.
    """

    def wrapper(*args, **kwargs):
        if ('platform' in kwargs and
                kwargs['platform'] not in [
                    PlatformOS.WINDOWS,
                    PlatformOS.LINUX,
                    PlatformOS.DARWIN,
                ]
        ):
            unsupported_platform = kwargs['platform']
            warnings.warn(
                f"Unsupported platform '{unsupported_platform}'."
                f" The platform will be automatically determined based on the operating system.")
            kwargs.pop('platform')
        return cls(*args, **kwargs)

    return wrapper


def deprecated(func=None, *, message=None, version=None):
    """
    A decorator to mark functions as deprecated.

    This decorator will emit a warning whenever the decorated function is called,
    indicating that the function is deprecated and should not be used. Optionally,
    a custom message or a removal version can be specified.

    Args:
        func: The function to be decorated.
        message: Optional. A custom message to include in the deprecation warning.
        version: Optional. The version when the function is expected to be removed.

    Returns:
        A new function that emits a deprecation warning and then calls the original function.
    """
    if func is None:
        return lambda func: deprecated(func, message=message, version=version)

    @functools.wraps(func)
    def new_func(*args, **kwargs):
        warn_message = message if message else f"Call to deprecated function {func.__name__}."
        if version:
            warn_message += f" This function will be removed in version {version}."
        warnings.warn(
            warn_message,
            DeprecationWarning,
            stacklevel=2,
        )
        return func(*args, **kwargs)

    return new_func


def retry_request():
    """
        A decorator to retry a function call on failure.

        This decorator retries the decorated function if it raises a timeout or connection error.
        It uses settings provided in the `settings` keyword argument to determine the number
        of retries, delay between retries, and timeout increment.

        The `settings` argument should have the following attributes:
        - `retries`: The maximum number of retries.
        - `delay`: The delay in seconds between retries.
        - `timeout_increment`: The amount to increment the timeout for each retry.
        - `timeout`: The initial timeout value.

        Returns:
            A decorator that wraps the function with retry logic.
    """

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


def coroutine(func):
    """
       A decorator to run a synchronous function as if it were asynchronous.

       This decorator wraps a synchronous function and runs it in an asynchronous event loop.
       It is useful for running synchronous code in an asynchronous context.

       Args:
           func: The synchronous function to be decorated.

       Returns:
           A function that runs the original function within an asynchronous event loop.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        async def async_func():
            return await func(*args, **kwargs)

        return asyncio.run(async_func())

    return wrapper
