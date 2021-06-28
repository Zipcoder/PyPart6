import unittest
import temperature_utils_v2

class Test_Temp_Utils_2(unittest.TestCase):
    
    def test_convert_to_c_from_k(self):
        
        result = temperature_utils_v2.convert_to_celsius_from_kelvin(0)
        self.assertEqual(result, -273)
    
    def test_convert_to_c_from_f(self):
        
        result = temperature_utils_v2.convert_to_celsius_from_fahrenheit(0)
        self.assertAlmostEqual
        