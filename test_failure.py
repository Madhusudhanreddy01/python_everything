import pytest
import math

def test_sqrt_failure():
   num = 25
   assert math.sqrt(num) == 5

def test_square_failure():
   num = 7
   assert 7*7 == 49

def test_equality_failure():
   assert 11 == 11
