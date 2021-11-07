"""A movie computing program."""

from typing import List, Union
import csv


class Movie:
    """A movie available for rent."""

    def __init__(self, title: str, year: str, genre):
        # Initialize a new movie.

        self.title = title
        self.year = year
        self.genre: List[str] = genre

    def get_title(self) -> str:
        return self.title

    def get_year(self) -> str:
        return self.year

    def get_genre(self) -> List[str]:
        return self.genre

    def is_genre(self, movie: str) -> bool:
        """Returns true if the string parameter matches one of the movie’s genre."""

        return movie in self.genre

    def __str__(self) -> str:
        return self.title


class MovieCatalog:
    """A movie catalog computing."""

    def __init__(self):
        self.movies_list = {}
        self.read_data()

    def read_data(self):
        movies = open("movies.csv", "r")
        read_file = csv.reader(movies)
        header = next(read_file)
        for i in read_file:
            self.movies_list[i[1]] = Movie(i[1], i[2], i[3].split("|"))

    def get_movie(self, title: str) -> Union[str, None]:
        try:
            return self.movies_list[title]
        except KeyError:
            self.read_data()
