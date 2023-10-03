"""
InputStr = "aaaabbbccccc111111@"
output = {'a': 4 , 'b':3, 'c':5, '1':6, '@':1 }
"""
InputStr = "aaaabbbccccc111111@"
CountDict = {}

"""This line of code creates or updates a key-value pair in a dictionary. 
The dictionary is called CountDict, and it is used to count the number of occurrences of each character in a string. 
The variable 'char' represents a character in the string. 
If the character already has a key in the dictionary, the value is incremented by 1. 
If the character is not already a key in the dictionary, a new key is created, and its value is set to 1. 
In other words, this line of code increases the count of a character in the dictionary by 1."""


dict = {}

for i in InputStr:
    # if i already appears as key in dict, increment the count
    if i in dict:
        dict[i] += 1

    # else i appears for the first time, add to dict
    else:
        dict[i] = 1

# printing result
print(dict)

# ======================================================================================================================
#
"""WAP to find first 5 even numbers using lamda function"""
even_lambda = lambda x: x % 2 == 0

even_nums = []

for i in range(0, 20):
    if even_lambda(i) and len(even_nums) < 5:
        even_nums.append(i)

print(even_nums)

# Appproach 2
def find_first_even_num():
    count = 0
    num = 0
    while count < 5:
        if num % 2 == 0:
            print(num,end=",")
            count += 1
        num += 1
find_first_even_num()

"""This function will keep incrementing the num variable until it finds the first 5 even numbers. 
The count variable is used to keep track of how many even numbers have been found so far. When count reaches 5, 
the loop will terminate."""

even_num = lambda x : x % 2 == 0

even_nums= []
for i in range(0,10):
    if even_num(i) and len(even_nums) < 5:
        even_nums.append(i)
print(even_nums)


