"""What happens if fixture and test both use parametrization?"""
import pytest


@pytest.fixture(params=[1,2])
def number(request):
    return request.param

@pytest.mark.parametrize("divisor",[2,3,4,5,6])
def test_number(number,divisor):
    return number * divisor

