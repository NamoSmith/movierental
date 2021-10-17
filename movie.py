from enum import Enum


class PriceCode(Enum):
    """An enumeration for different types of movies."""
    new_release = {
        "price": lambda days: 3.0 * days,
        "renter_point": lambda days: days
    }
    regular = {
        "price": lambda days: 2 if days <= 2 else 2 + (1.5 * (days - 2)),
        "renter_point": lambda days: 1
    }
    children = {
        "price": lambda days: 1.5 if days <= 3 else 1.5 + (1.5 * (days - 3)),
        "renter_point": lambda days: 1
    }

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days"""
        pricing = self.value["price"]
        return pricing(days)

    def renter_point(self, days: int) -> int:
        """Return the renter point for a given number of days."""
        point = self.value["renter_point"]
        return point(days)


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
