print([i**2 for i in range(1,11)])

# =======================================
"""from the list, return only even numbers.

nums = [3,6,8,1,10,7,2]"""
# nums = [3,6,8,1,10,7,2]
# print([i for i in nums if i % 2==0])

# ================================================
"""words = ["python","automation","testing"]

Output
["PYTHON","AUTOMATION","TESTING"]"""

# words = ["python","automation","testing"]
# print([word.upper() for word in words])

# ==============================================
"""words = ["apple","banana","cat"]

Output
[5,6,3]"""

# words = ["apple","banana","cat"]
# print([len(word) for word in words])

# ============================================================
"""words = ["apple","banana","cherry"]

Output
['a','b','c']"""

words = ["apple","banana","cherry"]
print([word[0] for word in words])

# ===========================================================
"""data = [[1,2,3],[4,5],[6,7,8]]

Output
[1,2,3,4,5,6,7,8]"""

# data = [[1,2,3],[4,5],[6,7,8]]
# print([j for i in data for j in i])

# ===========================================================
"""Find Numbers Divisible by Both 3 and 5

From 1–100.

Output example

[15,30,45,60,75,90]"""

# print([i for i in range(1,101) if i%3==i%5==0])

# ===========================================================
"""data = ["python","","automation","","testing"]

Output
["python","automation","testing"]"""

data = ["python","","automation","","testing"]

# print([i for i in data if i != ""])

# ===========================================================
"""For numbers 1–5.

Output
[(1,1),(2,4),(3,9),(4,16),(5,25)]"""

print([(i,i**2) for i in range(1,6)])

# ==============================================
"""nums = [5,-3,7,-1,4]

Output
[5,0,7,0,4]"""

# nums = [5,-3,7,-1,4]
# print([i if i > 0 else 0 for i in nums])

# =============================================================
"""matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

Output
[1,2,3,4,5,6,7,8,9]"""

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

print([j for i in matrix for j in i])
# =========================================================
"""list1 = [1,2,3]
list2 = ['a','b']

Output

[(1,'a'),(1,'b'),
 (2,'a'),(2,'b'),
 (3,'a'),(3,'b')]"""

