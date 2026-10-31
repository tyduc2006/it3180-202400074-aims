import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED


class TestCart(unittest.TestCase):

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
