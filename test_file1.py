"""Problem 2: Setup and Teardown

Create a fixture named setup_teardown_fixture that prints "Setup" before the test and "Teardown" after the test.
Write a test function that uses this fixture."""
import pytest


@pytest.fixture(scope="function")
def setup_teardown_fixture():
    print("setup")
    yield
    print("teardown")


def test_addition(setup_teardown_fixture):
    print("1")

