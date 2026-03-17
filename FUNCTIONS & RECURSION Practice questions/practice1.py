# Write a program using functions to find greatest of three numbers.
def greatest(a , b , c):
    if(a>b or a>c):
        return a
    elif(b>a or b>c):
        return b
    elif(c>a or c>b):
        return c
    
a = 8
b = 18
c = 10
print(greatest (a , b , c))