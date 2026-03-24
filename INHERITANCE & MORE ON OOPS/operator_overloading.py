class number:
    def __init__(self , n):
        self.n = n

    def __add__(self , num):
        return self.n + num.n
    

n = number(10)
m = number(18)

print(n+m)

# more methos
# p1.__add__
# p1.__sub__
# p1.__mul__
# p1.__truediv__
# p1.__floordiv__