# PROJECT 1: SNAKE, WATER, GUN GAME:
import random 
computer = random.choice([-1 , 1 , 0])
user_input = input("Enter your choice: ")
user_dict = {"s": 1, "w":-1, "g":0}
reverse_dict = {1:"Snake", -1:"Water", 0:"Gun"}

user = user_dict[user_input]

print(f"You chose {reverse_dict[user]}\nComputer chose {reverse_dict[computer]}")

if(computer == user):
    print("Its a Draw")

else:
       ''' if(computer == -1 or user == 1):
        print("Congratulations\nYou win!")
    
    elif(computer == -1 or user == 0):
        print("You Lose!")

    elif(computer == 1 or user == -1):
        print("You Lose!")

    elif(computer == 1 or user == 0):
        print("Congratulations\nYou win!")

    elif(computer == 0 or user ==-1):
        print("Congratulations\nYou win!")

    elif(computer == 0 or user == 1):
        print("You Lose!")
    
    else:
        print("Something went wrong")

         The below logic is written on the basis of the value of computer - you
        '''
if((computer - user == -1) or (computer - user ==2)):
        print("Ypu lose!")

else:
        print("You win!")