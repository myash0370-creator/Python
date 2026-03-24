class employee:
    a = 5
    @classmethod
    def show(cls):
        print(f"The attribute of a is {cls.a}")

e = employee()
e.a = 45
e.show()