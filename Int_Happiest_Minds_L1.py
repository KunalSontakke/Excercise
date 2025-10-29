"""
s='kunal'

replace last character with any another character without using any another variable
"""
# inp = "kunal"

s='kunal'
print(s.replace("l","s"))

"""
s='mynameiskunal' reverse the string without built_in_function

"""
inp ='mynameiskunal'
str = ""
for i in inp:
    str = i + str
print(str)

# =======================================================================================================================
lis = [1,2,3,4,5,6,7,8,9,10]

odd_lis=[i for i in lis if i%2==1]
print(odd_lis)

# =====================================================================================================================
l=[[1],[1,2],[1,2,3],[1,2,3,4]]

"""print sum of all elements in the list"""

total_sum = 0
for sublist in l:
    for j in sublist:
        total_sum = total_sum + j

print("Total sum of elements in list is",total_sum)

# =====================================================================================================================

# write a python program to create a decorator which will square a number if in range(1,10) else it will cube a number
def sqr_cube_decoartor(func):
    def wrapper(x):
        if 1 <= x <= 10:
            result = x ** 2
        else:
            result = x ** 3
        return func(result)
    return wrapper


@sqr_cube_decoartor
def print_num(num):
    return num


ip = int(input("Enter the number"))

print(print_num(ip))

