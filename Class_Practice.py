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


# class shopping_cart:
#     def __init__(self):
#         self.items = []
#
#     def adding_items(self, item_name, qty):
#         item = (item_name, qty)
#         self.items.append(item)
#
#     def removing_item(self, item_name):
#         for item in self.items:
#             if item[0] == item_name:
#                 self.items.remove(item)
#
#     def calculate_price(self):
#         total = 0
#         for item in self.items:
#             total += item[1]
#         print(total)
#
#
# Shopping_cart = shopping_cart()
# Shopping_cart.adding_items("cake", 1)
# Shopping_cart.adding_items("baking powder", 2)
# Shopping_cart.adding_items("shampoo", 10)
# Shopping_cart.calculate_price()
#
#
# class father:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def intro(self):
#         print("hi my name is {} and my age is {}".format(self.name,self.age))
#
# class son(father):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary
#
#     def intro(self):
#         super().intro()
#         print("my salary is {}".format(self.salary))
#
# Son = son("kunal",29,3000)
# Son.intro()
# print(issubclass(son,father))
#
#
# """"Write a Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions."""
#
# class Bank:
#     def __init__(self):
#         self.customers = {}
#
#     def create_account(self,account_number,init_bal=0):
#         if account_number not in self.customers:
#             self.customers[account_number] = init_bal
#             print(f"Account number {account_number} successfully created.....")
#
#         else:
#             print(f"{account_number} already exists.....")
#
#     def deposit_money(self,account_number,amount):
#         if account_number in self.customers:
#             self.customers[account_number] += amount
#             print(f"{amount} deposited into account number {account_number}")
#         else:
#             print(f"{account_number} does not exist....")
#
#     def withdraw_money(self,account_number,amount):
#         if account_number in self.customers:
#             if self.customers[account_number] >= amount:
#                 self.customers[account_number] -= amount
#                 print(f"{amount} debited from account number {account_number}...")
#     def show_balance(self,account_number):
#         if account_number in self.customers:
#             balance = self.customers[account_number]
#             print("current balance is",balance)
#         else:
#             print(f"{account_number} does not exist")
#
#
# bank = Bank()
# bank.create_account(34280821977)
# bank.deposit_money(34280821977,5000)
# bank.withdraw_money(34280821977,500)
# bank.show_balance(34280821977)

"""Create a Vehicle class with attributes like make, model, and year.
 Include a method that prints out the details of the vehicle."""

# class Vehicle:
#     def __init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def show_config(self):
#         print(f"it is made by {self.make} with model {self.model}")
#         print(f"It was launched in year {self.year}")
#
# vehicle= Vehicle("Toyota","Innova",2003)
# vehicle.show_config()

"""Design a BankAccount class that includes attributes such as account_number, account_holder, and balance. 
Implement methods for deposit, withdrawal, and displaying the account details."""

# class BankAccount:
#     def __init__(self,account_number,account_holder,balance=0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance
#         self.users = {}
#     def create_account(self):
#         if self.account_number not in self.users:
#             self.users[self.account_number] = self.account_holder
#             self.users[self.account_number] = self.balance
#         else:
#             print(f"{self.account_number} already exists...")
#
#     def deposit(self,amount):
#         if self.account_number in self.users:
#             self.users[self.account_number] = self.account_holder
#         else:
#             self.users[self.account_number] += amount
#     def withdrawl(self,amount):
#         if int(amount) >self.users[self.account_number]:
#             print("not sufficient funds...")
#         else:
#             self.users[self.account_number] -= amount
#
#     def account_details(self):
#         if self.account_number in self.users:
#             print(f"{self.users[self.account_number]}")
#
#
# bank  = BankAccount(123456,"kunal",0)
# bank.create_account()
# bank.deposit(5000)
# bank.withdrawl(500)
# bank.account_details()


"""Create a Student class with attributes like name, age, and grades. 
Include a method that calculates the average grade of the student"""
from datetime import datetime

