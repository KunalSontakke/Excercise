# """
#     Exercise 1: Convert two lists into a dictionary
#     Exercise 2: Merge two Python dictionaries into one
#     Exercise 3: Print the value of key ‘history’ from the below dict
#     Exercise 4: Initialize dictionary with default values
#     Exercise 5: Create a dictionary by extracting the keys from a given dictionary
#     Exercise 6: Delete a list of keys from a dictionary
#     Exercise 7: Check if a value exists in a dictionary
#     Exercise 8: Rename key of a dictionary
#     Exercise 9: Get the key of a minimum value from the following dictionary
#     Exercise 10: Change value of a key in a nested dictionary
#
# """
# # Exercise 1: Convert two lists into a dictionary
# import operator
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# Expected_output = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# #
# # Dict Comprehension
# dic_1 = {i:j for i,j in zip(keys,values)}
#
# print(dic_1)
# # For loop
# dic = {}
# for i in range(0,len(keys)):
#     dic.update({keys[i] : values[i]})
# print(dic)
#
# # Exercise 2: Merge two Python dictionaries into one
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Forty': 40, 'Fifty': 50}
# res_dict = {**dict1,**dict2}
# print(res_dict)
#
# # OR

# dict3 = dict1.copy()
# dict3.update(dict2)
#
# print(dict3)
#
# # ===================================================================================================
# # Exercise 3: Print the value of key ‘history’ from the below dict
#
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print("marks in History is",sampleDict['class']['student']['marks']['history'])
#
# # ====================================================================================================================

#  Exercise 4 :Initialize dictionary with default values
#
# # In Python, we can initialize the keys with the same values.
#
# # Given:
# employees = ['Kelly', 'Emma']
# defaults = {"designation": 'Developer', "salary": 8000}
#
# # Expected_output = {'Kelly': {'designation': 'Developer', 'salary': 8000},
# 'Emma': {'designation': 'Developer', 'salary': 8000}}
#
# dictionary = dict.fromkeys(employees,defaults)
# print(dictionary)
# print(dictionary['Kelly'])
#
# # ====================================================================================================================

# # Exercise 5: Create a dictionary by extracting the keys from a given dictionary
#
# # Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
#
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"}
#
# # Keys to extract
# keys = ["name", "salary"]
#
# # expected_output = {'name': 'Kelly', 'salary': 8000}
# dic_out = {k:sample_dict[k] for k in keys}
# print(dic_out)
#
# # =================================================================================
# # Exercise 6: Delete a list of keys from a dictionary
#
# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# # Keys to remove
# keys = ["name", "salary"]
#
# Expected_output = {'age': 25,'city': 'New york'}
#
# for i in keys:
#     sample_dict.pop(i)
# print(sample_dict)
#
# # =====================================================================================================
# # Write a Python program to check if value 200 exists in the following dictionary.
# #
# Sample_dict = {'a': 100, 'b': 200, 'c': 300}

# # expected_output = "200 present in a dict"
#
# for i in Sample_dict:
#     if 200 in Sample_dict.values():
#         print("200 present in a dict")
#         break
#     else:
#         print("200 not present")
#
# # =======================================================================================================
# # Exercise 8 :Write a program to rename a key city to a location in the following dictionary.
#
# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }
# sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)
#
# # ============================================================================================
# # Exercise 9: Get the key of a minimum value from the following dictionary
#
# simple_dict = {
#   'Physics': 82,
#   'Math': 65,
#   'history': 75
# }
#
# Expected_output = 'Math'
# print(min(simple_dict,key=simple_dict.get))
#
# # ===============================================================================================
# # Exercise 10: Change value of a key in a nested dictionary
#
# # Write a Python program to change Brad’s salary to 8500 in the following dictionary.
#
#
# sample_dict = {
#     'emp1': {'name': 'John', 'salary': 7500},
#     'emp2': {'name': 'Emma', 'salary': 8000},
#     'emp3': {'name': 'Brad', 'salary': 500}
# }
#
# # Expected_output ={
# #    'emp1': {'name': 'John', 'salary': 7500},
# #    'emp2': {'name': 'Emma', 'salary': 8000},
# #    'emp3': {'name': 'Brad', 'salary': 8500}
# # }

