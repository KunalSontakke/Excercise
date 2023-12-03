a = int(input("a :"))
b = int(input("b :"))

min_num = min(a,b)
hcf = 1
for i in range(1,min_num+1):
    if a % i == 0 and b % i ==0:
        hcf = i
print(hcf)