# class Student:
#     def __init__(self,name,age,grades=[]):
#         self.name = name
#         self.age = age
#         self.grades = grades
#
#     def calculate_avg_grade(self):
#         if not self.grades:
#             print("No grades")
#             return 0
#         else:
#             average = sum(self.grades)/len(self.grades)
#             return average
#
# student = Student("kunal",29,[23,45,67,24,12])
# print(f"average grade of {student.name} aged {student.age} is",student.calculate_avg_grade(),"marks")

"""Design a Book class with attributes like title, author, and publication_year. 
Include a method to check if the book is available or checked out."""

book_shelf = [
    {
        "author": "Chinua Achebe",
        "country": "Nigeria",
        "imageLink": "images/things-fall-apart.jpg",
        "language": "English",
        "link": "https://en.wikipedia.org/wiki/Things_Fall_Apart\n",
        "pages": 209,
        "title": "Things Fall Apart",
        "year": 1958
    },
    {
        "author": "Hans Christian Andersen",
        "country": "Denmark",
        "imageLink": "images/fairy-tales.jpg",
        "language": "Danish",
        "link": "https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.\n",
        "pages": 784,
        "title": "Fairy tales",
        "year": 1836
    },
    {
        "author": "Dante Alighieri",
        "country": "Italy",
        "imageLink": "images/the-divine-comedy.jpg",
        "language": "Italian",
        "link": "https://en.wikipedia.org/wiki/Divine_Comedy\n",
        "pages": 928,
        "title": "The Divine Comedy",
        "year": 1315
    },
    {
        "author": "Unknown",
        "country": "Sumer and Akkadian Empire",
        "imageLink": "images/the-epic-of-gilgamesh.jpg",
        "language": "Akkadian",
        "link": "https://en.wikipedia.org/wiki/Epic_of_Gilgamesh\n",
        "pages": 160,
        "title": "The Epic Of Gilgamesh",
        "year": -1700
    },
    {
        "author": "Unknown",
        "country": "Achaemenid Empire",
        "imageLink": "images/the-book-of-job.jpg",
        "language": "Hebrew",
        "link": "https://en.wikipedia.org/wiki/Book_of_Job\n",
        "pages": 176,
        "title": "The Book Of Job",
        "year": -600
    },
    {
        "author": "Unknown",
        "country": "India/Iran/Iraq/Egypt/Tajikistan",
        "imageLink": "images/one-thousand-and-one-nights.jpg",
        "language": "Arabic",
        "link": "https://en.wikipedia.org/wiki/One_Thousand_and_One_Nights\n",
        "pages": 288,
        "title": "One Thousand and One Nights",
        "year": 1200
    },
    {
        "author": "Unknown",
        "country": "Iceland",
        "imageLink": "images/njals-saga.jpg",
        "language": "Old Norse",
        "link": "https://en.wikipedia.org/wiki/Nj%C3%A1ls_saga\n",
        "pages": 384,
        "title": "Nj\u00e1l's Saga",
        "year": 1350
    },
    {
        "author": "Jane Austen",
        "country": "United Kingdom",
        "imageLink": "images/pride-and-prejudice.jpg",
        "language": "English",
        "link": "https://en.wikipedia.org/wiki/Pride_and_Prejudice\n",
        "pages": 226,
        "title": "Pride and Prejudice",
        "year": 1813
    },
    {
        "author": "Honor\u00e9 de Balzac",
        "country": "France",
        "imageLink": "images/le-pere-goriot.jpg",
        "language": "French",
        "link": "https://en.wikipedia.org/wiki/Le_P%C3%A8re_Goriot\n",
        "pages": 443,
        "title": "Le P\u00e8re Goriot",
        "year": 1835
    },
    {
        "author": "Samuel Beckett",
        "country": "Republic of Ireland",
        "imageLink": "images/molloy-malone-dies-the-unnamable.jpg",
        "language": "French, English",
        "link": "https://en.wikipedia.org/wiki/Molloy_(novel)\n",
        "pages": 256,
        "title": "Molloy, Malone Dies, The Unnamable, the trilogy",
        "year": 1952
    },
    {
        "author": "Giovanni Boccaccio",
        "country": "Italy",
        "imageLink": "images/the-decameron.jpg",
        "language": "Italian",
        "link": "https://en.wikipedia.org/wiki/The_Decameron\n",
        "pages": 1024,
        "title": "The Decameron",
        "year": 1351
    },
    {
        "author": "Jorge Luis Borges",
        "country": "Argentina",
        "imageLink": "images/ficciones.jpg",
        "language": "Spanish",
        "link": "https://en.wikipedia.org/wiki/Ficciones\n",
        "pages": 224,
        "title": "Ficciones",
        "year": 1965
    },
    {
        "author": "Emily Bront\u00eb",
        "country": "United Kingdom",
        "imageLink": "images/wuthering-heights.jpg",
        "language": "English",
        "link": "https://en.wikipedia.org/wiki/Wuthering_Heights\n",
        "pages": 342,
        "title": "Wuthering Heights",
        "year": 1847
    },
    {
        "author": "Albert Camus",
        "country": "Algeria, French Empire",
        "imageLink": "images/l-etranger.jpg",
        "language": "French",
        "link": "https://en.wikipedia.org/wiki/The_Stranger_(novel)\n",
        "pages": 185,
        "title": "The Stranger",
        "year": 1942
    },
    {
        "author": "Paul Celan",
        "country": "Romania, France",
        "imageLink": "images/poems-paul-celan.jpg",
        "language": "German",
        "link": "\n",
        "pages": 320,
        "title": "Poems",
        "year": 1952
    },
    {
        "author": "Louis-Ferdinand C\u00e9line",
        "country": "France",
        "imageLink": "images/voyage-au-bout-de-la-nuit.jpg",
        "language": "French",
        "link": "https://en.wikipedia.org/wiki/Journey_to_the_End_of_the_Night\n",
        "pages": 505,
        "title": "Journey to the End of the Night",
        "year": 1932
    },
]