# sample_dict['emp3']['salary'] = 8500
# #
# # print(sample_dict)
# import operator
#
import operator

#
# dic = {'a':103,'b':34,'c':45,'d':67,'e':87}
# # Sort the dictionary using keys
# sort_dict = sorted(dic.items(),key=lambda x:x[0])


"""The lambda item: item[0] specifies that the sorting should be done based on the first element of each tuple (the keys)."""
# print(sort_dict)

# ======================================================================================================================
# # sort the dictionary using values
# sort_dic = sorted(dic.items(),key=lambda x : x[1])

"""The lambda item: item[1] specifies that the sorting should be done based on the second element of each tuple (the values)."""
# print(sort_dic)

# my_dict = {'b': 2, 'a': 1, 'c': 3}
# sorted_dict = sorted(my_dict.items())
#
# print(sorted_dict)

# ===============================================================================================

# Write a Python script to add a key to a dictionary.
#
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

# Dic = {0:10,1:20}
#
# Dic[2] = 30
#
# print(Dic)

# ===============================================================================================
# Write a Python script to concatenate the following dictionaries to create a new one.
#
# # Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50, 6:60}
#
# # Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
# res_dic = {}
# res_dic.update(dic1)
# res_dic.update(dic2)
# res_dic.update(dic3)
#
# print(res_dic)

# ==========================================================================
# Write a Python program to check whether a given key already exists in a dictionary.
#
# def check_key(dic, key):
#     if key in dic:
#         return True
#
#     else:
#         return False


# dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}
# key = input("Enter a key : ")
#
# check_key(dic, key)

# ======================================================================================

# Write a Python program to iterate over dictionaries using for loops
# dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}
#
# for key,value in dic.items():
#     print(key,":",value)

# ==========================================================================================
# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x,x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# n = int(input("Enter the range"))

# dic = {x : x**2 for x in range(n+1)}

# print(dic)

# ==========================================================================================
# Write a Python script to merge two Python dictionaries.
# d1 = {'a': 100, 'b': 200}
# d2 = {'x': 300, 'y': 200}
#
# d3 = d1.copy()
# d3.update(d2)
#
# print(d3)

# ============================================================================================
# Write a Python program to sum all the items in a dictionary
# my_dict = {'data1':100,'data2':-54,'data3':247}
# sum = 0
# for key in my_dict:
#     sum = sum + my_dict[key]
#
# print(sum)

# ===========================================================================================
# Write a Python program to multiply all the items in a dictionary.
# my_dict = {'data1':100,'data2':54,'data3':247}
# mul = 1
# for key in my_dict:
#     mul = mul * my_dict[key]
# print(mul)

# ========================================================================================
# Write a Python program to remove a key from a dictionary.
# myDict = {'a': 1,'b': 2,'c': 3,'d': 4}
# key = input("Enter key to remove")
#
# print(myDict)
# if key in myDict:
#     del myDict[key]
#
# print(myDict)
# ====================================================================================================
# Write a Python program to map two lists into a dictionary.
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
#
# dic = {key:value for key,value in zip(keys,values)}
# print(dic)

# =================================================================================================

# Write a Python program to sort a given dictionary by key
# color_dict = {'red':'#FF0000',
#           'green':'#008000',
#           'black':'#000000',
#           'white':'#FFFFFF'}
#
# sort_dic = {key:color_dict[key] for key in sorted(color_dict)}
# print(sort_dic)

# ================================================================================================
# Write a Python program to get the maximum and minimum values of a dictionary.
# my_dict = {'x': 500, 'y': 5874, 'z': 560}

