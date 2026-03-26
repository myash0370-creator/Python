#  THE PERFECT GUESS 

import random 
n = random.randint(1 , 100)
a = -1
guesses = 1
while(a != n):
    a = int(input("Enter the Number: "))
    if(a>n):
        print("Give Lower Number Please")
        guesses += 1

    elif(a<n):
        print("Give Higher Number Please")
        guesses += 1

print(f"You have guessed the number {n} correctly in {guesses} attempts")