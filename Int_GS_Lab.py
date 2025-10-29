"""Write a program to remove the duplicate elements in a list

List = [1, 2,3, 4, 5, 6,5, 6]"""

List = [1, 2,3, 4, 5, 6,5, 6]

out = []
#
# str_ot = ""
# for i in List:
#     if i not in str_ot:
#         str_ot += i
# print("".split(str_ot))

# ===========================================
person = {"name":"kunal","company":"nitor","location":"nagpur"}
salary = {"PF":"1900"}

# dict = {**person,**salary}
# print(dict)
#
person.update(salary)
print(person)

# =============================================
print([key for key,value in person.items()])
print([value for key,value in person.items()])

# ============================================================