# print(min(my_dict.keys(), key=(lambda k: my_dict[k])))
# print(max(my_dict.keys(), key=(lambda k: my_dict[k])))
#
# # ================================================================================
# # Write a Python program to get a dictionary from an object's fields.
#
# class dicObj(object):
#     def __init__(self):
#         self.x = "green"
#         self.y = "yellow"
#         self.z = "white"
#
#     def func(self):
#         pass
#
# obj = dicObj()
#
# print(obj.__dict__)
#
# class dictObj(object):
#     def __init__(self):
#         self.x = 'red'
#         self.y = 'Yellow'
#         self.z = 'Green'
#
#     def do_nothing(self):
#         pass
#
#
# test = dictObj()
# print(test.__dict__)

# ====================================================================================================

# my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
#
# sort_dict = sorted(my_dict.keys())
# print(sort_dict)
#
# for keys in sort_dict:
#     value = my_dict[keys]
#     print(keys, ":", value)

# =====================================================================================================================

# sort_dic_value = dict(sorted(my_dict.items(), key=(lambda x: [x])))

# print(sort_dic_value)

# =====================================================================================================================
input_dict = {'Ethernet1/4': ['10G', '25G', '40G', '100G'],
              'Ethernet1/5': ['10G'],
              'Ethernet1/6': ['100G']

              }
#
# output_dict = {'10G': ['Ethernet1/4', 'Ethernet1/5'],
#                '25G': ['Ethernet1/5'],
#                '40G': ['Ethernet1/4'],
#                '100G': ['Ethernet1/4', 'Ethernet1/6']
#                }
output = {}
# Iterate through the input dictionary
for interface, speeds in input_dict.items():
    # Iterate through the speeds for each interface
    for speed in speeds:
        if speed not in output:
            output[speed] = []  # Initialize the list if speed is not in the output dictionary
        output[speed].append(interface)
#
print(output)
# # ======================================================================================================================
"""
1. Write a Python script to sort (ascending and descending) a dictionary by value.

# Sample Output
# 
# dictionary = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# 
# output:- 
# Ascending order = [ (0, 0), (2, 1), (1, 2), (4, 3), (3, 4) ]
# Descending order = {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}
# 
# """
#
# dic = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
#
# sort_dict1 = sorted(dic.items(),key=operator.itemgetter(1))
# sort_dict2 = dict(sorted(dic.items(),key=lambda x:x[1]))
#
# print(sort_dict1)
# print(sort_dict2)
#

# ======================================================================================================================
"""
# Write a Python program to add a key to a dictionary
# 
# Sample Output
# 
# dictionary = {"Name" : "Ram" , "Age" : 23}
# 
# add_key = {"City" : "Salem"}
# 
# dictionary = {'Name' : 'Ram', 'Age' : 23, 'City' : 'Salem'}
# 
# """
# dictionary = {"Name" : "Ram" , "Age" : 23}
#
# add_key = {"City" : "Salem"}
# dictionary.update(add_key)
#
# print(dictionary)

# =====================================================================================================================
# """
# Dictionary 1 = {"Name" : "Ram" , "Age" : 23}
#
# Dictionary 2 = {"City" : "Salem", "Gender" : "Male"}
#
# Concatenate Dictionaries = {'Name' : 'Ram', 'Age' : 23, 'City' : 'Salem', 'Gender': 'Male'}
# """
# Dictionary_1 = {"Name" : "Ram" , "Age" : 23}
#
# Dictionary_2 = {"City" : "Salem", "Gender" : "Male"}
#
# conc_dict = {**Dictionary_1,**Dictionary_2}
# print(conc_dict)

# ======================================================================================================================

"""
Write a Python program to check whether a given key already exists in a dictionary.

Sample Output

{'Name' : 'Ram', 'Age' : 23}

Key = Name

Key is Available in the Dictionary

"""
# dic = {'Name' : 'Ram', 'Age' : 23}
#
# key = input("Enter the key :")
#
# if key in dic.keys():
#     print(dic[key])
# else:
#     print(key,"is not present")
#

