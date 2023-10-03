"""
Comprehensions in Python provide us with a short and concise way to construct new sequences
(such as lists, sets, dictionaries, etc.) using previously defined sequences.
Comprehension in Python converts the four to five lines of code into a one-liner.

"""
# 1) list Comprehension

listA = []
for i in range(50):
    if i % 5 == 0:
        listA.append(i)
print(listA)

# OR

listA = [i for i in range(50) if i % 5 == 0]
print(listA)

# 2) Dictionary Comprehension
Normaldict = {
    0: "item0",
    1: "item1",
    2: "item2",
    3: "item3",
    4: "item4",
}
Compdict = {i: Normaldict[i] for i in range(5)}
print(Compdict)

Comp_dict = {key: value for key, value in Normaldict.items()}
print(Comp_dict)

# Find all the numbers from 1-1000 that are divisible by 7
list7 = [i for i in range(1, 1001) if i % 7 == 0]
print(list7)

# ======================================================================================================================


# Find all the numbers from 1-1000 that have a 3 in them
list3 = [i for i in range(1, 1001) if "3" in str(i)]

# ======================================================================================================================

# Create a list of all the consonants in the string
# “Yellow Yaks like yelling and yawning, and yesterday they yodeled while eating yucky yams”

stri = "Yellow Yaks like yelling and yawning and yesterday they yodeled while eating yucky yams"

consonents = [i for i in stri.split() if i not in 'aeiouAEIOU']
print("consonants in strings are", consonents)

# ======================================================================================================================

# Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’).
# Result would look like (index, value), (index, value)

lst = ["hi", 4, 8.99, "apple", ("t", "b", "n")]
result = [(index, value) for index, value in enumerate(lst)]
print(result)

# ======================================================================================================================

listA, listB = [1, 2, 3, 4], [2, 3, 4, 5]

common_items = [i for i in listA for j in listB if i == j]
print("common items are", common_items)

# ======================================================================================================================

# Get only the numbers in a sentence like
# ‘In 1984 there were 13 instances of a protest with over 1000 people attending’
string = "In 1984 there were 13 instances of a protest with over 1000 people attending"
str_spl = string.split()
numbers = [i for i in str_spl if i.isdigit()]
print(numbers)

# ======================================================================================================================

# Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even,
# and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’
nos = ["even" if i % 2 == 0 else "odd" for i in range(20)]
print(nos)

# Produce a list of tuples consisting of only the matching numbers in these lists
list_a = 1, 2, 3, 4, 5, 6, 7, 8, 9,
list_b = 2, 7, 1, 12
# Result would look like (4,4), (12,12)
match_no = [(i,j) for i in list_a for j in list_b if i == j]
print(match_no)

# Exercise 1 - rewrite the above example code using list comprehension syntax.
# Make a variable named upper cased_fruits to hold the output of the list comprehension.
# Output should be ['MANGO', 'KIWI']
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

fruit = [i.upper() for i in fruits]
print(fruit)

# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax
# to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
capitalized_fruits = [i.capitalize() for i in fruits]
print(capitalized_fruits)

# Exercise 5 - make a list that contains each fruit with more than 5 characters
lst1 = [i for i in fruits if len(i) > 5]
print(lst1)

# Exercise 6 - make a list that contains each fruit with exactly 5 characters
lst2 = [i for i in fruits if len(i) == 5]
print(lst2)

# Exercise 7 - Make a list that contains fruits that have less than 5 characters
lst3 = [i for i in fruits if len(i) < 5]
print(lst3)

# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
lst4 = [len(i) for i in fruit]
print(lst4)

# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the
# letter "a"
a_letter_fruit = [i for i in fruits if "a" in i]
print(a_letter_fruit)

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers
even_numb = [i for i in numbers if i % 2 == 0]
print(even_numb)

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numb = [i for i in numbers if i % 2 == 1]
print(odd_numb)

# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
positive_numb = [i for i in numbers if i > 0]
print(positive_numb)

# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
negative_numb = [i for i in numbers if i < 0]
print(negative_numb)

# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
numb1 = [i for i in numbers if len(str(i)) >= 2 and i > 0]
print(numb1)


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared.
# Output is [4, 9, 16, etc...]
numb_sqr = [i ** 2 for i in numbers]
print(numb_sqr)

# Exercise 16 Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
odd_neg = [i for i in numbers if i % 2 == 1 and i < 0]
print(odd_neg)

# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.
numbers_plus_5 = [i + 5 for i in numbers]
print(numbers_plus_5)

prime_nos = [i for i in numbers if i % i == 0 and i % 1 == i]
print(prime_nos)


# . Write a Python program to sum all the items in a list
def sum_list(lis):
    sum = 0
    for i in lis:
        sum = sum + i

    print(sum)


lis = [1, 1, 2, 5, 8, -5]
sum_list(lis)

# Write a Python program to count the number of strings from a given list of strings.
# The string length is 2 or more and the first and last characters are the same.
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2


List = ['abc', 'xyz', 'aba', '1221']
count = 0

for i in List:
    if len(i) > 1 and i[0] == i[-1]:
        print(i, end=",")
        count = count + 1

print("\ncount of string is", count)

