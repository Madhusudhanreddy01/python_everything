import math

def test_sqrt():
   num = 25
   assert math.sqrt(num) == 5

def testsquare():
   num = 7
   assert 7*1 == 7

def testequality():
   assert 11 == 11



import pytest
@pytest.mark.great
def test_greater():
   num = 100
   assert num > 99

@pytest.mark.great
def test_greater_equal():
   num = 100
   assert num >= 100

@pytest.mark.others
def test_less():
   num = 100
   assert num < 200