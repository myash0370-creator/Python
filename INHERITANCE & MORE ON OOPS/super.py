class employee:
    def __init__(self):
       print("constructor of employee")
    a = 43

class programmer(employee):
    def __init__(self):
      print("programmer of employee")
    b = 53

class coder(programmer):
    def __init__(self):
      super().__init__()
      print("coder of employee")
    
    c = 18


o = coder()
print(o.a , o.b , o.c)