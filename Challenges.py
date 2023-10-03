"""
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.
"""
count = 0
for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i,end=",")
        count = count + 1
print("\ncount of such numbers is",count)

# ======================================================================================================================

"""
Question:
With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
n = int(input("Enter a number : "))
dic = {i:i**2 for i in range(1,n+1)}
print(dic)

# ======================================================================================================================

"""
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.
Suppose the following input is supplied to the program:
34,67,55,33,12,98
Then, the output should be:
['34', '67', '55', '33', '12', '98']
('34', '67', '55', '33', '12', '98')
"""
nums = input("Enter numbers to add into list :")
lis = []
for i in nums.split(","):
    lis.append(int(i))
print(lis)

num_tuple = tuple(lis)
print(num_tuple)

# ====================================================================================================================
""""
write a python program to find HCF of two numbers

"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

min_num = min(num1,num2)
hcf =1
for i in range(1,min_num+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print(hcf)

