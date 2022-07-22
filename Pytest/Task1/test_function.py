from function import square

# Napisać cztery testy z dla funckji square dla 0, 1, -1 i 100

def test_one():
    assert square(0) == 0 ** 2

def test_two():
    assert square(1) == 1 ** 2

def test_three():
    assert square(-1) == (-1) ** 2 

def test_four():
    assert square(100) == 100 ** 2