<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->

[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="#">
    <img src="https://storage.enlorve.com/assets/file/photos/getman/getman_logo.png" alt="Logo" width="150" height="150">
  </a>

<h3 align="center">GetMan</h3>

  <p align="center">
   GetMan is a versatile tool inspired by Postman that simplifies the process of testing and exploring APIs.
    <br />
    <a href="#"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="#">Report Bug</a>
    ·
    <a href="#">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

GetMan is a Python-based API testing tool inspired by Postman. It simplifies the process of testing and exploring APIs
by providing a simple and intuitive functions for making HTTP requests.

Key features of GetMan include:

- **Versatile HTTP Client**: GetMan supports all common HTTP methods and allows you to customize your requests with
  headers, query parameters, and body data.
- **Queue Management**: GetMan allows you to queue your requests and execute them concurrently. This can significantly
  improve the performance of your program when dealing with a large number of requests.
- **Report Generation**: GetMan can generate detailed reports of your API requests, including the request URL, method,
  status code, headers, and response data.
- **And Much More...**

Whether you're a developer testing your own APIs or a tester exploring third-party APIs, GetMan provides a powerful and
flexible tool to help you get the job done.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

This project built with the following technologies:

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Before you can use GetMan, you need to have the following software installed on your system:

* Python
  ```sh 
  Install python from https://www.python.org/
  ```

### Installation

To install the library, you can just run the following command:

1. Install library
   ```sh
   pip install getman
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->

## Usage

GetMan is designed to be simple and intuitive to use. Below are some examples of how you can use GetMan to test and
explore APIs._

### Making a Simple GET Request

```python
from getman import GetMan
from getman.constant import HttpMethod
from getman.manager.dict import ParamManager

url = "https://example.com"
version = "your-version"  # Optional
client = GetMan(baseURL=url, version=version)
client.add_cookie("sessionid", "RANDOM SESSION ID")

params = ParamManager()
params["category"] = "tools"

route = client.routes("product")
response = client.perform_request(method=HttpMethod.GET, routes=route, params=params.data)

client.get_report(response)
```

### Making a POST Request with JSON Body

```python
from getman import GetMan
from getman.constant import HttpMethod
from getman.manager.dict import DictManager

url = "https://example.com"
version = "your-version"  # Optional
client = GetMan(baseURL=url, version=version)
client.add_cookie("sessionid", "RANDOM SESSION ID")

body = DictManager()
body["product_name"] = "getman"

route = client.routes("product")
response = client.perform_request(method=HttpMethod.POST, routes=route, body=body.data)

client.get_report(response)
```

### Making a Queue Request or simulate concurrent requests

```python

from getman import GetMan
from getman.constant import HttpMethod
from getman.manager.dict import DictManager

url = "https://example.com"

client = GetMan(baseURL=url)

body = DictManager()
body["product_name"] = "getman"

route = client.routes("product")
total_request = 100
for i in range(total_request):
	await client.perform_request(method=HttpMethod.POST, routes=route, body=body.data, queue=True)

client.execute_queue()  # Execute all queued requests concurrently
```

For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->

## Roadmap

- [x] Support Mock Server
- [ ] Generate Report such as PDF, HTML, etc
- [ ] Add Security scan
- [ ] Add stress testing

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (
and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also
simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites
to kick things off!

* [Python Official](https://www.python.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge

[forks-url]: https://github.com/vnpnh/GetMan/network/members

[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge

[stars-url]: https://github.com/vnpnh/GetMan/stargazers

[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge

[issues-url]: https://github.com/vnpnh/GetMan/issues

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge

[license-url]: https://github.com/vnpnh/GetMan/blob/master/LICENSE

[product-screenshot]: images/screenshot.png

[Python]:    https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white

[Python-url]: https://www.python.org/
