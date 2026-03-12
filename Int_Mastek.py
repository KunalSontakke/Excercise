mylist = [101, 62, 66, 45, 99, 18, 266, 18]
print(max(mylist))

for i in range(0,len(mylist)):
    for j in range(i,len(mylist)):
        if mylist[i] > mylist[j]:
            mylist[i],mylist[j] = mylist[j],mylist[i]
print(mylist)
max_element = mylist[-1]
print(max_element)

# name salary
# ====================================================
class Parent:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"name: {self.name}")
        print(f"salary : {self.salary}")

class Child(Parent):
    def show_details(self):
        print(self.name)
        print(self.salary)

child = Child("kunal",10000)
print(child.name)
print(child.salary)


# ========================================================================