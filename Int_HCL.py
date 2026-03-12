import requests
from selenium.webdriver.support.wait import WebDriverWait


class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

calculator = Calculator(4,3)
print(calculator.addition())
print(calculator.a)
print(calculator.b)

# =========================================================
"""input = {'All' : [1, 2, 3], 'is' : [1, 4], 'well' : [4, 2]}
# output = {1: ['All', 'is'], 2: ['All', 'well'], 3: ['All'], 4: ['is', 'well']}"""

inp1 = {'All' : [1, 2, 3], 'is' : [1, 4], 'well' : [4, 2]}
out = {}

for key,value in inp1.items():
    for i in value:
        if i not in out:
            out[i] = [key]
        else:
            out[i].append(key)
print(out)

# ==========================================================
ip="python compiler"

freq = {}
for i in ip:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

print(freq)

# ===================================================================
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def check_webpage():
    service_obj = Service('Drivers/chromedriver_win32/chromedriver.exe')
    driver = webdriver.Chrome(service=service_obj)

    driver.maximize_window()

    # open URL
    driver.get('https://www.amazon.in/')

    print(driver.title)

    wait = WebDriverWait(driver,10)

    # Hamburger menu
    hamburger_menu = wait.until(EC.presence_of_element_located((By.XPATH,'//a[@id="nav-hamburger-menu"]')))

    # verify menu is displayed or not
    assert hamburger_menu.is_displayed()

# ================================================================================
check = check_webpage()
# sample_json = {"name":"kunal","city":"nagpur","company":"nitor"}
# post_request =requests.post(url='www.amazon.com',json=sample_json,auth="12344",allow_redirects=True,verify=True)
#
# print(post_request.status_code)
# print(post_request.headers)
