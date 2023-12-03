from copy import copy


class sample:
    pass


a = sample()
a.lst = [1, 2, 3]
a.str = "hacker"
b = copy(a)
a.lst.append('earth')
a.str = 'Python'
print("b =",b.str)


# ========================================================

def sample(args):
    args.insert(args.index(args[-1]), 2)
    args.pop(0)


numbers = replica = [3, 4, 5, 6]
sample(replica)
print(replica)


# =======================================================================================================
iter_obj = iter([3, 4, 5])
print(next(iter_obj))
print(next(iter_obj))


def multipliers():
    return [lambda x: i * x for i in range(4)]


print([m(2) for m in multipliers()])


# =======================================================================================================

def Compute(prog):
    def ComputeInside(*args, **kwargs):
        return prog(*args, **kwargs) + 1

    return ComputeInside


@Compute
def result(n):
    return n - 4


print(result(5))


# =====================================================================================================

def ret_numbers(n):
    for i in n:
        yield i ** 2


cubes = ret_numbers([2, 6, 1, 9, 5])
print(list(sorted(cubes)))

# ====================================================================================================

L1 = [2, 's', 4]
L2 = ['m', '1', 10]
print(L1 + L2 * 2 ** 2)


# ====================================================================================================

def extendList(val, list=[]):
    list.append(val)
    return list


list1 = extendList(10)
list2 = extendList(420, [])
list3 = extendList('coriolis')

print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)




