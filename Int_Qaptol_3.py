import time

import pytest
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *


def test_webpage():
    service_obj = Service('Drivers/chromedriver_win32/chromedriver.exe')
    driver = webdriver.Chrome(service=service_obj)
    try:
        url = 'https://mypustak.com/'

        driver.maximize_window()
        driver.get(url)

        time.sleep(2)

        print(driver.title)

        book_title = driver.find_element(By.XPATH,'//div[@class="jsx-313054587 BookCard_textDiv__aJuti"]/child::h1[@title="CRACK IMU-CET Entrance Exam"]')
        assert book_title.text == 'Crack Imu-Cet Entrance Exam'

        add_to_cart_btn = driver.find_element(By.XPATH,'(//center[@class="jsx-313054587"]/child::button[@tabindex="0"])[1]')
        driver.execute_script(f'window.scrollBy(0,{add_to_cart_btn.location["y"]})')
        add_to_cart_btn.click()

    except NoSuchElementException as e:
        print(e)
    except StaleElementReferenceException as e:
        print(e)
    except WebDriverException as e:
        print(e)

    finally:
        driver.close()

@pytest.mark.skip
def test_webpage_2():
    service_obj = Service('Drivers/chromedriver_win32/chromedriver.exe')
    driver = webdriver.Chrome(service=service_obj)

    try:
        # visit URL
        driver.maximize_window()
        driver.get('https://untestable.site/the_glass_door')
        print(driver.title)

    #     Validate 'Visit Chicago'text
        Visit_Chicago_label = driver.find_element(By.XPATH,'//label[@class="card-label" and @for="visit-chicago-btn"]')
        if Visit_Chicago_label.text == 'Visit Chicago':
            print("Visit Chicago is present")
        else:
            print("Visit chicago is not present")

        Visit_Chicago_label.click()


    except NoSuchElementException as e:
        print(e)
    except StaleElementReferenceException as e:
        print(e)
    except WebDriverException as e:
        print(e)

    finally:
        driver.close()

