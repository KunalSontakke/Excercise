import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("Drivers/chromedriver_win32/chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.maximize_window()

driver.get("https://ultimateqa.com/dummy-automation-websites/")

time.sleep(3)
# button = driver.find_element(By.PARTIAL_LINK_TEXT,"DISCOVERY SESSION")
# locator = By.PARTIAL_LINK_TEXT,"DISCOVERY SESSION"
# wait = WebDriverWait(driver,10).until(expected_conditions.presence_of_element_located(locator))

# button.click()

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")

time.sleep(3)

class father:
    def intro(self):
        print("I am father")

class mom(father):
    def intro(self):
        print("I am mom")

class son(mom):
    def intro(self):
        father.intro(self)
        print("I am son")
#
#
Son = son()
Son.intro()

# inp = int(input("Enter number : "))
# print(inp)

# with open("Data/Text","r") as file:
#     data = file.read()
#     print(data)



# import requests

# request = requests.get("https://ultimateqa.com/dummy-automation-websites/",params=None,data=None,verify=False)

# print(request.status_code)
# print(request.text)

# status_code = [200,201,202,203,204]
# assert request.status_code in status_code

