# # """Append new string in the middle of a given string
# # s1 = "Ault"
# # s2 = "Kelly
# #
# # output = AuKellylt"""
# #
# # s1 = input("Enter first string :")
# # s2 = input("Enter first string :")
# #
# # mi = (len(s1) // 2)
# # first_half = s1[0:mi]
# # secnd_half = s1[mi:]
# #
# # print(first_half + s2 + secnd_half)
# #
# # """ Arrange string characters such that lowercase letters should come first"""
# # str = input("Enter a string : ")
# #
# # low_case = ""
# # up_case = ""
# #
# # for i in str:
# #     if i.islower():
# #         low_case = low_case + i
# #
# # for i in str:
# #     if i.isupper():
# #         up_case = up_case + i
# # print(low_case + up_case)
# ======================================================================================================================
# # #
# # """Count all letters, digits, and special symbols from a given string"""
# # inp = input("Enter characters")
# #
# # letters_cnt = 0
# # dig_cnt = 0
# # symb_cnt = 0
# #
# # for i in inp:
# #     if i.isalpha():
# #         letters_cnt =+ 1
# #     elif i.isdigit():
# #         dig_cnt =+ 1
# #     else:
# #         symb_cnt =+ 1
# #
# # print("letters count is ,", letters_cnt)
# # print("digits count is,", dig_cnt)
# # print("symb count is,", symb_cnt)
#
# # =====================================================================================
#
#
# # Write a program to count vowels and consonants in a string.
# #
# # Hint
# Input = "python"
# #
# # Expected output
# # Vowels count is: 1
# # Consonant count is: 5
#
# countA = 0
# countB = 0
# for i in Input:
#     if i in "aeiou":
#         countA = countA + 1
#     else:
#         countB = countB + 1
# print("Vowels count is", countA)
# print("Consonant count is", countB)
#
# # ===========================================================================================================
# # Write a program to remove duplicates in a string.
#
# # Hint
# Input1 = "pythonlobby"
#
# # Expected output
# # Result is: p y t h o n l b
# singles = []
# for i in Input1:
#     if i not in singles:
#         singles.append(i)
#
# for i in range(len(singles)):
#     print(singles[i], end=" ")
#
# # =================================================================================
# # Write a program to count the number of letters in a word.
#
# # Hint
# Input2 = "pythonlobby"
#
# # Expected output
# # Result is: 11
#
# count = 0
# for i in Input2::
#      count = count + 1
#
# print("\n",count)
#
# # ====================================================================================
# #  Python program to count the occurrence of each character in a word.
#
# # Hint
# x = "programm"
#
# # Expected output
# # Occurrence of each characters is :
# # {‘P’: 1, ‘r’: 2, ‘o’: 1, ‘g’: 1, ‘a’: 1, ‘m’: 2}
#
# freq = {}
#
# for i in x :
#     if i in freq:
#         freq[i] += 1
#
#     else:
#         freq[i] = 1
#
# print(freq)
#
# # Python program to convert lower letter to upper and upper letter to lower in a string.
# #
# # Hint
# Inut= "PrOgRaMM"
# #
# # Expected output
# # Result is: pRoGrAmm
# case = []
# for i in Inut:
#     if i.islower():
#         case.append(i.upper())
#
#     elif i.isupper():
#         case.append(i.lower())
#
# for i in case:
#     print(i,end="")
#
#
# # =====================================================================
# # Exercise 7: Python program to search a specific word in a string.
# #
# # Hint
# # Input:
# # Enter a String:  I am a boy
# # Enter a word to search: boy
# #
# # Expected output
# # boy exists in string
#
# print("\n")
# Input3 = input("Enter a string :")
# word = input("Enter a word to search : ")
# if word in Input3:
#     print(f"{word} exist in string")
# else:
#     print(f"{word} doesn't exist in string")
#
#
# # ==================================================================
# # Write a python program to sort letters of word by lower to upper case format.
# #
# # Hint
# # Input:
# String= "pytHOnloBBy"
# #
# # Expected output
# # Result: p y t n l o y H O B B
#
# result1 = []
# result2 = []
#
# for i in String:
#     if i.islower():
#         result1.append(i)
#
#     if i.isupper():
#         result2.append(i)
# res = result1 + result2
# for i in res:
#     print(i,end=" ")

