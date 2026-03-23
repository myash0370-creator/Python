class employee:
    a = 43

class programmer(employee):
    b = 53

class coder(programmer):
    c = 18

o = employee()
print(o.a)

o = programmer()
print(o.a , o.b)

o = coder()
print(o.a , o.b , o.c)