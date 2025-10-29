#  """
#  Question 1
#  Level 1
#
#  Question:
#  Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#  between 2000 and 3200 (both included).
#  The numbers obtained should be printed in a comma-separated sequence on a single line.
#  """
# count = 0
# for i in range(2000,3201):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i,end=",")
#         count = count + 1
# print("\ncount of such numbers is",count)
#
# ======================================================================================================================
#
# """
# Question:
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# """
# n = int(input("Enter a number : "))
# dic = {i:i**2 for i in range(1,n+1)}
# print(dic)
#
# ======================================================================================================================
#
# """
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# """
# nums = input("Enter numbers to add into list :")
# lis = []
# for i in nums.split(","):
#     lis.append(int(i))
# print(lis)
#
# num_tuple = tuple(lis)
# print(num_tuple)
#
# # ====================================================================================================================
# """"
# write a python program to find HCF of two numbers
#
# """
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# min_num = min(num1,num2)
# hcf =1
# for i in range(1,min_num+1):
#     if num1 % i == 0 and num2 % i == 0:
#         hcf = i
#
# print(hcf)
#
# # ===============================================================================================
# Input:
# word1 = "abc"
# word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
#
# output = ""
#
# Determine the length of the shorter word
# min_length = min(len(word1), len(word2))
#
# Merge strings alternatively
# for i in range(min_length):
#     output += word1[i] + word2[i]
#
# Add remaining characters from the longer word, if any
# output += word1[min_length:] + word2[min_length:]
#
# print(output)


# ====================================================================================================
# s = "abcd"
# t = "abcde"
# out = ""
# Output: "e"
# Explanation: 'e' is the letter that was added
# for i in t:
#     if i not in s:
#         out += i
# print(out)
#
# ==================================================================================================
# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
#
# Example 2:
#
# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1

# haystack = input("Enter the word : ")
# needle = input("Enter string to search")
#
# if needle not in haystack:
#     print("-1")
# else:
#     print(haystack.index(needle))
#

# ============================================================================================================
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false
#
# inp1 = input("Enter the first word : ")
# inp2 = input("Enter the second word :")
#
# if set(inp1) == set(inp2):
#     print("true")
# else:
#     print("false")

# =====================================================================================================================
# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# Example 1:
#
# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
#
# Example 2:
#
# Input: s = "aba"
# Output: false
#
# Example 3:
#
# Input: s = "abcabcabcabc"
# Output: true
# Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

# s = input("Enter the string: ")
#
# length = len(s)
# is_constructible = False
# repeated_count = 0
#
# # Iterate through possible substring lengths from 1 to half of the string length
# for i in range(1, length // 2 + 1):
#     # If the current substring length divides the input string length evenly
#     if length % i == 0:
#         substring = s[:i]  # Extract the substring of length i
#         # Construct a potential repeated string by repeating the substring
#         repeated_string = substring * (length // i)
#         # If the constructed string matches the input string, it can be formed by repeating the substring
#         if repeated_string == s:
#             is_constructible = True
#             repeated_count += 1
#             break
#
#  Check if the input string is constructible and print the result
# if is_constructible:
#     print("Output: true")
#     print(f" appeared {repeated_count} times")
# else:
#     print("Output: false")

# =======================================================================================================================
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2:
# Input: nums = [0]
# # Output: [0]
inp_lis = [1,0,2,3,0,6,0,8,8,0,9]
# res = []
# for i in inp_lis:
#     if i != 0:
#       res.append(i)
#
# for i in range(inp_lis.count(0)):
#     res.append(0)
# print(res)

# or

# nums = [num for num in inp_lis if num !=0] + [0] * inp_lis.count(0)
# print(nums)

# =====================================================================================================================
# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.
#
# Example 1:
#
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
#
# Example 2:
#
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].

digits = [1,2,3]
# sum = 0
# for i in range(len(digits)-1,-1,-1):
#     digits[i] += 1
#     if digits[i] == 10:
#         digits[i] = 0
#
#     else:
#         break
#
#     if digits[0] == 0:
#         digits.insert(0,1)
#
# print(digits)

# OR

# digits[-1] += 1
# print(digits)

# ======================================================================================================================
# There is a function signFunc(x) that returns:
#
#     1 if x is positive.
#     -1 if x is negative.
#     0 if x is equal to 0.
#
# You are given an integer array nums. Let product be the product of all values in the array nums.
#
# Return signFunc(product).

# Example 1:

# Input: nums = [-1,-2,-3,-4,3,2,1]
# Output: 1
# Explanation: The product of all values in the array is 144, and signFunc(144) = 1
# def signFunc(mul=1):
#     nums = [-1,-2,-3,-4,3,2,1,-2]
#     for i in nums:
#         mul = mul * i
#     if mul <0:
#         print(f"the product of all values in the array is {mul},and signFunc({mul}) = -1")
#     elif mul > 0:
#         print(f"the product of all values in the array is {mul},and signFunc({mul}) = 1")
#     else:
#         print(f"the product of all values in the array is {mul},and signFunc({mul} = 0")

# signFunc()

# ======================================================================================================================
# Given a string s consisting of words and spaces, return the length of the last word in the string.

# Example 1:

#Input:
# s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# s_spl = s.split()
# print(f"the last word is {s_spl[-1]} with length {len(s_spl[-1])}")

# ======================================================================================================================
# Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
# Example 1:
# Input:
s = "HELLO"
# Output: "hello"

# Example 2:
# Input: s = "here"
# Output: "here"

# Example 3:

# Input: s = "LOVELY"
# Output: "lovely

