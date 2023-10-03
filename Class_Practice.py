import math


class Student_info:
    def __init__(self, student_id, student_name, class_name):
        self.student_id = student_id
        self.student_name = student_name
        self.class_name = class_name


student = Student_info(1001, "Kunal", 10)

print(student.__dict__)
print(student.__getattribute__)

#
# # 1.Create a Circle class and initialize it with radius.
# # Make two methods getArea and getCircumference inside this class.
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def getArea(self):
#         return 3.14 * self.radius ** 2
#
#     def getCircumference(self):
#         return 2 * 3.14 * self.radius
#
#
# radius = int(input("enter radius : "))
#
# obj = Circle(radius)
#
# print("Area of Circle is", obj.getArea())
# print("Circumference of Circle is", round(obj.getCircumference()))
#
#
# # =======================================================================================
#
# # Create a Temperature class. Make two methods :
# # 1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
# # 2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
#
# class Temperature:
#     def convertFarenheit(self, celcius):
#         print("Temperature in Celcius is", (celcius * 9 / 5) + 32)
#
#     def convertCelius(self, faranheit):
#         print("Temperature in Faranheit is", (faranheit - 32) * 5 / 9)
#
#
# obj1 = Temperature()
# obj1.convertFarenheit(45)
# obj1.convertCelius(113)
#
#
# # ================================================================================================
# # Create a Student class and initialize it with name and roll number. Make methods to :
# # 1. Display - It should display all information of the student.
# # 2. setAge - It should assign age to student
# # 3. setMarks - It should assign marks to the student.
#
# class Student:
#     def __init__(self, name, roll_number):
#         self.name = name
#         self.roll_number = roll_number
#
#     def display(self):
#         print(self.name)
#         print(self.roll_number)
#
#     def setAge(self, age):
#         self.age = age
#
#     def setMarks(self, marks):
#         self.marks = marks
#
#
# obj = Student("Kunal", 52)
# obj.setAge(45)
#
#
# # =============================================================================================
#
# # Create a Time class and initialize it with hours and minutes.
# # 1. Make a method addTime which should take two time object and add them.
# # E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# # 2. Make a method displayTime which should print the time.
# # 3. Make a method DisplayMinute which should display the total minutes in the Time.
# # E.g.- (1 hr 2 min) should display 62 minute.
#
# class TimeClass:
#     def __init__(self, hours, minutes):
#         self.hours = hours
#         self.minutes = minutes
#
#     def addTime(self, t1, t2):
#         t3 = TimeClass(0, 0)
#         if t1.minutes + t2.minutes > 60:
#             t3.hours = (t1.hours + t2.hours) / 60
#         t3.hours = t3.hours + t1.hours + t2.hours
#         t3.minutes = (t1.minutes + t2.minutes) - (((t1.minutes + t2.minutes) / 60) * 60)
#         return t3
#
#     def displayTime(self):
#         print("current time is", self.hours, ".", self.minutes)
#
#     def displayMinute(self):
#         print("Total minutes are", (self.hours * 60) + self.minutes)
#
#
# obj2 = TimeClass(2, 45)
# a = TimeClass(3, 57)
# b = TimeClass(2, 50)
#
#
# # OOP Exercise 1: Create a Class with instance attributes
#
# # Write a Python program to create a Vehicle class with max_speed and mileage instance attributes
#
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#
# model_X = Vehicle(140, 15)
#
# print(model_X.max_speed)
# print(model_X.mileage)
#
#
# # ==================================================================================================
#
# # Exercise 2: Create a Vehicle class without any variables and methods
# class vehicle:
#     pass
#
#
# model_A = vehicle
#
#
# # =================================================================================================
# # OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# class Vehicle:
#     color = "White"
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_Capacity(self, capacity):
#         return f"Seating capacity of {bus.name} is {capacity} passengers"
#
#     def fare(self):
#         return self.seating_Capacity(capacity=50) * 100
#
#
# class Bus(Vehicle):
#     def seating_Capacity(self, capacity=50):
#         return super().seating_Capacity(capacity=50)
#
#
# bus = Bus("Eicher 2075H", 100, 6)
# print("Vehicle name:", bus.name, "\nmaximum speed : ", bus.max_speed, "\nmileage :", bus.mileage)
# print(bus.seating_Capacity())
#
#
# # ================================================================================================
# # OOP Exercise 5: Define a property that must have the same value for every class instance (object)
# class Bus(Vehicle):
#     pass
#
#
# class Car(Vehicle):
#     pass
#
#
# school_bus = Bus("Eicher", 80, 12)
# print(f"{bus.name} have maximum speed {bus.max_speed} and mileage is {bus.mileage} kms")
#
# car = Car("Volvo XC40", 250, 12)
# print(f"{car.name} have top speed {car.max_speed} and mileage is {car.mileage} kms")
#
#
# # ==================================================================================================
# # Create a Bus child class that inherits from the Vehicle class.
# # The default fare charge of any vehicle is seating capacity * 100.
# # If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge.
# # So total fare for bus instance will become the final amount = total fare + 10% of the total fare.
#
# class Bus(Vehicle):
#     def fare(self):
#         amount = super().fare()
#         amount = float(amount)  # Convert amount to a numerical type if it's a string
#         amount += amount * 10 / 100
#         return amount
#
#
# bus = Bus("Eicher 2075H", 100, 12)
# print(type(bus))
#
# # ====================================================================================================
# """Exercise 1
#     1) Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments.
#     Make sure to set these appropriately in the body of the __init__()method.
#     2) Create a variable named number_of_sides and set it equal to 3.
#     3) Create a method named check_angles. The sum of a triangle's three angles is
#     It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
#     4) Create a variable named my_triangle and set it equal to a new instance of your Triangle class.
#     Pass it three angles that sum to 180 (e.g. 90, 30, 60).
#     5) Print out my_triangle.number_of_sides and print out my_triangle.check_angles()"""
#
#
# class Triangle:
#     def __init__(self, angle1, angle2, angle3):
#         self.angle1 = angle1
#         self.angle2 = angle2
#         self.angle3 = angle3
#
#     number_of_sides = 3
#
#     def check_angles(self):
#         if self.angle1 + self.angle2 + self.angle3 == 180:
#             return True
#         else:
#             return False
#
#
# my_triangle = Triangle(90, 30, 60)
# print(my_triangle.number_of_sides)
# print(my_triangle.check_angles())

