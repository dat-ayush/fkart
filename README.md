# usage

```python3
from fkart import Fkart

product_url = "https://www.flipkart.com/web-application-hacker-s-handbook/p/itmfbj6x6myfgzrk"
product_price = Fkart(product_url).fetch_price()
print(product_price)
```

Note: For updating with latest working identifiers and request parameters. See `const.py`
