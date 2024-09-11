import requests
import requests.exceptions
from bs4 import BeautifulSoup

from .logger import Logger
from .consts import headers, data, price_html_identifier


def request_url(url, proxy=None, log_filename=None,
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                           "Chrome/127.0.6533.100 Safari/537.36"):
    try:
        headers["User-Agent"] = user_agent
        if proxy:
            return requests.get(url, headers=headers, data=data, proxies={"http": proxy, "https": proxy})
        else:
            return requests.get(url, headers=headers, data=data)
    except requests.exceptions.ProxyError:
        Logger.requests_error(exception="Proxy Error", log_filename=log_filename)
    except requests.exceptions.ConnectionError:
        Logger.requests_error(exception="Network Error", log_filename=log_filename)
    except requests.exceptions.Timeout:
        Logger.requests_error(exception="Timeout Error", log_filename=log_filename)


def extract_price_from_html(html_content):
    soup = BeautifulSoup(html_content, "lxml")
    price = soup.find(price_html_identifier.get("tag"),
                      class_=price_html_identifier.get("class")).text
    return price
