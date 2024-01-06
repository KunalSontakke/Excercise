import pytest

@pytest.mark.parametrize('a,b,result',[(4,2,2),(10,5,2),(9,3,3),(10,3,3)])
def test_div(a,b,result):
    assert a / b == result
