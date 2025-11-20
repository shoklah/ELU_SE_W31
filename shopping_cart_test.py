import random
from shopping_cart import calculate_total, display_total


def test_display_total(capfd):
    display_total(20)
    out, err = capfd.readouterr()
    assert out == "Total price: 20\n"


def test_calculate_total__empty_cart():
    assert calculate_total([]) == 0, 'Incorrect sum on empty cart'


def test_calculate_total__zero_cart():
    assert calculate_total([{'name': 'Item0', 'price': 0.0}]) == 0, 'Incorrect sum on empty cart'


def test_calculate_total__random_cart():
    random.seed(0)
    length = random.randint(1, 300)
    cart = []
    total_expected = 0.
    for x in range(length):
        item_price = random.random() * 100
        total_expected += item_price
        cart.append({'name': f'Item {x}', 'price': item_price})
    assert abs(calculate_total(cart) - total_expected) < 1e-7, f'Incorrect sum on cart {cart}'


def test_calculate_total__string_cart():
    random.seed(0)
    length = random.randint(1, 300)
    cart = []
    total_expected = 0.
    for x in range(length):
        item_price = random.random() * 100
        total_expected += item_price
        cart.append({'name': f'Item {x}', 'price': str(item_price)})
    assert abs(calculate_total(cart) - total_expected) < 1e-7,  f'Incorrect sum on string cart {cart}'
