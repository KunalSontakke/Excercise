"""
1) Introduction
2) Immutable and mutable
3) Automation API/ Request Module
4) REST API Status Codes
5) difference between PUT and Patch
6) Page object Model
7) Pytest Framework/parametrized

"""


""" remove spaces from input string without inbuilt function.
input = "remove spaCes from this stRing 123 "
output = "removespacesfromthisstring123" """

input = "remove spaces from this string 123 "

result = ''


# iterating the string
for i in input:
    # if the character is not a space
    if i != ' ':
        result = result + i
print("String after removing the spaces :",result)
#
# =======================================================================================================================

"""Python Program To Remove Duplicates From A Given String:"mississippi"""
string="mississippi"
p = ""
for char in string:
    if char not in p:
        p=p+char
print(p)