# ============================================================================
#  Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : google.com'
# Expected Result : {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
#
# Sample_String = "google.com"
# freq = {}
# for i in Sample_String:
#     if i not in freq:
#         freq[i] = 1
#     else:
#         freq[i] += 1
#
# print(freq)

# ============================================================================
#  Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
#  If the string length is less than 2, return the empty string instead.

# Sample String : 'w3resource'
# Expected Result : 'w3ce'
# Sample String : 'w3'
# Expected Result : 'w3w3'
# Sample String : ' w'
# Expected Result : Empty String
# ip_str = input("Enter A string : ")
# if len(ip_str) > 2:
#     print(ip_str[:2]+ip_str[-2:])
#
# else:
#     print("Empty String")

# =====================================================================================
# Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
#
# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'


# def swap_str(a, b):
#     a1 = b[:2] + a[2:]
#     b1 = a[:2] + b[2:]
#
#     return a1 + " " + b1
#
#
# a = input("Enter string : ")
# b = input("Enter String : ")
#
# print(swap_str(a, b))

# ===============================================================================================
# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' add 'ly' instead. If the string length of the given string is less than 3,
# leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# # Expected Result : 'stringly
#
# str_inp = input("Enter a string : ")
# if len(str_inp) > 3:
#     if str_inp[-3:] == "ing":
#         print(str_inp,"ly")
#     else:
#         print(str_inp + "ing")
# else:
#     print("No change",str_inp)

# ===========================================================================================
# Write a Python function that takes a list of words and return the longest word and the length of the longest one.
# Longest word:  Exercises
# Length of the longest word:  9

# def max_length(word_list):
#     word_len = []
#     for words in word_list:
#         word_len.append((len(words),words))
#     word_len.sort()
#     return word_len[-1][1],word_len[-1][0]
#
#
# print(max_length(["apple","university","capital"]))

# ===============================================================================
# Write a Python program to remove the nth index character from a nonempty string
# str_inp = input("Enter a string : ")
# index = int(input("Enter index to remove "))
# up_str = str_inp[:index] + str_inp[index+1:]
#
# print(up_str)

# ====================================================================================

# Write a Python program to change a given string to a newly string
# where the first and last chars have been exchanged.
# str_inp = input("Enter String")
#
# up_str = str_inp[-1] + str_inp[1:-1] + str_inp[0]
#
# print(up_str)
#
# ck me to see the sample solution

# =================================================================================================

# Write a Python program to remove characters that have odd index values in a given string
#
# str_inp = input("Enter String")
#
# up_str = str_inp[0::2]
#
# print(up_str)
#
# # Or
#
# str_op = ""
# for i in range(len(str_inp)):
#     if i % 2 ==0:
#         str_op = str_op + str_inp[i]
#
# print(str_op)

# ======================================================================================

# Write a Python script that takes input from the user and displays that input back in upper and lower cases.
# str_inp = input("Enter a string")
# upp_case = str_inp.upper()
# low_case = str_inp.lower()
#
# print(upp_case)
# print(low_case)

# =========================================================================================

# Write a Python program that accepts a comma-separated sequence of words as input and
# prints the distinct words in sorted form (alphanumerically)
# str_inp = input("enter comma separated items : ")
#
# items = [item for item in str_inp.split(",")]
#
# print(",".join(sorted(list(set(items)))))

# =========================================================================================
# Write a Python function to create an HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

#
# def add_tag(inp,tag):
#     print("<%s>%s<%s>" %(tag,inp,tag))
#
#
# str_inp = input("Enter a string")
# tag = input("Enter a tag")
#
# add_tag(str_inp,tag)

# =======================================================================================
# Write a Python function to get a string made of 4 copies of the last two characters of a specified string
# (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses
#
#
# def copy_str(inp):
#     print(inp[-2:] * 4)
#
#
# inp = input("Enter String : ")
#
# copy_str(inp)

