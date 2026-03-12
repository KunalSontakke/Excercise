"""difference between set and list"""

"""input_list=[1,2,[3,4,5,6],9,10,11,0,[23,45,78],[100,90],(1000,10001)]
flatten using list comprehension

out = [1,2,3,4,5,6,7,8,.....]

OR
 """
"""
sum of dict values my_dict = {
    'a': 1,
    'b': [2, 3],
    'c': {'x': 4, 'y': 5},
    'd': (6, 7),
    'e': {'z': 8}
}"""

inp1 = [1,2,[3,4,5,6],9,10,11,0,[23,45,78],[100,90],(1000,10001)]
out = []
for i in inp1:
    if isinstance(i,(list,tuple)):
        for j in i:
            out.append(j)
    else:
        out.append(i)
print(out)


# ========================================================

my_dict = {
    'a': 1,
    'b': [2, 3],
    'c': {'x': 4, 'y': 5},
    'd': (6, 7),
    'e': {'z': 8}
}
sum = 0
for key,value in my_dict.items():
    if isinstance(value,(list,tuple)):
        for i in value:
            sum += i
    elif isinstance(value,int):
        sum += value
    elif isinstance(value,dict):
        for v in value.values():
            sum += v

print(sum)

# ============================================================================================

s = "hello"
for j in range(-1, -len(s) - 1, -1):
    print(s[j])

for i in range(len(s) - 1, -1, -1):
    print(s[i])
#

d = {"a": 1, "b": 2}
"""
which is the
safest
option ?
"""
# print(d["c"])
# or
print(d.get("c"))



# ==============================================================================================
a = [0, 1, 2]

output = []

for i in range(3):
    output += list(filter(lambda a: a == i, a))

# A) [[0], [1], [2]]
#
# B) [0, 1, 2]
