def add_num(*args):
    sum = args[0] + args[1] + args[2] + args[3] + args[4]
    print(sum)


add_num(1, 2, 3, 4, 5)


# =========================================================================================================

def print_marks(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


marklist = {"kunal": 56, "shubham": 45, "rajat": 57, "suraj": 98}
print_marks(**marklist)


# =========================================================================================================


def multiplication(*args):
    mul = 1
    for num in args:
        mul = mul * num
    return mul


nos = (1, 2, 3, 4)

print(multiplication(*nos))
print(multiplication(2, 4, 5, 6, 7, 8))


# ======================================================================================================================

def dictionary(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


dict = {"kunal": "nagpur", "shubham": "pune", "sagar": "pune", "rajat": "mumbai"}

dictionary(**dict)


def method(*args, **kwargs):
    print(args)
    for key, value in kwargs.items():
        print(key, ":", value)


a = 10, 23, 34
dict = {'name': 'kunal',
        "surname": 'sontakke',
        "city": "nagpur"
        }

method(a, **dict)


# ===========================================================================================

def xyz(x,y,z):
    print(x,y,z)


dic = {"x":1,"y":2,"z":3}

xyz(**dic)