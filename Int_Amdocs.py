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
    digit = num % 10 #4 123 % 10
    reverse = reverse * 10 + digit #3
    num = num // 10 #123
print(reverse)
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

