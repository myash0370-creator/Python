class employee:
    company = "Microsoft"
    name = "Yash Mishra"
    def show(self):
        print(f"The company is {self.company} and the employee name is {self.name}")

class coder:
    language = "Python"
    def printLanguage(self):
        print(f"The language supported by employee is {self.language} ")

class programmer(employee , coder):
    department = "Microsoft"
    def showLanguage(self):
        print(f"The company is {self.company} and prefered language is {self.language} and department is {self.department}")

a = employee()
b = programmer() 

b.show()
b.printLanguage()
b.showLanguage()