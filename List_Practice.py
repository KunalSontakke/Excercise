# """"
#     Exercise 1: Reverse a list in Python
#     Exercise 2: Concatenate two lists index-wise
#     Exercise 3: Turn every item of a list into its square
#     Exercise 4: Concatenate two lists in the following order
#     Exercise 5: Iterate both lists simultaneously
#     Exercise 6: Remove empty strings from the list of strings
#     Exercise 7: Add new item to list after a specified item
#     Exercise 8: Extend nested list by adding the sublist
#     Exercise 9: Replace list’s item with new value if found
#     Exercise 10: Remove all occurrences of a specific item from a list.
# """
#
# # Exercise 1: Reverse a list in Python
# lis = [12, 45, 23, 64, 73, 87, 98]
# print("original list is.", lis)
#
# print("reversed list is,", lis[::-1])
#
# # =================================================================================================
# # Exercise 2: Concatenate two lists index - wise
#
# lis1 = ["my", "name", "is", "kunal"]
# lis2 = ["and", "I", "live", "in", "Nagpur"]
#
# print(lis1 + lis2)
#
# # =================================================================================================
# # Exercise 3: Turn every item of a list into its square
# lis3 = [1, 2, 3, 4, 5, 6]
#
# # 1 for loop
# sq = []
# for i in range(1, len(lis3) + 1):
#     sq.append(i ** 2)
# print(sq)
#
# # 2 list comprehension
# sqr = [i ** 2 for i in range(1, len(lis3) + 1)]
# print(sqr)
#
#  =====================================================================================================================
#  Exercise 4: Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
#
#  Expected output:
#
# var = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
#
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# #
# op_list = [i + j for i in list1 for j in list2]
# print(op_list)
#
# op_lis = []
# for i in list1:
#     for j in list2:
#         op_lis.append(i + j)
# print(op_lis)
#
# # ========================================================================================
# Exercise 5: Iterate both lists simultaneously
# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# out_list = []
# for i,j in zip(list1,list2[::-1]):
#     print(i,j)
#
#
# ==================================================================================================
#
# Exercise 6: Remove empty strings from the list of strings
# list_a = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# re_list = [i for i in list_a if i != ""]
# print(re_list)
#
# =================================================================================================
# # Exercise 7: Add new item to list after a specified item
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
#
# Expected_output = [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
#
# list1[2][2].append(7000)
# print(list1)
# #
# # ================================================================================================
# Exercise 8: Extend nested list by adding the sublist
# list_b = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#
# # sub list to add
# sub_list = ["h", "i", "j"]
#
# # Expected_Output=['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
# list_b[2][1][2].extend(sub_list)
# print(list_b)
#
# #  Exercise 9: Replace list’s item with new value if found
# # You have given a Python list. Write a program to find value 20 in the list,
# # and if it is present, replace it with 200. Only update the first occurrence of an item.
#
#
# list_c = [5, 10, 15, 20, 25, 50, 20]
# output = [5, 10, 15, 200, 25, 50, 20]
# index = list_c.index(20)
# list_c[index] = 200
# print(list_c)
#
# # =============================================================================================
# # Exercise 10: Remove all occurrences of a specific item from a list.
# list_d = [5, 20, 15, 20, 25, 50, 20]
# expected_output = [5, 15, 25, 50]
# res_list = [i for i in list_d if i != 20]
# # print(res_list)
# #
#
# # Write a program to print all the elements of a list in single line.
# #
# # Hint
# num = [23, 24, 54, 34]
# #
# # Expected output
# # 23  24  54  34
# for i in num:
#     print(i, end=" ")
#
# # ===============================================================================================
#
# # Python program to append an element to a list.
# #
# # Hint
# # Given_num = [23, 45, 67, 8, 9]
# # # Input: Enter the item to insert: study
# # #
# # # Expected output
# # # Result: [23,45,67,8,9, ‘study’]
# #
# # inp = input("enter the item to insert : ")
# # Given_num.append(inp)
# # print(Given_num)
# # Given_num.remove(inp)
#
# # =========================================================================
#
# # Exercise 8: Write a program to display those items from a list that is divisible by 5.
#
# # Hint
# num5 = [3, 5, 7, 9, 23, 15]
#
# # Expected output
# # Result: 5  15
#
# for i in num5:
#     if i % 5 == 0:
#         print(i, end=" ")
#
# # ===============================================================================
# # Exercise 8: Write a program to sum all the elements of a list.
# #
# # Hint
num6 = [2, 3, 2, 4, 7, 8]
# #
# # Expected output
# # Sum of list items 26
#
# Sum = 0
# for i in num6:
#     Sum = Sum + i
#
# print("\nSum of items in list is", Sum)


