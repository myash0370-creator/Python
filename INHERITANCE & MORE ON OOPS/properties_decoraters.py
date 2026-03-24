class employee:
    a = 5
    @classmethod
    def show(cls):
        print(f"The attribute of a is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name (self , value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = employee()
e.a = 45
e.name = "Yash Mishra"
print(e.fname , e.lname)
e.show()