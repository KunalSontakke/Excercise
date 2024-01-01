class Dad:
    def __init__(self, PIN):
        self.PIN = PIN

    def hobby(self):
        print("Watching TV news")

    def bike(self):
        print("Hero Passion")

    def mobile(self):
        print("Nokia 3310")

    @staticmethod
    def account_balance(self):
        print("balance is 250000")

    def withdraw_money(self):
        self.PIN = input("Enter PIN")
        if self.PIN == "1234":
            print("You have 2,50,000 into your account")
        else:
            print("You have entered Wrong PIN.Please try again")

    @property
    def Account(self):
        return self.PIN


class Mom(Dad):
    def __init__(self):
        super().__init__()
        print("Mom is initiated")

    def hobby(self):
        print("cooking")

    def mobile(self):
        print("Redmi")

    def account_balance(self):
        print("balance is 10,000")


class Son(Dad):
    def hobby(self):
        print("Playing Games")
        super().hobby()

    def bike(self):
        print("KTM Duke")

    def mobile(self):
        print("iPhone 12 pro max")

    def mobile(self):
        print("Realme")


class grandson(Son):
    def __init__(self):
        super().__init__()
        print("grandon is initiated")

    def hobby(self):
        print("reading comics")


obj3 = Son("1234")
obj3.hobby()

obj3.withdraw_money()
obj3.Account()

# ====================================================================================================================
"""Can we create baseclass without object"""


class empty:
    pass


person = empty()
person.name = "kunal"
person.age = "28"
person.gender = "male"

print(person.name)
print(person.age)
print(person.gender)


class person:
    def __init__(self):
        print("I am initiated")

    def print_details(self):
        print("my name is kunal.I am 30 years old.I am male")


person()
person.print_details


class Dad:
    def __init__(self):
        print("Dad is Initiated")

    def hobby(self):
        print("Reading NewsPaper")

    def hobby(self):
        print("Watching TV")

    def hobby(self):
        print("Jogging")


class Papa:
    def bike(self):
        print("Hero Passion Plus")


class Beta(Papa):
    def bike(self):
        super().bike()  # in method riding,childclass overrides baseclass method.but super class inherites method
        # from baseclass
        print("KTM Duke 250")


obj = Papa()
obj1 = Beta()
obj1.bike()


class baseclass:
    def __init__(self):
        self._name = "kunal"
        self.__acct_no = 1234

    def name(self):
        print("my name is ", self._name)

    def acct_no(self):
        print("my account no is", self._acct_no)


object = baseclass()
object.name()


# object.acct_no()
#
# class childClass(baseclass):
#     def name(self):
#         print(self._name)
#     def acct_no(self):
#         print(self.__acct_no)
#
# obj4 = childClass()
# obj4.name()
# obj4.acct_no()


class one:
    def __init__(self):
        print("id of self is", id(self))

    def print(self):
        print("I'll be printed")


obj5 = one()
print("id of object5 is", id(obj5))
obj6 = one()
print("id of object6 is", id(obj6))


class father:
    def __init__(self):
        print("father class is initiated")

    def account_statement(self):
        print("you have 1,00,000 Rs balance in your account")

    def property_statement(self):
        print("you have pension 1 CR policy")


class Son(father):
    def __init__(self):
        print("Son class is initiated")

    def account_statement(self):
        super().account_statement()
        print("you have 25,000 Rs in your account")

    def property_statement(self):
        super(Son, self).property_statement()
        print("you have 25 lacs policy and insurance")


son = Son()
son.account_statement()
son.property_statement()


class Camera:
    def __init__(self, pixels):
        self.pixels = pixels

    def click_picture(self):
        print("clicks HD Quality images")

    def record_video(self):
        print("records HD Videos")


class Mobile(Camera):
    def __init__(self, pixels, mobile_no):
        self.mobile_no = mobile_no
        super.__init__(pixels)

    def call(self):
        print("calling", self.mobile_no)

    def message(self):
        print("sending message", self.mobile_no)

    def click_picture(self):
        super().click_picture()
        print("clicks UHD Quality Image", self.pixels)


mobile = Mobile('9765383888')
mobile.call()
mobile.record_video()
mobile.click_picture()
