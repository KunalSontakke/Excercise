"""
1)Open "https://mathup.com/games/crossbit?mode=championship"
2) Click on Play Button
3) Count How much time it take to load page in seconds for 10 times
4)count Average time from 10 counts.


# This code opens the Google homepage using the Chrome browser driver,
# measures the time before and after the page loads, and calculates the load time.
# The `execute_script` method waits for the page to completely load and returns `true` when it is done. Finally,
# the code prints the load time in seconds using the `time` library.
"""

from time import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service("Drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
count = 0
sum = 0
while count != 10:
    driver.get("https://mathup.com/games/crossbit?mode=championship")

    driver.find_element(By.XPATH,"//div[@class='GamePostStart_desktop-view-prestart__RK3F2']"
                                 "//div[contains(@class,'GamePreStart_btn__S9w8W btn')][normalize-space()='Play']").click()


    open_time = time()

    driver.execute_script("return document.readyState == 'complete'")

    close_time = time()
    load_time = close_time - open_time
    print("the loading time for webpage is :", load_time,"seconds")
    count = count + 1
    sum = sum + load_time
driver.close()
print("Average time to load",sum /10,"seconds")


