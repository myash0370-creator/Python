# Write a program to filter a list of numbers which are divisible by 5.
def divisible5(n):
    if(n%5 == 0):
        return True
    return False
a = [ 1 , 44 , 4456 , 56 , 78 ,99, 55 , 354, 5 , 234235 , 0]
f = list(filter(divisible5 , a))
print(a)