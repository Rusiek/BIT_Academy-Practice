from cmplex import C

# Napisać testy sprawdzające mnożenie liczb zespolonych
# w załączonym pliku

class Test:
    def test_mini(self):
        assert C(0,0).__mul__(C(1,1)) == C(0,0)
        assert C(-1,-2).__mul__(C(-3,-4)) == C(-5,10)
        assert C(0,0).__mul__(C(0,0)) == C(0,0)
        
    def test_mid(self):
        assert C(45,67).__mul__(C(-23,98)) == C(-7601,2869)
        assert C(893,-1933).__mul__(C(0,2999)) == C(5797067,2678107)
        
    def test_max(self):
        assert C(91823434,1243344).__mul__(C(541313435,90710973)) == C(49592473528022078,9002431853867922)
