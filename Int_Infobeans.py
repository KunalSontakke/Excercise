
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

# print("square of numver is",print_num())

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