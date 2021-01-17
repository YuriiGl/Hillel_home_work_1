import unittest
from lesson_17 import lesson_6_1
from lesson_17 import lesson_7_2
from lesson_17 import lesson_11_2
from lesson_17 import lesson_15_16_2

class AllTests(unittest.TestCase):
    def test_dict(self):
        self.assertEqual(lesson_6_1.new_dict(('Bitcoin', 'Ether', 'Ripple', 'Litecoin'), ('BTC', 'ETH', 'XRP', 'LTC')),
                         {'Bitcoin': 'BTC', 'Ether': 'ETH', 'Ripple': 'XRP', 'Litecoin': 'LTC'})

    def test_temperature_calc(self):
        self.assertEqual(lesson_7_2.temperature('C', 0), (0.0, 273.15, 32.0))
        self.assertEqual(lesson_7_2.temperature('K', 0), (-273.15, 0, -459.67))
        self.assertEqual(lesson_7_2.temperature('F', 0), (-57.6, 255.37222222222223, 0))
    def test_email(self):
        self.assertEqual(lesson_11_2.hide_email('somebody_email@gmail.com'), 'somebody_em***@**il@gmail.com')
    def test_num_phone(self):
        self.assertEqual(lesson_15_16_2.)

if __name__ == '__main__':
    unittest.main()
