from functools import wraps

def validate_input(function):
    @wraps(function)
    def wrapper(number):
        if type(number) != int:
            raise ValueError('Input type not allowed, only integer')
        if number < 2:
            raise ValueError('Only numbers bigger than 1')
        return function(number)
    return wrapper

@validate_input
def prime_factors(number: int) -> list:
    i = 2
    factors = []
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return list(set(factors))