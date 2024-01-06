"""
1) Implicit wait,Explicit wait and time.sleep()
    Implicit wait is a setting applied globally to the WebDriver instance.
    It instructs the WebDriver to wait for a certain amount of time for an element to be present or become available before throwing a NoSuchElementException.
    The wait is applied automatically to all subsequent commands after it has been set, and it remains active for the entire lifespan of the WebDriver object.
    It is set using driver.implicitly_wait(time_in_seconds).



driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Sets an implicit wait of 10 seconds

Explicit Wait:

    Explicit wait is a targeted wait applied to specific elements with specific conditions.
    It allows you to wait for certain conditions (such as visibility, click ability, presence, etc.) to occur within a specified timeout period before performing further actions.
    It is more flexible and precise than implicit waits because it waits only for the specific condition to be satisfied.
    It is implemented using WebDriverWait along with Expected Conditions.

python

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "myElement"))
)

time.sleep():

    time.sleep() is a general-purpose Python function that causes the script to pause or sleep for a specified number of seconds.
    Unlike implicit and explicit waits, time.sleep() doesn’t consider any conditions or states of elements; it blindly pauses execution for the specified time.
    It's not recommended for use in Selenium automation testing as it causes unnecessary fixed delays and can make tests slower and less reliable.

python

    import time

    time.sleep(5)  # Pauses execution for 5 seconds

In summary:

    Implicit wait sets a global wait for elements throughout the WebDriver session.
    Explicit wait allows you to wait for specific conditions on specific elements.
    time.sleep() causes the script to pause for a fixed duration, irrespective of the element's state.

For efficient and reliable test automation, it's recommended to use Explicit waits over Implicit waits and avoid using time.sleep() wherever possible, favoring targeted waits based on conditions.


2) Exceptions in selenium
    NoSuchElementException:
        This exception is thrown when WebDriver is unable to locate an element in the DOM.
        It usually occurs when the specified element locator (such as ID, XPath, CSS selector, etc.) is incorrect or when the element is not present on the page.

    TimeoutException:
        TimeoutException is thrown when a command or action does not complete within the specified time limit.
        For example, it occurs when an element does not appear or become intractable within the expected timeout while using explicit waits.

    ElementNotVisibleException:
        This exception occurs when an element is present in the DOM but is not visible or intractable on the web page.
        It may occur due to the element being hidden, covered by another element, or not in the viewport.

    ElementNotIntractableException:
        ElementNotIntractableException is thrown when an element is present and visible but cannot be interacted with, such as clicking or sending keys.
        Reasons might include an element being disabled, readonly, or not in a state to accept interactions.

    StaleElementReferenceException:
        This exception occurs when an element is no longer attached to the DOM or has become stale since it was located.
        It typically happens when the DOM changes after the element is located, such as refreshing the page or navigating to a different page.

    WebDriverException:
        WebDriverException is a general exception for WebDriver-related issues that don’t fall into more specific exception categories.
        It can occur due to various reasons such as network issues, browser crashes, unexpected behavior, etc.

3) Stale Element Exception
4) Difference between Javascript Executor and Selenium API
5) Ancestor,Sibling,Parent in XPath
"""

# ======================================================================================================================
# Input :- "i am the input"
# Output:- "the input am i"

ip = "i am the input"

ip_spl = ip.split()
res = " ".join(ip_spl[2:]+ip_spl[-3:-5:-1])
print(res)
