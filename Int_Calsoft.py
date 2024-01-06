"""
1) Try and Except and Finally

Try and Except statement is used to handle these errors within our code in Python.The try block is used to
check some code for errors i.e the code inside the try block will execute when there is no error in the program.
Whereas the code inside the except block will execute whenever the program encounters some error in the preceding try block.

2) Method Over riding and method overloading


3) Raise Exception

"""


# """Program to validate the number or raise exception as it is invalid"""
# inputs = input("Enter a number : ")
# if type(inputs) != int:
#     raise Exception("this is not valid number")


"""program to remove duplicates from list"""
list = [34, 5, 34, 7, 5, 34]
rev_list = []
for i in list:
    if i not in rev_list:
        rev_list.append(i)
print(rev_list)

"""program to display square of number using lambda function"""
sqr = lambda a : a * a
# print(sqr(4))

equation = lambda a,b : a**2 + 2 * a * b + b**2
print(equation(2,3))


"""program to write 'circle' object and create 'radius' for it"""

class circle:
    def __init__(self,radius):
        self.radius = radius

        if self.radius > 0:
            print("the radius is valid")
        else:
            assert False


obj = circle(2)
print("the radius is",obj.radius)
#


"""program to remove duplicates from list"""


eqn = lambda a,b : a**2 + 2 * a * b + b**2
print(eqn(2,3))

