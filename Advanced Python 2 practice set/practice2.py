#  Write a program to input name, marks and phone number of a student and format it using the format function like below:
name = input("Enter a name: ")
marks = int(input("Enter a marks: "))
phone = int(input("Enter a phobne number: "))
s = "The name of the student is {}, his marks are {} and phone number is {}".format(name, marks, phone)
print(s)