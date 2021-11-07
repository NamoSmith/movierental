import unittest
from rental import Rental
from movie import Movie, PriceCode


class RentalTest(unittest.TestCase):
	
	def setUp(self):
		self.new_movie = Movie("Mulan", PriceCode.new_release)
		self.regular_movie = Movie("CitizenFour", PriceCode.regular)
		self.children_movie = Movie("Frozen", PriceCode.childrens)

	def test_movie_attributes(self):
		"""trivial test to catch refactoring errors or change in API of Movie"""
		m = Movie("CitizenFour", PriceCode.regular)
		self.assertEqual("CitizenFour", m.get_title())
		self.assertEqual(PriceCode.regular, m.get_price_code())

	def test_rental_price(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_price(), 3.0)
		rental = Rental(self.new_movie, 5)
		self.assertEqual(rental.get_price(), 15.0)
		rental = Rental(self.regular_movie, 9)
		self.assertEqual(rental.get_price(), 12.5)
		rental = Rental(self.children_movie, 20)
		self.assertEqual(rental.get_price(), 27.0)

	def test_rental_point(self):
		rental = Rental(self.new_movie, 1)
		self.assertEqual(rental.get_point(), 1)
		rental = Rental(self.regular_movie, 6)
		self.assertEqual(rental.get_point(), 1)
		rental = Rental(self.children_movie, 12)
		self.assertEqual(rental.get_point(), 1)