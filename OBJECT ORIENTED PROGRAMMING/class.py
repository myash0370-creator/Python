class employee:          #class
    language = "py"      # This is a class attribute
    salary = 600000

yash = employee()        #object
yash.name = "Yash"       # This is an instance attribute
print(yash.name , yash.salary , yash.language)

shikha = employee()
shikha.name = "Shikha"
print(shikha.name , shikha.language , shikha.salary)