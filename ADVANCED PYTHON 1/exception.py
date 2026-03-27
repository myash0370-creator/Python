try :
    a = int(input("Enter a number:"))

except ValueError as v:
    print("Hello")
    print(v)

except Exception as e:
    print(e)

print("Thankyou")