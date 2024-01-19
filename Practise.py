import random
import string
def password_generator(length=12,upper_case=True,lower_case=True,digits=True):
    password = ""
    if upper_case:
        password += string.ascii_uppercase
    elif lower_case:
        password += string.ascii_uppercase
    elif digits:
        password += string.digits

    for i in range(length):
        password += password
