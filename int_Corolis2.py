"""
1) Smoke and Regression
Smoke Testing:

Smoke testing is a testing technique that is used to check the basic functionalityof a software application or
system after a build or release.This testing is done to ensure that the build is stable enough for further testing.
Smoke testing involves a quick and shallow check of the software application to verify that it is functioning properly
and that there are no critical defects that could prevent further testing.Smoke testing is typically performed by
testers or developers before any detailed testing is performed.

Sanity Testing :
Sanity Testing: Sanity testing is a testing technique that is used to check that specific functionality or components
of a software application are working as expected after making changes or fixing defects.
The main objective of sanity testing is to verify that the changes made to the application have not introduced new defects
or issues in the specific functionality or components.
Sanity testing is typically performed after regression testing and is focused on specific areas of the application

Scope:
Smoke testing covers the entire system or application, whereas sanity testing is focused on specific functionality or components.


Timing:
Smoke testing is typically performed after a new build or release, while sanity testing is performed after making changes or fixing defects.

Depth:
Smoke testing is a shallow check of the software application to verify that there are no critical defects,
while sanity testing is a more detailed check of specific functionality or components of the application

Regression Testing:
is the process of testing the modified parts of the code and the parts that might get affected due to the modifications
to ensure that no new errors have been introduced in the software after the modifications have been made.
Regression means the return of something and in the software field, it refers to the return of a bug.

Techniques for the selection of Test cases for Regression Testing:

Select all test cases: In this technique, all the test cases are selected from the already existing test suite.
It is the simplest and safest technique but not much efficient.

Select test cases randomly: In this technique, test cases are selected randomly from the existing test-suite,
but it is only useful if all the test cases are equally good in their fault detection capability which is very rare.
Hence, it is not used in most of the cases.

Select modification traversing test cases: In this technique, only those test cases are selected which covers and tests
the modified portions of the source code the parts which are affected by these modifications.

Select higher priority test cases: In this technique, priority codes are assigned to each test case of the test suite
based upon their bug detection capability, customer requirements, etc. After assigning the priority codes,
test cases with the highest priorities are selected for the process of regression testing.
The test case with the highest priority has the highest rank.
For example, test case with priority code 2 is less important than test case with priority code 1.

2) Iterators
"""


# str = "great is india"
#
# lis = str.split()
# op = lis[::-1]
# print(op)
# result = " ".join(op)
# print(result)
#
# number = int(input("Enter the number"))
# temp =number
# rever = 0
#
# while number > 0:
#     digit = number % 10
#     rever = rever * 10 + digit
#     number = number // 10
# if temp == rever:
#     print("this number is palindrome")
# else:
#     print("this is not palindrome")



# list = [1,2,3,4,5,6,7]
#
# list.sort()
#
# print("the second element of list is ",list[-2])
#
#
# list = [23,45,5,34,76,56]
#
# list.remove(max(list))
#
# print(max(list))


# """to find 2nd max element of list"""
#
# list = [23,45,67,2,3,4,5]
# print(list)
# # 1st approach
# # removing maximum element

# output = list.remove(max(list))

# print(max(list))

# # 2nd approach sorting the list
# Output = list.sort()

# print(max(list))


# ======================================================================================================================
# """Calculate the sum of all numbers from 1 to a given number"""
#
# n = int(input("Enter the Number"))
# sum = 0
# for i in range(1,n+1):
#     sum = sum + i
# print(f"the sum of numbers upto {n} is :",sum)

# ===========================================================================================================================
# """Write a program to print multiplication table of a given number"""
# num = int(input("enter the number"))
#
# for i in range(1,11):
#      print(f"{num} x {i} :",num * i )



# ======================================================================================================================

# def triangle_pattern(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print("* " ,end= "")
#         print("\n")
#
#     for i in range(1,n+1):
#         print(" " * (n-i) + " *" * i)
#
#
# n = int(input("enter rows"))
# triangle_pattern(n)