# ===================================================================================================
# #  Write a program to get the maximum number from a list.
#
# # Hint
# num7 = [2, 3, 2, 4, 7, 8]
#
# # Expected output
# # Maximum number in list items is 8
# print("Max number in list items", max(num7))
#
# # ===============================================================================
# #  Write a program in Python to remove duplicate items from a list.
# #
# # Hint
# num8 = [2, 3, 4, 5, 2, 6, 3, 2]
# #
# # Expected output
# # Result: [2, 3, 4, 5, 6]
#
# res = []
# for i in num8:
#     if i not in res:
#         res.append(i)
# print(res)

# OR

# unique_nums = []
# [unique_nums.append(num) for num in num8 if num not in unique_nums]
# print(unique_nums)
#
# # ===============================================================================
# #  Write a program in Python to choose a random item from a list.
# #
# # Hint
# num9 = [2, 3, 4, 5, 6, 8, 9]
# #
# # Expected output
# # Result: 6
#
# import random
#
# result = random.choice(num9)
# print("random number from list is",result)
#
#
# # ================================================================================
# # Write a program to append data of the second list to the first list.
#
# # Hint
# list1 = [23, 24, 25, 26]
# list2 = [27, 28, 29, 30]
#
# # Expected output
# # Result:
# # [23, 24, 25, 26, 27, 28, 29, 30]
# list1.extend(list2)
# print(list1)
#
# # ================================================================================
# # Write a program in Python to filter odd and even number from a list.
# #
# # Hint
# Given = [2, 23, 24, 51, 46, 67]
#
# # Expected output
# # Even [2, 24, 46] Odd [23, 51, 67]
#
# even = []
# odd = []
# for i in Given:
#     if i % 2 ==0:
#         even.append(i)
#
#     else:
#         odd.append(i)
#
# print("Even",even,"","Odd",odd)
#
# # ====================================================================================
# # Write a Python program to create multiple lists.
# # output = {'1': [], '2': [], '3': [], '4': [], '5': [], '6': [], '7': [], '8': [], '9': [], '10': [], '11': [], '12':
# # [], '13': [], '14': [], '15': [], '16': [], '17': [], '18': [], '19': [], '20': []}
#
# dic = {i : [] for i in range(1,21)}
# print(dic)
#
# # ================================================================================
# # # Write a Python program to convert a list of multiple integers into a single integer.
# # Sample_list = [11, 33, 50]
# # # Expected Output: 113350
# # for i in Sample_list:
# #     print(i,end="")
# #
# # # . Write a Python program to change the position of every n-th value to the (n+1)th in a list.
# # Sample_list1= [0,1,2,3,4,5]
# # # Expected Output= [1, 0, 3, 2, 5, 4]
# # Sample_list1[0::2],Sample_list1[1::2] = Sample_list1[1::2],Sample_list1[0::2]
# #
# # print(Sample_list1)
#
# # ===================================================================================================
# Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# Sample_list3 = ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
# n = int(input("Enter the range : "))
# op = [['p'+str(i),'q'+str(i)] for i in range(1,n+1)]
#
# print(op)
#
# # ==================================================================================================
# #  Write a Python program to find missing and additional values in two lists.
# # Sample data : Missing values in second list: b,a,c
# # Additional values in second list: g,h
#
# # list1 = ['a','b','c','d','e','f']
# # list2 = ['d','e','f','g','h']
# #
# # oplis1 = []
# # oplis2 = []
# #
# # for i in list1:
# #     if i not in list2:
# #         oplis1.append(i)
# # for i in oplis1:
# #     print("missing values in second list",i,end=",")
# #
# # for i in list2:
# #     if i not in list1:
# #         oplis2.append(i)
# # print("\n")
# # for i in oplis2:
# #     print("missing values in first list",i,end=",")
#
# # =============================================================================================
# #
# # color = [("Black", "#000000", "rgb(0, 0, 0)"), ("Red", "#FF0000", "rgb(255, 0, 0)"),
# #          ("Yellow", "#FFFF00", "rgb(255, 255, 0)")]
# # # output =  ('Black', '#000000', 'rgb(0, 0, 0)')
# # # ('Red', '#FF0000', 'rgb(255, 0, 0)')
# # # ('Yellow', '#FFFF00', 'rgb(255, 255, 0)')
# #
# # for i in range(0,len(color)):
# #     print(color[i])
#
#
# # =============================================================================================
# # Write a Python program to generate groups of five consecutive numbers in a list.
# # [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
#
# # listop = [[5*i +j for j in range(1,6)] for i in range(5)]
# # print(listop)
#
# # ============================================================================================
# # Write a Python program to convert a pair of values into a sorted unique array
# OriginalList = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
# # Sorted Unique Data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Data = [i for i in OriginalList]
#
# print(Data)
#
# # ========================================================================================
# # Write a Python program to check if a list is empty or not.
# # lis = []
# # if len(lis) < 1:
# #     print("list is empty")
# # else:
# #     print("list is valid")
#
# # ==========================================================================================
# # Write a Python program to convert a pair of values into a sorted unique array.
# # Original_List=  [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]
# # # Sorted Unique Data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# # sin = []
# # for i in Original_List:
# #     if i not in sin:
# #         sin.append(i)
# # print(sin)
#
# # =========================================================================================
#
# # Write a Python program to insert an element before each element of a list.
# # colors = ['Red', 'Green', 'Black']
# # Original List:  ['c', 'Red', 'c', 'Green', 'c', 'Black']
#
# #
# # def add_prefix(input_list, prefix):
# #     output_list = [prefix, *input_list, prefix]  # Adding the prefix to the beginning and end
# #     return output_list
# #
# #
# # input_list = ['Red', 'Green', 'Black']
# # output_list = add_prefix(input_list, 'c')
# # print("Input List:", input_list)
# # print("Output List:", output_list)
#
# # ==================================================================================================
#
# # # Write a Python program to print nested lists (each list on a new line) using the print() function
# # colors = [['Red'], ['Green'], ['Black']]
# # # output = ['Red']
# # # ['Green']
# # # ['Black']
# #
# # for i in colors:
# #     print(i)
#
# # ==================================================================================================
# # color_name = ["Black", "Red", "Maroon", "Yellow"],
# # color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
#
# # Expected Output: [{'color_name': 'Black', 'color_code': '#000000'},
# # {'color_name': 'Red', 'color_code': '#FF0000'},
# # {'color_name': 'Maroon', 'color_code': '#800000'},
# # {'color_name': 'Yellow', 'color_code': '#FFFF00'}]
#
#
# # print([{'color_name': name, 'color_code': code} for name, code in zip(color_name, color_code)])
#
#
# # ==================================================================================================
# # Write a Python program to split a list every Nth element
#
# # C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# #
# # [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
#
# # out = []
#
#  for i in range(3):
#      out.append(C[i::3])
#
#  print(out)
#
# =========================================================================
# Write a Python program to move all zero digits to the end of a given list of numbers.
# Expected output:
# inp_list=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# Move all zero digits to end of the said list of numbers:
# oup_list = [3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# oup_list = []
#
# for i in inp_list:
#     if i !=0:
#         oup_list.append(i)
# for i in range(inp_list.count(0)):
#     oup_list.append(0)
# print(oup_list)
#

