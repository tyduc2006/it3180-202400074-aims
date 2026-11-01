import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_name


class TestSearchByName(unittest.TestCase):

    def test_search_by_name_case_insensitive(self):
        cart = Cart()
        dvd = DigitalVideoDisc("The Lion King")
        cart.items.append(dvd)

        result = search_by_name(cart, "lion")

        self.assertEqual(result, [dvd])


if __name__ == "__main__":
    unittest.main()
