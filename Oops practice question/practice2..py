# Write a class “Calculator” capable of finding square, cube and square root of a number.
class Calculator:
    def __init__(self , n):
        self.n = n

    def sqaure(self):
        print(f"The sqaure is : { self.n * self.n}")

    def cube(self):
        print(f"The cube is : { self.n ** 1/2}")

    def sqaureroot(self):
        print(f"The sqaureroot is : { self.n * self.n * self.n}")


a = Calculator(5)
a.sqaure()
a.sqaureroot()
a.cube()