# ================================================================================
"""
Exercise 2

Define a class called Songs, it will show the lyrics of a song.
Its __init__() method should have two arguments:self anf lyrics.lyrics is a list.
Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.
Define a variable:

happy_birthday = Song(["May god bless you, ",
                   "Have a sunshine on you,",
                   "Happy Birthday to you !"])

Call the sing_me_songmehod on this variable
"""
#
#
# class Songs:
#     def __init__(self, lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         print(self.lyrics)
#
#
# lyrics = ["May god bless you, ",
#           "Have a sunshine on you,",
#           "Happy Birthday to you !"]
# happy_birthday = Songs(lyrics)
# happy_birthday.sing_me_a_song()
#
# # ===================================================================================
"""
Exercise 3

1) Define a class called Lunch.Its __init__() method should have two arguments:self and menu.Where menu is a string.
2) Add a method called menu_price.It will involve a if statement:
3) if "menu 1" print "Your choice:", menu, "Price 12.00", if "menu 2" print "Your choice:", menu, "Price 13.40", else print "Error in menu".
4) To check if it works define: Paul=Lunch("menu 1") and call Paul.menu_price().
"""
#
#
# class Lunch:
#     def __init__(self, menu):
#         self.menu = menu
#
#     def menu_price(self):
#         if self.menu == "menu 1":
#             print("Your choice :", 1, "Price 12.00")
#         elif self.menu == "menu 2":
#             print("Your choice :", 2, "Price 13.40")
#         else:
#             print("Error is menu")
#
#
# Paul = Lunch("menu 1")
# Paul.menu_price()
#
# # ==========================================================================================
# """
# Exercise 4
#
# 1) Define a Point3D class that inherits from object Inside the Point3D class,
# 2) define an __init__() function that accepts self, x, y, and z,
# 3) and assigns these numbers to the member variables self.x,self.y,self.z. Define a __repr__() method that returns "(%d, %d, %d)" % (self.x, self.y, self.z).
# 4) This tells Python to represent this object in the following format: (x, y, z).
# 5) Outside the class definition, create a variable named my_point containing a new instance of Point3D with x=1, y=2, and z=3.
# Finally, print my_point.
# """
#
#
# class Point3D:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def __repr__(self):
#         return "(%d, %d, %d)" % (self.x, self.y, self.z)
#
#
# my_point = Point3D(1, 2, 3)
# print(my_point)
#
# ======================================================================================================================
# """
# Exercise 41. Rectangle class: ||  Solution
#
#  Write a Rectangle class in Python language, allowing you to build a rectangle with length and width attributes.
#  Create a Perimeter() method to calculate the perimeter of the rectangle and a Area() method to
#  calculate the area of the rectangle.
#  Create a method display() that display the length, width, perimeter
#  and area of an object created using an instantiation on rectangle class.
#  Create a Parallelepipede child class inheriting from the Rectangle class and with a height attribute
#  and another Volume() method to calculate the volume of the Parallelepiped
# """
#
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def perimeter(self):
#         return 2 * (self.length + self.width)
#
#     def area(self):
#         return self.length * self.width
#
#     def display(self):
#         print("length is", self.length)
#         print("width is", self.width)
#         print("perimeter is", self.perimeter())
#         print("area is", self.area())
#
#
# class Paralleled(Rectangle):
#     def __init__(self, length, width, height):
#         Rectangle.__init__(self, length, width)
#         self.height = height
#
#     def volume(self):
#         return self.length * self.width * self.height
#
#
# my_rectangle = Rectangle(4, 5)
# my_rectangle.display()
#
# my_parallelpipe = Paralleled(7, 5, 2)
# print("volume of paralleled is", my_parallelpipe.volume())
#
# # ==========================================================================================================
# """
# instance method,class method and Static method
# Instance method performs a set of actions on the data/value provided by the instance variables.
# If we use instance variables inside a method, such methods are called instance methods.
#
#
# Class method is method that is called on the class itself, not on a specific object instance.
# Therefore, it belongs to a class level, and all class instances share a class method.
#
#
# Static method is a general utility method that performs a task in isolation.
# This method doesn’t have access to the instance and class variable
# """
#
#
# class Student:
#     school_name = "N.I.T. College of engineering"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_details(self):
#         print("Student name : ", self.name)
#         print("Student age : ", self.age)
#         print("College Name: ", self.school_name)
#
#     @classmethod
#     # access class variable
#     def change_school_name(cls, name):
#         cls.school_name = name
#
#     @staticmethod
#     # can't access instance or class attributes
#     def find_notes(subject_name):
#         return ['chapter 1', 'chapter 2', 'chapter 3']
#
#
# student = Student('Kunal', 12)
# student.show_details()
#
# # Call Class method using class name
# Student.change_school_name("G.N.I.T. College of Engineering")
#
# # Call Class Method using Object variable
# student.change_school_name("R.C.O.E.M. College of Engineering")
#
# # Call Static Method using class name
# print(Student.find_notes("Engineering Maths"))
#
# # Call Static Method Using Object Name
# print(student.find_notes("Electronics Mechanics"))
#
#
# # ===============================================================
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         return (f"{self.name} says hello")
#
#
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#
#
# dog = Dog("Charlie", "Rottweiler")
# print(dog.breed)


