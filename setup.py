import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='getman',
    version='0.0.3.18',  # This is testing version
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
    ],
    include_package_data=True,
    install_requires=[
        "requests>=2.31.0",
        "rich>=13.5.0",
        "browser-cookie3>=0.19.1",
    ],
    python_requires=">=3.6",
    setup_requires=["wheel"],
)
