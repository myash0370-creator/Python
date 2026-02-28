a = int(input("Enter your age: "))

#if statement no. = 1
if(a%2 == 0 ):
    print("a is even")

#if statement no. = 2
if(a>=18):
    print("You are Eligible to join club")

elif(a==0):
    print("You are entered 0 this unvalid age")

elif(a<0):
    print("You are entered Negative age this is unvalid")

else:
     print("You are not Eligible to join club")

print("Thank You!")