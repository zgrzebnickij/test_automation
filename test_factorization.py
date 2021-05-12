
def test_import_function():
    try:
        from factorization import prime_factors
        assert callable(prime_factors), "prime_factors not callable" 
    except ImportError as error: 
        assert False, error