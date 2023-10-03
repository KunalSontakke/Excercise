""" Write a Python program to print the following string in a specific format (see the output). Go to the editor
Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky.
Twinkle, twinkle, little star, How I wonder what you are" Output :

Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are
"""

print("Twinkle, twinkle ,little star, \n \t How I wonder what you are!,\n \t \t Up above the world so high,"
      "\n \t \t Like a diamond in the sky.\nTwinkle, twinkle  little star,\n \tHow I wonder what you are")

# =====================================================================================================================

"""Print current time and date"""
import datetime

current_time = datetime.datetime.now()

print("Current Date and Time is....... ")

print(current_time.strftime("%d-%m-%Y %H:%M:%S"))

# =======================================================================================================================
""""" Write a Python program to create the HTML string with tags around the word(s).
Sample input and result :
input: 'i' and  'Python'
output: '<i>Python</i>'"""

inputs = input("Enter string : ")
tag = input("Enter tag : ")

print("<%s>%s</%s>" % (tag, inputs, tag))

name = input("Enter your name ")
company = input("Enter your company name")
package = input("Enter your package in annual")

print("my name is %s.my company is %s.my package is %s" % (name, company, package))

# ====================================================================================================


"""Write a Python program to remove the nth index character
from a nonempty string.
Hint: 'string' and 'index' both from user input"""

stri = input("Enter String")
index = int(input('Enter index'))
first_part = stri[:index]

print(first_part)

# ======================================================================
"""Python program to capitalize the first and last character of each word in a string"""
strings = input("enter string : ")
result = strings[0].upper() + strings[1:-1] + strings[-1].upper()
print(result)

# list = [12,3,4,5,6,7,2]
# list.copy()

# ===================================================================================

"""check anagram of two words"""
word1 = input("enter first word : ")
word2 = input("enter second word : ")

if set(word1) == set(word2):
    print(word1, "and", word2, "are anagrams")
else:
    print(word1, "and", word2, "are not anagrams")

# ========================================================================================

inputs = input("enter string : ")
rev_str = ""
half_indx = len(inputs) // 2

for index in range(len(inputs)):
    if index <= half_indx:
        rev_str = rev_str + inputs[index]
    if index >= half_indx:
        rev_str = rev_str + inputs[index].upper()

print(rev_str)

# ====================================================================================
