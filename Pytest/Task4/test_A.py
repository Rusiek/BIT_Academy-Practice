import pytest
from function import square

# Napisać 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie

class MyTestCase():
    skip_all = False

class Test_1:
    def test(self):
        assert square(-9) == 81
        assert square(-2) == 4
        assert square(0) == 0
        assert square(5) == 25
            
@pytest.mark.skipif(MyTestCase.skip_all, reason="Blad w wykonaniu testu 1")

class Test_2:
    def test(self):
        assert square(-90) == 8100
        assert square(-221) == 48841
        assert square(345) == 119025
        assert square(999) == 998001

@pytest.mark.skipif(MyTestCase.skip_all, reason="Blad w wykonaniu testu 2")

class Test_3:
    def test(self):
        assert square(20000) == 400000000
        assert square(543221) == 295089054841
        assert square(843445) == 711399468025
        assert square(953400) == 908971560000
            
MyTestCase.skip_all = True
@pytest.mark.skipif(MyTestCase.skip_all, reason="Blad w wykonaniu testu 3")

class Test_4:
    def test(self):
        assert square(2053540007654) == 2053540007654 * 2053540007654
        assert square(5437978988221) == 5437978988221 * 5437978988221
        assert square(8434278655545) == 8434278655545 * 8434278655545
        assert square(9537864036570) == 9537864036570 * 9537864036570