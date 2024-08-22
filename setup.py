import pathlib

from setuptools import find_packages, setup

from getman import version

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='getman',
    version=version.VERSION_TEXT,
    packages=find_packages(exclude=["tests", "tests.*"]),
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
        "Programming Language :: Python :: 3.12",
    ],
    include_package_data=True,
    install_requires=[
        "requests>=2.32.3",
        "rich>=13.7.1",
        "browser-cookie3>=0.19.1",
    ],
    python_requires=">=3.9",
    setup_requires=["wheel"],
)
