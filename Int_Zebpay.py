"""
1. How to create cookie for login and if multiple login cookies then store there into dictionary.
"""
import requests

# Perform login and get cookies
login_url = 'https://example.com/login'  # Replace with your login URL
credentials = {'username': 'your_username', 'password': 'your_password'}  # Replace with actual credentials

# Perform the login request
response = requests.post(login_url, data=credentials)

# Get the cookies from the response
cookies = response.cookies

# Store the cookies in a variable or container (e.g., list or dictionary)
# For a single cookie
single_cookie = cookies.get('cookie_name')

# If multiple cookies are present, you can store them in a dictionary
all_cookies = {cookie.name: cookie.value for cookie in cookies}

# =====================================================================================================================

# """
# +12,100
#
# """
# inp = "+12,100"
# res = ""
# for i in inp:
#     if i.isdigit():
#         res += i
# print(res)
#
#
# # =====================
# """
# inp = 12100
# out = 120
# """
# inp1 = "12100"
# out = ""
# for i in inp1:
#     if i not in out:
#         out += i
# print(out)
#
# """
# 1
# 12
# 123
# 1234
# 12345
#
# """
# for i in range(6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()
#


