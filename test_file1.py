import platform

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as SC
from selenium.webdriver.firefox.service import Service as SF

def test_multiplication():
    a = 11
    b = 2
    return a * b


@pytest.mark.parametrize("num,output",[(1,11),(2,22),(3,33),(4,44)])
def test_num(num,output):
    assert num * 11 == output


@pytest.fixture(params=["chrome","firefox"],scope="function")
def get_browser(request):
    if request.param == "chrome":
        service_chrome = SC("Drivers/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=service_chrome)
        print("Opening chrome Brwoser")
        yield driver
        driver.close()

    if request.param == "firefox":
        service_firefox = SF("Drivers/MozilaDriver/geckodriver.exe")
        driver = webdriver.Firefox(service=service_firefox)
        print('Opening firefox browser')
        yield driver
        driver.close()

def test_url(get_browser):
    driver = get_browser
    driver.get("https://www.amazon.com")

    print(driver.title)


@pytest.mark.skipif(platform.system()=="Windows",reason="test not supported to windows")
def test_add():
    a,b = 1,2
    return a + b

import pytest

# Fixture to set up a resource
@pytest.fixture
def setup_resource():
    print("\nSetting up resource")
    # Additional setup code can be added here
    yield
    print("\nTearing down resource")
    # Additional teardown code can be added here

# Test function using the setup_resource fixture
@pytest.mark.usefixtures("setup_resource")
def test_example():
    print("\nExecuting test")
    # Test logic goes here
    assert True