# =======================================================================================
# Write a Python function to get a string made of the first three characters of a specified string.
# If the length of the string is less than 3, return the original string.
# input = python
# output = pyt

# def function(inp):
#     return inp[:3] if len(inp) > 3 else inp
#
#
# inp = input("Enter string : ")
#
# print(function(inp))

# ===================================================================================
# Write a Python function to reverse a string if its length is a multiple of 4.
# def function(inp):
#     return inp[::-1] if len(inp) % 4 == 0 else inp
#
#
# inp = input("Enter the string")
#
#
# print(function(inp))

# ======================================================================================
# Write a Python function to convert a given string to all uppercase
# if it contains at least 2 uppercase characters in the first 4 characters.

# def upp_str(inp):
#     for i in inp[:4]:
#         if i.upper() == i:
#             return inp.upper()
#         else:
#             return inp


# inp = input("Enter string : ")

# print(upp_str(inp))

# =========================================================================================
# Write a Python program to check whether a string starts with specified characters.
# inp = input("Enter a string : ")
# string = input("Enter a substring")
#
# for i in inp:
#     if inp[0] == string :
#         print(inp,"strats with",string)
#         break
# else:
#     print(inp,"doesn't start with",string)


# ==================================================================================================================
"""
# You are given a string and your task is to swap cases. 
# In other words, convert all lowercase letters to uppercase letters and vice versa.
# 
# For Example:
# 
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2  
# 
# """
import re

#
# string = input("Enter the String : ")
# res = ""
# for i in string:
#     if i.islower():
#         res += i.upper()
#     else:
#         res += i.lower()
#
# print(res)


# count the numbers of 0's and 1's which are transversing
# str = "0110100110011"
# count = 0
# for i in range(0,len(str)):
#     if str[i] != str[i-1]:
#         count += 1
# print(count)


# str = "avinash"
# num = '5678'
# expected_output = "a5v6i7n8ash"
# out = ""
# for char,dig in zip(str,num):
#     out = out + char+ dig
#
#
# if len(str) > len(num):
#     out += str[len(num):]
# elif len(num) > len(str):
#     out += num[len(str):]
#
# print(out)

"""Write a Python program that returns a string sorted alphabetically by the first character of a given string of words.
Sample Data:
("Red Green Black White Pink") -> "Black Green Pink Red White"""

# str1 = "Red Green Black White Pink"
# out = "Black Green Pink Red White"
# print(" ".join(sorted([i for i in str1.split()])))

"""Write a Python program that takes a string and replaces all the characters with their respective numbers.
Sample Data:
("Python") -> "16 25 20 8 15 14"
("Java") -> "10 1 22 1"
("Python Tutorial") -> "16 25 20 8 15 14 20 21 20 15 18 9 1 12"""

# str2 = "python"
# order = [str(ord(i)-96) for i in str2]
# print(order)
# for i in order:
#     print(i,end=" ")


"""Write a Python program to insert space before every capital letter appears in a given word.
Sample Data:
("PythonExercises") -> "Python Exercises"
("Python") -> "Python"
("PythonExercisesPracticeSolution") -> "Python Exercises Practice Solution"""

# str3 = "PythonExercises"
# out = ""
# for i in str3:
#     if i.isupper() and out:
#         out = out + " " + i.upper()
#     else:
#         out = out + i
#
# print(out.strip())

"""Write a Python program that takes a string and returns # on both sides of each element, which are not vowels.
Sample Data:
("Green" -> "-G--r-ee-n-"
("White") -> "-W--h-i-t-e"
("aeiou") -> "aeiou"""

str4 = "green"
result = ""
# =================================================================

"""Given the Python test string below, which of the following pattern matching functions will find and print the value 'Blue'? 
testString = 'Yellow Blue Gold Green'
 1. re.findall (r'Blue', testString) [0] 
 2. re.search(r'Blue', testString) 
 3. re.search(r'Blue', testString).group(0) 
 4. re.match(r'Blue').group (0) 
 5. re.match(r'Blue')"""

testString = 'Yellow Blue Gold Green'

# print(re.findall('Blue',testString)[0])
# print(re.search('Blue',testString).group(0))

# =========================================================================