"""Design a Book class with attributes like title, author, and publication_year. 
Include a method to check if the book is available or checked out."""


# class Book:
#     def __init__(self, title, author, publication_year):
#         self.title = title
#         self.author = author
#         self.publication_year = publication_year
#
#     def check_availability(self):
#         for i in book_shelf:
#             if self.author in i['author']:
#                 print(f"{self.author} is available...")
#             # else:
#             #     print(f"{self.author} is not available")
#             #     break
#
#
# book = Book("Journey to the End of the Night", "Jane Austen", 1932)
# book.check_availability()

# =========================================================================================================
"""Create a class hierarchy for animals. Have a base class Animal with common attributes, 
and then create subclasses like Mammal, Bird, and Fish"""

# class Animals:
#     def __init__(self,name,speak,food):
#         self.name = name
#         self.speak = speak
#         self.food = food
#
#     def make_sound(self):
#         print(f"{self.name} makes a {self.speak} sound")
#
#
# class Mammal(Animals):
#     def __init__(self,name,speak,fur,food):
#         super(Mammal,self).__init__(name,speak,food)
#         self.fur = fur
#
#     def give_birth(self):
#         print(f"{self.name} gives birth to young one")
#
#
# class Bird(Animals):
#     def __init__(self,name,food,feet,speak):
#         super(Bird,self).__init__(name,speak,food)
#         self.feet = feet
#
#     def fly(self):
#         print(f"{self.name} can fly with {self.feet} feet")
#
#
# class Fish(Animals):
#     def __init__(self,name,food,scale,speak):
#         super(Fish,self).__init__(name,food,speak)
#         self.scale = scale
#
#     def lay_eggs(self):
#         print(f"{self.name} with {self.scale} can lay eggs")
#
#
# mammal = Mammal(name="dog",speak="bark",food="bone",fur="hair")
# mammal.make_sound()
# mammal.give_birth()
#
# bird = Bird(name="hen",food="corn",feet=2,speak="coo-koo")
# bird.make_sound()
# bird.fly()
#
# fish = Fish(name="whale",food="algae",scale="fin",speak="freq")
# fish.make_sound()
# fish.lay_eggs()


