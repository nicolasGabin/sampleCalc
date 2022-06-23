from .. import mult
import pytest

@pytest.mark.parametrize('a, b, c', [
    (1, 1, 1),
    (1, 0, 0),
    (0, 1, 0),
    (1, -1, -1),
    (-1, 1, -1)
])
def test_multi(a, b, c):
    assert mult.multiplicar(a, b) == c

def test_dividirZero():
    with pytest.raises(ZeroDivisionError) as e:
        mult.dividir(1, 0)
    assert "division by zero" in str(e.value)
# ZeroDivisionError: division by zero
