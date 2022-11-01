import pytest
from main import sumar


def test_sumar():
	assert sumar(2, 3) == 5

def test_restar():
	assert restar(4, 2) == 2
