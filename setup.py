import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
	name='getman',
	version='0.0.1',
	packages=['getman', 'getman.manager'],
	url='https://github.com/vnpnh/GetMan',
	license='MIT',
	keywords="API testing, API exploration, HTTP requests, API endpoints, request headers, query parameters, request bodies, API management, Postman alternative, RESTful APIs, testing tool, debugging tool, development tools, API client, API interaction.",
	author='vnpnh',
	author_email='no@email.com',
	description='GetMan is a versatile tool inspired by Postman that simplifies the process of testing and exploring APIs. It provides a user-friendly interface for sending HTTP requests, inspecting responses, and managing API endpoints. With API Explorer, you can easily set request headers, query parameters, and request bodies. You can also save and organize your favorite API endpoints, making it convenient to access and reuse them. Whether you are testing, debugging, or exploring APIs, API Explorer is your go-to tool for seamless API interaction.',
	long_description=README,
	long_description_content_type="text/markdown",
	classifiers=[
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3.11",
	],
	include_package_data=True,
	install_requires=["requests", "pycookiecheat", 'rich'],
)
