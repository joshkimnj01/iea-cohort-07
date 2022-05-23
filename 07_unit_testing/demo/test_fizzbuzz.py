from fizzbuzz import fizzbuzz

# In module test_fizzbuzz.py
# from fizzbuzz import fizzbuzz
def test_fizzbuzz_three():
    result = fizzbuzz(3)
    assert result == 'fizz'

def test_fizzbuzz_five():
    result = fizzbuzz(5)
    assert result == 'buzz'

def test_fizzbuzz_fifteen():
    result = fizzbuzz(15)
    assert result == 'fizzbuzz'

def test_fizzbuzz_two():
    result = fizzbuzz(2)
    assert result == 2

def test_fizzbuzz_none():
    result = fizzbuzz()
    assert result == "ERROR"

def test_fizzbuzz_str():
    result = fizzbuzz("2")
    assert result == "ERROR"


