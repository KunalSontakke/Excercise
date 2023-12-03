"""
1) what is Cookie
2) What is Cache
3) what to automate,when to automate,how to automate
4) difference between GET and POST
5) Can we send POST request using Query Parameter
6) Difference between PUT and Patch
7) Headers in API
8) How to Authenticate bearer token in API / how to send request to Authenticated Path
9) Abstraction
10) Polymorphism
11) Method Overloading
12) __init__ Constructor
13) Self keyword
14) Static Method and Instance method/cls
15) Call By reference / Call by Value
16) List and Tuple
17) Args and Kwargs
18) Decorators
19) page object Model
20) Implicitly wait

"""

"""input = [6,3,5,8,1]
output = [2,4,7]"""

inputs = [6, 3, 5, 8, 1]
result = []
for i in range(min(inputs), max(inputs)):
    if i not in inputs:
        result.append(i)
print(result)

# Immutable tuple
x = (1, 2, 3)
y = x
x = (4, 5, 6)
x = (6, 7, 8)

print("y is", y)
print("x is", x)

"""How to add cookie"""
"""what is cookie ?
-   A cookie is a small piece of data sent from a website and stored on the user’s computer. 
    Cookies also recognize users returning to a website and loading the previously stored information.
    Mainly, cookies store the user’s identity and track the user’s journey through the website’s pages. 
    WebDriver API provides a way to interact with cookies with built-in methods."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service("Drivers/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Navigate to website
driver.get("https://www.flipkart.com")

# create a cookie object
cookie = {"name": "flip_cookie",
          "value": "123456"}

# add cookie to the current session
driver.add_cookie(cookie)

# Refresh the page to apply the changes
driver.refresh()

# Now see added cookie in the browser's cookie storage

# ===============================================================
"""when to perform Automation

    Repetitive tests that run for multiple builds.
    Tests that tend to cause human error.
    Tests that require multiple data sets.
    Frequently used functionality that introduces high risk conditions.
    Tests that are impossible to perform manually.
    Tests that run on several different hardware or software platforms and configurations.
    Tests that take a lot of effort and time when manual testing.
    
"""


def main():
    print("Hi Interviewbit!")


if __name__ == "__main__":
    main()
