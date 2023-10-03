list = [1, 5, 76, 34, 67]

temp = 0

print("Elements of original list : ")
for i in range(1, len(list)):
    print(list[i], end=" ")

for i in range(1, len(list)):
    for j in range(i + 1, len(list)):
        if list[i] >= list[j]:
            list[i], list[j] = list[j], list[i]
print(list)
print("list in reverse order",list[::-1],"\n")