# ===========================================================================================================
# Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# inp = [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]
# print(max(inp,key=sum))

# ===========================================================================================================
# Write a Python program to extend a list without appending.
# data1 = [10, 20, 30]
# data2 = [40, 50, 60]
# # Expected output : [40, 50, 60, 10, 20, 30]
#
# print(data2 + data1)

# ==========================================================================================================
# Write a Python program to remove duplicates from a list of lists.
# data =[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# # New List : [[10, 20], [30, 56, 25], [33], [40]]
# op = []
# for i in data:
#     if i not in op:
#         op.append(i)
# print(op)

# =========================================================================================================
# Write a Python program to find items starting with a specific character from a list.
# Expected Output:

# data = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# Items start with a from the said list:
# ['abcd', 'abc', 'acjd']
# Items start with d from the said list:
# ['dagfa']
# Items start with w from the said list:
import random

[]
#
# item = input("Enter item first letter : ")
# for i in data:
#     if item == i[0]:
#         print(i)
#     else:
#         print([])
#         break

# ============================================================================================================
# Write a Python program to flatten a given nested list structure.
# data = [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# Flatten list:
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
# op = []
# for i in data:
#     if isinstance(i,list):
#         op.extend(i)
#
#     else:
#         op.append(i)
# print(op)

# ======================================================================================================================
# Write a Python program to split a given list into two parts where the length of the first part of the list is given.
# Original list:
# data = [1, 1, 2, 3, 4, 4, 5, 1]
# Length of the first part of the list: 3
# Split the said list into two parts:
# ([1, 1, 2], [3, 4, 4, 5, 1]
# index = int(input("Enter the length : "))
# print(data[:index] , data[index:])

