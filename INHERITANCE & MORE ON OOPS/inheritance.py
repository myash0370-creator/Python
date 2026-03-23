class Employee:
    company = "Microsoft,"
    salary = 60000
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "ITC Infotech"
    language = "python"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

print(a.company, a.salary, b.company , b.language)