import asyncio
import unittest
from unittest.mock import AsyncMock, MagicMock, patch

from getman.client import GetMan
from getman.constant import HttpMethod
from getman.settings import Settings


class TestGetMan(unittest.TestCase):

    @patch('getman.client.Console')
    def setUp(self, mock_console):
        self.settings = Settings()
        self.client = GetMan(base_url="https://example.com", version="v1", settings=self.settings)

    @patch('getman.client.GetMan.get')
    def test_request_get_method(self, mock_get):
        self.client.request(HttpMethod.GET, "users/123")
        mock_get.assert_called_once_with(url="users/123", headers=None, params=None, settings=self.settings)

    @patch('getman.client.GetMan.post')
    def test_request_post_method(self, mock_post):
        self.client.request(HttpMethod.POST, "users/123", data={"key": "value"})
        mock_post.assert_called_once_with(url="users/123", headers=None, params=None, data={"key": "value"},
                                          settings=self.settings)

    @patch('getman.client.GetMan.delete')
    def test_request_delete_method(self, mock_delete):
        self.client.request(HttpMethod.DELETE, "users/123")
        mock_delete.assert_called_once_with(url="users/123", headers=None, params=None, data=None,
                                            settings=self.settings)

    @patch('getman.client.GetMan.put')
    def test_request_put_method(self, mock_put):
        self.client.request(HttpMethod.PUT, "users/123", data={"key": "value"})
        mock_put.assert_called_once_with(url="users/123", headers=None, params=None, data={"key": "value"},
                                         settings=self.settings)

    @patch('getman.client.GetMan.patch')
    def test_request_patch_method(self, mock_patch):
        self.client.request(HttpMethod.PATCH, "users/123", data={"key": "value"})
        mock_patch.assert_called_once_with(url="users/123", headers=None, params=None, data={"key": "value"},
                                           settings=self.settings)

    @patch('getman.client.GetMan.options')
    def test_request_options_method(self, mock_options):
        self.client.request(HttpMethod.OPTION, "users/123", data={"key": "value"})
        mock_options.assert_called_once_with(url="users/123", headers=None, params=None, data={"key": "value"},
                                             settings=self.settings)


    def test_request_raises_value_error_for_invalid_method(self):
        with self.assertRaises(ValueError):
            self.client.request("INVALID_METHOD", "users/123")

    def test_normalized_url_combines_parts_correctly(self):
        result = self.client.normalized_url("https://example.com", "v1", "users", "123")
        self.assertEqual(result, "https://example.com/v1/users/123")

    def test_routes_constructs_correct_url(self):
        result = self.client.routes("users", "123", "profile")
        self.assertEqual(result, "https://example.com/v1/users/123/profile")

    @patch('getman.client.asyncio.create_task')
    def test_perform_request_queues_request_when_queue_is_true(self, mock_create_task):
        self.client.enqueue = MagicMock()
        asyncio.run(self.client.perform_request(HttpMethod.GET, queue=True))
        self.client.enqueue.assert_called_once()

    @patch('getman.client.asyncio.create_task')
    def test_perform_request_executes_request_when_queue_is_false(self, mock_create_task):
        self.client.async_request = AsyncMock()
        asyncio.run(self.client.perform_request(HttpMethod.GET, queue=False))
        self.client.async_request.assert_called_once()

    def test_get_report_raises_value_error_when_no_data_provided(self):
        with self.assertRaises(ValueError):
            self.client.get_report(None)

    def test_get_report_generates_correct_report(self):
        data = MagicMock()
        data.url = "https://example.com"
        data.request.method = "GET"
        data.status_code = 200
        data.reason = "OK"
        data.json.return_value = {"key": "value"}
        data.elapsed.total_seconds.return_value = 1.23
        result = self.client.get_report(data)
        self.assertIn("URL: https://example.com", result)
        self.assertIn("Method: GET", result)
        self.assertIn("Status Code: 200 (OK)", result)
        self.assertIn("JSON Response: {\n  \"key\": \"value\"\n}", result)
        self.assertIn("Elapsed Time (seconds): 1.23", result)

if __name__ == '__main__':
    unittest.main()