import json
import socket
from dataclasses import dataclass

host: str = 'localhost'
port: int = 8888


@dataclass
class MockMan:
    """
    A class to manage a mock server for testing HTTP requests.
    """
    host: str = 'localhost'
    port: int = 8888
    mock: dict = None

    def add_mock(self, key, value):
        """
        Add a key-value pair to the mock data.
        """
        self.mock[key] = value

    def remove_data(self, key):
        """
        Remove a key from the mock data.
        """
        self.mock.pop(key, None)

    def get_data(self):
        """
        Get the mock data.
        """
        return self.mock


def handle_request(client_socket):
    """
    Handle a client request by parsing the request, extracting the method, path, and headers,
    """
    request_data = client_socket.recv(1024).decode()
    request_lines = request_data.split('\r\n')

    # Extract request method, path, and headers
    method, path, _ = request_lines[0].split(' ')
    headers = {}
    for line in request_lines[1:]:
        if line:
            header, value = line.split(': ')
            headers[header] = value

    # Extract query parameters from path
    query_params = {}
    if '?' in path:
        query_string = path.split('?')[1]
        query_params = dict(qc.split('=') for qc in query_string.split('&'))

    # Process request based on method
    if method == 'GET':
        # Create response JSON
        response = {
            "message": "Mock GET request received",
            "params": query_params
        }
        response_data = json.dumps(response).encode()

        # Send response headers
        response_headers = [
            'HTTP/1.1 200 OK',
            'Content-type: application/json',
            f'Content-length: {len(response_data)}',
            '\r\n'
        ]
        client_socket.sendall('\r\n'.join(response_headers).encode())

        # Send response body
        client_socket.sendall(response_data)
    elif method == 'POST':
        # Read request body
        content_length = int(headers['Content-Length'])
        request_body = client_socket.recv(content_length).decode()

        # Parse JSON body
        json_data = json.loads(request_body)

        # Create response JSON
        response = {
            "message": "Mock POST request received",
            "data": json_data
        }
        response_data = json.dumps(response).encode()

        # Send response headers
        response_headers = [
            'HTTP/1.1 200 OK',
            'Content-type: application/json',
            f'Content-length: {len(response_data)}',
            '\r\n'
        ]
        client_socket.sendall('\r\n'.join(response_headers).encode())

        # Send response body
        client_socket.sendall(response_data)
    else:
        # Invalid request method
        response_data = b'Invalid request method'

        # Send response headers
        response_headers = [
            'HTTP/1.1 400 Bad Request',
            'Content-type: text/plain',
            f'Content-length: {len(response_data)}',
            '\r\n'
        ]
        client_socket.sendall('\r\n'.join(response_headers).encode())

        # Send response body
        client_socket.sendall(response_data)

    client_socket.close()


def run_mock_server():
    """
    Run a mock server that listens for incoming HTTP requests and responds with mock
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Mock server running on {host}:{port}")

    while True:
        client_socket, _ = server_socket.accept()
        handle_request(client_socket)


if __name__ == '__main__':
    run_mock_server()
