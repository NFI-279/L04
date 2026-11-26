import os
import sqlite3
import subprocess

import pytest

import exercise5
from exercise5 import *


# bug report 1
def test_r1_square():
    assert square(5) == 25


# bug report 2
def test_r2_is_adult_excludes_18():
    assert is_adult(18) == True


# bug report 3
def test_r3_safe_divide_division_by_zero():
    assert safe_divide(10, 0) == 0


# bug report 4
def test_r4_count_vowels_uppercase():
    assert count_vowels("AEIOU") == 5


# bug report 5
def test_r5_remove_duplicates():
    assert remove_duplicates([3, 1, 3, 2]) == [3, 1, 2]
