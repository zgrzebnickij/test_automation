import unittest
from unittest import result
from .numeralSystems import roman_to_decimal, decimal_to_roman

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

    def test_first_numbers(self):
        for roman, decimal in (('V', 5),('IV', 4), ('VIII', 8)):
            result =  roman_to_decimal(roman)
            assert result == decimal, f'Fail roman_to_decimal for {roman} should be {decimal}, but got {result}'

    def test_to_100_numbers(self):
        for roman, decimal in (('X', 10),('IX', 9), ('XVIII', 18), ('XXXV', 35), ('XCIX', 99)):
            result =  roman_to_decimal(roman)
            assert result == decimal, f'Fail roman_to_decimal for {roman} should be {decimal}, but got {result}'

    def test_to_1000_numbers(self):
        for roman, decimal in (('CXLVII', 147),('CCCXIII', 313), ('CLXXXV', 185), ('DLXXXV', 585), ('DCCLIV', 754)):
            result =  roman_to_decimal(roman)
            assert result == decimal, f'Fail roman_to_decimal for {roman} should be {decimal}, but got {result}'

    def test_invalid_types(self):
        'Test wrong types of input'
        for invalid in ('', 234, True):
            try:
                result =  roman_to_decimal(invalid)
                assert False, 'Should return Value error'
            except ValueError as error: 
                pass
            except Exception as error:
                assert False, f'Wrong error expected ValueError, but got {error}'

    def test_wrong_character(self):
        'Test wrong types of input'
        for invalid in ('ASD', 'LPTH', 'LB'):
            try:
                result =  roman_to_decimal(invalid)
                assert False, 'Should return Value error'
            except ValueError as error: 
                pass

    def test_incorect_order(self):
        # I can only be placed before V and X.
        # X can only be placed before L and C.
        # C can only be placed before D and M.
        tests = ['ID', 'IC', 'IM', 'IL', 'XD', 'XM']
        for invalid in tests:
            try:
                result =  roman_to_decimal(invalid)
                assert False, f'Should return Value error, but got {result} for {invalid}'
            except ValueError as error: 
                pass

    def test_incorect_order_2(self):
        # Numerals must be arranged in descending order of size.
        # M, C, and X cannot be equalled or exceeded by smaller denominations.
        # D, L, and V can each only appear once.
        tests = ['IM', 'XM', 'IXX', 'DD', 'LL', 'VV', 'MVVII']
        for invalid in tests:
            try:
                result =  roman_to_decimal(invalid)
                assert False, f'Should return Value error, but got {result} for {invalid}'
            except ValueError as error: 
                pass

class test_decimal_to_roman(unittest.TestCase):
    # I do MMMCMXCIX (1 do 3999 dziesiętnie)

    def test_import(self):
        try: 
            from .numeralSystems import decimal_to_roman
            assert callable(roman_to_decimal), "prime_factors not callable" 
        except ImportError as error: 
            assert False, error

    def test_first_numbers(self):
        for roman, decimal in (('V', 5),('IV', 4), ('VIII', 8)):
            result =  decimal_to_roman(decimal)
            assert result == roman, f'Fail roman_to_decimal for {decimal} should be {roman}, but got {result}'