class employee:          #class
    language = "py"      # This is a class attribute
    salary = 600000

yash = employee()        #object
yash.language = "R"       # This is an instance attribute
print(yash.salary , yash.language)
# Instance attributes, take preference over class attributes during assignment & retrieval.