# res = ""
# for i in s:
#     if i.isupper():
#         res = res + i.lower()
#     else:
#         res = res + i
# print(res)


# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
# Example 1:
# Input:
# nums = [1,2,3,4]
# # Output: [24,12,8,6]
# #
# # Example 2:
# # Input: nums = [-1,1,0,-3,3]
# # Output: [0,0,9,0,0]
#
# ======================================================================================================================
# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other

# def func():
#     lis = [1,2,3,5,6,7]
#     for i in range(1,len(lis)):
#         if len(lis) == len(set(lis)):
#             return True
#         else:
#             return False
#
# print(func())
#
# =====================================================================================================================
"""Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'. 
Ensure that each character is used only once"""


# import itertools
# vowels = ['a','e','i','o','u']
#
# all_permutations = list(itertools.permutations(vowels))
#
# for permutation in all_permutations:
#     print(''.join(permutation))

# ======================================================================================================================
#
"""Write a Python program that removes and prints every third number from a list of numbers until the list is empty"""
# lis1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
#
# while len(lis1) > 0:
#     index = (3 - 1) % len(lis1)
#     lis1.pop(index)
#     print("removed",lis1[index])
#     print(lis1)
#
# print(f"{lis1} is empty")

# =====================================================================================================================
"""Write a Python program that prints long text, converts it to a list, 
and prints all the words and the frequency of each word."""

text = '''United States Declaration of Independence
From Wikipedia, the free encyclopedia
The United States Declaration of Independence is the statement
adopted by the Second Continental Congress meeting at the Pennsylvania State
House (Independence Hall) in Philadelphia on July 4, 1776, which announced
that the thirteen American colonies, then at war with the Kingdom of Great
Britain, regarded themselves as thirteen independent sovereign states, no longer
under British rule. These states would found a new nation – the United States of
America. John Adams was a leader in pushing for independence, which was passed
on July 2 with no opposing vote cast. A committee of five had already drafted the
formal declaration, to be ready when Congress voted on independence.

John Adams persuaded the committee to select Thomas Jefferson to compose the original
draft of the document, which Congress would edit to produce the final version.
The Declaration was ultimately a formal explanation of why Congress had voted on July
2 to declare independence from Great Britain, more than a year after the outbreak of
the American Revolutionary War. The next day, Adams wrote to his wife Abigail: "The
Second Day of July 1776, will be the most memorable Epocha, in the History of America."
But Independence Day is actually celebrated on July 4, the date that the Declaration of
Independence was approved.

After ratifying the text on July 4, Congress issued the Declaration of Independence in
several forms. It was initially published as the printed Dunlap broadside that was widely
distributed and read to the public. The source copy used for this printing has been lost,
and may have been a copy in Thomas Jefferson's hand.[5] Jefferson's original draft, complete
with changes made by John Adams and Benjamin Franklin, and Jefferson's notes of changes made
by Congress, are preserved at the Library of Congress. The best-known version of the Declaration
is a signed copy that is displayed at the National Archives in Washington, D.C., and which is
popularly regarded as the official document. This engrossed copy was ordered by Congress on
July 19 and signed primarily on August 2.

The sources and interpretation of the Declaration have been the subject of much scholarly inquiry.
The Declaration justified the independence of the United States by listing colonial grievances against
King George III, and by asserting certain natural and legal rights, including a right of revolution.
Having served its original purpose in announcing independence, references to the text of the
Declaration were few in the following years. Abraham Lincoln made it the centerpiece of his rhetoric
(as in the Gettysburg Address of 1863) and his policies. Since then, it has become a well-known statement
on human rights, particularly its second sentence:

We hold these truths to be self-evident, that all men are created equal, that they are endowed by their
Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness.

This has been called "one of the best-known sentences in the English language", containing "the most potent
and consequential words in American history". The passage came to represent a moral standard to which
the United States should strive. This view was notably promoted by Abraham Lincoln, who considered the
Declaration to be the foundation of his political philosophy and argued that it is a statement of principles
through which the United States Constitution should be interpreted.

The U.S. Declaration of Independence inspired many other similar documents in other countries, the first
being the 1789 Declaration of Flanders issued during the Brabant Revolution in the Austrian Netherlands
(modern-day Belgium). It also served as the primary model for numerous declarations of independence across
Europe and Latin America, as well as Africa (Liberia) and Oceania (New Zealand) during the first half of the
19th century.'''

"""Write a Python program that prints long text, converts it to a list, 
and prints all the words and the frequency of each word."""
# text_list = [n for n in text.split()]

# for i in text_list:
#     print(i,":",text_list.count(i))

# ======================================================================================================================
"""Write a Python program to count the number of each character in a text file."""
# with open("C:\\Users\\Kunal\\PycharmProjects\\Excercise\\abc.json") as file:
#     data = file.read()
#
#     for char in data.split(" "):
#         print(char,':',data.count(char))

# ======================================================================================================================
"""Write a Python program to get a list of locally installed Python modules."""
import pkgutil
#
# installed_packages = []
# utils = pkgutil.iter_modules()
# for package in utils:
#     installed_packages.append(package)
#
# # print(installed_packages)
# for package in installed_packages:
#     print(package)

# ======================================================================================================================
"""Write a Python program to display some information about the OS where the script is running"""
# import platform
#
# print("system :",platform.system())
# print("system version :",platform.version())
# print("sytem release :",platform.release())
# print("system processor :",platform.processor())
# print("python branch :",platform.python_branch())
# print("python build :",platform.python_build())
# print("python compiler :",platform.python_compiler())
# print("python version :",platform.python_version())
#

# ======================================================================================================================
