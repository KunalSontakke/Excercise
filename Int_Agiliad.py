"""
1) Automated Framework
2) Dynamic Language
3) .py and .pyc

"""

""" Write python program to find fibonacci series"""

def Fibonacci(n):
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")

    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0

    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)


# # Driver Program


print(Fibonacci(10))
#  =========================================================================================================================

"""write python program to find vowels in string"""


def printVowels(string):
    # to print the vowels
    for i in string:
        if i in "aeiouAEIOU":
            print(i, end=',')


# take input
string = input('Enter any string: ')

# calling function
printVowels(string)

# =============================================================================================================================

""" Write a Python Program to Convert Comma Separated List to a String.
favorite_prog = ["Python", "SQL", "GO"]
Python, SQL, GO """

fav_prog = ["Python", "SQL", "GO"]

fav_prog = ",".join(fav_prog)

print(fav_prog)

names = "hat"
change = names.replace("h", "b")
print(names)





