import math


class Triangle_Calculator:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area_triangle(self, base, height):
        return 0.5 * self.base * self.height


class Circle_Calculator:
    pi = math.pi

    def __init__(self, radius):
        self.radius = radius

    def area_circle(self, radius):
        return self.pi * self.radius ** 2

    def circum_area_circle(self):
        return 2 * self.pi * self.radius

    def volume_sphere(self):
        return (4 / 3) * self.pi * self.radius ** 3

    def total_surface_sphere(self):
        return 4 * self.pi * self.radius ** 2


class Square_Calculator:
    def __init__(self, side):
        self.side = side

    def area_square(self):
        return self.side ** 2

    def perimeter_square(self):
        return 4 * self.side

    def volume_cube(self):
        return self.side ** 3

    def surface_area_cube(self):
        return 6 * self.side ** 2


class Rectangle_Calculator:
    def __init__(self, side, side1):
        self.side = side
        self.side1 = side1

    def area_rectangle(self):
        return self.side * self.side1

    def perimeter_rectangle(self):
        return 2 * self.side + 2 * self.side1


class Cuboid_Calculator:

    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def volume_cuboid(self):
        return self.length * self.breadth * self.height

    def surface_area_cuboid(self):
        return (2 * self.length + 2 * self.breadth) * self.height

    def perimeter_cuboid(self):
        return 4 * (self.length * self.breadth * self.height)


class Cylinder_Calculator:
    pi = math.pi

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume_cylinder(self):
        return self.pi * self.radius ** 2 * self.height

    def surface_area_cylinder(self):
        return 2 * self.pi * self.radius * self.height


obj = Triangle_Calculator()

obj1 = Circle_Calculator()

obj2 = Square_Calculator()

obj3 = Rectangle_Calculator()

obj4 = Cuboid_Calculator()

obj5 = Cylinder_Calculator()

choice = 1
while choice != 0:
    print("1.Triangle")
    print("2.Circle")
    print("3.Square")
    print("4.Rectangle")
    print("5.Cuboid")
    print("6.Cylinder")
    print("7.Sphere")
    print("0.Exit")

    choice = int(input("Enter the Option:"))

    if choice == 1:
        print("Area of Triangle is ", obj.area_triangle())

    if choice == 2:
        Option = 1
        while Option != 0:
            print("1.Area Of Circle")
            print("2.Circumference Area Of Circle")
            print("3.Exit")

            Option = int(input("Enter the Option"))

            if Option == 1:
                print("Area of Circle", obj1.area_circle())

            elif Option == 2:
                print("Circumference Area of Circle", obj1.circum_area_circle())

            elif Option == 3:
                print("Exiting application")
            else:
                print("Invalid Option......")

    if choice == 3:
        side = int(input("Enter side"))

        Option = 1
        while Option != 0:

            print("1.Area of Sqaure")
            print("2.Perimeter of Square")
            print("0.Exit")

            Option = int(input("Enter the Option"))

            if Option == 1:
                print("Area of Square is:", obj2.area_square(side))

            elif Option == 2:
                print("Perimeter Of Square is :", obj2.perimeter_square())

            elif Option == 0:
                print("Exiting Application")

            else:
                print("Invalid Option")

    if choice == 4:

        Option = 1
        while Option != 0:

            print("1.Area Of Rectangle")
            print("2.Perimeter Of Rectangle")

            Option = int(input("Enter the Option"))

            if Option == 1:
                print("Area of Rectangle is :", obj3.area_rectangle())

            elif Option == 2:
                print("Perimeter of Rectangle is :", obj3.perimeter_rectangle())

            elif Option == 0:
                print("Exiting application")

            else:
                print("Invalid Option")

    if choice == 5:
        Option = 1
        while Option != 0:
            print("1.Volume of Cuboid")
            print("2.Surface Area of Cuboid")
            print("3.Perimeter of Cuboid")
            print("0.Exit")

            Option = int(input("Enter the Option"))

            if Option == 1:
                print("Volume of Cuboid is : ", obj4.volume_cuboid())

            elif Option == 2:
                print("Surface area of Cuboid is :", obj4.surface_area_cuboid())

            elif Option == 3:
                print("Perimeter of Cuboid is :", obj4.perimeter_cuboid())

            elif Option == 0:
                print("Exiting Application")

        else:
            print("Invalid Application")

    if choice == 6:

        Option = 1
        while Option != 0:
            print("1.Volume of Cylinder")
            print("2.Surface Area of Cylinder")
            print("0.Exit the application")

            Option = int(input("Enter the Option"))

            if Option == 1:
                print("Volume of Sphere is ", obj5.volume_cylinder())

            elif Option == 2:
                print("Surface Area Of Cylinder is ", obj5.surface_area_cylinder())

            else:
                print("invalid Option")

    if choice == 7:

        Option = 1
        while Option != 0:
            print("1.Volume of Sphere is")
            print("2.Surface Area Of Sphere is")
            print("3.Exit")

            Option = int(input("Enter the Radius"))

            if Option == 1:
                print("Volume of Sphere is :", obj1.volume_sphere())

            elif Option == 2:
                print("Surface Area of Sphere is :", obj1.total_surface_sphere())

            elif Option == 3:
                print("Exiting the Application")

            else:
                print("Invalid Option")

