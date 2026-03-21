# Add a static method in problem 2, to greet the user with hello.
class Calculator:
    def __init__(self , n):
        self.n = n

    def sqaure(self):
        print(f"The sqaure is : { self.n * self.n}")

    def cube(self):
        print(f"The cube is : { self.n ** 1/2}")

    def sqaureroot(self):
        print(f"The sqaureroot is : { self.n * self.n * self.n}")

    @staticmethod
    def hello():
        print("Hello user!")


a = Calculator(5)
a.hello()
a.sqaure()
a.sqaureroot()
a.cube()