# =====================================================================================================================
# Write a Python program to remove duplicates from a list of lists.
#
# Original List [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List [[10, 20], [30, 56, 25], [33], [40]]

# lis = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# res = []
# for i in lis:
#     if i not in res:
#         res.append(i)
#
# print(res)

# ======================================================================================================================

#  Write a Python program to find items starting with a specific character from a list.
# Expected Output:
# Items start with a from the said list:a
# ['abcd', 'abc', 'acjd']
# Original list:
# ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']

# lis = ['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# ind = input("enter the first letter : ")
# res = []
# for i in lis:
#     if i[0] == ind:
#         res.append(i)
# print(res)

# =====================================================================================================================
# Write a Python program to remove consecutive (following each other continuously) duplicates (elements) from given list
# Original list:
# [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# After removing consecutive duplicates:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

# lis = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# res = []
# for i in range(0, len(lis)):
#     if lis[i] != lis[i - 1]:
#         res.append(lis[i])
# print(res)


# ====================================================================================================================
# Write a Python program to remove the K'th element from a given list, and print the updated list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After removing an element at the kth position of the said list:
# [1, 1, 3, 4, 4, 5, 1]

# lis = [1, 1, 2, 3, 4, 4, 5, 1]
# ind = int(input("Enter element to remove from list : "))
# lis.pop(ind)
# print(lis)

# =====================================================================================================================
# Write a Python program to insert an element at a specified position into a given list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# After inserting an element at kth position in the said list:
# [1, 1, 12, 2, 3, 4, 4, 5, 1]

# lis = [1, 1, 2, 3, 4, 4, 5, 1]
# ind = int(input("Enter the position :"))
# element = input("Enter the element ")
# lis.insert(ind,element)
# print(lis)

# =====================================================================================================================
#  Write a Python program to extract a given number of randomly selected elements from a given list.
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# Selected 3 random numbers of the above list:
# [4, 4, 1]

# import random
#
# lis = [1, 1, 2, 3, 4, 4, 5, 1]
# res = []
# while len(res) < 3:
#     res.append(random.choice(lis))
#
# print(res)

# =====================================================================================================================
# Write a Python program to round every number in a given list of numbers
# and print the total sum multiplied by the length of the list.
# Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]

# lis = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# res = []
# for i in lis:
#     res.append(round(i))
# sum = 0
# for i in res:
#     sum = sum + i
#     add = sum * len(res)
# print(add)

