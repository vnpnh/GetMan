import unittest
import warnings
from unittest.mock import MagicMock, patch

import requests

from getman.utils.decorators import deprecated, platform_checker, retry_request


class TestDecorators(unittest.TestCase):

    def test_platform_checker(self):
        @platform_checker
        class MockClass:
            def __init__(self, platform=None):
                self.platform = platform

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            instance = MockClass(platform="UNSUPPORTED")
            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[-1].category, UserWarning))
            self.assertIn("Unsupported platform", str(w[-1].message))
            self.assertIsNone(instance.platform)

    def test_deprecated(self):
        @deprecated(message="This function is deprecated.", version="2.0")
        def mock_function():
            return "test"

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            result = mock_function()
            self.assertEqual(result, "test")
            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))
            self.assertIn("This function is deprecated.", str(w[-1].message))
            self.assertIn("2.0", str(w[-1].message))

    @patch("time.sleep", return_value=None)
    def test_retry_request(self, _):
        settings = MagicMock(retries=3, delay=1, timeout_increment=1, timeout=1)

        @retry_request()
        def mock_request(settings):
            raise requests.Timeout("Timeout error")

        result = mock_request(settings=settings)
        self.assertIsNone(result)
        self.assertEqual(settings.timeout, 4)


if __name__ == "__main__":
    unittest.main()