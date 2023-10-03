arr_a = [20, 30, 50]

arr_b = [30, 50, 20]

# for i in range(0,len(arr_a)):
#     for j in range(0,len(arr_b)):
#         if arr_a[i] == arr_b[j]:
#               break
# print("all values are equal")

import requests

response = requests.get("https://anapioficeandfire.com/api")

print(response.text)

if response.status_code == 200:
    print("Succesfull.....!!!!!")

"""
card no,CVV,card no(16 digit)
submit button
OTP 5 digit
enter 5 digit OTP
submit button
"""

"""
1) CVV number should not be reused 
2) OTP cannot be reused again
3) card no should not be lesser than 16 digits
4) OTP can not be reused after 3 minutes

"""
