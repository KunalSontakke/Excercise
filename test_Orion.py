"""math teacher
- theory paper 70 marks
- practical  30 marks
"""
import pytest


class Maths_Class:
    def __init__(self,name : str,theory : int,practical=0):
        self.name = name
        self.theory = theory
        self.practical = practical
    def addition(self):
        return self.practical + self.theory
    def display_total_marks(self):
        total_marks = self.addition()
        print(f"name:{self.name}")
        print(f"theory marks:{self.theory}")
        print(f"practical marks:{self.practical}")
        print(f"total marks :{total_marks}")

maths = Maths_Class('history',40)
maths.display_total_marks()
# ================================================================

import pytest

@pytest.mark.parametrize('a,b,addition',[(1,2,3),(2,3,5),(5,6,13)])
def test_addition(a,b,addition):
    assert a + b == addition

@pytest.mark.parametrize('a,b,division',[(2,1,2),(6,3,2),(144,6,24)])
def test_division(a,b,division):
    assert a/b == division

