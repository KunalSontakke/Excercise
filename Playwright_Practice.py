import time

from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     #
#     context = browser.new_context(
#         viewport=None
#     )
#     context.tracing.start(screenshots=True,snapshots=True,title="webcheck",sources=True)
#
#     page = context.new_page()
#     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#
#     print(page.title())
#     print(page.url)
#
#     # find element
#     # fill
#     page.wait_for_selector("input[name='username']").fill("Admin")
#     page.locator("input[name='username']").press("Tab")
#
#     page.locator("input[name='password']").fill('admin123')
#
#     # click submit button
#     page.locator("button[type='submit']").click()
#
#     # click "Admin link"
#     page.locator("text='Admin'").click()
#
#     # Type Username
#     page.locator("//label[text()='Username']/following::input[contains(@class,'oxd-input')][1]").fill("Admin")
#
#     # Click the User Role dropdown
#     page.locator("//label[text()='User Role']/following::div[contains(@class,'oxd-select-text-input')][1]").click()
#
#     load_time =  page.evaluate("window.performance.timing.navigationStart")
#     print(load_time)
#
#     context.tracing.stop(path='trace.zip')
# with sync_playwright() as p:
#     request = p.request.new_context()
#
#     response = request.get('https://dog.ceo/api/breeds/image/random')
#     print(response.status)
#     print(type(response.text()))
#     print(type(response.json()))

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(viewport=None)
    page = context.new_page()

    page.goto('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')

    page.set_input_files(selector="input[type='file']",files='Data/screenshot.png')

    page.locator('//button[text()=" Alerts, Frames & Windows "]').click()
    page.get_by_role("link",name="Frames",exact=False).click()

    page.frame_locator('Iframe 1').locator('//button[text()="Menu"]').click()
    time.sleep(5)

    page.screenshot(path='Data/screenshot.png',type="png")
