"""
1) Project Overflow
2) Test Cases
3) Pytest Framework
4) Class
5) Polymorphism
6) func() in decorator in function
7) list and dictionary Comprehensions
8) List and Dictionary Difference
9)Map in python

"""
import math

""""
x = [1,2,3,4,5]
output= {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}

"""
x = [1, 2, 4, 4, 5]
Dict = {}
for i in x:
    Dict[i] = i
print(Dict)

# OR

dicti = {x: x for x in range(1, 6)}
print("dictionary elements are", dicti)

# ===========================================================================================================
"""
x = [1,2,3,4,5]
y = [4,5,6,7,8]
output = {1:4,2:5,3:6,4:7,5:8}"""

# Initializing lists
x = [1, 2, 3, 4, 5]
y = [4, 5, 6, 7, 8]


# Using dictionary comprehension to create dictionary
output = {x[i]: y[i] for i in range(len(x))}


# ==========================================================================
"""Decorators"""
"""what is func() in decorator
- In the given decorator code, `func()` is a reference to the function that will be passed as an argument to the `sqr_num()`
  decorator. It means that when we apply the `sqr_num()` decorator to a function, 
  that function will be decorated such that its return value will be squared. 
  The decorator `sqr_num()` creates a new function `wrapper()` which wraps the original function, 
  and computes the square of its return value. When the decorated function is called, `wrapper()` is called instead, 
  which in turn calls the original function with the arguments passed to it, and then squares the result."""
#
#
# def sqr_num(func):
#     def wrapper():
#         x = func()
#         return x * x
#
#     return wrapper
#
#
# @sqr_num
# def print_num():
#     return 10
#
#
# print(print_num())

# =============================================================
"""what is Map function ?
- The map in Python takes a function and an iterable/iterables. 
  It loops over each item of an iterable and applies the transformation function to it.
  Then, it returns a map object that stores the value of the transformed item. 
  The input function can be any callable function, including built-in functions.
  
  syntax = map(function,sequence)
  
"""

# number = [1, 2, 3, 4, 5]
#
#
# def sqr_num(i):
#     return i * i


# map function with function
# op = map(sqr_num, number)
# print(list(op))
#
# # map with module level function
# outp = map(math.sqrt, number)
# print(list(outp))
#
# # map with lambda function
# outp1 = map(lambda i: i * 2, number)
# print(list(outp1))
#
# # 3) Set Comprehensions
# # set = {set for set in ["a","b","c","a","b","b","c"]}
# # print(set)
# alpha = {alpha for alpha in ["a", "a", "b", "c", "d", "d"]}
# print(alpha)

"""what is filter function ?
- The filter() method filters the given sequence with the help of a function 
  that tests each element in the sequence to be true or not.
  
  syntax = filter(function, sequence)
"""


# function that filters vowels
# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
#         return False


# sequence
# sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
#
# # using filter function
# filtered = filter(fun, sequence)
#
# print('The filtered letters are:')
# for s in filtered:
#     print(s)
#
#
