from .. import suma
import pytest

@pytest.mark.parametrize('a, b, c', [
    (1, 1, 2),
    (1, 0, 1),
    (0, 1, 1),
    (0, 0, 0),
    (-1, 1, 0),
    (-1, -1, -2)
])
def test_suma(a, b, c):
    assert suma.sumar(a, b) == c

@pytest.mark.parametrize('a, b, c', [
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, -1),
    (0, 0, 0),
    (-1, 1, -2),
    (-1, -1, 0)
])
def test_resta(a, b, c):
    assert suma.restar(a, b) == c

@pytest.mark.parametrize('a, b', [
    (2, 2),
    (2, -2),
    (0, 0)
])
def test_opuestos(a, b):
    assert suma.sumar(a, b) == suma.restar(a, -b)

def test_exceptionSuma():
    with pytest.raises(ValueError) as e:
        suma.sumar("a", "b")
    #ValueError: invalid literal for int() with base 10: 'a'
    assert "invalid literal" in str(e.value)

def test_exceptionResta():
    with pytest.raises(ValueError) as e:
        suma.restar("a", "b")
    #ValueError: invalid literal for int() with base 10: 'a'
    assert "invalid literal" in str(e.value)
