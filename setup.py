import pathlib
from setuptools import setup
import os
lib_folder = os.path.dirname(os.path.realpath(__file__))
requirement_path = f"{lib_folder}/requirements.txt"
install_requires = [] # Here we'll add: ["gunicorn", "docutils>=0.3", "lxml==0.5a7"]
if os.path.isfile(requirement_path):
    with open(requirement_path) as f:
        install_requires = f.read().splitlines()

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

from os import path as os_path

from setuptools import setup, find_packages


this_directory = os_path.abspath(os_path.dirname(__file__))


def read_file(filename):
    with open(os_path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines() if not line.startswith('#')]

setup(
	name='getman',
	version='0.0.3.7.2',
	packages=['getman', 'getman.manager', 'getman.models'],
	url='https://github.com/vnpnh/GetMan',
	license='MIT',
	keywords="API testing, API exploration, HTTP requests, API endpoints, request headers, query parameters, request bodies, API management, Postman alternative, RESTful APIs, testing tool, debugging tool, development tools, API client, API interaction.",
	author='vnpnh',
	author_email='no@email.com',
	description='GetMan is a versatile tool inspired by Postman that simplifies the process of testing and exploring APIs.',
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
	# install_requires=[
	# 	"requests>=2.31.0",
	# 	"rich>=13.4.2",
	# 	"pycookiecheat>=0.5.0",
	# ],
	install_requires=read_requirements("requirements.txt")
)
