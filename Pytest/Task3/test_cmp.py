from cmplex import C

# Napisać testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku
def test_A():
    assert (C(0, 0) == C(0, 0)) == True

def test_B():
    assert (C(-5, 4) == C(-5, 4)) == True

def test_C():
    assert (C(-67, 23) == C(67, 23)) == False

def test_D():
    assert (C(342, 349) == C(38, 993)) == False