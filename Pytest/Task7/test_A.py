from random import randint
from function import quicker_sort
import pytest
from function import list2tab
from function import tab2list

class TestEdge:
    @pytest.mark.parametrize("tab", [[1], [1, 2], [2, 1], [x for x in range(100)], [], [randint(-10, 10) for _ in range(30)], [1, 1, 1, 1, 1]])
    def test(self, tab):
        # p = tab2list(tab)
        assert list2tab(quicker_sort(tab2list(tab))) == sorted(tab)
        

class TestSmallest:
    @pytest.mark.parametrize("tab", [[randint(-50, 50) for _ in range(100)] for _ in range(10)])
    def test(self, tab):
        assert list2tab(quicker_sort(tab2list(tab))) == sorted(tab)
        
class TestSmall:
    @pytest.mark.parametrize("tab", [[randint(-50, 50) for _ in range(1000)] for _ in range(10)])
    def test(self, tab):
        assert list2tab(quicker_sort(tab2list(tab))) == sorted(tab)

class TestMid:
    @pytest.mark.parametrize("tab", [[randint(0, 1000) for _ in range(10000)] for _ in range(10)])
    def test(self, tab):
        assert list2tab(quicker_sort(tab2list(tab))) == sorted(tab)
        
class TestMid2:
    @pytest.mark.parametrize("tab", [[randint(0, 10000) for _ in range(10000)] for _ in range(10)])
    def test(self, tab):
        assert list2tab(quicker_sort(tab2list(tab))) == sorted(tab)
        
class TestBig:
    @pytest.mark.parametrize("tab", [[randint(0, 1000) for _ in range(100000)] for _ in range(10)])
    def test(self, tab):
        assert list2tab(quicker_sort(tab2list(tab))) == sorted(tab)
        
class TestBig2:
    @pytest.mark.parametrize("tab", [[randint(0, 1000000) for _ in range(100000)] for _ in range(10)])
    def test(self, tab):
        assert list2tab(quicker_sort(tab2list(tab))) == sorted(tab)