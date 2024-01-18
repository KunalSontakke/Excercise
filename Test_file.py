import argparse
import platform

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as SF


def test_multiplication():
    num = 11
    for i in range(1, 11):
        print(f"{num} x i", num * i)


@pytest.mark.sanity
@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_browser(browser):
    global driver
    if browser == "chrome":
        service_chrome = Service("Drivers/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=service_chrome)
        return driver

    if browser == "firefox":
        service_firefox = SF("Drivers/MozilaDriver/geckodriver.exe")
        driver = webdriver.Firefox(service=service_firefox)
        return driver
    driver.get("https://www.automationexercise.com")


@pytest.mark.sanity
@pytest.fixture(scope="function", params=["chrome", "firefox"])
def get_driver(request):
    if request.param == "chrome":
        service_chrome = Service("Drivers/chromedriver_win32/chromedriver.exe")
        driver = webdriver.Chrome(service=service_chrome)
        print("Opening chrome")

        yield driver

        print("closing driver")

        driver.close()

    if request.param == "firefox":
        service_firefox = SF("Drivers/MozilaDriver/geckodriver.exe")
        driver = webdriver.Firefox(service=service_firefox)

        print("Opening firefox browser")
        yield driver

        print("closing browser")
        driver.close()


def test_url(get_driver):
    browser = get_driver
    browser.get("https://www.automationexercise.com")
    print(browser.title)


@pytest.mark.skip
def test_addition():
    a, b = 2, 3
    return a + b


# @pytest.mark.skipif(platform.system() == "Windows", reason="test is not supported windows")
# def test_url(browsers):
#     browsers.get("https://www.facebook.com")
#
#     print(browsers.title)


@pytest.mark.xfail
def test_division():
    a, b = 4, 0
    return a / b


def pytest_adoption(parser):
    parser.adoption("--browser",
                    action="store",
                    default="chrome",
                    choices=["chrome", "firefox", "edge"],
                    help="Specify the browser to test")



def parse_argument():
    parser = argparse.ArgumentParser()
    parser.add_argument("--browser", action="store", default="chrome", choices=["chrome", "firefox", "edge"],
                        help="Support")
    args = parser.parse_args()
    return args


@pytest.fixture(scope="function")
def browser_option(request):
    return request.config.getoption("--browser")

def test_div():
    a = 4
    b = 2
    div = a /b
    print(div)


@pytest.mark.parametrize("num,output",[(1,11),(2,22),(3,33),(4,44),(5,56)])
def test_output(num,output):
    assert num * 11 == output


