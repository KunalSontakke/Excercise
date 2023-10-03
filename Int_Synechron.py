"""
1) How to open blank Browser or no URL with selenium
2) How to select all options from dropdown
3) How to retrieve data from Set array using Collections

"""

import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# service_obj = Service("Drivers/chromedriver_win32/chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
cwd = os.getcwd()

print("current working directory",cwd)
print("sys version is",sys.version)
print("sys version.info is",sys.version_info)
print("sys.platform is",sys.platform)
print("sys.path is",sys.path)
print("sys.argv is",sys.argv)
print("api version is",sys.api_version)
print("bas exec prefix is",sys.base_exec_prefix)
print("sys.base_prefix is",sys.base_prefix)
print("bulletin module is",sys.builtin_module_names)

"""
Input array=[13,0,17,0,5,0,9]
output = [13,17,5,9,0,0,0]"""
input_array = [13,0,17,0,5,0,9]
rev_inp = []
for i in input_array:
    if i != 0:
        rev_inp.append(i)
for j in range(input_array.count(0)):
    rev_inp.append(0)
print(rev_inp)

# OR

non_zeros = [i for i in input_array if i!=0]
zeros = [0] * (len(input_array) - len(non_zeros))
oup = non_zeros +zeros
print(oup)

# ======================================================================================================================

"""How to retrieve data from set array using collections"""
from collections import Counter


my_array = [1, 2, 3, 2, 3, 4, 3, 4, 5, 6, 7, 5, 8, 9, 7, 9]

# 3.Pass the array to the Counter() function of the collectionmodule.It will create a dictionary
# with elements as keys and their count as values.

result = Counter(my_array)
print(result)

# =====================================================================================================================

# """How to open Blank browser using selenium"""
# driver.maximize_window()
# driver.get("about:blank")
# time.sleep(10)
# print("I have waited for 15 seconds...... ")



