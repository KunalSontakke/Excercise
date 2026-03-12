import platform
import sys

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as SF
from selenium.webdriver.chrome.service import Service as SC

"""Create a fixture named simple_fixture that returns a simple dictionary with key-value pairs.
Write a test function that uses this fixture to assert a value from the dictionary
"""
import pytest
from selenium.webdriver.chrome.service import Service

# @pytest.fixture
# def simple_fixture():
#     dic = {"name": "kunal", "company": "msys", "location": "pune"}
#     return dic
#
#
# def test_dictionary(simple_fixture):
#     assert "kunal" in simple_fixture.values()


# ==================================================================================================
"""Problem 2: Setup and Teardown

Create a fixture named setup_teardown_fixture that prints "Setup" before the test and "Teardown" after the test. 
Write a test function that uses this fixture."""

# @pytest.fixture(scope="function")
# def setup_teardown():
#     print("Setup")
#
#     yield
#
#     print("Teardown")
#
#
# def test_function(setup_teardown):
#     print("setup is under process")


# =========================================================================================
"""Create a parametrized fixture named param_fixture that takes a parameter and returns a list. 
Write a test function that uses this fixture with different parameters."""

#
# @pytest.fixture(params=[1,2,3,4])
# def param_fixture(request):
#     param = request.param
#
#     return [param,param * 2,param * 3]
#
# def test_params(param_fixture):
#     my_list = param_fixture
#
#     return my_list


# =================================================================================================

"""Create a fixture named file_fixture.txt that creates a temporary text file with some content before the test 
and deletes it after the test. Write a test function that reads the content from the file and asserts it."""

# @pytest.fixture(scope="function")
# def file_fixture.txt(request):
#     file_name = request.config.getoption("--filename",default="Data/file.txt")
#     file = open(file_name,"w")
#     yield file
#
#     file.close()
#     print("closed file")
#
#
# def test_file(file_fixture.txt):
#     read = file_fixture.txt.read()
#     print(read)
#
# #
# import pytest
#
# @pytest.fixture(scope="function")
# def file_fixture.txt(tmp_path):
#     file_path = tmp_path / "file.txt"
#     with open(file_path, "w") as file:
#         # Write some content to the file
#         file.write("Test content")
#
#     yield file_path  # Provide the file path to the test
#
#     # Teardown: The file will be automatically closed and deleted
#
# def test_file(file_fixture.txt):
#     with open(file_fixture.txt, "r") as file:
#         file_content = file.read()
#
#     # Assert the content from the file
#     print(file_content)
#


# ==========================================================================================
# @pytest.fixture(scope="class")
# def normal_fixture():
#     print("Setup is under process...")
#     yield
#     print("setup completed")
#
#
# def test_database_connection(normal_fixture):
#     print("database connected")
#
#
# def test_API_connection(normal_fixture):
#     print("API Setup completed")


# ====================================================================================================================
# """Task: Write a test that checks whether a given number is even or odd."""
#
# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
#
# @pytest.mark.parametrize("number,result",[
#                         (2,True),
#                         (3,False),
#                         (10,True),
#                         (101,True)])
# def test_even(number,result):
#     even = is_even(number)
#     assert result == even


# ==============================================================================================================
"""Task: Write a test that checks whether a given string is a palindrome."""
#
# def check_palindrome(string):
#     if string == string[::-1]:
#         print(f"{string} is palindrome")
#     else:
#         print(f"{string} is not palindrome")
#
# @pytest.mark.parametrize("string",["madam","malayalam","mississippi","america","carrom"])
# def test_palindrome(string):
#    return check_palindrome(string)


# =========================================================================================================
"""Task: Write a test for a function that performs a mathematical operation (e.g., addition, subtraction, multiplication, division)"""

# def perform_operation(a, b, operator):
#     # Function to perform a mathematical operation on two numbers
#     pass

#
# @pytest.mark.parametrize("a, b, operator, expected_result", [
#     (2, 3, '+', 5),
#     (5, 2, '-', 3),
#     (4, 6, '*', 24),
#     (8, 2, '/', 4),
# ])
# def test_perform_operation(a, b, operator, expected_result):
#     result = perform_operation(a, b, operator)
#     assert result == expected_result
#
#
# @pytest.fixture(params=["chrome","firefox","IE"])
# def browsers(request):
#     if request.param == "chrome":
#         service_chrome = Service("Drivers/chromedriver_win32/chromedriver.exe")
#         driver = webdriver.Chrome(service=service_chrome)
#         print("Opening chrome browser")
#         return driver
#
#     elif request.param == "firefox":
#         service_firefox = ServiceFiirefox("Drivers/MozilaDriver/geckodriver.exe")
#         driver = webdriver.Firefox(service=service_firefox)
#         print("Opening chrome browser")
#         return driver
#
#     else:
#         pass
#
# def test_link(browsers):
#     browsers.get("https://www.automationexercise.com")
#     print(browsers.title)
#
# def test_link2(browsers):
#     browsers.get("https://www.facebook.com")
#     print(browsers.title)
#
# #
# @pytest.fixture(params=["chrome","firefox"],scope="function")
# def get_browser(request):
#     if request.param == "chrome":
#         service_chrome = SC("Drivers/chromedriver_win32/chromedriver.exe")
#         driver = webdriver.Chrome(service=service_chrome)
#         print("Opening chrome Browser")
#         yield driver
#         driver.close()
#
#
#     if request.param == "firefox":
#         service_firefox = SF("Drivers/MozilaDriver/geckodriver.exe")
#         driver = webdriver.Firefox(service=service_firefox)
#
#         print("opening firefox browser")
#
#         yield driver
#
#         driver.close()
#
#
# def test_link(get_browser):
#     browser = get_browser
#     browser.get("https://automationexercise.com")
#     print(browser.title)


# @pytest.mark.parametrize("num1,num2,output",[(4,2,2),(16,4,4),(16,"a",16),(16,0,16)])
# def test_division(num1,num2,output):
#     try:
#         assert num1 / num2 == output
#     except ZeroDivisionError as e:
#         print(e)
#
#     except AttributeError as e:
#         print(e)
#     except Exception as e:
#         print(e)
#
# def is_even(n):
#     if n % 2 == 0:
#         return "even"
#     else:
#         return "odd"

from selenium.webdriver.firefox.service import Service as SF


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def call_driver(request):
    if request.param == 'chrome':
        service_obj = Service('Drivers/chromedriver_win32/chromedriver.exe')
        driver = webdriver.Chrome(service=service_obj)

        print("chrome browser is opened")
        driver.maximize_window()

        yield driver

        driver.close()
        print("browser closed....")

    elif request.param == "firefox":
        service_obj = SF('Drivers/MozilaDriver/geckodriver.exe')
        driver = webdriver.Firefox(service=service_obj)

        driver.maximize_window()
        print("firefox browser is opened....")
        yield driver

        driver.close()


@pytest.mark.xfail
def test_webpage(call_driver):
    driver = call_driver
    driver.get('https://www.google.com')

    print(driver.current_url)