# =====================================================================================================================
"""
Write a Python program to iterate over dictionaries using for loops.

dic ={"Name" : "Ram" , "Age" : 23 , "City" : "Salem", "Gender" : "Male"}

output :-
Name : Ram
Age : 23
City : Salem
Gender : Male

"""
# dic ={"Name" : "Ram" , "Age" : 23 , "City" : "Salem", "Gender" : "Male"}
#
# for key,value in dic.items():
#     print(key,":",value)

# =================================================================================================================
"""
Write a Python program to sum all the items in a dictionary.

Sample Output

{1 : 23, 2 : 45, 3 : -17, 4 : 87}

Sum all the Items = 138

"""
# dic = {1 : 23, 2 : 45, 3 : -17, 4 : 87}
# sum = 0
#
# for i in dic.values():
#     sum = sum + i
#
# print(sum)

# ======================================================================================================================
"""
A = {'Tamil' : 92, 'English' : 56, 'Maths' : 88, 'Science' : 97, 'Social' : 89}

B= {'Tamil' : 78, 'English' : 68, 'Maths' : 88, 'Science' : 97, 'Social' : 56}

Maths : 88 is present in both A and B
"""

# A = {'Tamil' : 92, 'English' : 56, 'Maths' : 88, 'Science' : 97, 'Social' : 89}
#
# B = {'Tamil' : 78, 'English' : 68, 'Maths' : 88, 'Science' : 97, 'Social' : 56}
#
# common_values = {}
# for key,value in A.items():
#     if key in B and B[key] == value:
#         common_values[key] = value
#
# for key,value in common_values.items():
#     print(key,":",value)

# =====================================================================================================================
"""
keys = ["One", "Two", "Three", "Four", "Five"]

values = [1, 2, 3, 4, 5]

Convert Two List to Dict = {'One' : 1, 'Two' : 2, 'Three' : 3, 'Four' : 4, 'Five' : 5}

"""
# keys = ["One", "Two", "Three", "Four", "Five"]
#
# values = [1, 2, 3, 4, 5]
#
# dic = {i:j for i,j in zip(keys,values)}
# print(dic)

# =====================================================================================================================
"""
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

Output: {'a': 1, 'b': [2, 3], 'c': [3, 4], 'd': 5}
"""
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 3, 'c': 4, 'd': 5}
# res = {}
# for key,value in dict1.items():
#     if key in dict2:
#         res[key] = [value,dict2[key]]
#     else:
#         res[key] = value
#
# for key,value in dict2.items():
#     if key not in dict1:
#         res[key] = value
#
# print(res)

# ===================================================================================================
"""
data = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 25}
]

Output: {25: [{'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 25}], 30: [{'name': 'Bob', 'age': 30}]}
"""
# data = [
#     {'name': 'Alice', 'age': 25},
#     {'name': 'Bob', 'age': 30},
#     {'name': 'Charlie', 'age': 25}
# ]
# res = {}
# for person in data:
#     age = person['age']
#     if age not in res:
#         res[age] = [person]
#     else:
#         res[age].append(person)
#
# print(res)

# ==============================================================================================
"""
text = "Hello world! This is a hello world example, world."

# Output: {'hello': 2, 'world': 3, 'this': 1, 'is': 1, 'a': 1, 'example': 1}

"""
# text = "Hello world ! This is a hello world example , world ."
# text_lower = text.lower()
# frequency = {}
# for i in text_lower.split():
#     if i.isalnum():
#         if i not in frequency:
#             frequency[i] = 1
#
#         else:
#             frequency[i] += 1
#
# print(frequency)

