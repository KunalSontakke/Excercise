"""Sort the dictionary on basis of values"""
import operator

dict1 = {'a': 5, 'b': 3, 'c': 4, 'd': 1, 'e': 2}

sorted_values = sorted(dict1.values())  # Sort the values
sorted_dict = {}

for i in sorted_values:
    for k in dict1.keys():
        if dict1[k] == i:
            sorted_dict[k] = dict1[k]

print(sorted_dict)

# sort the dictionary using values
sorted_dic = dict(sorted(dict1.items(),key= lambda x:x[1]))
print(sorted_dic)


"""how will be two mandatory and two optional parameter in function"""

def sum(a, b, c=None, d=None):
    return a + b + c + d


print(sum(2, 3, c=4, d=10))

"""Default 'Return' type of function"""
# - None


"""Write a program to find sum of consecutive numbers and print the maximum sum"""
L = [2, 5, 1, 6, 3, 8, 4, 3, 7, 1, 9, 2]
sum = []
for i in L:
    sum.append(L[i] + L[i + 1])
print(sum)
print(max(sum))

# =======================================================================

# inp = {'a': 5, 'b': 3, 'c': 4, 'd': 1, 'e': 2}
# output = {'d': 1, 'e': 2, 'b': 3, 'c': 4, 'a': 5}
#
#
# # Sort the dictionary by values in ascending order
# sorted_dict = dict(sorted(inp.items(), key=lambda x: x[1]))
# print(sorted_dict)


