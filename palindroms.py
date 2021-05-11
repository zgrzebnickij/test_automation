import re
import pytest

# run with pytest

def is_palindrome(data):
    if not data or type(data) not in [str, list, int, float]:
        raise ValueError
    if type(data) in [int, float]:
        data = str(data)
    if type(data) == str:
        s = re.sub(r'[^\w]','',data)
        if s.lower() == s[::-1].lower():
            return True
    elif type(data) == list:
        s = data
        if s == s[::-1]:
            return True
    return False

def test_palindrome_good():
    cases_good = [ 
    'Do geese see God.',
    'Devil lived',
    'Race fast, safe car',
    'Was it a cat I saw',
    'Able was I ere I saw Elba',
    'Rats live on no evil star',
    'A man a plan a Canal Panama',
    [1, 'a', 'b', 'a', 1],
    1234321,
    1.234321,
    12.21,
    ]
    for case in cases_good:
        result = is_palindrome(case)
        assert result == True, f"Value was {result}, should be True"


def test_palindrome_bad():
    cases_bad = [ 
    'sdf sfdsf',
    'this is not palindrome',
    123333,
    12.56,
    [1, 3, 'h']
    ]
    for case in cases_bad:
        result = is_palindrome(case)
        assert result == False, f"Value was {result}, should be False"


def test_palindrome_bad_input():
    cases_bad = [ 
    '',
    {1:2, 'a':4},
    None,
    ]
    for case in cases_bad:
        pytest.raises(ValueError, is_palindrome, case)

