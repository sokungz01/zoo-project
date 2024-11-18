import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_get_ticket_price_age_0(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)

    def test_get_ticket_price_age_12(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)

    def test_get_ticket_price_age_20(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)

    def test_get_ticket_price_age_21(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    
    def test_get_ticket_price_age_61(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)


if __name__ == '__main__':
    unittest.main()