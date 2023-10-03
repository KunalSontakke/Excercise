"""
1) pytest framework
2) Project Info
3) Suppose Bug is reproduced in Production environment
4) Story point
5) Sprint Framework Ceremonies
6) New changes introduced in project
7) difference between Query and Path Parameter
8) API Status Code
9) Difference between Bug and Defect

"""


"""prints the number of occurrences of each character in a string.
Examples:

Input: str = "GeeksForGeeks"
Output:
r 1
s 2
e 4
F 1
G 2
k 2
o 1"""

input_str = "GeeksForGeeks"
freq = {}
for i in input_str:
    if i in freq:
        freq[i] = freq[i] +1
    else:
        freq[i] = 1

print(freq)




# ======================================================================================================================
# """ step 1) click on google URL
#     step 2) Search your Name
#     step 3) Click on "Search on google" Button
#     step 4) Find the number of results
#     step 5) check if result is greater than 50,000
#     step 6) if not,take screenshot of that page
#     step 7) print the number of results and 'your test case is failed'  """
#
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# service_obj = Service("C:\\Users\\Kunal\\PycharmProjects\\Selenium_project\\Drivers\\chromedriver_win32\\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get("https://www.google.com/")
# driver.maximize_window()
#
# # to enter name in text Box
# time.sleep(2)
# driver.find_element(By.NAME,"q").send_keys("kunal Sontakke")
#
# # click on "Google Search" Button
# time.sleep(2)
# driver.find_element(By.CLASS_NAME,"gNO89b").click()
#
# # check if results number is greater than 50,000
# Result_Stats = driver.find_element(By.ID,"result-stats").text
#
# if "50,000" in Result_Stats:
#     assert True
# else:
#     driver.get_screenshot_as_file("Encora.png")
#     print(Result_Stats)
#     print("Your Test Case is Failed")

# =====================================================================================================================

"""python program to find palindrome"""
#
#
# input = str(input("Enter the String : "))
#
# reverse = input[::-1]
#
# if input == reverse:
#     print("the string is Palindrome")
# else:
#     print("the string is not palindrome")

