# # Define a function that accepts 2 values and return its sum, subtraction and multiplication.
# #
# # Hint
# # Input:
# # Enter value of a = 7
# # Enter value of b = 5
# #
# # Expected output
# # Sum is = 12
# # Sub is = 2
# # Multiplication is = 35
#
# def function1(a,b):
#     sum = a + b
#     print("Sum is",sum)
#
#     subtraction = a - b
#     print("Subtraction is",subtraction)
#
#     multiplication = a * b
#     print("multiplication",multiplication)
#
#
# a = int(input("Enter a:"))
# b = int(input("Enter b:"))
# function1(a,b)
#
# # ===========================================================================
# # Define a function that accepts roll number and returns whether the student is present or absent.

# # Hint
# # Use a list to store sample roll. no.
# # Get input from a user and check if the number
# # exist in the list or not, if exists return present
# # else return absent
#
# def attendance_status(roll_no):
#     roll_list = [1,2,3,4,6,7,8,9,11,12,13,14,15,18,20,22,23,24,25,26,27,30]
#
#     if roll_no in roll_list:
#         print(f"{roll_no} is present")
#
#     else:
#         print(f"{roll_no} is absent")
#
#
# roll_no = int(input("Enter roll no to check: "))
# attendance_status(roll_no)

a = "Kunal"
b = "Kunal"

print(id(a))
print(id(b))

lis1 = [10,20,30]
lis2 = [10,20,30]

print(id(lis1))
print(id(lis2))
