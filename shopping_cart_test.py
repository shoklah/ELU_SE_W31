import pytest
from shopping_cart import CalculateTotal, display_total
import random

def TestCalculateTotal_TestEmpty():
    assert CalculateTotal([]) == 0, 'Incorrect sum on empty cart'

def TestCalculateTotal_TestRandom():
    random.seed(0)
    length = random.randint(1, 300)
    cart = []
    total_expected = 0.
    for x in range(length):
        item_price = random.random() * 100
        total_expected += item_price
        cart.append( {'name': f'Item {x}', 'price': item_price})
    assert abs(CalculateTotal(cart) - total_expected) < 1e-7, f'Incorrect sum on cart {cart}'

def TestCalculateTotal_TestString():
    random.seed(0)
    length = random.randint(1, 300)
    cart = []
    total_expected = 0.
    for x in range(length):
        item_price = random.random() * 100
        total_expected += item_price
        cart.append( {'name': f'Item {x}', 'price': str(item_price)})
    assert abs(CalculateTotal(cart) - total_expected) < 1e-7,  f'Incorrect sum on string cart {cart}'

