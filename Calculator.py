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
#         print(f"Division of {a} and {b} is :", obj.division())
#     elif choice == 0:
#         print("Exiting application !!!")
#     else:
#         print("Invalid option !!!")

# =====================================================================================================================
class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


a = int(input("a : "))
b = int(input("b : "))
calculator = Calculator(a,b)

option = 1
while option != 0:
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print("0.exit...")

    option = int(input("Enter option :"))

    if option == 1:
        print(f"addition of {a} and {b} is",calculator.addition())

    elif option == 2:
        print(f"subtraction of {a} and {b} is",calculator.subtraction())

    elif option == 3:
        print(f"multiplication of {a} and {b} is",calculator.multiplication())

    elif option == 4:
        print(f"division of {a} and {b} is",calculator.division())

    elif option == 0:
        print("Exiting Application ........")

    else:
        print("Invalid Option.....")

