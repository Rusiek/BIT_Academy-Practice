from cmplex import C

# Napisać testy sprawdzające porównywanie liczb zespolonych
# w załączonym pliku

class Test:
    def test_mini(self):
        assert C(0,0).__eq__(C(1,1)) == False
        assert C(-1,-2).__eq__(C(-3,-4)) == False
        assert C(0,0).__eq__(C(0,0)) == True
    def test_mid(self):
        assert C(45,67).__eq__(C(-23,98)) == False
        assert C(893,-1933).__eq__(C(893,-1933)) == True
    def test_max(self):
        assert C(91823434,1243344).__eq__(C(91823434,1243344)) == True