"""Develop a simple employee management system. Create an Employee class with attributes like name, position, and salary.
Include methods for salary calculation and displaying employee details."""

# class Employee:
#     def __init__(self,name,position,salary):
#         self.name = name
#         self.position = position
#         self.salary = salary
#
#     def salary_calculation(self):
#         print(f"{self.salary}")
#
#     def display_details(self):
#         print(f"name:{self.name}")
#         print(f"position:{self.position}")
#         print(f"salary:{self.salary}")
#
#
# employee = Employee("kunal","Automation tester",10000)
# employee.display_details()
# employee.salary_calculation()


"""Design a class for a social media user. Include attributes like username, followers, and posts.
 Implement methods for posting, gaining followers, and displaying user details."""

# class Social_media:
#     def __init__(self,username):
#         self.username = username
#         self.followers = 0
#         self.posts = []
#
#     def post(self,content):
#         self.posts.append(content)
#         print(f"{self.username} posted {self.posts}")
#
#     def gain_followers(self,num_followers):
#         self.followers += num_followers
#
#     def display_details(self):
#         print(f"{self.username} with {self.followers} and {self.posts}")
#
#
# social_media = Social_media("kunal sontakke")
# social_media.post("HI I am on beach .....enjoying")
# social_media.gain_followers(50)
# social_media.display_details()
#
#

"""Create a Classroom class with attributes like class_name, teacher, and students. 
Include methods for adding and removing students, as well as displaying the class details"""
#
# class Classroom:
#     def __init__(self,class_name,teacher):
#         self.class_name = class_name
#         self.teacher = teacher
#         self.students = {}
#     def add_students(self,student_name):
#         if self.class_name not in self.students:
#             self.students[self.class_name] = []
#
#         if student_name not in self.students[self.class_name]:
#             self.students[self.class_name].append(student_name)
#         else:
#             print(f"{student_name} already exist in {self.class_name}")
#
#     def remove_student(self,student_name):
#         if self.class_name in self.students and student_name in self.students[self.class_name]:
#             self.students[self.class_name].remove(student_name)
#
#         else:
#             print(f"{student_name} does not exist.......")
#
#     def display_class_details(self):
#         print(f"{self.class_name}")
#         print(f"{self.teacher}")
#         print(f"students {self.students.get(self.class_name,[])}")
#
# class_obj = Classroom("5","suresh")
# class_obj.add_students("kunal")
# class_obj.add_students("shubham")
# class_obj.add_students("sagar")
# class_obj.remove_student("shubham")
# class_obj.display_class_details()


"""Develop a class-based car rental system. Create a Car class with attributes like make, model, and rental_price.
 Include methods for renting and returning cars, as well as displaying available cars."""
#
# class Car_rental_system:
#     def __init__(self,make,model,rental,availability=True):
#         self.make = make
#         self.model = model
#         self.rental = rental
#         self.availability = availability
#     def rent_car(self):
#         if self.availability:
#             self.availability = False
#             print(f"{self.model} with {self.make} has rented successfully...")
#
#         else:
#             print(f"{self.model} is not available")
#
#     def return_car(self):
#         if not self.availability:
#             self.availability = True
#             print(f"{self.model} is returned successfully.....")
#         else:
#             print(f"{self.model} is already available......")
#
#
# car = Car_rental_system("Maruti Suzuki","Swift Dzire",1000)
# car.rent_car()
# car.return_car()