# ========================================================================================
"""nested_dict = {
    'a': 1,
    'b': {
        'x': 2,
        'y': {
            'p': 3,
            'q': 4
        }
    },
    'c': 5
}

# Output: {'a': 1, 'b_x': 2, 'b_y_p': 3, 'b_y_q': 4, 'c': 5}
"""
# nested_dict = {
#     'a': 1,
#     'b': {
#         'x': 2,
#         'y': {
#             'p': 3,
#             'q': 4
#         }
#     },
#     'c': 5
# }
# res = {}


# ====================================================================================================================
"""Write a Python program to verify that all values in a dictionary are the same.
Original Dictionary:
{'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
Check all are 12 in the dictionary.
True
Check all are 10 in the dictionary.
False"""

# dic = {'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# inp = input("Enter input : ")
# result = all(inp == x for x in dic.values())
# print(result)

# ===============================================================================================================
""" Write a Python program to remove a specified dictionary from a given list.
Original list of dictionary:
[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
Remove id #FF0000 from the said list of dictionary:
[{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]"""

# lis = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# key = "#FF0000"
# for i in lis:
#     if i['id'] == key:
#         i.pop(key)
#
# print(lis)

# lis = [i for i in lis if i['id'] != key]
# print(lis)

# =====================================================================================================================
"""Write a Python program to filter a dictionary based on values.
Original Dictionary:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
Marks greater than 170:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}"""

# dic = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# marks = int(input("Enter marks : "))
# res = {}
# for name,mark in dic.items():
#     if mark > marks:
#         res[name] = mark
# print(res)
#
# # or
# out = {key:value for key,value in dic.items() if value > marks}
# print(out)

# ====================================================================================================================
"""Write a Python program to convert more than one list to a nested dictionary.
Original strings:
['S001', 'S002', 'S003', 'S004']
['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
[85, 98, 89, 92]
Nested dictionary:
[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}"""

# id = ['S001', 'S002', 'S003', 'S004']
# names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# marks = [85, 98, 89, 92]
#
# out = []
# for i,j,k in zip(id,names,marks):
#     temp_dict = {i:{j:k}}
#     out.append(temp_dict)
# print(out)
#
# # or
#
# print([{i:{j:k}} for i,j,k in zip(id,names,marks)])


# =====================================================================================================================
""" 
Write a Python program to filter the height and width of students, which are stored in a dictionary.
Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height > 6ft and Weight> 70kg:
{'Cierra Vega': (6.2, 70)}

# """
# dic = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# height = int(input("height : "))
# weight = int(input("weight : "))
#
# res = {key:value for key,value in dic.items() if value[0] > height and value[1] > weight}
# print(res)
#
# # or
# for key,value in dic.items():
#     if value[0] > height:
#         if value[1] > weight:
#             print(key,":",value)

#         else:
#            print(f"{height},{weight} is not present")
#            break

# =====================================================================================================================
""" A Python dictionary contains List as a value. Write a Python program to clear the list values in the said dictionary.
Original Dictionary:
{'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
Clear the list values in the said dictionary:
{'C1': [], 'C2': [], 'C3': []}

"""
# dic = {'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for key, value in dic.items():
#     dic[key].clear()
# print(dic)

# ======================================================================================================================
"""A Python Dictionary contains List as a value. Write a Python program to update the list values in the said dictionary.
Original Dictionary:
{'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
Update the list values of the said dictionary:
{'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}"""

# dic = {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

# dic['Math'][2] = 91
# dic['Physics'][2] = 87

# print(dic)

# ======================================================================================================================
"""Write a Python program to find the specified number of maximum values in a given dictionary.
Original Dictionary:
{'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
1 maximum value(s) in the said dictionary:
['f']
2 maximum value(s) in the said dictionary:
['f', 'i']
5 maximum value(s) in the said dictionary:
['f', 'i', 'g', 'd', 'c']"""
dic = {'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}

sort_dic = dict(sorted(dic.items(),key= lambda x : x[1]))
print(sort_dic)
