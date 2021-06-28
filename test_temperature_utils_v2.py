import unittest
import temperature_utils_v2

class Test_Temp_Utils_2(unittest.TestCase):
    
    def test_convert_to_c_from_k(self):
        
        result = temperature_utils_v2.convert_to_celsius_from_kelvin(0)
        self.assertAlmostEqual(result, -273.15)
    
    def test_convert_to_c_from_f(self):
        
        result = temperature_utils_v2.convert_to_celsius_from_fahrenheit(0)
        self.assertAlmostEqual(result, -17.78)

    def test_convert_to_k_from_f(self):
        
        result = temperature_utils_v2.convert_to_kelvin_from_fahrenheit(32)
        self.assertAlmostEqual(result, 273.15)

    def test_convert_to_k_from_c(self):
        
        result = temperature_utils_v2.convert_to_kelvin_from_celsius(32)
        self.assertAlmostEqual(result, 305.15)
        
    def test_convert_to_f_from_c(self):
        result = temperature_utils_v2.convert_to_fahrenheit_from_celsius(15)
        self.assertAlmostEqual(result, 59)

    def test_convert_to_f_from_k(self):
        result = temperature_utils_v2.convert_to_fahrenheit_from_kelvin(57)
        self.assertAlmostEqual(result, -357.07)

    def test_check_tuples_f_to_c(self):
        tempInput = (0, 32, 100, 57)
        result = temperature_utils_v2.temperature_tuple(tempInput, 'c', 'f')
        self.assertEqual(result, ((0, 32.0), (32, 89.6), (100, 212), (57, 134.6)))

    def test_check_tuples_c_to_k(self):
        tempInput = (0, 32, 100, 57)
        result = temperature_utils_v2.temperature_tuple(tempInput, 'c', 'k')
        self.assertEqual(result, ((0, 273.15), (32, 305.15), (100, 373.15), (57, 330.15)))

    