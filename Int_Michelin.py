"""write a python program to write/display count "t" letter in a string """

inputs = "I love about this country"
count = 0

for i in inputs:
    if i == "t":
        count = count + 1
print(count)


# ========================================================================================================

"""write a python program to multiply elements of two list save in new list"""
list1 = [2, 4, 6, 8, 10]
list2 = [2, 3, 4, 5, 6]

res_list = []

for i in range(0, len(list1)):
    res_list.append(list1[i] * list2[i])
print("Multiplication",res_list)

sum = [list1[i]+list2[i] for i in range(len(list1))]
print("Sum",sum)

# OR

op = [list1[i]*list2[i] for i in range(len(list1))]
print("Multiplication",op)

# =================================================================================

