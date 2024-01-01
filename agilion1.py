from Agilion import agilion

agilion.set_name

data = {
    1000: ('Task1', 'Module1'),
    1001: ('Task2', 'Module2'),
    1002: ('Task3', 'Module3'),
    1003: ('Task4', 'Module4'),
    1004: ('Task5', 'Module5'),
    1005: ('Task6', 'Module6'),
    1006: ('Task7', 'Module7')

}

test_case_id = int(input("Enter Test Case ID : "))
try:
    print(data[test_case_id])
except:
    print("This is not Valid Test case ID...")

# ===================================================================================================

list1 = [222343, 8, 7, 9000, 2345]
temp = 0
for i in range(0, len(list1)):
    for j in range(i + 1, len(list1)):
        if list1[i] > list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print(list1)
print(list1[-1])

# ====================================================================================================

string1 = "apple apple man monkey apply"
out = "man monkey apply"
res = []

str_spl = string1.split()
for i in str_spl:
    if str_spl.count(i) == 1:
        res.append(i)
print(" ".join(res))

# =========================================================================================================

import Agilion

print("main script name", __name__)

Agilion.show_module_name()
