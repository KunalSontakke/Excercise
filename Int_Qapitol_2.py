"""
1) Pytest Markers
2) pytest fixture
3) Fixture scope
4)  How can we Execute test files in serial order using pytest
5) out of 100 test files, I want to exclude 1 test file. how can we achieve it using pytest

- Run pytest and use the --ignore option followed by the path to the test file you want to exclude.
  command - pytest --ignore=path/to/test_file_to_exclude.py

6)
"""

# """write a command to exclude a particular test case"""
# import pytest
#
#
# # pytest Test_file.py
#
# @pytest.mark.parametrize("browser",['chrome','firefox'])
# def test_url(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         yield driver
#         driver.close()
#     elif browser =="firefox":
#         driver = webdriver.Firefox()
#         yield driver
#         driver.close()
#
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException,ElementClickInterceptedException,NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service('Drivers/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=service_obj)

try:
    driver.maximize_window()
    driver.get('https://www.mypustak.com/free-books')

    wait = WebDriverWait(driver,10)
    book_titles = wait.until(EC.presence_of_all_elements_located((By.XPATH,'//h1[@class="jsx-313054587 BookCard_bookTitle__oOJiw line-clamp-2"]')))

    for title in book_titles:
        if title.text == "NATIONAL GEOGRAPHIC APRIL 2010 VOL 217 NO 4":
            Add_to_cart_btn = driver.find_element(By.XPATH,'class="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeSmall MuiButton-containedSizeSmall button  mui-15bo7te"')
            Add_to_cart_btn.click()

    print("test case passed")
except NoSuchElementException as e:
    print(e)

finally:
    driver.close()



# lis1 = [1,2,3,4,5,6]
# output ="!23456"
#
# result = ""
# for i in lis1:
#     result += str(i)
# print(result)
#
# print("".join(lis1))


# dic1 = {'name':'kunal','age':30}
# dic1['compnay'],dic1['position'] = 'msys','automation engineer'
# print(dic1)
