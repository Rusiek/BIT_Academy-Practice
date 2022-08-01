from cmplex import C
def test_13():
    val=C(1,2).__sub__(C(1,2))
    assert val.x==0 and val.y==0
def test_14():
    val=C(11,-2).__sub__(C(10,2))
    assert val.x==1 and val.y==-4
def test_15():
    val=C(1245,-124).__sub__(C(45,1))
    assert val.x==1200 and val.y==-125
def test_16():
    val=C(-9213,8235).__sub__(C(77,-55))
    assert val.x==-9290 and val.y==8290
# Napisać testy sprawdzające odejmowanie liczb zespolonych
# w załączonym pliku