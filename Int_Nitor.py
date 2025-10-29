# """implictly wait"""
#
# driver,implicitly_wait(10)
#
# """explicit wait"""
#
# wait = WebDriverWait(driver,10).untill(expected_conditions.presence_of_element_located(locator))
#
# import pytest
#
#
# from lib,uiAutomation import get_driver
#
# driver = get_driver()
#
# driver.execute_Script('window.scrollBY(0,400)')
#

"""palindrome string"""
a = "madam"

if a == a[::-1]:
    print(f"{a} is palindrome")
else:
    print(f"{a} is not palindrome")

# =======================================================

"""fibonacci series"""


def find_fibonacci_series(n):
    fibonacci_series = []
    if n < 0:
        return fibonacci_series
    elif n == 0 or n == 1:
        fibonacci_series.append(1)
    else:
        fibonacci_series = [0, 1]
        for i in range(2, n):
            next_term = fibonacci_series[i - 1] + fibonacci_series[i - 2]
            fibonacci_series.append(next_term)
        return fibonacci_series


print(find_fibonacci_series(20))
