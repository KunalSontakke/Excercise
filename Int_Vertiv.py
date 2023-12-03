"""
1) SDlC and STLC
2) Unit testing and System testing
3) Smoke Testing
4) Bug report
5) Authentication and Authorization
6) DEEP and Shallow Copy
7) Polymorphism
8) Multithreading
9) Interpretation Process
10) Formatting

"""

# # #
# with open("D:\kunal.txt","r") as countletter:
#     count = 0
#     text = countletter.read()
#     for character in text:
#         if character.isupper():
#             count += 1
#     # print(character)
# print(count)


# ==========================================================================================
"""Interchange the a,b"""
a = 5
b = 10

temp = a
a = b
b = temp
print(a)
print(b)

# ============================================================================================

"""Reverse The string"""

def reverse(s):

    str = ""
    for i in s:
        str = i + str
    return str


s = "my name is kunal"
t = "My Name is {} and my age is {}".format("kunal",28)
print(t)


print(reverse(s))
print(s.format())
# ===================================================================================


"""Print Table of 5"""
x = 5

for i in range(1,11):
    print("5", "x" ,i, "=",x * i)

# ==========================================================================================

"""Decorator function"""

def Upper_Func(function):
    def wrapper():
        x=function()
        string_upper = x.upper()
        return string_upper
    return wrapper()

@Upper_Func
def print_hello():
    return "hello kunal"

print(print_hello)


