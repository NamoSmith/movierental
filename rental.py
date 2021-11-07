"""A rental computing program."""

from __future__ import annotations
from enum import Enum
from datetime import datetime
from movie import Movie


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

    def __init__(self, movie: Movie, days_rented: int):
        """Initialize a new movie rental object for
        a movie with known rental period (daysRented).
        """

        self.movie = movie
        self.days_rented = days_rented
        self.price_code = PriceCode.for_movie(movie)

    def get_movie(self) -> Movie:
        return self.movie

    def get_days_rented(self) -> int:
        return self.days_rented

    def get_price(self) -> float:
        return self.price_code.price(self.days_rented)

    def get_renter_point(self, renter_point: float = 0) -> float:
        renter_point += self.price_code.renter_point(self.days_rented)
        return renter_point


class PriceCode(Enum):
    """An enumeration for different types of movies."""

    new_release = {
        "price": lambda days: 3 * days,
        "frp": lambda days: days,
    }
    regular = {
        "price": lambda days: 2.0 if days <= 2 else 2.0 + (1.5 * (days - 2)),
        "frp": lambda days: 1,
    }
    childrens = {
        "price": lambda days: 1.5 if days <= 3 else 1.5 + (1.5 * (days - 3)),
        "frp": lambda days: 1,
    }

    def price(self, days: int) -> float:
        """Return the rental price for a given number of days."""

        pricing = self.value["price"]    # the enum member's price formula
        return pricing(days)

    def renter_point(self, days: int) -> float:
        """Return the renter point for a given number of days."""

        frp = self.value["frp"]
        return frp(days)

    @classmethod
    def for_movie(cls, movie: Movie) -> PriceCode:
        current_year = str(datetime.now().year)
        if movie.get_year() == current_year:
            return cls.new_release
        elif movie.get_genre() == "Children":
            return cls.childrens
        else:
            return cls.regular
