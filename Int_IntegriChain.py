"""Write a Python program to get a string from a given string where all occurrences of its first char have been
changed to '$', except the first char itself.
Sample String : 'restartthecomputer'
# Expected Result : 'resta$$$h$comp$$$'"""

sample_string = 'restartthecomputer'

# List method

lis = []
s= 'restartthecomputer'
for ch in s:
    if ch in lis:
        lis.append('$')
    else:
        lis.append(ch)
print(''.join(lis))

# ======================================================================================================================
# String Method

input = "restartthecomputer"
dup_str = ""

for i in input:
    if i not in dup_str:
        dup_str = dup_str + i
    else:
        dup_str= dup_str + "$"
print(dup_str)


# ================================================================================================================================================================================


"""Automate the following Flow in python with a framework you are comfortable -
1. Launch chrome and navigate https://www.magicbricks.com/
2. Close all popups
3. Select Rent -> Budget -> above 25K
4. Print the Agent names of the 1st 20 search results"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# service_obj = Service("C:\\Users\\Kunal\\PycharmProjects\\Selenium_project\\Selenium_Projects\\Drivers\\chromedriver_win32\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.magicbricks.com/")
# driver.maximize_window()

# Select Rent -> Budget -> above 25K

# time.sleep(1)

# Rent = driver.find_element(By.LINK_TEXT,"Rent")
# Rent.click()
# time.sleep(3)
#
# Option= driver.find_element(By.LINK_TEXT,"Above ₹ 25,000")
# Option.click()
#
#
# # Print the Agent names of the 1st 20 search results
#
# agents = driver.find_elements(By.XPATH,'//*[@class="mb-srp__card__ads--name"]')
# for agent in agents:
#     print(agent.text)
#

