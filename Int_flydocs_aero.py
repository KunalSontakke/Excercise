"""
1) Dynamic Typing
2) __name__ = __main__
3) Split Functions
4) Web scrapping
5) Delete Cookies
6) Encapsulation
7) Slicing
8) issubclass()
9) Can we create baseclass without object
10) Packing and Unpacking
11) How we use Inheritance in Page object model
12) text() in Xpath/how do we find text in locators

"""


def add_func(a, b):
    return a + b


print(__name__)
if __name__ == "__main__":
    print(add_func(10, 20))
# =========================================================================================================================

"""How to delete cookie while performing Automation testing on website"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service(
    "C:\\Users\\Kunal\\PycharmProjects\\Selenium_project\\Selenium_Projects\\Drivers\\chromedriver_win32\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.geeksforgeeks.org/")
print(driver.get_cookie("foo"))
driver.delete_cookie("foo")

# =======================================================================================================================


"""What is Packing in python ?
- Packing is a technique in python with which we put several values into a single iterator.
We can perform packing by using simple syntax for declaration of iterables 
like list or tuples or we can use asterisk operator * for packing. """

num1 = 1
num2 = 2
num3 = 3
*num, = num1, num2, num3

print(*num)


def mySum(*args):
    return sum(args)


print(mySum(1, 2, 3, 4, 5))
print(mySum(10, 20))

# ======================================================================================================================

"""How to find text element "__text"  using selenium"""

# driver.find_element(By.XPATH,"//*[text()='__text']")

# ======================================================================================================================
"""webscrapping in python" 
- Let’s suppose you want to get some information from a website? Let’s say an article from the website or some news article,
  what will you do? The first thing that may come in your mind is to copy and paste the information into your local media. 
  But what if you want a large amount of data on a daily basis and as quickly as possible.
  In such situations, copy and paste will not work and that’s where you’ll need web scraping.
  
  Requests library is used for making HTTP requests to a specific URL and returns the response. 
  Python requests provide inbuilt functionalities for managing both the request and response
  GET method is used to retrieve information from the given server using a given URI.
  The GET method sends the encoded user information appended to the page request."""

import requests

read = requests.get("https://www.geeksforgeeks.org/python-programming-language/")

print(read.content)

with open('file.txt', 'w') as f:
    f.write(read.text)

"""There are several ways to store the contents of web scraping using Selenium with Python into a file"""

# 1. Write to a text file: You can save the scraped content as text file using Python's built-in `open` function.

"""
with open('file.txt', 'w') as f:
    f.write(scraped_content)
"""

# 2. Write to a CSV file: You can save the scraped content as CSV file using Python's `csv` module.
"""import csv

with open('file.csv', 'w', newline='') as file:

writer = csv.writer(file)
writer.writerow(["Title", "Description"])
for i in range(len(titles)):
writer.writerow([titles[i], descriptions[i]])
"""

# 3. Write to a JSON file: You can save the scraped content as JSON file using Python's built-in `json` module.
"""
import json

with open('file.json', 'w') as f:
    json.dump(scraped_content, f)

"""
# 4. Write to a database: You can save the scraped content to a database such as MySQL, PostgreSQL, or MongoDB.
"""
import mysql.connector
# connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="database_name"
)

# create cursor object
cursor = mydb.cursor()

# insert data into table
sql = "INSERT INTO scraped_data (title, description) VALUES (%s, %s)"
for i in range(len(titles)):
    val = (titles[i], descriptions[i])
    cursor.execute(sql, val)

# commit changes and close connection
mydb.commit()
mydb.close()

"""

# =========================================================================================

"""get current window position"""
window_handle = driver.current_window_handle
driver.get("https://www.geeksforgeeks.org/python-programming-language/")

print(driver.get_window_position(windowHandle='current'))

