"""
Write a Python function that takes a string as input and returns "None" if the string is empty,
otherwise it returns the given string.

"""
# def func1(inp):
#     if not inp:
#         return "None"
#     else:
#         return inp
#
#
# inp = input("Enter the string")
#
# print(func1(inp))

# ================================================================================================
"""Write a Python function that returns the middle character of a string or "None" if the string length is odd"""

# def func2(inp):
#     mid_indx = len(inp)//2
#     if len(inp) % 2 ==0:
#         return inp[mid_indx]
#
#     else:
#         return "None"
#
#
# inp = input("Enter the string")
# print(func2(inp))

# ===================================================================================================================
"""
Write a Python program that iterates through a list of strings and prints each string. 
If a string is empty, print "Empty string" instead.

"""
# def func3(str_list):
#     for i in str_list:
#         if i:
#             print(i)
#         else:
#             print("Empty String")
#
#
# str_list = ["Python", "", "Java", "C++", "", "C#"]
#
# func3(str_list)

# ====================================================================================================================
"""
Write a Python function that checks if a given list is sorted in descending order. 
Return None if the list is empty.

"""

# def func4(lis):
#     if not lis:
#         return None
#
#     else:
#         sort_list = sorted(lis,reverse=True)
#         return sort_list
#
# lis =[1, 2, 3, 4, 5]
#
# if __name__ == "__main__":
#     print(func4(lis))

# ======================================================================================================================
"""
Write a Python program that takes a user's input and converts it to uppercase. If the input is empty, return None.
"""
# inp = input("Enter the string : ")
#
# if not inp:
#     print("None")
# else:
#     print(inp.upper())

# ======================================================================================================================
"""
Write a Python program that defines a dictionary and retrieves a value using a key. 
If the key is not found, return None

"""

# dic = {"name":"kunal","city":"Nagpur","company":"Calsoft","location":"Indore"}
# key  = input("Enter key : ")
#
# if key in dic:
#     print(dic[key])
# else:
#     print("None")

# ======================================================================================================================
"""
 Write a Python function that counts None values in a list recursively. Return 0 if the list is empty.
"""
def func5(lis):
    count = 0
    if not lis:
        return 0
    else:
        for i in lis:
            if i == "None":
                count += 1

        print(count)


lis = ["None",1,2,3,"None","None",7]

print(func5(lis))


"""
Write a Python function that takes two arguments and returns their sum if both aren't None, otherwise return None
"""
#
# def func6(a,b):
#     if not a:
#         return None
#
#     else:
#         return a + b
#
#
# a = int(input("Enter a"))
# b = int(input("Enter b"))
#
# print(func6(a,b))

# =====================================================================================================================
"""
Write a Python function that takes a list and returns a new list with None inserted between each element.
Original List: [2, 4, 6, 8, 10]
New List with None: [2, None, 4, None, 6, None, 8, None, 10]

"""
# def func6(lis):
#     new_list = []
#     if not lis:
#         return None
#     else:
#         for i in lis:
#             new_list.append(i)
#             new_list.append("None")
#         lis.pop()
#
#     print(new_list)
#
#
# lis = [2,4,6,8,10]
#
# print(func6(lis))

# ======================================================================================================================
"""
Write a Python function that replaces all occurrences of a substring in a string with another substring. 
Returns None if the original string is empty.

"""
def func7(inp,ip,op):
    if inp:
        if ip in inp:
            return inp.replace(ip,op)

    else:
        return None


inp = input("Enter the string : ")
ip = input("Enter the substring to replace : ")
op = input("Enter the substring to add : ")



if __name__ == "__main__":
    print(func7(inp, ip, op))


