# Check if String is Palindrome or not

strings = input("enter the string")

if strings == strings[::-1]:
    print("the string is palindrome")
else:
    print("string is not palindrome")

# ======================================================================================
#  Check if Number is Palindrome or not
num = int(input("Enter a number:"))
temp = num
rev = 0
while num > 0:
    dig = num % 10
    rev = rev * 10 + dig
    num = num // 10
if temp == rev:
    print("The number is palindrome!")
else:
    print("Not a palindrome!")





