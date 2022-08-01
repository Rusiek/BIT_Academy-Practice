from cmplex import C

def test_1():
    val=C(2,4).__add__(C(1,2))
    assert val.x==3 and val.y==6
def test_2():
    val=C(90,0).__add__(C(1,0))
    assert val.x==91 and val.y==0
def test_3():
    val=C(-11,25).__add__(C(34,-2543525))
    assert val.x==23 and val.y==-2543500
def test_4():
    val=C(5,20).__add__(C(-24,40))
    assert val.x==-19 and val.y==60

# Napisać testy sprawdzające dodawanie liczb zespolonych
# w załączonym pliku