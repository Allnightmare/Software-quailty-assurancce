import unittest
import function


class Testfunction(unittest.TestCase):
    def test_maximum(self):
        self.assertEqual(function.maximum(10, 5), 10)

    def test_reverse(self):
        self.assertEqual(function.reverse("abcd"), "dcba")

    def test_areaCircle(self):
        self.assertEqual(function.areaCircle(3), 28.274333882308138)

    def test_circumCircle(self):
        self.assertEqual(function.circumCircle(3), 18.84955592153876)

    def test_prime(self):
        self.assertEqual(function.prime(3), True)




if __name__ == '__main__':
    unittest.main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
