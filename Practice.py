# x = 2
#
# def func():
#     x = 3
#     print(x)
# print(x)
# func()
#
# def split_fun(func):
#     def inner():
#         x = func()
#         str_spl = x.split()
#         return str_spl
#     return inner
#
# @split_fun
# def ret_str():
#     return "hello world"
#
# print(ret_str())
#
# def capit_func(func):
#     def inner(arg_1,arg_2):
#         arg_1 = arg_1.capitalize()
#         arg_2 = arg_2.capitalize()
#         str_cap = func(arg_1,arg_2)
#         return str_cap
#     return inner
#
# @capit_func
# def name_cap(name1,name2):
#     return "Hi!"+name1,"Hello!"+name2
#
# print(name_cap("kunal","shruti"))
#
#
# # ========================================================================================
# Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34.
#
# inp = int(input("Enter the number : "))
#
# if inp > 4**4 :
#     if inp % 34 == 4:
#         print(True)
#     else:
#         print(False)


# =============================================================================================
#  Write a Python program to find the length of a given list of non-empty strings.
# Input:
# inp = ['cat', 'car', 'fear', 'center']
# # Output:
# # [3, 3, 4, 6]
# length = []
# for i in inp:
#     length.append(len(i))
# print(length)
#
# length1 = [len(s) for s in inp]
# print(length1)
#
# =================================================================================================
# Write a Python program to find the longest string in a given list of strings.
# Input:
# inp = ['cat', 'car', 'fear', 'center']
# # Output:
# # center
# longest = ""
# for i in inp:
#     if len(i) > len(longest):
#         longest = i
# print(i)

# =============================================================================================
# Write a Python program to sort the numbers in a given list by the sum of their digits.
inp = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# Output:
# [10, 11, 20, 12, 13, 14, 15, 16, 17, 18, 19]


def digit_sum(n):
    return sum(int(digit) for digit in str(n))


def sort_by_digit_sum(numbers):
    sorted_numbers = sorted(numbers, key=digit_sum)
    return sorted_numbers


input_list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sorted_list = sort_by_digit_sum(input_list)
print(sorted_list)

# =============================================================================


