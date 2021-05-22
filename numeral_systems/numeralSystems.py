from functools import wraps
import re

VALID_ROMAN_PATTERN = re.compile(r'^(?=[MDCLXVI])M*(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[XV]|V?I{0,3})$')

ROMAN_TO_DECIMAL_MAP = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

WHEN_BEFORE = { 
    'I': ('V', 'X'),
    'X': ('L', 'C'),
    'C': ('D', 'M'),
}

# I can only be placed before V and X.
# X can only be placed before L and C.
# C can only be placed before D and M.

# Numerals must be arranged in descending order of size.
# M, C, and X cannot be equalled or exceeded by smaller denominations.
# D, L, and V can each only appear once.

# Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.

def validation_roman(func):
    @wraps(func)
    def inner(*args, **kwargs):
        roman = args[0]
        if type(roman) != str:
            raise ValueError('Expected string')
        if roman == '':
            raise ValueError('String canot be empty')
        # valid_characters = list(ROMAN_TO_DECIMAL_MAP.keys())
        # if any(character not in valid_characters for character in roman):
        #     raise ValueError('Invalid Character')
        # if any(roman.count(char)>1 for char in ('D', 'L', 'V')):
        #     raise ValueError('D, L, and V can each only appear once.')
        if not VALID_ROMAN_PATTERN.match(roman):
            raise ValueError('Not a Roman numeral')
        return func(*args, **kwargs)
    return inner

@validation_roman
def roman_to_decimal(roman):
    before = ''
    result = 0
    for current in reversed(roman):
        print(current, before)
        if before in WHEN_BEFORE.get(current, []):
            result -= ROMAN_TO_DECIMAL_MAP[current]
        elif before == '' or (ROMAN_TO_DECIMAL_MAP[before] <= ROMAN_TO_DECIMAL_MAP[current]):
            result += ROMAN_TO_DECIMAL_MAP[current]
        # else:
        #     raise ValueError('Passed value is not a valid Roman number')
        before = current
    return result


def validate_decimal(func):
    @wraps(func)
    def inner(*args, **kwargs):
        decimal = args[0]
        if type(decimal) != int:
            raise ValueError('Expected decimal')
        if not (0 < decimal <= 4000):
            raise ValueError('Expected decimal from range 1 to 3999')
        return func(*args, **kwargs)
    return inner

@validate_decimal
def decimal_to_roman(decimal):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    result = ''
    for number, symbol in sorted(zip(num, sym), reverse=True):
        div = decimal // number
        decimal %= number

        for _ in range(div):
            result += symbol

    return result