import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service('Drivers/chromedriver_win32/chromedriver.exe')

driver = webdriver.Chrome(service=service_obj)
try:
    driver.maximize_window()



    driver.get('https://www.cisco.com')
    # loading_time = driver.execute_script("return window.performance.timing.navigationStart")
    #
    # End_time = driver.execute_script("return window.performance.timing.loadEventEnd")
    #

    # load_time = End_time - loading_time
    # print(f"page loaded in {load_time/1000} seconds")
    ready_state = driver.execute_script("return document.readyState == 'complete'")

except Exception as e:
    print(e)
