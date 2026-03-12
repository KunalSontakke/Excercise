"""
Write a  Python program to get the name of the operating system ( Platform independent),
information of the current operating system, current working directory,
print files and directories in the current directory, and raise errors if the path or file name is invalid.
"""
import os
import stat
import time

#
# print("os name:", os.name)
# # print("current operating system:") print(os.uname()))  # The os.uname() function is specific to Unix-like operating systems (Linux, macOS) and is not available on Windows.
#
# print("current working directory:", os.getcwd())
# print("directories:", os.listdir("."))
# print("data type of list of directories",type(os.listdir()))
#
# print("\n")
# try:
#     with open('Data/file.txt', 'r') as file:
#         print(file.read())
# except IOError as e:
#     print(e)
#
# # ======================================================================================================================
# """2. Write a Python program to list only directories, files and all directories, files in a specified path. """
#
# path = 'C:\\Users\\Kunal'
#
# print("directories:",[ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))])
#
# print("files",[name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name))])

# ======================================================================================================================

"""3. Write a  Python program to scan a specified directory and identify the subdirectories and files."""

import os
root = 'C:\\Users\\Kunal\\PycharmProjects'

for file in os.scandir(root):
    if file.is_dir():
        typ = "dir"

    elif file.is_file():
        typ = "file"

    elif file.is_symlink():
        typ = "sysmlik"

    else:
        typ = 'unknown'

    print(file,":",typ)

# ===================================================================================================================
""" Write a Python program to check access to a specified path. Test the existence, readability, writability and executability of the specified path"""

print('Exist:', os.access('c:\\Users\\Kunal\\PycharmProjects\\Excercise\\Data\\file.txt', os.F_OK))
print('Readable:', os.access('c:\\Users\\Kunal\\PycharmProjects\\Excercise\\Data\\file.txt', os.R_OK))
print('Writable:', os.access('c:\\Users\\Kunal\\PycharmProjects\\Excercise\\Data\\file.txt', os.W_OK))
print('Executable:', os.access('c:\\Users\\Kunal\\PycharmProjects\\Excercise\\Data\\file.txt', os.X_OK))

""" Write a Python program to get the size, permissions, owner, device, created, last modified and last accessed date and time of a specified path"""
path = 'c:\\Users\\Kunal\\PycharmProjects\\Excercise'
print("path name:({})".format(path))
print("size",stat.ST_SIZE)
print("Permissions",stat.ST_MODE)
print('Device:', stat.ST_DEV)
print('Created     :', time.ctime(stat.ST_CTIME))
print('Last modified:', time.ctime(stat.ST_MTIME))
print('Last accessed:', time.ctime(stat.ST_ATIME))
