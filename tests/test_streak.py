import pytest
from streak import longest_positive_streak

def test_empty_list():
    assert longest_positive_streak([]) == 0

def test_longest_streak_not_first():
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_with_zeros_and_negatives():
    assert longest_positive_streak([-1, -2, 0, 1, 2, 0, 3, -4]) == 2

def test_all_non_positive():
    assert longest_positive_streak([-1, -2, 0, -3]) == 0

def test_single_positive():
    assert longest_positive_streak([5]) == 1

def test_alternating():
    assert longest_positive_streak([1, -1, 2, -2, 3, -3]) == 1

def test_all_positive():
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_long_streak_at_end():
    assert longest_positive_streak([1, 2, -1, 1, 2, 3, 4, 5]) == 5

def test_streak_of_ones():
    assert longest_positive_streak([1, 1, 1]) == 3
