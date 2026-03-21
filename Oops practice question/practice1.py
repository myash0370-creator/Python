# Create a class “Programmer” for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self , name , salary , pin):
        self.name = name 
        self.salary = salary
        self.pin = pin

p = Programmer("Yash" , 80000 , 2578)
print(p.name , p.salary , p.pin , p.company)

p2 = Programmer("Vivek" , 750000 , 2345)
print(p2.name , p2.salary , p2.pin , p2.company)
