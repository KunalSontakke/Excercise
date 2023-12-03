# class Calculator:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def Addition(self):
#         return self.a + self.b
#
#     def Subtraction(self):
#         return self.a - self.b
#
#     def multiplication(self):
#         return self.a * self.b
#
#     def division(self):
#         return self.a / self.b
#
#     def square(self):
#         return self.a * self.a
#
#
# a = int(input("Enter the number :"))
# b = int(input("Enter the number :"))
#
# obj = Calculator(a, b)
#
# choice = 1
# while choice != 0:
#     print("0.Exit")
#     print("1.Addition")
#     print("2.Subtraction")
#     print("3.Multiplication")
#     print("4.Division")
#
#     choice = int(input("Enter Option"))
#     if choice == 1:
#         print(f"Addition of {a} and {b} is :", obj.Addition())
#     elif choice == 2:
#         print(f"Subtraction of {a} and {b} is :", obj.Subtraction())
#     elif choice == 3:
#         print(f"Multiplication of {a} and {b} is :", obj.multiplication())
#     elif choice == 4:
#         print(f"Division of {a} and {b} is :", obj.divison())
#     elif choice == 0:
#         print("Exiting application !!!")
#     else:
#         print("Invalid option !!!")

# =====================================================================================================================
# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def addition(self):
#         return self.a + self.b
#
#     def subtraction(self):
#         return self.a - self.b
#
#     def multiplication(self):
#         return self.a * self.b
#
#     def division(self):
#         return self.a / self.b
#
#
# x = int(input("Enter first number"))
# y = int(input("Enter second number"))
#
# calculator = Calculator(x,y)
# Option = 1
# print("1.Addition")
# print("2.Subtraction")
# print("3.Multiplication")
# print("4.Division")
# print("0.Exit")
#
# while Option != 0:
#     Option = int(input("Enter the option"))
#     if Option == 1:
#         print("Addition of", x, "and", y, "is", calculator.addition())
#
#     elif Option == 2:
#         print(f"Subtraction of {x} and {y} is", calculator.subtraction())
#
#     elif Option == 3:
#         print(f"Multiplication of {x} and {y} is", calculator.multiplication())
#
#     elif Option == 4:
#         print(f"Division of {x} and {y} is", calculator.division())
#
#     elif Option == 0:
#         print("Closing Application.............")
#
#     else:
#         print("Invalid Option")


# class calculator:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#
#     def addition(self):
#         return self.a + self.b
#
#     def subtraction(self):
#         return self.a - self.b
#
#     def multiplication(self):
#         return self.a * self.b
#     def divison(self):
#         return self.a + self.b
#
# a = int(input("Enter first Number"))
# b = int(input("Enter second Number"))
#
# calcy = calculator(a,b)
# print("1.Addition")
# print("2.Subtraction")
# print("3.Multiplication")
# print("4.Division")
# print("0.Addition")
# Option = 1
# while Option != 0:
#     Option = int(input("Enter the Option"))
#
#     if Option ==1:
#         print(f"addition of {a} and {b} is ",calcy.addition())
#
#     elif Option ==2:
#         print(f"Subtraction of {a} and {b} is ",calcy.subtraction())
#
#     elif Option ==3:
#         print(f"multiplication of {a} and {b} is ",calcy.multiplication())
#
#     elif Option ==4:
#         print(f"division of {a} and {b} is ",calcy.divison())
#
#     elif Option ==0:
#         print("Closing Application..... ")
#
#     else:
#         print("Invalid Option")
#

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def mutiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

a = int(input("a: "))
b = int(input("b: "))

calculator = Calculator(a,b)

option = 1
while option != 0:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("0.Exit....")

    option = int(input("Enter the Option: "))

    if option == 1:
        print(f"Addition of {a} and {b} is",calculator.addition())

    if option == 2:
        print(f"Subtraction of {a} and {b} is",calculator.subtraction())

    if option == 3:
        print(f"Multiplication of {a} and {b} is",calculator.mutiplication())

    if option == 4:
        print(f"Division of {a} and {b} is",calculator.division())

    if option == 0:
        print(f"Exiting Application.......")

    else:
        print("Invalid.........")


