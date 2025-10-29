import pytest


@pytest.mark.sanity
class Test_1:
    def test_intro(self):
        print("Hello I am kunal")


@pytest.mark.regression
class Test_2:
    def test_show_salary(self):
        print("my salary is 1000 rs")

