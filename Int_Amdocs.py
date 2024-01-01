"""
1.difference between 401 (Unauthorized) and 403 (forbidden)
2.Example of class and object
3.Multiple inheritance
4.Multiple Virtual environment
5.Private/public/Protected Access Modifier

"""

string = "hello world"
res = ""
for i in string:
    if i not in res:
        res += i
print(res[::-1])

# ==================================================================
num = 1234
out = 4321
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print(reverse)

"""
    Iteration 1:
        digit = 1234 % 10 = 4 (Extracts the last digit of num, which is 4)
        reverse = 0 * 10 + 4 = 4 (Adds the extracted digit to the reverse variable)
        num = 1234 // 10 = 123 (Removes the last digit from num)

    Iteration 2:
        digit = 123 % 10 = 3 (Extracts the last digit of the updated num, which is 3)
        reverse = 4 * 10 + 3 = 43 (Adds the extracted digit to the existing reverse)
        num = 123 // 10 = 12 (Removes the last digit from num)

    Iteration 3:
        digit = 12 % 10 = 2 (Extracts the last digit of the updated num, which is 2)
        reverse = 43 * 10 + 2 = 432 (Adds the extracted digit to the existing reverse)
        num = 12 // 10 = 1 (Removes the last digit from num)

    Iteration 4:
        digit = 1 % 10 = 1 (Extracts the last digit of the updated num, which is 1)
        reverse = 432 * 10 + 1 = 4321 (Adds the extracted digit to the existing reverse)
        num = 1 // 10 = 0 (Since num is now 0, the loop ends)
"""
# ================================================================
class A :
    def test(self):
        print("A")

class B:
    def test(self):
        print("B")

class C(B,A):
    pass


c = C()
c.test()

