#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions


from src.question_a.question_a import test_config
from src.question_a.question_a import get_fahrenheit
from src.question_b.question_b import get_miles_per_hour
from src.question_c.question_c import use_local_variable
from src.question_d.question_d import is_prime



class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_fahrenheit(self):
        self.assertEqual(32.0, get_fahrenheit(0))
        self.assertEqual(41.0, get_fahrenheit(5))
        self.assertEqual(50.0, get_fahrenheit(10))

    def test_get_miles_per_hour(self):
        self.assertEqual(19.883872, get_miles_per_hour(32, 60))

    def test_get_local_variable(self):
        num = 100
        use_local_variable(num)
        self.assertEqual(100, num)


    def test_is_prime(self):
        self.assertEqual(False, is_prime(4))
        self.assertEqual(True, is_prime(5))
        self.assertEqual(True, is_prime(11))


        
        



    