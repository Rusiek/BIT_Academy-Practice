from cmplex import C
def test_9():
    num=C(1,2).__mul__(C(1,1))
    assert num.x==-1 and num.y==3
def test_10():
    num=C(12,4).__mul__(C(11,2))
    assert num.x==124 and num.y==68
def test_11():
    num=C(-10,-1).__mul__(C(9,6))
    assert num.x==-84 and num.y==-69
def test_12():
    num=C(-1,3).__mul__(C(5,8))
    assert num.x==-29 and num.y==7
# Napisać testy sprawdzające mnożenie liczb zespolonych
# w załączonym pliku