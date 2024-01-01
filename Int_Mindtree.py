"""interviewer : Gopi mani"""

"""find the occurrence of each letter"""
inp = "automation tester"

freq = {}

for i in inp:
    if i.isalpha():
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

print(freq)

print(inp[::-1])



