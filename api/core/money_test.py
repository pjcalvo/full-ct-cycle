import unittest
import random
import string
from core import money

class TestHelper():
   def randomString(self, stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

class MoneyTest(unittest.TestCase):
   def test_format_int(self):
        expected_value = "2.00"
        test_value = 2
        self.assertEqual(money.formatMoney(test_value),expected_value)
   
   def test_format_float(self):
        expected_value = "2.12"
        test_value = 2.12312
        self.assertEqual(money.formatMoney(test_value),expected_value)

   def test_format_string(self):
        expected_value = "12 878 712.12"
        test_value = "12878712.12312"
        self.assertEqual(money.formatMoney(test_value),expected_value)
   
   def test_format_random_string_with_alpha(self):
        test_random = TestHelper.randomString(self)
        self.assertEqual(money.formatMoney(test_random),"")

   def test_format_with_boundaries(self):
        tests = [(-1123.222,"-1 123.22"),(-1,"-1.00"),(0,"0.00"),(99999.99999,"100 000.00")]
        for test, expected in tests:
             self.assertEqual(money.formatMoney(test),expected)
