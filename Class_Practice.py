"""
What is resolution in Python?

Method resolution order in Python Inheritance
In python, method resolution order defines the order in which the base classes are searched when executing a method.
First, the method or attribute is searched within a class, and then it follows the order we specified while inheriting.

"""
import datetime
import math

"""
Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter. 
"""
# class Circle:
#     def __init__(self,radius):
#         self.radius = radius
#
#     def calculate_area(self):
#         return math.pi * self.radius ** 2
#
#     def calculate_perimeter(self):
#         return 2 * math.pi * self.radius
#
#
# circle= Circle(3)
# print(circle.calculate_area())
# print(circle.calculate_perimeter())

"""
Write a Python program to create a person class. 
Include attributes like name, country and date of birth. Implement a method to determine the person's age.
"""

# from datetime import datetime


# class Person:
#     def __init__(self, name, country, DOB):
#         self.name = name
#         self.country = country
#         self.DOB = DOB
#

#
# def calculate_age(self):
#     age = datetime.now().year - self.DOB
#     return age


# person = Person("kunal", "india", 1994)
# print(person.calculate_age())

"""
Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter.
Implement subclasses for different shapes like circle, triangle, and square. 

"""
# class shape:
#     def calculate_area(self):
#         pass
#     def calculate_perimeter(self):
#         pass

# class circle(shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def calculate_area(self):
#         return math.pi * self.radius ** 2
#
#     def calculate_perimeter(self):
#         return 2 * math.pi * self.radius

# class triangle(shape):
#     def __init__(self,side1,side2,side3):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#     def calculate_area(self):
#         return 0.5 * self.side1 * self.side2
#
#     def calculate_perimeter(self):
#         return self.side1 + self.side2 + self.side3

# class rectangle(shape):
#     def __init__(self,length,breadth):
#         self.length = length
#         self.breadth = breadth
#
#     def calculate_area(self):
#         return self.length * self.breadth
#
#     def calculate_perimeter(self):
#         return 2 * (self.length + self.breadth)
#
#
# Circle = circle(7)
# print(Circle.calculate_area())
# print(Circle.calculate_perimeter())
#
# Triangle = triangle(4,5,6)
# print(Triangle.calculate_area())
# print(Triangle.calculate_perimeter())
#
# Rectangle = rectangle(4,5)
# print(Rectangle.calculate_area())
# print(Rectangle.calculate_perimeter())

"""
Write a Python program to create a class representing a stack data structure. 
Include methods for pushing and popping elements.

"""
# class Stack_Data:
#     def __init__(self):
#         self.list = []
#
#     def push_item(self,item_name):
#         self.list.append(item_name)
#
#     def pop_item(self,item_name):
#         if len(self.list) == 0:
#             print("Cannot be remove items....list is empty")
#         else:
#             self.list.remove(item_name)
#
#     def display_items(self):
#         return self.list
#
#
# stack = Stack_Data()
# stack.push_item("python")
# stack.push_item("java")
# stack.push_item("c++")
# stack.push_item("html")
# stack.pop_item("html")
# print(stack.display_items())
#

# =====================================================================================================================
"""
Write a Python program to create a class representing a shopping cart.
Include methods for adding and removing items, and calculating the total price

"""


class shopping_cart:
    def __init__(self):
        self.items = []

    def adding_items(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    def removing_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)

    def calculate_price(self):
        total = 0
        for item in self.items:
            total += item[1]
        print(total)


Shopping_cart = shopping_cart()
Shopping_cart.adding_items("cake", 1)
Shopping_cart.adding_items("baking powder", 2)
Shopping_cart.adding_items("shampoo", 10)
Shopping_cart.calculate_price()


class father:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def intro(self):
        print("hi my name is {} and my age is {}".format(self.name,self.age))

class son(father):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def intro(self):
        super().intro()
        print("my salary is {}".format(self.salary))

Son = son("kunal",29,3000)
Son.intro()

