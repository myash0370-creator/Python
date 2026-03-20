class employee:          #class
    language = "py"      # This is a class attribute
    salary = 600000
    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")
yash = employee()        #object
yash.language = "R"       # This is an instance attribute

yash.getinfo()
yash.greet()