"""find maximum in array"""
arr1 = [1,2,34,56,78,26]
print(max(arr1))

"""check palindrome for a string"""

str1 = "kunal"
if str1 == str1[::-1]:
    print(True)
else:
    print(False)

"""write a star pattern (half)"""
for i in range(1,6):
    for j in range(1,i+1):
        print("* ",end=" ")
    print()