# =====================================================================================================================
# Write a Python program to create a multidimensional list (lists of lists) with zeros.
# nums = []
# for i in range(3):
#     nums.append([])
#     for j in range(2):
#         nums[i].append(0)
# print(nums)
#
# ========================================================================================================================
# Write a Python program to create a 3X3 grid with numbers.
# 3X3 grid with numbers:
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# nums = []
# for i in range(3):
#     nums.append([])
#     for j in range(1,4):
#         nums[i].append(j)
# print(nums)

# =====================================================================================================================

# Write a Python program to count the number of lists in a given list of lists.
# Original list:
# [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# Number of lists in said list of lists:
# 4

# ip = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# count = 0
# for i in ip:
#     count += 1
# print("Number of lists in said list of lists",count)

# =====================================================================================================================
# Write a Python program to count the number of sublists that contain a particular element.
# Original list:
# [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# Count 1 in the said list:
# 3
# Count 7 in the said list:
# 2
# Original list:
# [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# Count 'A' in the said list:
# 3
# Count 'E' in the said list:
# 1

# lis = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]

# element = int(input("Enter the element :"))
# count = 0
# for i in lis:
#     if element in i:
#         count = count + 1
# print(f"count of {element} is",count)

# =============================================================================================
# Write a Python program to sort a given list of lists by length and value.
# Original list:
# [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# Sort the list of lists by length and value:
# [[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]
# inp = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# inp.sort()
# inp.sort(key=len)

# print(inp)

# ====================================================================================================================
# Write a Python program to extract common index elements from more than one given list.
# Original lists:
# a = [1, 1, 3, 4, 5, 6, 7]
# b = [0, 1, 2, 3, 4, 5, 7]
# c = [0, 1, 2, 3, 4, 5, 7]
# # Common index elements of the said lists:
# # output = [1, 7]
#
# out = [a[i] for i in range(len(a)) if a[i] == b[i] == c[i]]
# print(out)

# ======================================================================================================================
# Write a Python program to extract specified size of strings from a give list of string values.
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# length of the string to extract:
# 8
# After extracting strings of specified length from the said list:
# ['practice', 'solution']

# inp = ['Python', 'list', 'exercises', 'practice', 'solution']
# sets = []
# length = int(input("Enter the length of element to extract : "))
#
# for i in inp:
#     if length == len(i):
#         sets.append(i)
# print(sets)
#

# ======================================================================================================================
#  Write a Python program to extract specified number of elements from given list,which follows each other continuously.
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# Extract 2 number of elements from the said list which follows each other continuously:
# [1, 4]
# Original lists:
# [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]
# Extract 4 number of elements from the said list which follows each other continuously:
# [4]

# inp = [1, 1, 3, 4, 4, 5, 6, 7]
#
# num_count = int(input("Enter the counts of numbers : "))
# count = 1
# res = []
#
# for i in range(1, len(inp)):
#     if inp[i] == inp[i - 1]:
#         count = count + 1
#     else:
#         count = 1
#
#     if count == num_count:
#         res = inp[i - num_count + 1:i + 1]
#         break
#
# print(res)

# ======================================================================================================================
# Write a Python program to compute average of two given lists.
# Original list:
# [1, 1, 3, 4, 4, 5, 6, 7]
# [0, 1, 2, 3, 4, 4, 5, 7, 8]
# Average of two lists:
# 3.823529411764706
# lis1 = [1, 1, 3, 4, 4, 5, 6, 7]
# lis2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

# sum1 = sum(lis1)
# sum2 = sum(lis2)
# for i in lis1:
#     sum1 += i
# for i in lis2:
#     sum2 += i

# print((sum1+sum2)/(len(lis1)+len(lis2)))

# ======================================================================================================================
# Write a Python program to count integers in a given mixed list.
# Original list:
# [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# Number of integers in the said mixed list:
# 6
# inp = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22,34]
# count = 0
# for i in inp:
#     if isinstance(i,int):
#         count += 1
# print(count)
#

# ======================================================================================================================
# Write a Python program to remove a specified column from a given nested list.
# Original Nested list:
# [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# After removing 1st column:
# [[2, 3], [4, 5], [1, 1]]
# Original Nested list:
# [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
# After removing 3rd column:
# [[1, 2], [-2, 4], [1, -1]]

