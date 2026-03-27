a = int(input("Enter a number : "))
b = int(input("Enter a second number : "))
if(b == 0):
    raise ZeroDivisionError ("Sorry our program is not meant to divide numbers by zero")
else:
    print(f"Thr dividion of a/b is {a/b}")