import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED


class TestCart(unittest.TestCase):
    def test_sort_by_title(self):
        cart = Cart()

        dvd1 = type("DVD", (), {"title": "Star Wars", "cost": 20})()
        dvd2 = type("DVD", (), {"title": "Aladdin", "cost": 10})()
        dvd3 = type("DVD", (), {"title": "The Lion King", "cost": 30})()

        cart.items = [dvd1, dvd2, dvd3]
        cart.sort_by_title()

        self.assertEqual(
            [dvd.title for dvd in cart.items],
            ["Aladdin", "Star Wars", "The Lion King"]
        )

    def test_sort_by_cost(self):
        cart = Cart()

        dvd1 = type("DVD", (), {"title": "Star Wars", "cost": 20})()
        dvd2 = type("DVD", (), {"title": "Aladdin", "cost": 10})()
        dvd3 = type("DVD", (), {"title": "The Lion King", "cost": 30})()

        cart.items = [dvd1, dvd2, dvd3]
        cart.sort_by_cost()

        self.assertEqual(
            [dvd.cost for dvd in cart.items],
            [10, 20, 30]
        )
            
    def test_add_dvd_until_full(self):
        cart = Cart()

        # Thêm đủ 20 DVD
        for i in range(MAX_NUMBERS_ORDERED):
            dvd = type("DVD", (), {"title": f"DVD {i + 1}", "cost": 10})()
            result = cart.add_dvd(dvd)

            self.assertTrue(result)

        # Thử thêm DVD thứ 21
        dvd_21 = type("DVD", (), {"title": "DVD 21", "cost": 10})()
        result = cart.add_dvd(dvd_21)

        self.assertFalse(result)

        # Đảm bảo giỏ hàng vẫn chỉ có 20 DVD
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)


if __name__ == "__main__":
    unittest.main()
