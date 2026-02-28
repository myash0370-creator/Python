#Write a program to find whether a given username contains less than 10 characters or not.
username = input("Enter your username: ")
if(len(username)<10):
    print("Your username less than 10 characters")

else:
    print("Your username more than or equal to 10 characters")