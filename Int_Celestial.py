"""
1) Project Structure
2) Pytest Framework/ Fixture
3) Switching frames
4) API questions
5) POST and Put difference
6) less documentation in project
7) difference between Regression And Retesting

"""



"""Find all duplicate character of a string “iworkatcelestialsystems” Given any string,
the script should find all the duplicate  characters which are similar to each other
 and print the character.

Example: “iworkatcelestialsystems”
Output: etials"""

strng_inp = "iworkatcelestialsystems"
duplicate_chars = []

# Approach 1 (Using Empty list)
for i in strng_inp:
    if strng_inp.count(i) > 1:
        if i not in duplicate_chars:
           duplicate_chars.append(i)

print("".join(duplicate_chars))


# Approach 2 (using Empty String)
duplicate = ""
for i in strng_inp:
    if strng_inp.count(i)>1:
        if i not in duplicate:
            duplicate +=i
print(duplicate)

# ========================================================================================================

"""Given an array , write a script to find Second largest number, without using in-built functions
 
Ex: [30,15, 25, 20,5]
Output: second Largest number is 25"""

input = [30,15,25,20,5]
# sorting list using nested loops
for i in range(0, len(input)):
    for j in range(i + 1, len(input)):
        if input[i] >= input[j]:
            input[i], input[j] = input[j], input[i]
for i in  range(1,len(input)):
    print(input[i],end=",")
#
print("the second largest number is ",input[-2])



"""In the Gregorian calendar, three conditions are used to identify leap years:
 
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
 
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False."""


# def find_leap_year(year):
#     leap = False
#     if year % 400 == 0:
#         leap = True
#     elif year % 4 ==0 and year != 100:
#         leap = True
#     else:
#         return leap
#
# year = int(input("enter year : "))
# print(find_leap_year(year))
#

# =====================================================================================================================

l1 = [76, 23, 45, 12, 54, 9]
print("Original List:", l1)

# sorting list using nested loops
for i in range(0, len(l1)):
    for j in range(i + 1, len(l1)):
        if l1[i] >= l1[j]:
            l1[i], l1[j] = l1[j], l1[i]
""""
[76,23,45,12,54,9]
[23,76,45,12,54,9]
[23,45,76,12,54,9]
[23,45,12,76,54,9]
[23,45,12,54,76,9]
[23,45,12,54,9,76]
[23,12,45,54,9,76]
[12,23,45,9,54,76]
[12,23,9,45,54,76]
[12,9,23,45,54,76]
[9,12,23,45,54,76]

"""