# inp = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
# column_no = int(input("Enter the column number to remove"))
# while column_no < len(inp):
#     for i in range(len(inp)):
#         if column_no == i:
#             inp.pop(i)
#     print(inp)
#
# try:
#     num = input("Enter the input : ")
#     if num.isdigit():
#         print("This is digit")
#     else:
#         raise ValueError("Input is  not a digit")
#
# except Exception as e:
#     print("Error Occurred",e)
# except ValueError as e:
#     print(e)
#
# inp = [1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1]
#
# # Initialize variables
# current_streak = 0
# max_streak = 0
#
# for num in inp:
#     if num == 1:
#         current_streak += 1
#         if current_streak > max_streak:
#             max_streak = current_streak
#     else:
#         current_streak = 0
#
# print("Count of consecutive 1's:", max_streak)

# ======================================================================================================================
"""Write a Python program to scramble the letters of a string in a given list.
Original list:
['Python', 'list', 'exercises', 'practice', 'solution']
After scrambling the letters of the strings of the said list:
['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']"""

# inp = ['Python', 'list', 'exercises', 'practice', 'solution']
#
# from random import shuffle
#
# scrambled_word_list = random.sample(inp,len(inp))
# scrambled_word = "".join(scrambled_word_list)
# res = []
# for word in inp:
#     res.append(scrambled_word)
# print(res)

# ======================================================================================================================
"""
Write a Python Program to count unique values inside a list

Sample Output

[10, 20, 30, 50, 80, 70, 70, 80, 10]

No of Unique Items in List : 6

"""
# inp = [10, 20, 30, 50, 80, 70, 70, 80, 10]
# res = []
# count = 0
# for i in inp:
#     if i not in res:
#         res.append(i)
#         count += 1
#
# print("No of Unique Items in List",count)

# OR
# Set = set(inp)
# print("No of Unique Items in List ",len(Set))

# ======================================================================================================================
"""
 Write a Python Program to Extract elements with Frequency greater than K

Sample Output
[4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
"""

# inp = [4, 6, 4, 3, 3, 4, 3, 7, 8, 8]
# freq = int(input("Enter the frequency : "))
#
# for i in inp:
#     if inp.count(i) > freq:
#         print(i,end=",")

# ======================================================================================================================
"""
 Write a Python Program to Test if List contains elements in Range

Sample Output

[4, 5, 6, 7, 3, 9]

Does list contain all elements in range : True

"""
# inp = [4, 5, 6, 7, 3, 9]
# start = int(input("Enter the starting number"))
# end = int(input("Enter the ending number"))
#
# if start < min(inp) or end > max(inp):
#     print("False")
# else:
#     print("True")
#

# =====================================================================================================================
"""
Write a Python program to check if the list contains three consecutive common numbers in Python

Sample Output

[18, 18, 18, 6, 3, 4, 9, 9, 9]

Three Consecutive common numbers = 18, 9

"""
# inp = [18, 18, 18, 6, 3, 4, 9, 9, 9]
# for i in range(1,len(inp)):
#     if inp[i] == inp[i-1] and inp[i-1] == inp[i-2]:
#         print(inp[i])
#

"""
Write a Python Program to print all Possible Combinations from the three Digits

Sample Output

[1, 2, 3]

1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

"""
# inp = [1, 2, 3]
# for i in range(len(inp)):
#     for j in range(len(inp)):
#         for k in range(len(inp)):
#             if i != j and j != k and i != k:
#                 print(inp[i],inp[j],inp[k])

# =====================================================================================================================
"""
Write a Python program to get all unique combinations of two Lists

Sample Output

lis1 = ['A','B','C']

lis2  = [1,2,3]

[ [('A', 1), ('B', 2), ('C', 3)], [('A', 1), ('C', 2), ('B', 3)], [('B', 1), ('A', 2), ('C', 3)], [('B', 1), ('C', 2), 
('A', 3)], [('C', 1), ('A', 2), ('B', 3)], [('C', 1), ('B', 2), ('A', 3)] ]

"""
# a = ['A','B','C']
# b = [1, 2, 3]
# res = [(i,j) for i in a for j in b]
# print(res)

