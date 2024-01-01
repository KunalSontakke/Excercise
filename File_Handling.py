
#
# inp = input("Enter string to replace : ")
# op = input("Enter string to add : ")
# try:
#     with open("C:\\Users\\Kunal\\PycharmProjects\\Excercise\\Text", "r") as file:
#         content = file.read()
#         for string in file:
#             if string == op:
#                 updated_str = string.replace(inp,op)
#             with open("C:\\Users\\Kunal\\PycharmProjects\\Excercise\\Text","w") as file:
#                     file.write(updated_str)
#     print("string replacement successful")
# except Exception as e:
#     print("error occurred....")
# except FileNotFoundError:
#     print(f"No {file} has been found... ")
#
# try:
#     with open("C:\\Users\\Kunal\\Downloads\\sample3.txt") as file:
#         content = file.read()
#         print(content)
#
# except FileNotFoundError as f:
#     print(f)
#
# except UnicodeDecodeError as u:
#     print(u)

# ======================================================================================================================

# Write a Python program to read an entire text file.
# file = open("file_python","r")
#
# print(file.read())

# ======================================================================================================================
#  Write a Python program to read first n lines of a file.
# file = open("file_python","r")
# line_num = int(input("Enter the line number till want you read : "))
# lines = file.readlines()
# for i in range(1,line_num+1):
#     print(lines[i].strip())

# ======================================================================================================================
# Write a Python program to append text to a file and display the text.
# with open("file_python","a") as file:
#     inp = input("Enter the text to enter : ")
#     file.write(inp)
#
# with open("file_python","r") as file:
#     print(file.read())

# ======================================================================================================================
# Write a Python program to read a file line by line and store it into a list.
# file = open("file_python","r")
# lst = []
# lines = file.readlines()
# print(lines)

# ======================================================================================================================

""". Write a Python program to read a file line by line store it into a variable. """
# a = ""
# try:
#     with open("Data/Text","r") as file:
#         for line in file.readlines():
#             print(line.strip())
#             a += line
#     print(a)
#
# except FileNotFoundError as e:
#     print(e)

"""8. Write a python program to find the longest words."""

# try:
#     lis = []
#     with open("Data/Text", "r") as file:
#         words = file.read().split()
#     max_word = max(words,key=len)
#     print(max_word,":",len(max_word))
#
# except:
#     pass

"""Write a Python program to count the number of lines in a text file."""
# try:
#     count = 0
#     with open("Data/Text","r") as file:
#         for line in file.readlines():
#             count += 1
#     print(count)
#
# except:
#     pass

"""Write a Python program to count the frequency of words in a file."""
# try:
#     freq = {}
#     with open("Data/Text","r") as file:
#         for word in file.read().split():
#             if word not in freq:
#                 freq[word] = 1
#             else:
#                 freq[word] += 1
#     print(freq)
# except:
#     pass

"""Write a Python program to get the file size of a plain file."""
# try:
#     import os
#     stat = os.stat("Data/Text")
#     print("The size of file in byte is",stat.st_size)

# except:
#     pass

"""Write a Python program to write a list content to a file."""
# colors = ["pink", "black", "blue", "white", "yellow", "green"]
# with open("Data/Text", "w") as file:
#     for color in colors:
#         file.write("%s\n" % color)
# content = open("Data/Text")
# print(content.read())

"""Write a Python program to read a random line from a file. """
# import random
# with open("Data/Text","r") as file:
#     lines = file.read().splitlines()
#     print(random.choice(lines))

