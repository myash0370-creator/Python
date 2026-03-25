'''Override the __len__() method on vector of problem 5 to display the dimension of the vecto'''
class Vector:
    def __init__(self, l): 
        self.l = l

    
    
    def __len__(self):
        return len(self.l)

# Test the implementation
v1 = Vector([14, 20, 35 , 89]) 
print(len(v1))