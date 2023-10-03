num = int(input("Enter the Number : "))
reverse_num = 0
while num != 0:
    digit = num % 10
    reverse_num = reverse_num * 10 + digit
    num = num // 10
print("reverse number is ", reverse_num)


# ============================================================================
inp = int(input("enter a number : "))

stri = str(inp)

rev_str = stri[::-1]

print("reversed number is  :", rev_str)


str_inp = input("enter the string")

str_rev = str_inp[::-1]

if str_inp == str_rev:
    print("this str is palindrome")
else:
    print("not palindrome")

inp = input("enter number")
rev_inp = str(inp[::-1])
print("reverse number is : ",rev_inp)


num = int(input("Enter the number"))
rev = 0
while num != 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
print(rev)
