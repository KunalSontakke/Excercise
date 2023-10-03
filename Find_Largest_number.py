"""In this program, you'll learn to find the largest and second largest among three numbers using if else and display it."""

a = int(input("Enter First number : "))
b = int(input("Enter Second number : "))
c = int(input("Enter Third number : "))

largest = 0
second_largest = 0

if a > b and a > c:
    largest = a
    print("Largest Number is: ", a)
    if b > c:
        second_largest = b
        print("Second number is :",b)
    else:
        second_largest = c
        print("Second largest number is :",c)

elif b > a and b > c:
    largest = b
    print("Largest Number is: ",b)
    if a >c:
        second_largest = a
        print("Second largest number is :", a)
    else:
        second_largest = c
        print("Second largest number is :", c)
else:
    largest = c
    print("Largest Number is :",c)
    if a > b:
        second_largest =a
        print("Second largest number is :",a)
    else:
        second_largest = b
        print("Second largest number is :", b)

