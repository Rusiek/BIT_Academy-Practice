from cmplex import C
def test_5():
    num=C(1,2).__eq__(C(1,2))
    assert num==True
def test_6():
    num=C(1,3).__eq__(C(1,2))
    assert num==False
def test_7():
    num=C(1231,2228).__eq__(C(1231,2228))
    assert num==True
def test_8():
    num=C(14654,290823).__eq__(C(12432,3642))
    assert num==False
# Napisać testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku