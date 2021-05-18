ROMAN_TO_DECIMAL_MAP = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}



# Numerals must be arranged in descending order of size.
# M, C, and X cannot be equalled or exceeded by smaller denominations.
# D, L, and V can each only appear once.

# Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
WHEN_BEFORE = { 
    'I': ('V', 'X'),
    'X': ('L', 'C'),
    'C': ('D', 'M'),
}
# I can only be placed before V and X.
# X can only be placed before L and C.
# C can only be placed before D and M.


def roman_to_decimal(roman):
    before = ''
    result = 0
    for current in reversed(roman):
        if before in WHEN_BEFORE.get(current, ()):
            result -= ROMAN_TO_DECIMAL_MAP[current]
        else:
            result += ROMAN_TO_DECIMAL_MAP[current]
        before = current
    return result