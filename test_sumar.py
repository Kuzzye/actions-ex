import pytest
from main import sumar, restar, multiplicar


def test_sumar():
	assert sumar(2, 3) == 5

def test_restar():
	assert restar(4, 2) == 2

def test_multiplicar():
	assert mukltiplicar(3, 2) == 6
