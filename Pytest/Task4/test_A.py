from function import square
from random import randint


# Napisać 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie


class Mini:

    def mini1(self):
        num = randint(-10, 10)
        assert square(num) == num * num 

    def mini2(self):
        num = randint(-10, 10)
        assert square(num) == num * num

    def mini3(self):
        num = randint(-10, 10)
        assert square(num) == num * num 

    def mini4(self):
        num = randint(-10, 10)
        assert square(num) == num * num  


class Medium:

    def medium1(self):
        num = randint(-1000, 1000)
        assert square(num) == num * num 

    def medium2(self):
        num = randint(-1000, 1000)
        assert square(num) == num * num

    def medium3(self):
        num = randint(-1000, 1000)
        assert square(num) == num * num 

    def medium4(self):
        num = randint(-1000, 1000)
        assert square(num) == num * num  

class High:

    def high1(self):
        num = randint(10**4, 10**6)
        assert square(num) == num * num 

    def high2(self):
        num = randint(10**4, 10**6)
        assert square(num) == num * num

    def high3(self):
        num = randint(10**4, 10**6)
        assert square(num) == num * num 

    def high4(self):
        num = randint(10**4, 10**6)
        assert square(num) == num * num    

#@pytest.mark.skipif(High == False)

class Boss:

    def boss1(self):
        num = randint(10**12, 10**13)
        assert square(num) == num * num 

    def boss2(self):
        num = randint(10**12, 10**13)
        assert square(num) == num * num

    def boss3(self):
        num = randint(10**12, 10**13)
        assert square(num) == num * num 

    def boss4(self):
        num = randint(10**12, 10**13)
        assert square(num) == num * num 