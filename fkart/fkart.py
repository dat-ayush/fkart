from .utils import request_url
from .utils import extract_price_from_html


class Fkart:
    def __init__(self, product_url):
        self.product_url = product_url

    def fetch_html(self, user_agent=None):
        response = request_url(self.product_url, user_agent)
        return response.text

    def fetch_price(self, user_agent=None):
        product_price = extract_price_from_html(
            html_content=self.fetch_html(user_agent)
        )
        return product_price
