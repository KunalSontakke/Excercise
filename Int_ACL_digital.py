"""Write program using python and selenium to do below steps
1. Navigate to: https://www.flightradar24.com/data/airports/pnq
2. From the arrivals section, print the status of the flights coming in from Bangalore, Delhi, Goa, Chandigarh, Hyderabad, Nagpur & Dubai.
3. Output example:
Bangalore: Estimated 11:43 AM
Delhi: Estimated 12.32 PM
Goa: data not available (if there is no entry for a flight from Goa)
Dubai: data not available (if there is no entry for a flight from Dubai)"""
#
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#
# class find_arrival_status:
#     def print_arrival_status(self):
#         service_obj = Service("Drivers\\chromedriver_win32\\chromedriver.exe")
#         driver = webdriver.Chrome(service=service_obj)
#
#
#         # visit the site
#         driver.get("https://www.flightradar24.com/data/airports/pnq")
#         print(driver.title)
#         locator = By.XPATH,'//span[text()="Agree and close"]'
#         fram_alert_close_btn = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(locator))
#
#         if fram_alert_close_btn:
#             fram_alert_close_btn.click()
#
#         pref_cities = ["Bengaluru", "Delhi", "Goa", "Chandigarh", "Hyderabad", "Nagpur", "Dubai"]
#
#         arr_cities = driver.find_elements(By.XPATH, '//span[@class="hide-mobile-only ng-binding"]')
#         statuses = driver.find_elements(By.XPATH, "//td[@class='ng-binding']/span")
#         for city in arr_cities:
#             for status in statuses:
#                 if city in pref_cities:
#                     print(city.text,":",status.text)
#
# check = find_arrival_status()
# check.print_arrival_status()
#

""""My name is Ajay and I'm 24 years old and my birth date is 17th Oct 2000"
24+17+2000 => 2041"""

inp = "My name is Ajay and I'm 24 years old and my birth date is 17th Oct 2000"
sum = 0
num = []
for i in inp.split():
    if i.isdigit():
        num.append(int(i))
print(num)

"""Reverse the characters of word without reversing the order of the words.
Eg: How are you? => woH era ?uoy"""

inp2 = "How are you?"
print(" ".join([i[::-1] for i in inp2.split(" ")]))
