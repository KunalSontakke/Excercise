from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#
service_obj = Service("C:\\Users\\Kunal\\PycharmProjects\\Excercise\\Drivers\\chromedriver_win32\\chromedriver.exe")
#
driver = webdriver.Chrome(service=service_obj)
# driver.get("https://www.amazon.com")
#
# msg = driver.find_element(By.XPATH,"//input[text(),'Hi']")
# msg.click()

# ==============================
# table = ""
# arr = []
# for i in table:
#     arr.append(i)
#
# for i in arr:
#     if arr.index(i) == 4:
#         print(i)


# =======================================
driver.get("https://www.google.com")
search_box = driver.find_element(By.NAME,"search")
search_box.clear()

search_box.send_keys("kunal")


links = driver.find_elements(By.TAG_NAME,"a")
for link in links:
    print(link)


