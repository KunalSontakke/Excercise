# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.action_chains import ActionChains
#
# service_obj = Service("Drivers/chromedriver_win32/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.flipkart.com/")
# driver.maximize_window()
#
# groceries = driver.find_element(By.LINK_TEXT,"Groceries")
# act = ActionChains(driver)
#
# act.move_to_element(groceries).perform()
#
# driver.find_element(By.XPATH,"element").click()
# window_handle = driver.window_handles
# driver.switch_to.window(1)

lis1 = [2, 5, 2, 2, 5]
lis2 = [5, 5, 2, 2, 2]

"if count of 2 is more than count of 5 then True"

if lis1.count(2) > lis1.count(5):
    print("Success...........")

"swap the first and last element of list"

lis1[0], lis1[-1] = lis1[-1], lis1[0]
print(lis1)
lis2 = lis1

"check if there are consecutive elements or not"

lis1 = [2, 5, 2, 2, 5]
lis2 = [5, 5, 2, 2, 2]
for i in range(len(lis1)):
    if lis1[i] == lis1[i - 1]:
        print("True")