# =====================================================================================================================
"""
Write a Python Program to Remove Consecutive K element records

Sample Input

[ ('A', 'B', 'C', 'D'), ('B', 'C', 'C', 'I'), ('H', 'D', 'B', 'C'), ('C', 'C', 'G', 'F') ]

Sample Output
[ ('A', 'B', 'C', 'D'), ('H', 'D', 'B', 'C') ]

"""
# inp = [('A', 'B', 'C', 'D'), ('B', 'C', 'C', 'I'), ('H', 'D', 'B', 'C'), ('C', 'C', 'G', 'F')]
# for i in inp:
#     for j in range(1,len(i)):
#         if i[j] == "C" and i[j+1] == "C":
#             inp.pop(j)
# print(inp)

# ======================================================================================================================


# Write a Python program to count the number of sub lists that contain a particular element.
# Original list:
inp = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# Count 1 in the said list:
# 3
# Count 7 in the said list:
# 2
# count = 0
# num = int(input("Enter the number : "))
# for i in inp:
#     for j in i:
#         if j == num:
#             count += 1
# print(f"count {num} in the said list is {count}")

# ======================================================================================================================
# Write a Python function find the length of the longest increasing sub-sequence in a list.


# def increasing_sub_sequence():
#     """
#
#     :return: count of increasing sub-sequence
#     """
#
#     list = [10,20,30,40,50,60,70,80]
#     count = 1
#     # max_count = 1
#     for i in range(1,len(list)):
#         if list[i] > list[i-1]:
#             count += 1
#         else:
#             count = 1
#     print(count)
#
# increasing_sub_sequence()

# =====================================================================================================================
# Write a Python function to find the kth smallest element in a list.
# def find_kth_element(k):
#     """
#
#     :param k: kth element
#     :return: it will kth smallest element in list
#     """
#
#     nums = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]
#     for i in range(0,len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] > nums[j]:
#                 nums[i],nums[j] = nums[j],nums[i]
#     print(nums)
#     print(nums[k])
#
# k = int(input("Enter kth smallest element to find : "))
# print(f"{k}th element in list is {find_kth_element(k)}")

# =====================================================================================================================

# Write a Python function to find the kth the largest element in a list
# def find_kth_element(k):
#     """
#
#     :param k: kth element in list
#     :return: it returns kth largest element in list
#     """
#     nums = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]
#     for i in range(0,len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] >= nums[j]:
#                 nums[i],nums[j] = nums[j],nums[i]
#
#     print(nums)
#     print(nums[-k])
#
# k = int(input("Enter kth largest element in list :"))
#
# find_kth_element(k)

# ======================================================================================================================
#  Write a Python function to check if a list is a palindrome or not. Return true otherwise false
# def check_palindrome_list():
#     """
#
#     :return: return True if list is palindrome else False
#     """
#     nums = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]
#     return True if nums == nums[::-1] else False
#
# print(check_palindrome_list())

# ======================================================================================================================
# Write a Python function to remove duplicates from a list while preserving the order.
# def remove_duplicates():
#     res = []
#     lis = [1, 2, 4, 3, 5, 4, 6, 9, 2, 1]
#     for i in range(0,len(lis)):
#         for j in range(i+1,len(lis)):
#             if lis[i] >= lis[j]:
#                 lis[i],lis[j] = lis[j],lis[i]
#     for i in lis:
#         if i not in res:
#             res.append(i)
#     print(res)
#
# remove_duplicates()

# ======================================================================================================================
# Write a Python a function to find the maximum sum sub-sequence in a list. Return the maximum value
# def find_max_sum():
#     nums = [1, 2, 4, 3, 5, 4, 6, 9, 2, -10]
#     sum = 0
#     for i in nums:
#         if i > 0:
#             sum += i
#     print(sum)
#
# find_max_sum()
