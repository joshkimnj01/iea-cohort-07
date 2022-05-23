def fizzbuzz(num=None):
    """Returns 'fizz' for multiples of 3,
       'buzz' for multiples of 5,
       'fizzbuzz' for multiples of both,
       or returns the number passed."""
    result = ''
    try:
        if num % 3 == 0:
            result += 'fizz'
        if num % 5 == 0:
            result += 'buzz'
        result = result or num
    except TypeError:
        result = 'ERROR'

    return result

