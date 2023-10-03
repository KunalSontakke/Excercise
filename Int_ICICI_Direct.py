"""
1) Test cases in Current Project
2) Recursive Function
3) Web scrapping
4) Multithreading , Multitasking and Multiprocessing
5) How to copy the content from API request into Excel and Process it

"""


"""perform web scrapping using request module"""
import requests

read =requests.get("https://www.geeksforgeeks.org/python-programming-language/")

print(read.content)

"""write a python program to find factorial of number using recursive function"""

def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 0 or x == 1:
        return 1
    else:
        # recursive call to the function
        return (x * factorial(x-1))


print(factorial(5))

# =================================================================================================================
#
# string = input("Enter the string : ")
#
# rev_str = string[::-1]
#
# if string == rev_str:
#     print("this is palindrome")
# else:
#     print("this is not palindrome")
#

