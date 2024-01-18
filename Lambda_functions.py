#  """Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
#  also create a lambda function that multiplies argument x with argument y and prints the result."""
#
#  r = lambda x : x + 15
#  print(r(20))
#
#  r = lambda x,y : x + y
#  print(r(20,10))
#
# ======================================================================================================================
# """
# Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
# Sample Output:
# Double the number of 15 = 30
# Triple the number of 15 = 45
#
# """
#
# multi = lambda x,n : x * n
# print("double of number is ",multi(20,2))
#
# =====================================================================================================================
# """
# Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# lis = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# Sorting the List of Tuples:
# [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
# """
# lis = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
# lis.sort(key=lambda x:x[1])
# print(lis)

# ======================================================================================================================
# """
# Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# Sorting the List of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
#
# """
# phones = [{'make': 'Nokia', 'model': 216, 'color': 'Black'},
#           {'make': 'Mi Max', 'model': 2, 'color': 'Gold'},
#           {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
# phones.sort(key=lambda x : x['color'])
# print(phones)
#
# =====================================================================================================================
# """
# 5. Write a Python program to filter a list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Even numbers from the said list:
# [2, 4, 6, 8, 10]
# Odd numbers from the said list:
# [1, 3, 5, 7, 9]
#
# """
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = list(filter(lambda x : x % 2 == 0,lis))
# print(even)
# odd = list(filter(lambda x : x % 2 == 1,lis))
# print(odd)
#
# # ======================================================================================================================
# """
#  Write a Python program to square and cube every number in a given list of integers using Lambda.
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Square every number of the said list:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# Cube every number of the said list:
# [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
#
# """
# lis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# sqr = list(map(lambda x : x ** 2,lis))
# cube = list(map(lambda x : x ** 3,lis))
# print(sqr)
# print(cube)
#
# # =====================================================================================================================
# """
# Write a Python program to find if a given string starts with a given character using Lambda.
# Sample Output:
# True
# False
# """
# string = input("Enter input : ")
# letter = input("Enter starting letter: ")
# starts_with = lambda string,letter : True if string[0] == letter else False
# print(starts_with(string,letter))

# ======================================================================================================================
"""
Write a Python program to find the intersection of two given arrays using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
[1, 2, 4, 8, 9]
Intersection of the said arrays: [1, 2, 8, 9]

"""
lis1 = [1, 2, 3, 5, 7, 8, 9, 10]
lis2 = [1,2,4,8,9]

intersection = list(filter(lambda x: x in lis1,lis2))
print(intersection)

# =====================================================================================================================
"""
 Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
Original arrays:
[-1, 2, -3, 5, 7, 8, 9, -10]
Rearrange positive and negative numbers of the said array:
[2, 5, 7, 8, 9, -10, -3, -1]
"""
lis = [-1, 2, -3, 5, 7, 8, 9, -10]


result = sorted(lis, key = lambda i: 0 if i == 0 else -1 / i)
print("\nRearrange positive and negative numbers of the said array:")
print(result)

# =====================================================================================================================
"""
Write a Python program to count the even and odd numbers in a given array of integers using Lambda.
Original arrays:
[1, 2, 3, 5, 7, 8, 9, 10]
Number of even numbers in the above array: 3
Number of odd numbers in the above array: 5

"""
lis = [1, 2, 3, 5, 7, 8, 9, 10]
even = len(list(filter(lambda x: x % 2 == 0,lis)))
print(even)
odd = len(list(filter(lambda x : x % 2 ==1,lis)))
print(odd)

