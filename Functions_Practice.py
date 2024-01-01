# # Define a function that accepts 2 values and return its sum, subtraction and multiplication.
# #
# # Hint
# # Input:
# # Enter value of a = 7
# # Enter value of b = 5
# #
# # Expected output
# # Sum is = 12
# # Sub is = 2
# # Multiplication is = 35
#
# def function1(a,b):
#     sum = a + b
#     print("Sum is",sum)
#
#     subtraction = a - b
#     print("Subtraction is",subtraction)
#
#     multiplication = a * b
#     print("multiplication",multiplication)
#
#
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# function1(a,b)
#
# # ===========================================================================
# # Define a function that accepts roll number and returns whether the student is present or absent.

# # Hint
# # Use a list to store sample roll. no.
# # Get input from a user and check if the number
# # exist in the list or not, if exists return present
# # else return absent
#
# def attendance_status(roll_no):
#     roll_list = [1,2,3,4,6,7,8,9,11,12,13,14,15,18,20,22,23,24,25,26,27,30]
#
#     if roll_no in roll_list:
#         print(f"{roll_no} is present")
#
#     else:
#         print(f"{roll_no} is absent")
#
#
# roll_no = int(input("Enter roll no to check: "))
# attendance_status(roll_no)

# =====================================================================================================================
# Write a Python function to find the maximum of three numbers.
# def find_max_num(a,b,c):
#     """
#
#     :param a:
#     :param b:
#     :param c:
#     :return:maximum number from three numbers
#
#     """
#     if a > b and a > c:
#         return a
#     if b > a and b > c:
#         return b
#     if c > a and c > a:
#         return c
#
#
# print(find_max_num(76,123,87))

# ====================================================================================================================
# Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20

# def sum_nums(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
#
# sum_nums(8,2,3,0,7)

# ======================================================================================================================
# Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
# Note : A prime number (or a prime) is a natural number greater than 1 and
# that has no positive divisors other than 1 and itself.
# def find_number(n):
#     for i in range(2,n):
#         if n % i ==0:
#             print("This number is not prime")
#             break
#     else:
#         print("This is number is prime")

# find_number(7)

"""12. Write a Python function that checks whether a passed string is a palindrome or not. """


def check_palindrome(string):
    if string == string[::-1]:
        print(f"{string} is palindrome")
    else:
        print(f"{string} is not palindrome")


check_palindrome("madam")

# ==================================================================================================================
"""Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated
 sequence after sorting them alphabetically.

Sample Items : green-red-yellow-black-white
Expected Result : black-green-red-white-yellow"""

# def reverse_strings(inp):
#     items = [item for item in inp.split("-")]
#     print(items)

    # print("-".join(items))

# inp = input("Enter the items : ")
# reverse_strings(inp)

# ===================================================================================================================
""" Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included)."""
def create_list():
    sqres = [i**2 for i in range(1,31)]
    return sqres


print(create_list())

# ======================================================================================================================
"""Write a Python program to create a chain of function decorators (bold, italic, underline etc.)."""
# def make_bold(func):
#     def wrapper():
#         return "<b>" + func() + "</b>"
#     return wrapper
#
# def make_italic(func):
#     def wrapper():
#         return "<i>" + func() + "</i>"
#     return wrapper
#
# def make_underline(func):
#     def wrapper():
#         return "<u>" + func() + "</u>"
#     return wrapper
#
# @make_bold
# @make_italic
# @make_underline
# def show_something():
#     return "something"

# print(show_something())

# ====================================================================================================================

