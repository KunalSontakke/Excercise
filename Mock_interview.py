# """List"""
#
# lis1 = [1,2,3,4]
# lis2 = [5,6,7,8]
# lis3 = [9,10,11,12]
#
# out = lis1 + lis2
# print(out)
# print(lis1)
#
# """append"""
# lis1.append(lis2)
#
# print(lis1)
#
# """extend"""
# lis1.extend(lis3)
# print(lis1)
#
# str1 = "Hi my name is kunal"
# str_update = str1.upper()
#
# print(str_update)
#
#
#

"""dictionary"""
import time

from selenium.webdriver import ActionChains, Keys

# dic1 = {"name":"kunal","lastname":"sontakke"}
# dic2 = {"age":"30","company":"nitor"}
#
# dic2.update(dic1)
# print(dic2)
#
# dic3 = {**dic1,**dic2}
# print(dic3)
#
# def addition(*args):
#     sum = 0
#     for value in args:
#         sum += value
#     print(sum)
#
#
# def intro(**kwargs):
#     for key,value in kwargs.items():
#         print(key,":",value)
#
# intro(**dic1)

"""OOPS concept"""
"""Inheritance"""
"Multiple Inheritance"

# class Father:
#     def intro(self):
#         print("Hi I am father")
#
# class Mother():
#     def intro(self):
#         print("Hi I am mother")
#
# class Son(Mother,Father):
#     def intro(self):
#         print("Hi I am son")


"""Multi-level Inheritance"""
# class Father:
#     def intro(self):
#         print("Hi I am father")
#
# class Mother(Father):
#     def intro(self):
#         print("Hi I am mother")
#
# class Son(Mother,Father):
#     def intro(self):
#         Father().intro()
#         print("Hi I am son")


"""Hiarchial inheritance"""
# class A:
#     print("A")
#
# class B(A):
#     print("B")
#
# class C(A):
#     print("C")
#
# class D(A):
#     print("D")



# son = Son()
# son.intro()


#
# """Method Overloading"""
# class Person:
#     def intro(self):
#         print("Hi am Kunal")
#
#     def intro(self):
#         print("my age is 30")
#
#     def intro(self):
#         print("I live in nagpur")
#
#
# person = Person()
# print(person.intro())
#

"""Inheritance with Instance Variable"""
# class Father:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def intro(self):
#         print(f"Hi I am {self.name} and my age is {self.age}")
#
#
# class Son(Father):
#     def __init__(self,name,age,company):
#         super().__init__(name,age)
#         self.company = company
#
#     def intro(self):
#         super().intro()
#         print(f"Hi my company is {self.company}")
#
#
# son = Son('kunal',30,'Nitor')
# son.intro()


# def addition(a,b):
#     print(a+b)
#
# addition(1,2)
# addition(2,3)
# import openpyxl
#
# workbook = openpyxl.load_workbook("D:\\study\\Credence\\ETL_practical\\TEST_CASES.xlsx")

# Locate particular sheet
# sheet = workbook['Sheet1']
#
# # Read Data from sheet
# print(sheet.cell(row=1, column=1).value)
# print(sheet.cell(row=1, column=2).value)

# lis = []
# for i in range(1,100):
#     lis.append(i)
#     sheet.cell(row=1, column=1)= i
#
# print(lis)

# import json

# json_1 = "C:\Users\Kunal\PycharmProjects\Excercise\Data\abc.json")

# json_dict = json.load(json_1)

# print(type(json_dict))

