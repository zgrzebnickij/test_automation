# I do MMMCMXCIX (1 do 3999 dziesiętnie)

import unittest

class test_roman_to_decimal(unittest.TestCase):

    def test_import(self):
        try: 
            from numeralSystems import roman_to_decimal
            assert callable(roman_to_decimal), "prime_factors not callable" 
        except ImportError as error: 
            assert False, error