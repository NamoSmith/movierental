from rental import *


class Movie:
    """A movie available for rent."""

    def __init__(self, title, price_code: PriceCode):
        self.title = title
        self.price_code = price_code

    def get_price_code(self):
        return self.price_code

    def get_title(self):
        return self.title

    def __str__(self):
        return self.title
