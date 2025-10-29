num = 1234
reverse_num = 0
while num != 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10
print("reverse number is ", reverse_num)
"""
    digit = 1234 % 10 = 4
    reverse = 0 * 10 + 4 = 4
    num = 1234 // 10 = 123

    digit = 123 % 10 = 3
    reverse = 4 * 10 + 3 = 43
    num = 123 // 10 = 12

    digit = 12 % 10 = 2
    reverse = 43 * 10 + 2 = 432
    num = 12 // 10 = 1

    digit = 1 % 10 = 1
    reverse = 432 * 10 + 1 = 4321
    num = 1 // 10 = 0
"""

# ============================================================================
inp = int(input("enter a number : "))
stri = str(inp)
rev_str = stri[::-1]
print("reversed number is  :", rev_str)

num = 1234

rev = 0
while num != 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
print(rev)



