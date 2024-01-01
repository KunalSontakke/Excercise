
inp = "my name is kunal"
op = "kunal is name my"

print(" ".join(inp.split()[::-1]))


lst = [22,23,12,34,56,67,90,78]

# output = [90,78,22,23,12,34,56,67]

lst = lst[-2:] + lst[:-2]
print(lst)
