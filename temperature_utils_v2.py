from typing import Iterable, Tuple


def convert_to_kelvin_from_celsius(celsius):

    return celsius + 273.15

def convert_to_fahrenheit_from_celsius(celsius):

    return round((celsius * (9 / 5) + 32), 2)  

def convert_to_celsius_from_kelvin(kelvin):
    
    return kelvin - 273.15

def convert_to_fahrenheit_from_kelvin(kelvin):
    return round(((9/5) * (kelvin -273.15) + 32), 2)

def convert_to_kelvin_from_fahrenheit(fahrenheit):

    return round(((5/9) * (fahrenheit - 32) + 273.15), 2)

def convert_to_celsius_from_fahrenheit(fahrenheit):

    return round((fahrenheit - 32) * (5/9), 2)

def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str, output_unit_of_measurement) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    temp = ()
    tempChange = ()
    tempAndChange = ()

    if input_unit_of_measurement == 'c' and output_unit_of_measurement == 'k':
        for i in temperatures:
            temp += (i,)
            tempChange += (convert_to_kelvin_from_celsius(i),)
        for pair in zip(temp, tempChange):
            tempAndChange += (pair,)
        return tempAndChange
    elif input_unit_of_measurement == 'c' and output_unit_of_measurement == 'f':
        for i in temperatures:
            temp += (i,)
            tempChange += (convert_to_fahrenheit_from_celsius(i),)
        for pair in zip(temp, tempChange):
            tempAndChange += (pair,)
        return tempAndChange
    elif input_unit_of_measurement == 'k' and output_unit_of_measurement == 'c':
        for i in temperatures:
            temp += (i,)
            tempChange += (convert_to_celsius_from_kelvin(i),)
        for pair in zip(temp, tempChange):
            tempAndChange += (pair,)
        return tempAndChange
    elif input_unit_of_measurement == 'k' and output_unit_of_measurement == 'f':
        for i in temperatures:
            temp += (i,)
            tempChange += (convert_to_fahrenheit_from_kelvin(i),)
        for pair in zip(temp, tempChange):
            tempAndChange += (pair,)
        return tempAndChange
    elif input_unit_of_measurement == 'f' and output_unit_of_measurement == 'k':
        for i in temperatures:
            temp += (i,)
            tempChange += (convert_to_kelvin_from_fahrenheit(i),)
        for pair in zip(temp, tempChange):
            tempAndChange += (pair,)
        return tempAndChange
    elif input_unit_of_measurement == 'f' and output_unit_of_measurement == 'c':
        for i in temperatures:
            temp += (i,)
            tempChange += (convert_to_celsius_from_fahrenheit(i),)
        for pair in zip(temp, tempChange):
            tempAndChange += (pair,)
        return tempAndChange

print(temperature_tuple((32, 68, 100), 'f', 'c'))
        



        
    

