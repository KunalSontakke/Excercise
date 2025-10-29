class agilion:
    def __init__(self):
        print("this is agilion file")

    def set_name(self):
        print("my name is kunal")


def show_module_name():
    print("module name is",__name__)


if __name__ == "main":
    show_module_name()


class kunal_prep:
    def __init__(self):
        print("my name is kunal")

    def show_city(self):
        print("my city is nagpur")


kunal_prep().show_city()
