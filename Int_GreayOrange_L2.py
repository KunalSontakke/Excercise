# """openpyxl"""
# import openpyxl
#
# worbook = openpyxl.load_workbook("filename")
# sheet = worbook['sheet1']
#
# def max_row():
#     max_row = sheet.cell.amx_row
#     return max_row
#
# def max_column():
#     max_column = sheet.cell.max_column
#     return max_column
#
# def read_data(filenname):
#     cell_value = cell.value(row=max_row(),column=max_column())
#     return  cell_value
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# service_obj = Service("path to chromedriver")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get()
#
# s = "kunal"
# print(s[:3])
#
# print(s[-3:])
#
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

inp = "Hi my name is kunal , I am working msys"
for i in inp.split():
    if i.isalpha():
        print(i)
#
act = ActionChains(driver)

act.double_click(element).perform()

option = Select(element)
option.select_by_index(0)

response = requests.get(url,verify=True)
print(response.status_code)

assert response.status_code == 200
