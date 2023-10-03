str = "you are welcome to python programming are welcome to python programming"
str_spl = str.split()
count = 0

# Count method
for i in str_spl:
    if str_spl.count(i) > 1:
        count+= 1
    if str_spl.count(i) == 1:
        count = 1
    print("count of",i,"is",str_spl.count(i))

# =============================================================================================================
# Dictionary Method

dict = {}
for i in str_spl:
    if i not in dict:
        dict[i] = 1

    else:
        dict[i] += 1
print(dict)
