class First:
    def a(self):
        print("Inside method a")

    def b(self):
        print("Inside method b")

    def c(self):
        print("Inside method c")


class Second(First):
    # Overridden method
    def c(self):
        print("Inside new method c")


if __name__ == "__main__":
    obj = Second()

    # Parent reference pointing to child object
    r = obj

    r.a()
    r.b()
    r.c()