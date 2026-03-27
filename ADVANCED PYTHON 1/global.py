a = 19
def func():
    global a
    a = 8
    print(a)

func()
print (a)