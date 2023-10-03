import operator

lis = [1,2,3,4,6]

for i in range(min(lis),max(lis)):
    if i not in lis:
        print("Missing number is",i)


lis1 = [1,3,3,4,5,4,4,4,3,2,1,5]
# for i in lis1:
    # if lis1.count(i) == 3:
    #     print(i)
    #     break
freq = {}
for i in lis1:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

print(freq)

sort_dic = sorted(freq.items(),key=operator.itemgetter(1))
print(sort_dic)

try:
    inp = int(input("Enter the number"))
    div = int(input("Enter the divisor"))
    result = inp / div
    print(result)
except ZeroDivisionError as e:
    print("Can't be divided by Zero",e)





string = "television"
res = ""

for i in string:
    if string.count(i) > 1:
        res = res + "$"
    else:
        res = res + i

print(res)

# ===================================================================





