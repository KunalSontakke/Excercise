""" Program to print half pyramid using  * """
# def pyramid_pattern_star(n):
#     for i in range(0,n):
#         for j in range(0,i+1):
#             print("* ",end="")
#         print("\n")
#
# n = int(input("Enter number of rows : "))
#
# pyramid_pattern_star(n)
# #
# # ======================================================================================================
#
# """ Program to print half pyramid a using numbers"""
# def pyramid_patter_num(n):
#     for i in range(n+1):
#         for j in range(0,i):
#             print(j+1,end=" ")
#         print("\n")
#
#
# n = int(input("Enter number of rows : "))
#
# pyramid_patter_num(n)
#
# # # ===================================================================================================================
# """program to find star full pyramid pattern"""
#
# num = int(input("Enter rows : "))
# row = 0
# while row < num:
#     space = num - row - 1
#     while space > 0:
#         print(end= " ")
#         space = space - 1
#     star = row + 1
#     while star > 0:
#         print("*",end=" ")
#         star = star -1
#     row = row + 1
#
#     print()
#
# # ==============================================================================
# """python program to find star full pyramid pattern"""
#
# def star_full_pyramid(n):
#     for i in range(1,n+1):
#         print(" " * (n-i) + " *" * i)
#         # print("\n")
#
# n = int(input("Enter rows : "))
#
# star_full_pyramid(n)
#
#
#
# for i in range(0,num+1):
#     print(" " * (num-i) + " *" * i)
#
#
#
# row = int(input("enter rows"))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("* ",end="")
#     print("\n")
#
# for i in range(1, n+1):
#     print(" " * (row - i) + " *" * i )
#
# row = int(input("enter rows"))
# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print("* ",end=" ")
#     print("\n")
#
# for i in range(1,row+1):
#     print(" " * (row-i) + " *" * i)



"""
1

21

123

4321

12345

"""
# row = int(input("Enter number of Rows : "))

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")

    print()


# Define the number of rows for the pattern
num_rows = 5

# Loop through each row
for i in range(1, num_rows + 1):
    # Loop to print numbers in decreasing order
    for j in range(i, 0, -1):
        print(j, end='')
    print()  # Move to the next line after each row


# =====================================================================================================================
"""
Write a Python program to construct the following pattern, using a nested for loop.

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

"""
# for i in range(6):
#     for j in range(i):
#         print("* ",end="")
#     print(" ")
#
# for i in range(6,0,-1):
#     for j in range(i):
#         print("* ",end="")
#     print(" ")

for i in range(1,5):
    for j in range(1,i+1):
        print("* ",end=" ")
    print("\n")

for i in range(1,6):
    print(" " * (6-i) + " *" * i)

for i in range(1,6):
    for j in range(0,5):
        print(j,end=" ")
    print()

for i in range(1, 6):
    for j in range(1,3):
        print(j,end=" ")
    print()

rows = 5  # Number of rows in the pattern

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j % 2 + 1, end=" ")
    print()

