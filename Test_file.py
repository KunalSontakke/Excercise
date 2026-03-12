"""Task: Write a test that checks whether a given string is a palindrome."""
import os.path

import pytest

"""Write a pytest test function to test addition."""
@pytest.mark.parametrize('a,b',[(1,2),(2,3),(4,5),(5,11)])
def test_addition(a,b):
    return a + b

"""Test a function that divides two numbers and raises ZeroDivisionError."""

@pytest.mark.parametrize('a,b',[(4,2),(20,4),(25,5),(3,0)])
def test_division(a,b):
    try:
         return a/b

    except ZeroDivisionError as e:
        print(e)


"""Fixture returns: [1, 2, 3, 4, 5]
Write a test that checks if sum is 15."""

@pytest.fixture(scope='function')
def list_retriever():
    lis = [1,2,3,4,5]
    return lis

def test_sum(list_retriever):
    lis = list_retriever
    assert sum(lis) == 15


# =====================================================================
"""Example: Opening a file

Task:
Fixture opens a file → test writes to it → fixture closes file."""
@pytest.fixture(scope='function')
def open_file(mode='w'):
    file = open(os.path.join('Data','file_python'),mode)

    yield file

    file.close()

def test_file(open_file):
    file = open_file
    file.write('here I am adding new text using fixture')

    with open(file.name,'r') as f:
        print(f.read())
