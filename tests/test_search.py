import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_name


class TestSearchByCategory(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.items = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation")
        ]

    def test_search_existing_category(self):
        result = search_by_category(self.cart, "Animation")
        self.assertEqual(
            [dvd.title for dvd in result],
            ["The Lion King", "Aladdin"]
        )

    def test_search_case_insensitive(self):
        result = search_by_category(self.cart, "animation")
        self.assertEqual(len(result), 2)

    def test_search_non_existing_category(self):
        result = search_by_category(self.cart, "Comedy")
        self.assertEqual(result, [])


class TestSearchByName(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.items = [
            DigitalVideoDisc("The Lion King", "Animation"),
            DigitalVideoDisc("Star Wars", "Science Fiction"),
            DigitalVideoDisc("Aladdin", "Animation")
        ]

    def test_search_existing_name(self):
        result = search_by_name(self.cart, "Lion")
        self.assertEqual(
            [dvd.title for dvd in result],
            ["The Lion King"]
        )

    def test_search_case_insensitive(self):
        result = search_by_name(self.cart, "lion")
        self.assertEqual(
            [dvd.title for dvd in result],
            ["The Lion King"]
        )

    def test_search_non_existing_name(self):
        result = search_by_name(self.cart, "Harry Potter")
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()