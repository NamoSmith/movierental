from movie import *
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
    childrens = {
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


class Rental:
    """
    A rental of a movie by customer.
    From Fowler's refactoring example.
    A realistic Rental would have fields for the dates
    that the movie was rented and returned, from which the
    rental period is calculated.
    But for simplicity of the example only a days_rented
    field is used.
    """

    def __init__(self, movie: Movie, days_rented):
        """Initialize a new movie rental object for
           a movie with known rental period (daysRented).
        """
        self.movie = movie
        self.days_rented = days_rented

    def get_movie(self):
        return self.movie

    def get_days_rented(self):
        return self.days_rented

    def get_price(self):
        """Compute rental change."""
        return self.movie.get_price_code().price(self.days_rented)

    def get_point(self):
        """Award renter points."""
        return self.movie.get_price_code().renter_point(self.days_rented)