# =========================================================================================================
# Write a Python program to create a class representing a shopping cart.
# Include methods for adding and removing items, and calculating the total price.
#
# class shopping_cart:
#     def __init__(self):
#         self.items = []
#
#     def adding_items(self,item_name,quantity):
#         item = (item_name,quantity)
#         self.items.append(item)
#
#     def remove_items(self,item_name):
#         for item in self.items:
#             if item[0] == item_name:
#                 self.items.remove(item)
#
#     def Calculate_price(self):
#         total = 0
#         for item in self.items:
#             total = total +item[1]
#         return total
#
# cart = shopping_cart()
#
# cart.adding_items("apple",100)
# cart.adding_items("orange",200)
# cart.adding_items("papaya",400)
#
# print("current items in cart are")
# for item in cart.items:
#     print(item[0],"-",item[1])
#
#
# total_quality = cart.Calculate_price()
# print("Total Quantity ",total_quality)
#
# cart.remove_items("orange")
# print(cart.items)

# ====================================================================================================
# Write a Python program to create a class representing a bank.
# Include methods for managing customer accounts and transactions

class Bank:
    def __init__(self):
        self.customer = {}

    def create_account(self,account_number,init_balance=0):
        if account_number in self.customer:
            print("customer already exists")
        else:
            self.customer[account_number] = init_balance
            print("customer successfully added")

    def deposit_money(self,account_number,amount):
        if account_number in self.customer:
            self.customer[account_number] += amount

        else:
            print("customer doesn't exist")


    def withdrawl_money(self,account_number,amount):
        if account_number in self.customer:
            if self.customer[account_number] >=amount:
                self.customer[account_number] -= amount
                print("withdrawal successful")
            else:
                print("Insufficient funds")

        else:
            print("customer doesn't exist")

    def check_balance(self,account_number):
        if account_number in self.customer:
            balance = self.customer[account_number]

            print("Account balance is",balance)

        else:
            print("customer doesn't exist")


bank = Bank()
acct_no = 123456
amt = 1000

print("Account Number is :",acct_no,"\ndeposit amount is :",amt)

bank.create_account(acct_no,amt)

acct_no = 123101
amt = 2000

print("Account Number is :",acct_no,"\ndeposit amount is :",amt)

bank.deposit_money(acct_no,amt)

acct_no = 123101
withd_amt = 500

print("Withdraw amount in Rs.is",withd_amt,"from account",acct_no)
bank.withdrawl_money(acct_no,withd_amt)

bank.check_balance(123456)

class Cylinder:
    def __init__(self,radius,height,slant_height):
        self.radius = radius
        self.height = height
        self.slant_height = slant_height

    def volume(self):
        return 1/3 * math.pi * self.radius ** 2 * self.height

    def total_surface_area(self):
        return math.pi * self.radius * self.slant_height + math.pi * self.radius ** 2


cylinder = Cylinder(4,5,6)
print(cylinder.volume())
print(cylinder.total_surface_area())

