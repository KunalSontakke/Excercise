"""
1) Smoke and Regression
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

