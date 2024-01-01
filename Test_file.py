import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--headless")
options.add_argument("")



@pytest.fixture(scope="function")
def browser():
    service_obj = Service("Drivers/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj,options=options)
    driver.maximize_window()

    yield driver

    driver.close()


def test_url(browser):
    browser.get("https://www.facebook.com")


@pytest.mark.parametrize("name,password",[("kunal","kunal123"),("shrutika","shrutika123")])
def test_password(name,password):
    assert "kunal" in password



options.add_argument("--start-maximized")
