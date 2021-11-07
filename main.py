"""A demonstrate of the movie rental code."""

from movie import Movie
from rental import Rental
from customer import Customer


def make_movies():
    movies = [
        Movie("The Irishman", "2019", ["Mafia", "Drama", "Epic"]),
        Movie("CitizenFour", "2014", ["Documentary", "Historical Documentary"]),
        Movie("Frozen", "2013", ["Adventure", "Children", "Cartoon","Musical", "Comedy", "Fantasy"]),
        Movie("El Camino", "2019", ["Western", "Drama", "Crime"]),
        Movie("Particle Fever", "2013", ["Documentary", "Science fiction"]),
    ]
    return movies


if __name__ == '__main__':
    # Create a customer with some rentals

    customer = Customer("Edward Snowden")
    days = 1
    for movie in make_movies():
        customer.add_rental(Rental(movie, days))
        days += 1
    print(customer.statement())
