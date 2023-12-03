# Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
#
# exception ZeroDivisionError:
#
# Raised when the second argument of a division or modulo operation is zero.
# The associated value is a string indicating the type of the operands and the operation.
#
# def mod_by_Zero(x,y):
#     try:
#         result = x / y
#         print(int(result))
#
#     except ZeroDivisionError:
#         print("division by Zero is not possible")
#
#
# num = int(input("Enter a number : "))
# div = int(input("Enter a number : "))
#
# mod_by_Zero(num,div)

# ===============================================================================================

# Write a Python program that prompts the user to input an integer and raises a ValueError exception
# if the input is not a valid integer.
#
# exception ValueError

# def check_num(n):
#     try:
#         print(n)
#
#     except ValueError as e:
#         print(e)
#
#
# inp = int(input("Enter a number : "))
# check_num(inp)

# =====================================================================================================================
# Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.
# exception FileNotFoundError:
# Raised when a file or directory is requested but doesn't exist.

# try:
#     with open("C:\\Users\\Kunal\\PycharmProjects\\Excercise\\Text","r") as file:
#         print(file.read())
#
# except FileNotFoundError as e:
#     print("Error Found",e)

# ======================================================================================================================
# Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.
# Exception PermissionError:
# Raised when trying to run an operation without the adequate access rights - for example filesystem permissions.
# Corresponds to errno EACCES, EPERM, and ENOTCAPABLE.


# try:
#     with open("D:\kunal.txt") as file:
#         print(file.read())
#
# except PermissionError as e:
#     print("Error Found",e)
#

# ======================================================================================================================
# Write a Python program that executes an operation on a list and handles an IndexError exception
# if the index is out of range.
#
# exception IndexError:
#
# Raised when a sequence subscript is out of range.
# (Slice indices are silently truncated to fall in the allowed range; if an index is not an integer,TypeError is raised)

# try:
#     index = int(input("Enter index number in list : "))
#     lis = [1,2,3,4,5,7,8]
#     result = lis[index]
#     print(result)
#
# except IndexError as e:
#     print("Error Found :",e)

# Write a Python program that prompts the user to input a number and handles a
# KeyboardInterrupt exception if the user cancels the input.
#
# exception KeyboardInterrupt:
# try:
#     inp = int(input("Enter the number : "))
#     print(inp)
#
# except KeyboardInterrupt :
#     print("Input Canceled by User")


# ============================================================================================
# Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.
#
# exception UnicodeDecodeError:
#
# Raised when a Unicode-related error occurs during decoding. It is a subclass of UnicodeError.

try:
    with open ("/Data/Text", "r") as file:
        print(file.read())

except UnicodeDecodeError as e:
    print(e)

