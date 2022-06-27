from hypothesis import given
import hypothesis.strategies as st
from .. import suma

@given(intA = st.integers(), intB = st.integers())
def test_hypo_suma(intA, intB):
    assert (suma.sumar(intA, intB) == (intA + intB))

@given(intA = st.integers(), intB = st.integers())
def test_hypo_resta(intA, intB):
    assert (suma.restar(intA, intB) == (intA - intB))

@given(intA = st.integers(), intB = st.integers())
def test_hypo_sumaresta(intA, intB):
    assert (suma.sumar(intA, intB) == suma.restar(intA, (-intB)))
