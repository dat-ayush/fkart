import requests
import requests.exceptions
from bs4 import BeautifulSoup

from .logger import Logger

# import request constants
from .consts import (
    request_headers,
    request_data,
    price_identifier,
    default_userAgent,
    request_cookies
)


def request_url(url, proxy=None, log_filename=None, user_agent=default_userAgent):
    session = requests.session()
    request_headers["User-Agent"] = user_agent
    try:
        request_args = {
            "headers": request_headers,
            "data": request_data,
            "cookies": request_cookies
        }
        if proxy:
            request_args["proxies"] = {"http": proxy, "https": proxy}

        response = session.get(url, **request_args)
        response.raise_for_status()
        return response

    except requests.exceptions.HTTPError:
        Logger.requests_error(exception=f"Invalid status code: {response.status_code}. "
                                        "HTTP Error")
    except requests.exceptions.ProxyError:
        Logger.requests_error(exception="Proxy Error", log_filename=log_filename)
    except requests.exceptions.ConnectionError:
        Logger.requests_error(exception="Network Error", log_filename=log_filename)
    except requests.exceptions.Timeout:
        Logger.requests_error(exception="Timeout Error", log_filename=log_filename)


def extract_price_from_html(html_content):
    soup = BeautifulSoup(html_content, "lxml")
    try:
        return soup.find(price_identifier.get("tag"),
                         class_=price_identifier.get("class")).text
    except AttributeError:
        Logger.bs4_error("Attribute Error")
