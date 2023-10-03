"""
1) SDLC
2) Manual Testing
3) Severity and Priority
4) Python Language
5) .py and .pyc file
6) Virtual Env
7) python path
8) Lists and Tuples
9) Difference between Append and Extend
10)Inheritance
11)Selenium Components
12)driver navigation's
13)Scroll page
14)pytest module
15)Docstrings
16)Collection types
17) Lambda functions
18) PEP 8
19) Python packages
20) Multiple browsers

"""


list = [1,2,3,4,5]
list.append([4,8,9])
print(list)

list = [1, 2, 3, 4, 5]
list.extend([4, 8, 9])
print(list)
# #
class baseclass:
    # def __init__(self,str):
        # self.str = str

    def display(self):
        print("something")

class childclass(baseclass):
    def display(self):
        super(childclass, self).display()
        print("SOMETHING")


obj1 = childclass()
obj1.display()


