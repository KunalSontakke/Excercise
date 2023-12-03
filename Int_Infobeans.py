"""How memory is managed in Python ?

- Memory management in Python is handled by the Python Memory Manager.
The memory allocated by the manager is in form of a private heap space dedicated to Python.
All Python objects are stored in this heap and being private, it is inaccessible to the programmer.
for ex. x = 5
in this statement, "x" is reference and "10" is an object(since,Python is an Object-Oriented Programming language).
So, "x will be moved to "Stack Memory" and "10" is stored to "Private Heap Space".this private space is inaccessible to programmer.
whenever object has no reference/has no use then it is stored in "Garbage Collector".this all mechanism is managed by "Python Memory manager

"""
# class Dad:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def salary(self):
#         print("salary od Dad is",self.x)

#     def saving(self):
#         print("saving of Dad is",self.y)


# class son(Dad):
#     def __init__(self,x,z):
#         self.z = z
#         super().__init__self

#     def salary(self):
#         print("salary of Son is",self.x==self.z+self.x)

# Son = son(10000)
# Son.salary()


# def sqr_deco(func):
#     def wrapper():
#         x = func()
#         return x ** 2
#     return wrapper


# @sqr_deco
# def print_num():
#     return 10

# print("square of number is",print_num())

l = [1, 1, 2, 2, 9, 3, 4, 5, 6, 7, 8, 4, 3, 2, 6, 8]

freq = {}
for i in l:
    if i not in freq:
        freq[i] = 1
    else:
        freq[i] += 1

print(freq)

sort_dic = dict(sorted(freq.items(), key=lambda x: x[1]))

print(sort_dic)
