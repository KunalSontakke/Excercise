"""Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. 
If there is no middle letter, your function should return the empty string.
For example, mid("abc") should return "b" and mid("aaaa") should return """""
import pytest

# def mid(s):
#     try:
#
#         try:
#              mid_index = len(s) // 2
#              if len(s) >0:
#                 if len(s) % 2 ==1:
#                     return s[mid_index]
#                 else:
#                     return " "
#
#         except:
#             print("length of string should be greater than 0")
#
#     except Exception as e:
#         print("length of string should be greater than 0")
#
#
# print(mid())
#
# mid("")
# mid("abcd")
# mid("abcde")
# mid()
"""
for i in range(1, 101):
	if int(i*0.5)==i*0.5:"""

print([i for i in range(1, 101) if (i * 0.5) == 0.5])

"""Output of the following Python code?
a={i: 'A' + str(i) for i in range(5)}"""
"""
{0:"A0",1:"A1",2:"A2",3:"A3",4:"A4"}

"""

"""1. Write a Python program to print all distinct values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]"""

inp = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
res = []
for i in inp:
    for key, value in i.items():
        if value not in res:
            res.append(value)

print(res)


# class Citizen:
#     pass
#
class employee():
    def __init__(self, id, name, salary, department, rating):
        self.id = id
        self.name = name
        self.salary = salary
        self.department = department
        self.rating = rating

    def calculate_bonus(self):
        if self.rating == "A":
            self.salary += self.salary * 0.5
            return self.salary
        elif self.rating == "B":
            self.salary += self.salary * 0.4
            return self.salary, "Rs."
        elif self.rating == "C":
            self.salary += self.salary * 0.3
            return self.salary
        else:
            return self.salary


Employee = employee(101, "kunal", 50000, "QA", "B")
print(Employee.calculate_bonus())


#
@pytest.mark.parametrize("num1,num2,output", [(4, 2, 2), (10, 2, 5), (30, 3, 11), (12, 0, 12)])
def test_division(num1, num2, output):
    try:
        assert num1 / num2 == output
    except ZeroDivisionError as e:
        print(e)
    except AttributeError as e:
        print(e)
    except Exception as e:
        print(e)
