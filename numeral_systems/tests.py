import unittest
from unittest import result
from .numeralSystems import roman_to_decimal

class test_roman_to_decimal(unittest.TestCase):
    # I do MMMCMXCIX (1 do 3999 dziesiętnie)

    def test_import(self):
        try: 
            from .numeralSystems import roman_to_decimal
            assert callable(roman_to_decimal), "prime_factors not callable" 
        except ImportError as error: 
            assert False, error

    def test_few_first_number(self):
        for roman, decimal in (('I', 1),('III', 3)):
            result =  roman_to_decimal(roman)
            assert result == decimal, f'Fail roman_to_decimal for {roman} should be {decimal}, but got {result}'