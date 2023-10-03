
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

