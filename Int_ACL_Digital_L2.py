str1 = "hello123python"
print(str1[::-1])

print("".join([i[::-1] if i.isalpha() else i for i in str1 ]))

out = ""
for i in str1:
    if i.isalpha():
        out = i + out

    else:
        out += i
print(out)

# ==================================
L1 = [1, 2, 3]
L2 = [1, 8, 2]
# L3 = [2, 0, 6]
L3  = []
carry = 0
for a,b in zip(L1,L2):

    total = a + b + carry
    L3.append(total % 10)
    carry = total // 10
if carry:
    L3.append(carry)

print(L3)
# =====================================================
# class Vehicle
#     1)brand
#     2)wheels
#     method print(brand & whells)
#
# class Car
#         color
#         print(brand whells color)


class Vehicle:
    def __init__(self,brand,wheels):
        self.brand = brand
        self.wheels = wheels

    def print_details(self):
        print(f"brand:{self.brand}")
        print(f"wheels:{self.wheels}")

class Truck:
    def __init__(self,loading_qty):
        self.loading_qty = loading_qty

    def print_details(self):
        print(f"loading quantity : {self.loading_qty}")

class Car(Vehicle,Truck):
    def __init__(self,brand,wheels,color,loading_qty):
        Vehicle.__init__(self,brand,wheels)
        Truck.__init__(self,loading_qty)
        self.color = color

    def print_details(self):
        Vehicle.print_details(self)
        Truck.print_details(self)
        print(f"color:{self.color}")

obj1 = Car("Hyundai",4,"red",4)
obj1.print_details()
