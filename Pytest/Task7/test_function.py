# Drugi zawiera testy sprawdzającymi czy zadana linked-list'a jest posortowana,
# zastanowić się nad sposobem generowania testów oraz sposobu grupowania ich w klasy

import pytest
from function import merge_sort, tab_to_list, list_to_tab
from random import randint


class TestMini:
    tests = [[3, 1, 2], [1], [], [2, 3], [6, 6, 6, 6], [randint(-10, -1)for _ in range(10)], [randint(-10, 10)for _ in range(20)], [i for i in range(50)], [randint(-100, 100) for _ in range(100)]]

    @pytest.mark.parametrize("tab", tests)
    def test(self, tab):
        assert list_to_tab(merge_sort(tab_to_list(tab))) == sorted(tab)


class TestMidi:
    tests = [[randint(100, 1000) for _ in range(1000)] for _ in range(5)]

    @pytest.mark.parametrize("tab", tests)
    def test(self, tab):
        assert list_to_tab(merge_sort(tab_to_list(tab))) == sorted(tab)


class TestMaxi:
    tests = [[randint(1000, 1000000) for _ in range(10**4)] for _ in range(5)]

    @pytest.mark.parametrize("tab", tests)
    def test(self, tab):
        assert list_to_tab(merge_sort(tab_to_list(tab))) == sorted(tab)


class TestHudge:
    tests = [[randint(0, 100000) for _ in range(10**6)] for _ in range(5)]

    @pytest.mark.parametrize("tab", tests)
    def test(self, tab):
        assert list_to_tab(merge_sort(tab_to_list(tab))) == sorted(tab)


