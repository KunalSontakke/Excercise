import time
from typing import KeysView

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

#
def check_links():
    service_obj  = Service('Drivers/chromedriver_win32/chromedriver.exe')
    driver = webdriver.Chrome(service=service_obj)
    act = ActionChains(driver)
    try:
        # open google
        driver.maximize_window()

        driver.get("https://www.google.com")

        wait = WebDriverWait(driver,10)

        search_bx = wait.until(EC.presence_of_element_located((By.NAME,'q')))

        search_bx.send_keys("python")
        search_bx.send_keys(Keys.ENTER)

        captcha_exception = wait.until(EC.presence_of_element_located((By.XPATH,'//div[@class="recaptcha-checkbox-border"]')))
        if captcha_exception:
            captcha_exception.click()
        else:
            pass

    except Exception as e:
        print("Error Found :",e)
        driver.get_screenshot_as_file("Screenshots/error.png")

check_links()
# =========================================================================================


"Sasdfssdfe2  ssfesaasaasereaaAdk5"

str1 = "Sasdfssdfe2"

# dic1 = {}
# count = 0
# for i in str1.lower():
#     if i.isalpha():
#         if i not in dic1:
#             dic1[i] = 1
#         else:
#             dic1[i] += 1
#     else:
#         count += int(i)
#
#     if dic1[i] > count:
#         dic1[i] = 1


