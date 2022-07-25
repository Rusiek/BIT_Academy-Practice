from sort_linked_list import MergeSort
from sort_linked_list import tab_to_linked_list
from sort_linked_list import linked_list_to_tab
import pytest
from random import randint


class Boundary_Conditions:
    @pytest.mark.parametrize("tab", [[], [1], [1, 2], [1, 1, 1]])
    def test(self, tab):
        assert linked_list_to_tab(MergeSort(tab_to_linked_list(tab))) == sorted(tab)


class TestsMini:
    @pytest.mark.parametrize("tab", [ [randint(-10, 10) for _ in range (5)], [randint(-10, 10) for _ in range (10)],
    [randint(-100, 100) for _ in range (5)], [randint(-100, 100) for _ in range (10)] ])

    def test_mini(self, tab):
        assert linked_list_to_tab(MergeSort(tab_to_linked_list(tab))) == sorted(tab)


class TestMid:
    @pytest.mark.parametrize("tab", [ [randint(-1000, 1000) for _ in range (100)] for _ in range (5) ])

    def test_mid(self, tab):
        assert linked_list_to_tab(MergeSort(tab_to_linked_list(tab))) == sorted(tab)


class TestMaxi:
    @pytest.mark.parametrize("tab", [ [randint(10, 10**10) for _ in range (10**4)] for _ in range (5) ])

    def test_maxi(self, tab):
        assert linked_list_to_tab(MergeSort(tab_to_linked_list(tab))) == sorted(tab)


class TestBoss:
    @pytest.mark.parametrize("tab", [ [randint(1, 10**14) for _ in range (10**6)] for _ in range (5) ])

    def test_boss(self, tab):
        assert linked_list_to_tab(MergeSort(tab_to_linked_list(tab))) == sorted(tab)