"""how to find the duplicate records"""
"""select * from Table_name where count(id) = 1;"""

# =============================================================================================

"""miSsIsSiPpi
Print the number of occurrences of each character. (Expected output : i=4, m=1, p=2, s=4)

str1 = 'miSsIsSiPpi'

freq = {}

for i in str1.lower():
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1
print(dict(sorted(freq.items(),key= lambda x:x[0])))
"""
