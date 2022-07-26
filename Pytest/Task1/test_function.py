from function import square
# Napisać cztery testy z dla funckji square dla 0, 1, -1 i 100
def test_1():
    assert square(0) == 0
def test_2():
    assert square(1) == 1
def test_3():
    assert square(-1) == 1
def test_4():
    assert square(100) == 10000