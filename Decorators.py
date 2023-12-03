# def make_bold(func):
#     def inner():
#         return "<b>" + func() + "</b>"
#     return inner
#
#
# def make_italic(func):
#     def inner():
#         return "<i>" + func() + "</i>"
#     return inner
#
#
# def make_underline(func):
#     def inner():
#         return "<u>" + func() + "</u>"
#     return inner
#
# @make_bold
# @make_italic
# @make_underline
# def function():
#     return "hello world"

# print(function())

# =====================================================================================================================

# def decor1(func):
#     def inner():
#         x = func()
#         return x * x
#     return inner
#
#
# def decor(func):
#     def inner():
#         x = func()
#         return 2 * x
#     return inner
#
#
# @decor1
# @decor
# def numeric():
#     return 30
#
#
# print(numeric())


# =====================================================================================================================

"""Here's an example of a decorator function to click on a WebElement using Selenium:"""

# from functools import wraps
# from selenium.webdriver.common.by import By
#
# def click_element(function):
#     @wraps(function)
#     def wrapper(*args):
#         element = function(*args)
#         element.click()
#         return element
#     return wrapper

# This decorator can be applied to a function that returns a WebElement,
# and it will automatically click on the returned element. Here's an example usage with a Selenium driver instance:

# from selenium import webdriver
#
# @click_element
# def find_element(driver, locator):
#     return driver.find_element(*locator)
#
# driver = webdriver.Chrome("Drivers/chromedriver_win32/chromedriver.exe")
# driver.get("https://www.google.com")
# time.sleep(3)
# search_box = find_element(driver,(By.NAME, "q"))
# search_box.send_keys("Selenium")
# time.sleep(3)
# search_box.submit()

# =====================================================================================================================
"""In Selenium Python, we can write a decorator for dropdown by using the Select class.
The Select class provides methods to select and deselect options from a dropdown element.
Here's an example of a decorator for selecting an option from a dropdown:"""

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome("Drivers/chromedriver_win32/chromedriver.exe")
#
# def select_option(func):
#     def wrapper(*args, **kwargs):
#         dropdown_element = driver.find_element(By.XPATH,args[0])
#         select = Select(dropdown_element)
#         select.select_by_visible_text(args[1])
#         func(*args, **kwargs)
#     return wrapper
#
#
"""This decorator takes in the XPath of the dropdown element and the option to select.
It then finds the element using the XPath and creates a Select object from it.
It selects the option using the select_by_visible_text method and then invokes the original function.
To use this decorator, we can annotate our methods that interact with dropdowns:"""

# @select_option
# def test_select_dropdown():
#         driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
#         # assert in("Selenium Easy",driver.title)


"""This will ensure that the specified option is selected before the method is executed."""
# test_select_dropdown()

# =============================================================================================================

# def decor_sqr(func):
#     def wrapper():
#         x = func()
#         return x * x
#     return wrapper
#
# @decor_sqr
# def func():
#     return 10
#
# print(func())
#
#
# def addition(var1,var2):
#     def decorator(func):
#         def wrapper(*args):
#             total = var1 + var2
#             result = func(*args) + total
#             return result
#         return wrapper
#     return decorator
#
#
# @addition(1,2)
# def pri_num(a,b):
#     return a + b
#
#
# print(pri_num(3,4))


# =======================================================================================================
""" Write a Python program to create a decorator function to measure the execution time of a function"""
import time

# def measure_exec_time(func):
#     def wrapper(*args):
#         start_time = time.time()
#         result = func(args)
#         end_time = time.time()
#         exec_time = end_time - start_time
#         print(f"{func.__name__} took execution time {exec_time} in seconds")
#         return result
#     return wrapper

# @measure_exec_time
# def function(numbers):
#         mul = 1
#         for i in numbers:
#             mul = mul * i
#         return mul
#
# print(function(1,2,3,4,5))
#
#
# @measure_exec_time
# def numeric(n):
#     return n
#
# inp = int(input("Enter input"))
#
# print(numeric(inp))

# ======================================================================================================================
# write a decorator function for selecting option from dropdown

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# @staticmethod
# def select_dropdown_option(func):
#     def wrapper(*args):
#         try:
#             dropdown_element = driver.find_element(By.ID,'VendorId')
#             select = Select(dropdown_element)
#             return func(select,*args)
#         except Exception as e:
#             print("Error selecting option", e)
#
#     return wrapper
#
# @select_dropdown_option
# def select_dropdown_option(select,option):
#     return select.select_by_index(option)
#
# service_obj = Service("C:\\Users\\Kunal\\PycharmProjects\\Automation_Excercise\\Drivers\\chromedriver_win32\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
# driver.get("https://admin-demo.nopcommerce.com/Admin/Order/List")
#
# driver.maximize_window()
# driver.find_element(By.ID,"Email").clear()
# driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
# driver.find_element(By.ID,"Password").clear()
# driver.find_element(By.ID,"Password").send_keys("admin")
# driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
# time.sleep(2)
#
# select_dropdown_option(2)
# time.sleep(3)

# ======================================================================================================================

# def sqr_cube_num(func):
#     def wrapper(x):
#
#         if 1< x <=10:
#             result = x ** 2
#         else:
#             result = x ** 3
#         return func(result)
#
#     return wrapper
#
# @sqr_cube_num
# def pri_num(n):
#     return n
#
# inp = int(input("Enter the number: "))
#
# print(pri_num(inp))

# ======================================================================================================================

# Write a Python program to create a decorator that logs the arguments and return value of a function.The decorator
# in this code logs the function name, arguments, and return value whenever the decorated function is called

# def logs_function(func):
#     def wrapper(*args,**kwargs):
#         print(f"calling function {func.__name__} with args {args},kwargs {kwargs}")
#
#         result = func(*args,**kwargs)
#
#         print(f"{func.__name__} returned {result}")
#
#         return result
#     return wrapper
#
#
# @logs_function
# def addition(a,b):
#     return a + b
#
#
# print(addition(3,4))

# ======================================================================================================================
# Write a Python program to create a decorator to convert the return value of a function to a specified data type
# def show_data_type(data_type):
#     def decorator(func):
#         def wrapper(*args,**kwargs):
#             result = func(*args,**kwargs)
#             return data_type(result)
#         return wrapper
#     return decorator
#
# @show_data_type(str)
# def func(x,y):
#     return x + y
#
# result = func(10,20)
# print(type(result))

def measure_exec_time(func):
    def wrapper(*args):
        start_time = time.time()
        end_time = time.time()
        exec_time = end_time - start_time
        if args is not None:
            result = func(*args)
        else:
            result = func()
        print(f"{func.__name__} has taken {exec_time} in seconds")
        return result
    return wrapper

@measure_exec_time
def print_num(a):
    return a

print(print_num(12))
