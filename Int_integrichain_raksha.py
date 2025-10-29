"""Find the count of numbers containing '6' in it from the sequence 1 to 1000.
Also print the numbers"""

count = 0
for i in range(1001):
    if "6" in str(i):
        print(i)
        count = count + 1
print("count of '6' is,",count)
