from factorization import prime_factors
import pytest

def test_import_function():
    try:
        from factorization import prime_factors
        assert callable(prime_factors), "prime_factors not callable" 
    except ImportError as error: 
        assert False, error

def test_first_10_numbers():
    cases = {
        2: [2],
        3: [3],
        4: [2],
        5: [5],
        6: [2,3],
        7: [7],
        8: [2],
        9: [3],
        10: [2, 5],
    }
    for case, should_return in cases.items():
        result = prime_factors(case)
        assert result == should_return, f'prime_factors for {case} should return {should_return}, but get {result}'

def test_0_and_1():
    for number in [0,1]:
        pytest.raises(ValueError, prime_factors, number)

def test_illegal_input():
    for case in [None, '', False, 1.324, -3, '123']:
        pytest.raises(ValueError, prime_factors, case)