# How to check number is prime or not.

# num = int(input("enter a number: "))
#
# for i in range(2,num):
#     if num % i == 0:
#         print("It is not a prime number")
#         break
# else:
#     print("it is prime number")

# =====================================================================================================================

count = 0
for i in range(2,501):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        print(i)
        count += 1
print("count of prime numbers is",count)


num = int(input("Enter number :"))
prime_nos = []
for i in range(1,num):
    for j in range(2,i):
        if i %j == 0:
            break
    else:
        prime_nos.append(i)
print(prime_nos)
