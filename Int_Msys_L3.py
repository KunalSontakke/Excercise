"""
1.verify the endpoint is working
2.visit URL
3.check for page is visible or not

4.check for 'create new user' button and click
5.create a list of usernames
6.iterate over all tge usernames present
5.enter the desired data(email,phone,number,address)
6.click on create_new_user button
7.assert successful message is visible for all successful creation
8.send POST request for all usernames
9.assert 201 in success status code

"""
import time

#
# def test_register_user():
#     try:
#         driver = webdriver.Chrome()
#         driver.get("https//:example.com")
#         assert driver.title == "example"
#
#         time.sleep(1)
#         create_new_user_btn = driver.find_element(By.XAPTH."//button[@id='textbox']")
#         create_new_user_btn.click()
#
#         name_txtbx = driver.find_element(By.ID,"name")
#         email_txtbx = driver.find_element(By.ID,"email")
#         address_txtbx = driver.find_element(By.ID,"city")
#
#         users = [{"name":"abc","email":"abc@,ail.com","address":"Pune"},
#                {"name":"pqr","email":"pqr@mail.com","address":"Naagpur"}]
#
#         for name in users[0]['name']:
#             name_txtbx.send_keys(name)
#         for email in users[0]['email']:
#             email_txtbx.send_keys(email)
#         for address in users[0]['address']:
#             address_txtbx.send_keys(address)
#
#         create_btn = driver.find_element(By.ID,"Btn")
#         create_btn.click()
#
#         success_msg = driver.find_element(By.ID,'text')
#         assert "user is created succesfuuly" in success_msg
#         for
#         response = requests.post(url,json=users,verify=True)
#         print(response.text)
#         assert 201 in response.status_code
#
#     except WebdriverException as e:
#         print(e)
#
#     except Exception as e:
#         print(e)
#
#     finally:
#         driver.close()
#
#
# import  pytest
#
# @pytest.fixture(params=["chrome","firefox"])
# def browser(request):
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#     elif request.param == "firefox":
#         dr
#
