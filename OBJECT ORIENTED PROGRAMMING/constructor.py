class employee:          #class
    language = "py"      # This is a class attribute
    salary = 600000

    def __init__(self, name , salary , language):
        self.name = name
        self.salary = salary
        self.language= language
         
yash = employee("Yash" , 70000 , "R")
print(yash.name , yash.salary , yash.language)
        