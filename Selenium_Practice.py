
# =================================================================================
"Selenium"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_obj = Service("Drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

"visit url"
# driver.maximize_window()
#
# driver.get('https://www.google.com/')
#
# time.sleep(3)
#
# driver.close()

# =====================================================================
"Enter Text Input"

driver.maximize_window()

driver.get("https://seleniumpractise.blogspot.com/")

time.sleep(1)

# user_inp = driver.find_element(By.ID,'user')
# user_inp.send_keys('hindavi nalawade')
#
#
# password_inp = driver.find_element(By.NAME,'psw1')
# password_inp.send_keys('hindavi123')


# =====================================================================

"Click"
# "xpath = //tagname[@attribute_name='attribute_value']"
# Login_btn = driver.find_element(By.XPATH,'//button[@type="submit"]')
# Login_btn.click()
#
# time.sleep(3)

# ============================================================================================
"dropdwon"
# tools_drpdwn = Select(driver.find_element(By.ID,'tools'))

"select by index"
# tools_drpdwn.select_by_index(2)

"selct by visible text"
# tools_drpdwn.select_by_visible_text('Selenium')


"select by value"
# tools_drpdwn.select_by_value('Cucumber')

# time.sleep(3)

# ==================================================================================

"Hover"
# webTable_lnk = driver.find_element(By.LINK_TEXT,'WebTable In HTML')
#
# act = ActionChains(driver)
#
# act.move_to_element(webTable_lnk).perform()
#
# time.sleep(4)

# ===========================================================================================

"Scroll Page"
"scroll down to particular position"
# driver.execute_script('window.scrollBy(0,800)','')

"scroll down to page bottom"
# driver.execute_script('window.scrollBy(0,document.body.scrollHeight)')

"scroll down particular element location"
# alert_demo_lnk = driver.find_element(By.LINK_TEXT,'Alert Demo')

# print(alert_demo_lnk.location)
# driver.execute_script(f'window.scrollBy(0,{alert_demo_lnk.location["y"]})')

# time.sleep(3)

# ======================================================================================
"Screenshot"

# driver.save_screenshot("selenium_practice.png")


# ======================================================================================
"Press Keys"
# act = ActionChains(driver)
# act.key_down(Keys.CONTROL).send_keys("p").key_up(Keys.CONTROL).key_up("p").perform()
#
# time.sleep(4)

# ====================================================================================
"Alert"
# try_it_btn = driver.find_element(By.XPATH,"//button[text()='Try it']")
# try_it_btn.click()
#
# time.sleep(10)
#
# driver.switch_to.alert.accept()
#
# time.sleep(3)



