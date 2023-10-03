"""
What are Generators in Python?

- Generators are basically functions that return traversable objects or items.
- These functions do not produce all the items at once, rather they produce them one at a time and only when required.
- Whenever the for statement is included to iterate over a set of items, a generator function is run.
- Generators have a number of advantages as well.

"""


def fun_generator():
    yield "Hello world!!"
    yield "Geeksforgeeks"


obj = fun_generator()

print(type(obj))
print(next(obj))
print(next(obj))


def inf_sequence():
    num = 0
    while num != 10:
        yield num
        num += 1

for i in inf_sequence():
    print(i, end="\n")


# ======================================================================================================================
def fun(n):
    for i in range(n):
        yield i

f = fun(10)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())



"""
Advantages of using Generators

    Without Generators in Python, producing iterables is extremely difficult and lengthy.
    Generators easy to implement as they automatically implement __iter__(), __next__(), and StopIteration which otherwise, 
    need to be explicitly specified.
    Memory is saved as the items are produced when required, unlike normal Python functions.
    This fact becomes very important when you need to create a huge number of iterators. 
    This is also considered as the biggest advantage of generators.
    Can be used to produce an infinite number of items.
    They can also be used to pipeline a number of operations
"""

lis = ["apple","banana","mango","grapes","orange"]
print(lis)
lis_iter = iter(lis)
print(lis_iter)
print(next(lis_iter))
print(next(lis_iter))
print(next(lis_iter))
print(next(lis_iter))
print(next(lis_iter))




